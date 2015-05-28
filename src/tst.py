from random import shuffle

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

# TreeJudge is coded by Stefan Pochmann: https://gist.github.com/pochmann/adcd1e046c62390fd61b

class TreeJudge:
    def __init__(self, word_list_path='Word-List.txt'):
        self.root = {}
        with open(word_list_path) as f:
            for line in f:
                word = line.strip()
                node = self.root
                for letter in word:
                    node = node.setdefault(letter, {})
                node[None] = None
 
    def find(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                return False, False
            node = node[letter]
        return None in node, True