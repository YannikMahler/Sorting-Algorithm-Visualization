from tkinter import *
from tkinter import ttk
import random
import time
from sort_algorithm import bubble_sort


root = Tk()
root.title('Sorting Algorithm Visualisation')
root.geometry('1010x580')
root.config(bg='#121212')
root.iconphoto(False, PhotoImage(file='img/chemistry_16px.png'))

#Variabeln 
data = []
choose_algo = StringVar

def drawData(data):
    canvas.delete("all")
    
    c_width= 990
    c_height= 450
    x_width= c_width / (len(data))
    offset= 15
    spacing= 10
    normalizedData= [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0= i * x_width + offset + spacing
        y0= c_height - height * 340
        
        #bottom right
        x1= (i + 1) * x_width + offset
        y1= c_height
        
        canvas.create_rectangle(x0, y0, x1, y1, fill= 'red')
        canvas.create_text(x0+2, y0, anchor=SW, text= str(data[i]))
    
    root.update_idletasks()
        
        
        
def generate():
    global data 
    
    minVal= int(Min_Scale.get())
    maxVal= int(Max_Scale.get())
    size= int(Size_scale.get())
    
    if minVal > maxVal : minVal, maxVal = maxVal, minVal
    
    data= []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))
        
    drawData(data) 
    
def Start():
    global data
    bubble_sort(data, drawData, Speed_Scale.get())
    
def stop():
    print('Yes')
    
    
    
# User Interface
UI_Frame = Frame(root, width= 1500, height=200, bg= '#383838')
UI_Frame.grid(row= 0, column= 0, padx=10, pady= 5)
#row[0]
Label(UI_Frame, text='Algorithmus:', bg='#383838').grid(row=0, column=0, padx= 5, pady= 5, sticky= W)
AlgoMenu = ttk.Combobox(UI_Frame, textvariable= 'choose_algo', values=['Choose Algorithm',
                                                                            'Selectionsort',
                                                                            'Bubblesort',
                                                                            'Quicksort',
                                                                            'Mergesort',
                                                                            'Inserstionsort'])
AlgoMenu.grid(row= 0, column= 1, padx= 5, pady= 5)
AlgoMenu.current(0)
StartButton = Button(UI_Frame, text= 'Start', command= Start, bg= '#65a22b')
StartButton. grid(row= 0, column= 2, padx= 5, pady= 5, sticky= W )
GenerateButton = Button(UI_Frame, text= 'Generate', command=generate, bg= '#d6c535')
GenerateButton. grid(row= 0, column= 3, padx= 5, pady= 5, sticky= W )
StopButton = Button(UI_Frame, text= 'Stop', command=stop, bg= 'red')
StopButton. grid(row= 0, column= 4, padx= 5, pady= 5, sticky= W )

#row[1]

Label(UI_Frame, text='Array Size', bg= '#383838').grid(row=1, column=0, padx= 5, pady= 5, sticky= W)
Size_scale= Scale(UI_Frame, from_=0, to=50, orient= HORIZONTAL, showvalue= 1)
Size_scale. grid(row= 1, column= 1, padx= 5, pady= 5, sticky= W)

Label(UI_Frame, text='Min Value', bg= '#383838').grid(row=1, column=2, padx= 5, pady= 5, sticky= W)
Min_Scale= Scale(UI_Frame, from_=0, to=50, orient= HORIZONTAL, showvalue= 1)
Min_Scale. grid(row= 1, column= 3, padx= 5, pady= 5, sticky= W )

Label(UI_Frame, text='Max Value', bg= '#383838').grid(row=1, column=4, padx= 5, pady= 5, sticky= W)
Max_Scale= Scale(UI_Frame, from_=0, to=50, orient= HORIZONTAL, showvalue= 1)
Max_Scale. grid(row= 1, column= 5, padx= 5, pady= 5, sticky= W )

Label(UI_Frame, text='Speed [s]', bg= '#383838').grid(row=0, column=5, padx= 5, pady= 5, sticky= W)
Speed_Scale= Scale(UI_Frame, from_=0.1, to=2.0, length=100, digits= 2, resolution= 0.2, orient= HORIZONTAL, showvalue= 1)
Speed_Scale. grid(row= 0, column= 6, padx= 5, pady= 5, sticky= W )


#Canvas
canvas = Canvas(root, width= 990, height= 450, bg= '#FFFFFF')
canvas.grid(row= 1, column= 0, padx= 10, pady= 10, sticky= S)


root.mainloop()