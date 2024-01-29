
import numpy as np
import matplotlib.pyplot as plt


n_air = 1
n_water = 1.334


def calculate_coefficient(n_air, n_water, theta_i, theta_t):
    R_s_e = (n_air * np.cos(theta_i) - n_water * np.cos(theta_t)) / (n_air * np.cos(theta_t) + n_water * np.cos(theta_i))
    R_p_e = (n_air * np.cos(theta_t) - n_water * np.cos(theta_i)) / (n_air * np.cos(theta_i) + n_water * np.cos(theta_t))
    R_s_i = (n_water * np.cos(theta_i) - n_air * np.cos(theta_t)) / (n_water * np.cos(theta_i) + n_air * np.cos(theta_t))
    R_p_i = (n_water * np.cos(theta_i) - n_air * np.cos(theta_t)) / (n_water * np.cos(theta_i) + n_air * np.cos(theta_t))

    return R_s_e, R_p_e, R_s_i, R_p_i



