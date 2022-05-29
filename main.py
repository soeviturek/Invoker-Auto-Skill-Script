import keyboard
import ctypes
import time

# https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


if __name__ == '__main__':
    d = {'q': 0x10, 'w': 0x11, 'e': 0x12}
    last_input_key = 0x10
    enable_cheat = True
    enable_help = False
    print("T: Sunstrike\n"
          "Y: Cold Snap\n"
          "X: Tornado\n"
          "G: EMP\n"
          "3: Alacrity\n"
          "4: Forge Spirit\n"
          "C: Chaos Meteor\n"
          "V: Super Wave\n"
          "H: Ghost Walk\n"
          "F12: Enable Cheat\nF11: Enable Help")

    while (True):
        if keyboard.is_pressed('q'):
            last_input_key = d.get('q')
        if keyboard.is_pressed('w'):
            last_input_key = d.get('w')
        if keyboard.is_pressed('e'):
            last_input_key = d.get('e')
        # https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html
        # Q = 0x10
        # W = 0x11
        # E = 0x12
        # R = 0x13
        # D = 0x20
        # F = 0x21
        if keyboard.is_pressed('F12'):
            time.sleep(1)
            if enable_cheat:
                enable_cheat = False
            else:
                enable_cheat = True
        if keyboard.is_pressed('F11'):
            time.sleep(1)
            if enable_help:
                enable_help = False
            else:
                print("helpo enabled")
                enable_help = True
        if enable_help:
            if keyboard.is_pressed('a'):
                #switch to exort
                PressKey(0x12)
                ReleaseKey(0x12)
                PressKey(0x12)
                ReleaseKey(0x12)
                PressKey(0x12)
                ReleaseKey(0x12)
                time.sleep(0.4)
                #return to last element
                PressKey(last_input_key)
                ReleaseKey(last_input_key)
                PressKey(last_input_key)
                ReleaseKey(last_input_key)
                PressKey(last_input_key)
                ReleaseKey(last_input_key)

        if enable_cheat:
            if keyboard.is_pressed('t'):  # sun strike
                PressKey(0x12)
                ReleaseKey(0x12)
                PressKey(0x12)
                ReleaseKey(0x12)
                PressKey(0x12)
                ReleaseKey(0x12)
                PressKey(0x13)
                ReleaseKey(0x13)
                time.sleep(0.3)
            elif keyboard.is_pressed('y'):  # 急速冷却
                PressKey(0x10)
                ReleaseKey(0x10)
                PressKey(0x10)
                ReleaseKey(0x10)
                PressKey(0x10)
                ReleaseKey(0x10)
                PressKey(0x13)
                ReleaseKey(0x13)
                time.sleep(0.3)
            elif keyboard.is_pressed('x'):  # 吹风
                PressKey(0x11)
                ReleaseKey(0x11)
                PressKey(0x11)
                ReleaseKey(0x11)
                PressKey(0x10)
                ReleaseKey(0x10)
                PressKey(0x13)
                ReleaseKey(0x13)
                time.sleep(0.3)
            elif keyboard.is_pressed('g'):  # 磁暴
                PressKey(0x11)
                ReleaseKey(0x11)
                PressKey(0x11)
                ReleaseKey(0x11)
                PressKey(0x11)
                ReleaseKey(0x11)
                PressKey(0x13)
                ReleaseKey(0x13)
                time.sleep(0.3)
            elif keyboard.is_pressed('3'):  # 灵动迅捷
                PressKey(0x11)
                ReleaseKey(0x11)
                PressKey(0x11)
                ReleaseKey(0x11)
                PressKey(0x12)
                ReleaseKey(0x12)
                PressKey(0x13)
                ReleaseKey(0x13)
                time.sleep(0.3)
            elif keyboard.is_pressed('4'):  # forge spirit
                PressKey(0x12)
                ReleaseKey(0x12)
                PressKey(0x12)
                ReleaseKey(0x12)
                PressKey(0x10)
                ReleaseKey(0x10)
                PressKey(0x13)
                ReleaseKey(0x13)
                time.sleep(0.3)
            elif keyboard.is_pressed('c'):  # chaos meteor
                PressKey(0x12)
                ReleaseKey(0x12)
                PressKey(0x12)
                ReleaseKey(0x12)
                PressKey(0x11)
                ReleaseKey(0x11)
                PressKey(0x13)
                ReleaseKey(0x13)
                time.sleep(0.3)
            elif keyboard.is_pressed('v'):  # suerwave
                PressKey(0x10)
                ReleaseKey(0x10)
                PressKey(0x11)
                ReleaseKey(0x11)
                PressKey(0x12)
                ReleaseKey(0x12)
                PressKey(0x13)
                ReleaseKey(0x13)
                time.sleep(0.3)
            elif keyboard.is_pressed('h'):  # ghostwalk
                PressKey(0x10)
                ReleaseKey(0x10)
                PressKey(0x10)
                ReleaseKey(0x10)
                PressKey(0x11)
                ReleaseKey(0x11)
                PressKey(0x13)
                ReleaseKey(0x13)
                time.sleep(0.2)
                # press D
                PressKey(0x20)
                ReleaseKey(0x20)
                time.sleep(0.3)
