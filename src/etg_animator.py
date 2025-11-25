import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import sys

# Ensure we can import from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from etg_engine import ETGEngine

class ETGAnimator:
    """
    Generates animated assets (GIFs) for social media promotion.
    Visualizes the dynamic relationship between Entanglement and Geometry.
    """

    def __init__(self):
        self.engine = ETGEngine()
        # Dark background style for "Sci-Fi" look
        plt.style.use('dark_background')

    def generate_breathing_wormhole(self, filename="wormhole_breathing.gif", frames=60):
        """
        Creates an animation of a wormhole opening and closing.
        """
        print("Initializing Animation Generator...")
        
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Remove panes and axis for a clean look
        ax.set_axis_off()
        
        # Prepare data range (0 to pi and back to 0 to make it loop smoothly)
        # Phase 1: Opening (0 -> pi/2)
        # Phase 2: Closing (pi/2 -> 0)
        thetas = np.concatenate([
            np.linspace(0, np.pi/2, frames//2),
            np.linspace(np.pi/2, 0, frames//2)
        ])

        print(f"Generating {frames} frames for animation...")

        def update(frame_idx):
            ax.clear()
            ax.set_axis_off()
            
            theta = thetas[frame_idx]
            
            # Calculate entropy for this frame
            # (In a real heavy simulation we might pre-calculate, but this is fast enough)
            entropy = self.engine.calculate_entropy(theta)
            
            # --- Geometry Generation (Same logic as Visualizer) ---
            r_throat = 0.1 + (1.2 * entropy) # Slightly exaggerated scaling for visual impact
            
            u = np.linspace(0, 2 * np.pi, 40)
            v = np.linspace(-1.8, 1.8, 30) # Longer throat
            U, V = np.meshgrid(u, v)
            
            X = r_throat * np.cosh(V) * np.cos(U)
            Y = r_throat * np.cosh(V) * np.sin(U)
            Z = np.sinh(V)
            
            # --- Plotting ---
            # Use a colormap that shifts with entropy (Cool -> Hot)
            # Low entropy = Blue/Purple (Cold/Disconnected)
            # High entropy = Orange/Red (Hot/Connected)
            
            # Surface plot with wireframe style
            surf = ax.plot_surface(X, Y, Z, cmap='magma', alpha=0.8, 
                                 linewidth=0.2, antialiased=True)
            
            # Add title dynamically
            ax.set_title(f"Entanglement Entropy: {entropy:.2f} bits\nGeometry: {'Connected' if entropy > 0.5 else 'Disconnected'}", 
                         fontsize=14, color='white')
            
            # Fix camera angle to prevent wobble
            ax.view_init(elev=20, azim=frame_idx * (360/frames) * 0.2) # Slow rotation
            
            # Set consistent limits so the object doesn't "jump" in size
            limit = 3
            ax.set_xlim(-limit, limit)
            ax.set_ylim(-limit, limit)
            ax.set_zlim(-limit, limit)
            
            return surf,

        anim = FuncAnimation(fig, update, frames=len(thetas), interval=50, blit=False)
        
        output_path = os.path.join("plots", filename)
        os.makedirs("plots", exist_ok=True)
        
        print(f"Saving animation to {output_path} (this might take a moment)...")
        # Save as GIF using Pillow writer (standard in matplotlib)
        anim.save(output_path, writer='pillow', fps=15)
        print("Animation saved successfully!")

if __name__ == "__main__":
    animator = ETGAnimator()
    animator.generate_breathing_wormhole()
