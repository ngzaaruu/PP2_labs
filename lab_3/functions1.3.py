def solve(numheads, numlegs):
    
    # numheads = x + y
    # numlegs = 2x + 4y
    
    for chicken in range(numheads + 1):
        rabbits = numheads - chicken
        if 2 * chicken + 4 * rabbits == numlegs:
            return chicken, rabbits
    return "Error"

numheads = 35
numlegs = 94

chicken, rabbits = solve(numheads, numlegs)
print(chicken, rabbits)
