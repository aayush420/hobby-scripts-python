from openpyxl import load_workbook
import os

for i in os.listdir():
    if ".xlsx" in i:
        wb = load_workbook(i)
        wb['Dashboard']['C8'] = "___NEW_VALUE___"
        print(wb['Dashboard']['C8'].value)
        wb.save(i)
