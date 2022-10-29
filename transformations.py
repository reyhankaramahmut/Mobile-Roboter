from cmath import pi
import numpy as np
import math as m


def rot(theta: float):
    return np.array([
        [m.cos(theta), -m.sin(theta)],
        [m.sin(theta), m.cos(theta)]
    ])


def rotx(theta: float):
    return np.array([
        [1, 0, 0],
        [0, m.cos(theta), -m.sin(theta)],
        [0, m.sin(theta), m.cos(theta)]
    ])


def roty(theta: float):
    return np.array([
        [m.cos(theta), 0, m.sin(theta)],
        [0, 1, 0],
        [-m.sin(theta), 0, m.cos(theta)]
    ])


def rotz(theta: float):
    return np.array([
        [m.cos(theta), -m.sin(theta), 0],
        [m.sin(theta), m.cos(theta), 0],
        [0, 0, 1]
    ])


def rot2trans(r: np.ndarray):
    return np.vstack((np.hstack((r, np.zeros((r.shape[0], 1))), np.hstack((np.zeros((1, r.shape[0])), [[1]])))))


def trans(t: np.ndarray):
    if len(t) == 2:
        return np.array([
            [1, 0, t[0]],
            [0, 1, t[1]],
            [0, 0, 1]
        ])
    else:
        return np.array([
            [1, 0, 0, t[0]],
            [0, 1, 0, t[1]],
            [0, 0, 1, t[2]],
            [0, 0, 0, 1]
        ])


if __name__ == "__main__":
    print(rotz(np.pi).round(3))
