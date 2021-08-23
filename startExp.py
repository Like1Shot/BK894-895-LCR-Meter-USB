import time
import pyvisa as visa
import numpy as np
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

voltageArrayForward = np.arange(float(start), float(target)+float(step), float(step)).round(2)
voltageArrayBackward = np.arange(float(target) - float(step), float(start) - float(step), float(step)).round(2)
voltageArray = np.append(voltageArrayForward, voltageArrayBackward)
print(voltageArray)

#funtionSetting = input("Function type: ")
print("Function - ",vi.query("func:imp?"))

setBias = "bias:state "
vi.write(setBias + "1")

freqValue = input("Set Frequency(ex. 1MHz): ")
vi.write("freq" + freqValue)

fields = ["Bias Volatage[V]", "Cp", "d"]

with open("terminalOutput.csv", "w", newline = "") as f:
    cvswriter = csv.writer(f)
    cvswriter.writerow(fields) 

    for i in voltageArray:
        voltage = voltageArray[i]
        cmd = "bias:volt "+str(voltage)
        vi.write(cmd)
        resp = str(voltage)+","+vi.query("fetch?") 
        csvwriter.writerow()
        print(resp)
f.close()

vi.write(setBias + "0")
