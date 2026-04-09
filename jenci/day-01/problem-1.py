# Tököli Jenő-Richard
# Problem - Day 1: Not Quite Lisp
# Solution based on current project setup (directory/file structure)

with open("input.txt", "r") as f:
    s = f.read().strip()

# Solution for part 1
print(s.count('(') - s.count(')'))

# Solution for part 2
# st: story of the building
# sc: step counter

st = 0
sc = 0

for ch in s:
    sc += 1
    if ch == '(':
        st += 1
    if ch == ')':
        st -= 1
    if st < 0:
        break

print(sc)