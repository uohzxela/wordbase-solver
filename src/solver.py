import extract_gameboard
import simple_tst as tst


def make_graph(matrix):
	root = None
	graph = {root: set() }
	chardict = { root: ''}

	for i, row in enumerate(matrix):
		for j, char in enumerate(row):
			chardict[(i,j)] = char
			node = (i, j)
			children = set()
			graph[node] = children
			graph[root].add(node)
			add_children(node, children, matrix)
	return graph, chardict

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

def to_word(chardict, pos_list):
	return ''.join(chardict[x] for x in pos_list)

def find_words(graph, chardict, position, prefix, results, root):
	prefix.append(position)
	word = to_word(chardict, prefix).upper()
	print word 
	if len(word) >= 2:
		if tst.search(root, word):
			print "added"
			results.add(word)
		else:
			print 'rejected'
			return
	for child in graph[position]:
		print prefix
		if child not in prefix:
			prefix2 = list(prefix)
			find_words(graph, chardict, child, prefix2, results, root)
	return

matrix = extract_gameboard.get_matrix("wordbase.png")
# matrix = [['C', 'A'], ['T', 'B']]
root = tst.get_root()
graph, chardict = make_graph(matrix)
res = set()
find_words(graph, chardict, None, [], res, root)

print res 