from manim import *
import numpy as np

class BaseScene(Scene):
    """Base scene template with common settings and methods"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = "#0f0f0f"
        
    def create_title(self, text, subtitle=None):
        """Create standardized title"""
        title = Text(text, font_size=48, color=BLUE)
        title.to_edge(UP)
        
        if subtitle:
            sub = Text(subtitle, font_size=24, color=GRAY)
            sub.next_to(title, DOWN)
            return VGroup(title, sub)
        
        return title
    
    def create_footer(self, text):
        """Create footer info"""
        footer = Text(text, font_size=16, color=GRAY)
        footer.to_edge(DOWN)
        return footer
