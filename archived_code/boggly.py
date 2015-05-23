'''
TernarySearchTree:
    9.0706 seconds to build
    5.8701 seconds to judge all words
    3.8886 seconds to judge all halves
    7.4697 seconds to judge all junk
SetsJudge:
    2.8415 seconds to build
    0.4173 seconds to judge all words
    0.3252 seconds to judge all halves
    1.6681 seconds to judge all junk
TreeJudge:
    1.9294 seconds to build
    0.9376 seconds to judge all words
    0.5434 seconds to judge all halves
    0.9087 seconds to judge all junk
all judges agreed on everything
'''
 
#--------------------------------------------------------------------------------
 
# This tree part is from https://github.com/uohzxela/wordbase-solver/blob/master/src/tst.py
 
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
 
#--------------------------------------------------------------------------------
 
class SetsJudge:
    def __init__(self, word_list_path='Word-List.txt'):
        with open(word_list_path) as f:
            self.wordset = set(map(str.strip, f))
            self.prefixset = set.union(*(set(accumulate(word[:-1])) for word in self.wordset))
            
    def find(self, word):
        isword = word in self.wordset
        isprefix = word in self.prefixset
        return isword, isword or isprefix
 
#--------------------------------------------------------------------------------
 
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
 
#--------------------------------------------------------------------------------
# Preparation
#--------------------------------------------------------------------------------
 
from time import time
import string
from random import sample
from itertools import accumulate
 
word_list_path = 'Word-List.txt'
with open(word_list_path) as f:
    words = list(map(str.strip, f))
shuffle(words)
halves = [word[:(len(word)+1)//2] for word in words]
junk = [''.join(sample(string.ascii_lowercase, 10)) for _ in range(1000000)]
 
def showtime(task):
    print('%10.4f' % (time() - t), 'seconds to', task)
 
def checkmemory(when):
    #input('look at memory consumption ' + when + ', press enter to continue')
    pass
 
#--------------------------------------------------------------------------------
# Test the tree solution
#--------------------------------------------------------------------------------
 
results = {}
for judgeclass in TernarySearchTree, SetsJudge, TreeJudge:
    print(judgeclass.__name__ + ':')
 
    checkmemory('before building')
    t = time()
    judge = judgeclass(word_list_path)
    showtime('build')
    checkmemory('after building')
 
    for what, strings in ('words', words), ('halves', halves), ('junk', junk):
        t = time()
        result = [judge.find(string) for string in strings]
        showtime('judge all ' + what)
        results.setdefault(what, result)
        assert results[what] == result
 
print('all judges agreed on everything')