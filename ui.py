#!/usr/bin/env python
# coding=utf-8
import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter.ttk import Combobox

host = "localhost"
user = "root"
password = "root"
dbname = "system_choose_course"


def update_info(v, e):
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname, )
        cur = db.cursor()
        sql = "UPDATE studentinfo SET {}='{}' WHERE sid='{}'"
        cur.execute(sql.format(v.get(), e.get(), uid))
        db.commit()
        tkinter.messagebox.showinfo("successful", "插入成功")
    except pymysql.Error as e:
        tkinter.messagebox.showinfo("unsuccessful", "插入失败" + str(e))
        db.rollback()
    db.close()


def person_info():
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname,
                             )
        print("数据库连接成功")
        cur = db.cursor()
        sql = "SELECT * FROM studentinfo where sid = '{}'"
        cur.execute(sql.format(uid))
        results = cur.fetchall()
        return results

    except pymysql.Error as e:
        print("数据查询失败" + str(e))
    db.close()


def update_it(win):
    root = Toplevel(win)
    root.title("change_info")
    root.geometry("500x230")
    Label(root, text="{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}".format(
        "学生编号", "专业", "姓名", "学院", "性别", "出生日期")).grid(row=0, column=0, columnspan=2,
                                                      pady=9, sticky="w")
    var = StringVar()
    rels = person_info()
    cb = Combobox(root, textvariable=var, width=17)
    cb["value"] = ("major", "dept", "gender", "birthday")
    i = 1
    for rel in rels:
        s1 = (
            "{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}".format(
                rel[0], rel[1], rel[2], rel[3], rel[4], rel[5]))
        Label(root, text=s1).grid(row=i, column=0, columnspan=2, padx=5, pady=30, sticky="w")
        i = i + 1
    e1 = Entry(root)
    Label(root, text="请选择将要修改的信息").grid(padx=5, row=i, pady=8, column=0, sticky="e")
    cb.grid(padx=5, row=i, column=1, pady=8, sticky="w")
    i = i + 1
    Label(root, text="请输入要修改的值").grid(padx=5, row=i, column=0, sticky="e")
    e1.grid(padx=5, row=i, column=1, sticky="w")
    Button(root, text="提交", command=lambda: update_info(var, e1)).grid(row=i + 1, column=0, columnspan=2)


def insert_course(e):
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname, )
        cur = db.cursor()
        sql = "INSERT INTO sc(sId,cId) VALUES (%s,%s)"
        value = (uid, e.get())
        cur.execute(sql, value)
        db.commit()
        tkinter.messagebox.showinfo("successful", "插入成功")
    except pymysql.Error as e:
        tkinter.messagebox.showinfo("unsuccessful", "插入失败" + str(e))
        db.rollback()
    db.close()


def cour_all():
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname,
                             )
        print("数据库连接成功")
        cur = db.cursor()
        sql = "SELECT courseinfo.*,teacherinfo. tname ,classroom_arr. crId FROM courseinfo,teach, teacherinfo,classroom,classroom_arr WHERE  teach. tId =teacherinfo. tId  AND classroom. crId =classroom_arr. crId  AND classroom_arr. cId =courseinfo. cId  AND teach. cId =courseinfo. cId  ORDER BY courseinfo. cId  "
        cur.execute(sql)
        results = cur.fetchall()
        return results

    except pymysql.Error as e:
        print("数据查询失败" + str(e))
    db.close()


def choose_course(win):
    root = Toplevel(win)
    root.title("choose_course")
    root.geometry("600x500")
    Label(root, text="课程编号   课程名称   课程介绍    课程学时       课程学分      课程星期    老师姓名    班级号").grid(row=0, column=0,
                                                                                            columnspan=2,
                                                                                            padx=5, pady=9)
    rels = cour_all()
    i = 1
    for rel in rels:
        s1 = (
            "{:<14}{:<14}{:<14}{:>14}{:>14}{:>14}{:>14}{:>14}".format(
                rel[0], rel[1], rel[2], rel[3], rel[4], rel[5], rel[6], rel[7]))
        Label(root, text=s1).grid(row=i, column=0, columnspan=2, padx=5, pady=9)
        i = i + 1
    ee = Entry(root)
    Label(root, text="请填入要插入的课程编号").grid(padx=5, row=i, pady=20, column=0, sticky="e")
    ee.grid(padx=5, row=i, column=1, pady=10, sticky="w")
    Button(root, text="提交", command=lambda: insert_course(ee)).grid(row=i + 1, column=0, columnspan=2)


def chaKe():
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname,
                             )
        print("数据库连接成功")
        cur = db.cursor()
        sql = "SELECT studentinfo.sId,studentinfo.name,courseinfo.cName,courseinfo.cId,courseinfo.cIntro,courseinfo.cCredit,courseinfo.cWeek,teacherinfo.tName,classroom.crId FROM studentinfo, sc,courseinfo,teach, teacherinfo,classroom,classroom_arr WHERE studentinfo.sId = sc.sId AND courseinfo.cId=sc.cId AND  teach.tId=teacherinfo.tId AND classroom.crId=classroom_arr.crId AND classroom_arr.cId=courseinfo.cId AND teach.cId=courseinfo.cId AND studentinfo.name = '%s' "
        cur.execute((sql % name))
        results = cur.fetchall()
        return results

    except pymysql.Error as e:
        print("数据查询失败" + str(e))
    db.close()


def stu_course(win):
    root = Toplevel(win)
    root.title("stu_course")
    root.geometry("600x500")
    Label(root, text="学生学号   学生姓名   课程名称    课程id       课程介绍      课程学分    课程星期    老师姓名    班级号").pack(padx=5, pady=14,
                                                                                                    anchor="nw")
    rels = chaKe()
    for rel in rels:
        s1 = (
            "{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}".format(
                rel[0], rel[1], rel[2], rel[3], rel[4], rel[5], rel[6], rel[7], rel[8]))
        Label(root, text=s1).pack(padx=5, pady=14, anchor="nw")


def update_sql(table, pwd1, pwd2):
    if pwd1 == "":
        tkinter.messagebox.showwarning("error", "请不要输入空值")
    elif pwd2 != pwd1:
        tkinter.messagebox.showwarning("error", "上下密码不相等")
    else:
        try:
            db = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=dbname,
                                 )
            cur = db.cursor()
            sql = "UPDATE " + table + " SET pwd= " + pwd1 + " WHERE name= " + "'" + name + "'"
            cur.execute(sql)
            db.commit()
            tkinter.messagebox.showinfo("成功", "修改成功")
        except pymysql.Error as e:
            print(e)
            tkinter.messagebox.showinfo("失败", "修改失败")
            db.rollback()
        db.close()


def change_password(win, table):
    change_pwd = Toplevel(win)
    change_pwd.title("登录")
    change_pwd.geometry("350x200")
    idE = Entry(change_pwd, width=30)
    pwdE = Entry(change_pwd, width=30)
    Label(change_pwd, text="修改密码", font="微软雅黑 14").grid(row=0, column=0, columnspan=2, sticky="w",
                                                        pady=10)
    Label(change_pwd, text="新密码", font="微软雅黑 14").grid(row=1, column=0, sticky="w")
    idE.grid(row=1, column=1, sticky="e", padx=40)
    Label(change_pwd, text="确认密码", font="微软雅黑 14").grid(row=2, column=0, sticky="w")
    pwdE.grid(row=2, column=1, sticky="e", padx=40)
    Button(change_pwd, text="修改", font="微软雅黑 10", relief="solid",
           command=lambda: update_sql(table, pwdE.get(), idE.get())).grid(row=3, column=0,
                                                                          columnspan=2,
                                                                          pady=20,
                                                                          padx=20)


def admin_operate():
    admin_log = Tk()
    admin_log.title("管理员操作台")
    admin_log.geometry("310x310")
    Label(admin_log, text="Hello," + name + "\n请选择您的操作\n"
          , font="微软雅黑 14", justify=LEFT).grid(row=0, column=0, columnspan=2, sticky='w')
    Button(admin_log, text="增加学生", font="微软雅黑 12").grid(row=1, column=0, sticky="w")
    Button(admin_log, text="增加老师", font="微软雅黑 12").grid(row=1, column=1, padx=90)
    Button(admin_log, text="修改老师信息", font="微软雅黑 12").grid(row=2, column=0, sticky="w", pady=10)
    Button(admin_log, text="修改学生信息", font="微软雅黑 12").grid(row=2, column=1, padx=90)
    Button(admin_log, text="给老师加课", font="微软雅黑 12").grid(row=3, column=0, sticky="w")
    Button(admin_log, text="给学生加课", font="微软雅黑 12").grid(row=3, column=1, padx=90)
    Button(admin_log, text="修改成绩", font="微软雅黑 12").grid(row=4, column=0, sticky="w")
    Button(admin_log, text="修改密码", font="微软雅黑 12").grid(row=4, column=1, padx=90, pady=10)
    Button(admin_log, text="增加课程", font="微软雅黑 12").grid(row=5, column=0, sticky="w")


def teacher_operate():
    teacher_log = Tk()
    teacher_log.title("老师操作台")
    teacher_log.geometry("250x220")
    Label(teacher_log, text="Hello," + name + "\n请选择您的操作\n"
          , font="微软雅黑 12", justify=LEFT).grid(row=0, column=0, columnspan=2, sticky="w", pady=10)
    Button(teacher_log, text="修改密码", font="微软雅黑 12", relief="solid",
           command=lambda: change_password(teacher_log, "teacherpwd")).grid(row=1, column=0)
    Button(teacher_log, text="输入成绩", font="微软雅黑 12", relief="solid").grid(row=1, column=1, sticky="e", padx=80)
    Button(teacher_log, text="查看课程信息", font="微软雅黑 12", relief="solid").grid(row=2, column=1)
    Button(teacher_log, text="修改信息", font="微软雅黑 12", relief="solid").grid(row=2, column=0, pady=20)


def stu_operate():
    stu_log = Tk()
    stu_log.title("学生操作台")
    stu_log.geometry("250x220")
    Label(stu_log, text="Hello," + name + "\nchoose your choices\n"
          , font="微软雅黑 12", justify=LEFT).grid(row=0, column=0, columnspan=2, sticky="w", pady=10)
    Button(stu_log, text="修改密码", font="微软雅黑 12", relief="solid",
           command=lambda: change_password(stu_log, "stupwd")).grid(row=1, column=0)
    Button(stu_log, text="选课", font="微软雅黑 12", relief="solid", command=lambda: choose_course(stu_log)).grid(row=1,
                                                                                                            column=1,
                                                                                                            padx=80,
                                                                                                            sticky="e")
    Button(stu_log, text="查课", font="微软雅黑 12", relief="solid", command=lambda: stu_course(stu_log)).grid(row=2,
                                                                                                         column=0,
                                                                                                         pady=20,
                                                                                                         sticky="w")
    Button(stu_log, text="修改信息", font="微软雅黑 12", relief="solid", command=lambda: update_it(stu_log)).grid(row=2,
                                                                                                          column=1)


def check_pwd(s1, s2, DB):
    global name
    global uid
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname,
                             )
        cur = db.cursor()
        sql = "select * from " + DB + " where id= " + s1 + " and " + " pwd= " + s2
        marked = cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            uid = row[0]
            name = row[2]
        return marked
    except pymysql.Error as e:
        print("数据查询失败" + str(e))
    db.close()


def checkInfo(kind, e1, e2, w1):
    Id = e1.get()
    pwd = e2.get()
    if kind == "student login":
        marked = check_pwd(Id, pwd, "stupwd")
        if marked:
            w1.destroy()
            stu_operate()
        else:
            messagebox.showerror("error", "password is not right,please input again")
    elif kind == "teacher login":
        marked = check_pwd(Id, pwd, "teacherpwd")
        if marked:
            w1.destroy()
            teacher_operate()
        else:
            messagebox.showerror("error", "password is not right,please input again")
    else:
        marked = check_pwd(Id, pwd, "adminpwd")
        if marked:
            w1.destroy()
            admin_operate()
        else:
            messagebox.showerror("error", "password is not right,please input again")


def login(str, win):
    win.destroy()
    log_in = Tk()
    log_in.title("登录")
    log_in.geometry("350x200")
    idE = Entry(log_in, width=30)
    pwdE = Entry(log_in, width=30)
    Label(log_in, text=str, font="微软雅黑 14").grid(row=0, column=0, columnspan=2, sticky="w",
                                                 pady=10)
    Label(log_in, text="id", font="微软雅黑 14").grid(row=1, column=0, sticky="w", )
    idE.grid(row=1, column=1, sticky="e", padx=40)
    Label(log_in, text="pwd", font="微软雅黑 14").grid(row=2, column=0, sticky="w")
    pwdE.grid(row=2, column=1, sticky="e", padx=40)
    Button(log_in, text="登录", font="微软雅黑 10", relief="solid",
           command=lambda: checkInfo(kind=str, e1=idE, e2=pwdE, w1=log_in)).grid(row=3, column=0, columnspan=2,
                                                                                 pady=20,
                                                                                 padx=20)


name = ""
uid = ""
master = Tk()
master.title("欢迎")
master.geometry("450x370+500+200")
canvas = Canvas(master, height=130, width=440)
image3 = PhotoImage(file="welcome.gif")
canvas.create_image(0, 0, anchor='nw', image=image3)
canvas.grid(row=0, column=0, columnspan=2)
Label(text="你好\n"
           "请选择你的登录方式:\n", font="微软雅黑 14", justify=LEFT).grid(row=1, column=0, columnspan=2,
                                                              sticky='w', pady=10)
Button(master, text="学生", font="微软雅黑 14", relief="solid",
       command=lambda: login("student login", master)).grid(sticky='w', row=3, column=0, pady=10)
Button(master, text="老师", font="微软雅黑 14", relief="solid",
       command=lambda: login("teacher login", master)).grid(sticky='e', row=3, column=1)
Button(master, text="管理员", font="微软雅黑 14", relief="solid",
       command=lambda: login("adminstrator login", master)).grid(row=4, column=0, columnspan=2, pady=10)
master.mainloop()
