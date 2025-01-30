def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    return x, y

num_chickens, num_rabbits = solve(35, 94)
print(f"Chickens: {num_chickens}, Rabbits: {num_rabbits}")
