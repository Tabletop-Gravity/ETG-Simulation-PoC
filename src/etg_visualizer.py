import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
import os
import sys

# Ensure we can import from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from etg_engine import ETGEngine

class ETGVisualizer:
    """
    Handles scientific visualization and 3D asset generation for the ETG project.
    """

    def __init__(self):
        self.engine = ETGEngine()
        self.results = []  # Stores simulation data [{'theta': t, 'entropy': s}]

    def run_simulation(self, steps=50):
        """
        Runs the quantum simulation over a range of theta values (0 to pi).
        """
        print(f"Running simulation with {steps} steps...")
        thetas = np.linspace(0, np.pi, steps)
        self.results = []
        
        for theta in thetas:
            s = self.engine.calculate_entropy(theta)
            self.results.append({'theta': theta, 'entropy': s})
        
        print(f"Simulation complete. Generated {len(self.results)} data points.")

    def plot_2d_entropy(self, filename="entropy_plot.png"):
        """
        Generates a 2D plot of Entanglement Entropy vs Theta.
        """
        if not self.results:
            print("No data to plot. Run simulation first.")
            return

        thetas = [r['theta'] for r in self.results]
        entropies = [r['entropy'] for r in self.results]

        plt.figure(figsize=(10, 6))
        plt.plot(thetas, entropies, label='Von Neumann Entropy ($S_A$)', color='darkblue', linewidth=2)
        
        # Add theoretical max line
        plt.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5, label='Max Entanglement (1 bit)')
        
        plt.xlabel(r'Entanglement Parameter $\theta$ (Radians)')
        plt.ylabel('Entropy $S$ (Von Neumann)')
        plt.title('Ryu-Takayanagi Correspondence: Entanglement vs. Connectivity')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        output_path = os.path.join("plots", filename)
        # Ensure plots directory exists (it should, but good practice)
        os.makedirs("plots", exist_ok=True)
        
        plt.savefig(output_path, dpi=300)
        print(f"2D Plot saved to {output_path}")
        plt.close()

    def generate_wormhole_geometry(self, entropy):
        """
        Maps entropy to the throat radius of a hyperboloid (wormhole geometry).
        Returns X, Y, Z coordinates.
        """
        # Mapping: Higher Entropy -> Wider Throat (Stronger Geometric Connection)
        # r_throat = base_radius + (scaling_factor * entropy)
        r_throat = 0.2 + (0.8 * entropy) 
        
        # Create a grid for the hyperboloid surface
        u = np.linspace(0, 2 * np.pi, 50) # Angular coordinate
        v = np.linspace(-1.5, 1.5, 30)    # Height/Depth coordinate
        U, V = np.meshgrid(u, v)
        
        # Parametric equations for Hyperboloid of one sheet (x^2+y^2 - z^2 = r^2)
        # x = r * cosh(v) * cos(u)
        # y = r * cosh(v) * sin(u)
        # z = sinh(v)
        # Note: We scale x and y by r_throat
        
        X = r_throat * np.cosh(V) * np.cos(U)
        Y = r_throat * np.cosh(V) * np.sin(U)
        Z = np.sinh(V)
        
        return X.flatten(), Y.flatten(), Z.flatten()

    def plot_3d_wormhole(self, filename="wormhole_3d.png"):
        """
        Generates a 3D scatter plot of the wormhole geometry at maximum entanglement.
        Also exports the raw data for Blender.
        """
        if not self.results:
            return

        # Find the state with maximum entropy to visualize the "fully open" wormhole
        max_state = max(self.results, key=lambda x: x['entropy'])
        s_max = max_state['entropy']
        
        print(f"Generating 3D geometry for Max Entropy: {s_max:.4f}")
        
        X, Y, Z = self.generate_wormhole_geometry(s_max)
        
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Scatter plot to visualize the points
        sc = ax.scatter(X, Y, Z, c=Z, cmap='magma', s=10, alpha=0.8)
        
        ax.set_title(f'Emergent Geometry: Wormhole Throat at S={s_max:.2f}')
        ax.set_xlabel('X (Space)')
        ax.set_ylabel('Y (Space)')
        ax.set_zlabel('Z (Emergent Dimension)')
        
        # Remove grid for cleaner "space" look
        ax.grid(False)
        
        # Add colorbar
        plt.colorbar(sc, ax=ax, label='Depth')
        
        output_path = os.path.join("plots", filename)
        plt.savefig(output_path, dpi=300)
        print(f"3D Plot saved to {output_path}")
        plt.close()
        
        # Export raw data for Blender
        self.export_3d_data(X, Y, Z, "wormhole_coords.csv")

    def export_3d_data(self, X, Y, Z, filename):
        """
        Exports X, Y, Z coordinates to a CSV file in the data/ folder.
        """
        output_path = os.path.join("data", filename)
        os.makedirs("data", exist_ok=True)
        
        try:
            with open(output_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['X', 'Y', 'Z']) # Header
                for x, y, z in zip(X, Y, Z):
                    writer.writerow([x, y, z])
            print(f"3D Asset Data exported to {output_path}")
        except Exception as e:
            print(f"Error exporting data: {e}")

if __name__ == "__main__":
    # Standalone execution for testing
    viz = ETGVisualizer()
    viz.run_simulation()
    viz.plot_2d_entropy()
    viz.plot_3d_wormhole()
