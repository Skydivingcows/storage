#pip install pandas
#pip install xlrd
#python -m pip install --upgrade pip
import random
import datetime
import pandas as pd
now = datetime.datetime.now()
today = str(now.strftime("%A")).lower()
#print(now.strftime("%A")) # print the current day from system
day_lists = {
    "monday": ['m1','m2','m3'],
    "tuesday": ['t1','t2','t3'],
    "wednesday": ['w option1','w option2','w option3'],
    "thursday": ['th1','th2','th3'],
    "friday": ['f1','f2','f3'],
    "saturday": ['sa1','sa2','sa3'],
    "sunday": ['su1','su2','su3']}
day = random.choice(list(day_lists.keys())) # if you want a random day choice in list, keys on left values on right
choice = random.choice(day_lists[today]) # matches the system date to choice in list, change today to day if want all days random
#print(day) # prints the random day chosen in list
print(choice)
df = pd.read_excel('food_days.xlsx') # can also index sheet by name or fetch all sheets
mylist = df[today.title()].tolist()
# mylist = df['column name'].tolist()
print(mylist)
mychoice = random.choice(mylist)
print(mychoice)
