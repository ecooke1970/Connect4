#!/usr/bin/env python
# coding: utf-8

# creates a game board
# Author: Erik Cooke

class GameBoard:
	"""rows-number of rows in game board(max 9)
	columns-number of columns in game board(max 9)
	init_char - The character to fill the board with initially"""

	def __init__(self, rows=3, columns=3, init_char=' '):
		if rows > 9:
			self.rows = 9
		else:
			self.rows = rows
		if columns > 9:
			self.columns = 9
		else:
			self.columns = columns
		self.init_char = init_char
		self.board = [[init_char for i in range(self.columns)] for j in range(self.rows)]

	def init_board(self):
		"""Sets the board back to its original state"""
		self.board = [[self.init_char for i in range(self.columns)] for j in range(self.rows)]

	def get_num_rows(self):
		"""Returns the number of rows"""
		return self.rows

	def get_num_columns(self):
		"""Returns the number of columns"""
		return self.columns

	def get_row(self, row):
		"""Returns a list containing each element in row"""
		return self.board[row]

	def get_column(self, column):
		"""Returns a list containing each element in column"""
		col = []
		for i in range(0, self.rows):
			col.append(self.board[i][column])
		return col

	def get_diagonal(self, row, column, direction="ur", return_form="string"):
		"""Returns a list or string containing each element in a diagonal direction starting at the row, column
		going in the designated direction (ur = up-right, ul = up-left, dr = down-right, dl = down-left.
		Default direction is up-right.  return_form designates return type: "list" or default "string" """
		diagonal = ""
		if direction.lower() == "dr":
			# Down Right
			while row < self.rows and column < self.columns:
				diagonal += (self.board[row][column])
				row += 1
				column += 1
		elif direction.lower() == "dl":
			# Down Left
			while row < self.rows and column >= 0:
				diagonal += (self.board[row][column])
				row += 1
				column -= 1
		elif direction.lower() == "ul":
			# Up Left
			while row >= 0 and column >= 0:
				diagonal += (self.board[row][column])
				row -= 1
				column -= 1
		else:
			# Up Right
			while row >= 0 and column < self.columns:
				diagonal += (self.board[row][column])
				row -= 1
				column += 1
		if return_form == "list":
			return list(diagonal)
		else:
			return diagonal

	def get_position(self, row, column):
		"""Returns the character stored at the row, column position on the board"""
		return self.board[row][column]

	def set_position(self, player, row, column):
		"""Places the first character from player into the position row, column on the board"""
		self.board[row][column] = player[0]

	def print_board(self):
		"""Prints the board to the console with column number headings and lines between rows and columns"""
		print("")
		print(" ", end="")
		for i in range(self.columns):
			print(str(i + 1), end=" ")
		print("")
		print("-" * (self.columns * 2) + "-")
		for row in self.board:
			print("|", end="")
			for col in row:
				print(col + "|", end="")
			print("\n" + "-" * (self.columns * 2) + "-")
