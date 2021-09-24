#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time     :
# @Author   : Spike713
# @Site     :
# @File     : apk_download.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:
# @Licence  :

from flask import Flask, render_template, send_from_directory
import os, socket, qrcode, time, json

app = Flask(__name__)

"""
使用方法：
1、配置apk路径、端口（folder）
2、运行app.py
3、打开浏览器 localhost:7777
"""

file = "/Users/Administrator/Desktop/apk下载"
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
    name = 'jqdj_1.0.49_55_s.apk.png'
    img.save(name)


def get_file():
    file_list = ""
    for i in os.listdir(file):
        file_path = file + "/" + i
        create_time = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(file))))
        file_size = str(float("%.3f" % (os.path.getsize(file_path) / 1000000))) + "MB"
        file_list = file_list + i + "=" + create_time + "=" + file_size + ","
        get_qrcod(i, port)
    return file_list[:-1]


@app.route("/")
def index():
    return render_template("index.html", apks=(get_file()))


@app.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    return send_from_directory(file, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True, threaded=True)