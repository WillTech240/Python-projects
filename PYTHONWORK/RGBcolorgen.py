import random

def rgb_color_gen():
    r = random.randint(0, 255)  # red
    g = random.randint(0, 255)  # green
    b = random.randint(0, 255)  # blue
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())

