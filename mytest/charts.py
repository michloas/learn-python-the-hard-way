import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=600, height=480, bg='white')

canvas.create_text(302, 77,  # 使用crest_text绘制文字
                   text='use canvas',
                   fill='grey')  # 文字颜色为灰色

canvas.create_text(300, 75,
                   text='use canvas',
                   fill='blue')

canvas.create_polygon(290, 114, 316, 114, 330, 130, 310, 146, 284, 146, 270, 130)  # 调用绘制六边形的方法

canvas.create_oval(280, 120, 320, 140,  # 调用绘制椭圆的方法
                   fill='white')

canvas.create_line(250, 130, 350, 130)  # 绘制直线

canvas.create_line(300, 100, 300, 160)

canvas.create_rectangle(90, 190, 510, 410, width=5)  # 绘制矩形

canvas.create_arc(100, 200, 500, 400,  # 绘制圆弧
                  start=0, extent=240,  # 设置圆弧起止角度
                  fill="pink")  # 设置填充色为粉红色

canvas.create_arc(103, 203, 500, 400,
                  start=241, extent=118,
                  fill='red')
canvas.pack()  # 将Canvas添加到主窗口
root.mainloop()
