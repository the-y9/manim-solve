from manim.utils.color import *

TITLE_FONT_SIZE = 54
STEP_FONT_SIZE = 48

BGCOL = BLACK
qcolor = YELLOW

question = r"""
\begin{array}{c}
\lim_{n \to \infty} \dfrac{1^k + 2^k + 3^k + \cdots + n^k}{n^{k+1}} = \ ?
\\
\\
\text{if, } k \ge 1
\end{array}
"""

steps = [
    (r"\lim_{n \to \infty} \frac{1^k + 2^k + \cdots + n^k}{n^{k+1}}", YELLOW),
    (r"\text{Recall the sum of powers: }", YELLOW),
    (r"1^k + 2^k + \cdots + n^k", WHITE),
    (r"\approx \frac{n^{k+1}}{k+1} + \frac{n^k}{2} + \dots", WHITE),
    (r"\text{Divide both sides by } n^{k+1}", YELLOW),
    (r"\Rightarrow \frac{1^k + 2^k + \cdots + n^k}{n^{k+1}}", WHITE),
    (r"\approx \frac{1}{k+1} + \frac{1}{2n} + \dots", WHITE),
    (r"\text{As } n \to \infty, \frac{1}{2n} \to 0", WHITE),
    (r"\text{Hence, } = \frac{1}{k+1}", GREEN),
]

problem = (question, qcolor)
