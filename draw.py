from manim import *

# ---- Create a prism from two quadrilaterals ----
def create_irregular_prism(base1, base2, color=BLUE_E, fill_opacity=0.6):
    # Create faces
    faces = []
    n = len(base1)

    # Create side faces
    for i in range(n):
        p1 = base1[i]
        p2 = base1[(i + 1) % n]
        p3 = base2[(i + 1) % n]
        p4 = base2[i]
        face = Polygon(p1, p2, p3, p4, fill_opacity=fill_opacity, color=color)
        faces.append(face)

    # Create top and bottom faces
    top = Polygon(*base2, fill_opacity=fill_opacity, color=color)
    bottom = Polygon(*base1, fill_opacity=fill_opacity, color=color)

    return VGroup(*faces, top, bottom)

# ---- Scene ----
class IrregularPrismVolume(ThreeDScene):
    def construct(self):
        # Set camera angle
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

        # Base face (square): 5x5
        base1 = [
            [0, 0, 0],
            [5, 0, 0],
            [5, 5, 0],
            [0, 5, 0],
        ]

        # Top face (rectangle): 5x7, offset in Z
        height = 5
        base2 = [
            [0, 0, height],
            [5, 0, height],
            [5, 7, height],
            [0, 7, height],
        ]

        # Create the prism
        prism = create_irregular_prism(base1, base2, color=TEAL, fill_opacity=0.5)
        self.add(ThreeDAxes())
        self.play(FadeIn(prism))
        self.wait(1)

        # Display volume formula
        volume_text = MathTex(
            r"\text{Volume} = \frac{1}{2} (A_1 + A_2) \cdot h",
            r"= \frac{1}{2} (25 + 35) \cdot 5",
            r"= 150",
        ).scale(0.6).to_corner(UL)
        for part in volume_text:
            self.play(Write(part))
            self.wait(0.5)

        self.wait(2)

if __name__ == "__main__":
    config.output_file = "draw"  # output file name (without extension)
    qlty = ["low_quality", "medium_quality", "high_quality", "fourk_quality"]
    qlt_index = 2
    config.quality = qlty[qlt_index]   
    config.preview = True               # Automatically open video when done

    scene = IrregularPrismVolume()
    scene.render()
