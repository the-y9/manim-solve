from manim.utils.color import *

TITLE_FONT_SIZE = 60
STEP_FONT_SIZE = 54

MODE = "l"
if MODE == "d":
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
\sqrt{2 - \sqrt{5}} + \sqrt{2 + \sqrt{5}} = \ ?
\end{array}
"""

steps = [
    (r"\text{Let } x = \sqrt{2 - \sqrt{5}} + \sqrt{2 + \sqrt{5}}", COMMENT_COLOR),
    (r"\text{Square both sides: } x^2 = \left(\sqrt{2 - \sqrt{5}} + \sqrt{2 + \sqrt{5}}\right)^2", STEP_COLOR),
    (r"x^2 = (2 - \sqrt{5}) + (2 + \sqrt{5}) + 2\sqrt{(2 - \sqrt{5})(2 + \sqrt{5})}", STEP_COLOR),
    (r"x^2 = 4 + 2\sqrt{4 - 5}", STEP_COLOR),
    (r"x^2 = 4 + 2\sqrt{-1}", STEP_COLOR),
    (r"\text{Since } \sqrt{-1} = i,", COMMENT_COLOR),
    (r"x^2 = 4 + 2i", STEP_COLOR),
    (r"\text{Now write in polar form: } 4 + 2i = r e^{i\theta}", COMMENT_COLOR),
    (r"r = \sqrt{a^2 + b^2}", COMMENT_COLOR), 
    (r"= \sqrt{4^2 + 2^2} = 2\sqrt{5}", STEP_COLOR),
    (r"\theta = \tan^{-1}\left(\frac{b}{a}\right)", COMMENT_COLOR),
    (r"= \tan^{-1}\left(\frac{2}{4}\right)= \tan^{-1}\left(\frac{1}{2}\right)", STEP_COLOR),
    (r"\text{So, }x = \sqrt{r} \, e^{i\theta}", COMMENT_COLOR),
    (r"x = \sqrt{2\sqrt{5}} \, e^{i \tan^{-1}\left(\frac{2}{4}\right)}", ANS_COLOR),
]

problem = (question, QCOLOR)
