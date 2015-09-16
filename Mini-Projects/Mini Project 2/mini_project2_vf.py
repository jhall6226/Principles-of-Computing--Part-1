"""
Clone of 2048 game.
"""

#import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # Create new line object to store the merged line
    new_line = []
    
    # Add all non-zero elements to the new line
    for elem in line:
        if not elem == 0:
            new_line.append(elem)
    
    # Merge adjacent elements that are equal, set the left equal to the sum and the right equal to zero (ensures each element is only merged once)
    for index in range(len(new_line)-1):
        if new_line[index] == new_line[index+1]:
            new_line[index]	*= 2
            new_line[index + 1] = 0
    
    # Remove the zeroes added to the new line in the merge process
    for index in range(len(new_line)):
        if index < len(new_line) and new_line[index] == 0:
            new_line.pop(index)
            
    # Append zeroes to the end of the merged line until it is the same length as the original line
    new_line += [0]*(len(line)-len(new_line))
    
    # Return the merged line
    return new_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._starting_tiles = {  UP: [(0,col) for col in range(self._grid_width)],
                            DOWN: [(self._grid_height-1,col) for col in range(self._grid_width)],
                            LEFT: [(row,0) for row in range(self._grid_height)],
                            RIGHT: [(row,self._grid_width-1) for row in range(self._grid_height)]} 
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        str_of_grid = ''
        for index, row in enumerate(self._grid):
            str_of_grid += str(row)
            if not index == len(self._grid) - 1:
                str_of_grid += '\n'
                
        return str_of_grid
        
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def __path_through_grid__(self, start_tile, direction_offset, length_of_line):
        """
        Function that iterates through the tiles in a grid
        in a linear direction and returns the path taken
        
        Both start_cell is a tuple(row, col) denoting the
        starting cell
        
        direction is a tuple that contains difference between
        consecutive cells in the traversal
        """
        path = [] # Values from the path that is traversed
        for step in range(length_of_line):
            row = start_tile[0] + step * direction_offset[0]
            col = start_tile[1] + step * direction_offset[1]
            path.append(self._grid[row][col])
            
        return path
        
    def __set_values_on_path__(self, start_tile, direction_offset, line):
        """
        Function that iterates through the tiles in a grid
        in a linear direction and sets values based on the line provided
        
        Both start_cell is a tuple(row, col) denoting the
        starting cell
        
        direction is a tuple that contains difference between
        consecutive cells in the traversal
        """
        for step in range(len(line)):
            row = start_tile[0] + step * direction_offset[0]
            col = start_tile[1] + step * direction_offset[1]
            self._grid[row][col] = line[step]

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        
        moved = False # Denotes whether any of the lines along the direction of movement actually changed/moved
        
        # Identify the lines to be merged and construct a list of lines with the appropiate starting tiles at the zero index of each line
        lines_to_merge = []
        length_of_lines = max(abs(OFFSETS[direction][0]*self._grid_height),abs(OFFSETS[direction][1]*self._grid_width))
        
        for tile in self._starting_tiles[direction]:
            lines_to_merge.append(self.__path_through_grid__(tile,OFFSETS[direction],length_of_lines))
            
        
        # Merge the lines
        merged_lines = []
        for line in lines_to_merge:
            merged_line = merge(line)
            if not merged_line == line:
                moved = True
            merged_lines.append(merged_line)
        
        # If there was movement, reconstruct the grid with the merged lines
        if moved:
            for index in range(len(merged_lines)):
                self.__set_values_on_path__(self._starting_tiles[direction][index],OFFSETS[direction],merged_lines[index])	
            self.new_tile()	
        
    def __num_empty_tiles__(self):
        """
        Computes the number of empty tiles in the grid
        """
        empty_tiles = 0
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._grid[row][col] == 0:
                    empty_tiles += 1
        
        return empty_tiles

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        import random
        # Determine which empty tile to add the new tile at
        empty_tile = random.randint(1,self.__num_empty_tiles__())
        
        empty_tile_numbering = 0
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._grid[row][col] == 0:
                    empty_tile_numbering += 1
                    if empty_tile_numbering == empty_tile:
                        empty_tile_row = row
                        empty_tile_col = col
                        break
                
        # Determine whether the new tile will be a 2 or a 4
        
        if random.random() >= 0.9:
            self._grid[empty_tile_row][empty_tile_col] = 4
        else:
            self._grid[empty_tile_row][empty_tile_col] = 2		

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]
    
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))