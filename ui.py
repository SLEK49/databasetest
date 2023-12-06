#!/usr/bin/env python
# coding=utf-8
import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter.ttk import Combobox

host = "localhost"
user = "root"
password = "123456"
dbname = "system_choose_course"

#更新学生信息
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

#获取当前登录学生信息
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

#学生信息更新窗口
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


#学生插入课程
def insert_course(e):
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname, )
        cur = db.cursor()
        sql = "INSERT INTO sc(sId,cId,grade) VALUES (%s,%s,0)"
        value = (uid, e.get())
        cur.execute(sql, value)
        db.commit()
        tkinter.messagebox.showinfo("successful", "插入成功")
    except pymysql.Error as e:
        tkinter.messagebox.showinfo("unsuccessful", "插入失败" + str(e))
        db.rollback()
    db.close()

#获取所有课程信息
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

#学生选课窗口
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

#获取当前登录学生的课程信息
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

#当前学生课程信息窗口
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

#更新老师信息
def updateT_info(v, e):
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname, )
        cur = db.cursor()
        sql = "UPDATE teacherinfo SET {}='{}' WHERE tid='{}'"
        cur.execute(sql.format(v.get(), e.get(), uid))
        db.commit()
        tkinter.messagebox.showinfo("successful", "插入成功")
    except pymysql.Error as e:
        tkinter.messagebox.showinfo("unsuccessful", "插入失败" + str(e))
        db.rollback()
    db.close()

#获取当前登录老师信息
def personT_info():
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname,
                             )
        print("数据库连接成功")
        cur = db.cursor()
        sql = "SELECT * FROM teacherinfo where tid = '{}'"
        cur.execute(sql.format(uid))
        results = cur.fetchall()
        return results

    except pymysql.Error as e:
        print("数据查询失败" + str(e))
    db.close()

#老师信息更新窗口
def updateT_it(win):
    root = Toplevel(win)
    root.title("change_info")
    root.geometry("540x230")
    Label(root, text="{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}".format(
        "教师编号", "教师名称", "毕业院校", "职称", "学历", "性别", "出生日期")).grid(row=0, column=0, columnspan=2,
                                                                pady=9, sticky="w")
    var = StringVar()
    rels = personT_info()
    cb = Combobox(root, textvariable=var, width=17)
    cb["value"] = ("tTitle", "eduBg", "gender", "birthday")
    i = 1
    for rel in rels:
        s1 = (
            "{:<16}{:<16}{:<16}{:<16}{:<16}{:<16}{:<16}".format(
                rel[0], rel[1], rel[2], rel[3], rel[4], rel[5],rel[6]))
        Label(root, text=s1).grid(row=i, column=0,
                                  columnspan=2, padx=20, pady=30, sticky="w")
        i = i + 1
    e1 = Entry(root)
    Label(root, text="请选择将要修改的信息").grid(
        padx=5, row=i, pady=8, column=0, sticky="e")
    cb.grid(padx=5, row=i, column=1, pady=8, sticky="w")
    i = i + 1
    Label(root, text="请输入要修改的值").grid(padx=5, row=i, column=0, sticky="e")
    e1.grid(padx=5, row=i, column=1, sticky="w")
    Button(root, text="提交", command=lambda: updateT_info(
        var, e1)).grid(row=i + 1, column=0, columnspan=2)

#更新成绩信息
def updateG_info(g, s, c):
    try:

        if g.get() == "":
            tkinter.messagebox.showinfo("失败", "成绩不能为空")
            return

        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname, )
        cur = db.cursor()

        # 查询记录是否存在以及是否需要更新
        sql_select = "SELECT grade FROM sc WHERE sid='{}' AND cid='{}'".format(
            s.get(), c.get())
        cur.execute(sql_select)
        result = cur.fetchone()

        if result is None:
            tkinter.messagebox.showinfo("失败", "记录不存在")
            return

        sql = "UPDATE sc SET grade ='{}' WHERE sid='{}' AND cid='{}'"
        cur.execute(sql.format(g.get(), s.get(), c.get()))
        db.commit()
        tkinter.messagebox.showinfo("successful", "插入成功")
    except pymysql.Error as e:
        tkinter.messagebox.showinfo("unsuccessful", "插入失败" + str(e))
        db.rollback()
    db.close()

#获取当前登陆老师能修改成绩表
def get_grade():
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname,
                             )
        print("数据库连接成功")
        cur = db.cursor()
        sql = "SELECT sc.cId, sc.sId, sc.grade FROM sc JOIN teach t ON sc.cId = t.cId WHERE t.tId = '{}'"
        cur.execute(sql.format(uid))
        results = cur.fetchall()
        return results

    except pymysql.Error as e:
        print("数据查询失败" + str(e))
    db.close()

#老师输入成绩界面
def input_grade(win):
    root = Toplevel(win)
    root.title("input_grade")
    root.geometry("300x400")
    Label(root, text="{:<14}{:<14}{:<14}".format(
                    "课程编号", "学生编号", "成绩")).grid(row=0, column=0, columnspan=2,
                                                                pady=9, sticky="w")
    rels = get_grade()
    i = 1
    for rel in rels:
        s1 = (
            "{:<14}{:<14}{:<14}".format(
                rel[0], rel[1], rel[2]))
        Label(root, text=s1).grid(row=i, column=0,
                                  columnspan=2, padx=30, pady=10, sticky="w")
        i = i + 1
    c1 = Entry(root)
    i = i + 1
    Label(root, text="请输入cid").grid(padx=5, row=i, column=0, sticky="e")
    c1.grid(padx=5, row=i, column=1, sticky="w")
    s1 = Entry(root)
    i = i + 1
    Label(root, text="请输入sid").grid(padx=5, row=i, column=0, sticky="e")
    s1.grid(padx=5, row=i, column=1, sticky="w")
    g1 = Entry(root)
    i = i + 1
    Label(root, text="请输入grade").grid(padx=5, row=i, column=0, sticky="e")
    g1.grid(padx=5, row=i, column=1, sticky="w")
    Button(root, text="提交", command=lambda: updateG_info(g1, s1, c1)
    ).grid(row=i + 1, column=0, columnspan=2)

#获取当前登陆老师课程信息
def getT_course():
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname,
                             )
        print("数据库连接成功")
        cur = db.cursor()
        sql = "SELECT courseinfo.cid, courseinfo.cName, courseinfo.cIntro, courseinfo.cHour, courseinfo.cCredit, courseinfo.cWeek FROM courseinfo JOIN teach t ON courseinfo.cId = t.cId WHERE t.tId = '{}'"
        cur.execute(sql.format(uid))
        results = cur.fetchall()
        return results

    except pymysql.Error as e:
        print("数据查询失败" + str(e))
    db.close()

#老师查看课程信息界面
def teach_course(win):
    root = Toplevel(win)
    root.title("input_grade")
    root.geometry("500x230")
    Label(root, text="{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}".format(
        "课程编号", "课程名称", "课程介绍","课时","学分","上课星期")).grid(row=0, column=0, columnspan=2,
                                      pady=9, sticky="w")
    rels = getT_course()
    i = 1
    for rel in rels:
        s1 = (
            "{:<18}{:<18}{:<18}{:<18}{:<18}{:<18}".format(
                rel[0], rel[1], rel[2],rel[3], rel[4], rel[5]))
        Label(root, text=s1).grid(row=i, column=0,
                                  columnspan=5, padx=20, pady=10, sticky="w")
        i = i + 1

#管理员增加学生
def insert_student(id1, pwd, name):
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname,
                             )
        print("数据库连接成功")
        cur = db.cursor()
        sql = "INSERT INTO stupwd(id, pwd, name) VALUES('{}', '{}', '{}')"
        cur.execute(sql.format(id1, pwd ,name))
        sql = "INSERT INTO studentinfo(sid,major,name,dept,gender,birthday) VALUES('{}','none','none','none','1','2000-01-01')"
        cur.execute(sql.format(id1))
        sql = "INSERT INTO sc(sid, cid, grade) VALUES('{}', '100', 0)"
        cur.execute(sql.format(id1))
        db.commit()
        tkinter.messagebox.showinfo("successful", "添加成功")

    except pymysql.Error as e:
        print("数据查询失败" + str(e))
    db.close()

#管理员增加学生界面
def input_student(win):
    root = Toplevel(win)
    root.title("添加学生")
    root.geometry("300x400")

    id1 = Entry(root)
    i = 1
    Label(root, text="请输入id").grid(padx=5, row=i, column=0, sticky="e")
    id1.grid(padx=5, row=i, column=1, sticky="w")

    pwd1 = Entry(root)
    i = i + 1
    Label(root, text="请输入pwd").grid(padx=5, row=i, column=0, sticky="e")
    pwd1.grid(padx=5, row=i, column=1, sticky="w")

    name1 = Entry(root)
    i = i + 1
    Label(root, text="请输入name").grid(padx=5, row=i, column=0, sticky="e")
    name1.grid(padx=5, row=i, column=1, sticky="w")

    Button(root, text="提交", command=lambda: insert_student(id1.get(), pwd1.get(), name1.get())
    ).grid(row=i + 1, column=0, columnspan=2)

#管理员增加老师
def insert_teacher(id1, pwd, name):
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname,
                             )
        print("数据库连接成功")
        cur = db.cursor()
        sql = "INSERT INTO teacherpwd(id, pwd, name) VALUES('{}', '{}', '{}')"
        cur.execute(sql.format(id1, pwd, name))
        sql = "INSERT INTO teacherinfo(tid,tName,university,tTitle,eduBg,gender,birthday) VALUES('{}','none','none','none','none','1','2000-01-01')"
        cur.execute(sql.format(id1))
        sql = "INSERT INTO teach(tid,cid) VALUES('{}','100')"
        cur.execute(sql.format(id1))
        db.commit()
        tkinter.messagebox.showinfo("successful", "添加成功")

    except pymysql.Error as e:
        print("数据查询失败" + str(e))
    db.close()

#管理员增加老师界面
def input_teacher(win):
    root = Toplevel(win)
    root.title("添加老师")
    root.geometry("300x400")

    id1 = Entry(root)
    i = 1
    Label(root, text="请输入id").grid(padx=5, row=i, column=0, sticky="e")
    id1.grid(padx=5, row=i, column=1, sticky="w")

    pwd1 = Entry(root)
    i = i + 1
    Label(root, text="请输入pwd").grid(padx=5, row=i, column=0, sticky="e")
    pwd1.grid(padx=5, row=i, column=1, sticky="w")

    name1 = Entry(root)
    i = i + 1
    Label(root, text="请输入name").grid(padx=5, row=i, column=0, sticky="e")
    name1.grid(padx=5, row=i, column=1, sticky="w")

    Button(root, text="提交", command=lambda: insert_teacher(id1.get(), pwd1.get(), name1.get())
           ).grid(row=i + 1, column=0, columnspan=2)

#管理员给老师加课程
def insertT_course(tid,cid):
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname, )
        cur = db.cursor()
        sql = "INSERT INTO teach(tId,cId) VALUES (%s,%s)"
        value = (tid.get(), cid.get())
        cur.execute(sql, value)
        db.commit()
        tkinter.messagebox.showinfo("successful", "插入成功")
    except pymysql.Error as e:
        tkinter.messagebox.showinfo("unsuccessful", "插入失败" + str(e))
        db.rollback()
    db.close()

#管理员为老师加课窗口
def chooseT_course(win):
    root = Toplevel(win)
    root.title("choose_course")
    root.geometry("600x500")
    Label(root, text="课程编号   课程名称   课程介绍    课程学时       课程学分      课程星期    老师姓名    班级编号").grid(row=0, column=0,
                                                                                            columnspan=2,
                                                                                            padx=5, pady=9)
    rels = cour_all()
    i = 1
    for rel in rels:
        s1 = (
            "{:<14}{:<14}{:<14}{:>14}{:>14}{:>14}{:>14}{:>14}".format(
                rel[0], rel[1], rel[2], rel[3], rel[4], rel[5], rel[6], rel[7]))
        Label(root, text=s1).grid(
            row=i, column=0, columnspan=2, padx=5, pady=9)
        i = i + 1
    cid1 = Entry(root)
    Label(root, text="请填入要插入的课程编号").grid(
        padx=5, row=i, pady=20, column=0, sticky="e")
    cid1.grid(padx=5, row=i, column=1, pady=10, sticky="w")
    i = i + 1
    tid1 = Entry(root)
    Label(root, text="请填入要插入的老师编号").grid(
        padx=5, row=i, pady=20, column=0, sticky="e")
    tid1.grid(padx=5, row=i, column=1, pady=10, sticky="w")
    Button(root, text="提交", command=lambda: insertT_course(
        cid1,tid1)).grid(row=i + 1, column=0, columnspan=2)

#管理员增加课程
def add_course(cid,cname,cintro,chour,ccredit,cweek):
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname, )
        cur = db.cursor()
        sql = "INSERT INTO courseinfo(cId,cName,cIntro,cHour,cCredit,cWeek) VALUES ('{}','{}','{}','{}','{}','{}')"
        cur.execute(sql.format(cid,cname,cintro,chour,ccredit,cweek))
        sql = "INSERT INTO teach(cId,tId) VALUES ('{}',100)"
        cur.execute(sql.format(cid))
        sql = "INSERT INTO classroom_arr(crId,cId,cTime) VALUES (100,'{}','周三1-2，周三3-4')"
        cur.execute(sql.format(cid))
        db.commit()
        tkinter.messagebox.showinfo("successful", "插入成功")
    except pymysql.Error as e:
        tkinter.messagebox.showinfo("unsuccessful", "插入失败" + str(e))
        db.rollback()
    db.close()

#管理员增加课程窗口
def add_Course(win):
    root = Toplevel(win)
    root.title("add_cours")
    root.geometry("600x600")
    Label(root, text="课程编号   课程名称   课程介绍    课程学时       课程学分      课程星期    老师姓名    班级编号").grid(row=0, column=0,
                                                                                            columnspan=2,
                                                                                            padx=5, pady=9)
    rels = cour_all()
    i = 1
    for rel in rels:
        s1 = (
            "{:<14}{:<14}{:<14}{:>14}{:>14}{:>14}{:>14}{:>14}".format(
                rel[0], rel[1], rel[2], rel[3], rel[4], rel[5], rel[6], rel[7]))
        Label(root, text=s1).grid(
            row=i, column=0, columnspan=2, padx=5, pady=9)
        i = i + 1
    cid1 = Entry(root)
    Label(root, text="请填入要插入的课程编号").grid(
        padx=5, row=i, pady=10, column=0, sticky="e")
    cid1.grid(padx=5, row=i, column=1, pady=10, sticky="w")
    i = i + 1
    cname1 = Entry(root)
    Label(root, text="请填入要插入的课程名称").grid(
        padx=5, row=i, pady=10, column=0, sticky="e")
    cname1.grid(padx=5, row=i, column=1, pady=10, sticky="w")
    i = i + 1
    cintro1 = Entry(root)
    Label(root, text="请填入要插入的课程介绍").grid(
        padx=5, row=i, pady=10, column=0, sticky="e")
    cintro1.grid(padx=5, row=i, column=1, pady=10, sticky="w")
    i = i + 1
    chour1 = Entry(root)
    Label(root, text="请填入要插入的课程学时").grid(
        padx=5, row=i, pady=10, column=0, sticky="e")
    chour1.grid(padx=5, row=i, column=1, pady=10, sticky="w")
    i = i + 1
    ccredit1 = Entry(root)
    Label(root, text="请填入要插入的课程学分").grid(
        padx=5, row=i, pady=10, column=0, sticky="e")
    ccredit1.grid(padx=5, row=i, column=1, pady=10, sticky="w")
    i = i + 1
    cweek1 = Entry(root)
    Label(root, text="请填入要插入的课程星期").grid(
        padx=5, row=i, pady=10, column=0, sticky="e")
    cweek1.grid(padx=5, row=i, column=1, pady=10, sticky="w")
    Button(root, text="提交", command=lambda: add_course(cid1.get(), cname1.get(), cintro1.get(
    ), chour1.get(), ccredit1.get(), cweek1.get())).grid(row=i + 1, column=0, columnspan=2)

#更新密码
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

#更改密码窗口
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

#管理员操作台
def admin_operate():
    admin_log = Tk()
    admin_log.title("管理员操作台")
    admin_log.geometry("310x310")
    Label(admin_log, text="Hello," + name + "\n请选择您的操作\n"
          , font="微软雅黑 14", justify=LEFT).grid(row=0, column=0, columnspan=2, sticky='w')
    Button(admin_log, text="增加学生", font="微软雅黑 12",command=lambda: input_student(admin_log)).grid(row=1, column=0, sticky="w")
    Button(admin_log, text="增加老师", font="微软雅黑 12",command=lambda: input_teacher(admin_log)).grid(row=1, column=1, padx=90)
    Button(admin_log, text="给老师加课", font="微软雅黑 12",command=lambda: chooseT_course(admin_log)).grid(row=4, column=0, sticky="w")
    Button(admin_log, text="修改密码", font="微软雅黑 12",command=lambda: change_password(admin_log, "adminpwd")).grid(row=4, column=1, padx=90, pady=10)
    Button(admin_log, text="增加课程", font="微软雅黑 12",command=lambda: add_Course(admin_log)).grid(row=5, column=0, sticky="w")

#教师操作台
def teacher_operate():
    teacher_log = Tk()
    teacher_log.title("老师操作台")
    teacher_log.geometry("250x220")
    Label(teacher_log, text="Hello," + name + "\n请选择您的操作\n"
          , font="微软雅黑 12", justify=LEFT).grid(row=0, column=0, columnspan=2, sticky="w", pady=10)
    Button(teacher_log, text="修改密码", font="微软雅黑 12", relief="solid",
           command=lambda: change_password(teacher_log, "teacherpwd")).grid(row=1, column=0)
    Button(teacher_log, text="输入成绩", font="微软雅黑 12", relief="solid",command=lambda: input_grade(teacher_log)).grid(row=1, column=1, sticky="e", padx=80)
    Button(teacher_log, text="查看课程信息", font="微软雅黑 12", relief="solid",command=lambda: teach_course(teacher_log)).grid(row=2, column=1)
    Button(teacher_log, text="修改信息", font="微软雅黑 12", relief="solid", command=lambda: updateT_it(teacher_log)).grid(row=2, column=0, pady=20)

#学生操作台
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

#验证用户登录的用户名与密码
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

#根据不同登陆类型打开相应操作界面
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

#登陆窗口
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
