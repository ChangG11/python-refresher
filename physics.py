import math
import numpy as np

G = 9.81  # universal gravity constant, 9.81 m/s^2
density_water = 1000 # density of water is 1000 kg/m^3
mass_of_auv = 100 # defaults to 100 Kg
volume_of_auv = 0.1 # defaults to 0.1 m^3
thruster_distance = 0.5 # defaults to 0.5 m
inertia_of_AUV = 1 # defaults to 1 kg * m^2


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


def calculate_torque(F_magnitude, r): # torque = distance from axis of rotation * force applied
    '''
    calculates torque with torque = distance from axis of rotation * force applied, returns the torque
    '''
    torque  = r * F_magnitude 
    return torque


def calculate_moment_of_inertia(m, r): 
    '''
    the equation for calculating the moment of inertia is given by the following equation for rigid bodies: moment of inertia = mass of object * (distance from axis of ratation to the center of mass of the object)^2
    '''
    moment_of_inertia = m * r^2
    return moment_of_inertia

def calculate_auv_acceleration(F_magnitude, F_angle):
    F_x = F_magnitude * np.cos(F_angle)
    F_y = F_magnitude * np.sin(F_angle)
    a_x = F_x / mass_of_auv
    a_y = F_y / mass_of_auv
    acceleration_of_auv = np.sqrt(a_x**2 + a_y**2)
    return acceleration_of_auv

def calculate_auv_angular_acceleration(F_magnitude, F_angle): # angaccel = torque / moment of inertia, torque = distance from axis of rotation * force applied, moment of inertia = mass * distance ^2
    torque = thruster_distance * calculate_auv_acceleration(F_magnitude, F_angle)
    angular_acceleration = torque / inertia_of_AUV
    return angular_acceleration