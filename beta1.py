import tkinter
import threading
import sqlite3 as sql
import random
import time
import numpy as np
from tkinter import *
import tkinter.messagebox as tm
i,g,count,beg_row,beg_col,m=0,0,0,0,0,0
original_letters=[]
score_word=[]
score_made,actual_score=0,0
prev_beg_color,prev_end_color="gray79","gray79"
words=[]

#////////////////////////////////////////////// receiving data from database
conn=sql.connect('word_list.db')
c=conn.cursor()
c.execute("SELECT * FROM fruits")
rows = c.fetchall()
for p in rows:
    for q in p:
        words.append(q)
conn.close()

#/////////////////////////////////////// start arange words
def arange_words():
    mb=main.butons
    global original_letters,words,actual_score
    for x in range(len(mb)):
        original_letters.append('.')
         
    #///////////////////////////////// assigining words
    temp_word=[]
    x=0
    while x<7:
        overlap=0
        w=random.choice(words)
        if w not in temp_word:
            word_len=len(w)
            req_len=10-word_len+1
            dir=random.choice('123')
            #print(dir,w)
            
            #//////////////////////////
            if dir=='1':   #horizontal
                col=random.choice(range(0,req_len))
                row=random.choice(range(0,10))
                #print(row,col,w)
                column=col
                for i in range(word_len):
                    if not(original_letters[row*10+column]=='.' or original_letters[row*10+column]==w[i]):
                        overlap=1
                        break
                    column+=1
                    
                if overlap==0:
                    for i in range(word_len):
                        mb[row*10+col].a.set(w[i])
                        original_letters[row*10+col]=w[i]
                        col+=1
                else:
                    continue
                    
            #///////////////////////////////
            
            if dir=='2':   #Vertical
                row=random.choice(range(0,req_len))
                col=random.choice(range(0,10))
                #print(row,col,w)
                rows=row
                for i in range(word_len):
                    if not(original_letters[rows*10+col]=='.' or original_letters[rows*10+col]==w[i]):
                        overlap=1
                        break
                    rows+=1
                    
                if overlap==0:
                    for i in range(word_len):
                        mb[row*10+col].a.set(w[i])
                        original_letters[row*10+col]=w[i]
                        row+=1
                else:
                    continue
            #///////////////////////////////
            
             #//////////////////////////
            if dir=='3':   #diagonal
                col=random.choice(range(0,req_len))
                row=random.choice(range(0,req_len))
                #print(row,col,w)
                column=col
                rows=row
                for i in range(word_len):
                    if not(original_letters[rows*10+column]=='.' or original_letters[rows*10+column]==w[i]):
                        overlap=1
                        break
                    column+=1
                    rows+=1
                    
                if overlap==0:
                    for i in range(word_len):
                        mb[row*10+col].a.set(w[i])
                        original_letters[row*10+col]=w[i]
                        col+=1
                        row+=1
                else:
                    continue
                    
            #///////////////////////////////
            temp_word.append(w)
            actual_score+=word_len
            x+=1
        
        
    #/////////////////////////////////end assigining words
    
    
            
#////////////////////////////////////// end arange words

#///////////////////////////////////// start check word
def Check_Word(buton,beg_row,beg_col,end_row,end_col):
    global count,words,score_word
    word=""
    mb=main.butons
    color=['#fff999000','#fff888000','#fff777000','#fff666000','#fff555000','#fff444000','#fff333000']
    b=count%7
    bg_color=color[b]
    if beg_row==end_row:
        for x in range(beg_col,end_col+1):
            o=mb[beg_row*10+x].a.get()
            word+=o
        if (word in words) and (word not in score_word):
            for x in range(beg_col,end_col+1):
                buton[beg_row][x].configure(bg=bg_color,fg="black")
            
    elif beg_col==end_col:
        for x in range(beg_row,end_row+1):
            o=mb[x*10+beg_col].a.get()
            word+=o 
        if (word in words) and (word not in score_word):
            for x in range(beg_row,end_row+1):
                buton[x][beg_col].configure(bg=bg_color,fg="black")
            
    elif ((end_row-beg_row)==(end_col-beg_col)):
        y=beg_row
        for x in range(beg_col,end_col+1):
            o=mb[y*10+x].a.get()
            word+=o
            y+=1
            
        y=beg_row
        if (word in words) and (word not in score_word):   
            for x in range(beg_col,end_col+1):
                buton[y][x].configure(bg=bg_color,fg="black")
                y+=1
            
    if word!="":     
        return word    
#/////////////////////////////////////// end Check_Word
#///////////////////////////////// Start possiblebtn
def possiblebtn(buton,row,col):   
    for x in range(10):
        for y in range(10):
            if original_letters[x*10+y]=='.....':
                buton[x][y].configure(bg="gray79",fg="black")
    
    if i%2==0:
        #fgcolor="white"
        buton[row][col].configure(bg="red")
    
#////////////////////////////////////////////// end possiblebtn
                 
    #//////////////////////////////////////   label start
reset_val,exit_val=0,0        
def reset():
    global reset_val
    main.root.destroy()
    reset_val=1
    
def end():
    global exit_val
    main.root.destroy()
    exit_val=1
    
def timer(n):
    tm=n
    t=StringVar()
    while n!=0:
        n=n-1
        time.sleep(1)#time.sleep(seconds) #here you can mention seconds according to your requirement.
        print ("00 : ",tm-n)
        label=Label(display.labelframe,textvariable=t,padx=45,height=1,width=21,relief="raised",borderwidth=1,bg="chocolate1",fg="black",font=("arial bold ",25))
        label.place(x=0,y=550)
        t.set(tm-n)


txt=''        
r,grn,b='fff','999','000'
fnl_color='#fff999000'
def display(): 
    global fnl_color
    display.labelframe=Frame(main.root,bg="black",relief="raised",borderwidth=15,height=750,width=520)
    display.labelframe.place(x=1000,y=10)
    Title_label=Label(display.labelframe,text="SCORE BOARD",padx=71,relief="raised",borderwidth=1,bg="coral2",fg="black",font=("Times bold ",35))
    Title_label.place(x=0,y=0)
    
    label1=Label(display.labelframe,text="Total_Score",padx=45,height=1,width=21,relief="raised",borderwidth=1,bg="chocolate1",fg="black",font=("arial bold ",25))
    label1.place(x=0,y=60)
    
    c=IntVar()
    label2=Label(display.labelframe,textvariable=c,padx=21,relief="raised",borderwidth=1,bg="tan1",fg="black",font=("arial bold ",25))
    c.set(actual_score)
    label2.place(x=396,y=60)
    
    label3=Label(display.labelframe,text="Score_Gained",padx=45,height=1,width=21,relief="raised",borderwidth=1,bg="chocolate1",fg="black",font=("arial bold ",25))
    label3.place(x=0,y=411)
    
    d=IntVar()
    label4=Label(display.labelframe,textvariable=d,padx=20,relief="raised",borderwidth=1,height=1,width=2,bg=fnl_color,fg="black",font=("arial bold ",25))
    d.set(score_made)
    label4.place(x=396,y=411)
    #display.labelframe=Frame(root,bg="tomato",relief="raised",height=420,width=200,borderwidth=15)
    #display.labelframe.place(x=1000,y=105)    
    
    v,c=0,103
    r,g,b='fff','999','000'
    val=[IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()]
    index=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
    e1=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
    for x in range(7):
        label=Label(display.labelframe,text='',padx=6,height=1,width=25,relief="raised",bg="khaki2",fg="black",font=("arial bold ",25))
        label.place(x=0,y=c)
        color='#'+r+g+b
        #r,g,b=str((int(r)+10)),str((int(g)+50)),str((int(b)+100))
        g=str((int(g)-100))
        label=Label(display.labelframe,textvariable=val[v],padx=19,height=1,width=2,relief="raised",bg=color,fg="white",font=("arial bold ",25))
        label.place(x=396,y=c)
        label=Label(display.labelframe,textvariable=index[v],height=1,width=2,relief="raised",bg=color,fg="white",font=("arial bold ",25))
        label.place(x=0,y=c)
        label=Label(display.labelframe,textvariable=e1[v],padx=6,height=1,width=17,relief="raised",bg=color,fg="black",font=("arial bold ",25))
        label.place(x=50,y=c)
        if v<len(score_word):
            a=score_word[v]
        else:
            a=''   
        e1[v].set(a)
        if len(a)==0:
            t=''
        else:
            t=len(a)
        val[v].set(t)
        index[v].set(v+1)
        c+=44   
        v+=1
        
    label=Label(display.labelframe,text='',padx=4,pady=14,height=2,width=30,relief="raised",bg="khaki2",fg="black",font=("arial bold ",20))
    label.place(x=0,y=454)    
    reset_buton=Button(display.labelframe,text="Reset",padx=42,height=1,width=7,relief="raised",borderwidth=3,bg="red2",fg="black",font=("arial bold ",25),command=reset) 
    reset_buton.place(x=10,y=466)
    
    exit_buton=Button(display.labelframe,text="Quit",padx=42,height=1,width=7,relief="raised",borderwidth=3,bg="red2",fg="black",font=("arial bold ",25),command=end) 
    exit_buton.place(x=250,y=466)
    
    label=Label(display.labelframe,text='',padx=4,pady=4,height=5,width=30,relief="raised",bg="red",fg="black",font=("arial bold ",20))
    label.place(x=0,y=550)    
    
    display.labelx=Label(display.labelframe,text=txt,padx=30,height=4,width=21,relief="raised",borderwidth=1,bg="chocolate1",fg="black",font=("arial bold ",25))
    display.labelx.place(x=14,y=557)
    #//////////////////////////////////////////end  
#////////////////////////////////////////////start swap
def select(l,but,bg_color):
    global actual_score,score_made
    
    mb=main.butons
    global prev_beg_color,prev_end_color,score_word
    
    butonlist=[]
    for x in range(len(mb)):
        l=mb[x].b
        butonlist.append(l)
        
    letterlist=[]
    for x in range(len(mb)):
        l=mb[x].a.get()
        letterlist.append(l)
    
    letter=np.asarray(letterlist)
    letter=letter.reshape(10,10)
    # print(letter)

    global g,beg_row,beg_col
    
    buton=np.asarray(butonlist)
    buton=buton.reshape(10,10)
    
   ##############################################################    start
    global i,m
    #prev_beg_color,prev_end_color="gray79","gray79"
    for row in range(10):
        for col in range(10):
            if(str(but)==str(buton[row][col])):
                if i%2==0:
                    beg_row=row
                    beg_col=col
                    possiblebtn(buton,row,col)
                    i+=1
                    prev_beg_color=bg_color
                    #print("prev_beg ",prev_beg_color)
                    
                else:
                    end_row=row
                    end_col=col
                    i+=1
                    prev_end_color=bg_color
                    #print("prev_end ",prev_end_color)
                    
                    buton[row][col].configure(bg="limegreen",fg="black")
                    x=Check_Word(buton,beg_row,beg_col,end_row,end_col)
                    
                    #//////////////////////////////////////////////////// Check_Database
                    global words,count
                    if x in words and x not in score_word:
                        m=x
                        count+=1
                        print(x)
                        score_word.append(x)
                        score_made+=len(x)
                        global r,grn,b,fnl_color
                        if int(grn)<100:
                            grn='999'
                        fnl_color='#'+r+grn+b
                        grn=str((int(grn)-100))
                    
                    else:
                        buton[row][col].configure(bg=prev_end_color,fg="black")
                        buton[beg_row][beg_col].configure(bg=prev_beg_color,fg="black")
    display()                        
                    
                    #/////////////////////////////////////////////////// close Database
                         
                        
    ###########################################################################    end        
class button:
    def __init__(self,row,col):
        self.a=StringVar()
        self.b=Button(main.frame,textvariable=self.a,command=self.fun,bg='gray79',fg='black',font=("arial bold ",15),width=2,height=1)
        self.a.set(random.choice(' '))
        #abcdefghijklmnopqrstuvwxyz
        self.b.grid(row=row,column=col,ipadx=30,ipady=15,padx=1,pady=1)
            
    def fun(self):
        l=self.a.get()
        but=self.b
        bg_color=but['bg']
        #print('fun',a)
        select(l,but,bg_color)
        
now,tym,cnt=0,0,0
def update_clock():
    global now,tym,cnt,txt
    #now = time.strftime("%H:%M:%S")
    now = time.strftime("%S")
    now=int(now)%30
    now=(now-tym)
    if now<0:
        now=30+now
    if now==29 and cnt==0:  
        cnt=1
        score=score_made
    if cnt==1:
        txt='Time Over:\n'+str(score_made)+' Points'
        display.labelx.configure(text=txt)
    elif score_made==actual_score:
        txt='Congratulations\nTime:'+str(now)+' Sec'
        display.labelx.configure(text=txt)
    else:
        now=30-now
        txt='Time Remaining:\n'+str(now)+' Sec'
        display.labelx.configure(text=txt)
        display.labelframe.after(10, update_clock)
        
def main():
    global tym
    main.root=Tk()
    main.root.title("Word_Puzzle")
    main.root.geometry('2000x2000')
    main.butons=[]
    main.frame=Frame(main.root,bg="magenta3",relief="raised",borderwidth=15)
    main.frame.place(x=10,y=10)
    for i in range(1,11):
        for j in range(1,11):
            b=button(i,j)
            main.butons.append(b)        
    arange_words()
    display()
    tym=int(time.strftime("%S"))%30 
    t1=threading.Thread(target=update_clock)
    t1.start()
    main.root.mainloop()