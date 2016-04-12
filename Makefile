all:
	g++ -std=c++14 -O3 main.cpp -o nonogram
debug:
	g++ -std=c++14 -O0 -g main.cpp -o nonogram
clean:
	rm -f nonogram *.o
