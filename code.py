import openpyxl as op
import pandas as pd 

gr1 = pd.read_excel('D:/temp/friends/MilenaKravchenko/group1.xlsx')
gr2 = pd.read_excel('D:/temp/friends/MilenaKravchenko/group2.xlsx')
gr3 = pd.read_excel('D:/temp/friends/MilenaKravchenko/group3.xlsx')

print(gr1)

print(gr2)

print(gr3)

name = input("Vvdedite im'ia")
dis  = input("Dis:")
wb = op.Workbook()
wb.create_sheet(title = 'Первый лист', index = 0)
sheet = wb['Первый лист']
sheet['A1'] = 'ФИО'
sheet['B1'] = 'Дисциплина'
sheet['A2'] = name 
sheet['B2'] = dis

wb.save('D:/temp/friends/MilenaKravchenko/disnst.xlsx')

kk = pd.read_excel('D:/temp/friends/MilenaKravchenko/disnst.xlsx')

print(kk)
