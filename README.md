# 🛰️ Kepler Root Solver & Satellite Orbit Simulation

This project contains Python scripts to solve **Kepler's Equation** using the **Newton-Raphson method** and simulate the **orbital motion** of a satellite around Earth.  
It also estimates the time when the satellite reaches a specific distance (radius) from Earth.

---

## 🧠 Main Concepts

- Solving Kepler's Equation:
  \[
  M = E - e \sin(E)
  \]
- Computing orbital positions from the eccentric anomaly.
- Interpolating to find when a given radius is reached.
- Visualizing the full orbital trajectory.

---

## 📂 Project Structure
kepler-orbit-solver/ ├── README.md ├── kepler_orbit.py # Full code for orbit simulation and radius interpolation ├── figures/ │ └── orbit_plot.png # Orbit visualization (optional) └── notebooks/ └── kepler_orbit_demo.ipynb # Jupyter Notebook (optional, for step-by-step explanation)

tp = Time("2025-03-31 00:00:00", format='iso', scale='utc')
