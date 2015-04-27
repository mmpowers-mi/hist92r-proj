# Hist92r Parsing Script

# main() definition--------------------------------------------------------
def main():
    # Read in a file to parse
    fi = open("input/125.txt", "r")
    contents = fi.read()
    fi.close()
    words = contents.split()
    articles = []
    article = []
    alen = 0
    valid = False

    # Split into articles
    for word in words:
        if alen > 10 and word.isupper() and len(word) > 2 and valid:
            alen = 0
            articles.append(article)
            article = []
            valid = False
        if word == "Overseas":
            valid = True
        article.append(word)
        alen += 1
            
    # Output resulting article(s)
    fo = open("output/125.txt", "w")
    for a in articles:
        for w in a:
            fo.write(w)
            fo.write(" ")
        fo.write("\n\n")
        print a
        print
        print
    
    fo.close()

# Run program-----------------------------------------------------------
if __name__ == "__main__":
    main()
