import os, time


# def cpu_time():
#     f = os.popen("adb shell cat /proc/stat")
#     data = f.readlines()
#     f.close()
#     time_list = map(lambda x: int(x), data[0].split(" ")[2:-1])
#     return sum(time_list)
#
#
# def thread_time():
#     z = os.popen("adb shell cat /proc/3626/stat")
#     data = z.readlines()[0].split(" ")
#     z.close()
#     processCPUtime = sum(map(lambda x: int(x), [data[13], data[14], data[15], data[16]]))
#     return processCPUtime
#
#
#
#
# cpu_usage = 100*(thread_time()-thread_time())/(cpu_time()-cpu_time())
#
#
# print cpu_usage


f = os.popen("adb shell cat /proc/stat")
data = f.readlines()
f.close()
# print data
count = 0
for i in data:
    if "cpu" in i:
        count += 1
        print i
    else:
        count -= 1
        break
