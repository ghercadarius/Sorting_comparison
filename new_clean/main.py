import tkinter, win32api, random, os, subprocess, time
from tkinter import *
from win32api import GetSystemMetrics
from datetime import datetime
bg_colors = ["#C0C0C0", "#CD5C5C", "#A9A9A9"]
font_name = ["Arial"]
max_value = [1, 2, 4, 6, 9, 12, 15, 18] # for each x from max_value -> max_num = 1ex ( 10 ^ x)
width = int(GetSystemMetrics(0) * 0.8)
height = int(GetSystemMetrics(1) * 0.8)
# width and length scaled down to 0.8
def window_exit():
    root.destroy() # close the root window and main program

def file_gen(type, sort_name) :
    # in the main folder will be folder with main for each sort
    # for each sort i will give in infile number of numbers
    os.chdir(f"{sort_name}/cmake-build-debug")
    # change directory to executable of sorting method

    seconds = int(time.time() * 1000)
    # generate seed for random numbers
    n = random.randint(1, 10 ** 6)
    # number of numbers
    if type == "small":
        x = random.randint(0, 2)
    else:
        x = random.randint(3, 7)
    # x is maximum number
    #os.system(f"{sort_name}.exe {seconds} {n} {x}")
    subprocess.run([f"{sort_name}.exe", str(seconds), str(n), str(x)])
    # run sort
    output = open("output.out", "r")
    runtime = output.readline()
    # read runtime
    print(seconds, n, x)
    print("@")
    print(runtime)
    print("@")
    # if runtime != "init" and runtime != "err":
    #     runtime = str(float(runtime) * (10 ** (-6)))
    # else:
    #     print("@")
    output.close()

    os.chdir(os.path.dirname(os.path.dirname(os.getcwd())))
    #change back to root directory


def sort_table(sort_name, sort_type):
    sort_tab = Tk() # create a new window
    sort_tab.title(sort_name + "small numbers")
    sort_tab.configure(bg = bg_colors[0])
    sort_tab.geometry(f"{width}x{height}")
    sort_tab_gf = Frame(sort_tab) # insert a frame in the tab
    sort_tab_gf.pack() # display the frame
    small_sort_canvas = tkinter.Canvas(sort_tab_gf, bg = bg_colors[2], width = 0.8 * width, height = 0.8 * height)
    # create the drawing zone from the graph with a canvas
    canvw = 0.8 * width # set the width
    canvh = 0.8 * height # and the height
    table = []
    small_sort_canvas.create_line(0.02 * canvw, 0.98 * canvh, 0.9 * canvw, 0.1 * canvh, fill = "green", width = 5)
    # create the first line to modify
    small_sort_canvas.pack() # draw the line
    (timp, numere, maxim) = file_gen("small", sort_name)
    #DE RESCRIS file_gen pentru a compila codul sursa al lui sort_name si de scris file_gen de la 0
    #DE RESCRIS redraw_graph pentru a repara erorile din trecut

def mainsort(sort_name):
    sort_img = Tk() # create new window
    sort_img.title(sort_name) # name it after sort name
    sort_img.configure(bg = bg_colors[0]) # set background color
    sort_img.geometry(f"{width}x{height}") # set window height and width
    btn_small_sort = Button(sort_img, text = "Small numbers ( <= 10 ^ 4)", command =
                    lambda: sort_table(sort_name, "small"),font = (font_name[0], int(0.012 * width) ))
    # create button for small sort
    btn_small_sort.place(x = 0.2 * width, y = 0.3 * height) # place it in window
    btn_big_sort = Button(sort_img, text = "Big numbers ( >= 10 ^ 4 si <= 10 ^ 18)", command =
                    lambda: sort_table(sort_name, "big"), font = (font_name[0], int(0.012 * width)))
    # create button for big sort
    btn_big_sort.place(x = 0.4 * width, y = 0.3 * height) # place it
    sortare_exit = Button(sort_img, text = "Exit", command = sort_img.destroy, width = int(0.005 * width),
                    height = int(0.003 * height), background = bg_colors[1], font = (font_name[0], int(0.012 * width)))
    # create button for exit
    sort_img.mainloop()

def bubbleS():
    mainsort("bubble")

root = Tk() # create root window
root.title("Sorting Methods") # name it
root.configure(bg="#C0C0C0") # set background color
random.seed() # initialise the random seed to default ( time )
root.geometry( f"{width}x{height}") # set width and height
name = tkinter.Label(text="Sorting Methods", font = ("Arial", int(0.02*width)), background="#C0C0C0", height = 2)
# create text box
name.pack() # display text box
exit = Button( root , text = "exit", command = window_exit, width = int(0.005 * width), height = int(0.003 * height),
               background = "#CD5C5C", font = ("Arial", int(0.01*width))) # create exit button
exit.place( x = width - 0.07 * width, y = 0.05 * height) # place exit button
# create button for each sorting method
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
root.mainloop() # repeat until window_exit