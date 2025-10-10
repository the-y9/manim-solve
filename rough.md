from manim import *
from manim.utils.color import COLOR_MAP

class Col(Scene):
    def construct(self):
        # Get all named colors from COLOR_MAP
        colors = list(COLOR_MAP.items())
        colors.sort()  # Sort alphabetically by name

        # Layout settings
        colors_per_column = 15
        column_spacing = 5
        row_spacing = 0.8
        square_size = 0.5

        all_groups = []

        for col_index in range((len(colors) - 1) // colors_per_column + 1):
            group = VGroup()
            for row_index in range(colors_per_column):
                i = col_index * colors_per_column + row_index
                if i >= len(colors):
                    break
                name, hex_color = colors[i]
                color = Color(hex_color)

                # Create a colored square
                square = Square(side_length=square_size, color=WHITE, fill_color=color, fill_opacity=1)
                
                # Add color name
                label = Text(name, font_size=24).next_to(square, RIGHT, buff=0.2)
                
                item = VGroup(square, label)
                item.arrange(RIGHT)
                item.shift(DOWN * row_index)
                group.add(item)

            group.arrange(DOWN, aligned_edge=LEFT)
            group.shift(RIGHT * col_index * column_spacing)
            all_groups.append(group)

        final = VGroup(*all_groups)
        final.to_edge(UP)
        self.play(FadeIn(final))
        self.wait(3)
