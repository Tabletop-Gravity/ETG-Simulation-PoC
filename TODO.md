# Entanglement Tabletop Gravity (ETG) - Project Tasks

- [x] **Setup Environment**
    - [x] Create virtual environment commands
    - [x] Create folder structure (`src/`, `data/`, `plots/`)
    - [x] Create `requirements.txt`

- [ ] **Core Simulation (Engine)** `src/etg_engine.py`
    - [ ] Create Quantum Circuit (Alice-Bob pair)
    - [ ] Implement Entanglement variation (Ry(theta) + CNOT)
    - [ ] Calculate Density Matrix & Von Neumann Entropy
    - [ ] Add Noise Model simulation (Qiskit Aer)

- [x] **Scientific Visualization** `src/etg_visualizer.py`
    - [x] Generate 2D Plot (Theta vs Entropy)
    - [x] Save high-resolution plot (300 DPI)

- [x] **3D Asset Generation (Wormhole)**
    - [x] Map Entropy to 3D geometry (Hyperboloid/Sphere expansion)
    - [x] Generate 3D Scatter plot
    - [x] Export raw data (X, Y, Z) to CSV for Blender

- [x] **Final Output**
    - [x] Implement `main()` pipeline
    - [x] Add comprehensive comments (English)
    - [x] Verify execution and report
