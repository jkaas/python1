# 循环代码优化测试
import time

start = time.time()
for i in range(1000):
    result = []
    for m in range(10000):
        result.append(i*1000 + m*100)

end = time.time()
print("耗时：{0}".format((end-start)))

start2 = time.time()
for i in range(1000):
    result = []
    c = i * 1000
    for m in range(10000):
        result.append(c + m * 100)

end2 = time.time()
print("耗时：{0}".format((end2-start2)))

