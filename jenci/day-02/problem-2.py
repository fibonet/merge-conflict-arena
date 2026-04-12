# Tököli Jenő-Richard
# Problem - Day 2: I Was Told There Would Be No Math
# Solution based on the current project setup (directory/file structure)

# Part 1: Based on the formula given in the exercise
# Part 2: perimeter of the smallest side and added volume

import math

total_paper = 0
total_ribbon = 0

# Input & Calculations for both solutions
with open("input.txt","r") as f:
    for line in f:
        l, w, h = map(int, line.strip().split('x'))
        # Store multiplied sides, rectangle areas
        sides = [l*w, w*h, h*l]
        # Formula for calculating wrapping paper: 2 * (lw + wh + hl) + min(lw, wh, hl)
        total_paper += 2 * sum(sides) + min(sides)

        # Store dimensions for formula simplification
        dimensions = [l, w, h]
        dimensions.sort()
        # Formula for calculation ribbon length: 2 * (sorted dimensions last 2 / smallest perimeter) + volume
        total_ribbon += 2 * sum(dimensions[:2]) + math.prod(dimensions)

# Print results
print(total_paper)
print(total_ribbon)