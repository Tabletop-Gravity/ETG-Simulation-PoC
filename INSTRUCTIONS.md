# Entanglement Tabletop Gravity (ETG) - Project Instructions

## Project Overview
This project aims to validate the Ryu-Takayanagi formula ($S=A/4G$) in a simulated environment, demonstrating the correlation between Quantum Entanglement and Geometric Connectivity (Wormhole formation).

## Prerequisites
- Python 3.x
- PowerShell (Windows)

## Setup Instructions

1.  **Navigate to the project directory:**
    ```powershell
    cd C:\Users\anton\ETG_Project
    ```

2.  **Create and Activate Virtual Environment:**
    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```
    *Note: If you encounter permission errors, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`.*

3.  **Install Dependencies:**
    ```powershell
    pip install -r requirements.txt
    ```

## Project Structure
- `src/`: Source code (`etg_engine.py`, `etg_visualizer.py`)
- `data/`: Generated CSV data files
- `plots/`: Generated high-resolution plots
- `requirements.txt`: Python dependencies
- `TODO.md`: Project task list

## Running the Simulation
To run the full pipeline, execute the following command from the project root:

```powershell
python src/main.py
```

This will:
1.  Run the quantum simulation.
2.  Generate the entropy curve plot in `plots/`.
3.  Generate the 3D wormhole visualization in `plots/`.
4.  Export the 3D geometry data to `data/` for use in Blender.
