from manim import *
from steps import steps, problem

class Solve(Scene):
    def construct(self):
        title = MathTex(problem, font_size=60, color=BLUE)

        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeOut(title), title.animate.to_edge(UP))
        self.wait(0.5)


        group = VGroup()  # Group for all steps
        max_height = config.frame_height * 0.60

        for i, (latex_str, color) in enumerate(steps):
            step = MathTex(latex_str, font_size=48, color=color)
            if step.width > 12:
                step.scale_to_fit_width(12)

            # Check if group height exceeds 60% of screen
            if group.get_height() > max_height:
                # Shift the entire group up by height of one step + buffer
                if i % 4 ==0:
                    dynamic_shift = 1
                else:
                    dynamic_shift = 0.6
                shift_amount = step.height + dynamic_shift
                self.play(group.animate.shift(UP * shift_amount))

            if i == 0:
                # place below title initially
                step.to_edge(UP, buff=1)
            else:
                # place below the last step
                step.next_to(group[-1], DOWN, buff=0.6)

            group.add(step)
            self.play(Write(step), run_time=0.08*len(latex_str))
            self.wait(1)
        
        # Box ONLY the last step
        box = SurroundingRectangle(group[-1], color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(3)

if __name__ == "__main__":
    # Configure render settings
    config.output_file = "solve"  # output file name (without extension)
    qlty = ["low_quality", "medium_quality", "high_quality", "fourk_quality"]
    qlt_index = 2
    config.quality = qlty[qlt_index]   
    config.preview = True               # Automatically open video when done

    # Instantiate and render the scene
    scene = Solve()
    scene.render()