import sys
import simple_tst

root = None
if __name__ == "__main__":
    while True:
        if not root:
            root = simple_tst.get_root()
        print "Input search term:"
        word = sys.stdin.readline().strip()
        print simple_tst.search(root, word)
