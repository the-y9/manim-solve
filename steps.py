from manim.utils.color import *

qcolor = YELLOW

question = r"\sum_{k = 0}^\infty \left\lfloor \frac{n + 2^k}{2^{k+1}} \right\rfloor = \text{ ?}"

steps = [
    (r"\text{Let, } \left\lfloor \frac{n + 2^k}{2^{k+1}} \right\rfloor \text{ be } S", WHITE),
    (r"S = \sum_{k = 0}^\infty \left\lfloor \frac{n + 2^k}{2^{k+1}} \right\rfloor = \left\lfloor \frac{n + 2^0}{2^{0+1}}\right\rfloor + \left\lfloor \frac{n + 2^1}{2^{1+1}}\right\rfloor + \left\lfloor \frac{n + 2^2}{2^{2+1}}\right\rfloor + \left\lfloor \frac{n + 2^3}{2^{3+1}}\right\rfloor + \cdots", WHITE),
    (r"S = \left\lfloor \frac{n + 1}{2}\right\rfloor + \left\lfloor \frac{n + 2}{4}\right\rfloor + \left\lfloor \frac{n + 4}{8}\right\rfloor + \left\lfloor \frac{n + 8}{16}\right\rfloor + \cdots", WHITE),
    (r"S = \left\lfloor \left(\frac{n}{2} + \frac{1}{2}\right) \right\rfloor + \left\lfloor \left(\frac{n}{4} + \frac{1}{2}\right) \right\rfloor + \left\lfloor \left(\frac{n}{8} + \frac{1}{2}\right) \right\rfloor + \left\lfloor \left(\frac{n}{16} + \frac{1}{2}\right) \right\rfloor + \cdots", WHITE),
    (r"\because \text{ it's a floor function, we omit } \frac{1}{2}", YELLOW),
    (r"S = \frac{n}{2} + \frac{n}{4} + \frac{n}{8} + \frac{n}{16} + \cdots", WHITE),
    (r"\text{Multiplying both sides by } 2", YELLOW),
    (r"2S = n + \frac{n}{2} + \frac{n}{4} + \frac{n}{8} + \cdots", WHITE),
    (r"2S - S = \left(n + \frac{n}{2} + \frac{n}{4} + \cdots\right) - \left(\frac{n}{2} + \frac{n}{4} + \frac{n}{8} + \cdots\right)", WHITE),
    (r"S = n", GREEN),
    (r"\text{But since we used } \lfloor x + 1/2 \rfloor, \text{ the floor pulls it down slightly}", YELLOW),
    (r"\text{Still, adding all the rounded values gives exactly } n", YELLOW),
    (r"\sum_{k = 0}^\infty \left\lfloor \frac{n + 2^k}{2^{k+1}} \right\rfloor = n", GREEN),
]

problem = (question, qcolor)
