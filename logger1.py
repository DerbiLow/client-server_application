import GPUtil
import psutil
import platform
from datetime import datetime
import time
from threading import Thread
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("info", 10000))

def encrypt(): # Самая простая функция шифрования
    for i in  range (len(message)):
        if message[i] == "0":
            message[i] = ")"
        elif message[i] == "1":
            message[i] = "!"
        elif message[i] == "2":
            message[i] = "@"
        elif message[i] == "3":
            message[i] = "#"
        elif message[i] == "4":
            message[i] = "$"
        elif message[i] == "5":
            message[i] = "%"
        elif message[i] == "6":
            message[i] = "^"
        elif message[i] == "7":
            message[i] = "&"
        elif message[i] == "8":
            message[i] = "*"
        elif message[i] == "9":
            message[i] = "("

def decrypt(): # Самая простая функция дешифрования
    for i in  range (len(data)):
        if data[i] == ")":
            data[i] = "0"
        elif data[i] == "!":
            data[i] = "1"
        elif data[i] == "@":
            data[i] = "2"
        elif data[i] == "#":
            data[i] = "3"
        elif data[i] == "$":
            data[i] = "4"
        elif data[i] == "%":
            data[i] = "5"
        elif data[i] == "^":
            data[i] = "6"
        elif data[i] == "&":
            data[i] = "7"
        elif data[i] == "*":
            data[i] = "8"
        elif data[i] == "(":
            data[i] = "9"
    

iteration = 0
message = ""

while True:
    if iteration == 0: # Самая простая идентификация устройств
        message = f"{platform.uname().system}_{platform.uname().node}_{platform.uname().version}_{platform.uname().machine}"
        message = list(message)
        encrypt()
        message = "".join(message)
        client.send(message.encode("utf-8")) # Идентификатор
        time.sleep(2) # Время на задержку сети и обработку на стороне сервера
        data = client.recv(4096).decode("utf-8")
        data = list(data)
        decrypt()
        data = "".join(data)
        if data == "info":
            print("Auth true, connect")
        else:
            print ("Auth false, disconnect")
            break
    while True:
        print ("Выберите пункт меню: ")
        print ("1. Включить непрерывный мониторинг. ")
        print ("2. Взаимодействие с базой данных ")
        choice = input("Ваш выбор --> ")
        if choice == "1":
            message = f"{platform.uname().node}_Monitoring"
            message = list(message)
            encrypt()
            message = "".join(message)
            client.send(message.encode("utf-8"))
            while True:
                current_time = datetime.now()
                message = str(current_time) + "_" # Запись текущего времени в событии
                for partition in psutil.disk_partitions():
                    try:
                        partition_usage = psutil.disk_usage(partition.mountpoint)
                    except PermissionError:
                        continue
                    message = message + str(partition_usage.percent) + "_" # Запись процента использования диска
                for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                    message = message + str(percentage) + "_" # Запись наименования ядра и процент его загрузки
                message = message + str(psutil.cpu_percent()) + "_" + str(psutil.swap_memory().percent) + "_" + str(psutil.virtual_memory().percent) # Запись процента использования процессора/оперативной памяти/памяти подкачки
                gpu = GPUtil.getGPUs()[0]
                message = message + "_" + str(gpu.load*100) + "_" + str(gpu.temperature) + "_" + str((gpu.memoryUsed/gpu.memoryTotal) * 100) + "_" # Запись имени видеокарты, ее загрузки, температуры, использование видеопамяти
                message = list(message)
                encrypt()
                message = "".join(message)
                # print(message) #Как выглядят сообщения в канале#
                client.send(message.encode("utf-8"))
                time.sleep(1) # Таймаут мониторинга с последующей очисткой лога
                message = ""
        #elif choice == "2":
        #   message = f"{platform.uname().node}_DB"
        #   message = list(message)
        #   encrypt()
        #   message = "".join(message)
        #   client.send(message.encode("utf-8"))
        #Реализовать взаимодействие с БД, чтобы можно было противодействовать SQL иньекциям#
        else:
            print ("Похоже, вы ошиблись повторите ввод")
    iteration += 1