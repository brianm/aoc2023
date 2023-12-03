import sys
from parsimonious import Grammar, NodeVisitor

grammar = Grammar(
    r"""
    game    = game_id ws ":" ws (draw ";"? ws)+ 
    game_id  = "Game" ws number
    draw    = (marbles ","? ws)+ 
    marbles = number ws color ws
    number  = ~"\\d+"
    color   = "red" / "blue" / "green" / "yellow"
    ws      = ~"\\s*"
    """
)

class GameVisitor(NodeVisitor):
    def visit_game(self, node, visited_children):        
        game_id, _, _, _, draws = visited_children        
        return game_id, [draw for draw, _, _ in draws]        
    
    def visit_game_id(self, node, visited_children):
        _, _, game_id = visited_children
        return int(game_id)
    
    def visit_draw(self, node, visited_children):        
        return [draw for draw, _, _ in visited_children]
    
    def visit_marbles(self, node, visited_children):
        num, _, color, _= visited_children        
        return (num, color)

    def visit_number(self, node, visited_children):
        return int(node.text)

    def visit_color(self, node, visited_children):        
        return node.text
    
    def generic_visit(self, node, visited_children):
        return visited_children 

visitor = GameVisitor()

def part1(data: str) -> int:
    def possible(game) -> bool:
        top = top = {'red':0, 'green':0, 'blue':0,}
        for draw in game:
            for count, color in draw:                
                if count > top[color]:
                    top[color] = count

        return top['red'] <= 12 and top['blue'] <= 14 and top['green'] <= 13
    
    sum = 0
    for game in [visitor.visit(grammar.parse(line)) for line in data.splitlines()]:
        if possible(game[1]):
            sum += game[0]
    return sum

def part2(data: str) -> int:
    def power(game) -> int:
        top = {'red':0, 'green':0, 'blue':0,}
        for draw in game:
            for count, color in draw:                
                if count > top[color]:
                    top[color] = count

        return top['red'] * top['blue'] * top['green']
    
    sum = 0
    for line in data.splitlines():
        v = GameVisitor()
        tree = grammar.parse(line)
        game = v.visit(tree)
        sum += power(game[1])        
    return sum

if __name__ == '__main__':    
    input = sys.stdin.read()
    print("part 1", part1(input))
    print("part 2", part2(input))