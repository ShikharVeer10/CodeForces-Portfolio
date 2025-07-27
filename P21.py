def decompose_round_numbers(n):
    round_numbers = []
    place_value = 1  

    while n > 0:
        digit = n % 10
        if digit > 0:
            round_numbers.append(digit * place_value)
        n //= 10
        place_value *= 10 

    return round_numbers

def solve():
    t = int(input().strip()) 
    results = []
    
    for _ in range(t):
        n = int(input().strip()) 
        round_numbers = decompose_round_numbers(n)
        results.append(f"{len(round_numbers)} {' '.join(map(str, round_numbers))}")

    print("\n".join(results))

solve()
