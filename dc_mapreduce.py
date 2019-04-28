from datetime import datetime
from mrjob.job import MRJob


class MRDegreeCentrality(MRJob):

    def mapper(self, _, line):
        start, end, weight = line.split(',')
        weight = int(weight)
        yield str(start), weight
        yield str(end), weight

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRDegreeCentrality.run()
    