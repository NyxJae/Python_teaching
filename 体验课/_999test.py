# 站在前人的肩膀上,不重复造轮子
# 大神们已经写好了一些工具库

# 下面是两个可以操作文件的工具库
import os
import shutil

# 不同种类文件都有相应的后缀名来标志它的种类

# 以后缀名来规定如何分类文件
formats = {
    "音频": [".mp3"],
    "视频": [".mp4"],
    "图片": [".png", ".jpg"],
    "文档": [".txt", ".pdf", ".docx"],
    "程序": [".exe"],
    "压缩包": [".zip"],
}

# 定位到要整理的文件夹
os.chdir(r"体验课/演示文件夹")


for wenJian in os.listdir():
    ext = os.path.splitext(wenJian)[-1].lower()

    for d, exts in formats.items():
        if not os.path.isdir(d):
            os.mkdir(d)
        if ext in exts:
            shutil.move(wenJian, "{0}/{1}".format(d, wenJian))

print("整理完成")
