"""
Sudoku Puzzle solver

"""

from __future__ import annotations
from typing import List, Set, Union, Any


class SudokuPuzzle():
    """
    A sudoku puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, n: int, symbols: List[List[str]], symbol_set: Set[str]):
        """
        Create a new nxn SudokuPuzzle with symbols
        from symbol_set already selected.

        Note:
            Grid symbols are represented as letters or numerals
            The empty space is represented as a "*"

        Preconditions:
        - n is a positive integer, n > 0
        - there are n symbols in the given symbol_set
        - there are n lists in symbols, and each list has n strings
        """
        # Private attributes
        # _n
        #   The number of rows/columns in this puzzle's grid
        # _symbols
        #   All the symbols filled in so far in this puzzle; each sublist
        #   represents one row of symbols filled in
        # _symbol_set
        #   The set of all symbols that each row/column/subsquare must have
        #   exactly one of, for this puzzle to be solved
        _n: int
        _symbols: List[List[str]]
        _symbol_set: Set[str]

        self._n, self._symbols, self._symbol_set = n, symbols, symbol_set

    def is_solved(self) -> bool:
        """
        Return whether this SudokuPuzzle is solved.

        >>> r1 = ["A", "B", "C", "D"]
        >>> r2 = ["C", "D", "A", "B"]
        >>> r3 = ["B", "A", "D", "C"]
        >>> r4 = ["D", "C", "B", "A"]
        >>> grid = [r1, r2, r3, r4]
        >>> s = SudokuPuzzle(4, grid, {"A", "B", "C", "D"})
        >>> s.is_solved()
        True
        >>> r3[1] = "D"
        >>> r3[2] = "A"
        >>> grid = [r1, r2, r3, r4]
        >>> s = SudokuPuzzle(4, grid, {"A", "B", "C", "D"})
        >>> s.is_solved()
        False
        """

        # temporary variables to give convenient names to each attribute
        n, symbols = self._n, self._symbols

        # check that there is no "*" left and
        # all rows, column, subsquares have correct symbols
        return (not any("*" in row for row in symbols)) \
               and all([(self._row_set(i) == self._symbol_set and
                         self._column_set(j) == self._symbol_set and
                         self._subsquare_set(i, j) ==
                         self._symbol_set) for i in range(n) for j in range(n)])

    # some private helper methods (note the private docstrings for each of them)
    def _row_set(self, r: int) -> Set[str]:
        # Return set of symbols in row of SudokuPuzzle self's symbols
        # where position m occurs.

        # set of elements from symbols[r]
        return set(self._symbols[r])

    def _column_set(self, c: int) -> Set[str]:
        # Return set of symbols in column of SudokuPuzzle self's symbols
        # where position m occurs.

        # set of elements from symbols[0][c], symbols[1][c],
        # ... symbols[len(symbols)-1][c]
        return set([row[c] for row in self._symbols])

    def _subsquare_set(self, r: int, c: int) -> Set[str]:
        # Return set of symbols in subsquare of SudokuPuzzle self's symbols
        # where position m occurs.

        # convenient names
        n, symbols = self._n, self._symbols
        # length of subsquares
        ss = round(n ** (1 / 2))
        # upper-left position of m's subsquare
        ul_row = (r // ss) * ss
        ul_col = (c // ss) * ss

        subsquare_symbols = []
        for i in range(ss):
            for j in range(ss):
                subsquare_symbols.append(symbols[ul_row + i][ul_col + j])
        return set(subsquare_symbols)
