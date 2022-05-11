from optparse import Values
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import os

def openFolder():
    dir_path = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    rootEnt.delete(0,None)
    rootEnt.insert(0,dir_path)
    
    
root = Tk()
root.title("Easy Download") #창 이름
root.geometry("540x380+100+100") #창 크기
root.resizable(0,0) #창 크기 조절 비활성

searchEnt = Entry(root,width=53) #검색 엔트리
searchlabel=Label(root,text='검색',width=5,height=3) #검색 라벨
enginelabel=Label(root,text='검색 엔진',width=8,height=3) #검색 엔진 라벨
rootlabel=Label(root,text='다운로드 경로',width=10,height=3) #다운로드 경로 라벨
numlabel=Label(root,text='다운로드 개수',width=10,height=3) #다운로드 개수 라벨

values=['Google', 'Naver'] #검색 엔진 종류
engine = ttk.Combobox(root, values=values,state='readonly',width=50,height=3) #검색엔진 콤보박스

rootBtn = Button(root,text='경로 지정',width=10,height=1,command=openFolder) #경로 지정 버튼
rootEnt = Entry(root,width=40) #경로 출력 엔트리

downNum=[10, 20, 30, 40, 50] #다운로드 개수 종류
downNumCom = ttk.Combobox(root, height=3, values=downNum,state='readonly',width=50) #다운로드 개수 콤보박스

openBtn = Button(root,text='경로 열기',width=20,height=1) #경로열기 버튼
downBtn = Button(root,text='다운로드',width=20,height=1) #다운로드 버튼

searchlabel.place(x=30,y=63) #검색 라벨 위치
enginelabel.place(x=20,y=115)
rootlabel.place(x=13,y=163)
numlabel.place(x=13,y=214)
searchEnt.place(x=100,y=80) #검색 엔트리 위치
engine.place(x=100,y=130) #검색 엔진 콤보박스 위치
rootEnt.place(x=100,y=180) #경로 출력 엔트리 위치
rootBtn.place(x=395,y=177) #경로 출력 설정 버튼 위치
downNumCom.place(x=100,y=230) #다운로드 개수 지정 콤보박스 위치
openBtn.place(x=75,y=330) #경로열기 버튼 위치
downBtn.place(x=315,y=330) #다운로드 버튼 위치

root.mainloop()