# Hist92r Parsing Script

import os.path

# main() definition--------------------------------------------------------
def main():
    # For every file in our folder
    for num in range(1, 100):
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
                if word == "Overseas":
                    valid = True
                article.append(word)
                alen += 1
                
            # Output resulting article(s)
            ostr = "output/" + str(num) + ".txt"
            fo = open(ostr, "w")
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
