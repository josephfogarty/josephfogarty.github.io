---
layout: page
title: What is LES?
excerpt: "The importance of large-eddy simulations"
---

## Short Answer

A large-eddy simulation (LES) is a turbulence-resolving computational and numerical method that models fluid flow by solving the filtered equations of motion.

## Long Answer

Most geophysical flows are turbulent. Excluding subsurface flows, environmental fluids such as rivers, the atmosphere, and the ocean all have high _Reynolds numbers_ (a dimensionless number defined as the ratio between inertial and viscous forces), defined as
[$\text{Re}=\frac{UL}{\nu}$](https://render.githubusercontent.com/render/math?math=%24%5Ctext%7BRe%7D%3D%5Cfrac%7BUL%7D%7B%5Cnu%7D%24)
In the atmospheric boundary layer (ABL), ![$\text{Re}\approx10^8](https://render.githubusercontent.com/render/math?math=%24%5Ctext%7BRe%7D%5Capprox10%5E8), due to the turbulence generated from mechanical shear and buoyancy.

In fact, the number of floating-point operations needed to perform a DNS scales with ![$\text{Re}^3](https://render.githubusercontent.com/render/math?math=%24%5Ctext%7BRe%7D%5E3) (see quick derivation [here](docs\Relating_Reynolds_Number_to_DNS.pdf "Computational Cost of DNS")).

However, we _want_ to resolve turbulence in these simulations. Turbulence drastically enhances mixing and transport, and occurs mostly close to boundaries which is important for surface-atmosphere interactions.
