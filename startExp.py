from time import sleep
import pyvisa as visa
import numpy as np
import csv

#device info and select
rm=visa.ResourceManager()
li=rm.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which device?: ")
vi=rm.open_resource(li[int(choice)])
vi.timeout = 1000
print(vi.query("*idn?"))

#funtionSetting = input("Function type: ")
print("Function - ",vi.query("func:imp?"))

# turn on DC bias - 1
biasState = input(("Turn on DC Bias?: (yes-1, no-0)")
vi.write("bias:state " + biasState)

# set constant frequency
freqValue = input("Set Frequency(ex. 1MHz): ")
vi.write("freq " + freqValue)

# input start, target, and step voltage
start = input("Enter Start value?[V]: ")
target = input("Enter Target value?[V]: ")
step = input("Enter Step value[V]?: ")

#voltageArrayForward = np.arange(-5.0, 5.1, 0.1).round(2)
#voltageArrayBackward = np.arange(4.9, -5.1, -0.1).round(2)
voltageArrayForward = np.arange(float(start), float(target)+float(step), float(step)).round(2)
voltageArrayBackward = np.arange(float(target) - float(step), float(start) - float(step), float(step)).round(2)
voltageArray = np.append(voltageArrayForward, voltageArrayBackward)
print(voltageArray)

#fields = ["Bias Volatage[V]", "Cp", "d"]
with open("output.csv", "w", newline = "") as f:
    wr = csv.writer(f)
    #wr.writerow(fields) 
    for i in range(voltageArray):
        voltage = voltageArray[i]
        cmd = "bias:volt "+str(voltage)
        vi.write(cmd)
        resp = str(voltage)+","+vi.query("fetch?") 
        print(resp)
        #np.savetxt(f, delimiter = ",", fmt="%f")
        wr.writerow(resp)
f.close()

# initial DC bias setting - off
vi.write("bias:state " + "0")
