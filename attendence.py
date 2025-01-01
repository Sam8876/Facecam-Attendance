import xlwings as xw
#import camera
import json
#from camera import i
import xlwings as xw

wb = xw.Book("Attendence.xlsx")
sheet = wb.sheets["Attend"]
#xw.apps[xw.apps.keys()].books["Attendence.xlsx"]

def present(roll,name,i,date,time):
    sheet.range(f'D{i}').value = roll
    sheet.range(f'E{i}').value = name
    sheet.range(f'B{i}').value = date
    sheet.range(f'C{i}').value = time  



# def present(roll,name):
    

# present(48,"Sameer")
# print(js)