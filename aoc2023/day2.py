import sys
from parsimonious import Grammar, NodeVisitor

grammar = Grammar(
    r"""
    game    = game_id (":" _) (draw ";"? _)+ 
    game_id  = "Game" _ number
    draw    = (marbles ","? _)+ 
    marbles = number _ color _
    number  = ("0"/"1"/"2"/"3"/"4"/"5"/"6"/"7"/"8"/"9")+
    color   = "red" / "blue" / "green" / "yellow"
    _   = " "*
    """
)

Marbles = tuple[int, str]
Draw = list[tuple[int, str]]
Game = list[Draw]

class GameVisitor(NodeVisitor):
    def visit_game(self, node, visited_children) -> tuple[int, Game]:
        game_id, _, draws = visited_children        
        return game_id, [draw for draw, _, _ in draws]        
    
    def visit_game_id(self, node, visited_children) -> int:
        _, _, game_id = visited_children
        return int(game_id)
    
    def visit_draw(self, node, visited_children) -> Draw:        
        return [draw for draw, _, _ in visited_children]
    
    def visit_marbles(self, node, visited_children) -> Marbles:
        num, _, color, _= visited_children        
        return (num, color)

    def visit_number(self, node, visited_children) -> int:
        return int(node.text)

    def visit_color(self, node, visited_children) -> str:        
        return node.text
    
    def generic_visit(self, node, visited_children):
        return visited_children 

visitor = GameVisitor()

def part1(data: list[str]) -> int:
    def possible(game: Game) -> bool:
        top = {'red':0, 'green':0, 'blue':0,}
        for draw in game:
            for count, color in draw:                
                if count > top[color]:
                    top[color] = count
        return top['red'] <= 12 and top['blue'] <= 14 and top['green'] <= 13

    sum = 0
    for id, draws in [visitor.visit(grammar.parse(line)) for line in data]:
        if possible(draws):
            sum += id
    return sum

def part2(data: list[str]) -> int:
    def power(game: Game) -> int:
        top = {'red':0, 'green':0, 'blue':0,}
        for draw in game:
            for count, color in draw:                
                if count > top[color]:
                    top[color] = count

        return top['red'] * top['blue'] * top['green']
    
    sum = 0
    for _, draws in [visitor.visit(grammar.parse(line)) for line in data]:
        sum += power(draws)        
    return sum

if __name__ == '__main__':    
    input = sys.stdin.read()
    print("part 1", part1(input.splitlines()))
    print("part 2", part2(input.splitlines()))