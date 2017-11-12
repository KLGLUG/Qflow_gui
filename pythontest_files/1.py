import Tkinter
import subprocess

top = Tkinter.Tk()

def helloCallBack():
   print "Below is the output from the shell script in terminal"
   subprocess.call('./in.sh', shell=True)


B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
