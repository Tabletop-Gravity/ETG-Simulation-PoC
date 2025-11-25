import sys
import os
import time

# Ensure we can import modules from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from etg_visualizer import ETGVisualizer

def main():
    print("================================================================")
    print("   ENTANGLEMENT TABLETOP GRAVITY (ETG) - SIMULATION SUITE       ")
    print("================================================================")
    print("Initializing Quantum Engine & Visualization Modules...")
    
    start_time = time.time()
    
    # Initialize Visualizer (which initializes the Engine)
    viz = ETGVisualizer()
    
    # 1. Run Core Simulation
    print("\n[1/3] Running Quantum Simulation (Alice-Bob Entanglement)...")
    viz.run_simulation(steps=100) # Higher resolution for final run
    
    # 2. Generate Scientific Plots
    print("\n[2/3] Generating Scientific Visualizations...")
    viz.plot_2d_entropy("etg_entropy_curve.png")
    viz.plot_3d_wormhole("etg_wormhole_geometry.png")
    
    # 3. Final Report
    print("\n[3/3] Simulation Complete!")
    
    elapsed = time.time() - start_time
    
    print("\n----------------------------------------------------------------")
    print(f"Execution Time: {elapsed:.2f} seconds")
    print("----------------------------------------------------------------")
    print("OUTPUTS GENERATED:")
    print(f" > 2D Plot:      {os.path.abspath('plots/etg_entropy_curve.png')}")
    print(f" > 3D Plot:      {os.path.abspath('plots/etg_wormhole_geometry.png')}")
    print(f" > 3D Asset:     {os.path.abspath('data/wormhole_coords.csv')}")
    print("----------------------------------------------------------------")
    print("Ready for GitHub & Crowdfunding Campaign.")
    print("================================================================")

if __name__ == "__main__":
    main()
