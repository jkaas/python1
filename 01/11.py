empNum = 0
salarySum = 0
salary = []

while True:
    x = input("请输入员工的薪资（输入Q或q结束）")

    if x.upper() == "Q":
        print("录入完毕，结束程序")
        break
    if float(x) < 0:
        continue
    empNum += 1
    salary.append(float(x))
    salarySum += float(x)

print("员工数{0}".format(empNum))
print("录入薪资", salary)
print("平均薪资{0}".format(salarySum/empNum))
