import random
import collections

class Graph:

    def __init__(self):
        self.a, self.m, self.n = 0, 0, 0
        self.num_V = 0
        self.deg_V = collections.defaultdict(int)

    def add_E(self, i, j):
        self.deg_V[i] += 1
        self.deg_V[j] += 1
        self.matrix[i] = j

    def add_V(self):
        if self.num_V == 0:
            self.add_E(self.num_V, self.num_V)
            self.num_V += 1
            return

        p = random.uniform(0, (self.a+1)*(self.num_V+1))
        # print((self.a+1)*(self.num_V+1))
        for i in range(self.num_V):
            tmp = self.deg_V[i]+self.a-1
            # print(f"p={p} tmp={tmp} deg_V[{i}]={self.deg_V[i]}")
            if tmp >= p:
                self.add_E(self.num_V, i)
                self.num_V += 1
                return
            p -= tmp

        self.add_E(self.num_V, self.num_V)
        self.num_V += 1

    def generate(self, a, n, m):
        self.a, self.n, self.m = a, n, m

        self.matrix = [0 for i in range(m*n)]

        # Generate H mn a,1
        for i in range(m*n):
            self.add_V()

        # for i in self.matrix:
            # for j in range(n*m):
                # if i == j:
                    # print(1, end = ' ')
                # else:
                    # print(0, end = ' ')
            # print()

        self.matrix_final = [[0 for i in range(n)] for j in range(n)]
        # values = []
        # columns_index = []
        # rows_index = []
        for i in range(n*m):
            self.matrix_final[i//m][self.matrix[i] // m] += 1 

        # for i in self.matrix_final:
            # print(i)

        print(self.num_V, m * n)

# g = Graph()

# arr = input().split()
# g.generate(float(arr[0]), *map(int, arr[1:]))
