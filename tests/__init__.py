
SPRITESHEET_PATH = "tests/punyworld-overworld-tileset.png"

# worls size in tiles
WORLD_X = 60
WORLD_Y = 34

# Spritesheet tile size (original), and upscale factor
TILESIZE = 16
SCALETILE = 2

# Tile Types
TILE_GRASS = 0
TILE_WATER = 1
TILE_FOREST = 2
TILE_COASTN = 3
TILE_COASTE = 4
TILE_COASTS = 5
TILE_COASTW = 6
TILE_COASTNE = 7
TILE_COASTSE = 8
TILE_COASTSW = 9
TILE_COASTNW = 10
TILE_COASTNE2 = 11
TILE_COASTSE2 = 12
TILE_COASTSW2 = 13
TILE_COASTNW2 = 14
TILE_ROCKN = 15
TILE_ROCKE = 16
TILE_ROCKS = 17
TILE_ROCKW = 18
TILE_ROCKNE = 19
TILE_ROCKSE = 20
TILE_ROCKSW = 21
TILE_ROCKNW = 22
TILE_FORESTN = 23
TILE_FORESTE = 24
TILE_FORESTS = 25
TILE_FORESTW = 26
TILE_FORESTNE = 27
TILE_FORESTSE = 28
TILE_FORESTSW = 29
TILE_FORESTNW = 30
TILE_FORESTNE2 = 31
TILE_FORESTSE2 = 32
TILE_FORESTSW2 = 33
TILE_FORESTNW2 = 34

# Tile Edges
GRASS = 0
WATER = 1
FOREST = 2
COAST_N = 3
COAST_E = 4
COAST_S = 5
COAST_W = 6
FOREST_N = 7
FOREST_E = 8
FOREST_S = 9
FOREST_W = 10
ROCK_N = 11
ROCK_E = 12
ROCK_S = 13
ROCK_W = 14
ROCK = 15

rules = {
	TILE_GRASS : [GRASS, GRASS, GRASS, GRASS],
	TILE_WATER : [WATER, WATER, WATER, WATER],
	TILE_FOREST : [FOREST, FOREST, FOREST, FOREST],
	TILE_COASTN : [GRASS, COAST_N, WATER, COAST_N],
	TILE_COASTE : [COAST_E, GRASS, COAST_E, WATER],
	TILE_COASTS : [WATER, COAST_S, GRASS, COAST_S],
	TILE_COASTW : [COAST_W, WATER, COAST_W, GRASS],
	TILE_COASTNE : [GRASS, GRASS, COAST_E, COAST_N],
	TILE_COASTSE : [COAST_E, GRASS, GRASS, COAST_S],
	TILE_COASTSW : [COAST_W, COAST_S, GRASS, GRASS],
	TILE_COASTNW : [GRASS, COAST_N, COAST_W, GRASS],
	TILE_COASTNE2: [COAST_E, COAST_N, WATER, WATER],
	TILE_COASTSE2: [WATER, COAST_S, COAST_E, WATER],
	TILE_COASTSW2: [WATER, WATER, COAST_W, COAST_S],
	TILE_COASTNW2: [COAST_W, WATER, WATER, COAST_N],
	TILE_ROCKN : [ROCK, ROCK_N, GRASS, ROCK_N],
	TILE_ROCKE : [ROCK_E, ROCK, ROCK_E, GRASS],
	TILE_ROCKS : [GRASS, ROCK_S, ROCK, ROCK_S],
	TILE_ROCKW : [ROCK_W, GRASS, ROCK_W, ROCK],
	TILE_ROCKNE : [ROCK_E, ROCK_N, GRASS, GRASS],
	TILE_ROCKSE : [GRASS, ROCK_S, ROCK_E, GRASS],
	TILE_ROCKSW : [GRASS, GRASS, ROCK_W, ROCK_S],
	TILE_ROCKNW : [ROCK_W, GRASS, GRASS, ROCK_N],
	TILE_FORESTN : [FOREST, FOREST_N, GRASS, FOREST_N],
	TILE_FORESTE : [FOREST_E, FOREST, FOREST_E, GRASS],
	TILE_FORESTS : [GRASS, FOREST_S, FOREST, FOREST_S],
	TILE_FORESTW : [FOREST_W, GRASS, FOREST_W, FOREST],
	TILE_FORESTNE: [FOREST_E, FOREST_N, GRASS, GRASS],
	TILE_FORESTSE: [GRASS, FOREST_S, FOREST_E, GRASS],
	TILE_FORESTSW: [GRASS, GRASS, FOREST_W, FOREST_S],
	TILE_FORESTNW: [FOREST_W, GRASS, GRASS, FOREST_N],
	TILE_FORESTNE2: [FOREST, FOREST, FOREST_E, FOREST_N],
	TILE_FORESTSE2: [FOREST_E, FOREST, FOREST, FOREST_S],
	TILE_FORESTSW2: [FOREST_W, FOREST_S, FOREST, FOREST],
	TILE_FORESTNW2: [FOREST, FOREST_N, FOREST_W, FOREST],
}

weights = {
	TILE_GRASS : 16,
	TILE_WATER : 4,
	TILE_FOREST : 5,
	TILE_COASTN : 5,
	TILE_COASTE : 5,
	TILE_COASTS : 5,
	TILE_COASTW : 5,
	TILE_COASTNE : 5,
	TILE_COASTSE : 5,
	TILE_COASTSW : 5,
	TILE_COASTNW : 5,
	TILE_COASTNE2 : 2,
	TILE_COASTSE2 : 2,
	TILE_COASTSW2 : 2,
	TILE_COASTNW2 : 2,
	TILE_FORESTN : 4,
	TILE_FORESTE : 4,
	TILE_FORESTS : 4,
	TILE_FORESTW : 4,
	TILE_FORESTNE : 4,
	TILE_FORESTSE : 4,
	TILE_FORESTSW : 4,
	TILE_FORESTNW : 4,
	TILE_FORESTNE2: 2,
	TILE_FORESTSE2: 2,
	TILE_FORESTSW2: 2,
	TILE_FORESTNW2: 2,
	TILE_ROCKN : 4,
	TILE_ROCKE : 4,
	TILE_ROCKS : 4,
	TILE_ROCKW : 4,
	TILE_ROCKNE : 4,
	TILE_ROCKSE : 4,
	TILE_ROCKSW : 4,
	TILE_ROCKNW : 4,
}

sprites = {
	TILE_GRASS : (16, 0),
	TILE_WATER : (128, 176),
	TILE_FOREST: (16, 128),
	TILE_COASTN : (128, 160),
	TILE_COASTE : (144, 176),
	TILE_COASTS : (128, 192),
	TILE_COASTW : (112, 176),
	TILE_COASTNE : (144, 160),
	TILE_COASTSE : (144, 192),
	TILE_COASTSW : (112, 192),
	TILE_COASTNW : (112, 160),
	TILE_COASTNE2: (176, 160),
	TILE_COASTSE2: (176, 176),
	TILE_COASTSW2: (160, 176),
	TILE_COASTNW2: (160, 160),
	TILE_FORESTN : (16, 144),
	TILE_FORESTE : (0, 128),
	TILE_FORESTS : (16, 112),
	TILE_FORESTW : (32, 128),
	TILE_FORESTNE : (0, 144),
	TILE_FORESTSE : (0, 112),
	TILE_FORESTSW : (32, 112),
	TILE_FORESTNW : (32, 144),
	TILE_FORESTNE2: (96, 128),
	TILE_FORESTSE2: (96, 112),
	TILE_FORESTSW2: (112, 112),
	TILE_FORESTNW2: (112, 128),
	TILE_ROCKN : (16, 96),
	TILE_ROCKE : (0, 80),
	TILE_ROCKS : (16, 64),
	TILE_ROCKW : (32, 80),
	TILE_ROCKNE : (0, 96),
	TILE_ROCKSE : (0, 64),
	TILE_ROCKSW : (32, 64),
	TILE_ROCKNW : (32, 96),
}

#######################################################
#######################################################
#######################################################
#######################################################
#######################################################

import pygame
import os
import sys

FILE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

sys.path.append( os.path.join(FILE_DIRECTORY, '..') )

from WaveFunctionCollapse import AbstractTile, AbstractWorld, Direction, WaveCollapseConfig

sys.path.pop()

class DrawWorld:

	font0 : pygame.font.Font
	font1 : pygame.font.Font
	font2 : pygame.font.Font

	spritesheet : pygame.Surface
	world : AbstractWorld
	display : pygame.Surface

	def __init__( self, world : AbstractWorld ):
		self.font0 = pygame.font.Font(pygame.font.get_default_font(), 14)
		self.font1 = pygame.font.Font(pygame.font.get_default_font(), 11)
		self.font2 = pygame.font.Font(pygame.font.get_default_font(), 8)
		self.spritesheet = pygame.image.load(SPRITESHEET_PATH).convert_alpha()
		self.world = world
		self.display = pygame.Surface((WORLD_X * TILESIZE * SCALETILE, WORLD_Y * TILESIZE * SCALETILE))

	def update(self):
		lowest_entropy = self.world.get_lowest_entropy()
		for y in range(WORLD_Y):
			for x in range(WORLD_X):
				tile_entropy = self.world.get_entropy(x, y)
				tile_type = self.world.get_type(x, y)
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
					pos = sprites[tile_type]
					tile_image = self.spritesheet.subsurface(pygame.Rect(pos[0], pos[1], TILESIZE, TILESIZE))
				else:  # Forest needs a grass tile to be drawn first
					pos = sprites[TILE_GRASS]
					tile_image = self.spritesheet.subsurface(pygame.Rect(pos[0], pos[1], TILESIZE, TILESIZE))
					tile_image = pygame.transform.scale_by(tile_image, (SCALETILE, SCALETILE))
					self.display.blit(tile_image, (x * TILESIZE * SCALETILE, y * TILESIZE * SCALETILE))
					pos = sprites[tile_type]
					tile_image = self.spritesheet.subsurface(pygame.Rect(pos[0], pos[1], TILESIZE, TILESIZE))

				tile_image = pygame.transform.scale_by(tile_image, (SCALETILE, SCALETILE))
				self.display.blit(tile_image, (x * TILESIZE * SCALETILE, y * TILESIZE * SCALETILE))

	def draw( self, display : pygame.Surface ):
		display.blit(self.display, (0, 0))

def example_scenario( ) -> None:

	INTERACTIVE = True
	INTERACTIVE_KEYPRESS = False

	pygame.init()
	clock = pygame.time.Clock()

	displaySurface = pygame.display.set_mode((WORLD_X * TILESIZE * SCALETILE, WORLD_Y * TILESIZE * SCALETILE))
	pygame.display.set_caption("Wave Function Collapse")

	config = WaveCollapseConfig( weights, rules )

	world = AbstractWorld( WORLD_X, WORLD_Y, config )
	world.complete_collapse()

	done = False
	if INTERACTIVE == False:
		while done == False:
			result = world.wave_function_collapse()
			if result == 0:
				done = True

	drawWorld = DrawWorld( world )
	drawWorld.update()

	isRunning = True
	counter = 0

	while isRunning:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				isRunning = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					isRunning = False
				if event.key == pygame.K_SPACE:
					if INTERACTIVE == True and INTERACTIVE_KEYPRESS == True:
						world.wave_function_collapse()
						drawWorld.update()

		if INTERACTIVE == True and INTERACTIVE_KEYPRESS == False:
			if not done:
				result = world.wave_function_collapse()
				if result == 0:
					done = True
			drawWorld.update()

		if counter > 120:
			counter = 0
			drawWorld.draw(displaySurface)
			pygame.display.flip()
			clock.tick(60)
		else:
			counter += 1

	pygame.quit()

if __name__ == '__main__':

	example_scenario( )
