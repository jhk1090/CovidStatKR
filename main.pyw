from urllib import request
from bs4 import BeautifulSoup
from tkinter import *
import ctypes
import time

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("코로나 확진자 현황")
root.geometry("480x360")
url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11'
target = request.urlopen(url)
soup = BeautifulSoup(target, "html.parser")
now = time.strftime("%Y. %m. %d")
root.resizable(False, False)

def refresh():
    global target, soup, now
    target = request.urlopen(url)
    soup = BeautifulSoup(target, "html.parser")
    now = time.strftime("%Y. %m. %d")
    result_.config(text="+ [옵션 선택]")
    result.config(text="누적: ")
    result1.config(text="전일대비: ")
    refreshTime.config(text="기준: " + now)

def start(option: str):
    stack = soup.find_all(class_="ca_value")
    inner = soup.find_all(class_="inner_value")

    if option == "확진환자":
        result_.config(text="+ 확진환자")
        result.config(text="누적: " + stack[0].text.strip())
        result1.config(text="전일대비: " + inner[0].text.strip())
    elif option == "격리해제":
        result_.config(text="+ 격리해제")
        result.config(text="누적: " + stack[2].text.strip())
        result1.config(text="전일대비: " + stack[3].text.strip())
    elif option == "격리중":
        result_.config(text="+ 격리중")
        result.config(text="누적: " + stack[4].text.strip())
        result1.config(text="전일대비: " + stack[5].text.strip())
    else:
        result_.config(text="+ 사망")
        result.config(text="누적: " + stack[6].text.strip())
        result1.config(text="전일대비: " + stack[7].text.strip())

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

option = Button(frame_option, padx=5, pady=5, text="확진환자", command=lambda: start("확진환자"))
option.grid(row=0, column=0, padx=5, pady=5)

option1 = Button(frame_option, padx=5, pady=5, text="격리해제", command=lambda: start("격리해제"))
option1.grid(row=0, column=1, padx=5, pady=5)

option2 = Button(frame_option, padx=5, pady=5, text="격리중", command=lambda: start("격리중"))
option2.grid(row=0, column=2, padx=5, pady=5)

option3 = Button(frame_option, padx=5, pady=5, text="사망", command=lambda: start("사망"))
option3.grid(row=0, column=3, padx=5, pady=5)

# 결과 프레임
frame_result = LabelFrame(root, text="결과")
frame_result.pack(padx=5, pady=5, ipady=5)

result_ = Label(frame_result, text="+ [옵션 선택]", width=35, anchor=W)
result_.grid(row=0, column=0, sticky=W)

result = Label(frame_result, text="누적: -", width=35, anchor=W)
result.grid(row=1, column=0, sticky=W)

result1 = Label(frame_result, text="전일대비: -", width=35, anchor=W)
result1.grid(row=2, column=0, sticky=W)

refreshTime = Label(frame_result, text="기준: " + now, width=35, anchor=E)
refreshTime.grid(row=3, column=0, sticky=E)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="새로고침", width=12, command=refresh)
btn_start.pack(side="right", padx=5, pady=5)

root.mainloop()
