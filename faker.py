import random
from datetime import datetime
import sys

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

def writeEdges(vertexs, fo, p = 1):
    if p == 1:
        for start in xrange(len(vertexs)):
            for end in xrange(start+1,len(vertexs)):
                fo.write(str(start)+','+str(end)+',1\n')
        return len(vertexs)*(len(vertexs)-1)
    if p > 0:
        edge_num=long(len(vertexs)*(len(vertexs)-1)/2*p)
        for x in xrange(edge_num):
            start, end = random.sample(vertexs, 2)
            fo.write(str(start)+','+str(end)+',1\n')
        return edge_num
    if p <= 0:
        return -1

def genRandomGraph(nodeNum, p = 0, fo = "input.txt"):
    tup = genVertexTuple(nodeNum)
    fo = open(fo, 'w')
    print writeEdges(tup, fo, p)
    fo.close()


if __name__ == '__main__':
    nodes = int(sys.argv[1])
    p = float(sys.argv[2])
    fo = "edge_list.txt"
    if len(sys.argv)>=4:
        fo = sys.argv[3]
    start_time = datetime.now()
    genRandomGraph(nodes,p,fo)
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print 'elapsed_time: '+str(elapsed_time)