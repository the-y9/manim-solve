from manim import *

class Solve(Scene):
    def construct(self):
        # Draw square ABCD
        square = Square(side_length=3)
        square.shift(UP)  # Shift square up for visibility
        self.play(Create(square))
        self.wait(0.5)

        # Get corners A, B, C, D of the square
        A = square.get_corner(DOWN + LEFT)
        B = square.get_corner(DOWN + RIGHT)
        C = square.get_corner(UP + RIGHT)
        D = square.get_corner(UP + LEFT)

        # Draw and label corners
        dots = [
            Dot(A), Dot(B), Dot(C), Dot(D)
        ]
        labels = [
            MathTex("A").next_to(A, DOWN + LEFT, buff=0.2),
            MathTex("B").next_to(B, DOWN + RIGHT, buff=0.2),
            MathTex("C").next_to(C, UP + RIGHT, buff=0.2),
            MathTex("D").next_to(D, UP + LEFT, buff=0.2),
        ]

        for dot, label in zip(dots, labels):
            self.play(FadeIn(dot), Write(label))

        self.wait(0.5)

        # Define points P, Q on AB and R on CD
        p_ratio = 0.3
        q_ratio = 0.7
        r_ratio = 0.5

        P = interpolate(A, B, p_ratio)
        Q = interpolate(A, B, q_ratio)
        R = interpolate(C, D, r_ratio)

        # Draw points P, Q, R
        point_P = Dot(P, color=YELLOW)
        point_Q = Dot(Q, color=YELLOW)
        point_R = Dot(R, color=YELLOW)

        label_P = MathTex("P").next_to(P, DOWN, buff=0.2)
        label_Q = MathTex("Q").next_to(Q, DOWN, buff=0.2)
        label_R = MathTex("R").next_to(R, UP, buff=0.2)

        self.play(FadeIn(point_P), Write(label_P))
        self.play(FadeIn(point_Q), Write(label_Q))
        self.play(FadeIn(point_R), Write(label_R))
        self.wait(0.5)

        # Draw triangle PQR
        triangle = Polygon(P, Q, R, color=BLUE, stroke_width=3)
        self.play(Create(triangle))
        self.wait(2)

        # Optionally show a title
        title = MathTex(r"\text{Square } ABCD \text{ with } P, Q \in AB, R \in CD", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(3)
