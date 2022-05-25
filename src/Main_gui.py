#-*- coding:utf-8 -*-

from faulthandler import disable
from optparse import Values
import threading
import time
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.ttk as ttk
import os
from matplotlib.pyplot import text
import crolling

def openFolder():
    dir_path = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    rootEnt.delete(0,None)
    rootEnt.insert(0,dir_path)
    
def openFile():
    dir_file = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
    ('exe files', '*.exe'),('all files', '*.*')))
    driverEnt.delete(0,None)
    driverEnt.insert(0,dir_file)
    
def downAct():
    if len(searchEnt.get()) == 0 or len(engine.get()) == 0 or len(driverEnt.get()) == 0 or len(rootEnt.get()) == 0 or len(downNumCom.get()) == 0:
        messagebox.showerror('오류',"입력하지 않은 항목이 있습니다.")
    else :
        optionPhoto = [searchEnt.get(),engine.get(),driverEnt.get(),rootEnt.get(),downNumCom.get()]
        th = threading.Thread(target=crolling.action, args=(optionPhoto[0],optionPhoto[1],optionPhoto[2],optionPhoto[3],optionPhoto[4]))
        th.start()
        th.join()
        messagebox.showinfo('작업 완료','다운로드 완료')

    
def openPath():
    path = os.path.realpath(rootEnt.get())
    os.startfile(path)
    
def newWin():
    howUse='본 프로그램을 사용하기 위해 크롬과 크롬드라이버를 다운로드 해주세요.\n1. 검색어를 입력합니다.\n2. 검색 엔진을 선택합니다.\n3. 다운로드한 크롬 드라이버 파일을 선택합니다.\n4. 이미지를 다운로드할 경로를 선택합니다.\n5. 다운로드 할 이미지의 개수를 선택합니다.\n6. 다운로드 버튼을 클릭 후 완료창이 뜰때까지 기다려주세요'
    newWindow = Toplevel(root)
    newWindow.resizable(0,0)
    newLabel=Label(newWindow,text=howUse)
    newLabel.pack()
    
def testWin():
    output=[searchEnt.get(),engine.get(),driverEnt.get(),rootEnt.get(),downNumCom.get()]
    newWindow = Toplevel(root)
    Label1=Label(newWindow,text=output[0])
    Label2=Label(newWindow,text=output[1])
    Label3=Label(newWindow,text=output[2])
    Label4=Label(newWindow,text=output[3])
    Label5=Label(newWindow,text=output[4])
    Label1.pack()
    Label2.pack()
    Label3.pack()
    Label4.pack()
    Label5.pack()



root = Tk()
root.title("Easy Download") #창 이름
root.geometry("540x380+100+100") #창 크기 540
root.resizable(0,0) #창 크기 조절 비활성


menubar = Menu(root)#매뉴바 생성
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label='사용법',command=newWin)
fileMenu.add_command(label='테스트',command=testWin)
menubar.add_cascade(label='메뉴', menu=fileMenu)

searchEnt = Entry(root,width=53) #검색 엔트리
searchlabel=Label(root,text='검색',width=5,height=3) #검색 라벨

rootlabel=Label(root,text='다운로드 경로',width=10,height=3) #다운로드 경로 라벨
numlabel=Label(root,text='다운로드 개수',width=10,height=3) #다운로드 개수 라벨

enginelabel=Label(root,text='검색 엔진',width=8,height=3) #검색 엔진 라벨
values=['Google', 'Naver'] #검색 엔진 종류
engine = ttk.Combobox(root, values=values,state='readonly',width=50,height=3) #검색엔진 콤보박스

rootBtn = Button(root,text='경로 지정',width=10,height=1,command=openFolder) #경로 지정 버튼
rootEnt = Entry(root,width=40) #경로 출력 엔트리

downNum=[2,5,10, 20, 30, 40, 50] #다운로드 개수 종류
downNumCom = ttk.Combobox(root, height=3, values=downNum,state='readonly',width=50) #다운로드 개수 콤보박스

driverlabel=Label(root,text='드라이버 지정',width=10,height=3) #드라이버 지정 라벨
driverBtn = Button(root,text='찾아보기',width=10,height=1,command=openFile) #드라이버 버튼
driverEnt = Entry(root,width=40) #드라이버 엔트리

openBtn = Button(root,text='경로 열기',width=20,height=1,command=openPath) #경로열기 버튼
downBtn = Button(root,text='다운로드',width=20,height=1,command=downAct) #다운로드 버튼


#test출력 라벨 optionPhoto 확인용
#testLabel = Label(root,text=' ', width=80, height=1)
#testLabel.place(x=20,y=280)

searchlabel.place(x=41,y=34) #검색 라벨 위치
enginelabel.place(x=31,y=85) #엔진 선택 라벨 위치
rootlabel.place(x=23,y=183) #다운로드 경로 라벨 위치
numlabel.place(x=23,y=234) #다운로드 개수 라벨 위치
searchEnt.place(x=120,y=50) #검색 엔트리 위치
engine.place(x=120,y=100) #검색 엔진 콤보박스 위치
rootEnt.place(x=120,y=200) #경로 출력 엔트리 위치
rootBtn.place(x=415,y=197) #경로 출력 설정 버튼 위치
downNumCom.place(x=120,y=250) #다운로드 개수 지정 콤보박스 위치
openBtn.place(x=75,y=330) #경로열기 버튼 위치
downBtn.place(x=320,y=330) #다운로드 버튼 위치
driverlabel.place(x=23,y=134) #드라이버 지정 라벨 위치
driverBtn.place(x=415,y=145) #드라이버 지정 버튼 위치
driverEnt.place(x=120,y=150) #드라이버 지정 엔트리 위치


root.config(menu=menubar)
root.mainloop()