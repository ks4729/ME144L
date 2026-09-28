import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
filename = 'beamtest1.csv'
data = pd.read_csv(filename)

time = np.array(data.Time)
x = np.array(data.accX) # [counts]
y = np.array(data.accY) # [counts]
z = np.array(data.accZ) # [counts]
wx = np.array(data.wx)  # [counts]
wy = np.array(data.wy)  # [counts]
wz = np.array(data.wz)  # [counts]

# convert counts to gs
conv_accel =  0.488e-3 # 16g range; convert from int to float in [g]
# NOTE: 0.061 for 2g, 0.122 for 4g, 0.244 for 8g, 0.488 for 16g
accx_g = conv_accel*x   # [g]
accy_g = conv_accel*y   # [g] 
accz_g = conv_accel*z  # [g]

conv_gyro =  17.50e-3   #  500 dps range; convert from int to float in [dps]
# NOTE: 4.375 for 125 dps, 8.75 for 250, 17.50 for 500, 35 for 1000, 70 for 2000
wx_dps = conv_gyro*wx   # [dps]
wy_dps = conv_gyro*wy   # [dps]
wz_dps = conv_gyro*wz   # [dps]

plt.figure()
plt.plot(time, accx_g, label='x')
plt.plot(time, accy_g, label='y')
plt.plot(time, accz_g, label='z')
plt.grid()
plt.legend()
plt.xlabel('Time [s]')
plt.ylabel("Acceleration [g]")
plt.title("Acceleration vs Time")

plt.figure()
plt.plot(time, wx_dps, label='wx')
plt.plot(time, wy_dps, label='wy')
plt.plot(time, wz_dps, label='wz')
plt.grid()
plt.legend()
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [deg/sec]')
plt.title('Gyro Data vs Time')
plt.show()

'''
with open("output0g.txt", "w") as f:
    print("0g test, Accel in X mean: " + str(np.mean(accx_g)) + "    Accel in X std: " + str(np.std(accx_g)), file=f)
    print("0g test, Accel in Y mean: " + str(np.mean(accy_g)) + "    Accel in Y std: " + str(np.std(accy_g)), file=f)
    print("0g test, Accel in Z mean: " + str(np.mean(accz_g)) + "    Accel in Z std: " + str(np.std(accz_g)), file=f)

    print("0g test, Gyro data in X mean: " + str(np.mean(wx_dps)) + "    Gyro data in X std: " + str(np.std(accx_g)), file=f)
    print("0g test, Gyro data in Y mean: " + str(np.mean(wy_dps)) + "    Gyro data in Y std: " + str(np.std(wy_dps)), file=f)
    print("0g test, Gyro data in Z mean: " + str(np.mean(wz_dps)) + "    Gyro data in Z std: " + str(np.std(wz_dps)), file=f)
    '''