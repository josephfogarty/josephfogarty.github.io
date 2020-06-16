---
layout: page
title: What is LES?
excerpt: "The importance of large-eddy simulations"
---

## Short Answer

A large-eddy simulation (LES) is a turbulence-resolving computational and numerical method that models fluid flow by solving the filtered equations of motion.

## Long Answer

Most geophysical flows are turbulent. Excluding subsurface flows, environmental fluids such as rivers, the atmosphere, and the ocean all have high _Reynolds numbers_ (a dimensionless number defined as the ratio between inertial and viscous forces), defined as
![$\text{Re}=\frac{UL}{\nu}$](https://render.githubusercontent.com/render/math?math=%24%5Ctext%7BRe%7D%3D%5Cfrac%7BUL%7D%7B%5Cnu%7D%24)
In the atmospheric boundary layer (ABL), the Reynolds number is very high, about 8 orders of magnitude, due to the turbulence generated from both mechanical shear and buoyancy. In a nutshell, turbulence can be defined as the swirling motion of fluids that occurs irregularly in space and time. A decomposition can be performed that assumes superposition of a mean flow and a range of chaotic motions, known as _Reynolds decomposition_. However, there are still interactions between the mean flow and turbulent motions that cannot be neglected.

To simulate the ABL, one could apply the Reynolds-Averaged Navier-Stokes (RANS) technique, in which only the dynamics of the mean flow are modeled, and the interaction of the mean flow with turbulence is parameterized. However, this essentially averages out all of the three-dimensional unsteady turbulence, which is inadequate because we _want_ to resolve turbulence in these simulations. Turbulence drastically enhances mixing and transport, and occurs mostly close to boundaries which is important for surface-atmosphere interactions.

Another method that is commonly used to simulate turbulence is a direct numerical simulation, which entails solving the Navier-Stokes equations directly. However, to do this, the computational domain must capture all scales of motion from the largest scales (the integral scale) to the smallest scales (the Kolmogorov scale). In fact, it can be shown that the number of floating-point operations needed to perform a DNS scales with the third power of the Reynolds number of the flow being simulated (see quick derivation <a href="docs\Relating_Reynolds_Number_to_DNS.pdf" download="Relating_Reynolds_Number_to_DNS.pdf">here</a>). So the number of floating point operations for a DNS of the entire ABL is about 24 floating point operations! This is beyond what is computationally possible today.

This brings us to the middle ground, the large eddy simulation (LES).
