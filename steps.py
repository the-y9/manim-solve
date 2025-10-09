from manim.utils.color import *

problem = r"\sqrt{x+\sqrt{2x-1}}+\sqrt{x-\sqrt{2x-1}}=2" + r"\\" + r"x =\ ?" + r"\ ;" + r"x > 0"

steps = [
    (r"\sqrt{x+\sqrt{2x-1}}+\sqrt{x-\sqrt{2x-1}}=2", YELLOW),
    (r"\text{Squaring both sides:}", BLUE),
    (r"\because\ (a + b)^2 = a^2 + b^2 + 2ab", BLUE),
    (r"(x + \sqrt{2x - 1}) + (x - \sqrt{2x - 1}) + 2\sqrt{(x + \sqrt{2x - 1})(x - \sqrt{2x - 1})} = 4", WHITE),
    (r"2x + 2\sqrt{(x + \sqrt{2x - 1})(x - \sqrt{2x - 1})} = 4", WHITE),
    (r"2x + 2\sqrt{x^2 - (2x - 1)} = 4", WHITE),
    (r"2x + 2\sqrt{x^2 - 2x + 1} = 4", WHITE),
    (r"2x + 2\sqrt{(x - 1)^2} = 4", WHITE),
    (r"2x + 2|x - 1| = 4", WHITE),
    (r"\because\ x > 0,\ |x - 1| = x - 1", BLUE),
    (r"2x + 2(x - 1) = 4", WHITE),
    (r"2x + 2x - 2 = 4", WHITE),
    (r"4x = 6", WHITE),
    (r"x = \dfrac{3}{2}", GREEN),
]
