import socket
import platform
import time
import pyodbc

# Подключение клиента
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((socket.gethostname(),10000))
server.listen()

# Подключение к БД
conn = pyodbc.connect (r"Driver={SQL Server};Server=SERVER_NAME;Database=DATABASE_NAME;Trusted_Connection=yes;")
cursor = conn.cursor()

iteration = 0
num = 0
crit_message = ""

time_1 = [None] * 61
Disk_C = [0.0] * 61
Disk_D = [0.0] * 61
Core1 = [0.0] * 61
Core2 = [0.0] * 61
Core3 = [0.0] * 61
Core4 = [0.0] * 61
Core5 = [0.0] * 61
Core6 = [0.0] * 61
Core7 = [0.0] * 61
Core8 = [0.0] * 61
cpu = [0.0] * 61
ram = [0.0] * 61
vram = [0.0] * 61
gpu_load = [0.0] * 61
gpu_temp = [0.0] * 61
gpu_ram = [0.0] * 61

def decrypt(): # Простая функция дешифрования
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

def encrypt(): # Простая функция шифрования
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

def parser(num): # Парсер строки
    per = 0
    string = ""
    for i in range(len(data)):
        if data[i] != "_" and per == 0:
            if data[i] == " ":
                data[i] = "T"
            string = string + data[i]
        elif data[i] == "_" and per == 0:
            per = 1
            time_1[num] = string[:23]
            string = ""
        elif data[i] != "_" and per == 1:
            string = string + data[i]
        elif data[i] == "_" and per == 1:
            per = 2
            Disk_C[num] = string
            string = ""
        elif data[i] != "_" and per == 2:
            string = string + data[i]
        elif data[i] == "_" and per == 2:
            per = 3
            Disk_D[num] = string
            string = ""
        elif data[i] != "_" and per == 3:
            string = string + data[i]
        elif data[i] == "_" and per == 3:
            per = 4
            Core1[num] = string
            string = ""
        elif data[i] != "_" and per == 4:
            string = string + data[i]
        elif data[i] == "_" and per == 4:
            per = 5
            Core2[num] = string
            string = ""
        elif data[i] != "_" and per == 5:
            string = string + data[i]
        elif data[i] == "_" and per == 5:
            per = 6
            Core3[num] = string
            string = ""
        elif data[i] != "_" and per == 6:
            string = string + data[i]
        elif data[i] == "_" and per == 6:
            per = 7
            Core4[num] = string
            string = ""
        elif data[i] != "_" and per == 7:
            string = string + data[i]
        elif data[i] == "_" and per == 7:
            per = 8
            Core5[num] = string
            string = ""
        elif data[i] != "_" and per == 8:
            string = string + data[i]
        elif data[i] == "_" and per == 8:
            per = 9
            Core6[num] = string
            string = ""
        elif data[i] != "_" and per == 9:
            string = string + data[i]
        elif data[i] == "_" and per == 9:
            per = 10
            Core7[num] = string
            string = ""
        elif data[i] != "_" and per == 10:
            string = string + data[i]
        elif data[i] == "_" and per == 10:
            per = 11
            Core8[num] = string
            string = ""
        elif data[i] != "_" and per == 11:
            string = string + data[i]
        elif data[i] == "_" and per == 11:
            per = 12
            cpu[num] = string
            string = ""
        elif data[i] != "_" and per == 12:
            string = string + data[i]
        elif data[i] == "_" and per == 12:
            per = 13
            ram[num] = string
            string = ""
        elif data[i] != "_" and per == 13:
            string = string + data[i]
        elif data[i] == "_" and per == 13:
            per = 14
            vram[num] = string
            string = ""
        elif data[i] != "_" and per == 14:
            string = string + data[i]
        elif data[i] == "_" and per == 14:
            per = 15
            gpu_load[num] = string
            string = ""
        elif data[i] != "_" and per == 15:
            string = string + data[i]
        elif data[i] == "_" and per == 15:
            per = 16
            gpu_temp[num] = string
            string = ""
        elif data[i] != "_" and per == 16:
            string = string + data[i]
        elif data[i] == "_" and per == 16:
            per = 0
            gpu_ram[num] = string
            string = ""

def print_info(): # Для отладки
    print(time_1,
Disk_C,
Disk_D,
Core1,
Core2,
Core3,
Core4,
Core5,
Core6,
Core7,
Core8,
cpu,
ram,
vram,
gpu_load,
gpu_temp,
gpu_ram)

while True:
    if iteration == 0: # Самая простая идентификация устройств
        user, addr = server.accept()
        data = user.recv(4096).decode("utf-8")
        data = list(data)
        decrypt()
        data = "".join(data)
        if data == "info":
            print("Auth true, connect")
            message = f"{platform.uname().system}_{platform.uname().node}_{platform.uname().version}_{platform.uname().machine}"
            message = list(message)
            encrypt()
            message = "".join(message)
            user.send(message.encode("utf-8")) # Идентификатор
            time.sleep(2) # Время на задержку сети и обработку на стороне сервера
        else:
            print("Auth false, disconnect")
            server.close()
            break
    data = user.recv(4096).decode("utf-8")
    data = list(data)
    decrypt()
    data = "".join(data)
    if data == "info":
        while True:
            data = "null"
            data = user.recv(4096).decode("utf-8")
            data = list(data)
            decrypt()
            if data != "null":
                # data = "".join(data)
                # print(data) # Для отладки Как сообщение выглядит после дешифровки#
                # data = list(data)
                # print(num)
                parser(num)
                if num == 60:
                    # print_info()
                    for a in range (num):
                        Disk_C[a] = float(Disk_C[a])
                        Disk_D[a] = float(Disk_D[a])
                        Core1[a] = float(Core1[a])
                        Core2[a] = float(Core2[a])
                        Core3[a] = float(Core3[a])
                        Core4[a] = float(Core4[a])
                        Core5[a] = float(Core5[a])
                        Core6[a] = float(Core6[a])
                        Core7[a] = float(Core7[a])
                        Core8[a] = float(Core8[a])
                        cpu[a] = float(cpu[a])
                        ram[a] = float(ram[a])
                        vram[a] = float(vram[a])
                        gpu_load[a] = float(gpu_load[a])
                        gpu_temp[a] = float(gpu_temp[a])
                        gpu_ram[a] = float(gpu_ram[a]) 
                        if Disk_C[a] > 75:
                            crit_message = str(crit_message)  + "_Disk C:\\ перегружен до " + str(Disk_C[a]) + "%_"
                        if Disk_D[a] > 75:
                            crit_message = str(crit_message)  + "_Disk D:\\ перегружен до " + str(Disk_C[a]) + "%_"
                        if gpu_temp[a] > 88:
                            crit_message = str(crit_message)  + "_Видеокарта перегрета до " + str(gpu_temp[a]) + "°C_"
                        if ram[a] > 85:
                            crit_message = str(crit_message)  + "_Оперативная память переполнена до " + str(ram[a]) + "%_"
                        if vram[a] > 85:
                            crit_message = str(crit_message)  + "_Память подкачки переполнена до " + str(vram[a]) + "%_"
                        if gpu_ram[a] > 85:
                            crit_message = str(crit_message)  + "_Видеопамять переполнена до " + str(gpu_ram[a]) + "%_"
                        if Core1[a] > 85 and a < 50:
                            if float(Core1[a + 1]) < Core1[a]*0.5 and float(Core1[a + 2]) < Core1[a]*0.5 and float(Core1[a + 3]) < Core1[a]*0.5 and float(Core1[a + 10]) >= Core1[a]:
                                crit_message = str(crit_message)  + "_Возник тротлинг по первому ядру c " + str(Core1[a]) + "% до " + str(Core1[a + 1]) + "%"
                        if Core2[a] > 85 and a < 50:
                            if float(Core2[a + 1]) < Core2[a]*0.5 and float(Core2[a + 2]) < Core2[a]*0.5 and float(Core2[a + 3]) < Core2[a]*0.5 and float(Core2[a + 10]) >= Core2[a]:
                                crit_message = str(crit_message)  + "_Возник тротлинг по второму ядру c " + str(Core2[a]) + "% до " + str(Core2[a + 1]) + "%"
                        if Core3[a] > 85 and a < 50:
                            if float(Core3[a + 1]) < Core3[a]*0.5 and float(Core3[a + 2]) < Core3[a]*0.5 and float(Core3[a + 3]) < Core3[a]*0.5 and float(Core3[a + 10]) >= Core3[a]:
                                crit_message = str(crit_message)  + "_Возник тротлинг по третьему ядру c " + str(Core3[a]) + "% до " + str(Core3[a + 1]) + "%"
                        if Core4[a] > 85 and a < 50:
                            if float(Core4[a + 1]) < Core4[a]*0.5 and float(Core4[a + 2]) < Core4[a]*0.5 and float(Core4[a + 3]) < Core4[a]*0.5 and float(Core4[a + 10]) >= Core4[a]:
                                crit_message = str(crit_message)  + "_Возник тротлинг по четвертому ядру c " + str(Core4[a]) + "% до " + str(Core4[a + 1]) + "%"
                        if Core5[a] > 85 and a < 50:
                            if float(Core5[a + 1]) < Core5[a]*0.5 and float(Core5[a + 2]) < Core5[a]*0.5 and float(Core5[a + 3]) < Core5[a]*0.5 and float(Core5[a + 10]) >= Core5[a]:
                                crit_message = str(crit_message)  + "_Возник тротлинг по пятому ядру c " + str(Core5[a]) + "% до " + str(Core5[a + 1]) + "%"
                        if Core6[a] > 85 and a < 50:
                            if float(Core6[a + 1]) < Core6[a]*0.5 and float(Core6[a + 2]) < Core6[a]*0.5 and float(Core6[a + 3]) < Core6[a]*0.5 and float(Core6[a + 10]) >= Core6[a]:
                                crit_message = str(crit_message)  + "_Возник тротлинг по шестому ядру c " + str(Core6[a]) + "% до " + str(Core6[a + 1]) + "%"
                        if Core7[a] > 85 and a < 50:
                            if float(Core7[a + 1]) < Core7[a]*0.5 and float(Core7[a + 2]) < Core7[a]*0.5 and float(Core7[a + 3]) < Core7[a]*0.5 and float(Core7[a + 10]) >= Core7[a]:
                                crit_message = str(crit_message)  + "_Возник тротлинг по седьмому ядру c " + str(Core7[a]) + "% до " + str(Core7[a + 1]) + "%"
                        if Core8[a] > 85 and a < 50:
                            if float(Core8[a + 1]) < Core8[a]*0.5 and float(Core8[a + 2]) < Core8[a]*0.5 and float(Core8[a + 3]) < Core8[a]*0.5 and float(Core8[a + 10]) >= Core8[a]:
                                crit_message = str(crit_message)  + "_Возник тротлинг по седьмому ядру c " + str(Core8[a]) + "% до " + str(Core8[a + 1]) + "%"
                        if cpu[a] > 85 and a < 50:
                            if float(cpu[a + 1]) < cpu[a]*0.5 and float(cpu[a + 2]) < cpu[a]*0.5 and float(cpu[a + 3]) < cpu[a]*0.5 and float(cpu[a + 10]) >= cpu[a]:
                                crit_message = str(crit_message)  + "_Возник тротлинг процессора c " + str(cpu[a]) + "% до " + str(cpu[a + 1]) + "%"
                        if gpu_load[a] > 85 and a < 50:
                            if float(gpu_load[a + 1]) < gpu_load[a]*0.5 and float(gpu_load[a + 2]) < gpu_load[a]*0.5 and float(gpu_load[a + 3]) < gpu_load[a]*0.5 and float(gpu_load[a + 10]) >= gpu_load[a]:
                                crit_message = str(crit_message)  + "_Возник тротлинг видеокарты c " + str(gpu_load[a]) + "% до " + str(gpu_load[a + 1]) + "%"
                        insert = "INSERT INTO PC_INFO (time_,disk_c,disk_d,core1,core2,core3,core4,core5,core6,core7,core8,cpu_load,ram_load,vram_load,gpu_load,gpu_temp,gpu_ram_load,crit_message) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                        data_type = (time_1[a], Disk_C[a], Disk_D[a], Core1[a], Core2[a], Core3[a], Core4[a], Core5[a], Core6[a], Core7[a], Core8[a], cpu[a], ram[a], vram[a], gpu_load[a], gpu_temp[a], gpu_ram[a], crit_message)
                        cursor.execute(insert, data_type)
                        conn.commit()
                        crit_message = ""
                    time_1 = [None] * 61
                    Disk_C = [0.0] * 61
                    Disk_D = [0.0] * 61
                    Core1 = [0.0] * 61
                    Core2 = [0.0] * 61
                    Core3 = [0.0] * 61
                    Core4 = [0.0] * 61
                    Core5 = [0.0] * 61
                    Core6 = [0.0] * 61
                    Core7 = [0.0] * 61
                    Core8 = [0.0] * 61
                    cpu = [0.0] * 61
                    ram = [0.0] * 61
                    vram = [0.0] * 61
                    gpu_load = [0.0] * 61
                    gpu_temp = [0.0] * 61
                    gpu_ram = [0.0] * 61
                    num = -1
                    crit_message = ""
                num += 1
                data = "null"
    elif data == "info":
        while True:
            #!!!Тут ветвление на команды от ПК#
            data = user.recv(4096).decode("utf-8")
            data = list(data)
            decrypt()
            data = "".join(data)
            #!!!SQL инъекции, противостоять им#
    iteration += 1
