

class Grid:
    def __init__(self, grid: list[list[str]]) -> None:
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    def __iter__(self):
        class GridIter:
            def __init__(self, grid):
                self.grid = grid
                self.x = 0
                self.y = 0

            def __next__(self):
                if self.y == self.grid.height:
                    raise StopIteration
                else:
                    self.x += 1
                    if self.x == self.grid.width:
                        self.x = 0
                        self.y += 1
                    return self.grid.grid[self.y][self.x]
        return GridIter(self)

def process1(input: list[str]) -> int:
    grid = Grid([list(line) for line in input])
    print(grid)
    for x in grid:
        print(x)
    return 0

if __name__ == '__main__':
    import sys
    input = sys.stdin.read()
    print("Part1: ", process1(input.splitlines()))
    #print("Part2: ", process2(input))