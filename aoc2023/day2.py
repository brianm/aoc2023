from collections.abc import Sequence
import sys
import re
from parsimonious import Grammar, NodeVisitor

grammar = Grammar(
    r"""
    game = gameId ws ":" ws (draw ";"? ws)+ 
    gameId = "Game" ws ~"[0-9]+"        
    draw = (marbles ","? ws)+ 
    marbles = number ws color ws
    number = ("0"/"1"/"2"/"3"/"4"/"5"/"6"/"7"/"8"/"9")+
    color = "red" / "blue" / "green" / "yellow"
    ws          = ~"\\s*"
    """
)

class Part1Visitor(NodeVisitor):
    def visit_game(self, node, visited_children):        
        game_id, _, _, _, draws = visited_children              
        draws = [draw for draw, _, _ in draws]            
        return game_id, draws
    
    def visit_gameId(self, node, visited_children):
        return node.text
    
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
    for line in data.splitlines():
        v = Part1Visitor()
        tree = grammar.parse(line)
        game = v.visit(tree)
        print(game)
    return 0


if __name__ == '__main__':    
    input = sys.stdin.read()
    part1(input)