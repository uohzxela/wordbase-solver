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

class TernarySearchTree:
    def __init__(self, word_list_path='Word-List.txt'):
        self.root = None
        with open(word_list_path) as f:
            words  = f.readlines()
            shuffle(words)
            for word in words:
                self.root = self.insert(self.root, word.strip())

    def insert(self, root, word, i=0):
        if root is None:
            root =  Node(word[i])
        if word[i] < root.data:
            root.left = self.insert(root.left, word, i)
        elif word[i] > root.data:
            root.right = self.insert(root.right, word, i)
        else:
            if i+1 < len(word):
                root.eq = self.insert(root.eq, word, i+1)
            else:
                root.is_end_of_str = True
        return root

    def find(self, word):
        return self.search(self.root, word)

    def search(self, root, word, i=0):
        if root is None:
            return (False, False)
        if word[i] < root.data:
            return self.search(root.left, word, i)
        elif word[i] > root.data:
            return self.search(root.right, word, i)
        else:
            if i+1 == len(word):
                return (root.is_end_of_str, True)
            return self.search(root.eq, word, i+1)
