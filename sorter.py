import time
 
def draw(numbers, canvas,index):
    canvas.delete("all")
    for j in range(0,len(numbers)):
        if j==index or j-1==index:
            canvas.create_rectangle(2+(j*8), 300-250*(numbers[j]/float(100)), 8+(j*8), 300, fill="green")
        else:
            canvas.create_rectangle(2+(j*8), 300-250*(numbers[j]/float(100)), 8+(j*8), 300, fill="red")

def bubblesort(numbers, canvas, window):
    print('sort started')
    swapped =True
    

    while(swapped == True):
        swapped = False
        draw(numbers,canvas, 1000)
        for i in range(0,len(numbers)):

            if i<len(numbers)-1:
                if numbers[i]>numbers[i+1]:
                    temp = numbers[i]
                    numbers[i]=numbers[i+1]
                    numbers[i+1] = temp
                    canvas.delete("all")
                    draw(numbers, canvas, i)
                    window.update()
                   # time.sleep(0.000000000001)
                    swapped = True
    print('sort complete')

def partition(numbers, start, end):
    i = (start-1)         
    pivot = numbers[end]     
  
    for j in range(start, end):
        if numbers[j] <= pivot:
            i = i+1
            numbers[i], numbers[j] = numbers[j], numbers[i]
  
    numbers[i+1], numbers[end] = numbers[end], numbers[i+1]
    return (i+1)

def quicksort(numbers, start, end, canvas, window):
    if len(numbers) == 1:
        return numbers
    if start < end:
  
        p = partition(numbers, start, end)
  
        quicksort(numbers, start, p-1, canvas, window)
        canvas.delete("all")
        draw(numbers, canvas, p)
        window.update()


        quicksort(numbers, p+1, end, canvas, window)
        canvas.delete("all")
        draw(numbers, canvas, p)
        window.update()
    

