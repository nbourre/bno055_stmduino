import serial
import time
import csv 
from datetime import datetime

ser = serial.Serial('com3',115200)
ser.flushInput()

def main():
    now = datetime.now()
    prefix = now.strftime("%Y-%m-%d_%H;%M;%S")
    while True:
        try:
            ser_bytes = ser.readline()
            #decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            decoded_bytes = ser_bytes[:-2].decode("utf-8")+"\n"
            print(decoded_bytes)
            with open(prefix + "_databrute.csv","a") as f:
                #writer = csv.writer(f.write)
                f.writelines(decoded_bytes)
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            break
  
if __name__ == '__main__':
    main()


def main2():
    while True:
            try:
                ser_bytes = ser.readline()
                #decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                decoded_bytes = ser_bytes[:-2].decode("utf-8")
                print(decoded_bytes)
                with open("databrute.csv","a") as f:
                    writer = csv.writer(f,delimiter=",")
                    writer.writerow([decoded_bytes])
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                break
