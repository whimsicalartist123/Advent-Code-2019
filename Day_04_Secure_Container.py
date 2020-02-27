from math import log
from collections import Counter

def get_digits(num):
    digits = []
    l = int(log(num, 10))+1
    for _ in range(l):
        digits.append(num % 10)
        num = num // 10
    return list(reversed(digits))

def is_increasing(digits):
    for (x, y) in zip(digits, digits[1:]):
        if y < x:
            return False
    return True

def has_adjacent(digits):
    for (x, y) in zip(digits, digits[1:]):
        if y == x:
            return True
    return False

min_num = 108457 
max_num = 562041

part1 = []
part2 = []
for num in range(min_num+1, max_num):
    digits = get_digits(num)
    counts = Counter(digits)
    if has_adjacent(digits) and is_increasing(digits):
        part1.append(num)
    if is_increasing(digits) and has_adjacent(digits) and any(c==2 for _, c in counts.items()):
        part2.append(num)
    
print(len(part1))
print(len(part2))
