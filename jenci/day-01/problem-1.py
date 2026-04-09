# Tököli Jenő-Richard
# Problem - Day 1: Not Quite Lisp
# Solution based on current project setup (directory/file structure)

with open("input.txt", "r") as f:
    s = f.read().strip()

print(s.count('(') - s.count(')'))
