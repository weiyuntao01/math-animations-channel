from manim import *
import numpy as np

class FirstAnimation(Scene):
    """First example animation: Sine function transformations"""
    
    def construct(self):
        # Create title
        title = Text("Sine Function Transformations", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Create axes
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE}
        )
        axes.add_coordinates()
        
        # Fade out title, show axes
        self.play(FadeOut(title), Create(axes))
        
        # Original sine function
        sin_graph = axes.plot(lambda x: np.sin(x), color=RED)
        sin_label = axes.get_graph_label(sin_graph, "\\sin^(x^)")
        
        self.play(Create(sin_graph), Write(sin_label))
        self.wait(2)
        
        # End
        end_text = Text("Beautiful Sine Transformations", font_size=36, color=GOLD)
        self.play(FadeOut(axes), FadeOut(sin_graph), FadeOut(sin_label), Write(end_text))
        self.wait(3)
