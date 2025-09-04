"""
Mathematical Animation Formulas: Processing to Manim (CORRECTED)
Inspired by yuruyurau's organic mathematical creatures
10 Original Mathematical Formulas with Processing and Manim implementations
"""

from manim import *
import numpy as np

# ============================================
# FORMULA 1: Spiral Breathing Organism
# ============================================
class SpiralBreathingOrganism(Scene):
    def construct(self):
        def create_spiral_creature(t):
            points = []
            for i in range(500):
                r = np.sqrt(i) * 0.5
                theta = i * 0.1
                x = r * np.cos(theta + t) * (1 + 0.3 * np.sin(5*theta - t))
                y = r * np.sin(theta + t) * (1 + 0.3 * np.sin(5*theta - t))
                points.append([x, y, 0])
            return points
        
        dots = VGroup(*[Dot(point=p, radius=0.02, color=BLUE) for p in create_spiral_creature(0)])
        self.add(dots)
        
        time_tracker = ValueTracker(0)
        
        def update_dots(mob):
            t = time_tracker.get_value()
            new_points = create_spiral_creature(t)
            for dot, point in zip(mob, new_points):
                dot.move_to(point)
        
        dots.add_updater(update_dots)
        self.play(time_tracker.animate.set_value(10), run_time=10, rate_func=linear)
        dots.remove_updater(update_dots)

# ============================================
# FORMULA 2: Wave Interference Jellyfish
# ============================================
class WaveInterferenceJellyfish(Scene):
    def construct(self):
        def create_jellyfish(t):
            points = []
            for i in range(1600):
                u = (i % 40 - 20) * 0.2
                v = (i // 40 - 20) * 0.2
                x = u + 0.5 * np.sin(v - t) * np.cos(u + t*0.5)
                y = v + 0.5 * np.cos(u - t) * np.sin(v - t*0.5)
                points.append([x, y, 0])
            return points
        
        dots = VGroup(*[Dot(point=p, radius=0.015, color=PURPLE) for p in create_jellyfish(0)])
        self.add(dots)
        
        time_tracker = ValueTracker(0)
        
        def update_dots(mob):
            t = time_tracker.get_value()
            new_points = create_jellyfish(t)
            for dot, point in zip(mob, new_points):
                dot.move_to(point)
        
        dots.add_updater(update_dots)
        self.play(time_tracker.animate.set_value(20), run_time=10, rate_func=linear)
        dots.remove_updater(update_dots)

# ============================================
# FORMULA 3: Fractal Flow Field
# ============================================
class FractalFlowField(Scene):
    def construct(self):
        def create_flow_field(t):
            points = []
            colors = []
            for i in range(2500):
                x0 = (i % 50 - 25) * 0.15
                y0 = (i // 50 - 25) * 0.15
                x = x0 + 0.8 * np.sin(y0 + t) * np.cos(x0*0.5 + np.sin(t*0.5))
                y = y0 + 0.8 * np.cos(x0 - t) * np.sin(y0*0.5 + np.cos(t*0.5))
                points.append([x, y, 0])
                # Color based on distance from origin
                dist = np.sqrt(x**2 + y**2)
                colors.append(interpolate_color(BLUE, RED, min(dist/5, 1)))
            return points, colors
        
        points, colors = create_flow_field(0)
        dots = VGroup(*[Dot(point=p, radius=0.01, color=c) for p, c in zip(points, colors)])
        self.add(dots)
        
        time_tracker = ValueTracker(0)
        
        def update_dots(mob):
            t = time_tracker.get_value()
            new_points, new_colors = create_flow_field(t)
            for dot, point, color in zip(mob, new_points, new_colors):
                dot.move_to(point)
                dot.set_color(color)
        
        dots.add_updater(update_dots)
        self.play(time_tracker.animate.set_value(15), run_time=10, rate_func=linear)
        dots.remove_updater(update_dots)

# ============================================
# FORMULA 4: Quantum Oscillator Network
# ============================================
class QuantumOscillatorNetwork(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        def create_network(t):
            points = []
            for i in range(-3, 4):
                for j in range(-3, 4):
                    x = i + 0.3 * np.sin(j*0.5 - t) * np.cos(i*0.7 + t)
                    y = j + 0.3 * np.cos(i*0.5 + t) * np.sin(j*0.7 - t)
                    z = 0.5 * np.sin(i + j - t*2)
                    points.append([x, y, z])
            return points
        
        spheres = VGroup(*[Sphere(radius=0.1, color=TEAL).move_to(p) for p in create_network(0)])
        self.add(spheres)
        
        time_tracker = ValueTracker(0)
        
        def update_spheres(mob):
            t = time_tracker.get_value()
            new_points = create_network(t)
            for sphere, point in zip(mob, new_points):
                sphere.move_to(point)
        
        spheres.add_updater(update_spheres)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(time_tracker.animate.set_value(20), run_time=10, rate_func=linear)
        spheres.remove_updater(update_spheres)

# ============================================
# FORMULA 5: Möbius Heart Transformation
# ============================================
class MobiusHeartTransformation(Scene):
    def construct(self):
        def create_heart(t):
            points = []
            theta_values = np.linspace(0, 2*PI, 200)
            for theta in theta_values:
                r = 1.5 + np.sin(3*theta + t) * np.cos(2*theta - t*0.7)
                x = r * np.cos(theta) * (1 + 0.2*np.sin(5*theta - t))
                y = r * np.sin(theta) * (1 + 0.2*np.cos(5*theta + t))
                points.append([x, y, 0])
            return points
        
        # Create path with gradient color
        path = VMobject()
        path.set_points_as_corners(create_heart(0))
        path.set_stroke(color=PINK, width=3)
        self.add(path)
        
        time_tracker = ValueTracker(0)
        
        def update_path(mob):
            t = time_tracker.get_value()
            new_points = create_heart(t)
            mob.set_points_as_corners(new_points)
        
        path.add_updater(update_path)
        self.play(time_tracker.animate.set_value(20), run_time=10, rate_func=linear)
        path.remove_updater(update_path)

# ============================================
# FORMULA 6: Cellular Automata Dance
# ============================================
class CellularAutomataDance(Scene):
    def construct(self):
        def create_cells(t):
            cells = VGroup()
            for i in range(900):
                x = (i % 30 - 15) * 0.25 + 0.2 * np.sin(i*0.1 - t) * np.cos((i//30)*0.2 + t)
                y = (i // 30 - 15) * 0.25 + 0.2 * np.cos(i*0.1 + t) * np.sin((i % 30)*0.2 - t)
                scale = 0.03 * (1 + 0.5 * np.sin(i*0.05 - t*2))
                
                cell = Square(side_length=scale*2, color=interpolate_color(BLUE, YELLOW, (np.sin(t + i*0.1) + 1)/2))
                cell.move_to([x, y, 0])
                cells.add(cell)
            return cells
        
        cells = create_cells(0)
        self.add(cells)
        
        time_tracker = ValueTracker(0)
        
        def update_cells(mob):
            t = time_tracker.get_value()
            new_cells = create_cells(t)
            mob.become(new_cells)
        
        cells.add_updater(update_cells)
        self.play(time_tracker.animate.set_value(20), run_time=10, rate_func=linear)
        cells.remove_updater(update_cells)

# ============================================
# FORMULA 7: Lissajous Butterfly Swarm
# ============================================
class LissajousButterfly(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        
        def create_butterflies(t):
            butterflies = VGroup()
            for i in range(20):
                phase = i * PI / 10
                trail = []
                for j in range(50):
                    t_point = t - j * 0.02
                    x = 2 * np.sin(2*t_point + phase) * np.cos(t_point + i*0.1)
                    y = 2 * np.sin(3*t_point + phase + PI/2) * np.sin(t_point - i*0.1)
                    z = np.sin(5*t_point + phase + i*0.2)
                    trail.append([x, y, z])
                
                path = VMobject()
                path.set_points_as_corners(trail)
                path.set_stroke(color=interpolate_color(ORANGE, PINK, i/20), width=2, opacity=0.7)
                butterflies.add(path)
            return butterflies
        
        butterflies = create_butterflies(0)
        self.add(butterflies)
        
        time_tracker = ValueTracker(0)
        
        def update_butterflies(mob):
            t = time_tracker.get_value()
            new_butterflies = create_butterflies(t)
            mob.become(new_butterflies)
        
        butterflies.add_updater(update_butterflies)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(time_tracker.animate.set_value(20), run_time=10, rate_func=linear)
        butterflies.remove_updater(update_butterflies)

# ============================================
# FORMULA 8: Fibonacci Spiral Galaxy
# ============================================
class FibonacciSpiralGalaxy(Scene):
    def construct(self):
        def create_galaxy(t):
            points = []
            colors = []
            golden_angle = 137.5 * DEGREES
            
            for i in range(1, 500):
                angle = i * golden_angle
                r = np.sqrt(i) * 0.1
                x = r * np.cos(angle + t*0.1) * (1 + 0.1*np.sin(i*0.1 - t))
                y = r * np.sin(angle + t*0.1) * (1 + 0.1*np.cos(i*0.1 + t))
                points.append([x, y, 0])
                
                # Create spiral color gradient
                colors.append(interpolate_color(BLUE, GOLD, i/500))
            
            return points, colors
        
        points, colors = create_galaxy(0)
        dots = VGroup(*[Dot(point=p, radius=0.015, color=c) for p, c in zip(points, colors)])
        self.add(dots)
        
        time_tracker = ValueTracker(0)
        
        def update_galaxy(mob):
            t = time_tracker.get_value()
            new_points, new_colors = create_galaxy(t)
            for dot, point, color in zip(mob, new_points, new_colors):
                dot.move_to(point)
                dot.set_color(color)
        
        dots.add_updater(update_galaxy)
        self.play(time_tracker.animate.set_value(10), run_time=10, rate_func=linear)
        dots.remove_updater(update_galaxy)

# ============================================
# FORMULA 9: Torus Knot Metamorphosis
# ============================================
class TorusKnotMetamorphosis(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        
        def create_torus_knot(t):
            points = []
            s_values = np.linspace(0, 2*PI, 200)
            
            for s in s_values:
                x = (2 + np.cos(3*s)) * np.cos(2*s + t)
                y = (2 + np.cos(3*s)) * np.sin(2*s + t)
                z = np.sin(3*s) + 0.5*np.sin(5*s - t)
                points.append([x, y, z])
            return points
        
        # Create parametric curve
        curve = VMobject()
        curve.set_points_as_corners(create_torus_knot(0))
        curve.set_stroke(color=BLUE, width=4)
        self.add(curve)
        
        # Add trailing effect
        trails = VGroup()
        for i in range(5):
            trail = VMobject()
            trail.set_points_as_corners(create_torus_knot(-i*0.2))
            trail.set_stroke(color=BLUE, width=2, opacity=0.3*(1-i/5))
            trails.add(trail)
        self.add(trails)
        
        time_tracker = ValueTracker(0)
        
        def update_knot(mob):
            t = time_tracker.get_value()
            new_points = create_torus_knot(t)
            curve.set_points_as_corners(new_points)
            
            # Update trails
            for i, trail in enumerate(trails):
                trail_points = create_torus_knot(t - (i+1)*0.2)
                trail.set_points_as_corners(trail_points)
        
        curve.add_updater(update_knot)
        self.begin_ambient_camera_rotation(rate=0.15)
        self.play(time_tracker.animate.set_value(10), run_time=10, rate_func=linear)
        curve.remove_updater(update_knot)

# ============================================
# FORMULA 10: Chaotic Attractor Organism
# ============================================
class ChaoticAttractorOrganism(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES, distance=15)
        
        def lorenz_derivative(point, t):
            x, y, z = point
            sigma, rho, beta = 10, 28, 8/3
            
            # Clamp input values to prevent overflow
            x = np.clip(x, -50, 50)
            y = np.clip(y, -50, 50)
            z = np.clip(z, -50, 50)
            
            dx = sigma * (y - x) + 0.1 * np.sin(t)
            dy = x * (rho - z) - y + 0.1 * np.cos(t)
            dz = x * y - beta * z + 0.05 * np.sin(2*t)
            
            # Clamp derivatives to prevent overflow
            dx = np.clip(dx, -100, 100)
            dy = np.clip(dy, -100, 100)
            dz = np.clip(dz, -100, 100)
            
            return np.array([dx, dy, dz]) * 0.005
        
        # Create multiple particles with slightly different initial conditions
        particles = VGroup()
        trajectories = []
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE]
        
        for i in range(6):
            # Initial position with small variation
            initial = np.array([0.1 + i*0.01, 0.1, 0.1])
            particle = Sphere(radius=0.08, color=colors[i])
            particle.move_to(initial)
            particles.add(particle)
            
            # Store trajectory points
            trajectory = [initial.copy()]
            trajectories.append(trajectory)
        
        self.add(particles)
        
        # Add paths
        paths = VGroup()
        for i, color in enumerate(colors):
            path = VMobject()
            path.set_stroke(color=color, width=2, opacity=0.6)
            paths.add(path)
        self.add(paths)
        
        time_tracker = ValueTracker(0)
        current_positions = [np.array(p.get_center()) for p in particles]
        dt = 0.1  # Time step
        
        def update_system(mob):
            t = time_tracker.get_value()
            
            for i, particle in enumerate(particles):
                # Update particle position using smaller steps
                current_pos = current_positions[i]
                
                # Check for NaN or infinite values
                if np.any(np.isnan(current_pos)) or np.any(np.isinf(current_pos)):
                    # Reset position if invalid
                    current_pos = np.array([0.1 + i*0.01, 0.1, 0.1])
                
                derivative = lorenz_derivative(current_pos, t)
                new_pos = current_pos + derivative * dt
                
                # Clamp position to reasonable bounds
                new_pos = np.clip(new_pos, -10, 10)
                
                particle.move_to(new_pos)
                current_positions[i] = new_pos
                
                # Update trajectory
                trajectory = trajectories[i]
                trajectory.append(new_pos.copy())
                if len(trajectory) > 80:  # Keep only recent points
                    trajectory.pop(0)
                
                # Update path (only if we have enough valid points)
                if len(trajectory) > 2:
                    try:
                        # Filter out any invalid points
                        valid_trajectory = [p for p in trajectory if not (np.any(np.isnan(p)) or np.any(np.isinf(p)))]
                        if len(valid_trajectory) > 2:
                            paths[i].set_points_as_corners(valid_trajectory)
                    except:
                        # If path setting fails, just continue
                        pass
        
        particles.add_updater(update_system)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(time_tracker.animate.set_value(10), run_time=10, rate_func=linear)
        particles.remove_updater(update_system)

# ============================================
# Main Scene Compositor - Combines Multiple Effects
# ============================================
class UltimateMathCreature(Scene):
    """
    This scene combines multiple mathematical formulas to create
    an ultra-complex, organic-looking creature animation
    """
    def construct(self):
        # Set dark background for contrast
        self.camera.background_color = "#0a0a0a"
        
        def create_ultimate_creature(t):
            creature = VGroup()
            
            # Core body using spiral formula
            core_points = []
            for i in range(200):
                r = np.sqrt(i) * 0.3
                theta = i * 0.15
                x = r * np.cos(theta + t*0.5) * (1 + 0.3 * np.sin(5*theta - t))
                y = r * np.sin(theta + t*0.5) * (1 + 0.3 * np.sin(5*theta - t))
                core_points.append([x, y, 0])
            
            # Add tentacles using Lissajous curves
            for j in range(6):
                tentacle_angle = j * PI / 3
                tentacle = VMobject()
                tentacle_points = []
                
                for k in range(50):
                    s = k * 0.1
                    tx = np.cos(tentacle_angle) * s + 0.3 * np.sin(3*s - t) * np.cos(2*s + t)
                    ty = np.sin(tentacle_angle) * s + 0.3 * np.cos(3*s + t) * np.sin(2*s - t)
                    tentacle_points.append([tx*2, ty*2, 0])
                
                tentacle.set_points_as_corners(tentacle_points)
                tentacle.set_stroke(
                    color=interpolate_color(TEAL, PURPLE, j/6),
                    width=3,
                    opacity=0.8
                )
                creature.add(tentacle)
            
            # Add pulsating dots for the core
            for i, point in enumerate(core_points[::5]):  # Every 5th point
                dot = Dot(
                    point=point,
                    radius=0.02 * (1 + 0.5*np.sin(t*3 + i*0.2)),
                    color=interpolate_color(BLUE, PINK, (np.sin(t + i*0.1) + 1)/2)
                )
                creature.add(dot)
            
            # Add outer aura particles
            for i in range(100):
                angle = i * 2 * PI / 100
                r = 3 + 0.5 * np.sin(5*angle - t*2)
                px = r * np.cos(angle + t*0.3)
                py = r * np.sin(angle + t*0.3)
                
                particle = Dot(
                    point=[px, py, 0],
                    radius=0.01,
                    color=interpolate_color(YELLOW, ORANGE, (np.sin(t*2 + i*0.1) + 1)/2)
                )
                particle.set_opacity(0.6)
                creature.add(particle)
            
            return creature
        
        # Create and animate the creature
        creature = create_ultimate_creature(0)
        self.add(creature)
        
        time_tracker = ValueTracker(0)
        
        def update_creature(mob):
            t = time_tracker.get_value()
            new_creature = create_ultimate_creature(t)
            mob.become(new_creature)
        
        creature.add_updater(update_creature)
        
        # Add title
        title = Text("Mathematical Organism", font_size=24, color=GOLD)
        title.to_edge(UP)
        self.add(title)
        
        self.play(time_tracker.animate.set_value(30), run_time=15, rate_func=linear)
        creature.remove_updater(update_creature)

# ============================================
# Bonus: Interactive Parametric Explorer
# ============================================
class ParametricExplorer(Scene):
    """
    An interactive scene showing how different parameters affect the animations
    """
    def construct(self):
        # Create parameter displays
        param_text = VGroup(
            Text("Frequency: ", font_size=20),
            Text("Amplitude: ", font_size=20),
            Text("Phase: ", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        
        freq_val = ValueTracker(1)
        amp_val = ValueTracker(1)
        phase_val = ValueTracker(0)
        
        freq_num = DecimalNumber(freq_val.get_value(), font_size=20).next_to(param_text[0], RIGHT)
        amp_num = DecimalNumber(amp_val.get_value(), font_size=20).next_to(param_text[1], RIGHT)
        phase_num = DecimalNumber(phase_val.get_value(), font_size=20).next_to(param_text[2], RIGHT)
        
        freq_num.add_updater(lambda m: m.set_value(freq_val.get_value()))
        amp_num.add_updater(lambda m: m.set_value(amp_val.get_value()))
        phase_num.add_updater(lambda m: m.set_value(phase_val.get_value()))
        
        self.add(param_text, freq_num, amp_num, phase_num)
        
        # Create parametric curve
        def create_curve(f, a, p):
            t_values = np.linspace(0, 2*PI, 200)
            points = []
            for t in t_values:
                x = a * np.cos(f * t + p) * (1 + 0.3 * np.sin(5 * t))
                y = a * np.sin(f * t + p) * (1 + 0.3 * np.cos(5 * t))
                points.append([x, y, 0])
            return points
        
        curve = VMobject()
        curve.set_points_as_corners(create_curve(1, 2, 0))
        curve.set_stroke(color=BLUE, width=3)
        self.add(curve)
        
        def update_curve(mob):
            new_points = create_curve(
                freq_val.get_value(),
                amp_val.get_value(),
                phase_val.get_value()
            )
            mob.set_points_as_corners(new_points)
        
        curve.add_updater(update_curve)
        
        # Animate parameter changes
        self.play(
            freq_val.animate.set_value(3),
            run_time=3
        )
        self.play(
            amp_val.animate.set_value(2.5),
            run_time=3
        )
        self.play(
            phase_val.animate.set_value(PI),
            run_time=3
        )
        self.play(
            freq_val.animate.set_value(2),
            amp_val.animate.set_value(1.5),
            phase_val.animate.set_value(PI/2),
            run_time=4
        )

# ============================================
# Alternative Stable Version of Chaotic Attractor
# ============================================
class SimpleChaoticOrganism(Scene):
    """
    A simplified, more stable version of the chaotic organism
    """
    def construct(self):
        def create_organic_swarm(t):
            points = []
            colors = []
            
            # Create multiple oscillating points with chaotic-like behavior
            for i in range(200):
                # Use simpler, more controlled chaos
                phase = i * 0.1
                
                # Multiple coupled oscillators
                x1 = 2 * np.sin(t*0.7 + phase) * np.cos(t*0.5 + phase*2)
                y1 = 2 * np.cos(t*0.6 + phase) * np.sin(t*0.8 + phase*1.5)
                
                x2 = np.sin(t*2 + phase*3) * 0.5
                y2 = np.cos(t*1.5 + phase*2) * 0.5
                
                x = x1 + x2
                y = y1 + y2
                
                points.append([x, y, 0])
                
                # Color based on position and time
                color_param = (np.sin(t + i*0.05) + 1) / 2
                colors.append(interpolate_color(BLUE, ORANGE, color_param))
            
            return points, colors
        
        points, colors = create_organic_swarm(0)
        dots = VGroup(*[Dot(point=p, radius=0.03, color=c) for p, c in zip(points, colors)])
        self.add(dots)
        
        time_tracker = ValueTracker(0)
        
        def update_swarm(mob):
            t = time_tracker.get_value()
            new_points, new_colors = create_organic_swarm(t)
            for dot, point, color in zip(mob, new_points, new_colors):
                dot.move_to(point)
                dot.set_color(color)
        
        dots.add_updater(update_swarm)
        self.play(time_tracker.animate.set_value(20), run_time=10, rate_func=linear)
        dots.remove_updater(update_swarm)

# ============================================
# Example Usage and Rendering Commands
# ============================================
"""
To render these animations, use the following commands:

1. Spiral Breathing Organism:
   manim -pql math_animations.py SpiralBreathingOrganism

2. Wave Interference Jellyfish:
   manim -pql math_animations.py WaveInterferenceJellyfish

3. Fractal Flow Field:
   manim -pql math_animations.py FractalFlowField

4. Quantum Oscillator Network (3D):
   manim -pql math_animations.py QuantumOscillatorNetwork

5. Möbius Heart Transformation:
   manim -pql math_animations.py MobiusHeartTransformation

6. Cellular Automata Dance:
   manim -pql math_animations.py CellularAutomataDance

7. Lissajous Butterfly Swarm (3D):
   manim -pql math_animations.py LissajousButterfly

8. Fibonacci Spiral Galaxy:
   manim -pql math_animations.py FibonacciSpiralGalaxy

9. Torus Knot Metamorphosis (3D):
   manim -pql math_animations.py TorusKnotMetamorphosis

10. Chaotic Attractor Organism (3D) - FIXED VERSION:
    manim -pql math_animations.py ChaoticAttractorOrganism

11. Simple Chaotic Organism (Stable Alternative):
    manim -pql math_animations.py SimpleChaoticOrganism

For the ultimate combined effect:
   manim -pqh math_animations.py UltimateMathCreature

For interactive parameter exploration:
   manim -pql math_animations.py ParametricExplorer

Options:
   -p : Preview after rendering
   -q : Quality (l=low, m=medium, h=high, k=4K)
   -s : Save last frame as image
   --fps 60 : Set frame rate to 60fps for smoother animation

RECOMMENDED: Start with SimpleChaoticOrganism for a stable chaotic effect.
"""