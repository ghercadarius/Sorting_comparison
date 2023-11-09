def bubble_afis_mic_main():
    bubble_mic = Tk()
    bubble_mic.title("bubble nr mici")
    bubble_mic.configure( bg="#C0C0C0" )
    bubble_mic.geometry(f"{width}x{height}")
    bubble_mic_gf = Frame( bubble_mic )
    bubble_mic_gf.pack( )
    bubble_mic_canvas = tkinter.Canvas( bubble_mic_gf , bg="#A9A9A9" , width=0.8 * width , height=0.8 * height )
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = [ ]
    bubble_mic_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill="green" , width=5 )
    bubble_mic_canvas.pack( )
    def bubbleafis_mic() :
        (bubble_time , n , x) = file_gen("mic", "bubblemic.in", "bubbles.exe", "bubblemic.out")
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}\n\n" )
        debug_file.close( )
        bubble_mic_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}" )
        table.append((n, bubble_time))
        redraw_graph(table, bubble_mic_canvas, canvw, canvh)
        bubble_mic_label.after( 100 , bubbleafis_mic )

    bubble_mic_label = tkinter.Label( bubble_mic , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    bubbleexit = Button( bubble_mic , text="exit" , command=bubble_mic.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    bubbleexit.place( x=width - 0.07 * width , y=0.05 * height )
    bubble_mic_label.pack()
    bubbleafis_mic()
    bubble_mic.mainloop()

def bubble_afis_mare_main():
    bubble_mare = Tk()
    bubble_mare.title("bubble nr mari")
    bubble_mare.configure( bg="#C0C0C0" )
    bubble_mare.geometry( f"{width}x{height}" )
    bubble_mare_gf = Frame( bubble_mare )
    bubble_mare_gf.pack( )
    bubble_mare_canvas = tkinter.Canvas( bubble_mare_gf , bg="#A9A9A9" , width = 0.8 * width, height = 0.8 * height)
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = []
    bubble_mare_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill = "green" , width = 5 )
    bubble_mare_canvas.pack( )
    def bubbleafis_mare() :
        (bubble_time , n , x) = file_gen( "mare", "bubblemare.in", "bubbles.exe", "bubblemare.out" )
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}\n\n" )
        debug_file.close( )
        bubble_mare_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}" )
        table.append((n, bubble_time))
        redraw_graph(table, bubble_mare_canvas, canvw, canvh)
        bubble_mare_label.after( 100 , bubbleafis_mare)

    bubble_mare_label = tkinter.Label( bubble_mare , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    bubble_mare_label.pack( )
    bubbleexit = Button( bubble_mare , text="exit" , command=bubble_mare.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    bubbleexit.place(x=width - 0.07 * width , y=0.05 * height )
    bubbleafis_mare()
    bubble_mare.mainloop( )

def bubbleS():
    img_bubble = Tk()
    img_bubble.title("bubble")
    img_bubble.configure( bg="#C0C0C0" )
    img_bubble.geometry(f"{width}x{height}")
    btn_bubble_mic = Button(img_bubble, text = "Numere mici (<= 10^4)", command = bubble_afis_mic_main,
                           font = ("Arial", int(0.012 * width)))
    btn_bubble_mic.place(x = 0.2 * width, y = 0.3 * height)
    btn_bubble_mare = Button(img_bubble, text = "Numere mari (>=10^4 si <=10^18)", command = bubble_afis_mare_main,
                            font = ("Arial", int(0.012 * width)))
    btn_bubble_mare.place(x = 0.4 * width, y = 0.3 * height)
    #def bubbleafis_mic() :
        #(bubble_time , n , x) = bubble_gen("mic")
        #debug_file = open( "random_tests.txt" , "a" )
        #debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}\n\n" )
        #debug_file.close( )
        #bubble_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}" )
        #bubble_label.after( 100 , bubbleafis_mic() )
    #def bubbleafis() :
     #   (bubble_time , n , x) = bubble_gen( )
      #  debug_file = open( "random_tests.txt" , "a" )
       # debug_file.write(f"\n{datetime.now()}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}\n\n")
       # debug_file.close()
       # bubble_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}" )
       # bubble_label.after( 100 , bubbleafis)

    #bubble_label = tkinter.Label( img_bubble , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    bubbleexit = Button( img_bubble , text="exit" , command=img_bubble.destroy , width=int( 0.005 * width ) , 
        height=int( 0.003 * height ) , background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    bubbleexit.place( x=width - 0.07 * width , y=0.05 * height )
    #bubble_label.pack( )
    #bubbleafis()
    img_bubble.mainloop()