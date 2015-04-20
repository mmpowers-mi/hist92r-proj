# Hist92r Parsing Script

# main() definition--------------------------------------------------------
def main():
    # Read in a file to parse
    f = open("input/125.txt", "r")
    contents = f.read()
    words = contents.split()
    articles = []
    article = []
    alen = 0

    # Split into articles
    for word in words:
        if alen > 10 and word.isupper() and len(word) > 2:
            alen = 0
            articles.append(article)
            article = []
        article.append(word)
        alen += 1
            

    print articles[9]

    # Output resulting file

# Run program-----------------------------------------------------------
if __name__ == "__main__":
    main()
