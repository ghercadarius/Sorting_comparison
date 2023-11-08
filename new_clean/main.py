import tkinter, win32api, random, os, subprocess, time
from tkinter import *
from win32api import GetSystemMetrics
from datetime import datetime
culori_bg = ["#C0C0C0", "#CD5C5C", "#A9A9A9"]
nume_font = ["Arial"]
max_value = [1, 2, 4, 6, 9, 12, 15, 18] # x apartine max_value in a calcula valoarea maxima a unui numar intr-o sortare
# de exemplu daca x este 2 atunci nr maxim intr-o sortare este 1e2 (10 ^ 2)
width = int(GetSystemMetrics(0) * 0.8) # preluam latimea ferestrei din getsystemmetrics si o ajustam sa fie 0.8 pentru
# a fi sigur ca incape in ecran
height = int(GetSystemMetrics(1) * 0.8) # analog
def window_exit():
    root.destroy()

def sortare_tabel(nume_sortare, tip_sortare):
    sortare_tab = Tk() # cream un window nou
    sortare_tab.title(nume_sortare + "numere mici")
    sortare_tab.configure(bg = culori_bg[0])
    sortare_tab.geometry(f"{width}x{height}")
    sortare_tab_gf = Frame(sortare_tab) # structuram tab-ul intr-un frame
    sortare_tab_gf.pack() # afisam frame-ul
    sortare_mica_canvas = tkinter.Canvas(sortare_tab_gf, bg = culori_bg[2], width = 0.8 * width, height = 0.8 * height) # cream zona de desenat a graficului cu un canvas
    canvw = 0.8 * width # setam latinea
    canvh = 0.8 * height # si inaltimea
    table = []
    sortare_mica_canvas.create_line(0.02 * canvw, 0.98 * canvh, 0.9 * canvw, 0.1 * canvh, fill = "green", width = 5) # cream prima linie
    sortare_mica_canvas.pack() # o desenam
    #(timp, numere, maxim) = file_gen("mic", nume_sortare + tip_sortare + ".in", nume_sortare)
    #DE RESCRIS file_gen pentru a compila codul sursa al lui nume_sortare si de scris file_gen de la 0
    #DE RESCRIS redraw_graph pentru a repara erorile din trecut

def sortare(nume_sortare):
    img_sortare = Tk() # creeam o noua fereastra
    img_sortare.title(nume_sortare) # o denumim dupa sortarea aleasa
    img_sortare.configure(bg = culori_bg[0])
    img_sortare.geometry(f"{width}x{height}")
    btn_sortare_mic = Button(img_sortare, text = "Numere mici ( <= 10 ^ 4)", command =
                            lambda: sortare_tabel(nume_sortare, "mic"),font = (nume_font[0], int(0.012 * width) ))
    btn_sortare_mic.place(x = 0.2 * width, y = 0.3 * height)
    btn_sortare_mare = Button(img_sortare, text = "Numere mari ( >= 10 ^ 4 si <= 10 ^ 18)", command =
                            lambda: sortare_tabel(nume_sortare, "mare"), font = (nume_font[0], int(0.012 * width)))
    btn_sortare_mare.place(x = 0.4 * width, y = 0.3 * height)
    sortare_exit = Button(img_sortare, text = "Exit", command = img_sortare.destroy, width = int(0.005 * width),
                          height = int(0.003 * height), background = culori_bg[1], font = (nume_font[0], int(0.012 * width)))
    img_sortare.mainloop()

def bubbleS():
    sortare("bubble")

root = Tk()
root.title("Sortari")
root.configure(bg="#C0C0C0")
random.seed()
root.geometry( f"{width}x{height}")
name = tkinter.Label(text="Sortari", font = ("Arial", int(0.02*width)), background="#C0C0C0", height = 2)
name.pack()
exit = Button( root , text = "exit", command = window_exit, width = int(0.005 * width), height = int(0.003 * height),
               background = "#CD5C5C", font = ("Arial", int(0.01*width)))
exit.place( x = width - 0.07 * width, y = 0.05 * height)
# btn_radix = Button( root , text="Radix Sort" , command = radixS , font = ("Arial", int(0.012 * width)))
# btn_radix.place( x = 0.05 * width , y = 0.2 * height )
# btn_merge = Button( root , text="Merge Sort" , command = mergeS , font = ("Arial", int(0.012 * width)))
# btn_merge.place( x = 0.20 * width , y = 0.2 * height )
# btn_shell = Button( root , text="Shell Sort" , command = shellS , font = ("Arial", int(0.012 * width)))
# btn_shell.place( x = 0.35 * width , y = 0.2 * height )
# btn_quick = Button( root , text="Quick Sort" , command = quickS , font = ("Arial", int(0.012 * width)))
# btn_quick.place( x = 0.5 * width , y = 0.2 * height )
# btn_counting = Button( root , text="Counting Sort" , command = countS , font = ("Arial", int(0.012 * width)))
# btn_counting.place( x = 0.65 * width , y = 0.2 * height )
btn_bubble = Button( root , text="Bubble Sort" , command = bubbleS , font = ("Arial", int(0.012 * width)))
btn_bubble.place( x = 0.8 * width , y = 0.2 * height )
root.mainloop( )