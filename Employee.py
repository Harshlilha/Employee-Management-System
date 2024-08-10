import tkinter as tk

# create a dictionary to store employee information
employee_db = {}

# define functions for each operation
def add_employee():
    id = txt_id.get()
    name = txt_name.get()
    phone = txt_phone.get()
    dob = txt_dob.get()
    gender = txt_gender.get()
    address = txt_address.get()
    email = txt_email.get()
    adharcard = txt_adharcard.get()
    qualification = txt_qualification.get()
    designation = txt_designation.get()
    doj = txt_doj.get()
    salary = txt_salary.get()

    employee_db[id] = {'Name':name , 'Phone':phone , 'DOB':dob , 'Gender':gender , 'Address':address , 'Email-ID':email , 'ADHAR CARD':adharcard , 'Qualification':qualification , 'Designation':designation , 'DOJ':doj , 'Salary':salary}

    txt_id.delete(0, tk.END)
    txt_name.delete(0, tk.END)
    txt_phone.delete(0, tk.END)
    txt_dob.delete(0, tk.END)
    txt_gender.delete(0, tk.END)
    txt_address.delete(0, tk.END)
    txt_email.delete(0, tk.END)
    txt_adharcard.delete(0, tk.END)
    txt_qualification.delete(0, tk.END)
    txt_designation.delete(0, tk.END)
    txt_doj.delete(0, tk.END)
    txt_salary.delete(0, tk.END)

def search_employee():
    id = txt_id.get()
    if id in employee_db:
        name = employee_db[id]['Name']
        phone = employee_db[id]['Phone']
        dob = employee_db[id]['DOB']
        gender= employee_db[id]['Gender']
        address = employee_db[id]['Address']
        email = employee_db[id]['Email-ID']
        adharcard = employee_db[id]['ADHAR CARD']
        qualification = employee_db[id]['Qualification']
        designation = employee_db[id]['Designation']
        doj = employee_db[id]['DOJ']
        salary = employee_db[id]['Salary']

        result_label.config(text=f"ID: {id} , Name: {name} , Phone: {phone} , DOB: {dob} , Gender: {gender} , Address: {address} , Email-ID: {email} , ADHAR CARD: {adharcard} ,Qualification: {qualification} , Designation: {designation} , DOJ: {doj} , Salary: {salary}")
    else:
        result_label.config(text=f"{id} not found in database")

def display_employee():
    result_label.config(text="")
    for id, info in employee_db.items():
        name = info['Name']
        phone = info['Phone']
        dob = info['DOB']
        gender = info['Gender']
        address = info['Address']
        email = info['Email-ID']
        adharcard = info['ADHAR CARD']
        qualification = info['Qualification']
        designation = info['Designation']
        doj = info['DOJ']
        salary = info['Salary']

        result_label.config(text=result_label.cget("text") + f"ID: {id} , Name: {name} , Phone: {phone} , DOB: {dob} , Gender: {gender} , Address: {address} , Email-ID: {email} , ADHAR CARD: {adharcard} , Qualification: {qualification} , Designation: {designation} , DOJ: {doj} , Salary: {salary} \n")

def delete_employee():
    id = txt_id.get()
    if id in employee_db:
        del employee_db[id]
        result_label.config(text=f"{id} deleted from database")
    else:
        result_label.config(text=f"{id} not found in database")

# create GUI using Tkinter
root = tk.Tk()
root.title("Employee Database")

lbl_title = tk.Label(root, text='EMPLOYEE MANAGEMENT SYSTEM', font=('Arial', 37, 'bold'), fg='dark blue', bg='white')
lbl_title.place(x=0, y=0, width=1530, height=50)

# Main frame
main_frame = tk.Frame(root, bd=2, bg='white')
main_frame.place(x=20, y=70, width=1490, height=700)

# upper frame
upper_frame = tk.LabelFrame(main_frame, bd=2, bg='white', text='Employee Information', font=('Arial', 11, 'bold'), fg='red')
upper_frame.place(x=20, y=10, width=1450, height=310)

# ID
lbl_id = tk.Label(upper_frame, font=('arial', 11, 'bold'), text='Employee ID:-', bg='white')
lbl_id.grid(row=0, column=0, padx=2, pady=7)

txt_id = tk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
txt_id.grid(row=0, column=1, padx=2, pady=7)

# Name
lbl_name = tk.Label(upper_frame, font=('arial', 11, 'bold'), text='Name            :-', bg='white')
lbl_name.grid(row=1, column=0, padx=2, pady=7)

txt_name = tk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
txt_name.grid(row=1, column=1, padx=2, pady=7)

# Phone No.
lbl_phone = tk.Label(upper_frame, font=('arial', 11, 'bold'), text='Phone No.   :-', bg='white')
lbl_phone.grid(row=2, column=0, padx=2, pady=7)

txt_phone = tk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
txt_phone.grid(row=2, column=1, padx=2, pady=7)

# DOB
lbl_dob = tk.Label(upper_frame, font=('arial', 11, 'bold'), text='DOB             :-', bg='white')
lbl_dob.grid(row=3, column=0, padx=2, pady=7)

txt_dob = tk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
txt_dob.grid(row=3, column=1, padx=2, pady=7)

# Gender
lbl_gender = tk.Label(upper_frame, font=('arial', 11, 'bold'), text='Gender        :-', bg='white')
lbl_gender.grid(row=4, column=0, padx=2, pady=7)

txt_gender = tk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
txt_gender.grid(row=4, column=1, padx=2, pady=7)

# Address
lbl_address = tk.Label(upper_frame, font=('arial', 11, 'bold'), text='Address       :-', bg='white')
lbl_address.grid(row=5, column=0, padx=2, pady=7)

txt_address = tk.Entry(upper_frame, width=22, font=('arial', 11, 'bold'))
txt_address.grid(row=5, column=1, padx=2, pady=7)

#blank
lbl_blank = tk.Label(upper_frame, font=('arial', 11, 'bold'), text='                              ', bg='white')
lbl_blank.grid(row=0, column=2, padx=2, pady=7)

# Email
lbl_email = tk.Label(upper_frame, font=('arial', 11, 'bold'), text='Email                            :-', bg='white')
lbl_email.grid(row=0, column=4, padx=2, pady=7)

txt_email = tk.Entry(upper_frame, width=30, font=('arial', 11, 'bold'))
txt_email.grid(row=0, column=5, padx=2, pady=7)

# Adhar Card
lbl_adharcard = tk.Label(upper_frame, font=('arial', 11, 'bold'), text='Adhar Card                  :-', bg='white')
lbl_adharcard.grid(row=1, column=4, padx=2, pady=7)

txt_adharcard = tk.Entry(upper_frame, width=30, font=('arial', 11, 'bold'))
txt_adharcard.grid(row=1, column=5, padx=2, pady=7)

# Qualification
lbl_qualification = tk.Label(upper_frame, font=('arial', 11, 'bold'), text='Detailed Qualification :-', bg='white')
lbl_qualification.grid(row=2, column=4, padx=2, pady=7)

txt_qualification = tk.Entry(upper_frame, width=30, font=('arial', 11, 'bold'))
txt_qualification.grid(row=2, column=5, padx=2, pady=7)

# Designation
lbl_designation = tk.Label(upper_frame, font=('arial', 11, 'bold'), text='Designation                  :-', bg='white')
lbl_designation.grid(row=3, column=4, padx=2, pady=7)

txt_designation = tk.Entry(upper_frame, width=30, font=('arial', 11, 'bold'))
txt_designation.grid(row=3, column=5, padx=2, pady=7)

# DOJ
lbl_doj = tk.Label(upper_frame, font=('arial', 11, 'bold'), text='Date Of Joining             :-', bg='white')
lbl_doj.grid(row=4, column=4, padx=2, pady=7)

txt_doj = tk.Entry(upper_frame, width=30, font=('arial', 11, 'bold'))
txt_doj.grid(row=4, column=5, padx=2, pady=7)

# Salary
lbl_salary = tk.Label(upper_frame, font=('arial', 11, 'bold'), text='Salary                             :-', bg='white')
lbl_salary.grid(row=5, column=4, padx=2, pady=7)

txt_salary = tk.Entry(upper_frame, width=30, font=('arial', 11, 'bold'))
txt_salary.grid(row=5, column=5, padx=2, pady=7)

# Button frame
button_frame = tk.Frame(upper_frame, bd=2, bg='white')
button_frame.place(x=1050, y=0, width=250, height=245)

#blank
lbl_blank = tk.Label(button_frame, font=('arial', 11, 'bold'), text='        ', bg='white')
lbl_blank.grid(row=0, column=0, padx=2, pady=7)

#ADD
add_button = tk.Button(button_frame, text="Add",command=add_employee,font=('arial', 14, 'bold'), width=20, bg='blue', fg='white')
add_button.grid(row=1, column=0, padx=0, pady=0)

#Search
search_button = tk.Button(button_frame, text="Search",command=search_employee,font=('arial', 14, 'bold'), width=20, bg='blue', fg='white')
search_button.grid(row=2, column=0, padx=0, pady=3)

#Display
display_button = tk.Button(button_frame, text="Display",command=display_employee,font=('arial', 14, 'bold'), width=20, bg='blue', fg='white')
display_button.grid(row=3, column=0, padx=0, pady=3)

#Delete
delete_button = tk.Button(button_frame, text="Delete",command=delete_employee,font=('arial', 14, 'bold'), width=20, bg='blue', fg='white')
delete_button.grid(row=4, column=0, padx=0, pady=3)

# down frame
down_frame = tk.LabelFrame(main_frame, bd=2, bg='white', text='Employee Information Table',font=('Arial', 11, 'bold'), fg='red')
down_frame.place(x=20, y=330, width=1450, height=320)

# result
result_label = tk.Label(down_frame, text="")
result_label.grid(row=0, column=0)

root.mainloop()
