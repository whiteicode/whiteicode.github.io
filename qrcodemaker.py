from ttkbootstrap import *
from MyQR import myqr
def main():
    global root
    global entry1
    global entry2
    global entry3
    root=Window()
    root.title('二维码生成器')
    root.geometry('250x220')
    Label(root,text='内容').pack()
    entry1=StringVar()
    Entry(root,textvariable=entry1).pack()
    Label(root,text='保存文件名').pack()
    entry2=StringVar()
    Entry(root,textvariable=entry2).pack()
    Label(root,text='保存文件路径(留空为桌面)').pack()
    entry3=StringVar()
    entry=Entry(root,textvariable=entry3).pack()
    Button(root,text='开始生成！',command=make_qr).pack()
def make_qr():
    if entry3.get()=='':
        myqr.run(words=entry1.get(),version=9,save_name=entry2.get()+'.png',save_dir='C:/Users/Administrator/Desktop')
    else:
        myqr.run(words=entry1.get(),version=9,save_name=entry2.get()+'.png',save_dir=entry3.get())
if __name__=='__main__':
    main()
    root.mainloop()
