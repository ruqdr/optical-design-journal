# Optical Design Formulary

A collection of essential formulas for optical lens design.

## Geometric Optics

### Refraction
- **Snell's Law**: $n_1 \sin\theta_1 = n_2 \sin\theta_2$
- **Critical angle for total internal reflection**: $\theta_c = \sin^{-1}\left(\frac{n_2}{n_1}\right)$ ($n_1 > n_2$)

### Thin Lenses
- **Lensmaker's formula** (thin lens in air):
  $$
  \frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)
  $$
- **Plano‑convex lens** ($R_2 = \infty$):
  $$
  \frac{1}{f} = \frac{n-1}{R_1} \quad \Rightarrow \quad R_1 = (n-1)f
  $$
- **Bi‑convex symmetric lens** ($R_1 = -R_2 = R$):
  $$
  \frac{1}{f} = \frac{2(n-1)}{R}
  $$

### Magnification
- **Lateral (transverse) magnification**:
  $$
  m = -\frac{s_i}{s_o}
  $$
  where $s_o$ = object distance, $s_i$ = image distance (measured from the lens).
- **Angular magnification of a simple magnifier** (relaxed eye, image at infinity):
  $$
  M = \frac{25\ \text{cm}}{f}
  $$
- **Angular magnification when image at near point** (25 cm):
  $$
  M = 1 + \frac{25\ \text{cm}}{f}
  $$

### Optical Invariants
- **Lagrange invariant** (in a rotationally symmetric system):
  $$
  \mathcal{H} = n\,y\,\theta = \text{constant}
  $$
  where $y$ is the ray height and $\theta$ the paraxial angle.

### Surface Sagitta
For a spherical surface of radius $R$ and semi‑diameter $r$:
$$
z = R - \sqrt{R^2 - r^2} \approx \frac{r^2}{2R} \quad\text{(paraxial approximation)}
$$

## Aberrations

*To be filled after studying Chapter 2.*

## Paraxial Ray Tracing
- **Refraction at a single surface**:
  $$
  n' u' = n u - \frac{n' - n}{R} y
  $$
  where $u$ is the paraxial angle, $y$ the ray height, $R$ the radius of curvature.
- **Transfer to next surface**:
  $$
  y_{i+1} = y_i + d_i\,u_i'
  $$
  with $d_i$ the distance between surfaces.

## Chromatic Aberration
- **Abbe number**:
  $$
  V_d = \frac{n_d - 1}{n_F - n_C}
  $$
- **Chromatic focal shift** (thin lens):
  $$
  \frac{\Delta f}{f} = -\frac{1}{V_d}
  $$

---

*Last updated after Exercise 1.1 (magnifier design).*