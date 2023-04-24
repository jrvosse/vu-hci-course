'''
This file gives an example of how to create a simple GUI for the bachelors of AI course: "Human Computer Interaction"
Comments are more extensive than usual in code to give some more explanation of what the code does.
The following sources were used as a basis for this code:
https://levelup.gitconnected.com/10-interesting-python-tkinter-programs-with-code-df52174993e1
https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/
'''
from tkinter import *
from datetime import datetime
from datetime import date 

# We set some globals and define a function for consistent logging including timestamps
def logaction(logtext):
    #appends a line with logtext to the logfile, adds how long running the experiment it is in minutes and seconds.
    ct=datetime.timestamp(datetime.now())-starttime
    #determine minutes and seconds, another divmod could be used to also include hours
    m, s = divmod(int(ct), 60)
    #stringformating is used to nicely display the timestamps
    timestr = f'{m:02d}:{s:02d}'
    logfile.write(timestr + " " + logtext + "\n")
    
# of user interction
# Getting the current date and time for the logging
startdatetime = datetime.now()
#convert startdate to second so we can calculate with it.
starttime = datetime.timestamp(startdatetime)
#opening the logfile and append to it to indicate a new session.
logfile = open("logging.txt", "a")
logaction("New session started @" + str(startdatetime))




#all functions below are used for specific events.
def setcolor(x):
    displayage.config(bg=x)
    logaction("setcolor: "+x)
    
def setcursor(x):
    right_frame.config(cursor=x)
    logaction("setcursor: "+x)
    
def agecalc():
    #Any errors occuring in the try part, result in the except 
    # clause to be done instead.
    try:
        d=int(ddentry.get())
        m=int(mmentry.get())
        y=int(yyentry.get())
        dob=date(y,m,d)
        age=(date.today()-dob).days//365
        displayage.config(text="your age is: "+str(age))
        logaction("age was calculated")
    except:
        displayage.config(text="you incorrectly entered your dob!")
        logaction("Incorrect input to calculate age")
 
def clear(event):
    #note that event variable is needed as it is passed by default.
    displayage.config(bg='White')
    right_frame.config(cursor='arrow')
    logaction("white")
    

#Now we set up the GUI itself
root  =  Tk()  
root.title("GUI demo")
root.config(bg="skyblue")

# Create left and right frames, note that they are first assigned to a variable so that they can be referenced later
# Note that assigning them sizes would be pointless as the grid manager set their sizes such that their contents fit!
left_frame  =  Frame(root,  bg='grey')
left_frame.grid(row=0,  column=0,  padx=10,  pady=5, sticky="wens")

right_frame  =  Frame(root,  bg='grey')
right_frame.grid(row=0,  column=1,  padx=10,  pady=5, sticky="wens")

# Create frames and labels in left_frame
Label(left_frame,  text="Some controls",  relief=SUNKEN).grid(row=0,  column=0,  padx=5,  pady=5)

tool_bar  =  Frame(left_frame,  width=380,  height=185,  bg='grey')
tool_bar.grid(row=2,  column=0,  padx=5,  pady=5)

Label(tool_bar,  text="Colors",  relief=SUNKEN).grid(row=0,  column=0,  padx=5,  pady=3,  ipadx=10)
Label(tool_bar,  text="Cursors",  relief=SUNKEN).grid(row=0,  column=1,  padx=5,  pady=3,  ipadx=10)

# The use of lambda might be new to you. What it does in this case is that it ensures us we can pass
# an argument (even including a variable if we want!) to the function we call
Button(tool_bar,  text="red",  command=lambda:setcolor("Red")).grid(row=1,  column=0,  padx=5,  pady=5,  sticky='wens')
Button(tool_bar,  text="yellow",  command=lambda:setcolor("Yellow")).grid(row=2,  column=0,  padx=5,  pady=5,  sticky='wens')
Button(tool_bar,  text="spider",  command=lambda:setcursor("spider")).grid(row=1,  column=1,  padx=5,  pady=5,  sticky='wens')
Button(tool_bar,  text="clock",  command=lambda:setcursor("clock")).grid(row=2,  column=1,  padx=5,  pady=5,  sticky='wens')

#Note that we did not assign the buttons to variables as we do not need to use them again
#Many of the widgets below on the other hand we do need again!
Label(right_frame, text="Enter your birthday").grid(row=0, column=0, columnspan=3, sticky="wens")
#manually setting the size of widgets can be important as default sizes might be too large or
#changes during runtime might cause the laylout to change (This can happen in this app!)
entrywidth=5
#seperate entry fields for the date of birth
ddentry = Entry(right_frame, width=entrywidth)
ddentry.grid(row=1, column=0, padx=5, pady=5)
mmentry = Entry(right_frame,width=entrywidth)
mmentry.grid(row=1, column=1, padx=5, pady=5)
yyentry = Entry(right_frame, width=entrywidth)
yyentry.grid(row=1, column=2, padx=5, pady=5)
#We want to have a default value in these fields as instruction
#Generally if you don't know how to do something, google can help
#e.g. "tkinter Entry set value"
ddentry.insert(-1,'dd')
mmentry.insert(-1,'mm')
yyentry.insert(-1,'yyyy')
Button(right_frame, text="calculate age", command=agecalc).grid(row=2,column=1,columnspan=2,padx=5, pady=5)
displayage=Label(right_frame, text="This will show your age")
displayage.grid(row=3, column=0, columnspan=3, sticky="wens")
clearing=Label(right_frame, text="Hover to clear", padx=5, pady=5, relief=RAISED)
clearing.grid(row=4, column=0, columnspan=3, sticky="wens")
clearing.config(bg="Green")
#showing the use of a different kind of event
clearing.bind('<Enter>', clear)
root.mainloop()
