import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import sys

# Ensure we can import from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from etg_engine import ETGEngine

class SocialAssetsGenerator:
    """
    Generates optimized assets for social media profiles (X/Twitter).
    """

    def __init__(self):
        self.engine = ETGEngine()
        # Use dark background for that "Quantum/Space" look
        plt.style.use('dark_background')

    def generate_profile_pic(self, filename="social_profile.png"):
        """
        Generates a square, high-contrast image suitable for a round profile picture.
        Visualizes the 'throat' of the wormhole from a top-down perspective.
        """
        print("Generating Profile Picture...")
        
        # High entropy state for maximum "opening"
        entropy = 1.0 
        r_throat = 0.2 + (0.8 * entropy)
        
        # Geometry
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(-1, 1, 50)
        U, V = np.meshgrid(u, v)
        
        X = r_throat * np.cosh(V) * np.cos(U)
        Y = r_throat * np.cosh(V) * np.sin(U)
        Z = np.sinh(V)
        
        # Create figure with square aspect ratio
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Plot surface with a glowing colormap
        # 'plasma' or 'magma' look very energetic
        surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.9, 
                             linewidth=0, antialiased=True)
        
        # Top-down view to create a "Tunnel/Eye" effect perfect for round avatars
        ax.view_init(elev=90, azim=0)
        
        # Remove all axes and backgrounds for a clean look
        ax.set_axis_off()
        ax.grid(False)
        
        # Zoom in slightly to fill the frame
        limit = 1.5
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_zlim(-limit, limit)
        
        output_path = os.path.join("plots", filename)
        os.makedirs("plots", exist_ok=True)
        
        # Save with transparent background if possible, but dark bg is safer for X
        plt.savefig(output_path, dpi=300, bbox_inches='tight', pad_inches=0, facecolor='black')
        print(f"Profile picture saved to {output_path}")
        plt.close()

    def generate_cover_image(self, filename="social_cover.png"):
        """
        Generates a 1500x500 pixel header image (3:1 aspect ratio).
        Features a wide landscape of the quantum geometry.
        """
        print("Generating Cover Image...")
        
        # Create figure with 3:1 aspect ratio (e.g., 15x5 inches)
        fig = plt.figure(figsize=(15, 5))
        ax = fig.add_subplot(111, projection='3d')
        
        # Generate a "field" of geometry or a side view
        entropy = 0.9
        r_throat = 0.2 + (0.8 * entropy)
        
        u = np.linspace(0, 2 * np.pi, 80)
        v = np.linspace(-2, 2, 60) # Longer throat for the wide view
        U, V = np.meshgrid(u, v)
        
        X = r_throat * np.cosh(V) * np.cos(U)
        Y = r_throat * np.cosh(V) * np.sin(U)
        Z = np.sinh(V)
        
        # Wireframe style looks more "tech" for a header
        ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2, color='cyan', alpha=0.3, linewidth=0.5)
        
        # Add some scattered points to simulate "quantum fluctuations" or stars
        num_stars = 200
        xs = np.random.uniform(-4, 4, num_stars)
        ys = np.random.uniform(-4, 4, num_stars)
        zs = np.random.uniform(-3, 3, num_stars)
        ax.scatter(xs, ys, zs, c='white', s=1, alpha=0.5)

        # Side view to show the "bridge" shape
        ax.view_init(elev=10, azim=45)
        
        ax.set_axis_off()
        ax.grid(False)
        
        # Tight layout to maximize usage of the 3:1 space
        ax.set_xlim(-4, 4)
        ax.set_ylim(-4, 4)
        ax.set_zlim(-3, 3)
        
        output_path = os.path.join("plots", filename)
        
        plt.savefig(output_path, dpi=300, bbox_inches='tight', pad_inches=0, facecolor='black')
        print(f"Cover image saved to {output_path}")
        plt.close()

if __name__ == "__main__":
    gen = SocialAssetsGenerator()
    gen.generate_profile_pic()
    gen.generate_cover_image()
