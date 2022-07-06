#!/usr/bin/env python3


# Graphical User Interface.


# IMPORT MODUL PYTHON 3
import os
from os import *
# UNDUH MODUL YANG DIPERLUKAN.
# system("pip install pyfiglet")
# system("pip install pywhatkit")
# system("pip install tk")
system("clear")


import sys
from sys import *
# CEK VERSI PYTHON YANG TERUNDUH DI LAPTOP,KOMPUTER ATAU HANDPHONE USER.
if not sys.version_info.major==3:
	print("[!] Program GUI Ini Membutuhkan Python Versi 3")
	print("[!] Silahkan Install Python Versi 3")
	print("[!] Have A Good Day!\n")
elif sys.version_info.major==3:
	print("[!] Terima Kasih!")


import pyfiglet
from pyfiglet import *
Tampilan_Awal_Program_GUI=Figlet(font="smscript")
print(Tampilan_Awal_Program_GUI.renderText("PyGUI"))
print("[!] Dibuat Oleh: Ruben Leonardo Sigalingging.")
print("[!] Dibuat Pada: Selasa, 5 Juli, 2022, Pukul 22:27 PM.")
print("[!] Fungsi: Mengirim Pesan WhatsApp.")


import tkinter
from tkinter import *
import pywhatkit
from pywhatkit import *
from time import *


# BUAT FUNGSI UNTUK MEMBUAT GUI NYA.
def PyWhatKit_Graphical_User_Interface(Created_By="Ruben Leonardo Sigalingging"):
	# BUAT FUNGSI UTAMA GUI NYA, DENGAN METODE VAR=Tk()
	Fungsi_Utama=Tk()


	# UBAH TITLE ATAU JUDUL PROGRAM
	Fungsi_Utama.title("PyWhatKit Graphical User Interface")


	# UBAH WARNA BACKGROUND ATAU WARNA LATAR BELAKANG GUI, DENGAN METODE .CONFIGURE(BG="WARNA YANG KAMU PILIH")
	# Python - Tkinter Cursors
	Fungsi_Utama.configure(background="#000000",cursor="crosshair")


	# UBAH UKURAN JENDELA ROOT TKINTER SESUAI KEBUTUHAN PENGGUNA.
	# DENGAN METODE .RESIZABLE(3,3), .RESIZABLE()
	# Fungsi_Utama.resizable(width=True,height=True)


	# UBAH UKURAN LAYAR PROGRAM GUI NYA, DENGAN METODE .GEOMETRY("100X100")
	Fungsi_Utama.geometry("400x500")


	# UBAH UKURAN TEXT JUDUL PROGRAM GUI.
	Judul_Program_GUI_Pertama=Label(Fungsi_Utama,underline=(10),text=("PyWhatKit Graphical User Interface\nCreated By Ruben Leonardo Sigalingging."),height=3,activebackground="#008b8b",activeforeground="#008b8b",relief="solid",font=("Ubuntu",24,"bold"),anchor="center",cursor="pirate",width=48,background="#008b8b",foreground="#ffffff")
	Judul_Program_GUI_Pertama.pack(padx=25,pady=25,side="top")


	# BUAT TOMBOL UNTUK MENGINPUTKAN NOMOR TELEPON.
	Tombol_Input_Nomor_Telepon=Label(Fungsi_Utama,text="Input Nomor Telepon",font=("Ubuntu",15),width=20,bg="#ffffff",foreground="#008b8b",justify="center")
	Tombol_Input_Nomor_Telepon.pack(padx=0,pady=0)
	Tombol_Input_Nomor_Telepon=Entry(Fungsi_Utama,text="Input Nomor Telepon",bg="#008b8b",bd=2,cursor="spider",relief="solid",font=("Times",24,"bold","italic"),selectbackground="#008000",selectforeground="#008000",fg="#8b0000",justify="center",width=24)
	Tombol_Input_Nomor_Telepon.pack(padx=0,pady=0,side="top")


	# BUAT TOMBOL UNTUK MENGIRIM PESAN.
	Tombol_Input_Pesan=Label(Fungsi_Utama,text="Input Pesan WhatsApp",font=("Ubuntu",15),width=20,bg="#ffffff",foreground="#008b8b",justify="center")
	Tombol_Input_Pesan.pack(padx=0,pady=0)
	Tombol_Input_Pesan=Entry(Fungsi_Utama,text="Input Pesan WhatsApp",bg="#008b8b",bd=2,cursor="spider",relief="solid",font=("Times",24,"bold","italic"),selectbackground="#008000",selectforeground="#008000",fg="#8b0000",justify="center",width=24)
	Tombol_Input_Pesan.pack(padx=0,pady=0,side="top")


	# BUAT TOMBOL UNTUK INPUT JAM ATAU HOUR
	Tombol_Input_Jam=Label(Fungsi_Utama,text="Input Jam atau Hour",font=("Ubuntu",15),width=20,bg="#ffffff",foreground="#008b8b",justify="center")
	Tombol_Input_Jam.pack(padx=0,pady=0)
	Tombol_Input_Jam=Entry(Fungsi_Utama,text="Input Pesan WhatsApp",bg="#008b8b",bd=2,cursor="spider",relief="solid",font=("Times",24,"bold","italic"),selectbackground="#008000",selectforeground="#008000",fg="#8b0000",justify="center",width=24)
	Tombol_Input_Jam.pack(padx=0,pady=0,side="top")


	Tombol_Input_Menit=Label(Fungsi_Utama,text="Input Input Menit",font=("Ubuntu",15),width=20,bg="#ffffff",foreground="#008b8b",justify="center")
	Tombol_Input_Menit.pack(padx=0,pady=0)
	Tombol_Input_Menit=Entry(Fungsi_Utama,text="Input Pesan WhatsApp",bg="#008b8b",bd=2,cursor="spider",relief="solid",font=("Times",24,"bold","italic"),selectbackground="#008000",selectforeground="#008000",fg="#8b0000",justify="center",width=24)
	Tombol_Input_Menit.pack(padx=0,pady=0,side="top")


	# BUAT MENU PROGRAM
	Label_Program_Ke_1=Button(Fungsi_Utama,width=30,height=1,text=("Sending Message To A Contact"),font=("Ubuntu",15,"bold"),activebackground="#008b8b",activeforeground="#ffffff",bd=2,background="#ffffff",foreground="#008b8b",cursor="clock")
	Label_Program_Ke_1.pack(padx=5,pady=5)


	# BUAT PROGRAM BERJALAN TERUS.
	Fungsi_Utama.mainloop()


PyWhatKit_Graphical_User_Interface()