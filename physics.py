import math
import numpy as np

G = 9.81  # universal gravity constant, 9.81 m/s^2
density_water = 1000 # density of water is 1000 kg/m^3
# mass_of_auv = 100 # defaults to 100 Kg
volume_of_auv = 0.1 # defaults to 0.1 m^3
# thruster_distance = 0.5 # defaults to 0.5 m
# inertia_of_AUV = 1 # defaults to 1 kg * m^2


def calculate_buoyancy(
    v, density_fluid
):  # v should be iin m^3, density should be in kg/m^3, G is gravity = 9.81 m/s^2
    """
    This function calculates the buoyancy force based on the buoyancy force equation, p * V * g = Fb, and returns it
    """
    buoyancy_force = density_fluid * v * G
    return buoyancy_force


def will_it_float(v, mass):  # v in m^3, mass in kg
    """
    determines if an object will float in water by comparing the objects density to the density of water
    """
    density_of_object = mass / v
    if density_of_object > 1000: #density of water is 1000 kg/m^3
        return False
    elif density_of_object < 1000:
        return True
    
def calculate_pressure(depth): # p = density * gravity * depth
    '''
    calculates pressure in water based on the depth that the object is at using the equation pressure(Pa) = density(kg/m^3) * gravity(m/s^2) * depth(m), returns the pressure in pascals
    '''
    pressure = density_water * G * depth
    return pressure # pressure should be returned in pascals

def calculate_acceleration(F, m): # F is force applied to object in Newtons, m is the mass of object in Kg
    '''
    calculates acceleration based on newtons second law F = ma, but rewritten to solve for a. returns the acceleration in m/s^2. takes arguments F in Newtons, and mass in Kg
    '''
    acceleration = F/m
    return acceleration

def calculate_angular_acceleration(tau, I): # angular acceleration = torque (tau) / moment of inertia (I)
    """ 
    tau in Nm, I in kg*m^2, returns angular acceleration
    """
    angular_acceleration = tau / I
    return angular_acceleration


def calculate_torque(F_magnitude, F_direction_deg, r): # torque = distance from axis of rotation * force applied * angle between  force and lever arm
    '''
    calculates torque with torque = distance from axis of rotation * force applied, returns the torque
    '''
    F_direction = math.radians(F_direction_deg)
    torque  = r * F_magnitude  * math.sin(F_direction)
    return torque


def calculate_moment_of_inertia(m, r): 
    '''
    the equation for calculating the moment of inertia is given by the following equation for rigid bodies: moment of inertia = mass of object * (distance from axis of ratation to the center of mass of the object)^2
    '''
    moment_of_inertia = m * r**2
    return moment_of_inertia

def calculate_auv_acceleration(F_magnitude, F_angle, mass_of_auv):
    F_x = F_magnitude * math.cos(F_angle)
    F_y = F_magnitude * math.sin(F_angle)
    a_x = F_x / mass_of_auv
    a_y = F_y / mass_of_auv
    return (a_x, a_y)

def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia = 1.0, thruster_distance = 0.5): # angaccel = torque / moment of inertia, torque = distance from axis of rotation * force applied, moment of inertia = mass * distance ^2
    torque = thruster_distance * F_magnitude * math.sin(F_angle)
    angular_acceleration = torque / inertia
    return angular_acceleration


def calculate_auv2_acceleration(T, alpha, theta, mass = 100.0):
    cos_alpha = math.cos(alpha)
    sin_alpha = math.sin(alpha)

    F_x = (-T[0] + T[1] + T[2] - T[3]) * cos_alpha
    F_y = (T[0] + T[1] - T[2] - T[4]) * sin_alpha

    a_x = F_x / mass
    a_y = F_y / mass
    return (a_x, a_y)

def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia):
    torque_factor = (L * math.sin(alpha)) + (l * math.cos(alpha))
    toruqe = (T[0] + T[1] + T[2] + T[3]) * torque_factor
    angular_acceleration = toruqe / inertia
    return angular_acceleration

def simulate_auv2_motion(T, alpha, L, l, mass = 100.0, inertia = 100.0, dt = .1, t_final = 10.0, x0 = 0.0, y0 = 0.0, theta0 = 0.0):
    pass