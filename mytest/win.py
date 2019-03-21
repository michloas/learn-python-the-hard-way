#!/usr/bin/python
# -*- coding: UTF-8 -*-


from tkinter import *;

# 初始化一个窗体对象
window = Tk();

# 窗体内容
label = Label(window, text="This is the first python");
label.pack();

# 窗体输入
var = StringVar();
entry = Entry(window, textvariable=var);
entry.pack();


# 点击的方法；当点击按钮时，显示输入的值
def click():
    print(var.get());


# 按钮
button = Button(window, text="click", command=click);
button.pack();

# 窗体显示

window.mainloop();
