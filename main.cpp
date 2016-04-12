/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  Nonogram solver
 *
 *        Version:  1.0
 *        Created:  01/07/2016 01:39:43 PM
 *       Revision:  none
 *       Compiler:  g++
 *
 *         Author:  Andrew Epstein
 *
 * =====================================================================================
 */

#include <iostream>
#include <vector>

using namespace std;

/*
 * Print out an iterable with separator of your choice, \n by default.
 * @param I v The iterable to print
 * @param string sep optional, endl by default, gets printed after each element in v.
 * @param string end optional, "" by default, gets printed once after the entire iterable has been printed.
 * @return void
 */
template <typename I>
void printIterable( I v, string sep = "\n", string end = "" ) {
	for( auto it = v.begin(); it != v.end(); ++it ) {
		cout << *it << sep;
	}
	cout << end;
}

template<typename T>
auto generatePossibilities( T row, int length ) {
	vector<int> result( length, 0 );
	return result;
}

int main() {
	int width = 20;
	int height = 20;
	auto exampleRow = {15};
	auto result = generatePossibilities( exampleRow, width );
	printIterable( result );
	return 0;
}
