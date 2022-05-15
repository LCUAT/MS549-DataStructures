from timeit import default_timer as timer
import psutil

def printc(text,color="default",r=255, g=255, b=255):
    try:
        if(color == "red"):
            r = 255
            g = 0
            b = 0
        elif(color == "green"):
            r = 0
            g = 255
            b = 0
        elif(color == "blue"):
            r = 0
            g = 0
            b = 255
        elif(color == "yellow"):
            r= 255
            g = 255
            b = 0

        print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text))

    except Exception as e: 

        print("Unable to print: " + e)

def Time(func, text = "Elapsed Time: ", args=None, color="yellow"):
    try:
        start = timer()
        if(args != None):
            funcRes = func(args)
        else:
            funcRes = func()
        end = timer()
        #printc(text + " "+str(end - start)+"s", color)
        print(text + " "+str(end - start)+"s")
        return (funcRes,end - start)
    except Exception as e: 
        printc(e, "red")

def processorInfo(interval):
    #printc("Processor Time over " + str(interval) + "s: " + str(psutil.cpu_percent(interval)))
    print("Processor Time over " + str(interval) + "s: " + str(psutil.cpu_percent(interval)))
    return psutil.cpu_percent(interval)
