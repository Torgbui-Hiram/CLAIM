from tkinter import *
from tkinter import ttk
from webbrowser import get
from PIL import ImageTk
from tkinter import messagebox
import sqlite3


window = Tk()
window.title('IAS REQUEST FORM')
window.geometry('600x600+450+50')
window.resizable(0, 0)

request_date = StringVar()
team_leader = StringVar()
station_name = StringVar()
work_process1 = IntVar()
work_process2 = IntVar()
item = IntVar()
item_quantity = IntVar()
item_description = StringVar()
item_cost = DoubleVar()
total_cost = DoubleVar()
refrence_no = IntVar()
payment_type = StringVar()
payment_ref = StringVar()
authorised_by = StringVar()
signature = StringVar()
authorised_date = StringVar()
approved_lbl_en = StringVar()
approval_signature = StringVar()
approval_date_ent = StringVar()

# ==============Database=====================
con = sqlite3.connect("claim_db/claim_detail.db")
# ========== CREATING  TABLE IN DATABASE=====
cur = con.cursor()
# cur.execute("""CREATE TABLE claim_info (
#     REQUEST_DATE TEXT,
#     TEAM_LEADER TEXT,
#     STATION_NAME TEXT,
#     ITEM TEXT,
#     QUANTITY TEXT,
#     DESCRIPTION TEXT,
#     ITEM_COST TEXT,
#     TOTAL_COST TEXT,
#     REFRENCE_NO TEXT,
#     PAYMENT_TYPE TEXT,
#     PAYMENT_REF TEXT,
#     AUTHORISED_BY TEXT,
#     SIGNATURE TEXT,
#     AUTHORISED_DATE TEXT,
#     APPROVED_LBL TEXT,
#     APPROVAL_SIGNATURE TEXT,
#     APPROVAL_DATE TEXT
#     )""")
# con.commit()
# con.close()

# ============inserting data into database====

# ============ Functions ====================


def reset():
    request_date_entry.delete(0, END)
    team_leader_entry.delete(0, END)
    station_name_entry.delete(0, END)
    work_process1.get()
    work_process2.get()
    item_entry.delete(0, END)
    quantity_entry.delete(0, END)
    description_entry.delete(0, END)
    unit_cost_entry.delete(0, END)
    total_cost_entry.delete(0, END)
    refrence_no_entry.delete(0, END)
    payment_type_entry.delete(0, END)
    payment_ref_entry.delete(0, END)
    authorised_by_entry.delete(0, END)
    approval_signature_entry.delete(0, END)
    autorised_date_entry.delete(0, END)
    approved_lbl_entry.delete(0, END)
    approval_date_entry.delete(0, END)
    signature_entry.delete(0, END)


def cancel():
    if ".!button4":
        result = messagebox.askyesno(
            "CANCEL!", "Click Yes to cancel or No to continue")
        if result == True:
            window.destroy()
        else:
            pass


def extra():
    global item_gotten
    item_gotten = [item_entry.get(), quantity_entry.get(
    ), description_entry.get(), unit_cost_entry.get(), total_cost_entry.get()]

    # =======clear entry==========
    item_entry.delete(0, END)
    quantity_entry.delete(0, END)
    description_entry.delete(0, END)
    unit_cost_entry.delete(0, END)
    total_cost_entry.delete(0, END)

    print(item_gotten)


def tatal_cost(e):
    total_cost_entry.delete(0, END)
    a = item_quantity.get()
    b = item_cost.get()
    total = a*b
    total_cost_entry.insert(0, total)
    return total


def submit():
    cur.execute("INSERT INTO claim_info VALUES (:REQUEST_DATE,:TEAM_LEADER,:STATION_NAME,:ITEM,:QUANTITY,:DESCRIPTION,:ITEM_COST,:TOTAL_COST,:REFRENCE_NO,:PAYMENT_TYPE,:PAYMENT_REF,:AUTHORISED_BY,:SIGNATURE,:AUTHORISED_DATE,:APPROVED_LBL,:APPROVAL_SIGNATURE,:APPROVAL_DATE)",
                {
                    "REQUEST_DATE": request_date_entry.get(),
                    "TEAM_LEADER": team_leader_entry.get(),
                    "STATION_NAME": station_name_entry.get(),
                    "ITEM": item_entry.get(),
                    "QUANTITY": quantity_entry.get(),
                    "DESCRIPTION": description_entry.get(),
                    "ITEM_COST": item_entry.get(),
                    "TOTAL_COST": total_cost_entry.get(),
                    "REFRENCE_NO": refrence_no_entry.get(),
                    "PAYMENT_TYPE": payment_type_entry.get(),
                    "PAYMENT_REF": payment_ref_entry.get(),
                    "AUTHORISED_BY": authorised_by_entry.get(),
                    "SIGNATURE": authorised_by_entry.get(),
                    "AUTHORISED_DATE": autorised_date_entry.get(),
                    "APPROVED_LBL": approved_lbl_entry.get(),
                    "APPROVAL_SIGNATURE": approval_signature_entry.get(),
                    "APPROVAL_DATE": approval_date_entry.get()
                })
    con.commit()
    con.close()


# ===========================================
logo = ImageTk.PhotoImage(file="image\ias.png")
logo_img = Label(window, bd=0, image=logo)
logo_img.place(y=0, x=0)
main_lbl = Label(window, font=('impact', 19),
                 text=('PAYMENT REQUEST APP - MAINTENANCE'), foreground='#1A237E').place(x=165, y=35)
company_lbl = Label(window, font=('impact', 19),
                    text=('INDUSTRIAL AND ALLIED SERVICES'), foreground='#1A237E').place(x=200, y=0)

seperation = Frame(window, width=450, height=5, background='#E55247')
seperation.place(x=160, y=74)

date_lbl = Label(window, font=('impact', 12),
                 text=('DATE.'), foreground='black').place(x=415, y=105)
request_date_entry = ttk.Entry(
    window, textvariable=request_date, font=('Helvetica', 15, 'bold'))
request_date_entry.place(x=455, y=105, width=140)
request_date_entry.configure(background='white')

team_leader_lbl = Label(window, font=('impact', 12),
                        text=('TEAM LEADER:'), foreground='black').place(x=10, y=105)
team_leader_entry = ttk.Entry(
    window, textvariable=team_leader, font=('Helvetica', 15, 'bold'))
team_leader_entry.place(x=100, y=105)
team_leader_entry.configure(background='white')

preventative_lbl = Label(window, font=('impact', 12),
                         text=('STATION NAME:'), foreground='black').place(x=10, y=200)
station_name_entry = ttk.Entry(
    window, textvariable=station_name, font=('Helvetica', 15, 'bold'))
station_name_entry.place(x=120, y=200)
preventative_lbl = ttk.Label(window, font=('impact', 12),
                             text=('TYPE OF MAINTENANCE ACTIVITY:'), foreground='black').place(x=10, y=150)

corrective_check_box = ttk.Checkbutton(
    window, variable=work_process1, text='CORRECTIVE')
corrective_check_box.place(x=220, y=150)
preventive_check_box = ttk.Checkbutton(
    window, variable=work_process2, text='PREVENTATIVE')
preventive_check_box.place(x=330, y=150)
preventive_check_box.bind("<Button-1>")

item_lbl = Label(window, font=('impact', 12),
                 text=('ITEM'), foreground='black').place(x=10, y=260)
item_entry = ttk.Entry(window, textvariable=item,
                       font=('Helvetica', 15, 'bold'))
item_entry.place(x=5, y=290, width=50)
item_entry.configure(background='white')

quantity_lbl = Label(window, font=('impact', 12),
                     text=('QUANTITY'), foreground='black').place(x=75, y=260)
quantity_entry = ttk.Entry(
    window, textvariable=item_quantity, font=('Helvetica', 15, 'bold'))
quantity_entry.place(x=60, y=290, width=100)
quantity_entry.configure(background='white')
# ========================================================
descpription_lbl = Label(window, font=('impact', 12),
                         text=('DESCRIPTION'), foreground='black').place(x=190, y=260)
description_entry = ttk.Entry(
    window, textvariable=item_description, font=('Helvetica', 15, 'bold'))
description_entry.place(width=140, x=165, y=290)
description_entry.configure(background='white')

unit_cost_lbl = Label(window, font=('impact', 12),
                      text=('UNIT COST'), foreground='black').place(x=340, y=260)
unit_cost_entry = ttk.Entry(
    window, textvariable=item_cost, font=('Helvetica', 15, 'bold'))
unit_cost_entry.place(width=140, x=310, y=290)
unit_cost_entry.configure(background='white')

total_cost_lbl = Label(window, font=('impact', 12),
                       text=('TOTAL COST'), foreground='black').place(x=480, y=260)
total_cost_entry = ttk.Entry(
    window, textvariable=total_cost, font=('Helvetica', 15, 'bold'))
total_cost_entry.place(width=140, x=455, y=290)
total_cost_entry.configure(background='white')


# ============Action bindings===============
total_cost_entry.bind("<Button-1>", tatal_cost)


# ================== Reference column ====================
refrence_no_lbl = Label(window, font=('impact', 12),
                        text=('Ref No'), foreground='black').place(x=35, y=350)
refrence_no_entry = ttk.Entry(
    window, textvariable=refrence_no, font=('Helvetica', 15, 'bold'))
refrence_no_entry.place(width=70, x=85, y=350)
refrence_no_entry.insert(0, '#')

payment_type_lbl = Label(window, font=('impact', 12),
                         text=('Payment Type'), foreground='black').place(x=160, y=350)
payment_type_entry = ttk.Entry(
    window, textvariable=payment_type, font=('Helvetica', 15, 'bold'))
payment_type_entry.place(width=100, x=260, y=350)

payment_ref_lbl = Label(window, font=('impact', 12),
                        text=('Payment Ref'), foreground='black').place(x=385, y=350)
payment_ref_entry = ttk.Entry(
    window, textvariable=payment_ref, font=('Helvetica', 15, 'bold'))
payment_ref_entry.place(width=100, x=475, y=350)
payment_ref_entry.insert(0, '#')
# ===================== Authorised column =================
authorised_by_lbl = Label(window, font=('impact', 12),
                          text=('Authorised by'), foreground='black').place(x=25, y=390)
authorised_by_entry = ttk.Entry(
    window, textvariable=authorised_by, font=('Helvetica', 15, 'bold'))
authorised_by_entry.place(width=100, x=135, y=390)

signature_lbl = Label(window, font=('impact', 12),
                      text=('Signature'), foreground='black').place(x=245, y=390)
signature_entry = ttk.Entry(
    window, textvariable=signature, font=('Helvetica', 15, 'bold'))
signature_entry.place(width=100, x=315, y=390)

autorised_date_lbl = ttk.Label(window, font=('impact', 12),
                               text=('Date'), foreground='black').place(x=425, y=390)
autorised_date_entry = ttk.Entry(
    window, textvariable=authorised_date, font=('Helvetica', 15, 'bold'))
autorised_date_entry.place(width=100, x=475, y=390)
# =================== Approved column=====================
approved_lbl = ttk.Label(window, font=('impact', 12),
                         text=('Approved by'), foreground='black').place(x=25, y=430)
approved_lbl_entry = ttk.Entry(
    window, textvariable=approved_lbl_en, font=('Helvetica', 15, 'bold'))
approved_lbl_entry.place(width=100, x=135, y=430)

approval_signature_lbl = ttk.Label(window, font=('impact', 12),
                                   text=('Signature'), foreground='black').place(x=245, y=430)
approval_signature_entry = ttk.Entry(
    window, textvariable=approval_signature, font=('Helvetica', 15, 'bold'))
approval_signature_entry.place(width=100, x=315, y=430)

approval_date_lbl = ttk.Label(window, font=('impact', 12),
                              text=('Date'), foreground='black').place(x=425, y=430)
approval_date_entry = ttk.Entry(
    window, textvariable=approval_date_ent, font=('Helvetica', 15, 'bold'))
approval_date_entry.place(width=100, x=475, y=430)
# ================ Buttons For Action=================
submit_btn = ttk.Button(window, command=submit, text='SUBMIT', cursor='hand2')
submit_btn.place(x=500, y=500)

extra_btn = ttk.Button(window, command=extra, text='EXTRA', cursor='hand2')
extra_btn.place(x=415, y=500)

reset_btn = ttk.Button(window, command=reset, text='RESET', cursor='hand2')
reset_btn.place(x=330, y=500)

cancel_btn = ttk.Button(window, command=cancel, text='CANCEL', cursor='hand2')
cancel_btn.place(x=245, y=500)

# ================= Seperation Frame================

seperation_below_frame = Frame(
    window, width=600, height=50, background='white')
seperation_below_frame.place(x=0, y=550)

design_by_lbl = ttk.Label(seperation_below_frame, font=('Helvetiac', 12, 'bold'),
                          text=('By: ACTIVE-24/7 LTD.'), foreground='#1A237E', background='white').place(x=10, y=5)

phone_lbl_img = ImageTk.PhotoImage(file="image\icons8-telephone-24.png")
phone_contact_img = Label(seperation_below_frame, bd=0, image=phone_lbl_img)
phone_contact_img.place(y=10, x=520)

by_contact_lbl = ttk.Label(seperation_below_frame, font=('Helvetiac', 10, 'bold'),
                           text=('0548715522'), foreground='#1A237E', background='white').place(x=500, y=30)


window.mainloop()
