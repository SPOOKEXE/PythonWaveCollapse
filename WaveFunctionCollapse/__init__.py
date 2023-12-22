
from __future__ import annotations

import random

from dataclasses import dataclass, field
from time import sleep

class Direction:
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3
	# NORTH_EAST = 4
	# NORTH_WEST = 5
	# SOUTH_EAST = 6
	# SOUTH_WEST = 7

@dataclass
class WaveCollapseConfig:
	weights : dict[str, int] = field(default_factory=dict)
	rules : dict[str, list[str]] = field(default_factory=dict)

class AbstractTile:
	x : int
	y : int
	possibilities : list
	entropy : int
	neighbours : dict

	def __init__(self, x : int, y : int, possibilities : list[str]):
		self.x = x
		self.y = y
		self.possibilities = possibilities
		self.entropy = len(self.possibilities)
		self.neighbours = dict()

	def add_neighbour( self, direction, tile ) -> None:
		self.neighbours[direction] = tile

	def get_neighbour( self, direction ) -> AbstractTile:
		return self.neighbours[direction]

	def get_directions( self ) -> list:
		return list(self.neighbours.keys())

	def get_possibilities( self ) -> list:
		return self.possibilities

	def collapse( self, config : WaveCollapseConfig ) -> None:
		weights = [ config.weights[possibility] for possibility in self.possibilities ]
		self.possibilities = random.choices(self.possibilities, weights=weights, k=1)
		self.entropy = 0

	def constrain( self, neighbourPossibilities : list, direction : int, config : WaveCollapseConfig ) -> bool:
		reduced = False
		if self.entropy > 0:
			connectors = [
				config.rules[neighbourPossibility][direction]
				for neighbourPossibility in neighbourPossibilities
			]
			if direction == Direction.NORTH:
				opposite = Direction.SOUTH
			elif direction == Direction.EAST:
				opposite = Direction.WEST
			elif direction == Direction.SOUTH:
				opposite = Direction.NORTH
			elif direction == Direction.WEST:
				opposite = Direction.EAST
			# elif direction == Direction.NORTH_EAST:
			# 	opposite = Direction.SOUTH_WEST
			# elif direction == Direction.NORTH_WEST:
			# 	opposite = Direction.SOUTH_EAST
			# elif direction == Direction.SOUTH_EAST:
			# 	opposite = Direction.NORTH_WEST
			# elif direction == Direction.SOUTH_WEST:
			# 	opposite = Direction.NORTH_EAST
			for possibility in self.possibilities.copy():
				if config.rules[possibility][opposite] not in connectors:
					self.possibilities.remove(possibility)
					reduced = True
			self.entropy = len(self.possibilities)
		return reduced

class Stack:

	items : list

	def __init__(self):
		self.items = []

	def is_empty(self):
		return len(self.items) == 0

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.is_empty():
			return self.items.pop()
		else:
			raise IndexError("pop from empty stack")

	def size(self):
		return len(self.items)

class AbstractWorld:

	config : WaveCollapseConfig

	def __init__(self, width : int, height : int, config : WaveCollapseConfig):
		self.cols = width
		self.rows = height
		self.config = config

		possibilities : list[str] = list(config.rules.keys())
		self.tileRows = []
		for y in range(height):
			row = []
			for x in range(width):
				row.append( AbstractTile(x, y, possibilities.copy()) )
			self.tileRows.append(row)

		for y in range(height):
			for x in range(width):
				tile = self.tileRows[y][x]
				if y > 0:
					tile.add_neighbour(Direction.NORTH, self.tileRows[y-1][x])
				if x < width - 1:
					tile.add_neighbour(Direction.EAST, self.tileRows[y][x+1])
				if y < height - 1:
					tile.add_neighbour(Direction.SOUTH, self.tileRows[y+1][x])
				if x > 0:
					tile.add_neighbour(Direction.WEST, self.tileRows[y][x-1])
				# NE/SE/SW/NW

	def get_entropy(self, x : int, y : int):
		return self.tileRows[y][x].entropy

	def get_type(self, x : int, y : int):
		return self.tileRows[y][x].possibilities[0]

	def get_lowest_entropy(self):
		lowestEntropy = len(list(self.config.rules.keys()))
		for y in range(self.rows):
			for x in range(self.cols):
				tileEntropy = self.tileRows[y][x].entropy
				if tileEntropy > 0 and tileEntropy < lowestEntropy:
					lowestEntropy = tileEntropy
		return lowestEntropy

	def get_tiles_lowest_entropy( self ):
		lowestEntropy = len(list(self.config.rules.keys()))
		tileList = []
		for y in range(self.rows):
			for x in range(self.cols):
				tileEntropy = self.tileRows[y][x].entropy
				if tileEntropy > 0:
					if tileEntropy < lowestEntropy:
						tileList.clear()
						lowestEntropy = tileEntropy
					if tileEntropy == lowestEntropy:
						tileList.append(self.tileRows[y][x])
		return tileList

	def wave_function_collapse( self ):
		tilesLowestEntropy = self.get_tiles_lowest_entropy()
		if tilesLowestEntropy == []: return 0

		tileToCollapse : AbstractTile = random.choice(tilesLowestEntropy)
		tileToCollapse.collapse( self.config )

		stack = Stack()
		stack.push(tileToCollapse)

		while(stack.is_empty() == False):
			tile : AbstractTile = stack.pop()
			tilePossibilities = tile.get_possibilities()
			directions = tile.get_directions()
			for direction in directions:
				neighbour = tile.get_neighbour(direction)
				if neighbour.entropy != 0:
					reduced = neighbour.constrain(tilePossibilities, direction, self.config)
					if reduced == True:
						stack.push(neighbour) # When possibilities were reduced need to propagate further
		return 1

	def complete_collapse( self, interval : float | int = 0 ) -> None:
		while self.wave_function_collapse() != 0:
			sleep( interval )
