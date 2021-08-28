import time
import pyvisa as visa
import numpy as np
from numpy import ndarray
import csv

rm=visa.ResourceManager()
li=rm.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which device?: ")
vi=rm.open_resource(li[int(choice)])
vi.timeout = 2000

print(vi.query("*idn?"))

# input start, target, and step voltage
start = input("Enter Start value?[V]: ")
target = input("Enter Target value?[V]: ")
step = input("Enter Step value[V]?: ")

# Set measurement range with two different range (forward / backward) with 0.1 step size
#voltageArrayForward = np.arange(-5.0, 5.1, 0.1).round(2)
#voltageArrayBackward = np.arange(4.9, -5.1, -0.1).round(2)
#voltageArrayForward = np.arange(float(start), float(target)+float(step), float(step)).round(2)
#voltageArrayBackward = np.arange(float(target) - float(step), float(start) - float(step), -float(step)).round(2)
voltageArray1 = np.arange(0, float(start), -float(step)).round(2)
voltageArray2 = np.arange(float(start), 0, float(step)).round(2)
voltageArray3 = np.arange(0, float(target) + float(step), float(step)).round(2)
voltageArray4 = np.arange(float(target)-float(step), 0-float(step), -float(step)).round(2)
voltageArray = np.append(voltageArray1, voltageArray2)
voltageArray = np.append(voltageArray, voltageArray3)
voltageArray = np.append(voltageArray, voltageArray4)
print(voltageArray)
count = np.size(voltageArray)


#Measurement mode? (CPD, CPG, CPRP, etc., see a program manual
MesOp = "CPG"
vi.write("func:imp " + MesOp)

#Measurement speed (MED, ?)
MesSpd = "MED"
vi.write("APER " + MesSpd)

print("Function - ",vi.query("func:imp?"))

setBias = "bias:state "   ##set variable. For string insert, " ~~ " is needed. 895 can do action once it read
vi.write(setBias + "1")
setFreq = "freq 1MHz"
vi.write(setFreq)
setVolt = "Volt 1 V"
vi.write(setVolt)


print(setFreq)
print("Voltage level" + setVolt)
with open("output.csv", "w", newline = "") as f:
    #wr = csv.writer(f)
    #cvswriter.writerow(fields)
    for i in range(int(count)):
        voltage = voltageArray[i]
        cmd = "bias:volt "+str(voltage)
        vi.write(cmd)
        resp = str(voltage)+","+vi.query("fetch?")
        print(resp.rstrip('\n'))
        #print(type(resp))
        #csv.writer(f, delimiter=',')
        #np.savetxt(f, resp, delimiter = ",")
f.close()


vi.write(setBias + "0")

vi.write("*rst")
