from manim.utils.color import *

qcolor = YELLOW

question = r"(2^n + 1) \text{ is never divisible by } 7 \ \text{!}"

steps = [
    (r"\text{Let's assume: } 2^n + 1 \text{ to be a multiple of 7}", WHITE),
    (r"\text{Then } 2^n \text{ must leave a remainder of 6 when divided by 7}", WHITE),
    (r"\text{Trying different powers of 2}", YELLOW),
    (r"2^1 = 2, \quad 2 \div 7 \text{ leaves remainder } 2", WHITE),
    (r"2^2 = 4, \quad 4 \div 7 \text{ leaves remainder } 4", WHITE),
    (r"2^3 = 8, \quad 8 \div 7 \text{ leaves remainder } 1", WHITE),
    (r"2^4 = 16,\quad 16 \div 7 \text{ leaves remainder } 2", WHITE),
    (r"2^5 = 32,\quad 32 \div 7 \text{ leaves remainder } 4", WHITE),
    (r"2^6 = 64,\quad 64 \div 7 \text{ leaves remainder } 1", WHITE),
    (r"\text{We see a pattern in the remainders: } 2,\ 4,\ 1,\ 2,\ 4,\ 1,\ \dots", YELLOW),
    (r"\text{It keeps repeating and never gives remainder 6}", WHITE),
    (r"\text{Our assumption is contradicted}", WHITE),
    (r"\text{So } 2^n + 1 \text{ can never be a multiple of 7}", GREEN),
]


problem = (question, qcolor)
