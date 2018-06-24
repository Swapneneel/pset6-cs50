# mario less generate one column
from cs50 import get_int

h = get_int("Height of pyramid: ")
if h > 23 or h < 0:
    while h > 23 or h < 0:
        h = get_int("Retry: ")

for i in range(h):
    for j in range(h - i - 1):
        print(" ", end="")  # end is for to write in same line in Py3
    for k in range(i + 2):
        print("#", end="")
    print("")