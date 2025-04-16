# Slip Reference: Fuzzy Logic Application - Rule (b)

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# --- Fuzzy System: Motor Action based on Traffic Signal ---

# Define fuzzy input variable
traffic_signal = ctrl.Antecedent(np.arange(0, 3, 1), 'traffic_signal')
motor_action = ctrl.Consequent(np.arange(0, 101, 1), 'motor_action')  # 0 = Stop, 100 = Fast

# Linguistic values for traffic signal
# 0 = Red, 1 = Yellow, 2 = Green
traffic_signal['red'] = fuzz.trimf(traffic_signal.universe, [0, 0, 1])
traffic_signal['yellow'] = fuzz.trimf(traffic_signal.universe, [0, 1, 2])
traffic_signal['green'] = fuzz.trimf(traffic_signal.universe, [1, 2, 2])

# Motor actions: 0 (Stop), 50 (Slow), 100 (Fast)
motor_action['stop'] = fuzz.trimf(motor_action.universe, [0, 0, 50])
motor_action['slow'] = fuzz.trimf(motor_action.universe, [30, 50, 70])
motor_action['fast'] = fuzz.trimf(motor_action.universe, [60, 100, 100])

# Define fuzzy rule
rule_stop = ctrl.Rule(traffic_signal['red'], motor_action['stop'])

# Control system
traffic_ctrl = ctrl.ControlSystem([rule_stop])
traffic_sim = ctrl.ControlSystemSimulation(traffic_ctrl)

# Set input and compute output
traffic_sim.input['traffic_signal'] = 0  # Red light
traffic_sim.compute()
print(f"Motor Action for RED signal: {traffic_sim.output['motor_action']:.2f} (Expected: Stop)")

# Optional: View the membership functions
traffic_signal.view()
motor_action.view()
