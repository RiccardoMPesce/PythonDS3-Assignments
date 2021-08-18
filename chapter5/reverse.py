def reverse(s):
    return s if len(s) <= 1 else s[-1] + reverse(s[1:-1]) + s[0]

def main():
    s1 = "Python is awesome!"
    s2 = "Data Science rocks!"
    s3 = "Neuroscience"

    for s in (s1, s2, s3):
        print(reverse(s))

if __name__ == "__main__":
    main()