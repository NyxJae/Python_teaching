import imp
import os
import shutil

# 不同种类文件都有其后缀名
# 以后缀名来分类文件
formats = {
    "音频": [".mp3"],
    "视频": [".mp4"],
    "图片": [".png", ".jpg"],
    "文档": [".txt", ".pdf", ".docx"],
    "程序": [".exe"],
    "压缩包": [".zip"],

}

os.chdir(r"/Volumes/HHD/文档/教学/Python_teaching/体验课/演示文件夹")

for f in os.listdir():
    ext = os.path.splitext(f)[-1].lower()

    for d, exts in formats.items():
        if not os.path.isdir(d):
            os.mkdir(d)
        if ext in exts:
            shutil.move(f, "{0}/{1}".format(d, f))

print("整理完成")
