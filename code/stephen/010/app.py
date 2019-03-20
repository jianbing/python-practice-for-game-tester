#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 19-3-18 下午7:50
# @Author   : StephenZ
# @Site     :
# @File     : 1.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:   (c) zhangjian 2019
# @Licence  :     <@2019>
from flask import Flask, render_template, send_from_directory
import os, socket, qrcode, time, json

app = Flask(__name__)

"""
使用方法：
1、配置apk路径、端口（folder）
2、运行app.py
3、打开浏览器 localhost:7777
"""
# folder = "/home/zhang/snap/nextcloud-client/10/Nextcloud/slots-package/android/test"
folder = "/home/zhang/snap/nextcloud-client/10/Nextcloud/ArcheryElite/程序包/测试用"
port = 7777


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def get_qrcod(file, port):
    img = qrcode.make("http://" + get_host_ip() + ":%s/download/" % port + file)
    img.get_image()
    img.save("static/" + file + ".png")


def get_file():
    file_list = ""
    for i in os.listdir(folder):
        file_path = folder + "/" + i
        create_time = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(folder))))
        file_size = str(float("%.3f" % (os.path.getsize(file_path) / 1000000))) + "MB"
        # file_info["name"], file_info["time"], file_info["size"] = i, create_time, str(file_size) + "MB"
        file_list = file_list + i + "=" + create_time + "=" + file_size + ","
        get_qrcod(i, port)
    return file_list[:-1]


@app.route("/")
def index():
    # print(get_file())
    return render_template("index.html", apks=(get_file()))
    # return send_from_directory(dictionary, filename, as_attachment=True)


@app.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    dictionary = "/home/zhang/snap/nextcloud-client/10/Nextcloud/slots-package/android/test"
    return send_from_directory(dictionary, filename, as_attachment=True)


if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0", port=port, debug=True, threaded=True)
