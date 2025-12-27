#!/usr/bin/env python3
"""
Simple magnifier design calculation for Exercise 1.1.
"""

# Parameters
M = 5.0                     # magnification
near_point = 250.0          # near point of eye (mm)
n = 1.5168                  # refractive index of N-BK7

# Focal length from magnification (relaxed eye)
f = near_point / M          # mm
print(f"Magnification M = {M}")
print(f"Near point (relaxed eye) = {near_point} mm")
print(f"Required focal length f = {near_point} mm / {M} = {f:.2f} mm")

# Radius of curvature for plano-convex lens
# Lensmaker's formula: 1/f = (n-1)/R  (R2 = infinity)
R = (n - 1) * f
print(f"\nRefractive index n = {n}")
print(f"Radius of curvature R = (n - 1) * f = {R:.3f} mm")
print(f"R ≈ {R:.1f} mm")

# Optional: sagitta for a given semi-diameter (e.g., lens radius 20 mm)
semi_diameter = 20.0        # mm
sag = R - (R**2 - semi_diameter**2)**0.5
print(f"\nSagitta for semi‑diameter {semi_diameter} mm:")
print(f"sag = R - sqrt(R² - r²) = {sag:.3f} mm")

# Output summary
print("\n=== Design Summary ===")
print(f"Magnifier: {M}×")
print(f"Focal length: {f:.1f} mm")
print(f"Radius of curvature (convex surface): {R:.1f} mm")
print(f"Glass: N‑BK7 (n={n})")
