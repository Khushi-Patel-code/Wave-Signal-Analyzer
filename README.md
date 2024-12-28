# Signal Interference and Wave Analysis

This project simulates signal interference and visualizes waveforms in both time and distance domains. It computes the properties of two sinusoidal signals, determines their interference type, and plots the resulting waveforms.

## Features

- **Calculates Wave Properties:**
  - Angular Frequency: (ω = 2πf)
  - Wave Number: (k = 2π/λ)
  - Wavelength: (λ = c/f)

- **Signal Equation:**
  - `D(x,t) = A sin(kx - ωt + φ)`

- **Interference Type:**
  - Constructive Interference
  - Destructive Interference
  - Mixed Interference (Partial Constructive + Destructive)

- **Visualizations on Graph:**
  - Time-domain analysis at a fixed distance
  - Distance-domain analysis at a fixed time

- **User Inputs:**
  - Amplitude, frequency, and phase for two signals
  - Fixed distance and time values for analysis

## How It Works

1. **User Input:**  
   The program takes user input for signal properties:
   - Amplitude (in Volts)
   - Frequency (in Hertz)
   - Phase (in radians)
   - Fixed distance and time values for plotting

2. **Wave Calculations:**  
   Using the input, the program computes wave properties (wavelength, angular frequency, and wave number) and evaluates signal equations.

3. **Interference Type:**  
   Based on phase differences, the program determines whether the interference is:
   - Constructive
   - Destructive
   - Mixed

4. **Plot Generation:**  
   - **Time Domain:** Plots signal amplitudes over time at a fixed distance.
   - **Distance Domain:** Plots signal amplitudes over distance at a fixed time.

## Libraries Used
This project utilizes the following Python libraries:
- **NumPy**: For numerical calculations and array handling.
- **Matplotlib**: For generating the time-domain and distance-domain plots of the signals.
