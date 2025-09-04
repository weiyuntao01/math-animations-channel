import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse, Polygon
import matplotlib.patheffects as path_effects

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(16, 10))
ax.set_xlim(-10, 10)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('white')

# Define golden color gradients
gold_colors = ['#FFD700', '#FFA500', '#FF8C00', '#FF6347']

# Dragon body curve (S-shaped serpentine)
t = np.linspace(0, 4*np.pi, 200)
x_body = t - 5 + 2*np.sin(t/2)
y_body = 3*np.sin(t) * np.exp(-t/10)

# Draw body segments with scales effect
for i in range(0, len(x_body)-10, 5):
    # Body segment
    segment_width = 1.2 - i*0.003
    circle = Circle((x_body[i], y_body[i]), segment_width, 
                   facecolor=gold_colors[i%3], edgecolor='#B8860B', linewidth=1.5)
    ax.add_patch(circle)
    
    # Scale pattern
    if i % 10 == 0:
        scale = Ellipse((x_body[i], y_body[i]), segment_width*0.8, segment_width*0.5,
                       angle=np.degrees(np.arctan2(y_body[min(i+5, len(y_body)-1)] - y_body[i],
                                                   x_body[min(i+5, len(x_body)-1)] - x_body[i])),
                       facecolor='#FFB347', edgecolor='#B8860B', linewidth=0.5, alpha=0.7)
        ax.add_patch(scale)

# Dragon head
head_x, head_y = x_body[0] - 1.5, y_body[0]

# Main head shape (elongated triangle)
head_points = np.array([
    [head_x-2, head_y],
    [head_x-1.5, head_y+1],
    [head_x, head_y+0.8],
    [head_x+0.5, head_y],
    [head_x, head_y-0.8],
    [head_x-1.5, head_y-1],
])
head = Polygon(head_points, facecolor='#FFD700', edgecolor='#B8860B', linewidth=2)
ax.add_patch(head)

# Snout and jaw
snout_points = np.array([
    [head_x-2, head_y],
    [head_x-2.5, head_y+0.3],
    [head_x-2.8, head_y],
    [head_x-2.5, head_y-0.3],
])
snout = Polygon(snout_points, facecolor='#FFA500', edgecolor='#B8860B', linewidth=1.5)
ax.add_patch(snout)

# Eyes
eye1 = Circle((head_x-1, head_y+0.4), 0.15, facecolor='#FF0000', edgecolor='black', linewidth=1)
eye2 = Circle((head_x-1, head_y-0.4), 0.15, facecolor='#FF0000', edgecolor='black', linewidth=1)
ax.add_patch(eye1)
ax.add_patch(eye2)

# Horns
horn1_points = np.array([
    [head_x-0.5, head_y+0.8],
    [head_x-0.3, head_y+1.5],
    [head_x-0.7, head_y+1.4],
])
horn2_points = np.array([
    [head_x-0.5, head_y-0.8],
    [head_x-0.3, head_y-1.5],
    [head_x-0.7, head_y-1.4],
])
horn1 = Polygon(horn1_points, facecolor='#FFB347', edgecolor='#B8860B', linewidth=1)
horn2 = Polygon(horn2_points, facecolor='#FFB347', edgecolor='#B8860B', linewidth=1)
ax.add_patch(horn1)
ax.add_patch(horn2)

# Whiskers (using curved lines)
whisker_t = np.linspace(0, 1, 50)
for i in range(3):
    w_x = head_x - 2.5 - whisker_t * 1.5
    w_y1 = head_y + 0.2 + i*0.15 + 0.3*np.sin(whisker_t*np.pi*2)
    w_y2 = head_y - 0.2 - i*0.15 - 0.3*np.sin(whisker_t*np.pi*2)
    ax.plot(w_x, w_y1, color='#B8860B', linewidth=2)
    ax.plot(w_x, w_y2, color='#B8860B', linewidth=2)

# Mane/flames around head
flame_angles = np.linspace(0, 2*np.pi, 12)
for angle in flame_angles:
    if np.pi/4 < angle < 7*np.pi/4:  # Only on top and back of head
        flame_x = head_x - 0.5 + 1.2*np.cos(angle)
        flame_y = head_y + 1.2*np.sin(angle)
        flame_tip_x = flame_x + 0.8*np.cos(angle)
        flame_tip_y = flame_y + 0.8*np.sin(angle)
        
        flame_points = np.array([
            [flame_x-0.1, flame_y-0.1],
            [flame_tip_x, flame_tip_y],
            [flame_x+0.1, flame_y+0.1],
        ])
        flame = Polygon(flame_points, facecolor='#FFA500', edgecolor='#FF8C00', 
                       linewidth=1, alpha=0.8)
        ax.add_patch(flame)

# Legs and claws (4 legs along the body)
leg_positions = [20, 60, 100, 140]
for pos in leg_positions:
    if pos < len(x_body):
        leg_x, leg_y = x_body[pos], y_body[pos]
        
        # Upper leg
        for dy in [-1.2, 1.2]:  # Two legs at each position
            # Leg
            leg_points = np.array([
                [leg_x-0.2, leg_y],
                [leg_x+0.2, leg_y],
                [leg_x+0.1, leg_y+dy],
                [leg_x-0.1, leg_y+dy],
            ])
            leg = Polygon(leg_points, facecolor='#FFD700', edgecolor='#B8860B', linewidth=1)
            ax.add_patch(leg)
            
            # Claws
            for claw_offset in [-0.2, 0, 0.2]:
                claw_x = leg_x + claw_offset
                claw_y = leg_y + dy
                claw_points = np.array([
                    [claw_x, claw_y],
                    [claw_x-0.05, claw_y+dy*0.3],
                    [claw_x+0.05, claw_y+dy*0.3],
                ])
                claw = Polygon(claw_points, facecolor='#B8860B', edgecolor='#8B4513', linewidth=0.5)
                ax.add_patch(claw)

# Tail fin/flames
tail_x, tail_y = x_body[-1], y_body[-1]
tail_angles = np.linspace(-np.pi/3, np.pi/3, 7)
for angle in tail_angles:
    fin_length = 1.5 + 0.3*np.random.random()
    fin_x = tail_x + fin_length*np.cos(angle)
    fin_y = tail_y + fin_length*np.sin(angle)
    
    fin_points = np.array([
        [tail_x, tail_y],
        [fin_x-0.1, fin_y],
        [fin_x+0.2, fin_y+0.2],
        [fin_x+0.2, fin_y-0.2],
    ])
    fin = Polygon(fin_points, facecolor='#FFA500', edgecolor='#FF8C00', 
                 linewidth=1, alpha=0.7)
    ax.add_patch(fin)

# Add some decorative clouds/smoke
cloud_positions = [(-6, 3), (4, -3), (6, 2)]
for cx, cy in cloud_positions:
    for i in range(3):
        cloud = Circle((cx + i*0.5, cy + np.random.random()*0.5 - 0.25), 
                      0.4 + np.random.random()*0.2,
                      facecolor='white', alpha=0.3, edgecolor='none')
        ax.add_patch(cloud)

# Add teeth
teeth_x = np.linspace(head_x-2.7, head_x-2, 5)
for tx in teeth_x:
    tooth_upper = patches.FancyBboxPatch((tx, head_y+0.1), 0.08, 0.15,
                                         boxstyle="round,pad=0", 
                                         facecolor='white', edgecolor='gray')
    tooth_lower = patches.FancyBboxPatch((tx, head_y-0.25), 0.08, 0.15,
                                         boxstyle="round,pad=0", 
                                         facecolor='white', edgecolor='gray')
    ax.add_patch(tooth_upper)
    ax.add_patch(tooth_lower)

# Add title
plt.title('Golden Chinese Dragon', fontsize=20, fontweight='bold', color='#B8860B', pad=20)

# Show the plot
plt.tight_layout()
plt.show()