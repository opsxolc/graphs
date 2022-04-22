all:
	g++ bakly.cpp -o bakly -O3

plot:
	python3 plot.py

clean:
	rm bakly
