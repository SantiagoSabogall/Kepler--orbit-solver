import numpy as np
from astropy.time import Time, TimeDelta
from astropy import units as u 
import matplotlib.pyplot as plt

def newton(l, e, tol=1e-8, max_iter=100):
    E = l  # Initial Estimation
    for i in range(max_iter):
        f = E - e * np.sin(E) - l        # f(E)
        df = 1 - e * np.cos(E)           # f'(E)
        E_new = E - f / df               # Newton-Raphson method for find roots
        if abs(E_new - E) < tol:
            return E_new
        E = E_new

def position(t):
    t = Time(t, format ='iso', scale ='utc')
    delta_t = (t - tp).to('s').value
    l = np.sqrt(GM / a**3) * delta_t
    E = newton(l, e)
    f = 2 * np.arctan2(np.sqrt((1 + e)/(1 - e)) * np.tan(E / 2), 1) # Relation between anomalies
    r = a*(1-e**2) / (1 + e * np.cos(f)) # 
    phi = f + w
    return r, np.degrees(phi)

def orbit():
    global r_list, t_list 

    T = 2 * np.pi * np.sqrt(a**3 / GM)  # Orbital period in seconds
    n = 500
    times = [tp + TimeDelta(i * T / n, format='sec') for i in range(n)]

    x_list = [] #  Calculate positions and store radii and times
    y_list = []
    r_list = []
    t_list = []

    for t in times:
        r, phi = position(t.iso)  
        phi_rad = np.radians(phi)
        x = r * np.cos(phi_rad)
        y = r * np.sin(phi_rad)
        x_list.append(x)
        y_list.append(y)
        r_list.append(r)
        t_list.append((t - tp).to('s').value)  

    #  Plot the orbit
    plt.figure(figsize=(6, 6))
    plt.plot(x_list, y_list, color='r', label='Satellite Orbit')
    plt.scatter(0, 0, color='b', label='Earth')
    plt.grid()
    plt.legend(loc='upper right')
    plt.xlabel("x (km)")
    plt.ylabel("y (km)")
    plt.title("Satellite Orbit")
    plt.show()

def date(r0):
    for i in range(len(r_list) - 1):
        r1 = r_list[i]
        r2 = r_list[i + 1]
        t1 = t_list[i]
        t2 = t_list[i + 1]

        # Check if r0 is between r1 and r2
        if (r1 - r0) * (r2 - r0) < 0:
            # Linear interpolation
            t0_sec = t1 + (r0 - r1) * (t2 - t1) / (r2 - r1)
            t0 = tp + TimeDelta(t0_sec * u.second)
    
            # Verification
            r_verif, _ = position(t0.iso)
            error = abs(r_verif - r0)

            print(f"r0 reached with error of {error:.6e} km")
            return t0

    print("r0 not reached in orbit.")
    return None


tp = Time("2025-03-31 00:00:00", format='iso', scale='utc')

R = 6378              # Earth radius in km
GM = 398600.4405      # km³/s²
a = 1.30262 * R       # Semi-major axis in km
e  = 0.16561          # Eccentricity
w =np.radians(15)     # Argument of pericenter in radians
l = np.sqrt(GM/a**3)  # Mean motion
    
r, phi = position("2025-04-01 00:00:00")
print(f"r(t) = {r:.10f} km")
print(f"phi(t) = {phi:.10f} grades")
orbit()  
    
t0 = date(1.5 * R)
if t0:
    print("The satellite reaches r0 at :", t0.iso)

