# Tököli Jenő-Richard
# Problem - Day 3: Perfectly Spherical Houses in a Vacuum
# Solution based on current project setup (directory/file structure)

# Single-line input with a custom trailing character: #
with open("input.txt", "r") as f:
    s = f.read().strip() + '#'
    # s = f.read().strip().__add__('#')

# total_delivered = 0
# Create a set to store visited coordinates
coords = [(0,0)]
already_visited = set()
# Iterate through the input string
for ch in s:
    if coords[0] not in already_visited:
        already_visited.add(coords[0])
        # total_delivered += 1
    if ch == '^':
        coords[0] = (coords[0][0], coords[0][1] + 1)
    if ch == 'v':
        coords[0] = (coords[0][0], coords[0][1] - 1)
    if ch == '>':
        coords[0] = (coords[0][0] + 1, coords[0][1])
    if ch == '<':
        coords[0] = (coords[0][0] - 1, coords[0][1])
    if ch == '#':
        break

print(len(already_visited))
