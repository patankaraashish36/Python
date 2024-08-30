import textwrap

def wrap(string, max_width):
    wrapped_string = textwrap.fill(string, max_width)
    return wrapped_string

print(wrap("string", 2))


for i in range(3,-1, -1):
    print(i)