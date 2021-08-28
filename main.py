def CostofItem():
    global priceofdrinks, priceofcakes, tt, priceoffood, cakesPrice, drinksPrice, foodPrice
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 \
            or var8.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or \
            var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var1.get() != 0 or var17.get() != 0 or \
            var18.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or \
            var25.get() != 0 or var26.get() != 0 or var27.get() != 0:
        item1 = float(e_lassi.get())
        item2 = float(e_rohhafza.get())
        item3 = float(e_jaljeera.get())
        item4 = float(e_shikanji.get())
        item5 = float(e_coldrinks.get())
        item6 = float(e_badammilk.get())
        item7 = float(e_coffee.get())
        item8 = float(e_masalachai.get())
        item9 = float(e_faluda.get())

        item10 = float(e_apple.get())
        item11 = float(e_pineapple.get())
        item12 = float(e_banana.get())
        item13 = float(e_brownie.get())
        item14 = float(e_chocolate.get())
        item15 = float(e_oreo.get())
        item16 = float(e_vanilla.get())
        item17 = float(e_blackforest.get())
        item18 = float(e_kikat.get())

        item19 = float(e_daal.get())
        item20 = float(e_roti.get())
        item21 = float(e_fish.get())
        item22 = float(e_sabji.get())
        item23 = float(e_chawal.get())
        item24 = float(e_mutton.get())
        item25 = float(e_chicken.get())
        item26 = float(e_paneer.get())
        item27 = float(e_kebab.get())

        priceofdrinks = (item1 * 40) + (item2 * 30) + (item3 * 20) + (item4 * 30) + (item5 * 60) + (item6 * 50) + (
                    item7 * 40) + (item8 * 20) + (item9 * 50)

        priceofcakes = (item10 * 350) + (item11 * 380) + (item12 * 400) + (item13 * 550) + (item14 * 600) + (
                    item15 * 500) + (
                               item16 * 400) + (item17 * 550) + (item18 * 480)

        priceoffood = (item19 * 45) + (item20 * 10) + (item21 * 120) + (item22 * 50) + (item23 * 30) + (
                item24 * 160) + (
                              item25 * 140) + (item26 * 110) + (item27 * 100)

        drinksPrice = f'Rs {round(priceofdrinks, 2)}'
        cakesPrice = f'Rs {round(priceofcakes, 2)}'
        foodPrice = f'Rs {round(priceoffood, 2)}'

        costofcakes.set(cakesPrice)
        costofdrinks.set(drinksPrice)
        costoffood.set(foodPrice)
        sc = 'Rs', str('%.2f' % (15.5))
        servicecharge.set(sc)

        subtotalOfItems = 'Rs', str('%.2f' % (priceofcakes + priceofdrinks + priceoffood))
        subtotal.set(subtotalOfItems)

        tc = 'Rs', str('%.2f' % (priceofcakes + priceofdrinks + priceoffood + 15.5))
        totalcost.set(tc)

    else:
        tkinter.messagebox.showerror('Error', 'No Item Is Selected')


def roti():
    if (var19.get() == 1):
        textroti.config(state=NORMAL)
        textroti.focus()
        textroti.delete(0, END)
        e_roti.set('')
    elif (var19.get() == 0):
        textroti.config(state=DISABLED)
        e_roti.set('0')


def daal():
    if (var20.get() == 1):
        textdaal.config(state=NORMAL)
        textdaal.focus()
        textdaal.delete(0, END)
        e_daal.set('')
    elif (var20.get() == 0):
        textdaal.config(state=DISABLED)
        e_daal.set('0')


def fish():
    if (var21.get() == 1):
        textFish.config(state=NORMAL)
        textFish.focus()
        textFish.delete(0, END)
        e_fish.set('')
    elif (var21.get() == 0):
        textFish.config(state=DISABLED)
        e_fish.set('0')


def sabji():
    if (var22.get() == 1):
        textsabji.config(state=NORMAL)
        textsabji.focus()
        textsabji.delete(0, END)
        e_sabji.set('')
    elif (var22.get() == 0):
        textsabji.config(state=DISABLED)
        e_sabji.set('0')


def kebab():
    if (var23.get() == 1):
        textKebab.config(state=NORMAL)
        textKebab.focus()
        textKebab.delete(0, END)
        e_kebab.set('')
    elif (var23.get() == 0):
        textKebab.config(state=DISABLED)
        e_kebab.set('0')


def chawal():
    if (var24.get() == 1):
        textchawal.config(state=NORMAL)
        textchawal.focus()
        textchawal.delete(0, END)
        e_chawal.set('')
    elif (var24.get() == 0):
        textchawal.config(state=DISABLED)
        e_chawal.set('0')


def mutton():
    if (var25.get() == 1):
        textMutton.config(state=NORMAL)
        textMutton.focus()
        textMutton.delete(0, END)
        e_mutton.set('')
    elif (var25.get() == 0):
        textMutton.config(state=DISABLED)
        e_mutton.set('0')


def paneer():
    if (var26.get() == 1):
        textpaneer.config(state=NORMAL)
        textpaneer.focus()
        textpaneer.delete(0, END)
        e_paneer.set('')
    elif (var26.get() == 0):
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')


def chicken():
    if (var27.get() == 1):
        textChiken.config(state=NORMAL)
        textChiken.focus()
        textChiken.delete(0, END)
        e_chicken.set('')
    elif (var27.get() == 0):
        textChiken.config(state=DISABLED)
        e_chicken.set('0')


def lassi():
    if (var1.get() == 1):
        textLassi.config(state=NORMAL)
        textLassi.focus()
        textLassi.delete(0, END)
        e_lassi.set('')
    elif (var1.get() == 0):
        textLassi.config(state=DISABLED)
        e_lassi.set('0')


def coffee():
    if (var2.get() == 1):
        textCoffee.config(state=NORMAL)
        textCoffee.focus()
        textCoffee.delete(0, END)
        e_coffee.set('')
    elif (var2.get() == 0):
        textCoffee.config(state=DISABLED)
        e_coffee.set('0')


def faluda():
    if (var3.get() == 1):
        textFaluda.config(state=NORMAL)
        textFaluda.focus()
        textFaluda.delete(0, END)
        e_faluda.set('')
    elif (var3.get() == 0):
        textFaluda.config(state=DISABLED)
        e_faluda.set('0')


def shikanji():
    if (var4.get() == 1):
        textShikanji.config(state=NORMAL)
        textShikanji.focus()
        textShikanji.delete(0, END)
        e_shikanji.set('')
    elif (var4.get() == 0):
        textShikanji.config(state=DISABLED)
        e_shikanji.set('0')


def jaljeera():
    if (var5.get() == 1):
        textJaljeera.config(state=NORMAL)
        textJaljeera.focus()
        textJaljeera.delete(0, END)
        e_jaljeera.set('')
    elif (var5.get() == 0):
        textJaljeera.config(state=DISABLED)
        e_jaljeera.set('0')


def roohafza():
    if (var6.get() == 1):
        textRohhafza.config(state=NORMAL)
        textRohhafza.focus()
        textRohhafza.delete(0, END)
        e_rohhafza.set('')
    elif (var6.get() == 0):
        textRohhafza.config(state=DISABLED)
        e_rohhafza.set('0')


def masalachai():
    if (var7.get() == 1):
        textMasalachai.config(state=NORMAL)
        textMasalachai.focus()
        textMasalachai.delete(0, END)
        e_masalachai.set('')
    elif (var7.get() == 0):
        textMasalachai.config(state=DISABLED)
        e_masalachai.set('0')


def badammilk():
    if (var8.get() == 1):
        textbadammilk.config(state=NORMAL)
        textbadammilk.focus()
        textbadammilk.delete(0, END)
        e_badammilk.set('')
    elif (var8.get() == 0):
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')


def coldrinks():
    if (var9.get() == 1):
        textColdrinks.config(state=NORMAL)
        textColdrinks.focus()
        textColdrinks.delete(0, END)
        e_coldrinks.set('')
    elif (var9.get() == 0):
        textColdrinks.config(state=DISABLED)
        e_coldrinks.set('0')


def kitkat():
    if (var10.get() == 1):
        textKitkat.config(state=NORMAL)
        textKitkat.focus()
        textKitkat.delete(0, END)
        e_kikat.set('')
    elif (var10.get() == 0):
        textKitkat.config(state=DISABLED)
        e_kikat.set('0')


def apple():
    if (var11.get() == 1):
        textApple.config(state=NORMAL)
        textApple.focus()
        textApple.delete(0, END)
        e_apple.set('')
    elif (var11.get() == 0):
        textApple.config(state=DISABLED)
        e_apple.set('0')


def vanilla():
    if (var12.get() == 1):
        textvanilla.config(state=NORMAL)
        textvanilla.focus()
        textvanilla.delete(0, END)
        e_vanilla.set('')
    elif (var12.get() == 0):
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')


def blackforest():
    if (var13.get() == 1):
        textBlackforest.config(state=NORMAL)
        textBlackforest.focus()
        textBlackforest.delete(0, END)
        e_blackforest.set('')
    elif (var13.get() == 0):
        textBlackforest.config(state=DISABLED)
        e_blackforest.set('0')


def banana():
    if (var14.get() == 1):
        textBanana.config(state=NORMAL)
        textBanana.focus()
        textBanana.delete(0, END)
        e_banana.set('')
    elif (var14.get() == 0):
        textBanana.config(state=DISABLED)
        e_banana.set('0')


def brownie():
    if (var15.get() == 1):
        textBrownie.config(state=NORMAL)
        textBrownie.focus()
        textBrownie.delete(0, END)
        e_brownie.set('')
    elif (var15.get() == 0):
        textBrownie.config(state=DISABLED)
        e_brownie.set('0')


def pineapple():
    if (var16.get() == 1):
        textpineapple.config(state=NORMAL)
        textpineapple.focus()
        textpineapple.delete(0, END)
        e_pineapple.set('')
    elif (var16.get() == 0):
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')


def chocolate():
    if (var17.get() == 1):
        textChocolate.config(state=NORMAL)
        textChocolate.focus()
        textChocolate.delete(0, END)
        e_chocolate.set('')
    elif (var17.get() == 0):
        textChocolate.config(state=DISABLED)
        e_chocolate.set('0')


def oreo():
    if (var18.get() == 1):
        textoreo.config(state=NORMAL)
        textoreo.focus()
        textoreo.delete(0, END)
        e_oreo.set('')
    elif (var18.get() == 0):
        textoreo.config(state=DISABLED)
        e_oreo.set('0')


def receipt():
    global priceofdrinks, priceoffood, priceofcakes
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 \
            or var8.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or \
            var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var1.get() != 0 or var17.get() != 0 or \
            var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or \
            var25.get() != 0 or var26.get() != 0 or var27.get() != 0:
        textReceipt.delete(1.0, END)
        x = random.randint(100, 10000)
        randomRef = str(x)
        receipt_ref.set('BILL  ' + randomRef)

        textReceipt.insert(END, 'Receipt Ref:\t\t' + receipt_ref.get() + '\t\t' + dateofOrder.get() + '\n')
        textReceipt.insert(END, '*********************************************************************\n')
        textReceipt.insert(END, 'Items:\t\t' + '   Cost of Items (in Rs) \n')
        textReceipt.insert(END, '********************************************************************\n')

        if e_daal.get() != '0':
            textReceipt.insert(END, f'Daal:\t\t\t{float(e_daal.get()) * 45}\n\n')

        if e_roti.get() != '0':
            textReceipt.insert(END, f'Roti:\t\t\t{float(e_roti.get()) * 10}\n\n')

        if e_chawal.get() != '0':
            textReceipt.insert(END, f'Chawal:\t\t\t{float(e_chawal.get()) * 30}\n\n')

        if e_sabji.get() != '0':
            textReceipt.insert(END, f'Sabji:\t\t\t{float(e_sabji.get()) * 50}\n\n')

        if e_fish.get() != '0':
            textReceipt.insert(END, f'Fish:\t\t\t{float(e_fish.get()) * 120}\n\n')

        if e_paneer.get() != '0':
            textReceipt.insert(END, f'Paneer:\t\t\t{float(e_paneer.get()) * 110}\n\n')

        if e_kebab.get() != '0':
            textReceipt.insert(END, f'Kabab:\t\t\t{float(e_kebab.get()) * 100}\n\n')

        if e_chicken.get() != '0':
            textReceipt.insert(END, f'Chicken:\t\t\t{float(e_chicken.get()) * 140}\n\n')

        if e_mutton.get() != '0':
            textReceipt.insert(END, f'Mutton:\t\t\t{float(e_mutton.get()) * 160}\n\n')

        if e_lassi.get() != '0':
            textReceipt.insert(END, f'Lassi:\t\t\t{float(e_lassi.get()) * 40}\n\n')
        if e_coffee.get() != '0':
            textReceipt.insert(END, f'Coffee:\t\t\t{float(e_coffee.get()) * 40}\n\n')
        if e_faluda.get() != '0':
            textReceipt.insert(END, f'Faluda:\t\t\t{float(e_faluda.get()) * 50}\n\n')
        if e_shikanji.get() != '0':
            textReceipt.insert(END, f'Shikanji:\t\t\t{float(e_shikanji.get()) * 30}\n\n')
        if e_jaljeera.get() != '0':
            textReceipt.insert(END, f'Jal-jeera:\t\t\t{float(e_jaljeera.get()) * 20}\n\n')
        if e_rohhafza.get() != '0':
            textReceipt.insert(END, f'Rooh Afza:\t\t\t{float(e_rohhafza.get()) * 30}\n\n')
        if e_masalachai.get() != '0':
            textReceipt.insert(END, f'Masala Chai:\t\t\t{float(e_masalachai.get()) * 20}\n\n')
        if e_badammilk.get() != '0':
            textReceipt.insert(END, f'Badam Milk:\t\t\t{float(e_badammilk.get()) * 50}\n\n')
        if e_coldrinks.get() != '0':
            textReceipt.insert(END, f'Cold Drink:\t\t\t{float(e_coldrinks.get()) * 60}\n\n')

        if e_kikat.get() != '0':
            textReceipt.insert(END, f'Kitkat Cake:\t\t\t{float(e_kikat.get()) * 480}\n\n')
        if e_apple.get() != '0':
            textReceipt.insert(END, f'Apple Cake:\t\t\t{float(e_apple.get()) * 350}\n\n')
        if e_vanilla.get() != '0':
            textReceipt.insert(END, f'Vanilla Cake:\t\t\t{float(e_vanilla.get()) * 400}\n\n')
        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'Black Forest Cake :\t\t\t{float(e_blackforest.get()) * 550}\n\n')
        if e_brownie.get() != '0':
            textReceipt.insert(END, f'Brownie Cake:\t\t\t{float(e_brownie.get()) * 550}\n\n')
        if e_banana.get() != '0':
            textReceipt.insert(END, f'Banana Cake:\t\t\t{float(e_banana.get()) * 400}\n\n')
        if e_pineapple.get() != '0':
            textReceipt.insert(END, f'Pineapple Cake:\t\t\t{float(e_pineapple.get()) * 380}\n\n')
        if e_chocolate.get() != '0':
            textReceipt.insert(END, f'Chocolate Cake:\t\t\t{float(e_chocolate.get()) * 600}\n\n')
        if e_oreo.get() != '0':
            textReceipt.insert(END, f'Oreo Cheesecake:\t\t\t{float(e_oreo.get()) * 500}\n\n')
        textReceipt.insert(END, '********************************************************************\n')
        if costofdrinks.get() != 'Rs 0.0':
            textReceipt.insert(END, f'Cost of Drinks:\t\t\t{priceofdrinks} Rs\n\n')
        if costofcakes.get() != 'Rs 0.0':
            textReceipt.insert(END, f'Cost of Cakes:\t\t\t{priceofcakes} Rs\n\n')
        if costoffood.get() != 'Rs 0.0':
            textReceipt.insert(END, f'Cost of Food:\t\t\t {priceoffood} Rs\n\n')
        textReceipt.insert(END, f'Sub Total:\t\t\t{(priceofcakes + priceofdrinks + priceoffood)} Rs\n\n')
        textReceipt.insert(END,
                           f'Service Charge:\t\t\t {15.5} Rs\n\nTotal Cost:\t\t\t{priceofdrinks + priceofcakes + priceoffood + 15.5} Rs\n\n')
        textReceipt.insert(END, '*********************************************************************')

    else:
        tkinter.messagebox.showerror('Error', 'No Item Is Selected')


def save():
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 \
            or var8.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or \
            var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var1.get() != 0 or var17.get() != 0 or \
            var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or \
            var25.get() != 0 or var26.get() != 0 or var27.get() != 0:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                       filetypes=(('Text File', '.txt'), ('All files', '*.*')))
        if url == None:
            return
        bill_data = textReceipt.get('1.0', END)
        url.write(bill_data)
        url.close()
    else:
        tkinter.messagebox.showerror('Error', 'Nothing To Save')


import random
import time
import datetime
from tkinter import *
from tkinter import filedialog
import requests

import tkinter.messagebox

root = Tk()
root.geometry('1350x710+0+0')
root.resizable(0, 0)
# root.overrideredirect(True)
root.title('Restaurant Management Systems')
root.config(bg='firebrick4')

tops = Frame(root, bg='firebrick4', bd=10, pady=5, relief=RIDGE)
tops.pack(side=TOP)
labelTitle = Label(tops, font=('arial', 30, 'bold'), text='Restaurant Management System', bd=9, width=53,
                   bg='red4', fg='yellow', justify=CENTER)
labelTitle.grid(row=0, column=0)

recieptcalc_frame = Frame(root, bg='red4', bd=15, relief=RIDGE)
recieptcalc_frame.pack(side=RIGHT)

buttonFrame = Frame(recieptcalc_frame, bg='red4', bd=3, relief=RIDGE)
buttonFrame.pack(side=BOTTOM)

calculatorFrame = Frame(recieptcalc_frame, bg='red4', bd=1, relief=RIDGE)
calculatorFrame.pack(side=TOP)

receiptFrame = Frame(recieptcalc_frame, bg='red4', bd=4, relief=RIDGE)
receiptFrame.pack(side=BOTTOM)

menuFrame = Frame(root, bg='firebrick4', bd=10, relief=RIDGE)
menuFrame.pack(side=LEFT)
costFrame = Frame(menuFrame, bg='firebrick4', bd=4, )
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame, text='Food', font=('arial', 19, 'bold'), fg='red4', bg='white', bd=10,
                       relief=RIDGE)
foodFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame, text='Drinks', font=('arial', 19, 'bold'), fg='red4', bg='white', bd=10,
                         relief=RIDGE)
drinksFrame.pack(side=LEFT)
cakeFrame = LabelFrame(menuFrame, bg='white', bd=10, text='Cakes', fg='red4', font=('arial', 19, 'bold'), relief=RIDGE)
cakeFrame.pack(side=RIGHT)

#############################Variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

dateofOrder = StringVar()
receipt_ref = StringVar()
costoffood = StringVar()
subtotal = StringVar()
totalcost = StringVar()
costofcakes = StringVar()
costofdrinks = StringVar()
servicecharge = StringVar()

text_input = StringVar()
operator = ''

e_daal = StringVar()
e_roti = StringVar()
e_sabji = StringVar()
e_chawal = StringVar()
e_fish = StringVar()
e_mutton = StringVar()
e_kebab = StringVar()
e_chicken = StringVar()
e_paneer = StringVar()

e_lassi = StringVar()
e_coffee = StringVar()
e_faluda = StringVar()
e_shikanji = StringVar()
e_jaljeera = StringVar()
e_rohhafza = StringVar()
e_masalachai = StringVar()
e_badammilk = StringVar()
e_coldrinks = StringVar()

e_kikat = StringVar()
e_vanilla = StringVar()
e_apple = StringVar()
e_blackforest = StringVar()
e_banana = StringVar()
e_brownie = StringVar()
e_pineapple = StringVar()
e_chocolate = StringVar()
e_oreo = StringVar()

e_daal.set('0')
e_roti.set('0')
e_sabji.set('0')
e_fish.set('0')
e_kebab.set('0')
e_chawal.set('0')
e_mutton.set('0')
e_chicken.set('0')
e_paneer.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_rohhafza.set('0')
e_shikanji.set('0')
e_jaljeera.set('0')
e_masalachai.set('0')
e_badammilk.set('0')
e_coldrinks.set('0')

e_kikat.set('0')
e_banana.set('0')
e_pineapple.set('0')
e_apple.set('0')
e_chocolate.set('0')
e_oreo.set('0')
e_blackforest.set('0')
e_brownie.set('0')
e_vanilla.set('0')

dateofOrder.set(time.strftime('%d/%m/%Y'))


#####################################Functions


def reset():
    e_daal.set('0')
    e_roti.set('0')
    e_sabji.set('0')
    e_fish.set('0')
    e_kebab.set('0')
    e_chawal.set('0')
    e_mutton.set('0')
    e_chicken.set('0')
    e_paneer.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_rohhafza.set('0')
    e_shikanji.set('0')
    e_jaljeera.set('0')
    e_masalachai.set('0')
    e_badammilk.set('0')
    e_coldrinks.set('0')

    e_kikat.set('0')
    e_banana.set('0')
    e_pineapple.set('0')
    e_apple.set('0')
    e_chocolate.set('0')
    e_oreo.set('0')
    e_blackforest.set('0')
    e_brownie.set('0')
    e_vanilla.set('0')

    costoffood.set('')
    subtotal.set('')
    totalcost.set('')
    costofcakes.set('')
    costofdrinks.set('')
    servicecharge.set('')
    textReceipt.delete(1.0, END)
    textMsg.delete(1.0, END)
    textNumber.delete(0, END)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)

    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    textdaal.config(state=DISABLED)
    textchawal.config(state=DISABLED)
    textroti.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textKebab.config(state=DISABLED)
    textChiken.config(state=DISABLED)
    textMutton.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textFish.config(state=DISABLED)

    textLassi.configure(state=DISABLED)
    textCoffee.config(state=DISABLED)
    textJaljeera.config(state=DISABLED)
    textRohhafza.config(state=DISABLED)
    textShikanji.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textMasalachai.config(state=DISABLED)
    textFaluda.config(state=DISABLED)
    textColdrinks.config(state=DISABLED)

    textvanilla.config(state=DISABLED)
    textoreo.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textApple.config(state=DISABLED)
    textKitkat.config(state=DISABLED)
    textBanana.config(state=DISABLED)
    textBlackforest.config(state=DISABLED)
    textBrownie.config(state=DISABLED)
    textChocolate.config(state=DISABLED)


def send():
    global textMsg, textNumber

    def send_sms(number, message):
        url = 'https://www.fast2sms.com/dev/bulk'
        params = {
            'authorization': 'here you have to add your own,ask me how to do it',
            'message': message,
            'numbers': number,
            'sender_id': 'FSTSMS',
            'route': 'p',
            'language': 'english'
        }
        response = requests.get(url, params=params)
        dic = response.json()
        print(dic)
        return dic.get('return')

    def btn_click():

        num = textNumber.get()
        msg = textMsg.get("1.0", END)
        r = send_sms(num, msg)
        if r:
            tkinter.messagebox.showinfo("Send Success", "Message successfully sent!")
        else:
            tkinter.messagebox.showerror("Error", "Something went wrong")

    root2 = Toplevel()
    root2.title("Send Bill")
    root2.config(bg='red4')
    root2.geometry("485x590+50+50")
    font = ("helvetica", 22, "bold")

    logo = PhotoImage(file='sender.png')
    label = Label(root2, image=logo, bg='red4')
    label.pack(pady=5)
    numberlabel = Label(root2, text='Mobile Number', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
    numberlabel.place(x=5, y=150)
    textNumber = Entry(root2, font=font, bd=5, width=32)
    textNumber.place(x=0, y=185)
    messagelabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
    messagelabel.place(x=5, y=250)
    textMsg = Text(root2, height=9, font=('times new roman', 14, 'bold'), bd=8,
                   relief=GROOVE, width=46)
    textMsg.place(x=4, y=285)

    textMsg.insert(END, 'Receipt Ref:\t\t' + receipt_ref.get() + '\t\t' + dateofOrder.get() + '\n\n')

    textMsg.insert(END, 'Items:\t\t' + '   Cost of Items (in Rs) \n\n')

    if e_daal.get() != '0':
        textMsg.insert(END, f'Daal:\t\t\t{float(e_daal.get()) * 45}\n')

    if e_roti.get() != '0':
        textMsg.insert(END, f'Roti:\t\t\t{float(e_roti.get()) * 10}\n')

    if e_chawal.get() != '0':
        textMsg.insert(END, f'Chawal:\t\t\t{float(e_chawal.get()) * 30}\n')

    if e_sabji.get() != '0':
        textMsg.insert(END, f'Sabji:\t\t\t{float(e_sabji.get()) * 50}\n')

    if e_fish.get() != '0':
        textMsg.insert(END, f'Fish:\t\t\t{float(e_fish.get()) * 120}\n')

    if e_paneer.get() != '0':
        textMsg.insert(END, f'Paneer:\t\t\t{float(e_paneer.get()) * 110}\n')

    if e_kebab.get() != '0':
        textMsg.insert(END, f'Kabab:\t\t\t{float(e_kebab.get()) * 100}\n')

    if e_chicken.get() != '0':
        textMsg.insert(END, f'Chicken:\t\t\t{float(e_chicken.get()) * 140}\n')

    if e_mutton.get() != '0':
        textMsg.insert(END, f'Mutton:\t\t\t{float(e_mutton.get()) * 160}\n')

    if e_lassi.get() != '0':
        textMsg.insert(END, f'Lassi:\t\t\t{float(e_lassi.get()) * 40}\n')
    if e_coffee.get() != '0':
        textMsg.insert(END, f'Coffee:\t\t\t{float(e_coffee.get()) * 40}\n')
    if e_faluda.get() != '0':
        textMsg.insert(END, f'Faluda:\t\t\t{float(e_faluda.get()) * 50}\n')
    if e_shikanji.get() != '0':
        textMsg.insert(END, f'Shikanji:\t\t\t{float(e_shikanji.get()) * 30}\n')
    if e_jaljeera.get() != '0':
        textMsg.insert(END, f'Jal-jeera:\t\t\t{float(e_jaljeera.get()) * 20}\n')
    if e_rohhafza.get() != '0':
        textMsg.insert(END, f'Rooh Afza:\t\t\t{float(e_rohhafza.get()) * 30}\n')
    if e_masalachai.get() != '0':
        textMsg.insert(END, f'Masala Chai:\t\t\t{float(e_masalachai.get()) * 20}\n')
    if e_badammilk.get() != '0':
        textMsg.insert(END, f'Badam Milk:\t\t\t{float(e_badammilk.get()) * 50}\n')
    if e_coldrinks.get() != '0':
        textMsg.insert(END, f'Cold Drink:\t\t\t{float(e_coldrinks.get()) * 60}\n')

    if e_kikat.get() != '0':
        textMsg.insert(END, f'Kitkat Cake:\t\t\t{float(e_kikat.get()) * 480}\n')
    if e_apple.get() != '0':
        textMsg.insert(END, f'Apple Cake:\t\t\t{float(e_apple.get()) * 350}\n')
    if e_vanilla.get() != '0':
        textMsg.insert(END, f'Vanilla Cake:\t\t\t{float(e_vanilla.get()) * 400}\n')
    if e_blackforest.get() != '0':
        textMsg.insert(END, f'Black Forest Cake :\t\t\t{float(e_blackforest.get()) * 550}\n')
    if e_brownie.get() != '0':
        textMsg.insert(END, f'Brownie Cake:\t\t\t{float(e_brownie.get()) * 550}\n')
    if e_banana.get() != '0':
        textMsg.insert(END, f'Banana Cake:\t\t\t{float(e_banana.get()) * 400}\n')
    if e_pineapple.get() != '0':
        textMsg.insert(END, f'Pineapple Cake:\t\t\t{float(e_pineapple.get()) * 380}\n')
    if e_chocolate.get() != '0':
        textMsg.insert(END, f'Chocolate Cake:\t\t\t{float(e_chocolate.get()) * 600}\n')
    if e_oreo.get() != '0':
        textMsg.insert(END, f'Oreo Cheesecake:\t\t\t{float(e_oreo.get()) * 500}\n')
    textMsg.insert(END, '\n')
    if costofdrinks.get() != 'Rs 0.0':
        textMsg.insert(END, f'Cost of Drinks:\t\t\t{priceofdrinks} Rs\n')
    if costofcakes.get() != 'Rs 0.0':
        textMsg.insert(END, f'Cost of Cakes:\t\t\t{priceofcakes} Rs\n')
    if costoffood.get() != 'Rs 0.0':
        textMsg.insert(END, f'Cost of Food:\t\t\t {priceoffood} Rs\n')
    textMsg.insert(END, '\n')
    textMsg.insert(END, f'Sub Total:\t\t\t{(priceofcakes + priceofdrinks + priceoffood)} Rs\n')
    textMsg.insert(END,
                   f'Service Charge:\t\t\t {15.5} Rs\nTotal Cost:\t\t\t{priceofdrinks + priceofcakes + priceoffood + 15.5} Rs\n')

    sendBtn = Button(root2, text="SEND", command=btn_click, bd=7, relief=GROOVE, bg='white', fg='black',
                     font=('arial', 19, 'bold'))
    sendBtn.place(x=150, y=525)

    root.mainloop()


##################################################Food
Roti = Checkbutton(foodFrame, text='Roti', variable=var19, onvalue=1, offvalue=0,
                   font=('arial', 18, 'bold')
                   , bg='white', command=roti).grid(row=0, sticky=W)

Daal = Checkbutton(foodFrame, text='Daal', variable=var20, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                   , bg='white', command=daal).grid(row=1, sticky=W)
Fish = Checkbutton(foodFrame, text='Fish', variable=var21, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                   , bg='white', command=fish).grid(row=2, sticky=W)
Sabji = Checkbutton(foodFrame, text='Sabji', variable=var22, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                    , bg='white', command=sabji).grid(row=3, sticky=W)
Kebab = Checkbutton(foodFrame, text='Kebab', variable=var23, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                    , bg='white', command=kebab).grid(row=4, sticky=W)
Chawal = Checkbutton(foodFrame, text='Chawal', variable=var24, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                     , bg='white', command=chawal).grid(row=5, sticky=W)

Mutton = Checkbutton(foodFrame, text='Mutton', variable=var25, onvalue=1, offvalue=0,
                     font=('arial', 18, 'bold')
                     , bg='white', command=mutton).grid(row=6, sticky=W)

Paneer = Checkbutton(foodFrame, text='Paneer', variable=var26, onvalue=1, offvalue=0,
                     font=('arial', 18, 'bold')
                     , bg='white', command=paneer).grid(row=7, sticky=W)

Chicken = Checkbutton(foodFrame, text='Chicken', variable=var27, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                      , bg='white', command=chicken).grid(row=8, sticky=W)

##################################################Food entry
textroti = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_roti, justify=LEFT,
                 state=DISABLED)
textroti.grid(row=0, column=1)
textdaal = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_daal, justify=LEFT,
                 state=DISABLED)
textdaal.grid(row=1, column=1)
textFish = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_fish, justify=LEFT,
                 state=DISABLED)
textFish.grid(row=2, column=1)
textsabji = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_sabji, justify=LEFT,
                  state=DISABLED)
textsabji.grid(row=3, column=1)
textKebab = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_kebab, justify=LEFT,
                  state=DISABLED)
textKebab.grid(row=4, column=1)
textchawal = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_chawal, justify=LEFT,
                   state=DISABLED)
textchawal.grid(row=5, column=1)
textMutton = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_mutton, justify=LEFT,
                   state=DISABLED)
textMutton.grid(row=6, column=1)

textpaneer = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_paneer, justify=LEFT,
                   state=DISABLED)
textpaneer.grid(row=7, column=1)

textChiken = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_chicken, justify=LEFT,
                   state=DISABLED)
textChiken.grid(row=8, column=1)

#################################Drinks############################

lassi = Checkbutton(drinksFrame, text='Lassi', variable=var1, onvalue=1, offvalue=0,
                    font=('arial', 18, 'bold')
                    , bg='white', command=lassi).grid(row=0, sticky=W)

coffee = Checkbutton(drinksFrame, text='Coffee', variable=var2, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                     , bg='white', command=coffee).grid(row=1, sticky=W)
faluda = Checkbutton(drinksFrame, text='Faluda', variable=var3, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                     , bg='white', command=faluda).grid(row=2, sticky=W)
shikanji = Checkbutton(drinksFrame, text='Shikanji', variable=var4, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                       , bg='white', command=shikanji).grid(row=3, sticky=W)
jaljeera = Checkbutton(drinksFrame, text='Jal-jeera', variable=var5, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                       , bg='white', command=jaljeera).grid(row=4, sticky=W)
roohafza = Checkbutton(drinksFrame, text='Rooh Afza', variable=var6, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                       , bg='white', command=roohafza).grid(row=5, sticky=W)

masalachai = Checkbutton(drinksFrame, text='Masala Tea', variable=var7, onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold')
                         , bg='white', command=masalachai).grid(row=6, sticky=W)

badammilk = Checkbutton(drinksFrame, text='Badam Milk', variable=var8, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                        , bg='white', command=badammilk).grid(row=7, sticky=W)
Coldrinks = Checkbutton(drinksFrame, text='Cold Drinks', variable=var9, onvalue=1, offvalue=0,
                        font=('arial', 18, 'bold')
                        , bg='white', command=coldrinks).grid(row=8, sticky=W)

##############################Textbox for drinks################################


textLassi = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_lassi, justify=LEFT,
                  state=DISABLED)
textLassi.grid(row=0, column=1)
textCoffee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_coffee, justify=LEFT,
                   state=DISABLED)
textCoffee.grid(row=1, column=1)
textFaluda = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_faluda, justify=LEFT,
                   state=DISABLED)
textFaluda.grid(row=2, column=1)
textShikanji = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_shikanji, justify=LEFT,
                     state=DISABLED)
textShikanji.grid(row=3, column=1)
textJaljeera = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_jaljeera, justify=LEFT,
                     state=DISABLED)
textJaljeera.grid(row=4, column=1)
textRohhafza = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_rohhafza, justify=LEFT,
                     state=DISABLED)
textRohhafza.grid(row=5, column=1)

textMasalachai = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_masalachai, justify=LEFT,
                       state=DISABLED)
textMasalachai.grid(row=6, column=1)
textbadammilk = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_badammilk, justify=LEFT,
                      state=DISABLED)
textbadammilk.grid(row=7, column=1)
textColdrinks = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_coldrinks, justify=LEFT,
                      state=DISABLED)
textColdrinks.grid(row=8, column=1)

######################Cakes#############################
kitkatcake = Checkbutton(cakeFrame, text='Kitkat ', variable=var10, onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold')
                         , bg='white', command=kitkat).grid(row=2, sticky=W)
applecake = Checkbutton(cakeFrame, text='Apple ', variable=var11, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                        , bg='white', command=apple).grid(row=1, sticky=W)
vanillacake = Checkbutton(cakeFrame, text='Vanilla ', variable=var12, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold')
                          , bg='white', command=vanilla).grid(row=3, sticky=W)
blackforest = Checkbutton(cakeFrame, text='Black Forest', variable=var13, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold')
                          , bg='white', command=blackforest).grid(row=8, sticky=W)
bananacake = Checkbutton(cakeFrame, text='Banana ', variable=var14, onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold')
                         , bg='white', command=banana).grid(row=4, sticky=W)
brownie = Checkbutton(cakeFrame, text='Brownie ', variable=var15, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                      , bg='white', command=brownie).grid(row=5, sticky=W)
pineapplecake = Checkbutton(cakeFrame, text='Pineapple ', variable=var16, onvalue=1, offvalue=0,
                            font=('arial', 18, 'bold')
                            , bg='white', command=pineapple).grid(row=6, sticky=W)
chocolatecake = Checkbutton(cakeFrame, text='Chocolate', variable=var17, onvalue=1, offvalue=0,
                            font=('arial', 18, 'bold')
                            , bg='white', command=chocolate).grid(row=7, sticky=W)

oreocheesecake = Checkbutton(cakeFrame, text='Oreo ', variable=var18, onvalue=1, offvalue=0,
                             font=('arial', 18, 'bold')
                             , bg='white', command=oreo).grid(row=0, sticky=W)

#########################textbox for cakes

textKitkat = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                   textvariable=e_kikat)
textKitkat.grid(row=2, column=1)
textApple = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_apple, justify=LEFT,
                  state=DISABLED)
textApple.grid(row=1, column=1)
textBlackforest = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_blackforest, justify=LEFT,
                        state=DISABLED)
textBlackforest.grid(row=8, column=1)
textBanana = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_banana, justify=LEFT,
                   state=DISABLED)
textBanana.grid(row=4, column=1)
textBrownie = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_brownie, justify=LEFT,
                    state=DISABLED)
textBrownie.grid(row=5, column=1)
textpineapple = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_pineapple, justify=LEFT,
                      state=DISABLED)
textpineapple.grid(row=6, column=1)
textChocolate = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_chocolate, justify=LEFT,
                      state=DISABLED)
textChocolate.grid(row=7, column=1)
textvanilla = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_vanilla, justify=LEFT,
                    state=DISABLED)
textvanilla.grid(row=3, column=1)
textoreo = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_oreo, justify=LEFT,
                 state=DISABLED)
textoreo.grid(row=0, column=1)

###########################Receipt

textReceipt = Text(receiptFrame, width=46, height=14, bg='white', bd=4, font=('arial', 12, 'bold'))
textReceipt.grid(row=0, column=0)

###############################Total costs

labelCostofDrinks = Label(costFrame, font=('arial', 16, 'bold'), text='Cost of Drinks\t',
                          bg='firebrick4', fg='cornsilk', justify=CENTER)
labelCostofDrinks.grid(row=0, column=0, sticky=W)

textcostofdrinks = Entry(costFrame, font=('arial', 16, 'bold'), bd=7, textvariable=costofdrinks, bg='white', width=14,
                         justify=RIGHT, state='readonly')
textcostofdrinks.grid(row=0, column=1)

labelCostofCake = Label(costFrame, font=('arial', 16, 'bold'), text='Cost of Cake\t',
                        bg='firebrick4', fg='cornsilk')
labelCostofCake.grid(row=1, column=0, sticky=W)

textcostofCake = Entry(costFrame, font=('arial', 16, 'bold'), bd=7, textvariable=costofcakes, bg='white', width=14,
                       justify=RIGHT, state='readonly')
textcostofCake.grid(row=1, column=1)

labelcostofFood = Label(costFrame, font=('arial', 16, 'bold'), text='Cost of Food\t',
                        bg='firebrick4', fg='cornsilk')
labelcostofFood.grid(row=2, column=0, sticky=W)

textcostofFood = Entry(costFrame, font=('arial', 16, 'bold'), bd=7, textvariable=costoffood, bg='white', width=14,
                       justify=RIGHT, state='readonly')
textcostofFood.grid(row=2, column=1)

#######################Payment Information
labelsubTotal = Label(costFrame, font=('arial', 16, 'bold'), text='    Sub Total\t',
                      bg='firebrick4', fg='cornsilk')
labelsubTotal.grid(row=0, column=2, sticky=W)

textsubTotal = Entry(costFrame, font=('arial', 16, 'bold'), bd=7, textvariable=subtotal, bg='white', width=14,
                     justify=RIGHT, state='readonly')
textsubTotal.grid(row=0, column=3)

labelServiceCharge = Label(costFrame, font=('arial', 16, 'bold'), text='    Service Charge\t',
                           bg='firebrick4', fg='cornsilk', justify=CENTER)
labelServiceCharge.grid(row=1, column=2, sticky=W)

textServiceCharge = Entry(costFrame, font=('arial', 16, 'bold'), bd=7, textvariable=servicecharge, bg='white', width=14,
                          justify=RIGHT, state='readonly')
textServiceCharge.grid(row=1, column=3)

labelTotalCost = Label(costFrame, font=('arial', 16, 'bold'), text='    Total Cost\t',
                       bg='firebrick4', fg='cornsilk')
labelTotalCost.grid(row=2, column=2, sticky=W)

textTotalCost = Entry(costFrame, font=('arial', 16, 'bold'), bd=7, textvariable=totalcost, bg='white', width=14,
                      justify=RIGHT, state='readonly')
textTotalCost.grid(row=2, column=3)

################Buttons

buttonTotal = Button(buttonFrame, padx=16, pady=1, bd=4, fg='white', font=('arial', 14, 'bold'), width=4, text='Total'
                     , bg='red4', command=CostofItem).grid(row=0, column=0)
buttonReceipt = Button(buttonFrame, padx=16, pady=1, bd=4, fg='white', font=('arial', 14, 'bold'), width=4,
                       text='Receipt'
                       , bg='red4', command=receipt).grid(row=0, column=1)

buttonSave = Button(buttonFrame, padx=16, pady=1, bd=4, fg='white', font=('arial', 14, 'bold'), width=4,
                    text='Save'
                    , bg='red4', command=save).grid(row=0, column=2)
buttonSend = Button(buttonFrame, padx=16, pady=1, bd=4, fg='white', font=('arial', 14, 'bold'), width=4,
                    text='Send'
                    , bg='red4', command=send).grid(row=0, column=3)

buttonReset = Button(buttonFrame, padx=16, pady=1, bd=4, fg='white', font=('arial', 14, 'bold'), width=4, text='Reset'
                     , bg='red4', command=reset).grid(row=0, column=4)


########################################Calculator Display################


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btnClear():
    global operator
    operator = ''
    text_input.set('')


def btnAnswer():
    try:
        global operator
        sumup = str(eval(operator))
        text_input.set(sumup)
        operator = ''
    except:
        pass


#########################Calculator

textDisplay = Entry(calculatorFrame, width=35, bg='white', bd=4, textvariable=text_input, font=('arial', 16, 'bold'),
                    justify=RIGHT)
textDisplay.grid(row=0, column=0, columnspan=4, pady=1)
textDisplay.insert(0, '0')

button7 = Button(calculatorFrame, padx=16, pady=1, bd=7, fg='yellow', font=('arial', 16, 'bold'), width=4, text='7'
                 , bg='red4', command=lambda: btnClick(7)).grid(row=2, column=0)

button8 = Button(calculatorFrame, padx=16, pady=1, bd=7, fg='yellow', font=('arial', 16, 'bold'), width=4, text='8'
                 , bg='red4', command=lambda: btnClick(8)).grid(row=2, column=1)

button9 = Button(calculatorFrame, padx=16, pady=1, bd=7, fg='yellow', font=('arial', 16, 'bold'), width=4, text='9'
                 , bg='red4', command=lambda: btnClick(9)).grid(row=2, column=2)

buttonAdd = Button(calculatorFrame, padx=16, pady=1, bd=7, fg='yellow', font=('arial', 16, 'bold'), width=4, text='+'
                   , bg='red4', command=lambda: btnClick('+')).grid(row=2, column=3)

button4 = Button(calculatorFrame, padx=16, pady=1, bd=7, fg='yellow', font=('arial', 16, 'bold'), width=4, text='4'
                 , bg='red4', command=lambda: btnClick(4)).grid(row=3, column=0)

button5 = Button(calculatorFrame, padx=16, pady=1, bd=7, bg='white', font=('arial', 16, 'bold'), width=4, text='5'
                 , fg='red4', command=lambda: btnClick(5)).grid(row=3, column=1)

button6 = Button(calculatorFrame, padx=16, pady=1, bd=7, bg='white', font=('arial', 16, 'bold'), width=4, text='6'
                 , fg='red4', command=lambda: btnClick(6)).grid(row=3, column=2)

buttonsub = Button(calculatorFrame, padx=16, pady=1, bd=7, fg='yellow', font=('arial', 16, 'bold'), width=4, text='-'
                   , bg='red4', command=lambda: btnClick('-')).grid(row=3, column=3)

button1 = Button(calculatorFrame, padx=16, pady=1, bd=7, fg='yellow', font=('arial', 16, 'bold'), width=4, text='1'
                 , bg='red4', command=lambda: btnClick(1)).grid(row=4, column=0)

button2 = Button(calculatorFrame, padx=16, pady=1, bd=7, bg='white', font=('arial', 16, 'bold'), width=4, text='2'
                 , fg='red4', command=lambda: btnClick(2)).grid(row=4, column=1)

button3 = Button(calculatorFrame, padx=16, pady=1, bd=7, bg='white', font=('arial', 16, 'bold'), width=4, text='3'
                 , fg='red4', command=lambda: btnClick(3)).grid(row=4, column=2)

buttonmult = Button(calculatorFrame, padx=16, pady=1, bd=7, fg='yellow', font=('arial', 16, 'bold'), width=4, text='*'
                    , bg='red4', command=lambda: btnClick('*')).grid(row=4, column=3)

buttonans = Button(calculatorFrame, padx=16, pady=1, bd=7, fg='yellow', font=('arial', 16, 'bold'), width=4, text='Ans'
                   , bg='red4', command=btnAnswer).grid(row=5, column=0)

buttonclear = Button(calculatorFrame, padx=16, pady=1, bd=7, fg='yellow', font=('arial', 16, 'bold'), width=4,
                     text='Clear'
                     , bg='red4', command=btnClear).grid(row=5, column=1)

button0 = Button(calculatorFrame, padx=16, pady=1, bd=7, fg='yellow', font=('arial', 16, 'bold'), width=4, text='0'
                 , bg='red4', command=lambda: btnClick(0)).grid(row=5, column=2)

buttondiv = Button(calculatorFrame, padx=16, pady=1, bd=7, fg='yellow', font=('arial', 16, 'bold'), width=4, text='/'
                   , bg='red4', command=lambda: btnClick('/')).grid(row=5, column=3)

root.mainloop()
