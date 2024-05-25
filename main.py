from tkinter import*

#Main Window
root = Tk()
root.geometry('980x600+0+0')
root.resizable(0,0)
root.title('Restaurant Managment')
root.config(bg='firebrick4')

#All Frames
topFrame = Frame(root, bd=10, relief=RIDGE)
topFrame.pack(side=TOP)
labelTitle = Label(topFrame, text='Restaurant Management System',
font=('arial',30,'bold'), fg='yellow',bd=9,bg='red4', width=39)
labelTitle.grid(row=0, column=0)

#Menu Frame

menuFrame = Frame(root, bd=10, relief=RIDGE, bg='firebrick4')
menuFrame.pack(side=LEFT)
#Cost frame
costFrame = Frame(menuFrame, bd=4, relief=RIDGE, 
                  bg='firebrick4', pady=10)
costFrame.pack(side=BOTTOM) 

#Food Frame
foodFrame=LabelFrame(menuFrame,text='Food',
    font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
foodFrame.pack(side=LEFT)

#Drinks Frame
drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
drinksFrame.pack(side=LEFT)

#Cake Frame
cakesFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
cakesFrame.pack(side=LEFT)

#RightFrame
rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

#CalculatorFrame
calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

#ButtonFrame
buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()



#variable
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

#variable input for Input field
e_ruti = StringVar()
e_dal = StringVar()
e_fish = StringVar()
e_Sabji = StringVar()
e_kebab = StringVar()
e_chawal = StringVar()
e_Mutton = StringVar()
e_Paneer = StringVar()
e_Chicken = StringVar()
e_Lassi = StringVar()
e_Coffee = StringVar()
e_Faluda= StringVar()
e_Shikanji = StringVar()
e_Jaljeera= StringVar()
e_Roohafza = StringVar()
e_Masala = StringVar()
e_BadamMilk = StringVar()
e_ColdDrinks = StringVar()
e_oreo = StringVar()
e_Apple = StringVar()
e_Kitkat =StringVar()
e_Vanilla = StringVar()
e_Banana = StringVar()
e_Pineapple = StringVar()
e_Chocolate = StringVar()
e_Brownie = StringVar()
e_BlackForest = StringVar()








#Default value for Input Field
e_ruti.set('0')
e_dal.set('0')
e_fish.set('0')
e_Sabji.set('0')
e_kebab.set('0')
e_chawal.set('0')
e_Mutton.set('0')
e_Paneer.set('0')
e_Chicken.set('0')
e_Lassi.set('0')
e_Coffee.set('0')
e_Faluda.set('0')
e_Shikanji.set('0')
e_Jaljeera.set('0')
e_Roohafza.set('0')
e_Masala.set('0')
e_BadamMilk.set('0')
e_ColdDrinks.set('0')
e_oreo.set('0')
e_Apple.set('0')
e_Kitkat.set('0')
e_Vanilla.set('0')
e_Banana.set('0')
e_Pineapple.set('0')
e_Chocolate.set('0')
e_Brownie.set('0')
e_BlackForest.set('0')



#Food Frame
ruti=Checkbutton(foodFrame,text='Ruti',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var1,command="")
ruti.grid(row=1,column=0,sticky=W)

dal=Checkbutton(foodFrame,text='dal',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var2,command="")
dal.grid(row=2,column=0,sticky=W)

fish=Checkbutton(foodFrame,text='fish',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var3,command="")
fish.grid(row=3,column=0,sticky=W)

Sabji=Checkbutton(foodFrame,text='Sabji',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var4,command="")
Sabji.grid(row=4,column=0,sticky=W)

kebab=Checkbutton(foodFrame,text='kebab',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var5,command="")
kebab.grid(row=5,column=0,sticky=W)

chawal=Checkbutton(foodFrame,text='chawal',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var6,command="")
chawal.grid(row=6,column=0,sticky=W)

Mutton=Checkbutton(foodFrame,text='Mutton',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var7,command="")
Mutton.grid(row=7,column=0,sticky=W)

Paneer=Checkbutton(foodFrame,text='Paneer',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var8,command="")
Paneer.grid(row=8,column=0,sticky=W)

Chicken=Checkbutton(foodFrame,text='Chicken',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var9,command="")
Chicken.grid(row=9,column=0,sticky=W)


#Food Entry Field
textruti = Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_ruti)
textruti.grid(row=1,column=1)

textdal = Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_dal)
textdal.grid(row=2,column=1)

textfish = Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_fish)
textfish.grid(row=3,column=1)

textSabji = Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Sabji)
textSabji.grid(row=4,column=1)

textkebab = Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_kebab)
textkebab.grid(row=5,column=1)

textchawal = Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_chawal)
textchawal.grid(row=6,column=1)

textMutton = Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Mutton)
textMutton.grid(row=7,column=1)

textPaneer = Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Paneer)
textPaneer.grid(row=8,column=1)

textChicken = Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Chicken)
textChicken.grid(row=9,column=1)



#Drinks Frame
Lassi=Checkbutton(drinksFrame,text='Lassi',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var10,command="")
Lassi.grid(row=0,column=1,sticky=W)

Coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var11,command="")
Coffee.grid(row=1,column=1,sticky=W)

Faluda=Checkbutton(drinksFrame,text='Faluda',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var12,command="")
Faluda.grid(row=2,column=1,sticky=W)

Shikanji=Checkbutton(drinksFrame,text='Shikanji',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var13,command="")
Shikanji.grid(row=3,column=1,sticky=W)

Jaljeera=Checkbutton(drinksFrame,text='Jaljeera',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var14,command="")
Jaljeera.grid(row=4,column=1,sticky=W)

Roohafza=Checkbutton(drinksFrame,text='Roohafza',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var15,command="")
Roohafza.grid(row=5,column=1,sticky=W)

Masala=Checkbutton(drinksFrame,text='Masala',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var16,command="")
Masala.grid(row=6,column=1,sticky=W)

BadamMilk=Checkbutton(drinksFrame,text='Badam Milk',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var17,command="")
BadamMilk.grid(row=7,column=1,sticky=W)

ColdDrinks=Checkbutton(drinksFrame,text='Cold Drinks',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var18,command="")
ColdDrinks.grid(row=8,column=1,sticky=W)

#Drinks Entry Field

textLassi = Entry(drinksFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Lassi)
textLassi.grid(row=0,column=2)

textCoffee = Entry(drinksFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Coffee)
textCoffee.grid(row=1,column=2)

textFaluda = Entry(drinksFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Faluda)
textFaluda.grid(row=2,column=2)

textShikanji = Entry(drinksFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Shikanji)
textShikanji.grid(row=3,column=2)

textJaljeera = Entry(drinksFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Jaljeera)
textJaljeera.grid(row=4,column=2)

textRoohafza = Entry(drinksFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Roohafza)
textRoohafza.grid(row=5,column=2)

textMasala = Entry(drinksFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Masala)
textMasala.grid(row=6,column=2)

textBadamMilk = Entry(drinksFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_BadamMilk)
textBadamMilk.grid(row=7,column=2)

textColdDrinks = Entry(drinksFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_ColdDrinks)
textColdDrinks.grid(row=8,column=2)


#Cakes Frame
oreo=Checkbutton(cakesFrame,text=' oreo',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var19,command="")
oreo.grid(row=0,column=2,sticky=W)

Apple=Checkbutton(cakesFrame,text='Apple',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var20,command="")
Apple.grid(row=1,column=2,sticky=W)

Kitkat=Checkbutton(cakesFrame,text='Kitkat',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var21,command="")
Kitkat.grid(row=2,column=2,sticky=W)

Vanilla=Checkbutton(cakesFrame,text='Vanilla',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var22,command="")
Vanilla.grid(row=3,column=2,sticky=W)

Banana=Checkbutton(cakesFrame,text='Banana',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var23,command="")
Banana.grid(row=4,column=2,sticky=W)

Pineapple=Checkbutton(cakesFrame,text='Pineapple',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var24,command="")
Pineapple.grid(row=5,column=2,sticky=W)

Chocolate=Checkbutton(cakesFrame,text='Chocolate',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var25,command="")
Chocolate.grid(row=6,column=2,sticky=W)

Brownie=Checkbutton(cakesFrame,text='Brownie',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var26,command="")
Brownie.grid(row=7,column=2,sticky=W)

BlackForest=Checkbutton(cakesFrame,text='Black Forest',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var27,command="")
BlackForest.grid(row=8,column=2,sticky=W)

#Cakes Entry Field

textoreo = Entry(cakesFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_oreo)
textoreo.grid(row=0,column=3)

textApple = Entry(cakesFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Apple)
textApple.grid(row=1,column=3)

textKitkat = Entry(cakesFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Kitkat)
textKitkat.grid(row=2,column=3)

textVanilla = Entry(cakesFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Vanilla)
textVanilla.grid(row=3,column=3)

textBanana = Entry(cakesFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Banana)
textBanana.grid(row=4,column=3)

textPineapple = Entry(cakesFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Pineapple)
textPineapple.grid(row=5,column=3)

textChocolate = Entry(cakesFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Chocolate)
textChocolate.grid(row=6,column=3)

textBrownie = Entry(cakesFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_Brownie)
textBrownie.grid(row=7,column=3)

textBlackForest = Entry(cakesFrame, font=('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_BlackForest)
textBlackForest.grid(row=8,column=3)

#CostLabels entry feild

LabelCostoffood =Label(costFrame,text="cost of Food",font=('arial',18,'bold'),bg='firebrick4', fg='white')
LabelCostoffood.grid(row=0,column=0)

textcostoffood =Entry (costFrame,font=('arial',18,'bold'),bd=7,width=6)
textcostoffood.grid(row=0,column=1)

LabelCostoffood =Label(costFrame,text="cost of Drinks",font=('arial',18,'bold'),bg='firebrick4', fg='white')
LabelCostoffood.grid(row=1,column=0)

textcostoffood =Entry (costFrame,font=('arial',18,'bold'),bd=7,width=6)
textcostoffood.grid(row=1,column=1)


LabelCostoffood =Label(costFrame,text="cost of Cakes",font=('arial',18,'bold'),bg='firebrick4', fg='white')
LabelCostoffood.grid(row=2,column=0)

textcostoffood =Entry (costFrame,font=('arial',18,'bold'),bd=7,width=6)
textcostoffood.grid(row=2,column=1)




root.mainloop()