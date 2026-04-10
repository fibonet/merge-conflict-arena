# Tököli Jenő-Richard
# Problem - Day 2: I Was Told There Would Be No Math
# Solution based on current project setup (directory/file structure)

total = 0

with open("input.txt","r") as f:
    for line in f:
        l, w, h = map(int, line.strip().split('x'))
        # Store multiplied sides, rectangle areas
        sides = [l*w, w*h, h*l]
        # Formula for calculating: 2 * (lw + wh + hl) + min(lw, wh, hl)
        total += 2 * sum(sides) + min(sides)

print(total)