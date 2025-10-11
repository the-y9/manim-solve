from manim.utils.color import *

qcolor = BLACK

question = r"""
\begin{array}{c}
\text{Product of solutions of:} \\
\\
e^{5(\ln x)^2 + 3} = x^8 \text{, for } x > 0
\end{array}
"""
steps = [
    (r"e^{5(\ln x)^2 + 3} = x^8 \text{, for } x > 0", BLACK),
    (r"\text{Take natural logarithm on both sides:}", BLUE_E),
    (r"\ln\left(e^{5(\ln x)^2 + 3}\right) = \ln(x^8)", BLUE_E),
    (r"(5(\ln x)^2 + 3)\ln(e) = 8 \ln x", BLUE_E),
    (r"\ln(e) = 1, \text{Let } y = \ln x", BLACK),
    (r"\Rightarrow 5y^2 + 3 = 8y", BLUE_E),
    (r"\Rightarrow 5y^2 - 8y + 3 = 0", BLUE_E),
    (r"\text{Using quadratic formula: } y = \frac{8 \pm \sqrt{(-8)^2 - 4 \cdot 5 \cdot 3}}{2 \cdot 5}", BLUE_E),
    (r"= \frac{8 \pm \sqrt{64 - 60}}{10} = \frac{8 \pm \sqrt{4}}{10}", BLUE_E),
    (r"= \frac{8 \pm 2}{10} \Rightarrow y = 1 \text{ or } y = \frac{3}{5}", BLUE_E),
    (r"\text{Recall: } y = \ln x \Rightarrow x = e^y", BLACK),
    (r"\Rightarrow x = e^1 = e \quad \text{or} \quad x = e^{3/5}", BLUE_E),
    (r"\text{Product of all solutions: } e \cdot e^{3/5} = e^{1 + 3/5}", BLUE_E),
    (r"= e^{8/5}", RED_E),
]

problem = (question, qcolor)
