# Hist92r Parsing Script
# Created by Marcus Powers

import os.path

# main() definition--------------------------------------------------------
def main():
    # Setup our diagnostic dict to determine dist. of num. articles per page
    dist = {}
    # For every file in our folder
    for num in range(1, 5300):
        # Read in a file to parse
        instr = "input/" + str(num) + ".txt"
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
                if alen > 10 and word.isupper() and len(word) > 2:
                    alen = 0
                    if valid:
                        articles.append(article)
                    article = []
                    valid = False
                if levenshtein(word.lower(),"Overseas".lower()) < 3:
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
                #print a
                #print
                #print
            # Add to our diagnostic dict
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
    print
    for key, value in dist.iteritems():
        print key, "articles:", value

# Levenshtein edit distance function definition 
# Borrowed with permission from:
# http://hetland.org/coding/python/levenshtein.py ----------------------
def levenshtein(a,b):
    "Calculates the Levenshtein distance between a and b."
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
        
# Run program-----------------------------------------------------------
if __name__ == "__main__":
    main()
