from tkinter import *
from tkinter import ttk
import pandas as pd
from PIL import ImageTk
# db = open('info.txt', 'r')
# db = open('info.txt', 'a')
# vals = db.write(f'{user}, {password}\n')

# data = dict(zip(user, password))

window = Tk()
window.title('IAS REQUEST FORM')
window.geometry('600x600+450+50')
window.resizable(0, 0)
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
request_date_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
request_date_entry.place(x=455, y=105, width=140)
request_date_entry.configure(background='white')

team_leader_lbl = Label(window, font=('impact', 12),
                        text=('TEAM LEADER:'), foreground='black').place(x=10, y=105)
team_leader_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
team_leader_entry.place(x=100, y=105)
team_leader_entry.configure(background='white')

preventative_lbl = Label(window, font=('impact', 12),
                         text=('STATION NAME:'), foreground='black').place(x=10, y=200)
station_name_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
station_name_entry.place(x=120, y=200)
preventative_lbl = ttk.Label(window, font=('impact', 12),
                             text=('TYPE OF MAINTENANCE ACTIVITY:'), foreground='black').place(x=10, y=150)

corrective_check_box = ttk.Checkbutton(window, text='CORRECTIVE')
corrective_check_box.place(x=220, y=150)
corrective_check_box = ttk.Checkbutton(window, text='PREVENTATIVE')
corrective_check_box.place(x=330, y=150)

item_lbl = Label(window, font=('impact', 12),
                 text=('ITEM'), foreground='black').place(x=10, y=260)
item_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
item_entry.place(x=5, y=290, width=50)
item_entry.configure(background='white')

quantity_lbl = Label(window, font=('impact', 12),
                     text=('QUANTITY'), foreground='black').place(x=75, y=260)
quantity_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
quantity_entry.place(x=60, y=290, width=100)
quantity_entry.configure(background='white')
# ========================================================
descpription_lbl = Label(window, font=('impact', 12),
                         text=('DESCRIPTION'), foreground='black').place(x=190, y=260)
description_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
description_entry.place(width=140, x=165, y=290)
description_entry.configure(background='white')

unit_cost_lbl = Label(window, font=('impact', 12),
                      text=('UNIT COST'), foreground='black').place(x=340, y=260)
unit_cost_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
unit_cost_entry.place(width=140, x=310, y=290)
unit_cost_entry.configure(background='white')

total_cost_lbl = Label(window, font=('impact', 12),
                       text=('TOTAL COST'), foreground='black').place(x=480, y=260)
total_cost_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
total_cost_entry.place(width=140, x=455, y=290)
total_cost_entry.configure(background='white')
# ================== Reference column ====================
refrence_no_lbl = Label(window, font=('impact', 12),
                        text=('Ref No'), foreground='black').place(x=35, y=350)
refrence_no_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
refrence_no_entry.place(width=50, x=85, y=350)

payment_type_lbl = Label(window, font=('impact', 12),
                         text=('Payment Type'), foreground='black').place(x=160, y=350)
payment_type_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
payment_type_entry.place(width=100, x=260, y=350)

payment_ref_lbl = Label(window, font=('impact', 12),
                        text=('Payment Ref'), foreground='black').place(x=385, y=350)
payment_ref_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
payment_ref_entry.place(width=100, x=475, y=350)
# ===================== Authorised column =================
authorised_by_lbl = Label(window, font=('impact', 12),
                          text=('Authorised by'), foreground='black').place(x=25, y=390)
authorised_by_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
authorised_by_entry.place(width=100, x=135, y=390)

signature_lbl = Label(window, font=('impact', 12),
                      text=('Signature'), foreground='black').place(x=245, y=390)
signature_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
signature_entry.place(width=100, x=315, y=390)

autorised_date_lbl = ttk.Label(window, font=('impact', 12),
                               text=('Date'), foreground='black').place(x=425, y=390)
autorised_date_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
autorised_date_entry.place(width=100, x=475, y=390)
# =================== Approved column=====================
approved_lbl = ttk.Label(window, font=('impact', 12),
                         text=('Approved by'), foreground='black').place(x=25, y=430)
approved_lbl_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
approved_lbl_entry.place(width=100, x=135, y=430)

approval_signature_lbl = ttk.Label(window, font=('impact', 12),
                                   text=('Signature'), foreground='black').place(x=245, y=430)
approval_signature_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
approval_signature_entry.place(width=100, x=315, y=430)

approval_date_lbl = ttk.Label(window, font=('impact', 12),
                              text=('Date'), foreground='black').place(x=425, y=430)
approval_date_entry = ttk.Entry(window, font=('Helvetica', 15, 'bold'))
approval_date_entry.place(width=100, x=475, y=430)
# ================ Buttons For Action=================
submit_btn = ttk.Button(window, text='SUBMIT', cursor='hand2')
submit_btn.place(x=500, y=500)

extra_btn = ttk.Button(window, text='EXTRA', cursor='hand2')
extra_btn.place(x=415, y=500)

reset_btn = ttk.Button(window, text='RESET', cursor='hand2')
reset_btn.place(x=330, y=500)

cancel_btn = ttk.Button(window, text='CANCEL', cursor='hand2')
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
