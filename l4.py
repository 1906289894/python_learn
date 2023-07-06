"""
MySQL
"""
import openpyxl
import pymysql

conn = pymysql.connect(host="82.157.173.166", port=3306, user='root', password='sunjian990609', database='hrs',
                       charset='utf8mb4', autocommit=True)


def insert():
    no = int(input('部门编号：'))
    name = input('部门名称：')
    location = input('部门所在地：')
    try:
        with conn.cursor() as cursor:
            affected_rows = cursor.execute('insert into `tb_dept` values (%s, %s, %s)', (no, name, location))
            if affected_rows == 1:
                print('success')
        conn.commit()
    except pymysql.MySQLError as err:
        conn.rollback()
        print(type(err), err)
    finally:
        conn.close()


def delete(no=30):
    try:
        with conn.cursor() as cursor:
            row = cursor.execute('delete from `tb_dept` where `dno` = %s', (no,))
            if row == 1:
                print('del success')
        conn.commit()
    except pymysql.MySQLError as err:
        conn.rollback()
        print(type(err), err)
    finally:
        conn.close()


def select():
    try:
        with conn.cursor() as cursor:
            cursor.execute('select * from `tb_dept`')
            row = cursor.fetchall()
            for i in row:
                print(i)
    except pymysql.MySQLError as err:
        conn.rollback()
        print(type(err), err)
    finally:
        conn.close()


def export():
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = '员工基本信息'
    sheet.append(('工号', '姓名', '职位', '月薪', '补贴', '部门'))
    # sheet.append((10, '朱九真', '会计', 5566, 2500, '会计部'))
    # workbook.save('hrx.xlsx')
    try:
        with conn.cursor() as cursor:
            cursor.execute('select dept.dno, emp.ename, emp.job, emp.mgr, emp.sal, dept.dname '
                           'from `tb_emp` as emp INNER JOIN `tb_dept` as dept on emp.dno = dept.dno')
            row = cursor.fetchall()
            for i in row:
                sheet.append(i)
        workbook.save('hrx.xlsx')
    except pymysql.MySQLError as err:
        print(err)
    finally:
        conn.close()


if __name__ == '__main__':
    export()
