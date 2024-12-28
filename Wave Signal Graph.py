import numpy as np
import matplotlib.pyplot as plt

# Calculating the angular frequncy ω = 2πf
def calculate_angular_frequency(frequency):
    return 2 * np.pi * frequency

# Calculating the wave number k = 2π/λ
def calculate_wave_number(wavelength):
    return 2 * np.pi / wavelength

#calculating the wavelength λ = c/f  
def calculate_wavelength(frequency):
    c = 3 * 10**8           # Speed of light in m/s
    return c / frequency

# Calculating the signal equation D(x,t) = A sin(kx – ωt + φ)
def calculate_signal_equation(A ,k , omega, x, t , phase):
    return A * np.sin(k * x - omega * t + phase)

#deciding the interference type
def define_interference_type(phase1 , phase2 ):
    phase_difference = (phase2 - phase1) % (2 * np.pi)
    tolerance = 0.01  #using tolerance as phase is a float
    if phase_difference < tolerance or phase_difference > (2 * np.pi - tolerance):
        interference_type = "Constructive Interference"
    elif abs(phase_difference - np.pi) < tolerance:
        interference_type = "Destructive Interference"
    else:
        interference_type = "Constructive Interference + Destructive Interference"

    return interference_type

def validate_input(prompt , value_type=float , min_value=None, max_value=None):
    while True:
        try:
            value = value_type(input(prompt))   #coverts input to float
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):    #checks if value between min and max
                print(f"Value must be between {min_value} and {max_value}. Try again!")
            else:
                return value
        except ValueError as e:  #error when tries to covert invalid value to float  #e stores specific error mssg
            print(f"Invalid input. Please enter a valid {value_type.__name__}. \nError: {str(e)}")      #displays the error as string for user
# value_type.__name__ gets the expected value in the code i.e float in here.

print("\nEnter the properties for Signal D1:")
print("================ Wave 1 ================")
A1 = validate_input("\nAmplitude A1 (Volts, 0V-25V): ", float, 0, 25)   #Amplitude not too high
f1 = validate_input("\nFrequency f1 (Hertz, non-negative): ", float, 0)   #frequency in Hz can be high
phase1 = validate_input("\nPhase φ for Signal D1 (in radians, 0-2π(6.28 rads)): ", float, 0, 2 * np.pi)  #want φ between 0 and 2π

print("\nEnter the properties for Signal D2:")
print("================ Wave 2 ================")
A2 = validate_input("\nAmplitude A2 (Volts, 0-25): ", float, 0, 25)
f2 = validate_input("\nFrequency f2 (Hertz, non-negative): ", float, 0)
phase2 = validate_input("\nPhase φ for Signal D2 (in radians, 0-2π): ", float, 0, 2 * np.pi)

#asking user for the values of fixed distance and time for the graph
x_fix = float(input("\nEnter the fixed distance (x1) for time domain analysis: "))
t_fix = float(input("\nEnter the fixed time (t1) for distance domain analysis: "))

# Calculating angular frequencies and wave numbers for signals
lambda1 = calculate_wavelength(f1)
omega1 = calculate_angular_frequency(f1)
k1 = calculate_wave_number(lambda1)

lambda2 = calculate_wavelength(f2)
omega2 = calculate_angular_frequency(f2)
k2 = calculate_wave_number(lambda2)

interference_type = define_interference_type(phase1 , phase2)

# Create arrays of time (0 to 1 sec) with 1000 data points
time_values = np.linspace(0, 1, 1000)  

# Signal Equation of D1 and D2 over time at fixed distance
D1_time = calculate_signal_equation(A1 ,k1, omega1, x_fix, time_values , phase1) 
D2_time = calculate_signal_equation(A2 ,k2, omega2, x_fix, time_values , phase2)
sum_time = D1_time + D2_time 

# Plot signals in time domain at a fixed distance
plt.figure(figsize=(12, 6))    #Plot window --> 12 inches wide, 6 inches tall
plt.plot(time_values, D1_time, label="D1 (Time Domain)")  #Plots D1_time (y-axis) v.s time_values(x-axis)
plt.plot(time_values, D2_time, label="D2 (Time Domain)")  #label -->label for the legend
plt.plot(time_values, sum_time, label="D_Sum  (Time Domain)", linestyle="--")  #linestyle --> changing the style of the line
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (Volts)")
plt.title(f"Time Domain at Fixed Distance x = {x_fix} meters , {interference_type}")
plt.legend()  #identifies which line corresponds to which signal.
plt.grid(True)
plt.show()

distance_values = np.linspace(0, 2 * max(lambda1, lambda2), 1000)  

#Signal equation for D1 and D2 over distance at fixed time
D1_distance = calculate_signal_equation(A1, k1, omega1, distance_values, t_fix, phase1)
D2_distance = calculate_signal_equation(A2, k2, omega2, distance_values, t_fix, phase2)
sum_distance = D1_distance + D2_distance

# Plot signals in distance domain at a fixed time
plt.figure(figsize=(12, 6))
plt.plot(distance_values, D1_distance, label="D1 (Distance Domain)")
plt.plot(distance_values, D2_distance, label="D2 (Distance Domain)")
plt.plot(distance_values, sum_distance, label="D_Sum (Distance Domain)", linestyle="--")
plt.xlabel("Distance (meters)")
plt.ylabel("Amplitude (Volts)")
plt.title(f"Distance Domain at Fixed Time t = {t_fix} seconds , {interference_type}")
plt.legend()
plt.grid(True)
plt.show()