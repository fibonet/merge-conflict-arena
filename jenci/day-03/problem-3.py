# Tököli Jenő-Richard
# Problem - Day 3: Perfectly Spherical Houses in a Vacuum
# Solution based on current project setup (directory/file structure)

# Single-line input with a custom trailing character: #
with open("input.txt", "r") as f:
    s = f.read().strip()

# Create a set to store visited coordinates
coords = [(0,0)]
already_visited = {coords[0]}

# Iterate through the input string
for ch in s:
    if ch == '^':
        coords[0] = (coords[0][0], coords[0][1] + 1)
    if ch == 'v':
        coords[0] = (coords[0][0], coords[0][1] - 1)
    if ch == '>':
        coords[0] = (coords[0][0] + 1, coords[0][1])
    if ch == '<':
        coords[0] = (coords[0][0] - 1, coords[0][1])
    if coords[0] not in already_visited:
        already_visited.add(coords[0])

# Print the number of unique coordinates visited
print(len(already_visited))
