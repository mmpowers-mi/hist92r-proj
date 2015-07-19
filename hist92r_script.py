# Hist92r Parsing Script
# Created by Marcus Powers, April 2015

import os.path
import sys

# main() definition--------------------------------------------------------
def main():
    # Constants
    MIN_FILENUM = 1           # First file number to check
    MAX_FILENUM = 5300        # Last file number to check
    MIN_ARTLEN = 40           # Minimum length of an article before starting a new one
    MIN_CAPSLEN = 2           # Minimum number of capital letters in a word to be considered a headline
    MAX_DIFFLEN = 4           # Maximum difference in word lengths to be compared to edit distance
    MAX_EDITDIST = 3          # Maximum edit distance between words to be considered a misspelling
    KEYWORD = "overseas"      # Keyword we're looking for

    # Diagnostics/Stats
    dist = {}                 # dict to determine dist. of num. articles per page
    failures = []             # List of all failed pages (no match found)

    # Determine which files we should parse
    # NOTE ON USAGE: run without args, runs range(1,...,MAX_FILENUM)
    # run with single num for specific file (eg, python hist92r_script.py 2322)
    files = []
    if len(sys.argv) == 2:
        files.append(str(sys.argv[1]))
    else:
        files = range(MIN_FILENUM, MAX_FILENUM)

    # For every file in our folder
    for num in files:
        # Read in a file to parse
        instr = "input/" + str(num) + ".txt"
        # Make sure the file exists
        if os.path.isfile(instr):
            fi = open(instr, "r")
            contents = fi.read()
            fi.close()
            words = contents.split()
            articles = []
            article = []
            alen = 0
            valid = False

            # Split into articles
            for word in words:
                if alen > MIN_ARTLEN and word.isupper() and numLetters(word) > MIN_CAPSLEN:
                    alen = 0
                    if valid:
                        articles.append(article)
                    article = []
                    valid = False
                if abs(len(word) - len(KEYWORD)) < MAX_DIFFLEN and levenshtein(word.lower(), KEYWORD) < MAX_EDITDIST:
                    valid = True
                article.append(word)
                alen += 1
            # Don't forget to check the last one:
            if valid:
                articles.append(article)

            # Output resulting article(s)
            ostr = "output/" + str(num) + ".txt"
            fo = open(ostr, "w")
            for a in articles:
                for w in a:
                    fo.write(w)
                    fo.write(" ")
                fo.write("\n\n")
            if not len(articles):
                failures.append(num)
                #print a
                #print
                #print

            # Add to our diagnostic dict and print info
            na = len(articles)
            if na in dist:
                dist[na] = dist[na] + 1
            else:
                dist[na] = 1
            print "Page", str(num), "parsed:", na, "articles found"
            fo.close()

    # Print final distribution
    print
    print " Distribution Results"
    print "-----------------------------"
    for key, value in dist.iteritems():
        print key, "articles:", value
    print "-----------------------------"
    print
    print "Failures:"
    print "----------"
    for fail in failures:
        print "Page", fail
    print


# Levenshtein edit distance function definition 
# Borrowed with permission from:
# http://hetland.org/coding/python/levenshtein.py ----------------------
def levenshtein(a,b):
    # Calculates the Levenshtein distance between a and b.
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n + 1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1,n+1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]


# numLetters definition
# Takes a string and returns the number of letters----------------------
def numLetters(w):
    num = 0
    for c in w:
        if c.isalpha():
            num += 1
    return num
        
# Run program-----------------------------------------------------------
if __name__ == "__main__":
    main()
