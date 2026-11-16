import numpy as np

# OpenLoopControlResults

wm_ref =   np.array([300, 400, 200])
wm_exp =   np.array([250, 356, 147])
PWM_out =  np.array([200, 255, 133])
wm_error = wm_ref - wm_exp
pct_err =  wm_error/wm_ref

# PID values
# kp = 2.50
# ki = 1.5
# kd = 0.05

PID + FF 
# FF Gain = 0.6663
# kp = 1.2
# ki = 0.7
# kd = 0.01

