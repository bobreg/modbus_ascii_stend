import serial
import minimalmodbus
from tkinter import messagebox


adressies = ['81', '80', '82']
commands = ['49', '51', '49']
vkl_vikl_module = [['vkl_vikl_vum1', ['00', '00', '00']],
                   ['vkl_vikl_fs', ['00', '00', '00', '05']],
                   ['vkl_vikl_vum2', ['00', '00', '00']]]

otvet = [['b', "'", "'"], ['b', "'", "'"], ['b', "'", "'"]]
flag_sbros_avarii = False

flag_phase_ok_plus = False
flag_phase_ok_minus = False
flag_phase_kp_plus = False
flag_phase_kp_minus = False

increment_phase_ok = 0
increment_phase_kp = 0

'''Флаги супермега окна'''

flag_start_stop_obmen = True


def find_port():
    global port_open
    port = 0
    ports = dict()
    for number_port in range(10):
        try:
            i = serial.Serial('com{}'.format(number_port), 115200, timeout=1, stopbits=2, bytesize=7)
            ports[number_port] = ('com{}'.format(number_port))
            i.close()
        except serial.serialutil.SerialException:
            pass
    if len(ports) == 0:
        messagebox.showinfo('Ахтунг!', message='Отсутствуют сом-порты')
        exit()
    elif len(ports) > 1:
        print(ports)
        port = int(input('Выберите нужный порт:'))
    elif len(ports) == 1:
        port = str(ports.keys())[11:12]  # port.keys возвращает что-то типа (dict_keys([2])).
        # это надо перевести в строку, затем извлечь слайсом двойку
        # и передать двойку в port
    port_open = serial.Serial('com{}'.format(port), 115200, timeout=0.2, stopbits=2, bytesize=7)


def read_increment_from_fs():
    global increment_phase_kp
    global increment_phase_ok
    global port_open
    try:
        port_open.write((':800310000001B3\r\n').encode('ascii'))
        increment_phase_ok = int(repr(port_open.read(100))[11:13], 16)
        port_open.write((':800310100001B2\r\n').encode('ascii'))
        increment_phase_kp = int(repr(port_open.read(100))[11:13], 16)
    except ValueError:
        pass


def obmen():
    global otvet
    global vkl_vikl_module
    global adressies
    global commands
    global port_open
    global flag_sbros_avarii
    global flag_phase_ok_plus
    global flag_phase_ok_minus
    global flag_phase_kp_plus
    global flag_phase_kp_minus
    global flag_start_stop_obmen
    while True:
        if flag_start_stop_obmen is True:
            for i in range(0, 3):
                LRC = hex(ord(minimalmodbus._calculateLrcString(adressies[i] + '44' + commands[i] +
                                                                ''.join(map(str, vkl_vikl_module[i][1])))))[2:]
                message = ':' + adressies[i] + '44' + commands[i] + \
                          ''.join(map(str, vkl_vikl_module[i][1])) + LRC.upper() + '\r\n'
                print(message)
                port_open.write(message.encode('ascii'))
                otvet[i] = repr(port_open.read(120))
                print(otvet[i])
                #  print(list(bin(int(otvet[i][19:21], 16))), list(bin(int(otvet[i][21:23], 16))))
                #  подсмотреть аварийные байты только для 49 команды
        if flag_sbros_avarii is True:
            sbros_avarii()
            flag_sbros_avarii = False
        elif flag_phase_ok_plus is True:
            change_phase()
            flag_phase_ok_plus = False
        elif flag_phase_ok_minus is True:
            change_phase()
            flag_phase_ok_minus = False
        elif flag_phase_kp_plus is True:
            change_phase()
            flag_phase_kp_plus = False
        elif flag_phase_kp_minus is True:
            change_phase()
            flag_phase_kp_minus = False


def sbros_avarii():
    global port_open
    port_open.write((':80050201FF0084\r\n').encode('ascii'))
    print(repr(port_open.read(100)))
    port_open.write((':81050201FF0083\r\n').encode('ascii'))
    print(repr(port_open.read(100)))
    port_open.write((':82050201FF0082\r\n').encode('ascii'))
    print(repr(port_open.read(100)))
    print('улетела команда')


def change_phase():
    global increment_phase_ok
    global increment_phase_kp
    global flag_phase_ok_plus
    global flag_phase_ok_minus
    global flag_phase_kp_plus
    global flag_phase_kp_minus
    if flag_phase_ok_plus is True:
        increment_phase_ok += 1
        if increment_phase_ok == 64:
            increment_phase_ok = 63
        LRC = hex(ord(minimalmodbus._calculateLrcString('8006100000' + hex(increment_phase_ok)[2:])))[2:]
        port_open.write((':8006100000' + hex(increment_phase_ok)[2:] + LRC + '\r\n').encode('ascii'))
        print(':800610000001' + hex(increment_phase_ok)[2:] + LRC + '\r\n')
        print(repr(port_open.read(100)))
    elif flag_phase_ok_minus is True:
        increment_phase_ok -= 1
        if increment_phase_ok == -1:
            increment_phase_ok = 0
        LRC = hex(ord(minimalmodbus._calculateLrcString('8006100000' + hex(increment_phase_ok)[2:])))[2:]
        port_open.write((':8006100000' + hex(increment_phase_ok)[2:] + LRC + '\r\n').encode('ascii'))
        print(':800610000001' + hex(increment_phase_ok)[2:] + LRC + '\r\n')
        print(repr(port_open.read(100)))
    elif flag_phase_kp_plus is True:
        increment_phase_kp += 1
        if increment_phase_kp == 64:
            increment_phase_kp = 63
        LRC = hex(ord(minimalmodbus._calculateLrcString('8006101000' + hex(increment_phase_kp)[2:])))[2:]
        port_open.write((':8006101000' + hex(increment_phase_kp)[2:] + LRC + '\r\n').encode('ascii'))
        print(':800610000001' + hex(increment_phase_kp)[2:] + LRC + '\r\n')
        print(repr(port_open.read(100)))
    elif flag_phase_kp_minus is True:
        increment_phase_kp -= 1
        if increment_phase_kp == -1:
            increment_phase_kp = 0
        LRC = hex(ord(minimalmodbus._calculateLrcString('8006101000' + hex(increment_phase_kp)[2:])))[2:]
        print(':800610000001' + hex(increment_phase_kp)[2:] + LRC + '\r\n')
        port_open.write((':8006101000' + hex(increment_phase_kp)[2:] + LRC + '\r\n').encode('ascii'))
        print(repr(port_open.read(100)))
    print('поменяли фазу')


def return_dannie_moduls_to_window():
    global otvet
    return otvet


if __name__ == '__main__':
    pass