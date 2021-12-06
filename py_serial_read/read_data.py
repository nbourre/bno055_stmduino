import csv
import serial
import time

arduino = serial.Serial(port='COM23', baudrate=115200, timeout=.1)

def read_data():
    time.sleep(0.05)
    data = arduino.readline().decode('utf-8')[:-1]
    return data


#function that show a menu with 3 qchoices and return the choice
def menu():
    print("1. Read data from Arduino")
    print("2. Write data to Arduino")
    print("3. Exit")
    return input("Enter your choice: ")

def reading_loop():
    data = ""
    count = 0
    data_to_display = ""
    while True:
        try:
            current = read_data()
            data += current
            data_to_display += current
            count += 1
            if count % 10:
                print(data_to_display)
                data_to_display = ""
        except KeyboardInterrupt:
            print("\nExiting loop...")
            break
    return data

def main():
    choice = menu()
    while choice != '3':
        if choice == '1':
            data = reading_loop()
            with open('data.csv', 'w') as f:
                f.write(data)
        elif choice == '2':
            print("Write data to Arduino")
        else:
            print("Invalid choice")
        choice = menu()
    
if __name__ == '__main__':
    main()