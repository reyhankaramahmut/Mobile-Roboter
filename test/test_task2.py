import numpy as np
from task2.task2 import *


# TODO: Extend tests for more test cases if necessary.

def test_forward_kinematics():
    robot = Robot()
    result = robot.forward_kinematics().round(3)
    expected = (2.525, 1.973, 0.821, 1.000)
    assert np.array_equal(result, expected)


def test_inverse_kinematics():
    robot = Robot()  # TODO: Adjust params for inverse_kinematics
    p_r = ()
    res_alpha, res_beta_1, res_beta2 = robot.inverse_kinematics(p_r)
    assert False


def test_draw_circle():
    # TODO: Test for correct alphas, beta_1s, beta_2s
    assert False


