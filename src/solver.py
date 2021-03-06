import extractor
import tst
import sys
from operator import itemgetter

WHITE = 0
ORANGE = 1
BLUE = 2
BLACK = 3
PLAYER_MAP = {'orange': ORANGE, 'blue': BLUE}

def make_graph(matrix, color_map, player):
	root = None
	graph = {root: set() }

	for i, row in enumerate(matrix):
		for j, char in enumerate(row):
			node = (i, j)
			children = set()
			graph[node] = children
			if player == color_map[i, j]:
				graph[root].add(node)
			add_children(node, children, matrix)
	return graph

def add_children(node, children, matrix):
	x0, y0 = node
	for i in [-1, 0, 1]:
		x = x0 + i
		if not (0 <= x < len(matrix)):
			continue
		for j in [-1, 0, 1]:
			y = y0 + j
			if not (0 <= y < len(matrix[0])) or (i==j==0):
				continue
			children.add((x,y))

def to_word(matrix, pos_list):
	return ''.join(matrix[pos[0]][pos[1]] for pos in pos_list if pos is not None)

def get_weight(pos_list):
	return sum(pos[0] for pos in pos_list if pos is not None)

def find_words(graph, matrix, position, prefix, results, dictionary):
	prefix.append(position)
	word = to_word(matrix, prefix).upper()
	if len(word) >= 2:
		(is_valid, is_prefix) = dictionary.find(word)
		if is_valid:
			results.add((word, prefix[-1][0]))
		elif not is_prefix:
			return
	for child in graph[position]:
		if child not in prefix:
			child_prefix = list(prefix)
			find_words(graph, matrix, child, child_prefix, results, dictionary)
	return

def solve(color, img_path, word_list_path=None):
	player = PLAYER_MAP[color]
	matrix, color_map = extractor.get_matrix(img_path)
	for i, row in enumerate(matrix):
		print row
	dictionary = tst.TreeJudge(word_list_path) if word_list_path else tst.TreeJudge()
	graph = make_graph(matrix, color_map, player)
	res = set()
	find_words(graph, matrix, None, [], res, dictionary)
	res = list(res)
	if player == ORANGE:
		return sorted(res, key=itemgetter(1), reverse=True)
	else:
		return sorted(res, key=itemgetter(1))

def main():
	if len(sys.argv) == 3:
		print solve(sys.argv[1].lower(), sys.argv[2])
	else:
		raise Exception("Wrong number of arguments!")

if __name__ == '__main__':
    main()
