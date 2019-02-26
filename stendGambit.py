import tkinter
from threading import Thread
import helpwindow
import opros
import time
import windowmegaclass

flag_vum1 = False
flag_fs = False
flag_vum2 = False

opros.find_port()  # поиск сом-порта
opros.read_increment_from_fs()  # считывание приращений фазы из ФСа


def update_window():
    global otvet
    while True:
        otvet = opros.return_dannie_moduls_to_window()
        if len(list(otvet[0])) < 10:
            VUM1_rabota['text'] = 'обмена нет'
            VUM1_rabota['fg'] = 'red'
        else:
            VUM1_serN['text'] = int(otvet[0][49:55], 16)  # Серийный номер   (температура обрабатывается в авариях)
            VUM1_serN['fg'] = 'black'
            VUM1_time['text'] = int(otvet[0][55:59], 16)  # Часы наработки
            VUM1_time['fg'] = 'black'
            VUM1_verN['text'] = int(otvet[0][61:63], 16)  # Версия прошивки
            VUM1_verN['fg'] = 'black'
            VUM1_Pvh_OK_label['text'] = int(otvet[0][9:11], 16)  # Уровень входной мощности
            VUM1_Pvh_OK_label['fg'] = 'black'
            VUM1_Pvih_OK_label['text'] = int(otvet[0][11:13], 16)  # Уровень выходной мощности
            VUM1_Pvih_OK_label['fg'] = 'black'
            VUM1_Potr_OK_label['text'] = int(otvet[0][13:15], 16)  # Уровень отражённой мощности
            VUM1_Potr_OK_label['fg'] = 'black'
            VUM1_Pvh_KP_label['text'] = int(otvet[0][31:33], 16)  # Уровень входной мощности
            VUM1_Pvh_KP_label['fg'] = 'black'
            VUM1_Pvih_KP_label['text'] = int(otvet[0][33:35], 16)  # Уровень выходной мощности
            VUM1_Pvih_KP_label['fg'] = 'black'
            VUM1_Potr_KP_label['text'] = int(otvet[0][35:37], 16)  # Уровень отражённой мощности
            VUM1_Potr_KP_label['fg'] = 'black'
            avarii_vim1()
        if len(list(otvet[1])) < 10:
            fs_rabota['text'] = 'обмена нет'
            fs_rabota['fg'] = 'red'
        else:
            fs_serN['text'] = int(otvet[1][15:23], 16)  # Серийный номер
            fs_serN['fg'] = 'black'
            fs_time['text'] = int(otvet[1][23:27], 16)  # Часы наработки
            fs_time['fg'] = 'black'
            fs_verN['text'] = int(otvet[1][29:31], 16)  # Версия прошивки
            fs_verN['fg'] = 'black'
            fs_Pvih_OK1_label['text'] = int(otvet[1][33:35], 16)  # Уровень выходной мощности
            fs_Pvih_OK1_label['fg'] = 'black'
            fs_Potr_OK1_label['text'] = int(otvet[1][36:38], 16)  # Уровень отражённой мощности
            fs_Potr_OK1_label['fg'] = 'black'
            fs_Pvih_KP1_label['text'] = int(otvet[1][51:53], 16)  # Уровень выходной мощности
            fs_Pvih_KP1_label['fg'] = 'black'
            fs_Potr_KP1_label['text'] = int(otvet[1][53:55], 16)  # Уровень отражённой мощности
            fs_Potr_KP1_label['fg'] = 'black'
            fs_Pvih_OK2_label['text'] = int(otvet[1][69:71], 16)  # Уровень выходной мощности
            fs_Pvih_OK2_label['fg'] = 'black'
            fs_Potr_OK2_label['text'] = int(otvet[1][71:73], 16)  # Уровень отражённой мощности
            fs_Potr_OK2_label['fg'] = 'black'
            fs_Pvih_KP2_label['text'] = int(otvet[1][87:89], 16)  # Уровень выходной мощности
            fs_Pvih_KP2_label['fg'] = 'black'
            fs_Potr_KP2_label['text'] = int(otvet[1][89:91], 16)  # Уровень отражённой мощности
            fs_Potr_KP2_label['fg'] = 'black'
            fs_faza_OK_label['text'] = int(otvet[1][41:43], 16)  # Текущая фаза канала ОК
            fs_faza_OK_label['fg'] = 'black'
            fs_faza_KP_label['text'] = int(otvet[1][59:61], 16)  # Текущая фаза канала КП
            fs_faza_KP_label['fg'] = 'black'
            avarii_fs()
        if len(list(otvet[2])) < 10:
            VUM2_rabota['text'] = 'обмена нет'
            VUM2_rabota['fg'] = 'red'
        else:
            VUM2_serN['text'] = int(otvet[2][49:55], 16)  # Серийный номер   (температура обрабатывается в авариях)
            VUM2_serN['fg'] = 'black'
            VUM2_time['text'] = int(otvet[2][55:59], 16)  # Часы наработки
            VUM2_time['fg'] = 'black'
            VUM2_verN['text'] = int(otvet[2][61:63], 16)  # Версия прошивки
            VUM2_verN['fg'] = 'black'
            VUM2_Pvh_OK_label['text'] = int(otvet[2][9:11], 16)  # Уровень входной мощности
            VUM2_Pvh_OK_label['fg'] = 'black'
            VUM2_Pvih_OK_label['text'] = int(otvet[2][11:13], 16)  # Уровень выходной мощности
            VUM2_Pvih_OK_label['fg'] = 'black'
            VUM2_Potr_OK_label['text'] = int(otvet[2][13:15], 16)  # Уровень отражённой мощности
            VUM2_Potr_OK_label['fg'] = 'black'
            VUM2_Pvh_KP_label['text'] = int(otvet[2][31:33], 16)  # Уровень входной мощности
            VUM2_Pvh_KP_label['fg'] = 'black'
            VUM2_Pvih_KP_label['text'] = int(otvet[2][33:35], 16)  # Уровень выходной мощности
            VUM2_Pvih_KP_label['fg'] = 'black'
            VUM2_Potr_KP_label['text'] = int(otvet[2][35:37], 16)  # Уровень отражённой мощности
            VUM2_Potr_KP_label['fg'] = 'black'
            avarii_vim2()
        time.sleep(0.1)


def sbros_avarii():
    opros.flag_sbros_avarii = True


def avarii_vim1():
    ks1b1 = ['0', '0', '0', '0', '0', '0', '0', '0']
    ks1b2 = ['0', '0', '0', '0', '0', '0', '0', '0']
    ks2b1 = ['0', '0', '0', '0', '0', '0', '0', '0']
    ks2b2 = ['0', '0', '0', '0', '0', '0', '0', '0']
    for i in range(-1, -len(list(bin(int(otvet[0][19:21], 16)))[2:]) - 1, -1):
        ks1b1[i] = list(bin(int(otvet[0][19:21], 16)))[i]
    for i in range(-1, -len(list(bin(int(otvet[0][21:23], 16)))[2:]) - 1, -1):
        ks1b2[i] = list(bin(int(otvet[0][21:23], 16)))[i]
    for i in range(-1, -len(list(bin(int(otvet[0][37:39], 16)))[2:]) - 1, -1):
        ks2b1[i] = list(bin(int(otvet[0][37:39], 16)))[i]
    for i in range(-1, -len(list(bin(int(otvet[0][39:41], 16)))[2:]) - 1, -1):
        ks2b2[i] = list(bin(int(otvet[0][39:41], 16)))[i]
    '''обработка КС1 байт первый'''
    if ks1b1[-1] == '1' or ks2b1[-1] == '1':
        VUM1_rabota['text'] = 'Авария'
        VUM1_mod_avaria['text'] = 'Перегрузка по T/Q'
        VUM1_mod_avaria['font'] = 'arial 10'
        VUM1_mod_avaria['fg'] = 'red'
        VUM1_rabota['fg'] = 'red'
    if ks1b1[-2] == '1' or ks2b1[-2] == '1':
        VUM1_rabota['text'] = 'Авария'
        VUM1_mod_avaria['text'] = 'Нет ИМ'
        VUM1_mod_avaria['font'] = 'arial 15'
        VUM1_mod_avaria['fg'] = 'red'
        VUM1_rabota['fg'] = 'red'
    if ks1b1[-3] == '1' or ks2b1[-3] == '1':
        VUM1_rabota['text'] = 'Авария'
        VUM1_pitan_avaria['text'] = 'Авария питания'
        VUM1_pitan_avaria['font'] = 'arial 10'
        VUM1_pitan_avaria['fg'] = 'red'
        VUM1_rabota['fg'] = 'red'
    if ks1b1[-4] == '1' or ks2b1[-4] == '1':
        VUM1_temp['text'] = 'Неисправен\nдатчик'
        VUM1_temp['fg'] = 'red'
        VUM1_temp['font'] = 'arial 10'
    else:
        VUM1_temp['text'] = int(otvet[0][15:17], 16)
        VUM1_temp['fg'] = 'black'
        VUM1_temp['font'] = 'arial 15'
    if ks1b1[-1] == '0' and ks1b1[-2] == '0' and ks1b1[-3] == '0' and ks2b1[-1] == '0' and ks2b1[-2] == '0' and \
            ks2b1[-3] == '0':
        VUM1_pitan_avaria['text'] = 'норма'
        VUM1_pitan_avaria['fg'] = 'green'
        VUM1_pitan_avaria['font'] = 'arial 15'
        VUM1_mod_avaria['text'] = 'норма'
        VUM1_mod_avaria['fg'] = 'green'
        VUM1_mod_avaria['font'] = 'arial 15'
    '''обработка КС1 байт второй'''
    if (ks1b2[-4] == '1' or ks2b2[-4] == '1') and (ks1b1[-1] == '0' and ks1b1[-2] == '0' and ks1b1[-3] == '0' and
                                                   ks2b1[-1] == '0' and ks2b1[-2] == '0' and ks2b1[-3] == '0'):
        VUM1_rabota['text'] = 'Pвх меньше нормы'
        VUM1_rabota['fg'] = 'dark orange'
        VUM1_rabota['font'] = 'arial 10'
    if (ks1b2[-5] == '1' or ks2b2[-5] == '1') and (ks1b1[-1] == '0' and ks1b1[-2] == '0' and ks1b1[-3] == '0' and
                                                   ks2b1[-1] == '0' and ks2b1[-2] == '0' and ks2b1[-3] == '0'):
        VUM1_rabota['text'] = 'Pвх больше нормы'
        VUM1_rabota['fg'] = 'dark orange'
        VUM1_rabota['font'] = 'arial 10'
    if ks1b2[-6] == '1' or ks2b2[-6] == '1' and (ks1b1[-1] == '0' and ks1b1[-2] == '0' and ks1b1[-3] == '0' and
                                                 ks2b1[-1] == '0' and ks2b1[-2] == '0' and ks2b1[-3] == '0'):
        VUM1_rabota['text'] = 'Pвых меньше нормы'
        VUM1_rabota['fg'] = 'red'
        VUM1_rabota['font'] = 'arial 10'
    if ks1b2[-7] == '1' or ks2b2[-7] == '1':
        VUM1_rabota['text'] = 'Pотр больше нормы'
        VUM1_rabota['fg'] = 'red'
        VUM1_rabota['font'] = 'arial 10'
    if ks1b2[-8] == '1' or ks2b2[-8] == '1':
        VUM1_rabota['text'] = 'Перегрев'
        VUM1_rabota['fg'] = 'dark orange'
    if ks1b1[-1] == '0' and ks1b1[-2] == '0' and ks1b1[-3] == '0' and ks1b2[-4] == '0' and ks1b2[-5] == '0' and \
            ks1b2[-6] == '0' and ks1b2[-7] == '0' and ks1b2[-8] == '0' and \
            ks2b1[-1] == '0' and ks2b1[-2] == '0' and ks2b1[-3] == '0' and ks2b2[-4] == '0' and ks2b2[-5] == '0' and\
            ks2b2[-6] == '0' and ks2b2[-7] == '0' and ks2b2[-8] == '0':
        VUM1_rabota['text'] = 'норма'
        VUM1_rabota['fg'] = 'green'
        VUM1_rabota['font'] = 'arial 15'


def avarii_fs():
    ks1b1 = ['0', '0', '0', '0', '0', '0', '0', '0']
    ks1b2 = ['0', '0', '0', '0', '0', '0', '0', '0']
    ks2b1 = ['0', '0', '0', '0', '0', '0', '0', '0']
    ks2b2 = ['0', '0', '0', '0', '0', '0', '0', '0']
    ks3b1 = ['0', '0', '0', '0', '0', '0', '0', '0']
    ks3b2 = ['0', '0', '0', '0', '0', '0', '0', '0']
    ks4b1 = ['0', '0', '0', '0', '0', '0', '0', '0']
    ks4b2 = ['0', '0', '0', '0', '0', '0', '0', '0']
    for i in range(-1, -len(list(bin(int(otvet[1][37:39], 16)))[2:]) - 1, -1):
        ks1b1[i] = list(bin(int(otvet[1][37:39], 16)))[i]
    for i in range(-1, -len(list(bin(int(otvet[1][39:41], 16)))[2:]) - 1, -1):
        ks1b2[i] = list(bin(int(otvet[1][39:41], 16)))[i]
    for i in range(-1, -len(list(bin(int(otvet[1][55:57], 16)))[2:]) - 1, -1):
        ks2b1[i] = list(bin(int(otvet[1][55:57], 16)))[i]
    for i in range(-1, -len(list(bin(int(otvet[1][57:59], 16)))[2:]) - 1, -1):
        ks2b2[i] = list(bin(int(otvet[1][57:59], 16)))[i]
    for i in range(-1, -len(list(bin(int(otvet[1][73:75], 16)))[2:]) - 1, -1):
        ks3b1[i] = list(bin(int(otvet[1][73:75], 16)))[i]
    for i in range(-1, -len(list(bin(int(otvet[1][75:77], 16)))[2:]) - 1, -1):
        ks3b2[i] = list(bin(int(otvet[1][75:77], 16)))[i]
    for i in range(-1, -len(list(bin(int(otvet[1][91:93], 16)))[2:]) - 1, -1):
        ks4b1[i] = list(bin(int(otvet[1][91:93], 16)))[i]
    for i in range(-1, -len(list(bin(int(otvet[1][93:95], 16)))[2:]) - 1, -1):
        ks4b2[i] = list(bin(int(otvet[1][93:95], 16)))[i]
    '''обработка КС1 байт первый'''
    if ks1b1[-1] == '1' or ks2b1[-1] == '1' or ks3b1[-1] == '1' or ks4b1[-1] == '1':
        fs_rabota['text'] = 'Авария'
        fs_mod_avaria['text'] = 'Перегрузка по T/Q'
        fs_mod_avaria['font'] = 'arial 10'
        fs_mod_avaria['fg'] = 'red'
        fs_rabota['fg'] = 'red'
    if ks1b1[-2] == '1' or ks2b1[-2] == '1' or ks3b1[-2] == '1' or ks4b1[-2] == '1':
        fs_rabota['text'] = 'Авария'
        fs_mod_avaria['font'] = 'arial 15'
        fs_mod_avaria['text'] = 'Нет ИМ'
        fs_mod_avaria['fg'] = 'red'
        fs_rabota['fg'] = 'red'
    if ks1b1[-3] == '1':
        fs_rabota['text'] = 'Авария'
        fs_pitan_avaria['text'] = 'Авария питания'
        fs_pitan_avaria['font'] = 'arial 10'
        fs_pitan_avaria['fg'] = 'red'
        fs_rabota['fg'] = 'red'
    if ks1b1[-4] == '1':
        fs_temp['text'] = 'Неисправен\nдатчик'
        fs_temp['fg'] = 'red'
        fs_temp['font'] = 'arial 10'
    else:
        fs_temp['text'] = int(otvet[1][11:13], 16)
        fs_temp['fg'] = 'black'
        fs_temp['font'] = 'arial 15'
    if ks1b1[-1] == '0' and ks1b1[-2] == '0' and ks1b1[-3] == '0' and \
            ks2b1[-1] == '0' and ks2b1[-2] == '0' and \
            ks3b1[-1] == '0' and ks4b1[-2] == '0' and \
            ks4b1[-1] == '0' and ks4b1[-2] == '0':
        fs_pitan_avaria['text'] = 'норма'
        fs_pitan_avaria['fg'] = 'green'
        fs_pitan_avaria['font'] = 'arial 15'
        fs_mod_avaria['text'] = 'норма'
        fs_mod_avaria['fg'] = 'green'
        fs_mod_avaria['font'] = 'arial 15'
    '''обработка КС1 байт второй'''
    if (ks1b2[-6] == '1' or ks2b2[-6] == '1' or ks3b2[-6] == '1' or ks4b2[-6] == '1') and \
            (ks1b1[-1] == '0' and ks1b1[-2] == '0' and ks1b1[-3] == '0' and
             ks2b1[-1] == '0' and ks2b1[-2] == '0' and
             ks3b1[-1] == '0' and ks3b1[-2] == '0' and
             ks4b1[-1] == '0' and ks4b1[-2] == '0'):
        fs_rabota['text'] = 'Pвых меньше нормы'
        fs_rabota['fg'] = 'red'
        fs_rabota['font'] = 'arial 10'
    if ks1b2[-7] == '1' or ks2b2[-7] == '1' or ks3b2[-7] == '1' or ks4b2[-7] == '1':
        fs_rabota['text'] = 'Pотр больше нормы'
        fs_rabota['fg'] = 'red'
        fs_rabota['font'] = 'arial 10'
    if ks1b2[-8] == '1':
        fs_rabota['text'] = 'Перегрев'
        fs_rabota['fg'] = 'dark orange'
    if ks1b1[-1] == '0' and ks1b1[-2] == '0' and ks1b1[-3] == '0' and ks1b2[-4] == '0' and ks1b2[-5] == '0' and \
            ks1b2[-6] == '0' and ks1b2[-7] == '0' and ks1b2[-8] == '0' and \
            ks2b1[-1] == '0' and ks2b1[-2] == '0' and ks2b2[-4] == '0' and ks2b2[-5] == '0' and ks2b2[-6] == '0' and ks2b2[-7] == '0' and \
            ks3b1[-1] == '0' and ks3b1[-2] == '0' and ks3b2[-4] == '0' and ks3b2[-5] == '0' and ks3b2[-6] == '0' and ks3b2[-7] == '0' and \
            ks4b1[-1] == '0' and ks4b1[-2] == '0' and ks4b2[-4] == '0' and ks4b2[-5] == '0' and ks4b2[-6] == '0' and ks4b2[-7] == '0':
        fs_rabota['text'] = 'норма'
        fs_rabota['fg'] = 'green'
        fs_rabota['font'] = 'arial 15'


def avarii_vim2():
    ks1b1 = ['0', '0', '0', '0', '0', '0', '0', '0']
    ks1b2 = ['0', '0', '0', '0', '0', '0', '0', '0']
    ks2b1 = ['0', '0', '0', '0', '0', '0', '0', '0']
    ks2b2 = ['0', '0', '0', '0', '0', '0', '0', '0']
    for i in range(-1, -len(list(bin(int(otvet[2][19:21], 16)))[2:]) - 1, -1):
        ks1b1[i] = list(bin(int(otvet[2][19:21], 16)))[i]
    for i in range(-1, -len(list(bin(int(otvet[2][21:23], 16)))[2:]) - 1, -1):
        ks1b2[i] = list(bin(int(otvet[2][21:23], 16)))[i]
    for i in range(-1, -len(list(bin(int(otvet[2][37:39], 16)))[2:]) - 1, -1):
        ks2b1[i] = list(bin(int(otvet[2][37:39], 16)))[i]
    for i in range(-1, -len(list(bin(int(otvet[2][39:41], 16)))[2:]) - 1, -1):
        ks2b2[i] = list(bin(int(otvet[2][39:41], 16)))[i]
    '''обработка КС1 байт первый'''
    if ks1b1[-1] == '1' or ks2b1[-1] == '1':
        VUM2_rabota['text'] = 'Авария'
        VUM2_mod_avaria['text'] = 'Перегрузка по T/Q'
        VUM2_mod_avaria['font'] = 'arial 10'
        VUM2_mod_avaria['fg'] = 'red'
        VUM2_rabota['fg'] = 'red'
    if ks1b1[-2] == '1' or ks2b1[-2] == '1':
        fs_rabota['text'] = 'Авария'
        VUM2_mod_avaria['font'] = 'arial 15'
        VUM2_mod_avaria['text'] = 'Нет ИМ'
        VUM2_mod_avaria['fg'] = 'red'
        VUM2_rabota['fg'] = 'red'
    if ks1b1[-3] == '1' or ks2b1[-3] == '1':
        VUM2_rabota['text'] = 'Авария'
        VUM2_pitan_avaria['text'] = 'Авария питания'
        VUM2_pitan_avaria['font'] = 'arial 10'
        VUM2_pitan_avaria['fg'] = 'red'
        VUM2_rabota['fg'] = 'red'
    if ks1b1[-4] == '1' or ks2b1[-4] == '1':
        VUM2_temp['text'] = 'Неисправен\nдатчик'
        VUM2_temp['fg'] = 'red'
        VUM2_temp['font'] = 'arial 10'
    else:
        VUM2_temp['text'] = int(otvet[2][15:17], 16)
        VUM2_temp['fg'] = 'black'
        VUM2_temp['font'] = 'arial 15'
    if ks1b1[-1] == '0' and ks1b1[-2] == '0' and ks1b1[-3] == '0' and ks2b1[-1] == '0' and ks2b1[-2] == '0' and \
            ks2b1[-3] == '0':
        VUM2_pitan_avaria['text'] = 'норма'
        VUM2_pitan_avaria['fg'] = 'green'
        VUM2_pitan_avaria['font'] = 'arial 15'
        VUM2_mod_avaria['text'] = 'норма'
        VUM2_mod_avaria['fg'] = 'green'
        VUM2_mod_avaria['font'] = 'arial 15'
    '''обработка КС1 байт второй'''
    if (ks1b2[-4] == '1' or ks2b2[-4] == '1') and (ks1b1[-1] == '0' and ks1b1[-2] == '0' and ks1b1[-3] == '0' and
                                                   ks2b1[-1] == '0' and ks2b1[-2] == '0' and ks2b1[-3] == '0'):
        VUM2_rabota['text'] = 'Pвх меньше нормы'
        VUM2_rabota['fg'] = 'dark orange'
        VUM2_rabota['font'] = 'arial 10'
    if (ks1b2[-5] == '1' or ks2b2[-5] == '1') and (ks1b1[-1] == '0' and ks1b1[-2] == '0' and ks1b1[-3] == '0' and
                                                   ks2b1[-1] == '0' and ks2b1[-2] == '0' and ks2b1[-3] == '0'):
        VUM2_rabota['text'] = 'Pвх больше нормы'
        VUM2_rabota['fg'] = 'dark orange'
        VUM2_rabota['font'] = 'arial 10'
    if (ks1b2[-6] == '1' or ks2b2[-6] == '1') and (ks1b1[-1] == '0' and ks1b1[-2] == '0' and ks1b1[-3] == '0' and
                                                   ks2b1[-1] == '0' and ks2b1[-2] == '0' and ks2b1[-3] == '0'):
        VUM2_rabota['text'] = 'Pвых меньше нормы'
        VUM2_rabota['fg'] = 'red'
        VUM2_rabota['font'] = 'arial 10'
    if ks1b2[-7] == '1' or ks2b2[-7] == '1':
        VUM2_rabota['text'] = 'Pотр больше нормы'
        VUM2_rabota['fg'] = 'red'
        VUM2_rabota['font'] = 'arial 10'
    if ks1b2[-8] == '1' or ks2b2[-8] == '1':
        VUM2_rabota['text'] = 'Перегрев'
        VUM2_rabota['fg'] = 'dark orange'
    if ks1b1[-1] == '0' and ks1b1[-2] == '0' and ks1b1[-3] == '0' and ks1b2[-4] == '0' and ks1b2[-5] == '0' and \
            ks1b2[-6] == '0' and ks1b2[-7] == '0' and ks1b2[-8] == '0' and \
            ks2b1[-1] == '0' and ks2b1[-2] == '0' and ks2b1[-3] == '0' and ks2b2[-4] == '0' and ks2b2[-5] == '0' \
            and ks2b2[-6] == '0' and ks2b2[-7] == '0' and ks2b2[-8] == '0':
        VUM2_rabota['text'] = 'норма'
        VUM2_rabota['fg'] = 'green'
        VUM2_rabota['font'] = 'arial 15'


def vkl_vum1():
    global flag_vum1
    flag_vum1 = not flag_vum1
    if flag_vum1 is True:
        opros.vkl_vikl_module[0][1] = ['01', '01', '01']
        VUM1_vkl_button['bg'] = 'green yellow'
        VUM1_vkl_button['text'] = 'Выключить'
    else:
        opros.vkl_vikl_module[0][1] = ['00', '00', '00']
        VUM1_vkl_button['bg'] = 'snow3'
        VUM1_vkl_button['text'] = 'Включить'


def vkl_fs():
    global flag_fs
    flag_fs = not flag_fs
    if flag_fs is True:
        opros.vkl_vikl_module[1][1] = ['01', '01', '01', '05']
        fs_vkl_button['bg'] = 'green yellow'
        fs_vkl_button['text'] = 'Выключить'
    else:
        opros.vkl_vikl_module[1][1] = ['00', '00', '00', '05']
        fs_vkl_button['bg'] = 'snow3'
        fs_vkl_button['text'] = 'Включить'


def vkl_vum2():
    global flag_vum2
    flag_vum2 = not flag_vum2
    if flag_vum2 is True:
        opros.vkl_vikl_module[2][1] = ['01', '01', '01']
        VUM2_vkl_button['bg'] = 'green yellow'
        VUM2_vkl_button['text'] = 'Выключить'
    else:
        opros.vkl_vikl_module[2][1] = ['00', '00', '00']
        VUM2_vkl_button['bg'] = 'snow3'
        VUM2_vkl_button['text'] = 'Включить'


def change_faza_ok_plus():
    opros.flag_phase_ok_plus = True


def change_faza_ok_minus():
    opros.flag_phase_ok_minus = True


def change_faza_kp_plus():
    opros.flag_phase_kp_plus = True


def change_faza_kp_minus():
    opros.flag_phase_kp_minus = True


thread_obmen = Thread(target=opros.obmen, daemon=True)
thread_update_window = Thread(target=update_window, daemon=True)


'''Создание окна'''
window = tkinter.Tk()
window.title("Gambit. ver 1.0. Alex_Chel_Man Inc. from 34 sektor OKB")
window.geometry("1024x600")

c1 = tkinter.Canvas(window, width=1, height=500, bg='black')  # Граничные линии
c2 = tkinter.Canvas(window, width=1, height=500, bg='black')
c3 = tkinter.Canvas(window, width=1, height=180, bg='black')  # |вум1
c4 = tkinter.Canvas(window, width=1, height=180, bg='black')
c5 = tkinter.Canvas(window, width=1, height=135, bg='black')  # |фс
c6 = tkinter.Canvas(window, width=1, height=135, bg='black')
c7 = tkinter.Canvas(window, width=1, height=135, bg='black')
c8 = tkinter.Canvas(window, width=1, height=135, bg='black')
c9 = tkinter.Canvas(window, width=1, height=180, bg='black')  # |вум2
c10 = tkinter.Canvas(window, width=1, height=180, bg='black')
c11 = tkinter.Canvas(window, width=200, height=1, bg='black')  # -вум1
c12 = tkinter.Canvas(window, width=200, height=1, bg='black')
c13 = tkinter.Canvas(window, width=200, height=1, bg='black')
c14 = tkinter.Canvas(window, width=340, height=1, bg='black')  # -фс
c15 = tkinter.Canvas(window, width=340, height=1, bg='black')
c16 = tkinter.Canvas(window, width=200, height=1, bg='black')  # -вум2
c17 = tkinter.Canvas(window, width=200, height=1, bg='black')
c18 = tkinter.Canvas(window, width=200, height=1, bg='black')

help_button = tkinter.Button(window, text='Техподдержка', width=10, heigh=1, command=helpwindow.help_button,
                             font='arial 11')
sbros_avaria_button = tkinter.Button(window, text='Сброс аварии', width=10, heigh=1, command=sbros_avarii,
                                     font='arial 11')
VUM1_vkl_button = tkinter.Button(window, text='Включить', width=10, heigh=1, command=vkl_vum1, font='arial 11')
fs_vkl_button = tkinter.Button(window, text='Включить', width=10, heigh=1, command=vkl_fs, font='arial 11')
VUM2_vkl_button = tkinter.Button(window, text='Включить', width=10, heigh=1, command=vkl_vum2, font='arial 11')

VUM1_label = tkinter.Label(window, text='ВУМ 1', font='arial 20')
fs_label = tkinter.Label(window, text='ФС', font='arial 20')
VUM2_label = tkinter.Label(window, text='ВУМ 2', font='arial 20')

VUM1_label_temp = tkinter.Label(window, text='Температура, град:', font='arial 15')
fs_label_temp = tkinter.Label(window, text='Температура, град:', font='arial 15')
VUM2_label_temp = tkinter.Label(window, text='Температура, град:', font='arial 15')
VUM1_temp = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
fs_temp = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM2_temp = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')

VUM1_label_serN = tkinter.Label(window, text='Серийный номер:', font='arial 15')
fs_label_serN = tkinter.Label(window, text='Серийный номер:', font='arial 15')
VUM2_label_serN = tkinter.Label(window, text='Серийный номер:', font='arial 15')
VUM1_serN = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
fs_serN = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM2_serN = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')

VUM1_label_time = tkinter.Label(window, text='Время наработки:', font='arial 15')
fs_label_time = tkinter.Label(window, text='Время наработки:', font='arial 15')
VUM2_label_time = tkinter.Label(window, text='Время наработки:', font='arial 15')
VUM1_time = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
fs_time = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM2_time = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')

VUM1_label_verN = tkinter.Label(window, text='Версия прошивки:', font='arial 15')
fs_label_verN = tkinter.Label(window, text='Версия прошивки:', font='arial 15')
VUM2_label_verN = tkinter.Label(window, text='Версия прошивки:', font='arial 15')
VUM1_verN = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
fs_verN = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM2_verN = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')

VUM1_label_OK = tkinter.Label(window, text='ОК', font='arial 15')
VUM1_label_KP = tkinter.Label(window, text='КП', font='arial 15')
fs_label_OK1 = tkinter.Label(window, text='ОК1', font='arial 15')
fs_label_OK2 = tkinter.Label(window, text='ОК2', font='arial 15')
fs_label_KP1 = tkinter.Label(window, text='КП1', font='arial 15')
fs_label_KP2 = tkinter.Label(window, text='КП2', font='arial 15')
VUM2_label_OK = tkinter.Label(window, text='ОК', font='arial 15')
VUM2_label_KP = tkinter.Label(window, text='КП', font='arial 15')

VUM1_label_Pvh = tkinter.Label(window, text='Pвх', font='arial 15')
VUM1_label_Pvih = tkinter.Label(window, text='Рвых', font='arial 15')
VUM1_label_Potr = tkinter.Label(window, text='Ротр', font='arial 15')
fs_label_Pvih = tkinter.Label(window, text='Рвых', font='arial 15')
fs_label_Potr = tkinter.Label(window, text='Ротр', font='arial 15')
VUM2_label_Pvh = tkinter.Label(window, text='Рвх', font='arial 15')
VUM2_label_Pvih = tkinter.Label(window, text='Рвых', font='arial 15')
VUM2_label_Potr = tkinter.Label(window, text='Ротр', font='arial 15')

VUM1_Pvh_OK_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM1_Pvih_OK_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM1_Potr_OK_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM1_Pvh_KP_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM1_Pvih_KP_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM1_Potr_KP_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')

fs_Pvih_OK1_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
fs_Potr_OK1_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
fs_Pvih_OK2_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
fs_Potr_OK2_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
fs_Pvih_KP1_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
fs_Potr_KP1_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
fs_Pvih_KP2_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
fs_Potr_KP2_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')

VUM2_Pvh_OK_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM2_Pvih_OK_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM2_Potr_OK_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM2_Pvh_KP_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM2_Pvih_KP_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
VUM2_Potr_KP_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')

fazirovka_label = tkinter.Label(window, text='Фазировка', font='arial 15')
fazirovka_OK_label = tkinter.Label(window, text='ОК', font='arial 15')
fs_faza_plus_OK_button = tkinter.Button(window, text='+', width=2, heigh=1, command=change_faza_ok_plus)
fs_faza_minus_OK_button = tkinter.Button(window, text='-', width=2, heigh=1, command=change_faza_ok_minus)
fs_faza_OK_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')
fazirovka_KP_label = tkinter.Label(window, text='КП', font='arial 15')
fs_faza_plus_KP_button = tkinter.Button(window, text='+', width=2, heigh=1, command=change_faza_kp_plus)
fs_faza_minus_KP_button = tkinter.Button(window, text='-', width=2, heigh=1, command=change_faza_kp_minus)
fs_faza_KP_label = tkinter.Label(window, text='FF', font='arial 15', fg='dark orange')

VUM1_label_rabota = tkinter.Label(window, text='Работа:', font='arial 15')
VUM1_label_pitan_avaria = tkinter.Label(window, text='Питание:', font='arial 15')
VUM1_label_mod_avaria = tkinter.Label(window, text='Модуляция:', font='arial 15')
VUM1_rabota = tkinter.Label(window, text='НД', font='arial 15', fg='dark orange')
VUM1_pitan_avaria = tkinter.Label(window, text='НД', font='arial 15', fg='dark orange')
VUM1_mod_avaria = tkinter.Label(window, text='НД', font='arial 15', fg='dark orange')

fs_label_rabota = tkinter.Label(window, text='Работа:', font='arial 13')
fs_label_pitan_avaria = tkinter.Label(window, text='Питание:', font='arial 13')
fs_label_mod_avaria = tkinter.Label(window, text='Модуляция:', font='arial 13')
fs_rabota = tkinter.Label(window, text='НД', font='arial 13', fg='dark orange')
fs_pitan_avaria = tkinter.Label(window, text='НД', font='arial 13', fg='dark orange')
fs_mod_avaria = tkinter.Label(window, text='НД', font='arial 13', fg='dark orange')

VUM2_label_rabota = tkinter.Label(window, text='Работа:', font='arial 15')
VUM2_label_pitan_avaria = tkinter.Label(window, text='Питание:', font='arial 15')
VUM2_label_mod_avaria = tkinter.Label(window, text='Модуляция:', font='arial 15')
VUM2_rabota = tkinter.Label(window, text='НД', font='arial 15', fg='dark orange')
VUM2_pitan_avaria = tkinter.Label(window, text='НД', font='arial 15', fg='dark orange')
VUM2_mod_avaria = tkinter.Label(window, text='НД', font='arial 15', fg='dark orange')

super_mega_okno = tkinter.Button(window, text='Суперспецрежим', width=13, heigh=2, command=windowmegaclass.megawindow)


'''Упаковка элементов окна'''
c1.place(x=300, y=0)  # разделение модулей
c2.place(x=720, y=0)
c3.place(x=90, y=190)  # |вум1
c4.place(x=170, y=190)
c5.place(x=380, y=190)  # |фс
c6.place(x=460, y=190)
c7.place(x=540, y=190)
c8.place(x=620, y=190)
c9.place(x=820, y=190)  # |вум2
c10.place(x=900, y=190)
c11.place(x=50, y=220)  # -вум1
c12.place(x=50, y=270)
c13.place(x=50, y=320)
c14.place(x=350, y=220)  # -фс
c15.place(x=350, y=270)
c16.place(x=780, y=220)  # -вум2
c17.place(x=780, y=270)
c18.place(x=780, y=320)

help_button.place(x=900, y=530)
sbros_avaria_button.place(x=600, y=530)
VUM1_vkl_button.place(x=100, y=510)
fs_vkl_button.place(x=450, y=510)
VUM2_vkl_button.place(x=740, y=510)
super_mega_okno.place(x=300, y=530)

VUM1_label.place(x=100, y=5)
fs_label.place(x=490, y=5)
VUM2_label.place(x=840, y=5)


VUM1_label_temp.place(x=10, y=50)
fs_label_temp.place(x=320, y=50)
VUM2_label_temp.place(x=740, y=50)
VUM1_temp.place(x=200, y=50)
fs_temp.place(x=510, y=50)
VUM2_temp.place(x=930, y=50)

VUM1_label_serN.place(x=10, y=80)
fs_label_serN.place(x=320, y=80)
VUM2_label_serN.place(x=740, y=80)
VUM1_serN.place(x=180, y=80)
fs_serN.place(x=490, y=80)
VUM2_serN.place(x=910, y=80)

VUM1_label_time.place(x=10, y=110)
fs_label_time.place(x=320, y=110)
VUM2_label_time.place(x=740, y=110)
VUM1_time.place(x=185, y=110)
fs_time.place(x=495, y=110)
VUM2_time.place(x=915, y=110)

VUM1_label_verN.place(x=10, y=140)
fs_label_verN.place(x=320, y=140)
VUM2_label_verN.place(x=740, y=140)
VUM1_verN.place(x=190, y=140)
fs_verN.place(x=500, y=140)
VUM2_verN.place(x=920, y=140)

VUM1_label_OK.place(x=115, y=180)
VUM1_label_KP.place(x=200, y=180)
fs_label_OK1.place(x=400, y=180)
fs_label_OK2.place(x=480, y=180)
fs_label_KP1.place(x=560, y=180)
fs_label_KP2.place(x=640, y=180)
VUM2_label_OK.place(x=845, y=180)
VUM2_label_KP.place(x=930, y=180)

VUM1_label_Pvh.place(x=10, y=230)
VUM1_label_Pvih.place(x=10, y=280)
VUM1_label_Potr.place(x=10, y=330)
fs_label_Pvih.place(x=320, y=230)
fs_label_Potr.place(x=320, y=280)
VUM2_label_Pvh.place(x=740, y=230)
VUM2_label_Pvih.place(x=740, y=280)
VUM2_label_Potr.place(x=740, y=330)

VUM1_Pvh_OK_label.place(x=115, y=230)
VUM1_Pvih_OK_label.place(x=115, y=280)
VUM1_Potr_OK_label.place(x=115, y=330)
VUM1_Pvh_KP_label.place(x=200, y=230)
VUM1_Pvih_KP_label.place(x=200, y=280)
VUM1_Potr_KP_label.place(x=200, y=330)

fs_Pvih_OK1_label.place(x=400, y=230)
fs_Potr_OK1_label.place(x=400, y=280)
fs_Pvih_OK2_label.place(x=480, y=230)
fs_Potr_OK2_label.place(x=480, y=280)
fs_Pvih_KP1_label.place(x=560, y=230)
fs_Potr_KP1_label.place(x=560, y=280)
fs_Pvih_KP2_label.place(x=640, y=230)
fs_Potr_KP2_label.place(x=640, y=280)

VUM2_Pvh_OK_label.place(x=845, y=230)
VUM2_Pvih_OK_label.place(x=845, y=280)
VUM2_Potr_OK_label.place(x=845, y=330)
VUM2_Pvh_KP_label.place(x=930, y=230)
VUM2_Pvih_KP_label.place(x=930, y=280)
VUM2_Potr_KP_label.place(x=930, y=330)

fazirovka_label.place(x=450, y=335)
fazirovka_OK_label.place(x=350, y=380)
fs_faza_plus_OK_button.place(x=390, y=380)
fs_faza_minus_OK_button.place(x=420, y=380)
fs_faza_OK_label.place(x=450, y=380)
fazirovka_KP_label.place(x=510, y=380)
fs_faza_plus_KP_button.place(x=550, y=380)
fs_faza_minus_KP_button.place(x=580, y=380)
fs_faza_KP_label.place(x=610, y=380)

VUM1_label_rabota.place(x=10, y=380)
VUM1_label_pitan_avaria.place(x=10, y=410)
VUM1_label_mod_avaria.place(x=10, y=440)
VUM1_rabota.place(x=150, y=380)
VUM1_pitan_avaria.place(x=150, y=410)
VUM1_mod_avaria.place(x=150, y=440)

fs_label_rabota.place(x=320, y=415)
fs_label_pitan_avaria.place(x=500, y=415)
fs_label_mod_avaria.place(x=320, y=445)
fs_rabota.place(x=385, y=415)
fs_pitan_avaria.place(x=570, y=415)
fs_mod_avaria.place(x=420, y=445)

VUM2_label_rabota.place(x=740, y=380)
VUM2_label_pitan_avaria.place(x=740, y=410)
VUM2_label_mod_avaria.place(x=740, y=440)
VUM2_rabota.place(x=880, y=380)
VUM2_pitan_avaria.place(x=880, y=410)
VUM2_mod_avaria.place(x=880, y=440)


thread_update_window.start()
thread_obmen.start()

window.mainloop()
