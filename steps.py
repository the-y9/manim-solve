from manim.utils.color import *

TITLE_FONT_SIZE = 60
STEP_FONT_SIZE = 48

BGCOL = BLACK
qcolor = YELLOW

question = r"""
\begin{array}{c}
u+v=8; u,v>0
\\
A = 5u^2 + 11v^2
\\
min(A) = ?
\end{array}
"""
steps = [
    (r"u+v = 8, A = 5u^2 + 11v^2", YELLOW),
    (r"v = 8-u \Rightarrow A = 5u^2 + 11(8-u)^2", WHITE),
    (r"\Rightarrow A = 5u^2 + 11(u^2-16u+64)", WHITE),
    (r"\Rightarrow A = 5u^2 + 11u^2-176u+704", WHITE),
    (r"\Rightarrow A = 16u^2 -176u +704", WHITE),

    (r"\text{Differentiation Trick to find min: }", YELLOW),
    (r"\frac{dA}{du} = 32u -176 = 0", WHITE),
    (r"\Rightarrow u = \frac{176}{32} = 5.5", WHITE), 
    (r"\Rightarrow v = 8 - u = 2.5", WHITE),

    (r"\text{Double Check with 2nd Derivative: }", YELLOW),
    (r"\frac{d^2A}{du^2} = 32 > 0 \Rightarrow \text{Min at } u=5.5", WHITE),

    (r"\text{Calculate Minimum of}\ A", YELLOW),
    (r"A_{min} = 5(5.5)^2 + 11(2.5)^2", WHITE),
    (r"= 5(30.25) + 11(6.25) = 151.25 + 68.75", WHITE),
    (r"= 220", GREEN),

]
problem = (question, qcolor)
