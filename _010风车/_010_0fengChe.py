import turtle as t

# 设置背景颜色
t.bgcolor("lightBlue")

# region 绘制风车支架
t.color("gray")
t.pensize(20)
# 转向下
t.right(90)
t.forward(150)
t.backward(150)
# endregion

# region 绘制4个粉色半圆扇叶
t.color("black")
t.pensize(1)
t.fillcolor("pink")
t.begin_fill()
# 循环4次画4个扇叶
for i in range(4):
    # 直边
    t.forward(100)
    # 转向定圆弧方向
    t.left(90)
    # 半圆弧,半径为
    t.circle(100, 180)
t.end_fill()
# endregion

# 连接点
t.dot(20)
t.hideturtle()

t.done()
