import random

def vertexName(max):
	for x in xrange(max):
		#type your name generator method

		#yield chr(97+x%26)*(x/26+1)
		#x=0, name=a;x=1, name=b...
		#x=26, name=aa;x=27, name=bb...

		#yield chr(ord('A')+x%58)*(x/58+1)
		yield x

def genVertexTuple(max):
	resultTuple = []
	for name in vertexName(max):
		resultTuple.append(name)
	tuple(resultTuple)
	return resultTuple

def writeEdges(vertexs, fo, edge_num = 0):
	if edge_num == 0:
		for start in xrange(len(vertexs)):
			for end in xrange(start+1,len(vertexs)):
				fo.write(str(start)+','+str(end)+'\n')
		return
	if edge_num > 0:
		for x in xrange(edge_num):
			start, end = random.sample(vertexs, 2)
			fo.write(str(start)+','+str(end)+'\n')
		return
	if edge_num < 0:
		return -1

def genRandomGraph(nodeNum, edge_num = 0, fo = "output.txt"):
	tup = genVertexTuple(nodeNum)
	fo = open('output.txt', 'w')
	writeEdges(tup, fo, edge_num)
	fo.close()


if __name__ == '__main__':
	genRandomGraph(10000,1000000)
		