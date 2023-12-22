import random
import pygame

from Config import *

class Stack:
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

class Tile:

	def __init__(self, x, y):
		self.possibilities = list(tileRules.keys())
		self.entropy = len(self.possibilities)
		self.neighbours = dict()

	def addNeighbour(self, direction, tile):
		self.neighbours[direction] = tile

	def getNeighbour(self, direction):
		return self.neighbours[direction]

	def getDirections(self):
		return list(self.neighbours.keys())

	def getPossibilities(self):
		return self.possibilities

	def collapse(self):
		weights = [tileWeights[possibility] for possibility in self.possibilities]
		self.possibilities = random.choices(self.possibilities, weights=weights, k=1)
		self.entropy = 0

	def constrain(self, neighbourPossibilities, direction):
		reduced = False

		if self.entropy > 0:
			connectors = []
			for neighbourPossibility in neighbourPossibilities:
				connectors.append(tileRules[neighbourPossibility][direction])

			# check opposite side
			if direction == NORTH: opposite = SOUTH
			if direction == EAST:  opposite = WEST
			if direction == SOUTH: opposite = NORTH
			if direction == WEST:  opposite = EAST

			for possibility in self.possibilities.copy():
				if tileRules[possibility][opposite] not in connectors:
					self.possibilities.remove(possibility)
					reduced = True

			self.entropy = len(self.possibilities)

		return reduced
class World:

	def __init__(self, sizeX, sizeY):
		self.cols = sizeX
		self.rows = sizeY

		self.tileRows = []
		for y in range(sizeY):
			tiles = []
			for x in range(sizeX):
				tile = Tile(x, y)
				tiles.append(tile)
			self.tileRows.append(tiles)

		for y in range(sizeY):
			for x in range(sizeX):
				tile = self.tileRows[y][x]
				if y > 0:
					tile.addNeighbour(NORTH, self.tileRows[y - 1][x])
				if x < sizeX - 1:
					tile.addNeighbour(EAST, self.tileRows[y][x + 1])
				if y < sizeY - 1:
					tile.addNeighbour(SOUTH, self.tileRows[y + 1][x])
				if x > 0:
					tile.addNeighbour(WEST, self.tileRows[y][x - 1])


	def getEntropy(self, x, y):
		return self.tileRows[y][x].entropy


	def getType(self, x, y):
		return self.tileRows[y][x].possibilities[0]


	def getLowestEntropy(self):
		lowestEntropy = len(list(tileRules.keys()))
		for y in range(self.rows):
			for x in range(self.cols):
				tileEntropy = self.tileRows[y][x].entropy
				if tileEntropy > 0:
					if tileEntropy < lowestEntropy:
						lowestEntropy = tileEntropy
		return lowestEntropy


	def getTilesLowestEntropy(self):
		lowestEntropy = len(list(tileRules.keys()))
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


	def waveFunctionCollapse(self):

		tilesLowestEntropy = self.getTilesLowestEntropy()
		if tilesLowestEntropy == []:
			return 0

		tileToCollapse = random.choice(tilesLowestEntropy)
		tileToCollapse.collapse()

		stack = Stack()
		stack.push(tileToCollapse)

		while(stack.is_empty() == False):
			tile = stack.pop()
			tilePossibilities = tile.getPossibilities()
			directions = tile.getDirections()

			for direction in directions:
				neighbour = tile.getNeighbour(direction)
				if neighbour.entropy != 0:
					reduced = neighbour.constrain(tilePossibilities, direction)
					if reduced == True:
						stack.push(neighbour)    # When possibilities were reduced need to propagate further

		return 1

class DrawWorld:

	def __init__(self, world):
		self.font0 = pygame.font.Font(pygame.font.get_default_font(), 14)
		self.font1 = pygame.font.Font(pygame.font.get_default_font(), 11)
		self.font2 = pygame.font.Font(pygame.font.get_default_font(), 8)
		self.spritesheet = pygame.image.load(SPRITESHEET_PATH).convert_alpha()
		self.world = world
		self.worldSurface = pygame.Surface((WORLD_X * TILESIZE * SCALETILE, WORLD_Y * TILESIZE * SCALETILE))

	def update(self):
		lowest_entropy = self.world.getLowestEntropy()
		for y in range(WORLD_Y):
			for x in range(WORLD_X):
				tile_entropy = self.world.getEntropy(x, y)
				tile_type = self.world.getType(x, y)
				if tile_entropy > 0:
					tile_image = pygame.Surface((TILESIZE, TILESIZE))
					if tile_entropy == 27:
						textSurface = self.font2.render(str(tile_entropy), True, "darkgrey")
						tile_image.blit(textSurface, (3, 3))
					elif tile_entropy >= 10:
						textSurface = self.font1.render(str(tile_entropy), True, "grey")
						tile_image.blit(textSurface, (2, 3))
					elif tile_entropy < 10:
						if tile_entropy == lowest_entropy:
							textSurface = self.font0.render(str(tile_entropy), True, "green")
						else:
							textSurface = self.font0.render(str(tile_entropy), True, "white")
						tile_image.blit(textSurface, (4, 1))
				elif tile_type < TILE_FORESTN:
					pos = tileSprites[tile_type]
					tile_image = self.spritesheet.subsurface(pygame.Rect(pos[0], pos[1], TILESIZE, TILESIZE))
				else:  # Forest needs a grass tile to be drawn first
					pos = tileSprites[TILE_GRASS]
					tile_image = self.spritesheet.subsurface(pygame.Rect(pos[0], pos[1], TILESIZE, TILESIZE))
					tile_image = pygame.transform.scale_by(tile_image, (SCALETILE, SCALETILE))
					self.worldSurface.blit(tile_image, (x * TILESIZE * SCALETILE, y * TILESIZE * SCALETILE))
					pos = tileSprites[tile_type]
					tile_image = self.spritesheet.subsurface(pygame.Rect(pos[0], pos[1], TILESIZE, TILESIZE))

				tile_image = pygame.transform.scale_by(tile_image, (SCALETILE, SCALETILE))
				self.worldSurface.blit(tile_image, (x * TILESIZE * SCALETILE, y * TILESIZE * SCALETILE))

	def draw(self, displaySurface):
		displaySurface.blit(self.worldSurface, (0, 0))
