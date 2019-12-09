from collections import Counter

def check_part1(i: int) -> bool:
    s = str(i)
    return all(i <= j for i, j in zip(s,s[1:])) and (max(Counter(s).values()) >= 2)

def check_part2(i: int) -> bool:
    s = str(i)
    return all(i <= j for i, j in zip(s,s[1:])) and (2 in Counter(s).values())

print(sum(check_part1(i) for i in range(156218,652527+1)))
print(sum(check_part2(i) for i in range(156218,652527+1)))