from manim import *
from datetime import datetime
from steps import steps, problem, BGCOL, TITLE_FONT_SIZE, STEP_FONT_SIZE

class Solve(Scene):
    def construct(self):
        # self.add_sound("songs/fall.mp3", time_offset=0)

        title = MathTex(problem[0], font_size=TITLE_FONT_SIZE, color=problem[1])

        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeOut(title), title.animate.to_edge(UP))
        self.wait(0.5)


        group = VGroup()  # Group for all steps
        max_height = config.frame_height * 0.60

        for i, (latex_str, color) in enumerate(steps):
            step = MathTex(latex_str, font_size=STEP_FONT_SIZE, color=color)
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
            rrun = 0.08 *len(latex_str)
            prun = min(2, rrun)
            self.play(Write(step), run_time=prun)
            self.wait(1.5)
        
        # Box ONLY the last step
        box = SurroundingRectangle(group[-1], color=color, buff=0.3)
        self.play(Create(box))
        self.wait(3)




def apply_config(qlt_index: int = 2, preset: str = "v"):
    qlty = ["low_quality", "medium_quality", "high_quality", "fourk_quality"]
    
    BASE_CONFIG = {
        "background_color": BGCOL,
        "quality": qlty[qlt_index],
        "preview": True,
    }

    now_str = datetime.now().strftime("%Y%m%d_%H%M%S")

    RENDER_PRESETS = {
        "v": {
            **BASE_CONFIG,
            "frame_width": 16,
            "frame_height": 9,
            "pixel_width": 1920,
            "pixel_height": 1080,
            "output_file": f"vid_{now_str}",
        },
        "s": {
            **BASE_CONFIG,
            "frame_width": 9,
            "frame_height": 16,
            "pixel_width": 1080,
            "pixel_height": 1920,
            "output_file": f"short_{now_str}",
        }
    }
    cfg = RENDER_PRESETS.get(preset)
    if not cfg:
        raise ValueError(f"Unknown preset '{preset}'")

    for key, value in cfg.items():
        setattr(config, key, value)


if __name__ == "__main__":
    apply_config(2, "s")
    scene = Solve()
    scene.render()