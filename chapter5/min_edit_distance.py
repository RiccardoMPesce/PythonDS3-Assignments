"""
This problem is called the string edit distance problem, and is quite useful in many areas of research. 
Suppose that you want to transform the word “algorithm” into the word “alligator.” 
For each letter you can either copy the letter from one word to another at a cost of 5, you can delete 
a letter at cost of 20, or insert a letter at a cost of 20. The total cost to transform one word into 
another is used by spell check programs to provide suggestions for words that are close to one another. 
Use dynamic programming techniques to develop an algorithm that gives you the smallest edit distance 
between any two words.
"""

def min_edit_distance(src, dest, tab={}):
    if (src, dest) not in tab:
        # Insertion and deletion take 20
        if len(src) == 0:
            tab[(src, dest)] = len(dest) * 20
        elif len(dest) == 0:
            tab[(src, dest)] = len(src) * 20
        else:
            if src[0] == dest[0]:
                dist = min_edit_distance(src[1:], dest[1:], tab)
            else:
                # Copying (Substitution) takes 5
                dist = 5 + min(
                    min_edit_distance(src[1:], dest[1:], tab),
                    min_edit_distance(src, dest[1:], tab),
                    min_edit_distance(src[1:], dest, tab)
                )
            tab[(src, dest)] = dist

    return tab[(src, dest)]


def main():
    print(min_edit_distance("alligator", "algorithm"))


if __name__ == "__main__":
    main()
