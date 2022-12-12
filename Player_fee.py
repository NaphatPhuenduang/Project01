from tkinter import *

def submit():
    sum = int(transfer_fee.get()) + int(signing_fee.get()) + (int(wage.get()) * (int(stayed_year.get())*52))
    income = int(transfer_fee.get()) - ((int(transfer_fee.get()) / int(contact_year.get())) * int(stayed_year.get()))
    profit = int(selling_fee.get()) - income
    sale_on = int(selling_fee.get()) * (int(sale_on_clause.get()) / 100)
    
    sumLabel = Label(wd, text='sum: ' + str(sum), fg='red', font=('Helvetica', 12))
    sumLabel.place(x=240, y=280)
    profitLabel = Label(wd, text='profit: ' + str(profit), fg='red', font=('Helvetica', 12))
    profitLabel.place(x=240, y=320)
    saleLabel = Label(wd, text='sale on clause: ' + str(sale_on), fg='red', font=('Helvetica', 12))
    saleLabel.place(x=240, y=360)

wd = Tk()

contractYear = Label(wd, text='Contract year', fg='black', font=('Helvetica', 16))
contractYear.place(x=30, y=20)
contract_year = Entry(wd)
contract_year.place(x=30, y=60)

transferFee = Label(wd, text='Transfer fee', fg='black', font=('Helvetica', 16))
transferFee.place(x=240, y=20)
transfer_fee = Entry(wd)
transfer_fee.place(x=240, y=60)

saleOnClause = Label(wd, text='Sale on clause', fg='black', font=('Helvetica', 16))
saleOnClause.place(x=30, y=105)
sale_on_clause = Entry(wd)
sale_on_clause.place(x=30, y=145)

wagePerWeek = Label(wd, text='Wage per week', fg='black', font=('Helvetica', 16))
wagePerWeek.place(x=240, y=105)
wage = Entry(wd)
wage.place(x=240, y=145)

signingFee = Label(wd, text='Signing fee', fg='black', font=('Helvetica', 16))
signingFee.place(x=30, y=190)
signing_fee = Entry(wd)
signing_fee.place(x=30, y=230)

stayedYear = Label(wd, text='Stayed year', fg='black', font=('Helvetica', 16))
stayedYear.place(x=240, y=190)
stayed_year = Entry(wd)
stayed_year.place(x=240, y=230)

sellingFee = Label(wd, text='Selling fee', fg='black', font=('Helvetica', 16))
sellingFee.place(x=30, y=275)
selling_fee = Entry(wd)
selling_fee.place(x=30, y=315)

bt = Button(wd, text='Submit', font=('Helvetica', 14), command=submit)
bt.place(x=30, y=370)

wd.title('Expenses for player')
wd.geometry('460x430')
wd.mainloop()