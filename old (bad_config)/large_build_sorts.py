import tkinter, win32api, random, os, subprocess, time
from tkinter import *
from win32api import GetSystemMetrics
from datetime import datetime


max_value = [1, 2, 4, 6, 9, 12, 15, 18]
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

def window_exit():
    root.destroy()

def redraw_graph(L, canvas, w, h):
    canvas.delete("all")
    L.sort(key = lambda x: x[0])
    wa = w * 0.001
    ha = h * 0.999
    for el in L:
        if float(el[1]) < 0.5:
            nh = h - 0.6 * float( el[ 1 ] ) * h
        elif float(el[1]) < 10:
            nh = h - 0.3 * h - 0.03 * float( el[ 1 ] ) * h
        else:
            nh = h - 0.6 * h - 0.1 * float(el[1]) * h
        #nh = h - 0.064 * float(el[1]) * h
        nw = (0.96 * el[0] * w) / 100000000 #* el[0]* w
        print(nh, nw)
        canvas.create_line( wa , ha , nw , nh , fill = "green" , width = 5 )
        wa = nw
        ha = nh

def file_gen(var, infile, exec, outfile) :
    mainfile = open("file_name.in", "w")
    mainfile.write(infile + " " + outfile + "\n")
    mainfile.close()
    n = random.randint( 1 , 10 ** 8)
    if var == "mic":
        x = random.randint( 0 , 2 )
    elif var == "mare":
        x = random.randint(3, 7)
    seconds = int(time.time()*1000)
    ifile = open( infile , "w" )
    ifile.write( f"{seconds}\n{n}\n{10 ** max_value[x]}" )
    #for y in range( n ) :
        #fradix.write( str( random.randint( 1 , 10 ** max_value[ x ] ) ) + "\n" )
    ifile.close( )
    # win32api.ShellExecute( 0 , "open" , "radix/radixs.exe" , None , "/" , 0 )
    os.system( exec )
    # subprocess.run("radix/radixs.exe")
    ofile = open( outfile , "r" )
    radix_time = ofile.read( )
    if time != "alocat" and time != "err":
        time = str( float( time ) * (10 ** (-6)) )
    ofile.close( )
    return (time , n , x)

def radix_afis_mic_main():
    radix_mic = Tk()
    radix_mic.title("Radix nr mici")
    radix_mic.configure( bg="#C0C0C0" )
    radix_mic.geometry(f"{width}x{height}")
    radix_mic_gf = Frame( radix_mic )
    radix_mic_gf.pack( )
    radix_mic_canvas = tkinter.Canvas( radix_mic_gf , bg="#A9A9A9" , width=0.8 * width , height=0.8 * height )
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = [ ]
    radix_mic_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill="green" , width=5 )
    radix_mic_canvas.pack( )
    def radixafis_mic() :
        (radix_time , n , x) = file_gen("mic", "rsmic.in", "radixsmic.exe", "rsmic.out")
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}\n\n" )
        debug_file.close( )
        radix_mic_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}" )
        redraw_graph(table, radix_mic_canvas, canvw, canvh)
        radix_mic_label.after( 100 , radixafis_mic )

    radix_mic_label = tkinter.Label( radix_mic , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    radexit = Button( radix_mic , text="exit" , command=radix_mic.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    radexit.place( x=width - 0.07 * width , y=0.05 * height )
    radix_mic_label.pack()
    radixafis_mic()
    radix_mic.mainloop()

def radix_afis_mare_main():
    radix_mare = Tk()
    radix_mare.title("Radix nr mari")
    radix_mare.configure( bg="#C0C0C0" )
    radix_mare.geometry( f"{width}x{height}" )
    radix_mare_gf = Frame( radix_mare )
    radix_mare_gf.pack( )
    radix_mare_canvas = tkinter.Canvas( radix_mare_gf , bg="#A9A9A9" , width = 0.8 * width, height = 0.8 * height)
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = []
    radix_mare_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill = "green" , width = 5 )
    radix_mare_canvas.pack( )
    def radixafis_mare() :
        (radix_time , n , x) = file_gen( "mare", "rsmare.in", "radixsmare.exe", "rsmare.out" )
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}\n\n" )
        debug_file.close( )
        radix_mare_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}" )
        table.append((n, radix_time))
        redraw_graph(table, radix_mare_canvas, canvw, canvh)
        radix_mare_label.after( 100 , radixafis_mare)

    radix_mare_label = tkinter.Label( radix_mare , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    radix_mare_label.pack( )
    radexit = Button( radix_mare , text="exit" , command=radix_mare.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    radexit.place(x=width - 0.07 * width , y=0.05 * height )
    radixafis_mare()
    radix_mare.mainloop( )

def radixS():
    img_radix = Tk()
    img_radix.title("Radix")
    img_radix.configure( bg="#C0C0C0" )
    img_radix.geometry(f"{width}x{height}")
    btn_radix_mic = Button(img_radix, text = "Numere mici (<= 10^4)", command = radix_afis_mic_main,
                           font = ("Arial", int(0.012 * width)))
    btn_radix_mic.place(x = 0.2 * width, y = 0.3 * height)
    btn_radix_mare = Button(img_radix, text = "Numere mari (>=10^4 si <=10^18)", command = radix_afis_mare_main,
                            font = ("Arial", int(0.012 * width)))
    btn_radix_mare.place(x = 0.4 * width, y = 0.3 * height)
    #def radixafis_mic() :
        #(radix_time , n , x) = radix_gen("mic")
        #debug_file = open( "random_tests.txt" , "a" )
        #debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}\n\n" )
        #debug_file.close( )
        #radix_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}" )
        #radix_label.after( 100 , radixafis_mic() )
    #def radixafis() :
     #   (radix_time , n , x) = radix_gen( )
      #  debug_file = open( "random_tests.txt" , "a" )
       # debug_file.write(f"\n{datetime.now()}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}\n\n")
       # debug_file.close()
       # radix_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}" )
       # radix_label.after( 100 , radixafis)

    #radix_label = tkinter.Label( img_radix , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    radexit = Button( img_radix , text="exit" , command=img_radix.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    radexit.place( x=width - 0.07 * width , y=0.05 * height )
    #radix_label.pack( )
    #radixafis()
    img_radix.mainloop()

def merge_afis_mic_main():
    merge_mic = Tk()
    merge_mic.title("Merge nr mici")
    merge_mic.configure( bg="#C0C0C0" )
    merge_mic.geometry(f"{width}x{height}")
    merge_mic_gf = Frame( merge_mic )
    merge_mic_gf.pack( )
    merge_mic_canvas = tkinter.Canvas( merge_mic_gf , bg="#A9A9A9" , width=0.8 * width , height=0.8 * height )
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = [ ]
    merge_mic_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill="green" , width=5 )
    merge_mic_canvas.pack( )
    def mergeafis_mic() :
        (merge_time , n , x) = file_gen("mic", "mergmic.in", "mergesmic.exe", "mergmic.out")
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}\n\n" )
        debug_file.close( )
        merge_mic_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}" )
        redraw_graph(table, merge_mic_canvas, canvw, canvh)
        merge_mic_label.after( 100 , mergeafis_mic )

    merge_mic_label = tkinter.Label( merge_mic , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    mergexit = Button( merge_mic , text="exit" , command=merge_mic.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    mergexit.place( x=width - 0.07 * width , y=0.05 * height )
    merge_mic_label.pack()
    mergeafis_mic()
    merge_mic.mainloop()

def merge_afis_mare_main():
    merge_mare = Tk()
    merge_mare.title("Merge nr mari")
    merge_mare.configure( bg="#C0C0C0" )
    merge_mare.geometry( f"{width}x{height}" )
    merge_mare_gf = Frame( merge_mare )
    merge_mare_gf.pack( )
    merge_mare_canvas = tkinter.Canvas( merge_mare_gf , bg="#A9A9A9" , width = 0.8 * width, height = 0.8 * height)
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = []
    merge_mare_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill = "green" , width = 5 )
    merge_mare_canvas.pack( )
    def mergeafis_mare() :
        (merge_time , n , x) = file_gen( "mare", "rsmare.in", "mergesmare.exe", "rsmare.out" )
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}\n\n" )
        debug_file.close( )
        merge_mare_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}" )
        table.append((n, merge_time))
        redraw_graph(table, merge_mare_canvas, canvw, canvh)
        merge_mare_label.after( 100 , mergeafis_mare)

    merge_mare_label = tkinter.Label( merge_mare , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    merge_mare_label.pack( )
    mergexit = Button( merge_mare , text="exit" , command=merge_mare.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    mergexit.place(x=width - 0.07 * width , y=0.05 * height )
    mergeafis_mare()
    merge_mare.mainloop( )

def mergeS():
    img_merge = Tk()
    img_merge.title("Merge")
    img_merge.configure( bg="#C0C0C0" )
    img_merge.geometry(f"{width}x{height}")
    btn_merge_mic = Button(img_merge, text = "Numere mici (<= 10^4)", command = merge_afis_mic_main,
                           font = ("Arial", int(0.012 * width)))
    btn_merge_mic.place(x = 0.2 * width, y = 0.3 * height)
    btn_merge_mare = Button(img_merge, text = "Numere mari (>=10^4 si <=10^18)", command = merge_afis_mare_main,
                            font = ("Arial", int(0.012 * width)))
    btn_merge_mare.place(x = 0.4 * width, y = 0.3 * height)
    #def mergeafis_mic() :
        #(merge_time , n , x) = merge_gen("mic")
        #debug_file = open( "random_tests.txt" , "a" )
        #debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}\n\n" )
        #debug_file.close( )
        #merge_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}" )
        #merge_label.after( 100 , mergeafis_mic() )
    #def mergeafis() :
     #   (merge_time , n , x) = merge_gen( )
      #  debug_file = open( "random_tests.txt" , "a" )
       # debug_file.write(f"\n{datetime.now()}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}\n\n")
       # debug_file.close()
       # merge_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}" )
       # merge_label.after( 100 , mergeafis)

    #merge_label = tkinter.Label( img_merge , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    mergexit = Button( img_merge , text="exit" , command=img_merge.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    mergexit.place( x=width - 0.07 * width , y=0.05 * height )
    #merge_label.pack( )
    #mergeafis()
    img_merge.mainloop()

def shellS():
    top = Toplevel( root , background="#808080" )
    top.mainloop( )

def quickS():
    top = Toplevel( root , background="#808080" )
    top.mainloop( )

def countingS():
    top = Toplevel( root , background="#808080" )
    top.mainloop( )

def bubbleS():
    top = Toplevel( root , background="#808080" )
    top.mainloop( )

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
btn_radix = Button( root , text="Radix Sort" , command = radixS , font = ("Arial", int(0.012 * width)))
btn_radix.place( x = 0.05 * width , y = 0.2 * height )
btn_merge = Button( root , text="Merge Sort" , command = mergeS , font = ("Arial", int(0.012 * width)))
btn_merge.place( x = 0.20 * width , y = 0.2 * height )
btn_shell = Button( root , text="Shell Sort" , command = shellS , font = ("Arial", int(0.012 * width)))
btn_shell.place( x = 0.35 * width , y = 0.2 * height )
btn_quick = Button( root , text="Quick Sort" , command = quickS , font = ("Arial", int(0.012 * width)))
btn_quick.place( x = 0.5 * width , y = 0.2 * height )
btn_counting = Button( root , text="Counting Sort" , command = countingS , font = ("Arial", int(0.012 * width)))
btn_counting.place( x = 0.65 * width , y = 0.2 * height )
btn_bubble = Button( root , text="Bubble Sort" , command = bubbleS , font = ("Arial", int(0.012 * width)))
btn_bubble.place( x = 0.8 * width , y = 0.2 * height )
root.mainloop( )
