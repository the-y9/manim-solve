from manim.utils.color import *

TITLE_FONT_SIZE = 60
STEP_FONT_SIZE = 54

MODE = "l"
if MODE == "l":
    BGCOL = WHITE
    QCOLOR = BLACK
    COMMENT_COLOR = BLACK
    STEP_COLOR = BLUE_E
    ANS_COLOR = RED_E
else:
    BGCOL = BLACK
    QCOLOR = YELLOW
    COMMENT_COLOR = YELLOW
    STEP_COLOR = WHITE
    ANS_COLOR = GREEN

question = r"""
\begin{array}{c}
x > -1 
\\
\\
y = x + \dfrac{1}{x+1} + 2, 
\\
\\
y_{\min} =  ?
\end{array}
"""

steps = [
    (r"\text{Given } y = x + \dfrac{1}{x+1} + 2, \quad x > -1", COMMENT_COLOR),
    (r"\text{To find the minimum value of } y,", COMMENT_COLOR),
    (r"\text{ we differentiate } y \text{ with respect to } x.", COMMENT_COLOR),
    (r"\dfrac{dy}{dx} = 1 - \dfrac{1}{(x+1)^2}", STEP_COLOR),
    (r"\text{Set } \dfrac{dy}{dx} = 0 \Rightarrow 1 - \dfrac{1}{(x+1)^2} = 0", STEP_COLOR),
    (r"(x+1)^2 = 1", STEP_COLOR),
    (r"x + 1 = \pm 1", STEP_COLOR),
    (r"\text{Since } x > -1,", COMMENT_COLOR),
    (r"x+1 > 0 \Rightarrow x+1 = 1", STEP_COLOR),
    (r"x = 0", STEP_COLOR),
    (r"\text{Check second derivative: }", COMMENT_COLOR),
    (r"\dfrac{d^2y}{dx^2} = \dfrac{2}{(x+1)^3}", STEP_COLOR),
    (r"\dfrac{d^2y}{dx^2}_{x=0} = 2 > 0 \Rightarrow \text{Minimum}", COMMENT_COLOR),
    (r"\therefore y_{\min} = 0 + \dfrac{1}{1} + 2", STEP_COLOR),
    (r"y_{\min} = 3", ANS_COLOR),
]

problem = (question, QCOLOR)
