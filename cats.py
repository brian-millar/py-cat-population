def nextGen(start, litterSize, gens):
    if (gens == 0):
        return 0
    return start + nextGen(start * litterSize, litterSize, gens - 1)

print(nextGen(int(input("Starting Cats: ")), int(input("Litter Size: ")), int(input("Generations: "))))
