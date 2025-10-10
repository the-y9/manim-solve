from manim import *
import manim.utils.color.manim_colors as Colors
from manim import Color, Scene, Square, Text, VGroup, DOWN, RIGHT, WHITE

class ShowAllShades(Scene):
    def construct(self):
        # Get all uppercase color attributes which are Color instances
        color_shades = [
            (name, getattr(Colors, name))
            for name in dir(Colors)
            if name.isupper() and isinstance(getattr(Colors, name), Color)
        ]
        color_shades.sort(key=lambda x: x[0])  # Sort by name

        colors_per_column = 15
        column_spacing = 5
        row_spacing = 0.8
        square_size = 0.5

        columns = []
        for col_idx in range((len(color_shades) + colors_per_column - 1) // colors_per_column):
            group = VGroup()
            for row_idx in range(colors_per_column):
                idx = col_idx * colors_per_column + row_idx
                if idx >= len(color_shades):
                    break
                name, color = color_shades[idx]
                square = Square(side_length=square_size, stroke_color=WHITE, fill_color=color, fill_opacity=1)
                label = Text(name, font_size=20).next_to(square, RIGHT, buff=0.2)
                item = VGroup(square, label).arrange(RIGHT)
                item.shift(DOWN * row_idx * row_spacing)
                group.add(item)
            group.arrange(DOWN, aligned_edge=LEFT)
            group.shift(RIGHT * col_idx * column_spacing)
            columns.append(group)

        final = VGroup(*columns)
        final.to_edge(UP, buff=1)
        self.play(FadeIn(final))
        self.wait(4)

if __name__ == "__main__":
    # Configure render settings
    config.output_file = "solve"  # output file name (without extension)
    qlty = ["low_quality", "medium_quality", "high_quality", "fourk_quality"]
    qlt_index = 2
    config.quality = qlty[qlt_index]   
    config.preview = True               # Automatically open video when done

    # Instantiate and render the scene
    scene = ShowAllShades()
    scene.render()