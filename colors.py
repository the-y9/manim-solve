from manim import *
import manim.utils.color.manim_colors as Colors

class ColorsOverview(Scene):
    def construct(self):
        # Define a helper to create groups of colored lines
        def color_group(color):
            subnames = [color + "_" + c for c in "abcde"]
            group = VGroup(
                *[
                    Line(ORIGIN, RIGHT * 1.5, stroke_width=35, color=getattr(Colors, name.upper()))
                    for name in subnames
                ]
            ).arrange(DOWN, buff=0.4)
            label = Text(color).scale(0.6).next_to(group, UP, buff=0.3)
            group.add(label)
            return group

        # Create color groups for some base colors
        base_colors = ["blue", "teal", "green", "yellow", "gold", "red", "maroon", "purple"]
        color_groups = VGroup(*[color_group(color) for color in base_colors])

        color_groups.arrange_in_grid(rows=2, cols=4, buff=1.0)

        self.add(color_groups)
        
        self.wait()


if __name__ == "__main__":
    config.output_file = "colors"  # output file name (without extension)
    qlty = ["low_quality", "medium_quality", "high_quality", "fourk_quality"]
    qlt_index = 2
    config.quality = qlty[qlt_index]
    config.media_format = "png"    
    config.preview = True               # Automatically open video when done

    # Instantiate and render the scene
    scene = ColorsOverview()
    scene.render()
