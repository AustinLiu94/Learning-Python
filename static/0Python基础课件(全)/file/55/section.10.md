## 综合应用-学生管理系统\(文件版\)

```python
import time
import os

# 定一个列表，用来存储所有的学生信息(每个学生是一个字典)
info_list = []


def print_menu():
    print("---------------------------")
    print("      学生管理系统 V1.0")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:保存数据")
    print(" 7:退出系统")
    print("---------------------------")


def add_new_info():
    """添加学生信息"""

    new_name = input("请输入姓名:")
    new_tel = input("请输入手机号:")
    new_qq = input("请输入QQ:")

    for temp_info in info_list:
        if temp_info['name'] == new_name:
            print("此用户名已经被占用,请重新输入")
            return  # 如果一个函数只有return就相当于让函数结束，没有返回值

    # 定义一个字典，用来存储用户的学生信息(这是一个字典)
    info = {}

    # 向字典中添加数据
    info["name"] = new_name
    info["tel"] = new_tel
    info["qq"] = new_qq

    # 向列表中添加这个字典
    info_list.append(info)


def del_info():
    """删除学生信息"""

    del_num = int(input("请输入要删除的序号:"))
    if 0 <= del_num < len(info_list):
        del_flag = input("你确定要删除么?yes or no")
        if del_flag == "yes":
            del info_list[del_num]
    else:
        print("输入序号有误,请重新输入")


def modify_info():
    """修改学生信息"""

    modify_num = int(input("请输入要修改的序号:"))
    if 0 <= modify_num < len(info_list):
        print("你要修改的信息是:")
        print("name:%s, tel:%s, QQ:%s" % (info_list[modify_num]['name'],
            info_list[modify_num]['tel'],info_list[modify_num]['qq']))
        info_list[modify_num]['name'] = input("请输入新的姓名:")
        info_list[modify_num]['tel'] = input("请输入新的手机号:")
        info_list[modify_num]['qq'] = input("请输入新QQ:")
    else:
        print("输入序号有误,请重新输入")


def search_info():
    """查询学生信息"""
    search_name = input("请输入要查询的学生姓名:")
    for temp_info in info_list:
        if temp_info['name'] == search_name:
            print("查询到的信息如下:")
            print("name:%s, tel:%s, QQ:%s" % (temp_info['name'],
                temp_info['tel'], temp_info['qq']))
            break
    else:
        print("没有您要找的信息....")


def print_all_info():
    """遍历学生信息"""
    print("序号\t姓名\t\t手机号\t\tQQ")
    i = 0
    for temp in info_list:
        # temp是一个字典
        print("%d\t%s\t\t%s\t\t%s" % (i, temp['name'], temp['tel'], temp['qq']))
        i += 1


def save_data():
    """加载之前存储的数据"""
    f = open("info_data.data", "w")
    f.write(str(info_list))
    f.close()


def load_data():
    """加载之前存储的数据"""
    global info_list
    f = open("info_data.data")
    content = f.read()
    info_list = eval(content)
    f.close()

def main():
    """用来控制整个流程"""

    # 加载数据（1次即可）
    load_data()

    while True:
        # 1. 打印功能
        print_menu()

        # 2. 获取用户的选择
        num = input("请输入要进行的操作(数字):")

        # 3. 根据用户选择,做相应的事情
        if num == "1":
            # 添加学生
            add_new_info()
        elif num == "2":
            # 删除学生
            del_info()
        elif num == "3":
            # 修改学生
            modify_info()
        elif num == "4":
            # 查询学生
            search_info()
        elif num == "5":
            # 遍历所有的信息
            print_all_info()
        elif num == "6":
            # 保存数据到文件中
            save_data()
        elif num == "7":
            # 退出系统
            exit_flag = input("亲,你确定要退出么?~~~~(>_<)~~~~(yes or no) ")
            if exit_flag == "yes":
                break
        else:
            print("输入有误,请重新输入......")


        input("\n\n\n按回车键继续....")
        os.system("clear")  # 调用Linux命令clear完成清屏

# 程序的开始
main()
```

### 注意：

* 以上程序，在运行之前请先建立info\_data.data文件，并且写入一对中括号\[\]即可
* 等到后面讲解完`异常`之后就解决了这个问题



