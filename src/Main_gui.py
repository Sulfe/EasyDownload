from optparse import Values
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import os
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
    optionPhoto = [searchEnt.get(),engine.get(),driverEnt.get(),rootEnt.get(),downNumCom.get()]
    crolling.googleColling(optionPhoto)
    #testLabel.configure(text=optionPhoto)
    
def openPath():
    path = os.path.realpath(rootEnt.get())
    os.startfile(path)
    
root = Tk()
root.title("Easy Download") #창 이름
root.geometry("540x380+100+100") #창 크기 540
root.resizable(0,0) #창 크기 조절 비활성

searchEnt = Entry(root,width=53) #검색 엔트리
searchlabel=Label(root,text='검색',width=5,height=3) #검색 라벨

rootlabel=Label(root,text='다운로드 경로',width=10,height=3) #다운로드 경로 라벨
numlabel=Label(root,text='다운로드 개수',width=10,height=3) #다운로드 개수 라벨

enginelabel=Label(root,text='검색 엔진',width=8,height=3) #검색 엔진 라벨
values=['Google', 'Naver'] #검색 엔진 종류
engine = ttk.Combobox(root, values=values,state='readonly',width=50,height=3) #검색엔진 콤보박스

rootBtn = Button(root,text='경로 지정',width=10,height=1,command=openFolder) #경로 지정 버튼
rootEnt = Entry(root,width=40) #경로 출력 엔트리

downNum=[10, 20, 30, 40, 50] #다운로드 개수 종류
downNumCom = ttk.Combobox(root, height=3, values=downNum,state='readonly',width=50) #다운로드 개수 콤보박스

driverlabel=Label(root,text='드라이버 지정',width=10,height=3) #드라이버 지정 라벨
driverBtn = Button(root,text='찾아보기',width=10,height=1,command=openFile) #드라이버 버튼
driverEnt = Entry(root,width=40) #드라이버 엔트리

openBtn = Button(root,text='경로 열기',width=20,height=1,command=openPath) #경로열기 버튼
downBtn = Button(root,text='다운로드',width=20,height=1,command=downAct) #다운로드 버튼

#test출력 라벨 optionPhoto 확인용
#testLabel = Label(root,text=' ', width=80, height=1)
#testLabel.place(x=20,y=280)

searchlabel.place(x=30,y=14) #검색 라벨 위치
enginelabel.place(x=20,y=65) #엔진 선택 라벨 위치
rootlabel.place(x=13,y=163) #다운로드 경로 라벨 위치
numlabel.place(x=13,y=214) #다운로드 개수 라벨 위치
searchEnt.place(x=100,y=30) #검색 엔트리 위치
engine.place(x=100,y=80) #검색 엔진 콤보박스 위치
rootEnt.place(x=100,y=180) #경로 출력 엔트리 위치
rootBtn.place(x=395,y=177) #경로 출력 설정 버튼 위치
downNumCom.place(x=100,y=230) #다운로드 개수 지정 콤보박스 위치
openBtn.place(x=75,y=330) #경로열기 버튼 위치
downBtn.place(x=315,y=330) #다운로드 버튼 위치
driverlabel.place(x=13,y=114) #드라이버 지정 라벨 위치
driverBtn.place(x=395,y=125) #드라이버 지정 버튼 위치
driverEnt.place(x=100,y=130) #드라이버 지정 엔트리 위치







root.mainloop()