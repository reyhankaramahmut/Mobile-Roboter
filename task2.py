import numpy as np
from task1.transformations import *


class Robot:
    def __init__(self, x_r=2, y_r=1, theta=np.radians(30), l=0.6, h=0.2, r=0.1, a=0.1, b=0.1, l_1=0.5, l_2=0.5):
        self.x_r = x_r
        self.y_r = y_r
        self.theta = theta
        self.l = l
        self.h = h
        self.r = r
        self.a = a
        self.b = b
        self.l_1 = l_1
        self.l_2 = l_2

    def forward_kinematics(self, alpha=np.radians(40), beta_1=np.radians(30), beta_2=np.radians(-10)):
        p_a2 = (0, 0, 0, 1)
        pass

    def inverse_kinematics(self, p_r):
        pass


def draw_circle(robot, km_r=(1, 0, 0.55, 1), radius=0.25, positions_in_circle=50):
    # positions_in_circle specifies how many points of the circle to be drawn should be approached by the arm.
    # This function is not intended for plotting. Instead, it calculates the angular progression.
    pass


def plot_angles(alphas, beta_1s, beta_2s, positions_in_circle=50):
    pass


def plot_circle(reached_points):
    pass


if __name__ == '__main__':
    # Create plots with regular execution. Everything else should be run within tests.
    plot_angles()

    plot_circle()
