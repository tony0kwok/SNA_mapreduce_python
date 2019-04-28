from datetime import datetime
from mrjob.job import MRJob


class MRDegreeCentrality(MRJob):

    def mapper(self, _, line):
        start, end = line.split(',')
        yield str(start), 1
        yield str(end), 1

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRDegreeCentrality.run()
    