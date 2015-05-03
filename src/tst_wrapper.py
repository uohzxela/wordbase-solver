import sys
import tst

t = None
if __name__ == "__main__":
    while True:
        if not t:
            t = tst.TernarySearchTree()
        print "Input search term:"
        word = sys.stdin.readline().strip()
        (is_valid, is_prefix) = t.find(word)
        print "is prefix?"
        print is_prefix
        print "is valid?"
        print is_valid
