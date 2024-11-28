# Huffman Coding
class Node:
    def __init__(self, character=None, frequency=None):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

def buildTree():
    while len(nodes) > 1:
        nodes.sort(key= lambda x: x.frequency)
        left = nodes.pop(0)
        right = nodes.pop(0)

        merged = Node(frequency=left.frequency + right.frequency)
        merged.left = left
        merged.right = right

        nodes.append(merged)

    return nodes[0]

def generateCodes(node, current_code, codes):
    if node is None:
        return
    
    if node.character is not None:
        codes[node.character] = current_code

    generateCodes(node.left, current_code + '0', codes)
    generateCodes(node.right, current_code + '1', codes)

char_freq = {
    'a': 5,
    'b': 9,
    'c': 12,
    'd': 13,
    'e': 16,
    'f': 45
}

nodes = []

for c, f in char_freq.items():
    nodes.append(Node(character=c, frequency=f))

codes = {}
generateCodes(buildTree(), '', codes)

print(codes)