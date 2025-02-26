num_heads = 35
num_legs = 94

# rabbits = x; chicken = y
# x + y = 35 
# 4x + 2y = 94

def solve(num_heads, num_legs):
    rabbits = (num_legs - 2 * num_heads) // 2
    chickens = num_heads - rabbits
    
    return chickens, rabbits

res = solve(num_heads, num_legs)
print(f"Chickens: {res[0]}, Rabbits: {res[1]} ")
