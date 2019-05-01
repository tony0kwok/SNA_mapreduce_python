from datetime import datetime
from mrjob.job import MRJob
import re

class MRDegreeCentrality(MRJob):

    def mapper(self, _, line):
        start, end, weight = re.findall(r'"[^"\\]*(?:\\.[^"\\]*)*"|[^,]+',line)
        start = start.replace("\"", "")
        end = end.replace("\"", "")
        weight = int(weight)
        yield str(start), weight
        yield str(end), weight

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    start_time = datetime.now()
    MRDegreeCentrality.run()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print 'elapsed_time: '+str(elapsed_time)
    