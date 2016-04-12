#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

# POS_CHAR = u"\u25A1"
# NEG_CHAR = u"\u2716"
# UNK_CHAR = u"\u25A0"

POS_CHAR = "Y"
NEG_CHAR = "N"
UNK_CHAR = "?"

print 'POS_CHAR:', POS_CHAR
print 'NEG_CHAR:', NEG_CHAR
print 'UNK_CHAR:', UNK_CHAR

input1 = [[3,1], 5]
expected1 = [
    (POS_CHAR * 3) +
    (NEG_CHAR * 1) +
    (POS_CHAR * 1)
]

input2 = [[], 10]
expected2 = [
    (NEG_CHAR * 10)
]

input3 = [[5], 7]
expected3 = [
    (POS_CHAR * 5) +
    (NEG_CHAR * 2),

    (NEG_CHAR * 1) +
    (POS_CHAR * 5) +
    (NEG_CHAR * 1),

    (NEG_CHAR * 2) +
    (POS_CHAR * 5)
]


def spaceRequired(blockSizes):
    return sum(blockSizes) + (len(blockSizes) - 1)


def generate(blockSizes, rowLength):
    requiredSpace = spaceRequired(blockSizes)

    if rowLength < requiredSpace:
        return []

    if not blockSizes:
        return [NEG_CHAR * rowLength]

    if len(blockSizes) == 1 and blockSizes[0] == rowLength:
        return [POS_CHAR * rowLength]

    result = []

    for i in generate(blockSizes[1:], rowLength - (blockSizes[0] + 1)):
        result.append((POS_CHAR * blockSizes[0]) + NEG_CHAR + i)

    for i in generate(blockSizes, rowLength - 1):
        result.append(NEG_CHAR + i)

    return result


def noConflict(line1, line2):
    assert len(line1) == len(line2)
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            if line1[i] != UNK_CHAR and line2[i] != UNK_CHAR:
                return False
    return True


def rowSolve(fRows, existingBoard):
    rows = []
    for i in range(len(fRows)):
        fullResults = generate(fRows[i], len(fRows))
        noConflictLambda = lambda x: noConflict(existingBoard[i], x)
        results = filter(noConflictLambda, fullResults)
        output = ''
        for j in range(len(fRows)):
            if all(result[j] == POS_CHAR for result in results):
                output += POS_CHAR
            elif not any(result[j] == POS_CHAR for result in results):
                output += NEG_CHAR
            else:
                output += UNK_CHAR
        rows.append(output)

    return rows

def colSolve(fCols, existingBoard):
    output = [''] * len(fCols)
    for i in range(len(fCols)):
        fullResults = generate(fCols[i], len(fCols))
        currentCol = ''.join([row[i] for row in existingBoard])
        noConflictLambda = lambda x: noConflict(currentCol, x)
        results = filter(noConflictLambda, fullResults)
        for j in range(len(fCols)):
            if all(result[j] == POS_CHAR for result in results):
                output[j] += POS_CHAR
            elif not any(result[j] == POS_CHAR for result in results):
                output[j] += NEG_CHAR
            else:
                output[j] += UNK_CHAR

    return output


assert generate(*input1) == expected1
assert generate(*input2) == expected2
assert generate(*input3) == expected3

def read(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    formattedLines = []
    for line in lines:
        formattedLines.append(map(int, line.split(',')))
    return formattedLines


gchqRows = read('gchqRows.txt')
gchqCols = read('gchqCols.txt')
simpleRows = read('simpleRows.txt')
simpleCols = read('simpleCols.txt')


def solve(rows, cols):
    board = [UNK_CHAR * len(rows)] * len(cols)
    # TODO: Proper termination condition (like "while not solved:" or something)
    for _ in range(20):
        result = [''] * len(cols)
        solvedRows = rowSolve(rows, board)
        solvedCols = colSolve(cols, board)
        # Combine what we know into one board state
        for i in range(len(rows)):
            for j in range(len(cols)):
                if solvedRows[i][j] == solvedCols[i][j]: # If the value from the row solution and column solution match, take it
                    result[i] += solvedRows[i][j]
                elif solvedRows[i][j] == UNK_CHAR: # If the value from the row solution was unknown, take the column solution value
                    result[i] += solvedCols[i][j]
                elif solvedCols[i][j] == UNK_CHAR: # If the value from the column solution was unknown, take the row solution value
                    result[i] += solvedRows[i][j]
                else: # This should never happen
                    result[i] += UNK_CHAR
                    print 'MISMATCH!!! (ERROR)'

        board = result

        print ('='*len(formattedRows) + '\n')*2
        for row in result:
            print row



solve(formattedRows, formattedCols)

