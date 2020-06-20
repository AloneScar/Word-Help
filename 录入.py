import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os
import time



master_global = None

class Write:
    def __init__(self):
        self.root = tk.Tk()
        self.word_dict = {}
        self.word_dict.setdefault('English',{})
        self.word_dict.setdefault('Chinese',{})
        self.label1_text = tk.StringVar()
        self.button1_text = tk.StringVar()
        self.openfigure = 1
        self.quitfigure = 1
        if not os.path.exists(r'./file'):
            os.mkdir(r'./file')
        if not os.path.exists(r'./file/English.txt'):
            with open(r'./file/English.txt', 'w') as file1:
                pass
        if not os.path.exists(r'./file/Chinese.txt'):
            with open(r'./file/Chinese.txt', 'w') as file1:
                pass
        self.readTxt()
        print(self.word_dict)

    def quit(self):
        self.root.quit()


    def readTxt(self):
        with open(r'./file/English.txt', 'r') as file1:
            for word in file1.readlines():
                if word == "\n":
                    break
                else:
                    word = word.strip()
                if "unit" in word or "标题:" in word or len(word.split('-')) == 3:
                    if "标题:" in word:
                        word = word.replace('标题:', "")
                    unit = word
                    continue
                self.word_dict['English'].setdefault(unit,[]).append(word)

        with open(r'./file/Chinese.txt', 'r') as file1:
            for word in file1.readlines():
                if word == "\n":
                    break
                else:
                    word = word.strip()
                if "unit" in word or "标题:" in word or len(word.split('-')) == 3:
                    if "标题:" in word:
                        word = word.replace('标题:', "")
                    unit = word
                    continue
                self.word_dict['Chinese'].setdefault(unit,[]).append(word)

    def deleteGroupButton(self):
        if len(self.word_dict['English'].keys()) != 0:
                if tkinter.messagebox.askokcancel('危险操作','删除找不回的哟，\n真的很久的！'):
                    try:
                        deleleGroupName = self.cmb.get()
                        del self.word_dict['English'][deleleGroupName]
                        del self.word_dict['Chinese'][deleleGroupName]
                        self.cmb['value'] = tuple(self.word_dict['English'].keys())
                        if len(self.word_dict['English'].keys()) != 0:
                            self.cmb.current(0)
                        else:
                            self.cmb['value'] = ('暂无词组',)
                            self.cmb.current(0)
                    except:
                        pass
        else:
            self.cmb['value'] = ('暂无词组',)
            self.cmb.current(0)
            tkinter.messagebox.askokcancel('错误', '词库为空')

    def deleteCancelButton(self):
        self.label1_text.set('请选择您要操作的词组')
        self.button2.place_forget()
        self.button3.place_forget()
        self.button1.place(x=100, y=100)

    def deleteGroup(self):
        try:
            self.button1.place_forget()
        except:
            pass
        try:
            self.entry1.place_forget()
        except:
            pass
        try:
            self.button4.place_forget()
        except:
            pass
        try:
            self.button5.place_forget()
        except:
            pass
        self.cmb.place(x=70, y=30)
        self.button2 = tk.Button(self.root, text='删除', width=8, command=self.deleteGroupButton)
        self.button2.place(x=70, y=100)
        self.button3 = tk.Button(self.root, text='取消', width=8, command=self.deleteCancelButton)
        self.button3.place(x=160, y=100)
        self.label1_text.set('请选择要删除的词组')

    def deleteAll(self):
        if tkinter.messagebox.askokcancel('危险操作', '将永久删除哦！\n真的很久的！'):
            self.word_dict['English'].clear()
            self.word_dict['Chinese'].clear()
            self.cmb['value'] = ('暂无词组',)
            self.cmb.current(0)

    def saveWords(self):
        if len(self.word_dict['English']) != 0:
            saveList = []
            saveUnit = list(self.word_dict['English'].keys())
            with open('./file/English.txt', 'w') as file2:
                for unit in saveUnit:
                    if "unit" not in unit and len(unit.split('-')) != 3:
                        file2.write('标题:'+unit)
                        file2.write('\n')
                    else:
                        file2.write(unit)
                        file2.write('\n')
                    for word in self.word_dict['English'][unit]:
                        file2.write(word)
                        file2.write('\n')
            with open('./file/Chinese.txt', 'w') as file3:
                for unit in saveUnit:
                    if "unit" not in unit and len(unit.split('-')) != 3:
                        file3.write('标题:'+unit)
                        file3.write('\n')
                    else:
                        file3.write(unit)
                        file3.write('\n')
                    for word in self.word_dict['Chinese'][unit]:
                        file3.write(word)
                        file3.write('\n')

    def addGroup(self):
        self.entry1_text = tk.StringVar()
        try:
            self.cmb.place_forget()
            self.button1.place_forget()
            self.button2.place_forget()
            self.button3.place_forget()
        except:
            pass
        self.label1_text.set('请输入要添加的词组名称')
        self.button4 = tk.Button(self.root, text='添加', width=8, command=self.addGroupButton)
        self.button4.place(x=70, y=100)
        self.button5 = tk.Button(self.root, text='返回', width=8, command=self.addCancelButton)
        self.button5.place(x=160, y=100)
        self.entry1 = tk.Entry(self.root, textvariable=self.entry1_text)
        self.entry1.place(x=80, y=30)
        self.entry1.configure(state="normal")
        self.entry1_text.set('')

    def addWild(self):
        self.addGroup()
        today_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        self.entry1_text.set(today_time)
        self.label1_text.set('每天记录亿点点')
        self.entry1['text'] = today_time
        self.entry1.configure(state="readonly")
    def addGroupButton(self):
        addword = self.entry1.get()
        if addword not in self.word_dict['English'].keys():
            self.word_dict['English'].setdefault(addword,[]).append('暂无英文')
            self.word_dict['Chinese'].setdefault(addword,[]).append('暂无中文')
            self.entry1.delete(0, tk.END)
            self.label1_text.set('添加成功')
            self.cmb['value'] = tuple(self.word_dict['English'].keys())
        else:
            tkinter.messagebox.showwarning(title='注意', message='该词组已经存在！')

    def addCancelButton(self):
        self.button4.place_forget()
        self.button5.place_forget()
        self.entry1.place_forget()
        self.cmb.place(x=70, y=30)
        self.button1.place(x=100, y=100)
        self.label1_text.set('请选择您要操作的词组')

    def help(self):
        tkinter.messagebox.showinfo('帮助','还未开发')

    def openadd(self):
        self.root.withdraw()
        add = Add(self.root)
        if self.openfigure == 1:
            add.run()
            self.openfigure = 0
        else:
            master_global.update()
            master_global.deiconify()
            master_global.mainloop()

    def run(self):
        self.root.title('录入单词')
        self.root.geometry('300x150')
        self.root.resizable(0, 0)
        m1 = tk.Menu(self.root)
        m2 = tk.Menu(m1, tearoff=False)
        m3 = tk.Menu(m1, tearoff=False)
        m1.add_cascade(label="添加", menu=m3)
        m3.add_command(label="一组单词", command=self.addGroup)
        m3.add_command(label="野生单词", command=self.addWild)
        m1.add_cascade(label="删除", menu=m2)
        m2.add_command(label="清空所有", command=self.deleteAll)
        m2.add_command(label="一组单词", command=self.deleteGroup)
        m2.add_command(label="单个单词", command=lambda: self.label1_text.set('请进入词组再进行删除哦!'))
        m1.add_command(label="保存", command=self.saveWords)
        m1.add_command(label="帮助", command=self.help)
        self.root.config(menu=m1)
        self.cmb = ttk.Combobox(self.root)
        self.cmb.place(x=70, y=30)
        self.cmb['value'] = tuple(self.word_dict['English'].keys())
        self.cmb.configure(state="readonly")
        try:
            self.cmb.current(0)
        except:
            pass
        # self.root.protocol("WM_DELETE_WINDOW", self.quit)
        label1 = tk.Label(self.root, textvariable=self.label1_text, fg='red').place(x=82, y=65)
        self.label1_text.set('请选择您要操作的词组')
        self.button1 = tk.Button(self.root, textvariable=self.button1_text, width=10, command=self.openadd)
        self.button1.place(x=100, y=100)
        self.button1_text.set('进入')
        self.root.mainloop()


class Add:
    def __init__(self, root):
        self.root = root

    def quit_past(self):
        self.master.withdraw()
        self.root.update()
        self.root.deiconify()
        self.root.mainloop()

    def run(self):
        self.master = tk.Tk()
        global master_global
        master_global = self.master
        self.master.title('录入单词')
        self.master.geometry('500x300')
        m1 = tk.Menu(self.master)
        m1.add_command(label="搜索")
        m1.add_command(label="删除")
        m1.add_command(label="返回上一级", command=self.quit_past)
        self.master.config(menu=m1)
        self.master.protocol("WM_DELETE_WINDOW", self.quit_past)
        self.master.resizable(0,0)
        Text1 = tk.Text(self.master, width=10, height=4, state='disabled')
        Text2 = tk.Text(self.master, width=10, height=4, state='disabled')
        Text3 = tk.Text(self.master, width=10, height=4, state='disabled')
        Text4 = tk.Text(self.master, width=10, height=4, state='disabled')
        Text1.place(x=50, y=40)
        Text3.place(x=360, y=40)
        Text2.place(x=50, y=200)
        Text4.place(x=360, y=200)
        Text5 = tk.Text(self.master, width=10, height=4)
        Text6 = tk.Text(self.master, width=10, height=4)
        Text5.place(x=200, y=40)
        Text6.place(x=200, y=200)
        # button1 = tk.Button(self.master, text='返回', command=self.fd)
        # button1.pack()

if __name__ == '__main__':
    write = Write()
    write.run()