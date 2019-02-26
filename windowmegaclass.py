import tkinter
import opros
import threading
import time


def update_window2():
    while True:
        increment_phase_ok['text'] = opros.increment_phase_ok
        increment_phase_kp['text'] = opros.increment_phase_kp
        time.sleep(0.1)
        if len(opros.otvet[0]) > 10:
            pass
        if len(opros.otvet[1]) > 10:
            pass
        if len(opros.otvet[2]) > 10:
            pass

def start_stop():
    opros.flag_start_stop_obmen = not opros.flag_start_stop_obmen


def megawindow():
    global increment_phase_ok
    global increment_phase_kp
    window2 = tkinter.Tk()
    window2.title("Это супермега окно!")
    window2.geometry("300x200")

    write_param = tkinter.Button(window2, text='Отправить', width=10, heigh=1)
    start_stop_zapros = tkinter.Checkbutton(window2,
                                            text='Остановить\nобмен',
                                            command=start_stop,
                                            justify='left')
    increment_phase_ok = tkinter.Label(window2, text=opros.increment_phase_ok)
    increment_phase_kp = tkinter.Label(window2, text=opros.increment_phase_kp)
    increment_phase_ok_label = tkinter.Label(window2, text='Приращение фазы ОК')
    increment_phase_kp_label = tkinter.Label(window2, text='Приращение фазы КП')

    start_stop_zapros.place(x=190, y=10)
    write_param.place(x=190, y=160)
    increment_phase_ok.place(x=10, y=10)
    increment_phase_kp.place(x=10, y=30)
    increment_phase_ok_label.place(x=30, y=10)
    increment_phase_kp_label.place(x=30, y=30)

    a = threading.Thread(target=update_window2)
    a.start()
    window2.mainloop()


if __name__ == '__main__':
    megawindow()
