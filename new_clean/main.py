import tkinter, win32api, random, os, subprocess, time
from tkinter import *
from win32api import GetSystemMetrics
from datetime import datetime
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


bg_colors = ["#C0C0C0", "#CD5C5C", "#A9A9A9"]
font_name = ["Arial"]
max_value = [1, 2, 4, 6, 9, 12, 15, 18] # for each x from max_value -> max_num = 1ex ( 10 ^ x)
width = int(GetSystemMetrics(0) * 0.8)
height = int(GetSystemMetrics(1) * 0.8)
h_ratio = height / (10 ** 2)
w_ratio = width / (10 ** 7)
# width and length scaled down to 0.8
def window_exit():
    root.destroy() # close the root window and main program
#TO RECONFIGURE
def plot_graph(x_values, y_values):
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, marker='o')
    ax.set_xlabel('Time (miliseconds)')
    ax.set_ylabel('Number of Numbers')
    ax.set_title('Sorting Time vs Number of Numbers')

    return fig

def update_graph(x_values, y_values, m_frame):
    fig = plot_graph(x_values, y_values)
    canvas = FigureCanvasTkAgg(fig, master=m_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=10, pady=10)
#TO RECONFIGURE


# def redraw_graph(L, canvas, w, h):
#     # x[0] number of numbers x[1] runtime
#     canvas.delete("all")
#     # sort points based on runtime
#     L.sort(key = lambda x: x[0])
#     # base x coordonate for line - numbers
#     wa = w * 0.001
#     # base y coordonate for line - runtime
#     ha = h * 0.999
#     for el in L:
#         # process the new y for line based on nr of numbers
#         # nh = h - (0.064 * float(el[1] / ) * h)
#         nw = (float(el[0])) * w_ratio
#         nh = h - (float(el[1]) * 10 * h_ratio)  # * el[0]* w
#         print("COORD: ", nh, nw, " TIME: ", el[1])
#         canvas.create_line(wa, ha, nw, nh, fill = "green", width = 5)
#         wa = nw
#         ha = nh


def file_gen(type, sort_name) :
    # in the main folder will be folder with main for each sort
    # for each sort i will give in infile number of numbers
    os.chdir(f"{sort_name}/cmake-build-release")
    # change directory to executable of sorting method

    seconds = int(time.time() * 1000)
    # generate seed for random numbers based on seconds
    n = random.randint(1, 10 ** 4)
    # number of numbers
    if type == "small":
        x = random.randint(0, 2)
    else:
        x = random.randint(3, 7)
    # x is maximum number
    #os.system(f"{sort_name}.exe {seconds} {n} {x}")
    # call example: bubble.exe 218379324 1000 10
    max_number = 10 ** (max_value[x])
    subprocess.run([f"{sort_name}.exe", str(seconds), str(n), str(max_number)])
    # run sort
    output = open("output.out", "r")
    # read runtime
    runtime = output.readline()
    print(runtime)
    # convert to seconds
    runtime = str(float(runtime) * (10 ** (-6)))
    output.close()
    os.chdir(os.path.dirname(os.path.dirname(os.getcwd())))
    #change back to root directory
    return (runtime, n, x)


def sort_table(sort_name, sort_type):
    sort_tab = Tk() # create a new window
    sort_tab.title(sort_name + "small numbers")
    sort_tab.configure(bg = bg_colors[0])
    sort_tab.geometry(f"{width}x{height}")
    sort_tab_gf = Frame(sort_tab) # insert a frame in the tab
    sort_tab_gf.pack() # display the frame
    canvw = 0.8 * width # set the width
    canvh = 0.8 * height # and the height
    x_values = []
    y_values = []
    # create the first line to modify
    def sort_draw(): # function to redraw
        # get runtime for a small type sort
        (time, numbers, digit_nr) = file_gen("small", sort_name)
        # write in window results
        sort_label.config(text = f"Numbers: {numbers} of {max_value[digit_nr]} digits\nTime in seconds: {time}")
        # add number of numbers and time in draw table to be redrawn
        y_values.append(numbers)
        x_values.append(time)
        # redraw table
        #redraw_graph(table, sort_canvas, canvw, canvh)
        update_graph(x_values, y_values, sort_tab_gf)
        # repeat
        sort_label.after(1000, sort_draw)

    # create text label to write results
    sort_label = tkinter.Label(sort_tab, font = (font_name[0], int(0.02 * width)), background = bg_colors[0])
    # create exit button
    sort_exit = Button(sort_tab, text = "Exit", command = sort_tab.destroy, width = int(0.005 * width), height = int(0.003 * height), background = bg_colors[1], font = (font_name[0], int(0.01 * width)))
    sort_exit.place(x = width - 0.07 * width, y = 0.05 * height)
    sort_label.pack()
    sort_draw()
    sort_tab.mainloop()


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
btn_merge = Button( root , text="Merge Sort" , command = lambda: mainsort("merge") , font = ("Arial", int(0.012 * width)))
btn_merge.place( x = 0.20 * width , y = 0.2 * height )
# btn_shell = Button( root , text="Shell Sort" , command = shellS , font = ("Arial", int(0.012 * width)))
# btn_shell.place( x = 0.35 * width , y = 0.2 * height )
# btn_quick = Button( root , text="Quick Sort" , command = quickS , font = ("Arial", int(0.012 * width)))
# btn_quick.place( x = 0.5 * width , y = 0.2 * height )
btn_counting = Button( root , text="Counting Sort" , command = lambda: mainsort("counting") , font = ("Arial", int(0.012 * width)))
btn_counting.place( x = 0.65 * width , y = 0.2 * height )
btn_bubble = Button( root , text="Bubble Sort" , command = lambda: mainsort("bubble") , font = ("Arial", int(0.012 * width)))
btn_bubble.place( x = 0.8 * width , y = 0.2 * height )
root.mainloop() # repeat until window_exit