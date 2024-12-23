from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import tkinter as tk
from tkinter import Toplevel, Label, Frame, Button, Scrollbar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = Tk()
window.geometry("500x500")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python8"
)
mycursor = mydb.cursor()


def login():
    Account = entry_a.get()
    Password = entry_b.get()
    mycursor.execute("SELECT EmployeeID, role FROM accounts WHERE Account=%s AND Password=%s", (Account, Password))
    dn = mycursor.fetchone()
    if dn:
        employee_id, role = dn
        mycursor.execute("SELECT FirstName, LastName FROM employees WHERE EmployeeID=%s", (employee_id,))
        employee_name = mycursor.fetchone()
        if employee_name:
            employee_name = f"{employee_name[0]} {employee_name[1]}"
        else:
            employee_name = "Unknown"

        window.withdraw()
        if role == 'admin':
            show_trang_chu()
        elif role == 'nhanvien':
            show_trang_nv(employee_id, employee_name)
        else:
            messagebox.showerror("Lỗi", "Quyền truy cập không hợp lệ!")
    else:
        messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")

def exit_program():
    window.destroy()

def close_main_window():
    main_window_nv.withdraw()
    window.deiconify()

def show_trang_chu():
    global main_window
    main_window = Toplevel()
    main_window.geometry("1000x800")
    main_window.title("Quản lý")

    lable_tc = Label(main_window, text="QUẢN LÝ CỬA HÀNG NÔNG SẢN", font=("Arial", 30, "bold"), fg='Black')
    lable_tc.place(x=30, y=10, width=1000, height=100)

    buton_sp = Button(main_window, text="Quản lý sản phẩm", font=("Arial", 20, "bold"), fg='Black', bg='red',
                      command=Quan_ly_san_pham)
    buton_sp.place(x=150, y=150, width=300, height=200)
    buton_kh = Button(main_window, text="Quản lý khách hàng", font=("Arial", 20, "bold"), fg='Black', bg='blue',
                      command=Quan_ly_khach_hang)
    buton_kh.place(x=150, y=300, width=400, height=200)
    buton_dh = Button(main_window, text="Quản lý đơn hàng", font=("Arial", 20, "bold"), fg='Black', bg='yellow',
                      command=Quan_ly_don_hang)
    buton_dh.place(x=450, y=150, width=400, height=200)
    buton_dh = Button(main_window, text="Quản lý nhân viên", font=("Arial", 20, "bold"), fg='Black', bg='green',
                      command=Quan_ly_nhan_vien)
    buton_dh.place(x=500, y=300, width=350, height=300)
    buton_bc = Button(main_window, text="Báo cáo thông kê", font=("Arial", 20, "bold"), fg='Black',
                      command=Xuat_bao_cao_va_thong_ke)
    buton_bc.place(x=150, y=500, width=500, height=200)
    buton_bc = Button(main_window, text="Quản lý tài khoản", font=("Arial", 20, "bold"), fg='Black', bg='violet',
                      command=Quan_ly_tai_khoan)
    buton_bc.place(x=550, y=600, width=300, height=100)
    button_exit = Button(main_window, text="Thoát", font=("Arial", 10, "bold"), fg='Black', bg='red',
                         command=exit_program)
    button_exit.place(x=30, y=70, width=100, height=30)

    def close_main_window():
        main_window.withdraw()
        window.deiconify()

    button_close = Button(main_window, text="Đăng xuất", font=("Arial", 10, "bold"), bg='pink',fg='black', command=close_main_window)
    button_close.place(x=30, y=30, width=100, height=30)

def Quan_ly_san_pham():
    main_window.destroy()
    Quan_ly_san_pham_window = Tk()
    Quan_ly_san_pham_window.geometry("1000x800")
    Quan_ly_san_pham_window.title("Quản lý sản phẩm")
    Quan_ly_san_pham_window.configure(bg='#F2CED8')

    def close_quan_ly_san_pham_window():
        Quan_ly_san_pham_window.destroy()
        show_trang_chu()

    def hien_thi_san_pham():
        for widget in Quan_ly_san_pham_window.winfo_children():
            widget.destroy()

        scrollbar = Scrollbar(Quan_ly_san_pham_window)
        scrollbar.place(x=900, y=130, height=500)

        global tree
        style = ttk.Style()
        style.configure('mystyle.Treeview', rowheight=25, bd=5, relief='solid')

        tree = ttk.Treeview(Quan_ly_san_pham_window, columns=("ProductID", "ProductName", "Price", "Inventory", "DateAdded"),
                            show="headings", style='mystyle.Treeview')
        tree.place(x=320, y=120, width=700, height=670)
        scrollbar.config(command=tree.yview)

        tree.heading("ProductID", text="ProductID")
        tree.heading("ProductName", text="ProductName")
        tree.heading("Price", text="Price")
        tree.heading("Inventory", text="Inventory")
        tree.heading("DateAdded", text="Date Added")

        tree.column("ProductID", width=100)
        tree.column("ProductName", width=200)
        tree.column("Price", width=100)
        tree.column("Inventory", width=100)
        tree.column("DateAdded", width=100)

        sql = "SELECT ProductID, ProductName, Price, Inventory, DateAdded FROM products"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for product in result:
            tree.insert("", END, values=product)

        label_doc7 = Label(Quan_ly_san_pham_window, text="QUẢN LÝ SẢN PHẨM", font=("Arial", 30, "bold"), fg='black')
        label_doc7.place(x=300, y=30, width=500, height=60)
        label_ngang = Label(Quan_ly_san_pham_window, text="", bg='#F08080')
        label_ngang.place(x=0, y=100, width=1000, height=10)
        label_doc = Label(Quan_ly_san_pham_window, text="", bg='#F08080')
        label_doc.place(x=300, y=100, width=10, height=700)

        global entry_tim_kiem
        entry_tim_kiem = Entry(Quan_ly_san_pham_window)
        entry_tim_kiem.place(x=20, y=130, width=250, height=25)
        button_tim_sp = Button(Quan_ly_san_pham_window, text="Tìm sản phẩm", font=("Arial", 10, "bold"), fg='Black',

                                bg='#97CADB', command=tim_kiem_san_pham)
        button_tim_sp.place(x=50, y=160, width=100, height=25)
        button_refresh = Button(Quan_ly_san_pham_window, text="Refresh", font=("Arial", 10, "bold"), fg='Black',
                                bg='#97CADB', command=hien_thi_san_pham)
        button_refresh.place(x=150, y=160, width=100, height=25)

        button_close = Button(Quan_ly_san_pham_window, text="Quay lại", font=("Arial", 15, "bold"), fg='Black',
                              bg='lightyellow', command=close_quan_ly_san_pham_window)
        button_close.place(x=30, y=30, width=100, height=50)

        button_them_sp = Button(Quan_ly_san_pham_window, text="Thêm sản phẩm", font=("Arial", 10, "bold"), fg='Black',
                                bg='#97CADB', command=them_san_pham)
        button_them_sp.place(x=0, y=220, width=300, height=100)

        button_sua_sp = Button(Quan_ly_san_pham_window, text="Sửa sản phẩm", font=("Arial", 10, "bold"), fg='Black',
                               bg='#97CADB', command=sua_san_pham)
        button_sua_sp.place(x=0, y=350, width=300, height=100)

        button_xoa_sp = Button(Quan_ly_san_pham_window, text="Xóa sản phẩm", font=("Arial", 10, "bold"), fg='Black',
                               bg='#97CADB', command=xoa_san_pham)
        button_xoa_sp.place(x=0, y=480, width=300, height=100)

    def them_san_pham():
        def luu_san_pham():
            ProductName = entry_ten.get()
            Price = entry_gia.get()
            Inventory = entry_inventory.get()
            DateAdded = entry_date_added.get()

            if not ProductName or not Price or not Inventory or not DateAdded:
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin sản phẩm")
                return

            sql = "INSERT INTO products (ProductName, Price, Inventory, DateAdded) VALUES (%s, %s, %s, %s)"
            val = (ProductName, Price, Inventory, DateAdded)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Thông báo", "Thêm sản phẩm thành công")
            them_san_pham_window.destroy()
            hien_thi_san_pham()

        them_san_pham_window = Toplevel(Quan_ly_san_pham_window)
        them_san_pham_window.geometry("400x200")
        them_san_pham_window.title("Thêm sản phẩm")

        label_ten = Label(them_san_pham_window, text="Tên sản phẩm:", font=("Arial", 12))
        label_ten.grid(row=0, column=0, padx=10, pady=10)
        entry_ten = Entry(them_san_pham_window, font=("Arial", 12))
        entry_ten.grid(row=0, column=1, padx=10, pady=10)

        label_gia = Label(them_san_pham_window, text="Giá:", font=("Arial", 12))
        label_gia.grid(row=1, column=0, padx=10, pady=10)
        entry_gia = Entry(them_san_pham_window, font=("Arial", 12))
        entry_gia.grid(row=1, column=1, padx=10, pady=10)

        label_inventory = Label(them_san_pham_window, text="Inventory:", font=("Arial", 12))
        label_inventory.grid(row=2, column=0, padx=10, pady=10)
        entry_inventory = Entry(them_san_pham_window, font=("Arial", 12))
        entry_inventory.grid(row=2, column=1, padx=10, pady=10)

        label_date_added = Label(them_san_pham_window, text="Date Added:", font=("Arial", 12))
        label_date_added.grid(row=3, column=0, padx=10, pady=10)
        entry_date_added = Entry(them_san_pham_window, font=("Arial", 12))
        entry_date_added.grid(row=3, column=1, padx=10, pady=10)

        button_luu = Button(them_san_pham_window, text="Lưu", font=("Arial", 12), command=luu_san_pham)
        button_luu.grid(row=4, column=0, columnspan=2, pady=10)

    def sua_san_pham():
        def cap_nhat_san_pham():
            newProductName = entry_ten_moi.get()
            newPrice = entry_gia_moi.get()
            newInventory = entry_inventory_moi.get()
            newDateAdded = entry_date_added_moi.get()
            selected_product_id = tree.item(tree.selection())['values'][0]

            sql = "UPDATE products SET ProductName=%s, Price=%s, Inventory=%s, DateAdded=%s WHERE ProductID=%s"
            val = (newProductName, newPrice, newInventory, newDateAdded, selected_product_id)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Thông báo", "Cập nhật sản phẩm thành công")
            sua_san_pham_window.destroy()
            hien_thi_san_pham()

        if not tree.selection():
            messagebox.showerror("Lỗi", "Vui lòng chọn sản phẩm cần sửa")
            return

        selected_product = tree.item(tree.selection())['values']
        sua_san_pham_window = Toplevel(Quan_ly_san_pham_window)
        sua_san_pham_window.geometry("400x400")
        sua_san_pham_window.title("Sửa sản phẩm")

        label_ten_cu = Label(sua_san_pham_window, text="Tên sản phẩm cũ:", font=("Arial", 12))
        label_ten_cu.grid(row=0, column=0, padx=10, pady=10)
        label_ten_cu_val = Label(sua_san_pham_window, text=selected_product[1], font=("Arial", 12))
        label_ten_cu_val.grid(row=0, column=1, padx=10, pady=10)

        label_ten_moi = Label(sua_san_pham_window, text="Tên sản phẩm mới:", font=("Arial", 12))
        label_ten_moi.grid(row=1, column=0, padx=10, pady=10)
        entry_ten_moi = Entry(sua_san_pham_window, font=("Arial", 12))
        entry_ten_moi.grid(row=1, column=1, padx=10, pady=10)

        label_gia_cu = Label(sua_san_pham_window, text="Giá cũ:", font=("Arial", 12))
        label_gia_cu.grid(row=2, column=0, padx=10, pady=10)
        label_gia_cu_val = Label(sua_san_pham_window, text=selected_product[2], font=("Arial", 12))
        label_gia_cu_val.grid(row=2, column=1, padx=10, pady=10)

        label_gia_moi = Label(sua_san_pham_window, text="Giá mới:", font=("Arial", 12))
        label_gia_moi.grid(row=3, column=0, padx=10, pady=10)
        entry_gia_moi = Entry(sua_san_pham_window, font=("Arial", 12))
        entry_gia_moi.grid(row=3, column=1, padx=10, pady=10)

        label_inventory_cu = Label(sua_san_pham_window, text="Inventory cũ:", font=("Arial", 12))
        label_inventory_cu.grid(row=4, column=0, padx=10, pady=10)
        label_inventory_cu_val = Label(sua_san_pham_window, text=selected_product[3], font=("Arial", 12))
        label_inventory_cu_val.grid(row=4, column=1, padx=10, pady=10)

        label_inventory_moi = Label(sua_san_pham_window, text="Inventory mới:", font=("Arial", 12))
        label_inventory_moi.grid(row=5, column=0, padx=10, pady=10)
        entry_inventory_moi = Entry(sua_san_pham_window, font=("Arial", 12))
        entry_inventory_moi.grid(row=5, column=1, padx=10, pady=10)

        label_date_added_cu = Label(sua_san_pham_window, text="Date Added cũ:", font=("Arial", 12))
        label_date_added_cu.grid(row=6, column=0, padx=10, pady=10)
        label_date_added_cu_val = Label(sua_san_pham_window, text=selected_product[4], font=("Arial", 12))
        label_date_added_cu_val.grid(row=6, column=1, padx=10, pady=10)

        label_date_added_moi = Label(sua_san_pham_window, text="Date Added mới:", font=("Arial", 12))
        label_date_added_moi.grid(row=7, column=0, padx=10, pady=10)
        entry_date_added_moi = Entry(sua_san_pham_window, font=("Arial", 12))
        entry_date_added_moi.grid(row=7, column=1, padx=10, pady=10)

        button_cap_nhat = Button(sua_san_pham_window, text="Cập nhật", font=("Arial", 12), command=cap_nhat_san_pham)
        button_cap_nhat.grid(row=8, column=0, columnspan=2, pady=10)

    def xoa_san_pham():
        if not tree.selection():
            messagebox.showerror("Lỗi", "Vui lòng chọn sản phẩm cần xóa")
            return
        selected_product_id = tree.item(tree.selection())['values'][0]

        sql = "DELETE FROM products WHERE ProductID=%s"
        val = (selected_product_id,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Thông báo", "Xóa sản phẩm thành công")
        hien_thi_san_pham()

    def tim_kiem_san_pham():
        search_term = entry_tim_kiem.get()

        sql = "SELECT ProductID, ProductName, Price, Inventory, DateAdded FROM products WHERE ProductName LIKE %s"
        val = ("%" + search_term + "%",)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()

        tree.delete(*tree.get_children())
        for product in result:
            tree.insert("", END, values=product)

    hien_thi_san_pham()

def Quan_ly_khach_hang():
    main_window.destroy()
    Quan_ly_khach_hang_window = Tk()
    Quan_ly_khach_hang_window.geometry("1000x800")
    Quan_ly_khach_hang_window.title("Quản lý khách hàng")

    def close_quan_ly_khach_hang_window():
        Quan_ly_khach_hang_window.destroy()
        show_trang_chu()

    def hien_thi_khach_hang():
        for widget in Quan_ly_khach_hang_window.winfo_children():
            widget.destroy()

        scrollbar = Scrollbar(Quan_ly_khach_hang_window)
        scrollbar.place(x=880, y=130, height=500)

        global tree
        style = ttk.Style()
        style.configure('mystyle.Treeview', rowheight=25, bd=5, relief='solid')

        tree = ttk.Treeview(Quan_ly_khach_hang_window, columns=("CustomerID", "FirstName", "LastName", "Address", "Phone"),
                            show="headings", style='mystyle.Treeview')
        tree.place(x=320, y=120, width=680, height=670)
        scrollbar.config(command=tree.yview)

        tree.heading("CustomerID", text="CustomerID")
        tree.heading("FirstName", text="FirstName")
        tree.heading("LastName", text="LastName")
        tree.heading("Address", text="Address")
        tree.heading("Phone", text="Phone")

        tree.column("CustomerID", width=100)
        tree.column("FirstName", width=150)
        tree.column("LastName", width=150)
        tree.column("Address", width=200)
        tree.column("Phone", width=100)

        sql = "SELECT CustomerID, FirstName, LastName, Address, Phone FROM customers"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for customer in result:
            tree.insert("", END, values=customer)

        label_doc7 = Label(Quan_ly_khach_hang_window, text="QUẢN LÝ KHÁCH HÀNG", font=("Arial", 30, "bold"), fg='black')
        label_doc7.place(x=300, y=30, width=500, height=60)
        label_ngang = Label(Quan_ly_khach_hang_window, text="", bg='blue')
        label_ngang.place(x=0, y=100, width=1000, height=10)
        label_doc = Label(Quan_ly_khach_hang_window, text="", bg='blue')
        label_doc.place(x=300, y=100, width=10, height=700)

        global entry_tim_kiem
        entry_tim_kiem = Entry(Quan_ly_khach_hang_window)
        entry_tim_kiem.place(x=30, y=130, width=250, height=20)
        button_tim_kh = Button(Quan_ly_khach_hang_window, text="Tìm khách hàng", command=tim_kiem_khach_hang)
        button_tim_kh.place(x=50, y=160, width=100, height=25)
        button_refresh = Button(Quan_ly_khach_hang_window, text="Refresh",
                                command=hien_thi_khach_hang)
        button_refresh.place(x=150, y=160, width=100, height=25)

        button_close = Button(Quan_ly_khach_hang_window, text="Quay lại", font=("Arial", 15, "bold"), fg='Black',
                              bg='lightyellow', command=close_quan_ly_khach_hang_window)
        button_close.place(x=30, y=30, width=100, height=50)

        button_them_kh = Button(Quan_ly_khach_hang_window, text="Thêm khách hàng", font=("Arial", 10, "bold"), fg='Black',
                                bg='#97CADB', command=them_khach_hang)
        button_them_kh.place(x=0, y=220, width=300, height=100)

        button_sua_kh = Button(Quan_ly_khach_hang_window, text="Sửa khách hàng", font=("Arial", 10, "bold"), fg='Black',
                               bg='#97CADB', command=sua_khach_hang)
        button_sua_kh.place(x=0, y=350, width=300, height=100)

        button_xoa_kh = Button(Quan_ly_khach_hang_window, text="Xóa khách hàng", font=("Arial", 10, "bold"), fg='Black',
                               bg='#97CADB', command=xoa_khach_hang)
        button_xoa_kh.place(x=0, y=480, width=300, height=100)

    def them_khach_hang():
        def luu_khach_hang():
            FirstName = entry_ten.get()
            LastName = entry_ho.get()
            Address = entry_dia_chi.get()
            Phone = entry_sdt.get()

            if not FirstName or not LastName or not Address or not Phone:
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin khách hàng")
                return

            sql = "INSERT INTO customers (FirstName, LastName, Address, Phone) VALUES (%s, %s, %s, %s)"
            val = (FirstName, LastName, Address, Phone)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Thông báo", "Thêm khách hàng thành công")
            them_khach_hang_window.destroy()
            hien_thi_khach_hang()

        them_khach_hang_window = Toplevel(Quan_ly_khach_hang_window)
        them_khach_hang_window.geometry("350x250")
        them_khach_hang_window.title("Thêm khách hàng")

        label_ten = Label(them_khach_hang_window, text="Họ:", font=("Arial", 12))
        label_ten.grid(row=0, column=0, padx=10, pady=10)
        entry_ten = Entry(them_khach_hang_window, font=("Arial", 12))
        entry_ten.grid(row=0, column=1, padx=10, pady=10)

        label_ho = Label(them_khach_hang_window, text="Tên:", font=("Arial", 12))
        label_ho.grid(row=1, column=0, padx=10, pady=10)
        entry_ho = Entry(them_khach_hang_window, font=("Arial", 12))
        entry_ho.grid(row=1, column=1, padx=10, pady=10)

        label_dia_chi = Label(them_khach_hang_window, text="Địa chỉ:", font=("Arial", 12))
        label_dia_chi.grid(row=2, column=0, padx=10, pady=10)
        entry_dia_chi = Entry(them_khach_hang_window, font=("Arial", 12))
        entry_dia_chi.grid(row=2, column=1, padx=10, pady=10)

        label_sdt = Label(them_khach_hang_window, text="Số điện thoại:", font=("Arial", 12))
        label_sdt.grid(row=3, column=0, padx=10, pady=10)
        entry_sdt = Entry(them_khach_hang_window, font=("Arial", 12))
        entry_sdt.grid(row=3, column=1, padx=10, pady=10)

        button_luu = Button(them_khach_hang_window, text="Lưu", font=("Arial", 12), command=luu_khach_hang)
        button_luu.grid(row=4, column=0, columnspan=2, pady=10)

    def sua_khach_hang():
        def cap_nhat_khach_hang():
            newFirstName = entry_ten_moi.get()
            newLastName = entry_ho_moi.get()
            newAddress = entry_dia_chi_moi.get()
            newPhone = entry_sdt_moi.get()
            selected_customer_id = tree.item(tree.selection())['values'][0]

            sql = "UPDATE customers SET FirstName=%s, LastName=%s, Address=%s, Phone=%s WHERE CustomerID=%s"
            val = (newFirstName, newLastName, newAddress, newPhone, selected_customer_id)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Thông báo", "Cập nhật khách hàng thành công")
            sua_khach_hang_window.destroy()
            hien_thi_khach_hang()

        if not tree.selection():
            messagebox.showerror("Lỗi", "Vui lòng chọn khách hàng cần sửa")
            return

        selected_customer = tree.item(tree.selection())['values']
        sua_khach_hang_window = Toplevel(Quan_ly_khach_hang_window)
        sua_khach_hang_window.geometry("450x450")
        sua_khach_hang_window.title("Sửa khách hàng")

        label_ten_cu = Label(sua_khach_hang_window, text="Tên cũ:", font=("Arial", 12))
        label_ten_cu.grid(row=0, column=0, padx=10, pady=10)
        entry_ten_cu = Entry(sua_khach_hang_window, font=("Arial", 12), state='readonly')
        entry_ten_cu.grid(row=0, column=1, padx=10, pady=10)
        entry_ten_cu.insert(0, selected_customer[1])

        label_ho_cu = Label(sua_khach_hang_window, text="Họ cũ:", font=("Arial", 12))
        label_ho_cu.grid(row=1, column=0, padx=10, pady=10)
        entry_ho_cu = Entry(sua_khach_hang_window, font=("Arial", 12), state='readonly')
        entry_ho_cu.grid(row=1, column=1, padx=10, pady=10)
        entry_ho_cu.insert(0, selected_customer[2])

        label_dia_chi_cu = Label(sua_khach_hang_window, text="Địa chỉ cũ:", font=("Arial", 12))
        label_dia_chi_cu.grid(row=2, column=0, padx=10, pady=10)
        entry_dia_chi_cu = Entry(sua_khach_hang_window, font=("Arial", 12), state='readonly')
        entry_dia_chi_cu.grid(row=2, column=1, padx=10, pady=10)
        entry_dia_chi_cu.insert(0, selected_customer[3])

        label_sdt_cu = Label(sua_khach_hang_window, text="Số điện thoại cũ:", font=("Arial", 12))
        label_sdt_cu.grid(row=3, column=0, padx=10, pady=10)
        entry_sdt_cu = Entry(sua_khach_hang_window, font=("Arial", 12), state='readonly')
        entry_sdt_cu.grid(row=3, column=1, padx=10, pady=10)
        entry_sdt_cu.insert(0, selected_customer[4])

        label_ten_moi = Label(sua_khach_hang_window, text="Tên mới:", font=("Arial", 12))
        label_ten_moi.grid(row=4, column=0, padx=10, pady=10)
        entry_ten_moi = Entry(sua_khach_hang_window, font=("Arial", 12))
        entry_ten_moi.grid(row=4, column=1, padx=10, pady=10)

        label_ho_moi = Label(sua_khach_hang_window, text="Họ mới:", font=("Arial", 12))
        label_ho_moi.grid(row=5, column=0, padx=10, pady=10)
        entry_ho_moi = Entry(sua_khach_hang_window, font=("Arial", 12))
        entry_ho_moi.grid(row=5, column=1, padx=10, pady=10)

        label_dia_chi_moi = Label(sua_khach_hang_window, text="Địa chỉ mới:", font=("Arial", 12))
        label_dia_chi_moi.grid(row=6, column=0, padx=10, pady=10)
        entry_dia_chi_moi = Entry(sua_khach_hang_window, font=("Arial", 12))
        entry_dia_chi_moi.grid(row=6, column=1, padx=10, pady=10)

        label_sdt_moi = Label(sua_khach_hang_window, text="Số điện thoại mới:", font=("Arial", 12))
        label_sdt_moi.grid(row=7, column=0, padx=10, pady=10)
        entry_sdt_moi = Entry(sua_khach_hang_window, font=("Arial", 12))
        entry_sdt_moi.grid(row=7, column=1, padx=10, pady=10)

        button_cap_nhat = Button(sua_khach_hang_window, text="Cập nhật", font=("Arial", 12), command=cap_nhat_khach_hang)
        button_cap_nhat.grid(row=8, column=0, columnspan=2, pady=10)

    def xoa_khach_hang():
        if not tree.selection():
            messagebox.showerror("Lỗi", "Vui lòng chọn khách hàng cần xóa")
            return

        selected_customer_id = tree.item(tree.selection())['values'][0]
        sql = "DELETE FROM customers WHERE CustomerID=%s"
        val = (selected_customer_id,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Thông báo", "Xóa khách hàng thành công")
        hien_thi_khach_hang()

    def tim_kiem_khach_hang():
        customer_name = entry_tim_kiem.get().strip()
        for row in tree.get_children():
            tree.delete(row)

        if customer_name:
            sql = "SELECT CustomerID, FirstName, LastName, Address, Phone FROM customers WHERE FirstName LIKE %s OR LastName LIKE %s"
            val = ('%' + customer_name + '%', '%' + customer_name + '%')

            mycursor.execute(sql, val)
            result = mycursor.fetchall()

            if result:
                for customer in result:
                    tree.insert("", END, values=customer)
            else:
                messagebox.showinfo("Thông báo", "Không tìm thấy khách hàng nào phù hợp")
        else:
            hien_thi_khach_hang()

    hien_thi_khach_hang()

def Quan_ly_don_hang():
    main_window.destroy()
    quan_ly_don_hang_window = Tk()
    quan_ly_don_hang_window.geometry("1300x700")
    quan_ly_don_hang_window.title("Quản lý Đơn Hàng")
    quan_ly_don_hang_window.configure(bg="#ADEBAD")

    def close_quan_ly_don_hang_window():
        quan_ly_don_hang_window.destroy()
        show_trang_chu()

    def show_orders_table():
        clear_table()
        columns = ("OrderID", "OrderDate", "EmployeeID", "CustomerID", "ProductID", "Quantity", "Status", "TotalPaymentAmount")
        create_table(columns, "SELECT * FROM orders")

    def show_customers_table():
        clear_table()
        columns = ("CustomerID", "FirstName", "LastName", "Address", "Phone")
        create_table(columns, "SELECT * FROM customers")

    def show_products_table():
        clear_table()
        columns = ("ProductID", "ProductName", "Price", "Inventory", "DateAdded")
        create_table(columns, "SELECT ProductID, ProductName, Price, Inventory, DateAdded FROM products")

    def show_order_status_chart():
        clear_table()
        status_frame = Frame(detailed_frame, padx=20, pady=20)
        status_frame.pack(fill=tk.BOTH, expand=True)

        mycursor.execute("SELECT Status, COUNT(*) FROM orders GROUP BY Status")
        status_data = mycursor.fetchall()
        statuses = [x[0] for x in status_data]
        counts = [x[1] for x in status_data]

        fig, ax = plt.subplots()
        ax.pie(counts, labels=statuses, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title("Phân bố trạng thái đơn hàng")

        canvas = FigureCanvasTkAgg(fig, master=status_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def clear_table():
        for widget in detailed_frame.winfo_children():
            widget.destroy()

    def create_table(columns, query):
        tree = ttk.Treeview(detailed_frame, columns=columns, show="headings", height=15)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor=tk.CENTER)
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = Scrollbar(detailed_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscroll=scrollbar.set)

        mycursor.execute(query)
        rows = mycursor.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)

    label_title = Label(quan_ly_don_hang_window, text="QUẢN LÝ ĐƠN HÀNG", font=("Arial", 30, "bold"), fg='black')
    label_title.place(x=550, y=20)

    summary_frame = Frame(quan_ly_don_hang_window)
    summary_frame.place(x=0, y=100, width=600, height=100)

    mycursor.execute("SELECT COUNT(*), SUM(TotalPaymentAmount) FROM orders")
    total_orders, total_revenue = mycursor.fetchone()

    mycursor.execute("SELECT COUNT(*) FROM customers")
    total_customers = mycursor.fetchone()[0]

    mycursor.execute("SELECT COUNT(*) FROM products")
    total_products = mycursor.fetchone()[0]

    Label(summary_frame, text=f"Tổng số đơn hàng: {total_orders}", font=("Arial", 15)).grid(row=0, column=0, padx=20, pady=10)
    Label(summary_frame, text=f"Tổng số khách hàng: {total_customers}", font=("Arial", 15)).grid(row=0, column=1, padx=20, pady=10)
    Label(summary_frame, text=f"Tổng số sản phẩm: {total_products}", font=("Arial", 15)).grid(row=1, column=0, padx=20, pady=10)
    Label(summary_frame, text=f"Tổng doanh thu: {total_revenue:.2f} VND", font=("Arial", 15)).grid(row=1, column=1, padx=20, pady=10)

    Button(quan_ly_don_hang_window, text="Hiển thị đơn hàng", font=("Arial", 15), command=show_orders_table).place(x=20, y=220, width=200, height=50)
    Button(quan_ly_don_hang_window, text="Hiển thị khách hàng", font=("Arial", 15), command=show_customers_table).place(x=240, y=220, width=200, height=50)
    Button(quan_ly_don_hang_window, text="Hiển thị sản phẩm", font=("Arial", 15), command=show_products_table).place(x=460, y=220, width=200, height=50)
    Button(quan_ly_don_hang_window, text="Hiển thị trạng thái đơn hàng", font=("Arial", 15), command=show_order_status_chart).place(x=680, y=220, width=250, height=50)

    button_close = Button(quan_ly_don_hang_window, text="Quay lại", font=("Arial", 15, "bold"), fg='Black', bg='lightyellow', command=close_quan_ly_don_hang_window)
    button_close.place(x=950, y=220, width=200, height=50)

    detailed_frame = Frame(quan_ly_don_hang_window, bd=2, relief=SUNKEN)
    detailed_frame.place(x=20, y=300, width=1300, height=400)

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=1, bd=1, font=('Arial', 12))
    style.configure("mystyle.Treeview.Heading", font=('Arial', 13, 'bold'))

    detailed_frame.grid_rowconfigure(0, weight=1)
    detailed_frame.grid_columnconfigure(0, weight=1)

def Xuat_bao_cao_va_thong_ke():
    main_window.destroy()
    bao_cao_va_thong_ke_window = Tk()
    bao_cao_va_thong_ke_window.geometry("1200x800")
    bao_cao_va_thong_ke_window.title("Xuất Báo Cáo và Thống Kê")
    bao_cao_va_thong_ke_window.configure(bg='#EAE7D6')

    def close_bao_cao_va_thong_ke_window():
        bao_cao_va_thong_ke_window.destroy()
        show_trang_chu()

    def show_orders():
        orders_frame.pack(fill=BOTH, expand=True)
        revenue_frame.pack_forget()
        products_frame.pack_forget()

    def show_revenue():
        orders_frame.pack_forget()
        revenue_frame.pack(fill=BOTH, expand=True)
        products_frame.pack_forget()

    def show_products():
        orders_frame.pack_forget()
        revenue_frame.pack_forget()
        products_frame.pack(fill=BOTH, expand=True)

    def generate_report():
        global entry_order_id
        global entry_revenue_date
        global entry_amount

        def load_revenue_data(month=None):
            tree_revenue.delete(*tree_revenue.get_children())
            if month:
                mycursor.execute(
                    "SELECT RevenueDate, SUM(Amount) as TotalAmount FROM revenue WHERE MONTH(RevenueDate) = %s GROUP BY RevenueDate",
                    (month,))
            else:
                mycursor.execute("SELECT RevenueDate, SUM(Amount) as TotalAmount FROM revenue GROUP BY RevenueDate")
            revenues = mycursor.fetchall()
            for revenue in revenues:
                tree_revenue.insert("", END, values=revenue)

        def filter_revenue_by_month():
            selected_month = month_var.get()
            if selected_month:
                load_revenue_data(selected_month)
                mycursor.execute("SELECT SUM(Amount) FROM revenue WHERE MONTH(RevenueDate) = %s", (selected_month,))
                total_revenue = mycursor.fetchone()[0]
                if total_revenue:
                    lbl_total_revenue.config(text=f"Tổng doanh thu tháng {selected_month}: {total_revenue:.2f} VND")
                else:
                    lbl_total_revenue.config(text=f"Tổng doanh thu tháng {selected_month}: 0 VND")
            else:
                messagebox.showerror("Lỗi", "Vui lòng chọn tháng")

        bao_cao_va_thong_ke_window = Toplevel()
        bao_cao_va_thong_ke_window.geometry("1000x750")
        bao_cao_va_thong_ke_window.title("Tạo Báo Cáo")

        Button(bao_cao_va_thong_ke_window, text="Hiển thị tất cả", font=("Arial", 12), command=load_revenue_data).pack(
            pady=10)

        Label(bao_cao_va_thong_ke_window, text="Chọn tháng:", font=("Arial", 12)).pack(pady=10)
        month_var = StringVar()
        month_combobox = ttk.Combobox(bao_cao_va_thong_ke_window, textvariable=month_var, font=("Arial", 12))
        month_combobox['values'] = [str(i) for i in range(1, 13)]
        month_combobox.pack(pady=10)

        Button(bao_cao_va_thong_ke_window, text="Lọc theo tháng", font=("Arial", 12),
               command=filter_revenue_by_month).pack(
            pady=10)

        lbl_total_revenue = Label(bao_cao_va_thong_ke_window, text="", font=("Arial", 12))
        lbl_total_revenue.pack(pady=10)

        columns = ("RevenueDate", "TotalAmount")
        tree_revenue = ttk.Treeview(bao_cao_va_thong_ke_window, columns=columns, show="headings")
        tree_revenue.heading("RevenueDate", text="Ngày Doanh Thu")
        tree_revenue.heading("TotalAmount", text="Tổng Số Tiền")

        tree_revenue.pack(expand=True, fill=BOTH)
        load_revenue_data()


    label_title = Label(bao_cao_va_thong_ke_window, text="BÁO CÁO VÀ THỐNG KÊ", font=("Arial", 30, "bold"), fg='black')
    label_title.pack(pady=20)

    label_divider = Label(bao_cao_va_thong_ke_window, text="", bg='blue')
    label_divider.pack(fill=X, padx=10, pady=10)

    summary_frame = LabelFrame(bao_cao_va_thong_ke_window, text="Tổng Quan", font=("Arial", 20, "bold"), fg='black',
                               padx=20, pady=20)
    summary_frame.pack(fill=X, padx=10, pady=10)

    mycursor.execute("SELECT COUNT(*), SUM(TotalPaymentAmount) FROM orders")
    total_orders, total_revenue = mycursor.fetchone()

    mycursor.execute("SELECT COUNT(*) FROM customers")
    total_customers = mycursor.fetchone()[0]

    mycursor.execute("SELECT COUNT(*) FROM products")
    total_products = mycursor.fetchone()[0]

    Label(summary_frame, text=f"Tổng số đơn hàng: {total_orders}", font=("Arial", 15)).grid(row=0, column=0, padx=20, pady=10)
    Label(summary_frame, text=f"Tổng doanh thu: {total_revenue:.2f} VND", font=("Arial", 15)).grid(row=0, column=1, padx=20, pady=10)
    Label(summary_frame, text=f"Tổng số khách hàng: {total_customers}", font=("Arial", 15)).grid(row=1, column=0, padx=20, pady=10)
    Label(summary_frame, text=f"Tổng số sản phẩm: {total_products}", font=("Arial", 15)).grid(row=1, column=1, padx=20, pady=10)

    button_frame = Frame(bao_cao_va_thong_ke_window)
    button_frame.pack(pady=10)

    button_orders = Button(button_frame, text="Chi Tiết Đơn Hàng", font=("Arial", 15, "bold"), fg='Black', bg='lightyellow', command=show_orders)
    button_orders.grid(row=0, column=0, padx=20, pady=10)

    button_revenue = Button(button_frame, text="Chi Tiết Doanh Thu", font=("Arial", 15, "bold"), fg='Black', bg='lightyellow', command=show_revenue)
    button_revenue.grid(row=0, column=1, padx=20, pady=10)

    button_products = Button(button_frame, text="Chi Tiết Sản Phẩm", font=("Arial", 15, "bold"), fg='Black', bg='lightyellow', command=show_products)
    button_products.grid(row=0, column=2, padx=20, pady=10)

    button_generate_report = Button(button_frame, text="Doanh Thu Theo Tháng", font=("Arial", 15, "bold"), fg='Black', bg='lightyellow', command=generate_report)
    button_generate_report.grid(row=0, column=3, padx=20, pady=10)

    detailed_frame = Frame(bao_cao_va_thong_ke_window)
    detailed_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    orders_frame = LabelFrame(detailed_frame, text="Chi Tiết Đơn Hàng", font=("Arial", 20, "bold"), fg='black')
    orders_frame.pack_forget()

    columns = ("OrderID", "OrderDate", "EmployeeID", "CustomerID", "ProductID", "Quantity", "Status", "TotalPaymentAmount")
    tree_orders = ttk.Treeview(orders_frame, columns=columns, show="headings", height=10)

    for col in columns:
        tree_orders.heading(col, text=col)
        tree_orders.column(col, anchor=CENTER)

    tree_orders.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar_orders = Scrollbar(orders_frame, orient="vertical", command=tree_orders.yview)
    scrollbar_orders.pack(side=RIGHT, fill=Y)

    tree_orders.configure(yscroll=scrollbar_orders.set)

    mycursor.execute("SELECT * FROM orders")
    orders = mycursor.fetchall()

    for order in orders:
        tree_orders.insert("", END, values=order)

    revenue_frame = LabelFrame(detailed_frame, text="Chi Tiết Doanh Thu", font=("Arial", 20, "bold"), fg='black')
    revenue_frame.pack_forget()

    columns_revenue = ("RevenueID", "OrderID", "RevenueDate", "Amount")
    tree_revenue = ttk.Treeview(revenue_frame, columns=columns_revenue, show="headings", height=10)

    for col in columns_revenue:
        tree_revenue.heading(col, text=col)
        tree_revenue.column(col, anchor=CENTER)

    tree_revenue.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar_revenue = Scrollbar(revenue_frame, orient="vertical", command=tree_revenue.yview)
    scrollbar_revenue.pack(side=RIGHT, fill=Y)

    tree_revenue.configure(yscroll=scrollbar_revenue.set)

    mycursor.execute("SELECT * FROM revenue")
    revenues = mycursor.fetchall()

    for revenue in revenues:
        tree_revenue.insert("", END, values=revenue)

    products_frame = LabelFrame(detailed_frame, text="Chi Tiết Sản Phẩm", font=("Arial", 20, "bold"), fg='black')
    products_frame.pack_forget()

    columns_products = ("ProductID", "ProductName", "Price", "Inventory", "DateAdded")
    tree_products = ttk.Treeview(products_frame, columns=columns_products, show="headings", height=10)

    for col in columns_products:
        tree_products.heading(col, text=col)
        tree_products.column(col, anchor=CENTER)

    tree_products.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar_products = Scrollbar(products_frame, orient="vertical", command=tree_products.yview)
    scrollbar_products.pack(side=RIGHT, fill=Y)

    tree_products.configure(yscroll=scrollbar_products.set)

    mycursor.execute("SELECT ProductID, ProductName, Price, Inventory, DateAdded FROM products")
    products = mycursor.fetchall()

    for product in products:
        tree_products.insert("", END, values=product)

    button_close = Button(bao_cao_va_thong_ke_window, text="Quay lại", font=("Arial", 15, "bold"), fg='Black', bg='lightyellow',
                          command=close_bao_cao_va_thong_ke_window)
    button_close.place(x=30, y=30, width=100, height=50)

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=1, bd=1, font=('Arial', 12))
    style.configure("mystyle.Treeview.Heading", font=('Arial', 13, 'bold'))

    tree_orders.configure(style="mystyle.Treeview")
    tree_revenue.configure(style="mystyle.Treeview")
    tree_products.configure(style="mystyle.Treeview")

    detailed_frame.grid_rowconfigure(0, weight=1)
    detailed_frame.grid_rowconfigure(1, weight=1)
    detailed_frame.grid_columnconfigure(0, weight=1)
    detailed_frame.grid_columnconfigure(1, weight=1)

def Quan_ly_nhan_vien():
    main_window.destroy()
    Quan_ly_nhan_vien_window = Tk()
    Quan_ly_nhan_vien_window.geometry("1200x800")
    Quan_ly_nhan_vien_window.title("Quản lý nhân viên")
    Quan_ly_nhan_vien_window.configure(bg='#D7F9FA')

    def close_quan_ly_nhan_vien_window():
        Quan_ly_nhan_vien_window.destroy()
        show_trang_chu()

    def hien_thi_nhan_vien():
        for widget in Quan_ly_nhan_vien_window.winfo_children():
            widget.destroy()

        scrollbar = Scrollbar(Quan_ly_nhan_vien_window)
        scrollbar.place(x=880, y=130, height=500)

        global tree
        style = ttk.Style()
        style.configure('mystyle.Treeview', rowheight=25, bd=5, relief='solid')

        tree = ttk.Treeview(Quan_ly_nhan_vien_window, columns=(
        "EmployeeID", "FirstName", "LastName", "DateOfBirth", "Position", "StartDate", "Salary", "Address", "Phone"),
                            show="headings", style='mystyle.Treeview')
        tree.place(x=320, y=120, width=865, height=670)
        scrollbar.config(command=tree.yview)

        tree.heading("EmployeeID", text="EmployeeID")
        tree.heading("FirstName", text="FirstName")
        tree.heading("LastName", text="LastName")
        tree.heading("DateOfBirth", text="DateOfBirth")
        tree.heading("Position", text="Position")
        tree.heading("StartDate", text="StartDate")
        tree.heading("Salary", text="Salary")
        tree.heading("Address", text="Address")
        tree.heading("Phone", text="Phone")

        tree.column("EmployeeID", width=60)
        tree.column("FirstName", width=80)
        tree.column("LastName", width=80)
        tree.column("DateOfBirth", width=60)
        tree.column("Position", width=85)
        tree.column("StartDate", width=60)
        tree.column("Salary", width=80)
        tree.column("Address", width=150)
        tree.column("Phone", width=50)

        sql = "SELECT EmployeeID, FirstName, LastName, DateOfBirth, Position, StartDate, Salary, Address, Phone FROM employees"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for employee in result:
            tree.insert("", END, values=employee)

        label_doc7 = Label(Quan_ly_nhan_vien_window, text="QUẢN LÝ NHÂN VIÊN", font=("Arial", 30, "bold"), fg='black')
        label_doc7.place(x=300, y=30, width=500, height=60)
        label_ngang = Label(Quan_ly_nhan_vien_window, text="", bg='#593E67')
        label_ngang.place(x=0, y=100, width=1200, height=10)
        label_doc = Label(Quan_ly_nhan_vien_window, text="", bg='#593E67')
        label_doc.place(x=300, y=100, width=10, height=700)

        global entry_tim_kiem
        entry_tim_kiem = Entry(Quan_ly_nhan_vien_window)
        entry_tim_kiem.place(x=30, y=130, width=250, height=20)
        button_tim_nv = Button(Quan_ly_nhan_vien_window, text="Tìm nhân viên", command=tim_kiem_nhan_vien)
        button_tim_nv.place(x=50, y=160, width=100, height=25)
        button_refresh = Button(Quan_ly_nhan_vien_window, text="Refresh",
                                command=hien_thi_nhan_vien)
        button_refresh.place(x=150, y=160, width=100, height=25)

        button_close = Button(Quan_ly_nhan_vien_window, text="Quay lại", font=("Arial", 15, "bold"), fg='Black',
                              bg='lightyellow', command=close_quan_ly_nhan_vien_window)
        button_close.place(x=30, y=30, width=100, height=50)

        button_them_nv = Button(Quan_ly_nhan_vien_window, text="Thêm nhân viên", font=("Arial", 10, "bold"), fg='Black',
                                bg='#97CADB', command=them_nhan_vien)
        button_them_nv.place(x=0, y=220, width=300, height=100)

        button_sua_nv = Button(Quan_ly_nhan_vien_window, text="Sửa nhân viên", font=("Arial", 10, "bold"), fg='Black',
                               bg='#97CADB', command=sua_nhan_vien)
        button_sua_nv.place(x=0, y=350, width=300, height=100)

        button_xoa_nv = Button(Quan_ly_nhan_vien_window, text="Xóa nhân viên", font=("Arial", 10, "bold"), fg='Black',
                               bg='#97CADB', command=xoa_nhan_vien)
        button_xoa_nv.place(x=0, y=480, width=300, height=100)

    def them_nhan_vien():
        def luu_nhan_vien():
            FirstName = entry_first_name.get()
            LastName = entry_last_name.get()
            DateOfBirth = entry_date_of_birth.get()
            Position = entry_position.get()
            StartDate = entry_start_date.get()
            Salary = entry_salary.get()
            Address = entry_address.get()
            Phone = entry_phone.get()

            if not FirstName or not LastName or not Position or not DateOfBirth or not StartDate or not Salary or not Address or not Phone:
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin nhân viên")
                return

            sql = "INSERT INTO employees (FirstName, LastName, DateOfBirth, Position, StartDate, Salary, Address, Phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (FirstName, LastName, DateOfBirth, Position, StartDate, Salary, Address, Phone)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Thông báo", "Thêm nhân viên thành công")
            them_nhan_vien_window.destroy()
            hien_thi_nhan_vien()

        them_nhan_vien_window = Toplevel(Quan_ly_nhan_vien_window)
        them_nhan_vien_window.geometry("450x400")
        them_nhan_vien_window.title("Thêm nhân viên")

        label_first_name = Label(them_nhan_vien_window, text="Họ và tên đệm:", font=("Arial", 12))
        label_first_name.grid(row=0, column=0, padx=10, pady=10)
        entry_first_name = Entry(them_nhan_vien_window, font=("Arial", 12))
        entry_first_name.grid(row=0, column=1, padx=10, pady=10)

        label_last_name = Label(them_nhan_vien_window, text="Tên:", font=("Arial", 12))
        label_last_name.grid(row=1, column=0, padx=10, pady=10)
        entry_last_name = Entry(them_nhan_vien_window, font=("Arial", 12))
        entry_last_name.grid(row=1, column=1, padx=10, pady=10)

        label_date_of_birth = Label(them_nhan_vien_window, text="Ngày sinh:", font=("Arial", 12))
        label_date_of_birth.grid(row=2, column=0, padx=10, pady=10)
        entry_date_of_birth = Entry(them_nhan_vien_window, font=("Arial", 12))
        entry_date_of_birth.grid(row=2, column=1, padx=10, pady=10)

        label_position = Label(them_nhan_vien_window, text="Chức vụ:", font=("Arial", 12))
        label_position.grid(row=3, column=0, padx=10, pady=10)
        entry_position = Entry(them_nhan_vien_window, font=("Arial", 12))
        entry_position.grid(row=3, column=1, padx=10, pady=10)

        label_start_date = Label(them_nhan_vien_window, text="Ngày bắt đầu:", font=("Arial", 12))
        label_start_date.grid(row=4, column=0, padx=10, pady=10)
        entry_start_date = Entry(them_nhan_vien_window, font=("Arial", 12))
        entry_start_date.grid(row=4, column=1, padx=10, pady=10)

        label_salary = Label(them_nhan_vien_window, text="Lương:", font=("Arial", 12))
        label_salary.grid(row=5, column=0, padx=10, pady=10)
        entry_salary = Entry(them_nhan_vien_window, font=("Arial", 12))
        entry_salary.grid(row=5, column=1, padx=10, pady=10)

        label_address = Label(them_nhan_vien_window, text="Địa chỉ:", font=("Arial", 12))
        label_address.grid(row=6, column=0, padx=10, pady=10)
        entry_address = Entry(them_nhan_vien_window, font=("Arial", 12))
        entry_address.grid(row=6, column=1, padx=10, pady=10)

        label_phone = Label(them_nhan_vien_window, text="Điện thoại:", font=("Arial", 12))
        label_phone.grid(row=7, column=0, padx=10, pady=10)
        entry_phone = Entry(them_nhan_vien_window, font=("Arial", 12))
        entry_phone.grid(row=7, column=1, padx=10, pady=10)

        button_luu = Button(them_nhan_vien_window, text="Lưu", font=("Arial", 12), command=luu_nhan_vien)
        button_luu.grid(row=8, column=0, columnspan=2, pady=10)

    def sua_nhan_vien():
        def cap_nhat_nhan_vien():
            newFirstName = entry_first_name_moi.get()
            newLastName = entry_last_name_moi.get()
            newPosition = entry_position_moi.get()

            selected_employee_id = tree.item(tree.selection())['values'][0]

            if not newFirstName:
                newFirstName = entry_first_name_cu.get()
            if not newLastName:
                newLastName = entry_last_name_cu.get()
            if not newPosition:
                newPosition = entry_position_cu.get()

            sql = "UPDATE employees SET FirstName=%s, LastName=%s, Position=%s WHERE EmployeeID=%s"
            val = (newFirstName, newLastName, newPosition, selected_employee_id)
            mycursor.execute(sql, val)
            mydb.commit()

            messagebox.showinfo("Thông báo", "Cập nhật nhân viên thành công")
            sua_nhan_vien_window.destroy()
            hien_thi_nhan_vien()

        if not tree.selection():
            messagebox.showerror("Lỗi", "Vui lòng chọn nhân viên cần sửa")
            return

        selected_employee = tree.item(tree.selection())['values']
        sua_nhan_vien_window = Toplevel(Quan_ly_nhan_vien_window)
        sua_nhan_vien_window.geometry("400x300")
        sua_nhan_vien_window.title("Sửa nhân viên")

        label_first_name_cu = Label(sua_nhan_vien_window, text="Họ và tên đệm cũ:", font=("Arial", 12))
        label_first_name_cu.grid(row=0, column=0, padx=10, pady=10)
        entry_first_name_cu = Entry(sua_nhan_vien_window, font=("Arial", 12), state='readonly')
        entry_first_name_cu.grid(row=0, column=1, padx=10, pady=10)
        entry_first_name_cu.insert(0, selected_employee[1])

        label_first_name_moi = Label(sua_nhan_vien_window, text="Họ và tên đệm mới:", font=("Arial", 12))
        label_first_name_moi.grid(row=1, column=0, padx=10, pady=10)
        entry_first_name_moi = Entry(sua_nhan_vien_window, font=("Arial", 12))
        entry_first_name_moi.grid(row=1, column=1, padx=10, pady=10)

        label_last_name_cu = Label(sua_nhan_vien_window, text="Tên cũ:", font=("Arial", 12))
        label_last_name_cu.grid(row=2, column=0, padx=10, pady=10)
        entry_last_name_cu = Entry(sua_nhan_vien_window, font=("Arial", 12), state='readonly')
        entry_last_name_cu.grid(row=2, column=1, padx=10, pady=10)
        entry_last_name_cu.insert(0, selected_employee[2])

        label_last_name_moi = Label(sua_nhan_vien_window, text="Tên mới:", font=("Arial", 12))
        label_last_name_moi.grid(row=3, column=0, padx=10, pady=10)
        entry_last_name_moi = Entry(sua_nhan_vien_window, font=("Arial", 12))
        entry_last_name_moi.grid(row=3, column=1, padx=10, pady=10)

        label_position_cu = Label(sua_nhan_vien_window, text="Chức vụ cũ:", font=("Arial", 12))
        label_position_cu.grid(row=4, column=0, padx=10, pady=10)
        entry_position_cu = Entry(sua_nhan_vien_window, font=("Arial", 12), state='readonly')
        entry_position_cu.grid(row=4, column=1, padx=10, pady=10)
        entry_position_cu.insert(0, selected_employee[3])

        label_position_moi = Label(sua_nhan_vien_window, text="Chức vụ mới:", font=("Arial", 12))
        label_position_moi.grid(row=5, column=0, padx=10, pady=10)
        entry_position_moi = Entry(sua_nhan_vien_window, font=("Arial", 12))
        entry_position_moi.grid(row=5, column=1, padx=10, pady=10)

        button_cap_nhat = Button(sua_nhan_vien_window, text="Cập nhật", font=("Arial", 12), command=cap_nhat_nhan_vien)
        button_cap_nhat.grid(row=6, column=0, columnspan=2, pady=10)

    def xoa_nhan_vien():
        if not tree.selection():
            messagebox.showerror("Lỗi", "Vui lòng chọn nhân viên cần xóa")
            return

        selected_employee_id = tree.item(tree.selection())['values'][0]
        sql = "DELETE FROM employees WHERE EmployeeID=%s"
        val = (selected_employee_id,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Thông báo", "Xóa nhân viên thành công")
        hien_thi_nhan_vien()

    def tim_kiem_nhan_vien():
        employee_name = entry_tim_kiem.get().strip()
        for row in tree.get_children():
            tree.delete(row)

        if employee_name:
            sql = "SELECT EmployeeID, FirstName, LastName, Position FROM employees WHERE FirstName LIKE %s OR LastName LIKE %s"
            val = ('%' + employee_name + '%', '%' + employee_name + '%')

            mycursor.execute(sql, val)
            result = mycursor.fetchall()

            if result:
                for employee in result:
                    tree.insert("", END, values=employee)
            else:
                messagebox.showinfo("Thông báo", "Không tìm thấy nhân viên nào phù hợp")
        else:
            hien_thi_nhan_vien()

    hien_thi_nhan_vien()

def Quan_ly_tai_khoan():
    main_window.destroy()
    Quan_ly_tai_khoan_window = Tk()
    Quan_ly_tai_khoan_window.geometry("1000x800")
    Quan_ly_tai_khoan_window.title("Quản lý tài khoản")
    Quan_ly_tai_khoan_window.configure(bg='#F2CED8')

    def close_quan_ly_tai_khoan_window():
        Quan_ly_tai_khoan_window.destroy()
        show_trang_chu()

    def hien_thi_tai_khoan():
        for widget in Quan_ly_tai_khoan_window.winfo_children():
            widget.destroy()

        scrollbar = Scrollbar(Quan_ly_tai_khoan_window)
        scrollbar.place(x=900, y=130, height=500)

        global tree
        style = ttk.Style()
        style.configure('mystyle.Treeview', rowheight=25, bd=5, relief='solid')

        tree = ttk.Treeview(Quan_ly_tai_khoan_window, columns=("IDAccount", "Account", "Password", "role", "EmployeeID"),
                            show="headings", style='mystyle.Treeview')
        tree.place(x=320, y=120, width=700, height=670)
        scrollbar.config(command=tree.yview)

        tree.heading("IDAccount", text="IDAccount")
        tree.heading("Account", text="Account")
        tree.heading("Password", text="Password")
        tree.heading("role", text="Role")
        tree.heading("EmployeeID", text="EmployeeID")

        tree.column("IDAccount", width=100)
        tree.column("Account", width=200)
        tree.column("Password", width=100)
        tree.column("role", width=100)
        tree.column("EmployeeID", width=100)

        sql = "SELECT IDAccount, Account, Password, role, EmployeeID FROM accounts"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for account in result:
            tree.insert("", END, values=account)

        label_doc7 = Label(Quan_ly_tai_khoan_window, text="QUẢN LÝ TÀI KHOẢN", font=("Arial", 30, "bold"), fg='black')
        label_doc7.place(x=300, y=30, width=500, height=60)
        label_ngang = Label(Quan_ly_tai_khoan_window, text="", bg='#F08080')
        label_ngang.place(x=0, y=100, width=1000, height=10)
        label_doc = Label(Quan_ly_tai_khoan_window, text="", bg='#F08080')
        label_doc.place(x=300, y=100, width=10, height=700)

        global entry_tim_kiem
        entry_tim_kiem = Entry(Quan_ly_tai_khoan_window)
        entry_tim_kiem.place(x=20, y=130, width=250, height=25)
        button_tim_tk = Button(Quan_ly_tai_khoan_window, text="Tìm tài khoản", font=("Arial", 10, "bold"), fg='Black',
                                bg='#97CADB', command=tim_kiem_tai_khoan)
        button_tim_tk.place(x=50, y=160, width=100, height=25)
        button_refresh = Button(Quan_ly_tai_khoan_window, text="Refresh", font=("Arial", 10, "bold"), fg='Black',
                                bg='#97CADB', command=hien_thi_tai_khoan)
        button_refresh.place(x=150, y=160, width=100, height=25)

        button_close = Button(Quan_ly_tai_khoan_window, text="Quay lại", font=("Arial", 15, "bold"), fg='Black',
                              bg='lightyellow', command=close_quan_ly_tai_khoan_window)
        button_close.place(x=30, y=30, width=100, height=50)

        button_them_tk = Button(Quan_ly_tai_khoan_window, text="Thêm tài khoản", font=("Arial", 10, "bold"), fg='Black',
                                bg='#97CADB', command=them_tai_khoan)
        button_them_tk.place(x=0, y=220, width=300, height=100)

        button_sua_tk = Button(Quan_ly_tai_khoan_window, text="Sửa tài khoản", font=("Arial", 10, "bold"), fg='Black',
                               bg='#97CADB', command=sua_tai_khoan)
        button_sua_tk.place(x=0, y=350, width=300, height=100)

        button_xoa_tk = Button(Quan_ly_tai_khoan_window, text="Xóa tài khoản", font=("Arial", 10, "bold"), fg='Black',
                               bg='#97CADB', command=xoa_tai_khoan)
        button_xoa_tk.place(x=0, y=480, width=300, height=100)

    def tim_kiem_tai_khoan():
        search_term = entry_tim_kiem.get()
        sql = "SELECT IDAccount, Account, Password, role, EmployeeID FROM accounts WHERE Account LIKE %s"
        val = ("%" + search_term + "%",)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        tree.delete(*tree.get_children())
        for account in result:
            tree.insert("", END, values=account)

    def them_tai_khoan():
        def luu_tai_khoan():
            Account = entry_ten.get()
            Password = entry_pw.get()
            role = "nhanvien"
            EmployeeID = entry_employee_id.get()

            if not Account or not Password or not EmployeeID:
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin tài khoản")
                return

            sql_check = "SELECT * FROM accounts WHERE EmployeeID = %s"
            val_check = (EmployeeID,)
            mycursor.execute(sql_check, val_check)
            if mycursor.fetchone():
                messagebox.showerror("Lỗi", "EmployeeID đã tồn tại trong hệ thống")
                return

            sql = "INSERT INTO accounts (Account, Password, role, EmployeeID) VALUES (%s, %s, %s, %s)"
            val = (Account, Password, role, EmployeeID)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Thông báo", "Thêm tài khoản thành công")
            them_tai_khoan_window.destroy()
            hien_thi_tai_khoan()

        them_tai_khoan_window = Toplevel(Quan_ly_tai_khoan_window)
        them_tai_khoan_window.geometry("400x200")
        them_tai_khoan_window.title("Thêm tài khoản")

        label_ten = Label(them_tai_khoan_window, text="Account:", font=("Arial", 12))
        label_ten.grid(row=0, column=0, padx=10, pady=10)
        entry_ten = Entry(them_tai_khoan_window, font=("Arial", 12))
        entry_ten.grid(row=0, column=1, padx=10, pady=10)

        label_pw = Label(them_tai_khoan_window, text="Password:", font=("Arial", 12))
        label_pw.grid(row=1, column=0, padx=10, pady=10)
        entry_pw = Entry(them_tai_khoan_window, font=("Arial", 12))
        entry_pw.grid(row=1, column=1, padx=10, pady=10)

        label_employee_id = Label(them_tai_khoan_window, text="EmployeeID:", font=("Arial", 12))
        label_employee_id.grid(row=2, column=0, padx=10, pady=10)
        entry_employee_id = Entry(them_tai_khoan_window, font=("Arial", 12))
        entry_employee_id.grid(row=2, column=1, padx=10, pady=10)

        button_luu = Button(them_tai_khoan_window, text="Lưu", font=("Arial", 12), bg='#97CADB', command=luu_tai_khoan)
        button_luu.grid(row=3, column=1, padx=10, pady=10)

    def sua_tai_khoan():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Lỗi", "Vui lòng chọn tài khoản cần sửa")
            return

        data = tree.item(selected_item, "values")
        IDAccount = data[0]

        def cap_nhat_tai_khoan():
            Account = entry_ten_moi.get()
            Password = entry_pw_moi.get()
            role = "nhanvien"
            EmployeeID = entry_gia_moi.get()

            if not Account or not Password or not EmployeeID:
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin tài khoản")
                return

            sql = "UPDATE accounts SET Account = %s, Password = %s, role = %s, EmployeeID = %s WHERE IDAccount = %s"
            val = (Account, Password, role, EmployeeID, IDAccount)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Thông báo", "Cập nhật tài khoản thành công")
            cap_nhat_tai_khoan_window.destroy()
            hien_thi_tai_khoan()

        cap_nhat_tai_khoan_window = Toplevel(Quan_ly_tai_khoan_window)
        cap_nhat_tai_khoan_window.geometry("400x200")
        cap_nhat_tai_khoan_window.title("Cập nhật tài khoản")

        label_ten_moi = Label(cap_nhat_tai_khoan_window, text="Account:", font=("Arial", 12))
        label_ten_moi.grid(row=0, column=0, padx=10, pady=10)
        entry_ten_moi = Entry(cap_nhat_tai_khoan_window, font=("Arial", 12))
        entry_ten_moi.grid(row=0, column=1, padx=10, pady=10)
        entry_ten_moi.insert(0, data[1])

        label_pw_moi = Label(cap_nhat_tai_khoan_window, text="Password:", font=("Arial", 12))
        label_pw_moi.grid(row=1, column=0, padx=10, pady=10)
        entry_pw_moi = Entry(cap_nhat_tai_khoan_window, font=("Arial", 12))
        entry_pw_moi.grid(row=1, column=1, padx=10, pady=10)
        entry_pw_moi.insert(0, data[2])

        label_gia_moi = Label(cap_nhat_tai_khoan_window, text="EmployeeID:", font=("Arial", 12))
        label_gia_moi.grid(row=2, column=0, padx=10, pady=10)
        entry_gia_moi = Entry(cap_nhat_tai_khoan_window, font=("Arial", 12))
        entry_gia_moi.grid(row=2, column=1, padx=10, pady=10)
        entry_gia_moi.insert(0, data[4])

        button_cap_nhat = Button(cap_nhat_tai_khoan_window, text="Cập nhật", font=("Arial", 12), bg='#97CADB', command=cap_nhat_tai_khoan)
        button_cap_nhat.grid(row=3, column=1, padx=10, pady=10)

    def xoa_tai_khoan():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Lỗi", "Vui lòng chọn tài khoản cần xóa")
            return

        data = tree.item(selected_item, "values")
        IDAccount = data[0]

        sql = "DELETE FROM accounts WHERE IDAccount = %s"
        val = (IDAccount,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Thông báo", "Xóa tài khoản thành công")
        hien_thi_tai_khoan()

    hien_thi_tai_khoan()

def show_trang_nv(employee_id, employee_name):
    global main_window_nv
    main_window_nv = Toplevel()
    main_window_nv.geometry("1200x700")
    main_window_nv.title("Bán hàng")
    main_window_nv.configure(bg='lightyellow')

    lable_tc = Label(main_window_nv, text="CỬA HÀNG NÔNG SẢN NAM ANH", font=("Arial", 30, "bold"), fg='Black')
    lable_tc.place(x=200, y=10, width=800, height=100)
    button_bh = Button(main_window_nv, text="Bán hàng", font=("Arial", 10, "bold"), bg='#6C7EE1', fg='black',
                       command=lambda: Ban_hang(employee_id, employee_name))
    button_bh.place(x=250, y=150, width=150, height=400)
    button_ttkh = Button(main_window_nv, text="Thông tin khách hàng", font=("Arial", 10, "bold"),bg='#92B9E3',fg='black',
                         command=lambda : Quan_ly_thong_tin_khach_hang(employee_id, employee_name))
    button_ttkh.place(x=250, y=550, width=400, height=150)
    button_khoh = Button(main_window_nv, text="Kho hàng",font=("Arial", 10, "bold"), bg='#8C7EE1', fg='black',
                         command=lambda: Quan_ly_kho_hang(employee_id, employee_name))
    button_khoh.place(x=650, y=300, width=150, height=400,)
    button_ls = Button(main_window_nv, text="Lịch sử giao dịch",font=("Arial", 10, "bold"), bg='#FFC4A4',fg='black'
                       ,command= lambda :lich_su_giao_dich(employee_id, employee_name))
    button_ls.place(x=400, y=150, width=400, height=150)
    label_tennv = Label(main_window_nv, text=employee_name, font=("Arial", 15, "bold"), bg='#FBA2D0')
    label_tennv.place(x=400, y=300, width=250, height=250)
    button_exit1 = Button(main_window_nv, text="Thoát", font=("Arial", 10, "bold"), fg='Black', bg='red',
                          command=exit_program)
    button_exit1.place(x=30, y=70, width=100, height=30)
    button_close_nv = Button(main_window_nv, text="Đăng xuất", font=("Arial", 10, "bold"), bg='pink', fg='black',
                             command=close_main_window)
    button_close_nv.place(x=30, y=30, width=100, height=30)

def Ban_hang(employee_id, employee_name):
    main_window_nv.destroy()
    sales_window = tk.Tk()
    sales_window.title("Nhân Viên Sale")
    sales_window.geometry("1200x800")
    sales_window.configure(bg="#F5F5F5")

    entry_customer_id = tk.Entry(sales_window, font=("Arial", 12))

    global cart_items
    cart_items = []

    def load_products():
        tree_products.delete(*tree_products.get_children())
        mycursor.execute("SELECT ProductID, ProductName, Price, Inventory FROM products")
        products = mycursor.fetchall()
        for product in products:
            tree_products.insert("", "end", values=product)

    def load_customers():
        tree_customers.delete(*tree_customers.get_children())
        mycursor.execute("SELECT * FROM customers")
        customers = mycursor.fetchall()
        for customer in customers:
            tree_customers.insert("", "end", values=customer)

    def load_cart():
        tree_cart.delete(*tree_cart.get_children())
        for item in cart_items:
            tree_cart.insert("", "end", values=item)

    def search_customer():
        phone_number = entry_customer_phone.get().strip()
        if not phone_number:
            messagebox.showerror("Error", "Please enter a phone number to search.")
            return

        tree_customers.delete(*tree_customers.get_children())

        mycursor.execute("SELECT * FROM customers WHERE Phone LIKE %s", (f"%{phone_number}%",))
        customers = mycursor.fetchall()
        for customer in customers:
            tree_customers.insert("", "end", values=customer)

    def on_customer_select(event):
        nonlocal entry_customer_id
        selected_item = tree_customers.focus()
        if selected_item:
            customer_id = tree_customers.item(selected_item, 'values')[0]
            entry_customer_id.delete(0, tk.END)
            entry_customer_id.insert(0, customer_id)

    def add_to_cart():
        selected_item = tree_products.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a product to add to cart.")
            return

        product_id, product_name, price, inventory = tree_products.item(selected_item, 'values')
        quantity = entry_quantity.get()
        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showerror("Error", "Please enter a valid quantity.")
            return

        total_price = float(price) * int(quantity)
        cart_items.append((product_id, product_name, price, quantity, total_price))
        load_cart()
        update_total_amount()

    def update_total_amount():
        total_amount = sum(float(item[4]) for item in cart_items)
        label_total_amount.config(text=f"Total Amount: ${total_amount:.2f}")

    def finalize_sale():
        customer_id = entry_customer_id.get()
        if not customer_id:
            messagebox.showerror("Error", "Please select a customer from the list.")
            return

        try:
            for item in cart_items:
                product_id, _, price, quantity, total_price = item
                mycursor.execute("SELECT inventory FROM products WHERE ProductID = %s", (product_id,))
                current_inventory = mycursor.fetchone()[0]

                if int(quantity) > current_inventory:
                    messagebox.showerror("Error", "Không đủ số lượng hàng!")
                    return

                updated_inventory = current_inventory - int(quantity)
                mycursor.execute("UPDATE products SET inventory = %s WHERE ProductID = %s",
                                 (updated_inventory, product_id))

                mycursor.execute(
                    "INSERT INTO orders (OrderDate, EmployeeID, CustomerID, ProductID, Quantity, Status, TotalPaymentAmount) VALUES (CURDATE(), %s, %s, %s, %s, 'Completed', %s)",
                    (employee_id, customer_id, product_id, quantity, total_price))
                order_id = mycursor.lastrowid

                mycursor.execute("INSERT INTO revenue (OrderID, RevenueDate, Amount) VALUES (%s, CURDATE(), %s)",
                                 (order_id, total_price))

            mydb.commit()
            messagebox.showinfo("Success", "Sale finalized successfully!")
            cart_items.clear()
            load_cart()
            update_total_amount()
            load_products()
            load_customers()
        except mysql.connector.Error as err:
            mydb.rollback()
            messagebox.showerror("Error", f"Error finalizing sale: {err}")

    def clear_cart():
        cart_items.clear()
        load_cart()
        update_total_amount()

    columns_products = ("ProductID", "ProductName", "Price", "Inventory")
    tree_products = ttk.Treeview(sales_window, columns=columns_products, show="headings")
    for col in columns_products:
        tree_products.heading(col, text=col)
    tree_products.place(x=50, y=50, width=600, height=300)
    load_products()

    columns_cart = ("ProductID", "ProductName", "Price", "Quantity", "TotalPrice")
    tree_cart = ttk.Treeview(sales_window, columns=columns_cart, show="headings")
    for col in columns_cart:
        tree_cart.heading(col, text=col)
    tree_cart.place(x=50, y=400, width=600, height=300)

    label_quantity = tk.Label(sales_window, text="Quantity", bg="#F5F5F5", font=("Arial", 12))
    label_quantity.place(x=700, y=50)
    entry_quantity = tk.Entry(sales_window, font=("Arial", 12))
    entry_quantity.place(x=800, y=50, width=100)

    button_add_to_cart = tk.Button(sales_window, text="Add to Cart", font=("Arial", 12), bg="#87CEEB",
                                   command=add_to_cart)
    button_add_to_cart.place(x=920, y=50)

    button_refresh = Button(sales_window, text="Refresh", font=("Arial", 10, "bold"), fg='Black',
                            bg='#97CADB', command=clear_cart)
    button_refresh.place(x=350, y=365, width=100, height=30)

    columns_customers = ("CustomerID", "FirstName", "LastName", "Address" ,"Phone")
    tree_customers = ttk.Treeview(sales_window, columns=columns_customers, show="headings")
    for col in columns_customers:
        tree_customers.heading(col, text=col)
    tree_customers.place(x=700, y=150, width=350, height=300)
    load_customers()

    tree_customers.bind("<ButtonRelease-1>", on_customer_select)

    label_search_phone = tk.Label(sales_window, text="Search by Phone:", bg="#F5F5F5", font=("Arial", 12))
    label_search_phone.place(x=700, y=470)
    entry_customer_phone = tk.Entry(sales_window, font=("Arial", 12))
    entry_customer_phone.place(x=830, y=470, width=150)
    button_search_customer = tk.Button(sales_window, text="Search", font=("Arial", 12), bg="#ADD8E6", command=search_customer)
    button_search_customer.place(x=990, y=470)

    label_employee_name = tk.Label(sales_window, text=f"Employee: {employee_name}", bg="#F5F5F5", font=("Arial", 12))
    label_employee_name.place(x=700, y=520)

    label_total_amount = tk.Label(sales_window, text="Total Amount: $0.00", bg="#F5F5F5", font=("Arial", 16))
    label_total_amount.place(x=700, y=570)

    button_finalize_sale = tk.Button(sales_window, text="Finalize Sale", font=("Arial", 12), bg="#32CD32",
                                     command=finalize_sale)
    button_finalize_sale.place(x=700, y=620, width=300, height=50)

    def close_sales_window():
        sales_window.destroy()
        show_trang_nv(employee_id, employee_name)

    button_close_sp = tk.Button(sales_window, text="Trang chủ", command=close_sales_window, bg='#C688EB')
    button_close_sp.place(x=950, y=700, width=100, height=30)


def Quan_ly_kho_hang(employee_id, employee_name):
    main_window_nv.destroy()
    Quan_ly_kho_hang_window = tk.Tk()
    Quan_ly_kho_hang_window.title("Nhân Viên Sale")
    Quan_ly_kho_hang_window.geometry("1200x800")
    Quan_ly_kho_hang_window.configure(bg="#F5F5F5")
    def close_quan_ly_san_pham_window():
        Quan_ly_kho_hang_window.destroy()
        show_trang_nv(employee_id, employee_name)

    def hien_thi_san_pham():
        for widget in Quan_ly_kho_hang_window.winfo_children():
            widget.destroy()

        scrollbar = Scrollbar(Quan_ly_kho_hang_window)
        scrollbar.place(x=900, y=130, height=500)

        global tree
        style = ttk.Style()
        style.configure('mystyle.Treeview', rowheight=25, bd=5, relief='solid')

        tree = ttk.Treeview(Quan_ly_kho_hang_window, columns=("ProductID", "ProductName", "Price", "Inventory", "DateAdded"),
                            show="headings", style='mystyle.Treeview')
        tree.place(x=320, y=120, width=700, height=670)
        scrollbar.config(command=tree.yview)

        tree.heading("ProductID", text="ProductID")
        tree.heading("ProductName", text="ProductName")
        tree.heading("Price", text="Price")
        tree.heading("Inventory", text="Inventory")
        tree.heading("DateAdded", text="Date Added")

        tree.column("ProductID", width=100)
        tree.column("ProductName", width=200)
        tree.column("Price", width=100)
        tree.column("Inventory", width=100)
        tree.column("DateAdded", width=100)

        sql = "SELECT ProductID, ProductName, Price, Inventory, DateAdded FROM products"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for product in result:
            tree.insert("", END, values=product)

        label_doc7 = Label(Quan_ly_kho_hang_window, text="QUẢN LÝ SẢN PHẨM", font=("Arial", 30, "bold"), fg='black')
        label_doc7.place(x=300, y=30, width=500, height=60)
        label_ngang = Label(Quan_ly_kho_hang_window, text="", bg='#F08080')
        label_ngang.place(x=0, y=100, width=1000, height=10)
        label_doc = Label(Quan_ly_kho_hang_window, text="", bg='#F08080')
        label_doc.place(x=300, y=100, width=10, height=700)

        global entry_tim_kiem
        entry_tim_kiem = Entry(Quan_ly_kho_hang_window)
        entry_tim_kiem.place(x=20, y=130, width=250, height=25)
        button_tim_sp = Button(Quan_ly_kho_hang_window, text="Tìm sản phẩm", font=("Arial", 10, "bold"), fg='Black',

                                bg='#97CADB', command=tim_kiem_san_pham)
        button_tim_sp.place(x=50, y=160, width=100, height=25)
        button_refresh = Button(Quan_ly_kho_hang_window, text="Refresh", font=("Arial", 10, "bold"), fg='Black',
                                bg='#97CADB', command=hien_thi_san_pham)
        button_refresh.place(x=150, y=160, width=100, height=25)

        button_close = Button(Quan_ly_kho_hang_window, text="Quay lại", font=("Arial", 15, "bold"), fg='Black',
                              bg='lightyellow', command=close_quan_ly_san_pham_window)
        button_close.place(x=30, y=30, width=100, height=50)

        button_them_sp = Button(Quan_ly_kho_hang_window, text="Nhập sản phẩm vào kho hàng", font=("Arial", 10, "bold"), fg='Black',
                                bg='#97CADB', command=nhap_san_pham)
        button_them_sp.place(x=0, y=220, width=300, height=100)

        button_xoa_sp = Button(Quan_ly_kho_hang_window, text="Xóa sản phẩm hư, hỏng", font=("Arial", 10, "bold"), fg='Black',
                               bg='#97CADB', command=xoa_san_pham)
        button_xoa_sp.place(x=0, y=350, width=300, height=100)

    def nhap_san_pham():
        def luu_san_pham():
            ProductName = entry_ten.get()
            Price = entry_gia.get()
            Inventory = entry_inventory.get()
            DateAdded = entry_date_added.get()

            if not ProductName or not Price or not Inventory or not DateAdded:
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin sản phẩm")
                return

            sql = "INSERT INTO products (ProductName, Price, Inventory, DateAdded) VALUES (%s, %s, %s, %s)"
            val = (ProductName, Price, Inventory, DateAdded)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Thông báo", "Đã nhập sản phẩm vào kho thành công")
            them_san_pham_window.destroy()
            hien_thi_san_pham()

        them_san_pham_window = Toplevel(Quan_ly_kho_hang_window)
        them_san_pham_window.geometry("400x300")
        them_san_pham_window.title("Thêm sản phẩm")

        label_ten = Label(them_san_pham_window, text="Tên sản phẩm:", font=("Arial", 12))
        label_ten.grid(row=0, column=0, padx=10, pady=10)
        entry_ten = Entry(them_san_pham_window, font=("Arial", 12))
        entry_ten.grid(row=0, column=1, padx=10, pady=10)

        label_gia = Label(them_san_pham_window, text="Giá:", font=("Arial", 12))
        label_gia.grid(row=1, column=0, padx=10, pady=10)
        entry_gia = Entry(them_san_pham_window, font=("Arial", 12))
        entry_gia.grid(row=1, column=1, padx=10, pady=10)

        label_inventory = Label(them_san_pham_window, text="Inventory:", font=("Arial", 12))
        label_inventory.grid(row=2, column=0, padx=10, pady=10)
        entry_inventory = Entry(them_san_pham_window, font=("Arial", 12))
        entry_inventory.grid(row=2, column=1, padx=10, pady=10)

        label_date_added = Label(them_san_pham_window, text="Date Added:", font=("Arial", 12))
        label_date_added.grid(row=3, column=0, padx=10, pady=10)
        entry_date_added = Entry(them_san_pham_window, font=("Arial", 12))
        entry_date_added.grid(row=3, column=1, padx=10, pady=10)

        button_luu = Button(them_san_pham_window, text="Lưu", font=("Arial", 12), command=luu_san_pham)
        button_luu.grid(row=4, column=0, columnspan=2, pady=10)

    def xoa_san_pham():
        if not tree.selection():
            messagebox.showerror("Lỗi", "Vui lòng chọn sản phẩm cần xóa")
            return
        selected_product_id = tree.item(tree.selection())['values'][0]

        sql = "DELETE FROM products WHERE ProductID=%s"
        val = (selected_product_id,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Thông báo", "Xóa sản phẩm thành công")
        hien_thi_san_pham()

    def tim_kiem_san_pham():
        search_term = entry_tim_kiem.get()

        sql = "SELECT ProductID, ProductName, Price, Inventory, DateAdded FROM products WHERE ProductName LIKE %s"
        val = ("%" + search_term + "%",)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()

        tree.delete(*tree.get_children())
        for product in result:
            tree.insert("", END, values=product)

    hien_thi_san_pham()


def Quan_ly_thong_tin_khach_hang(employee_id, employee_name):
    main_window_nv.destroy()
    Quan_ly_thong_tin_khach_hang_window = tk.Tk()
    Quan_ly_thong_tin_khach_hang_window.title("Nhân Viên Sale")
    Quan_ly_thong_tin_khach_hang_window.geometry("1200x800")
    Quan_ly_thong_tin_khach_hang_window.configure(bg="#F5F5F5")

    def close_quan_ly_thong_tin_khach_hang_window():
        Quan_ly_thong_tin_khach_hang_window.destroy()
        show_trang_nv(employee_id, employee_name)

    def hien_thi_khach_hang():
        for widget in Quan_ly_thong_tin_khach_hang_window.winfo_children():
            widget.destroy()

        scrollbar = Scrollbar(Quan_ly_thong_tin_khach_hang_window)
        scrollbar.place(x=880, y=130, height=500)

        global tree
        style = ttk.Style()
        style.configure('mystyle.Treeview', rowheight=25, bd=5, relief='solid')

        tree = ttk.Treeview(Quan_ly_thong_tin_khach_hang_window, columns=("CustomerID", "FirstName", "LastName", "Address", "Phone"),
                            show="headings", style='mystyle.Treeview')
        tree.place(x=320, y=120, width=680, height=670)
        scrollbar.config(command=tree.yview)

        tree.heading("CustomerID", text="CustomerID")
        tree.heading("FirstName", text="FirstName")
        tree.heading("LastName", text="LastName")
        tree.heading("Address", text="Address")
        tree.heading("Phone", text="Phone")

        tree.column("CustomerID", width=100)
        tree.column("FirstName", width=100)
        tree.column("LastName", width=100)
        tree.column("Address", width=200)
        tree.column("Phone", width=100)

        sql = "SELECT CustomerID, FirstName, LastName, Address, Phone FROM customers"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for customer in result:
            tree.insert("", END, values=customer)

        label_doc7 = Label(Quan_ly_thong_tin_khach_hang_window, text="THÔNG TIN KHÁCH HÀNG", font=("Arial", 30, "bold"), fg='black')
        label_doc7.place(x=300, y=30, width=500, height=60)
        label_ngang = Label(Quan_ly_thong_tin_khach_hang_window, text="", bg='blue')
        label_ngang.place(x=0, y=100, width=1000, height=10)
        label_doc = Label(Quan_ly_thong_tin_khach_hang_window, text="", bg='blue')
        label_doc.place(x=300, y=100, width=10, height=700)

        global entry_tim_kiem
        entry_tim_kiem = Entry(Quan_ly_thong_tin_khach_hang_window)
        entry_tim_kiem.place(x=30, y=130, width=250, height=20)
        button_tim_kh = Button(Quan_ly_thong_tin_khach_hang_window, text="Tìm khách hàng", command=tim_kiem_khach_hang)
        button_tim_kh.place(x=50, y=160, width=100, height=25)
        button_refresh = Button(Quan_ly_thong_tin_khach_hang_window, text="Refresh",
                                command=hien_thi_khach_hang)
        button_refresh.place(x=150, y=160, width=100, height=25)

        button_close = Button(Quan_ly_thong_tin_khach_hang_window, text="Quay lại", font=("Arial", 15, "bold"), fg='Black',
                              bg='lightyellow', command=close_quan_ly_thong_tin_khach_hang_window)
        button_close.place(x=30, y=30, width=100, height=50)

        button_them_kh = Button(Quan_ly_thong_tin_khach_hang_window, text="Thêm khách hàng", font=("Arial", 10, "bold"), fg='Black',
                                bg='#97CADB', command=them_khach_hang)
        button_them_kh.place(x=0, y=220, width=300, height=100)

        button_sua_kh = Button(Quan_ly_thong_tin_khach_hang_window, text="Sửa khách hàng", font=("Arial", 10, "bold"), fg='Black',
                               bg='#97CADB', command=sua_khach_hang)
        button_sua_kh.place(x=0, y=350, width=300, height=100)


    def them_khach_hang():
        def luu_khach_hang():
            FirstName = entry_ten.get()
            LastName = entry_ho.get()
            Address = entry_dia_chi.get()
            Phone = entry_sdt.get()

            if not FirstName or not LastName or not Address or not Phone:
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin khách hàng")
                return

            sql = "INSERT INTO customers (FirstName, LastName, Address, Phone) VALUES (%s, %s, %s, %s)"
            val = (FirstName, LastName, Address, Phone)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Thông báo", "Thêm khách hàng thành công")
            them_khach_hang_window.destroy()
            hien_thi_khach_hang()

        them_khach_hang_window = Toplevel(Quan_ly_thong_tin_khach_hang_window)
        them_khach_hang_window.geometry("350x250")
        them_khach_hang_window.title("Thêm khách hàng")

        label_ten = Label(them_khach_hang_window, text="Tên:", font=("Arial", 12))
        label_ten.grid(row=0, column=0, padx=10, pady=10)
        entry_ten = Entry(them_khach_hang_window, font=("Arial", 12))
        entry_ten.grid(row=0, column=1, padx=10, pady=10)

        label_ho = Label(them_khach_hang_window, text="Họ:", font=("Arial", 12))
        label_ho.grid(row=1, column=0, padx=10, pady=10)
        entry_ho = Entry(them_khach_hang_window, font=("Arial", 12))
        entry_ho.grid(row=1, column=1, padx=10, pady=10)

        label_dia_chi = Label(them_khach_hang_window, text="Địa chỉ:", font=("Arial", 12))
        label_dia_chi.grid(row=2, column=0, padx=10, pady=10)
        entry_dia_chi = Entry(them_khach_hang_window, font=("Arial", 12))
        entry_dia_chi.grid(row=2, column=1, padx=10, pady=10)

        label_sdt = Label(them_khach_hang_window, text="Số điện thoại:", font=("Arial", 12))
        label_sdt.grid(row=3, column=0, padx=10, pady=10)
        entry_sdt = Entry(them_khach_hang_window, font=("Arial", 12))
        entry_sdt.grid(row=3, column=1, padx=10, pady=10)

        button_luu = Button(them_khach_hang_window, text="Lưu", font=("Arial", 12), command=luu_khach_hang)
        button_luu.grid(row=4, column=0, columnspan=2, pady=10)

    def sua_khach_hang():
        def cap_nhat_khach_hang():
            newFirstName = entry_ten_moi.get()
            newLastName = entry_ho_moi.get()
            newAddress = entry_dia_chi_moi.get()
            newPhone = entry_sdt_moi.get()
            selected_customer_id = tree.item(tree.selection())['values'][0]

            sql = "UPDATE customers SET FirstName=%s, LastName=%s, Address=%s, Phone=%s WHERE CustomerID=%s"
            val = (newFirstName, newLastName, newAddress, newPhone, selected_customer_id)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Thông báo", "Cập nhật khách hàng thành công")
            sua_khach_hang_window.destroy()
            hien_thi_khach_hang()

        if not tree.selection():
            messagebox.showerror("Lỗi", "Vui lòng chọn khách hàng cần sửa")
            return

        selected_customer = tree.item(tree.selection())['values']
        sua_khach_hang_window = Toplevel(Quan_ly_thong_tin_khach_hang_window)
        sua_khach_hang_window.geometry("450x450")
        sua_khach_hang_window.title("Sửa khách hàng")

        label_ten_cu = Label(sua_khach_hang_window, text="Tên cũ:", font=("Arial", 12))
        label_ten_cu.grid(row=0, column=0, padx=10, pady=10)
        entry_ten_cu = Entry(sua_khach_hang_window, font=("Arial", 12), state='readonly')
        entry_ten_cu.grid(row=0, column=1, padx=10, pady=10)
        entry_ten_cu.insert(0, selected_customer[1])

        label_ho_cu = Label(sua_khach_hang_window, text="Họ cũ:", font=("Arial", 12))
        label_ho_cu.grid(row=1, column=0, padx=10, pady=10)
        entry_ho_cu = Entry(sua_khach_hang_window, font=("Arial", 12), state='readonly')
        entry_ho_cu.grid(row=1, column=1, padx=10, pady=10)
        entry_ho_cu.insert(0, selected_customer[2])

        label_dia_chi_cu = Label(sua_khach_hang_window, text="Địa chỉ cũ:", font=("Arial", 12))
        label_dia_chi_cu.grid(row=2, column=0, padx=10, pady=10)
        entry_dia_chi_cu = Entry(sua_khach_hang_window, font=("Arial", 12), state='readonly')
        entry_dia_chi_cu.grid(row=2, column=1, padx=10, pady=10)
        entry_dia_chi_cu.insert(0, selected_customer[3])

        label_sdt_cu = Label(sua_khach_hang_window, text="Số điện thoại cũ:", font=("Arial", 12))
        label_sdt_cu.grid(row=3, column=0, padx=10, pady=10)
        entry_sdt_cu = Entry(sua_khach_hang_window, font=("Arial", 12), state='readonly')
        entry_sdt_cu.grid(row=3, column=1, padx=10, pady=10)
        entry_sdt_cu.insert(0, selected_customer[4])

        label_ten_moi = Label(sua_khach_hang_window, text="Tên mới:", font=("Arial", 12))
        label_ten_moi.grid(row=4, column=0, padx=10, pady=10)
        entry_ten_moi = Entry(sua_khach_hang_window, font=("Arial", 12))
        entry_ten_moi.grid(row=4, column=1, padx=10, pady=10)

        label_ho_moi = Label(sua_khach_hang_window, text="Họ mới:", font=("Arial", 12))
        label_ho_moi.grid(row=5, column=0, padx=10, pady=10)
        entry_ho_moi = Entry(sua_khach_hang_window, font=("Arial", 12))
        entry_ho_moi.grid(row=5, column=1, padx=10, pady=10)

        label_dia_chi_moi = Label(sua_khach_hang_window, text="Địa chỉ mới:", font=("Arial", 12))
        label_dia_chi_moi.grid(row=6, column=0, padx=10, pady=10)
        entry_dia_chi_moi = Entry(sua_khach_hang_window, font=("Arial", 12))
        entry_dia_chi_moi.grid(row=6, column=1, padx=10, pady=10)

        label_sdt_moi = Label(sua_khach_hang_window, text="Số điện thoại mới:", font=("Arial", 12))
        label_sdt_moi.grid(row=7, column=0, padx=10, pady=10)
        entry_sdt_moi = Entry(sua_khach_hang_window, font=("Arial", 12))
        entry_sdt_moi.grid(row=7, column=1, padx=10, pady=10)

        button_cap_nhat = Button(sua_khach_hang_window, text="Cập nhật", font=("Arial", 12), command=cap_nhat_khach_hang)
        button_cap_nhat.grid(row=8, column=0, columnspan=2, pady=10)

    def tim_kiem_khach_hang():
        customer_name = entry_tim_kiem.get().strip()
        for row in tree.get_children():
            tree.delete(row)

        if customer_name:
            sql = "SELECT CustomerID, FirstName, LastName, Address, Phone FROM customers WHERE FirstName LIKE %s OR LastName LIKE %s"
            val = ('%' + customer_name + '%', '%' + customer_name + '%')

            mycursor.execute(sql, val)
            result = mycursor.fetchall()

            if result:
                for customer in result:
                    tree.insert("", END, values=customer)
            else:
                messagebox.showinfo("Thông báo", "Không tìm thấy khách hàng nào phù hợp")
        else:
            hien_thi_khach_hang()

    hien_thi_khach_hang()

def lich_su_giao_dich(employee_id, employee_name):
    main_window_nv.destroy()
    Lich_su_giao_dich_window = tk.Tk()
    Lich_su_giao_dich_window.title("Nhân Viên Sale")
    Lich_su_giao_dich_window.geometry("1200x800")
    Lich_su_giao_dich_window.configure(bg='#EAE7D6')
    def close_lich_su_giao_dich_window():
        Lich_su_giao_dich_window.destroy()
        show_trang_nv(employee_id, employee_name)




    def show_orders():
        orders_frame.pack(fill=BOTH, expand=True)
        revenue_frame.pack_forget()
        products_frame.pack_forget()

    def show_revenue():
        orders_frame.pack_forget()
        revenue_frame.pack(fill=BOTH, expand=True)
        products_frame.pack_forget()


    label_title = Label(Lich_su_giao_dich_window, text="LICH SỬ GIAO DỊCH", font=("Arial", 30, "bold"), fg='black')
    label_title.pack(pady=20)

    label_divider = Label(Lich_su_giao_dich_window, text="", bg='blue')
    label_divider.pack(fill=X, padx=10, pady=10)

    summary_frame = LabelFrame(Lich_su_giao_dich_window, text="Tổng Quan", font=("Arial", 20, "bold"), fg='black',
                               padx=20, pady=20)
    summary_frame.pack(fill=X, padx=10, pady=10)

    mycursor.execute("SELECT COUNT(*), SUM(TotalPaymentAmount) FROM orders")
    total_orders, total_revenue = mycursor.fetchone()

    mycursor.execute("SELECT COUNT(*) FROM customers")
    total_customers = mycursor.fetchone()[0]

    mycursor.execute("SELECT COUNT(*) FROM products")
    total_products = mycursor.fetchone()[0]

    Label(summary_frame, text=f"Tổng số đơn hàng: {total_orders}", font=("Arial", 15)).grid(row=0, column=0, padx=20, pady=10)
    Label(summary_frame, text=f"Tổng doanh thu: {total_revenue:.2f} VND", font=("Arial", 15)).grid(row=0, column=1, padx=20, pady=10)
    Label(summary_frame, text=f"Tổng số khách hàng: {total_customers}", font=("Arial", 15)).grid(row=1, column=0, padx=20, pady=10)
    Label(summary_frame, text=f"Tổng số sản phẩm: {total_products}", font=("Arial", 15)).grid(row=1, column=1, padx=20, pady=10)

    button_frame = Frame(Lich_su_giao_dich_window)
    button_frame.pack(pady=10)

    button_orders = Button(button_frame, text="Chi Tiết Đơn Hàng", font=("Arial", 15, "bold"), fg='Black', bg='lightyellow', command=show_orders)
    button_orders.grid(row=0, column=0, padx=20, pady=10)

    button_revenue = Button(button_frame, text="Lịch sử giao dịch", font=("Arial", 15, "bold"), fg='Black', bg='lightyellow', command=show_revenue)
    button_revenue.grid(row=0, column=1, padx=20, pady=10)

    detailed_frame = Frame(Lich_su_giao_dich_window)
    detailed_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    orders_frame = LabelFrame(detailed_frame, text="Chi Tiết Đơn Hàng", font=("Arial", 20, "bold"), fg='black')
    orders_frame.pack_forget()

    columns = ("OrderID", "OrderDate", "EmployeeID", "CustomerID", "ProductID", "Quantity", "Status", "TotalPaymentAmount")
    tree_orders = ttk.Treeview(orders_frame, columns=columns, show="headings", height=10)

    for col in columns:
        tree_orders.heading(col, text=col)
        tree_orders.column(col, anchor=CENTER)

    tree_orders.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar_orders = Scrollbar(orders_frame, orient="vertical", command=tree_orders.yview)
    scrollbar_orders.pack(side=RIGHT, fill=Y)

    tree_orders.configure(yscroll=scrollbar_orders.set)

    mycursor.execute("SELECT * FROM orders")
    orders = mycursor.fetchall()

    for order in orders:
        tree_orders.insert("", END, values=order)

    revenue_frame = LabelFrame(detailed_frame, text="Lịch sử giao dịch", font=("Arial", 20, "bold"), fg='black')
    revenue_frame.pack_forget()

    columns_revenue = ("RevenueID", "OrderID", "RevenueDate", "Amount")
    tree_revenue = ttk.Treeview(revenue_frame, columns=columns_revenue, show="headings", height=10)

    for col in columns_revenue:
        tree_revenue.heading(col, text=col)
        tree_revenue.column(col, anchor=CENTER)

    tree_revenue.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar_revenue = Scrollbar(revenue_frame, orient="vertical", command=tree_revenue.yview)
    scrollbar_revenue.pack(side=RIGHT, fill=Y)

    tree_revenue.configure(yscroll=scrollbar_revenue.set)

    mycursor.execute("SELECT * FROM revenue")
    revenues = mycursor.fetchall()

    for revenue in revenues:
        tree_revenue.insert("", END, values=revenue)

    products_frame = LabelFrame(detailed_frame, text="Chi Tiết Sản Phẩm", font=("Arial", 20, "bold"), fg='black')
    products_frame.pack_forget()

    columns_products = ("ProductID", "ProductName", "Price", "Inventory", "DateAdded")
    tree_products = ttk.Treeview(products_frame, columns=columns_products, show="headings", height=10)

    for col in columns_products:
        tree_products.heading(col, text=col)
        tree_products.column(col, anchor=CENTER)

    tree_products.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar_products = Scrollbar(products_frame, orient="vertical", command=tree_products.yview)
    scrollbar_products.pack(side=RIGHT, fill=Y)

    tree_products.configure(yscroll=scrollbar_products.set)

    mycursor.execute("SELECT ProductID, ProductName, Price, Inventory, DateAdded FROM products")
    products = mycursor.fetchall()

    for product in products:
        tree_products.insert("", END, values=product)

    button_close = Button(Lich_su_giao_dich_window, text="Quay lại", font=("Arial", 15, "bold"), fg='Black', bg='lightyellow',
                          command=close_lich_su_giao_dich_window)
    button_close.place(x=30, y=30, width=100, height=50)

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=1, bd=1, font=('Arial', 12))
    style.configure("mystyle.Treeview.Heading", font=('Arial', 13, 'bold'))

    tree_orders.configure(style="mystyle.Treeview")
    tree_revenue.configure(style="mystyle.Treeview")
    tree_products.configure(style="mystyle.Treeview")

    detailed_frame.grid_rowconfigure(0, weight=1)
    detailed_frame.grid_rowconfigure(1, weight=1)
    detailed_frame.grid_columnconfigure(0, weight=1)
    detailed_frame.grid_columnconfigure(1, weight=1)


label_login = Label(text="ĐĂNG NHẬP", font=("Arial", 24, "bold"))
label_login.configure(fg = 'Black')
label_login.place(x=150, y=80, width=200, height=50)

label_a = Label(window, text="Tên đăng nhập", font=("Arial", 15, "bold"), fg='Black', bg='lightyellow')
label_a.place(x=60, y=160)

label_b = Label(window, text="Mật khẩu", font=("Arial", 15, "bold"), fg='Black', bg='lightyellow')
label_b.place(x=60, y=200)

entry_a = Entry(window, font=("Arial", 15, "bold"))
entry_a.place(x=250, y=160, width=200)

entry_b = Entry(window, font=("Arial", 15, "bold"), show='*')
entry_b.place(x=250, y=200, width=200)

button_a = Button(window, text="Đăng nhập", font=("Arial", 12, "bold"), fg='Black', bg='#97CADB', command=login)
button_a.place(x=180, y=250, width=150, height=30)

button_exit = Button(window, text="Thoát", font=("Arial", 12), fg='Black', bg='red', command=exit_program)
button_exit.place(x=350, y=250, width=100, height=30)


window.mainloop()