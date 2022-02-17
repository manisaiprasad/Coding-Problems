from mrjob.job import MRJob
from mrjob.step import MRStep


class MatrixMultiplication(MRJob):
    def __init__(self, m, n, k):
        self.m = m
        self.n = n
        self.k = k

    def mapper(self, _, line):
        i, j, v = line.split()
        i = int(i)
        j = int(j)
        v = float(v)
        if i < self.m and j < self.n:
            yield (i, j), (v, 1)

    def reducer(self, key, values):
        v = 0
        n = 0
        for v, n in values:
            v += v
            n += n
        yield key, (v, n)

    def mapper2(self, key, value):
        i, j = key
        v, n = value
        if i < self.m and j < self.k:
            yield (i, j), (v, n)

    def reducer2(self, key, values):
        v = 0
        n = 0
        for v, n in values:
            v += v
            n += n
        yield key, v / n

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(mapper=self.mapper2, reducer=self.reducer2)
        ]


if __name__ == '__main__':
    MatrixMultiplication.run()
