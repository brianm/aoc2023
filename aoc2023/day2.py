import sys
import re
from parsimonious import Grammar

grammar = Grammar(
    r"""
    game = GameId ws ":" ws (draw ";"? ws)+ 
    GameId = "Game" ws ~"[0-9]+"        
    draw = (marbles ","? ws)+ 
    marbles = number ws color ws
    number = ("0"/"1"/"2"/"3"/"4"/"5"/"6"/"7"/"8"/"9")+
    color = "red" / "blue" / "green" / "yellow"
    ws          = ~"\\s*"
    """
)

def part1(data: str) -> int:
    for line in data.splitlines():
        print(line)
        match = grammar.parse(line)        
        print(match)
    return 0


if __name__ == '__main__':    
    input = sys.stdin.read()
    part1(input)