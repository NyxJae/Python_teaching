# 为课堂项目成品

# 站在前人的肩膀上,不重复造轮子
# 大神们已经写好了一些工具库

# 下面是两个可以操作文件的工具库
import os
import shutil

# 不同种类文件都有相应的后缀名来标志它的种类

# 以后缀名来规定如何分类文件
zhengLiGuiZe = {
    "音频": [".mp3"],
    "视频": [".mp4"],
    "图片": [".png", ".jpg"],
    "文档": [".txt", ".pdf", ".docx"],
    "程序": [".exe"],
    "压缩包": [".zip"],
}

# 定位到要整理的文件夹 体验课/演示文件夹
os.chdir(r"体验课/演示文件夹")

# 按照定好的规则,一个一个来建立文件夹
for wenJianZhongLei, houZhuis in zhengLiGuiZe.items():
    # 如果已经有同名的文件夹,就不要建立

    # 如果没有,才建立
    if not os.path.isdir(wenJianZhongLei):
        os.mkdir(wenJianZhongLei)

# 一个一个来整理文件
for wenJian in os.listdir():
    # 记下当前文件的后缀名
    houZhui = os.path.splitext(wenJian)[-1].lower()
    # 将文件的后缀与我们定义的整理规则挨个对比
    for wenJianZhongLei, houZhuis in zhengLiGuiZe.items():
        # 看看这个文件属于那个种类
        if houZhui in houZhuis:
            # 将其放到对应的文件夹中
            shutil.move(wenJian, "{0}/{1}".format(wenJianZhongLei, wenJian))


print("整理完成")
