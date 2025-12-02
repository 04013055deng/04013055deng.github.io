import random as r
import time
import tkinter as t
from tkinter import messagebox as m #导入所需库
root=t.Tk()
root.withdraw() #隐藏主仓库
while True:
    x=["张三","李四","王五","赵六","吴七"] #创建名单元组
    a=r.choice(x) #抽取名单里的人
    # print(a) #打印中奖人
    m.showinfo('中奖信息',"中奖的是："+a) #弹窗提示
    time.sleep(0.5) #休眠0.5ms



