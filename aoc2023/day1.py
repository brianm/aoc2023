import re

def digits(line) -> tuple[int, int]:
    digits = [c for c in line if c.isdigit()]        
    return digits[0], digits[-1]

def process(data) -> int:    
    count = 0    
    for line in data.splitlines():
        one, two = digits(line)
        count += int(one+two)
    return count

def process2(data) -> tuple[int, int]:
    sum1 = 0
    sum2 = 0
    for line in data.splitlines():
        f1, l1 = doline1(line)
        f2, l2 = doline2(line)

        if (f1 != f2) or (l1 != l2):
            print("mismatch: ", line, f1, l1, f2, l2)

        sum1 += (10*f1)+l1
        sum2 += (10*f2)+l2

    return sum1, sum2

def doline1(line) -> tuple[int, int]:
    values = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
            'six':6, 'seven': 7, 'eight': 8, 'nine':9}

    regex = re.compile(r'(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))')
    parts = regex.findall(line)
    
    first = parts[0]
    last = parts[-1]

    if first.isdigit():
        first = int(first)
    else:
        first = values[first]
    if last.isdigit():
        last = int(last)
    else:
        last = values[last]
    return first,last

def doline2(line) -> tuple[int, int]:
    line = line.replace("zero", "zero0zero")
    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three")
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eight8eight")
    line = line.replace("nine", "nine9nine")
    first, last = digits(line)
    return int(first),int(last)

if __name__ == '__main__':
    import sys
    input = sys.stdin.read()
    print("Part1: ", process(input))    
    print("Part2: ", process2(input))    