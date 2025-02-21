import tkinter as tk
from tkinter import messagebox
from tkinter import Listbox, Entry
from datetime import date
import os
import json

# 保存数据
def save_data():
    name = name_box.get("1.0", "end-1c").strip()
    date = str(date_box.get("1.0", "end-1c").strip())
    class_time = get_class_time()
    performance = performance_box.get("1.0", "end-1c").strip()
    last_homework = last_homework_box.get("1.0", "end-1c").strip()
    class_point = class_point_box.get("1.0", "end-1c").strip()
    class_content = class_content_box.get("1.0", "end-1c").strip()
    nextclass_point = nextclass_point_box.get("1.0", "end-1c").strip()
    homework = homework_box.get("1.0", "end-1c").strip()

    # 数据库里没有的新学生
    new_data =[
        [
            {
                "name":name
            },
            [
                {
                    "time":date,
                    "class_time":class_time,
                    "performance":performance,
                    "last_homework":last_homework,
                    "class_point":class_point,
                    "class_content":class_content,
                    "nextclass_point":nextclass_point,
                    "homework":homework
                }
            ]
        ]
    ]

    # 数据库已有新学生
    old_data ={
        # "name":name,
        "time":date,
        "class_time":class_time,
        "performance":performance,
        "last_homework":last_homework,
        "class_point":class_point,
        "class_content":class_content,
        "nextclass_point":nextclass_point,
        "homework":homework
    }
    # 数据库存在该同学，添加到该同学的数据中
    with open(data_path,'r+',encoding='utf-8') as file:
        data = json.load(file)
        for i in data:
            js_name = i[0]['name']
            if js_name == name:
                i_data = i[1]
                for ii in i_data:
                    ii_date = ii['time']
                    if ii_date == date:
                        ii["class_time"] = class_time
                        ii["performance"] = performance
                        ii['last_homework'] = last_homework
                        ii['class_point'] = class_point
                        ii["class_content"] = class_content
                        ii["nextclass_point"] = nextclass_point
                        ii["homework"] = homework
                        file.seek(0)
                        file.truncate()
                        json.dump(data, file, ensure_ascii=False, indent=4)
                        messagebox.showinfo("成功", "反馈已修改！")
                    else:
                        pass
                date_list = []
                for ii in i_data:
                    date_list.append(ii['time'])
                if date in date_list:
                    pass
                else:
                    i[1].append(old_data)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, ensure_ascii=False, indent=4)
                    messagebox.showinfo("成功", "反馈已保存！")
            else:
                pass
    # 数据库没有该同学，创建新的数据
    with open(data_path,'r+',encoding='utf-8') as file:
        data = json.load(file)
        name_list = []
        for i in data:
            name_list.append(i[0]['name'])
        if name not in name_list:
            if name == '':
                messagebox.showinfo("错误", "请输入名字！")
            else:
                data.extend(new_data)
                file.seek(0)
                file.truncate()
                json.dump(data, file, ensure_ascii=False, indent=4)
                messagebox.showinfo("成功", "反馈已保存！")
        else:
            pass

# 搜索最近一次的学生反馈    
def search_data():
    name = name_box.get("1.0", "end-1c").strip()
    with open(data_path,'r+',encoding='utf-8') as file:
        data = json.load(file)
        for i in data:
            js_name = i[0]['name']
            if js_name == name:
                clear_data()
                s_date = i[1][-1]['time']
                s_class_time = i[1][-1]['class_time']
                s_performance = i[1][-1]['performance']
                s_last_homework = i[1][-1]['last_homework']
                s_class_point = i[1][-1]['class_point']
                s_class_content = i[1][-1]['class_content']
                s_nextclass_point = i[1][-1]['nextclass_point']
                s_homework = i[1][-1]['homework']
                name_box.insert(tk.END,js_name)
                date_box.insert(tk.END,s_date)
                radio_var.set(s_class_time)
                performance_box.insert(tk.END,s_performance)
                last_homework_box.insert(tk.END,s_last_homework)
                class_point_box.insert(tk.END,s_class_point)
                class_content_box.insert(tk.END,s_class_content)
                nextclass_point_box.insert(tk.END,s_nextclass_point)
                homework_box.insert(tk.END,s_homework)
            else:
                pass

# 同时搜索名字和日期对应的反馈
def search_name_date_data():
    name = name_box.get("1.0", "end-1c").strip()
    date = str(date_box.get("1.0", "end-1c").strip())
    with open(data_path,'r+',encoding='utf-8') as file:
        data = json.load(file)
        for i in data:
            js_name = i[0]['name']
            if js_name == name:
                i_data = i[1]
                # print(i_data)
                date_list = []
                for ii in i_data:
                    ii_date = ii['time']
                    date_list.append(ii_date)
                    # print(ii_date)
                    if ii_date == date:
                        clear_data()
                        s_date = ii['time']
                        s_class_time = ii['class_time']
                        s_performance = ii['performance']
                        s_last_homework = ii['last_homework']
                        s_class_point = ii['class_point']
                        s_class_content = ii['class_content']
                        s_nextclass_point = ii['nextclass_point']
                        s_homework = ii['homework']

                        radio_var.set(s_class_time)
                        name_box.insert(tk.END,js_name)
                        date_box.insert(tk.END,s_date)
                        performance_box.insert(tk.END,s_performance)
                        last_homework_box.insert(tk.END,s_last_homework)
                        class_point_box.insert(tk.END,s_class_point)
                        class_content_box.insert(tk.END,s_class_content)
                        nextclass_point_box.insert(tk.END,s_nextclass_point)
                        homework_box.insert(tk.END,s_homework)
                    else:
                        pass
                if date not in date_list:
                    radio_var.set("0")
                    performance_box.delete("1.0", tk.END)
                    last_homework_box.delete("1.0", tk.END)
                    class_point_box.delete("1.0", tk.END)
                    class_content_box.delete("1.0", tk.END)
                    nextclass_point_box.delete("1.0", tk.END)
                    homework_box.delete("1.0", tk.END)
                else:
                    pass
            else:
                pass
    return

# 搜索往日的所有日期的反馈
def search_all_date():
    history_box.delete(0, tk.END)
    name = name_box.get("1.0", "end-1c").strip()
    with open(data_path,'r+',encoding='utf-8') as file:
        data = json.load(file)
        for i in data:
            js_name = i[0]['name']
            
            if js_name == name:
                history_box.delete(0, tk.END)
                ii = i[1]
                date_list = []
                for ii_date in ii:
                    history_box.insert(tk.END, ii_date['time'])
            else:
                pass
    return

# 绑定列表框项目点击事件
def on_item_select(event):
    widget = event.widget
    selection = widget.curselection()
    if selection:
        date = widget.get(selection[0])
        name = name_box.get("1.0", "end-1c").strip()
        with open(data_path,'r+',encoding='utf-8') as file:
            data = json.load(file)
            for i in data:
                js_name = i[0]['name']
                if js_name == name:
                    i_data = i[1]
                    # print(i_data)
                    date_list = []
                    for ii in i_data:
                        ii_date = ii['time']
                        date_list.append(ii_date)
                        # print(ii_date)
                        if ii_date == date:
                            # clear_data()
                            date_box.delete("1.0", tk.END)
                            radio_var.set("0")
                            performance_box.delete("1.0", tk.END)
                            last_homework_box.delete("1.0", tk.END)
                            class_point_box.delete("1.0", tk.END)
                            class_content_box.delete("1.0", tk.END)
                            nextclass_point_box.delete("1.0", tk.END)
                            homework_box.delete("1.0", tk.END)

                            s_date = ii['time']
                            s_class_time = ii['class_time']
                            s_performance = ii['performance']
                            s_last_homework = ii['last_homework']
                            s_class_point = ii['class_point']
                            s_class_content = ii['class_content']
                            s_nextclass_point = ii['nextclass_point']
                            s_homework = ii['homework']

                            radio_var.set(s_class_time)
                            # name_box.insert(tk.END,js_name)
                            date_box.insert(tk.END,s_date)
                            performance_box.insert(tk.END,s_performance)
                            last_homework_box.insert(tk.END,s_last_homework)
                            class_point_box.insert(tk.END,s_class_point)
                            class_content_box.insert(tk.END,s_class_content)
                            nextclass_point_box.insert(tk.END,s_nextclass_point)
                            homework_box.insert(tk.END,s_homework)
                        else:
                            pass
                        # search_all_date()



# 复制当前的显示的学生反馈，并把反馈格式化为能够粘贴发送的内容
def copy_data():
    name = name_box.get("1.0", "end-1c").strip()
    date = str(date_box.get("1.0", "end-1c").strip())
    performance = performance_box.get("1.0", "end-1c").strip()
    last_homework = last_homework_box.get("1.0", "end-1c").strip()
    class_point = class_point_box.get("1.0", "end-1c").strip()
    class_content = class_content_box.get("1.0", "end-1c").strip()
    nextclass_point = nextclass_point_box.get("1.0", "end-1c").strip()
    homework = homework_box.get("1.0", "end-1c").strip()
    text = str(name) + "家长您好，以下是孩子本节课的课堂反馈：" + "\n" + "【上课日期】：" + "\n" + \
        str(date) + "\n" + "【课堂状态】："+ "\n" + str(performance) + "\n" +"【作业完成情况】" + "\n" + \
        str(last_homework) +"\n" + "【课堂内容】：" + "\n" + str(class_point) + "\n" + "【掌握情况】" + \
        "\n" + str(class_content) + "\n" + "【下节课内容】：" + "\n" + str(nextclass_point) + \
        "\n" + "【课后作业】：" + "\n" + str(homework)
    r = tk.Tk()
    r.withdraw()  # 隐藏主窗口
    text_to_copy = text
    r.clipboard_clear()  # 清空剪贴板
    r.clipboard_append(text_to_copy)  # 添加新的内容到剪贴板
    r.update()  # 确保更新，使内容真正添加到剪贴板
    r.destroy()  # 销毁Tk对象
    messagebox.showinfo("成功", "反馈已复制到剪切板！")
    return

# 清楚当前的所有信息
def clear_data():
    name_box.delete("1.0", tk.END)
    date_box.delete("1.0", tk.END)
    radio_var.set("0")
    performance_box.delete("1.0", tk.END)
    last_homework_box.delete("1.0", tk.END)
    class_point_box.delete("1.0", tk.END)
    class_content_box.delete("1.0", tk.END)
    nextclass_point_box.delete("1.0", tk.END)
    homework_box.delete("1.0", tk.END)
    history_box.delete(0, tk.END)

# 获取今天日期
def get_date():
    now_date = date.today()
    date_box.delete("1.0", tk.END)
    date_box.insert(tk.END,now_date)
    # return now_date

# 获取当前的课段
def get_class_time():
    c_time = radio_var.get()
    return c_time

# 生成范例反馈
def example_text():
    class_content_box.delete("1.0", tk.END)
    class_content_box.insert(tk.END,ExampleText)
    return

# 数据管理和检测
file_name = 'Data.json'
now_path = os.getcwd()
folder_path_name = "数据"
folder_path = os.path.join(now_path,folder_path_name)
data_path = os.path.join(folder_path,file_name)

if not os.path.exists(data_path):
    os.makedirs(folder_path)
    # print("没有找到数据文件夹，已创建")
else:
    # print("数据文件夹正常")
    pass
if not os.path.exists(data_path):
    with open(data_path,'w') as file:
        json.dump([],file)
        # print("没有找到反馈数据，已创建新数据")
else:
    # print("数据正常")
    pass

ExampleText = '''孩子上节课作业：完成的很好，部分完成，没有完成。\n本节课的新讲的知识点有【】。其中【】比较重要，\
是我们本节课学习的重点。孩子对于这个知识点目前：基本掌握，比较熟练，还不太熟悉。\
针对这个情况我们接下来的解决办法是【】。孩子目前整个知识体系的掌握是【】。孩子在学习中遇到的问题有【】对于这个情况，\
接下来打算通过【】来解决。我们下节课学习的内容是【】。本周的作业是【】。
'''

# 创建主窗口
root = tk.Tk()
root.title("课堂反馈\u03B1-2.0版")
root.iconbitmap("icon.ico")
root.geometry("900x650")  # 设置窗口大小
root.configure(bg='#e3fdfd')

# 创建1号子窗口，里面放置基础界面
frame_1 = tk.Frame(root)
frame_1.configure(bg='#e3fdfd')
frame_1.grid(row=1,column=1)

# 创建1-1号窗口，里面放置时间段单选框界面
frame1_1 = tk.Frame(frame_1)
frame1_1.configure(bg='#e3fdfd')
frame1_1.grid(row=3, column=1)

frame_2 = tk.Frame()
frame_2.configure(bg='#ffd460')
frame_2.grid(row=1,column=2)


# frame_1内的组件
# 定义一个StringVar变量用于存储单选按钮的状态
radio_var = tk.StringVar()

# 设置默认选中的单选按钮
radio_var.set('0')  # 默认不选中

# 创建单选按钮
radiobtn1 = tk.Radiobutton(frame1_1, text="1段", variable=radio_var, value="1", command=get_class_time)
radiobtn1.configure(bg='#e3fdfd')
radiobtn2 = tk.Radiobutton(frame1_1, text="2段", variable=radio_var, value="2", command=get_class_time)
radiobtn2.configure(bg='#e3fdfd')
radiobtn3 = tk.Radiobutton(frame1_1, text="3段", variable=radio_var, value="3", command=get_class_time)
radiobtn3.configure(bg='#e3fdfd')
radiobtn4 = tk.Radiobutton(frame1_1, text="4段", variable=radio_var, value="4", command=get_class_time)
radiobtn4.configure(bg='#e3fdfd')
radiobtn5 = tk.Radiobutton(frame1_1, text="5段", variable=radio_var, value="5", command=get_class_time)
radiobtn5.configure(bg='#e3fdfd')
radiobtn6 = tk.Radiobutton(frame1_1, text="6段", variable=radio_var, value="6", command=get_class_time)
radiobtn6.configure(bg='#e3fdfd')

# 将单选按钮放置到窗口中
radiobtn1.grid(row=0,column=0,padx=5,pady=5)
radiobtn2.grid(row=0,column=1,padx=5,pady=5)
radiobtn3.grid(row=0,column=2,padx=5,pady=5)
radiobtn4.grid(row=0,column=3,padx=5,pady=5)
radiobtn5.grid(row=0,column=4,padx=5,pady=5)
radiobtn6.grid(row=0,column=5,padx=5,pady=5)

# 创建标签
label = tk.Label(root, text="课堂反馈", font=("黑体", 15,"bold"),fg='#2b2e4a')
label.configure(bg='#e3fdfd')
label.grid(row=0,column=1,padx=5,pady=5)

# 创建标签和文本框
name_label = tk.Label(frame_1,text='姓名', font=("黑体", 10))
name_label.grid(row=1,column=0,padx=5,pady=5)
name_box = tk.Text(frame_1,height=2, width=50,wrap=tk.WORD, font=("微软雅黑", 12))
name_box.grid(row=1,column=1,padx=5,pady=5)

# 创建标签和文本框
date_label = tk.Label(frame_1,text='日期', font=("黑体", 10))
date_label.grid(row=2,column=0,padx=5,pady=5)
date_box = tk.Text(frame_1,height=2, width=50,wrap=tk.WORD, font=("微软雅黑", 12))
date_box.grid(row=2,column=1,padx=5,pady=5)

# 创建标签和文本框
performance_label = tk.Label(frame_1,text='课堂表现', font=("黑体", 10))
performance_label.grid(row=4,column=0,padx=5,pady=5)
performance_box = tk.Text(frame_1,height=2, width=50,wrap=tk.WORD, font=("微软雅黑", 12))
performance_box.grid(row=4,column=1,padx=5,pady=5)

# 创建标签和文本框
last_homework_label = tk.Label(frame_1,text='上节课作业', font=("黑体", 10))
last_homework_label.grid(row=5,column=0,padx=5,pady=5)
last_homework_box = tk.Text(frame_1,height=2, width=50,wrap=tk.WORD, font=("微软雅黑", 12))
last_homework_box.grid(row=5,column=1,padx=5,pady=5)

# 创建标签和文本框
class_point_label = tk.Label(frame_1,text='课堂内容', font=("黑体", 10))
class_point_label.grid(row=6,column=0,padx=5,pady=5)
class_point_box = tk.Text(frame_1,height=2, width=50,wrap=tk.WORD, font=("微软雅黑", 12))
class_point_box.grid(row=6,column=1,padx=5,pady=5)

# 创建标签和文本框
class_content_label = tk.Label(frame_1,text='掌握情况', font=("黑体", 10))
class_content_label.grid(row=7,column=0,padx=5,pady=5)
class_content_box = tk.Text(frame_1, height=6, width=50, wrap=tk.WORD, font=("微软雅黑", 12))
class_content_box.grid(row=7,column=1, padx=5,pady=5)

# 创建标签和文本框
nextclass_point_label = tk.Label(frame_1,text='下节课内容', font=("黑体", 10))
nextclass_point_label.grid(row=8,column=0,padx=5,pady=5)
nextclass_point_box = tk.Text(frame_1,height=2, width=50,wrap=tk.WORD, font=("微软雅黑", 12))
nextclass_point_box.grid(row=8,column=1,padx=5,pady=5)

# 创建标签和文本框
homework_label = tk.Label(frame_1,text='课后作业', font=("黑体", 10))
homework_label.grid(row=9,column=0,padx=5,pady=5)
homework_box = tk.Text(frame_1,height=2, width=50,wrap=tk.WORD, font=("微软雅黑", 12))
homework_box.grid(row=9,column=1,padx=5,pady=5)

# 创建按钮
save_button = tk.Button(frame_1, text="保存", command=save_data)
save_button.grid(row=10,column=1,padx=5,pady=5)

# 创建按钮
clear_button = tk.Button(frame_1, text="清除", command=clear_data)
clear_button.grid(row=10,column=2,padx=5,pady=5)

# 创建按钮
copy_button = tk.Button(frame_1, text="复制", command=copy_data)
copy_button.grid(row=10,column=3,padx=5,pady=5)

# 创建按钮
search_button = tk.Button(frame_1, text="搜索最近", command=search_data)
search_button.grid(row=1,column=2,padx=5,pady=5)

# 创建按钮
search_name_date_button = tk.Button(frame_1, text="搜索当日", command=search_name_date_data)
search_name_date_button.grid(row=1,column=3,padx=5,pady=5)

# 创建按钮
date_button = tk.Button(frame_1, text="当日时间", command=get_date)
date_button.grid(row=2,column=2,padx=5,pady=5)

# 创建按钮
date_button = tk.Button(frame_1, text="搜索往日", command=search_all_date)
date_button.grid(row=2,column=3,padx=5,pady=5)

# 创建按钮
example_text_button = tk.Button(frame_1, text="生成范例", command=example_text)
example_text_button.grid(row=7,column=2, padx=5,pady=5)

# frame_2内的组件
history_label = tk.Label(frame_2,text='往日反馈', font=("黑体", 12))
history_label.grid(row=0,column=0,padx=5,pady=5)

# 历史列表
history_box = Listbox(frame_2, height=23, width=20, font=("微软雅黑", 12))
history_box.grid(row=1,column=0,padx=5,pady=5)

history_box.bind('<<ListboxSelect>>', on_item_select)

# 运行主循环
root.mainloop()