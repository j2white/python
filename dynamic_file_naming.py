import time as t

dynamic_report = 'My_Report_{m}.xlsx'

style1_date = t.strftime('%Y-%m-%d %H:%M:%S')
style1 = dynamic_report.format(m=style1_date)
print(style1)
# My_Report_2019-08-20 13:33:47.xlsx

style2_date = t.strftime('%Y_%m_%d %H_%M_%S')
style2 = dynamic_report.format(m=style2_date)
print(style2)
# My_Report_2019_08_20 13_33_47.xlsx

style3_date = t.strftime('%Y%m%d_%H%M%S')
style3 = dynamic_report.format(m=style3_date)
print(style3)
# My_Report_20190820_133347.xlsx

style4_date = t.strftime('%Y%m%d')
style4 = dynamic_report.format(m=style4_date)
print(style4)
# My_Report_20190820.xlsx





