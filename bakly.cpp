#include <iostream>
#include <fstream>
#include <chrono>
#include <random>

class Graph {

    private:
        double a;
        int n, m;

        int **matrix; // итоговая матрица смежности графа

        std::default_random_engine re;

    void add_edge(int* degries, int from, int to) {
        degries[from]++;
        degries[to]++;

        // for (int i = 0; i < n * m; ++i)
            // std::cout << ((i == to)?1:0) << " ";
        // std::cout << "\\" << std::endl;

        matrix[from/m][to/m] += 1;
    }

    public:
        Graph(int n, int m, double a) {
            re.seed(std::chrono::system_clock::now().time_since_epoch().count());

            this->n = n;
            this->m = m;
            this->a = a;

            int degries[n*m];
            double tmp = 0, p = 0;

            matrix = (int**) malloc(n * sizeof(int*));
            for (int i = 0; i < n; ++i)
                matrix[i] = (int*) malloc(n * sizeof(int));

            for(int i = 0; i < n * m; ++i) {
                degries[i] = 0;

                if (i == 0) {
                    add_edge(degries, i, i);
                    continue;
                }
                
                std::uniform_real_distribution<double> unif(0, (a+1)*(i+1));
                p = unif(re);

                for(int j = 0; j < i; ++j) {
                    tmp = degries[j] + a - 1;
                    p -= tmp;
                    if (p <= 0) {
                        add_edge(degries, i, j);
                        break;
                    }
                }

                if (p > 0)
                    add_edge(degries, i, i);
            }
        }

        void print() {
            print(std::cout);
        }

        void print(std::ostream &stream) {
            stream << n << std::endl;
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j)
                    stream << matrix[i][j] << " ";
                stream << std::endl;
            }
        }

        void print(const char* file_name) {
            std::ofstream f;
            f.open(file_name);
            print(f);
            f.close();
        }

        ~Graph() {
            for (int i = 0; i < n; ++i)
                free(matrix[i]);
            free(matrix);
        }

};


int main(int argc, char** argv) {
    int n, m;
    double a;

    try {
        sscanf(argv[1], "%d", &n);
        sscanf(argv[2], "%d", &m);
        sscanf(argv[3], "%lf", &a);
    } catch(...) {
        std::cout << "Error reading parameters, try again: n, m, a\n";
    }

    Graph g(n, m, a);
    g.print("graph.txt");

    return 0;
}
