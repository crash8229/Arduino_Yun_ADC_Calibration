import serial
import os

if os.path.isfile("results.txt"):
    os.os.remove("results.txt")
file = open("results.csv", "w")
file.write("Voltage,Analog0,Analog1,Analog2,Analog3,Analog4,Analog5\n")
port = serial.Serial(port="COM17", baudrate=115200)

increment = int(input("Enter mV increment -> "))
numberOfPoints = int(input("How many data points do you want to collect per increment? -> "))

print("\nSet Voltage to value shown then press \'enter\'\n")
for mV in range(0, 5001, increment):
    result = str()
    average = [0, 0, 0, 0, 0, 0]
    dataset = list()
    input("Voltage: {0}".format(mV / 1000))
    port.reset_input_buffer()
    port.readline()
    port.reset_input_buffer()
    port.readline()
    for i in range(0, numberOfPoints):
        dataset.append(port.readline().decode("UTF-8"))
    for data in dataset:
        data = data.strip()
        data = data.split()
        for i in range(0, len(data)):
            average[i] += int(data[i])
    for i in range(0, len(average)):
        average[i] = round(average[i] / numberOfPoints)
        result += "{0},".format(average[i])
        print("Analog {0}: {1}   ".format(i, average[i]), end="")
    file.write(result + '{0}\n'.format(mV / 1000))
    print("\n")

