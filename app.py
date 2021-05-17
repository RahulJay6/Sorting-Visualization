## Bubble Sort Application

from tkinter import *
import creator
import sorter

bar_start = 2
bar_end = 8
bar_gap = 8


class start_window(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        Frame.grid(self)

def draw(sizes, canvas):
    canvas.delete("all")
    for i in range(0,len(sizes.numbers)):
        canvas.create_rectangle(bar_start+(i*bar_gap), 300-250*(sizes.numbers[i]/float(100)), bar_end+(i*bar_gap), 300, fill="red")

def generate(sizes,canvas):
    sizes.createlist()
    draw(sizes,canvas)


if __name__ == '__main__': 
    ## Initial Stuff
    root = Tk()
    root.geometry("1010x400")
    root.title = "Application"
    root.wm_title(root.title)

    a = Label(root, text ="Bubble Sorter")
    a.grid(row=0,column=1)

    ##Canvas creation
    canvas = Canvas(root, width = 1010, height = 300)  
    canvas.grid(row=2,column=0,columnspan = 3)  
    sizes = creator.Collection()
    sizes.createlist()

    #Buttons
    B1=Button(root, text ="Generate!",command = (lambda: generate(sizes,canvas)))
    B1.grid(row=1,column=0)
    B2=Button(root, text ="Sort!",command = (lambda: sorter.bubblesort(sizes.numbers, canvas, root)))
    B2.grid(row=1,column=1)

    
    draw(sizes,canvas)
    

    app = start_window(root)
    root.mainloop()

  


