from task1.transformations import *
import numpy as np

def exercise_21_a_t_ab():
    t = trans(np.array([-2,0,0]))
    r = rot2trans(rotz(np.radians(180)))
    return np.matmul(t,r)

def exercise_21_a_t_bc():
    t = trans(np.array([-4,-1,0]))
    r = rot2trans(rotz(np.radians(-90)))
    return np.matmul(t,r)

def exercise_21_a_t_ac():
    t = trans(np.array([2,1,0]))
    r = rot2trans(rotz(np.radians(90)))
    return np.matmul(t,r)

def exercise_21_b_t_ac():
    return np.matmul(exercise_21_a_t_ab(), exercise_21_a_t_bc())

def exercise_21_c_t_ca():
    t = trans(np.array([2,1,0]))
    r = rot2trans(rotz(np.radians(90)))
    t_ac = np.matmul(t,r)
    return np.linalg.inv(t_ac)

def exercise_21_d(pb):
    if len(pb) < 4:
        pb = np.append(pb,1)
    result = np.matmul(exercise_21_a_t_ab(),pb)
    return result[0:3]

# Task 2.2 from lecture
def exercise_22_a_t_oa():
    t = trans(np.array([1,1]))
    r = rot2trans(rot(np.radians(0)))
    return np.matmul(t,r)

def exercise_22_a_t_ob():
    t = trans(np.array([3,2]))
    r = rot2trans(rot(np.radians(30)))
    return np.matmul(t,r)

def exercise_22_b(pb):
    if len(pb) < 3:
        pb = np.append(pb,1)
    result = np.matmul(exercise_22_a_t_ob(),pb)
    return result[0:2]

def exercise_22_c_t_ab():
    t_oa_i = np.linalg.inv(exercise_22_a_t_oa())
    t_ob = exercise_22_a_t_ob()
    return np.matmul(t_oa_i,t_ob)

def exercise_22_d(pb):
    if len(pb) < 3:
        pb = np.append(pb,1)
    result = np.matmul(exercise_22_c_t_ab(), pb)
    return result[0:2]

def exercise_22_e(pa):
    if len(pa) < 3:
        pa = np.append(pa,1)
    result = np.matmul(exercise_22_c_t_ab(), pa)
    return result[0:2]
