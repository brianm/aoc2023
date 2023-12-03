import sys
from parsimonious import Grammar, NodeVisitor

grammar = Grammar(
    r"""
    game    = gameId ws ":" ws (draw ";"? ws)+ 
    gameId  = "Game" ws number
    draw    = (marbles ","? ws)+ 
    marbles = number ws color ws
    number  = ("0"/"1"/"2"/"3"/"4"/"5"/"6"/"7"/"8"/"9")+
    color   = "red" / "blue" / "green" / "yellow"
    ws      = ~"\\s*"
    """
)

class Part1Visitor(NodeVisitor):
    def visit_game(self, node, visited_children):        
        game_id, _, _, _, draws = visited_children              
        draws = [draw for draw, _, _ in draws]            
        return game_id, draws
    
    def visit_gameId(self, node, visited_children):
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

    def visit_ws(self, node, visited_children):
        return None
    
    def generic_visit(self, node, visited_children):
        return visited_children 

def part1(data: str) -> int:
    def possible(game) -> bool:
        """
        [
            [(6, 'red'), (1, 'blue'), (3, 'green')], 
            [(2, 'blue'), (1, 'red'), (2, 'green')]
        ]
        """
        top = {
            'red':0,
            'green':0,
            'blue':0,         
        }
        for draw in game:
            for count, color in draw:                
                if count > top[color]:
                    top[color] = count

        if top['red'] <= 12 and top['blue'] <= 14 and top['green'] <= 13:
            return True
        return False
    
    sum = 0
    for line in data.splitlines():
        v = Part1Visitor()
        tree = grammar.parse(line)
        game = v.visit(tree)
        if possible(game[1]):
            sum += game[0]
    return sum


if __name__ == '__main__':    
    input = sys.stdin.read()
    print("part 1", part1(input))