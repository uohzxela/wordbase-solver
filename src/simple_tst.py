from random import shuffle
import cPickle as pickle
import redis

class Node:
    def __init__(self, data):
        self.data = data
        self.is_end_of_str = False
        self.left = None
        self.eq = None
        self.right = None


def insert(root, word, i=0):
    if root is None:
        root =  Node(word[i])
    if word[i] < root.data:
        root.left = insert(root.left, word, i)
    elif word[i] > root.data:
        root.right = insert(root.right, word, i)
    else:
        if i+1 < len(word):
            root.eq = insert(root.eq, word, i+1)
        else:
            root.is_end_of_str = True
    return root


def search(root, word, i=0):
    if root is None:
        return False
    if word[i] < root.data:
        return search(root.left, word, i)
    elif word[i] > root.data:
        return search(root.right, word, i)
    else:
        if i+1 == len(word):
            return root.is_end_of_str
        return search(root.eq, word, i+1)

def get_root():
    root = None
    with open("Word-List.txt") as f:
        words  = f.readlines()
        shuffle(words)
        for word in words:
            root = insert(root, word.strip())
    return root

# r = redis.StrictRedis(host='localhost', port=6379, db=0)
# pickled_obj = pickle.dumps(root)
# r.set('tst', pickled_obj)
# root = pickle.loads(r.get('tst'))


