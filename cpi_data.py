#####################################################
#   0. 	Report information
py_script = 'cpi_data.py'

#####################################################
#   1.  Toggles | Flow Control | Errata
mess_base = """ <!DOCTYPE html><html><body><small> <p style="font-family: TimesNewRoman"> CPI Data Updated </p> </small> </body> </html>"""

#####################################################
#	2. 	Bring in the modules we will be using. Set proxies and descriptors
# 		connections | proxies | registrationkey agnostic
from pprint import pprint
import sys, os, requests, json, pandas as pd, time as t

import cx_Oracle
from datetime import datetime, date, time
with cx_Oracle.connect('x/x@x') as con:
	con.autocommit = True
	cur = con.cursor()

os.environ["HTTP_PROXY"] = 'http://@proxy.xxxx.xxx:8080'
os.environ["HTTPS_PROXY"] = 'https://@proxy.xxx.xxx:8080'
headers = {'Content-type': 'application/json'}

descriptors = [
('CUUR0000SETA','Vehicles','New and Used Motor Vehicles'),
('CUUR0000SETC','Vehicles','Motor Vehicle Parts and Equipment'),
('CUSR0000SETD','Vehicles','Motor Vehicle Maintenance and Repair'),
('CUSR0000SETA01','Vehicles','New Vehicles'),
('CUUR0000SETA02','Vehicles','Used Cars and Trucks'),
('CUSR0000SETB01','Vehicles','Gasoline'),
('CUUR0000SAM','Medical Care','Medical care commodities and medical care services'),
('CUUR0000SAM1','Medical Care Commodities','Prescription drugs, nonprescription over-the-counter-drugs, and other medical equipment and supplies'),
('CUUR0000SAM2','Medical Care Services','Professional medical services, hospital services, nursing home services, adult day care, and health insurance'),
('CUUR0000SEMD','Hospital and Related Services','Services provided to inpatients and outpatients. Includes emergency room visits, nursing home care and adult day care'),
('CUUR0000SS5702','Inpatient Services','Services for inpatients. Includes a mixture of itemized services, Diagnosis Related Group -based services, per diems, packages, or other bundled services.'),
('CUUR0000SS5703','Outpatient Services','Services provided to patients classified as outpatients in hospitals, free standing services facilities, ambulatory surgery, and urgent care centers.')
]

data = json.dumps({"seriesid": ['CUSR0000SETD','CUUR0000SETC','CUUR0000SETA','CUSR0000SETA01','CUUR0000SETA02','CUSR0000SETB01','CUUR0000SAM','CUUR0000SAM1','CUUR0000SAM2','CUUR0000SEMD','CUUR0000SS5702','CUUR0000SS5703'],"startyear":"2015", "endyear":"2019","registrationkey":"x"})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

data = []
def get_results():
	# pprint(json_data)
	load = t.strftime('%Y-%m-%d %H:%M:%S')
	for series in json_data['Results']['series']:
		seriesId = series['seriesID']
		for item in series['data']:
			rpt = seriesId
			year = item['year']
			period = item['period']
			value = item['value']
			rec = (rpt,year,period,value,load)
			data.append(rec)

#####################################################
#	4. 	Execute the pull
def get_data():
	get_results()
	labels = ['SERIES','YEAR','PERIOD','INDX_VALUE','LOAD']
	df = pd.DataFrame.from_records(data, columns=labels)
	df.to_csv('cpi_data.csv',header=True,index=False)

def get_desc():
	labels = ['SERIES','ITEM','DESC']
	df2 = pd.DataFrame.from_records(descriptors, columns=labels)
	df2.to_csv('cpi_desc.csv',header=True,index=False)

get_data()
get_desc()

#####################################################
#   5. communicate
def email_x():
	import sys
	if sys.platform == 'win32':
		trackspeed()
	else:
		sender = 'x.com'
		distro_list = """ x.com """
		import smtplib
		from email.mime.multipart import MIMEMultipart
		from email.mime.text import MIMEText
		SERVER = 'localhost'
		FROM = 'x.com'
		SUBJECT = 'CPI Data Updated'
		BODY =    mess_base
		msg = MIMEMultipart('alternative')
		msg['Subject'] = SUBJECT
		msg['From'] = sender
		msg['To'] = str(distro_list)
		part0 = MIMEText(BODY, 'html')
		msg.attach(part0)
		s = smtplib.SMTP(SERVER)
		s.sendmail(sender, distro_list.split(','), msg.as_string())
		s.quit()

email_x()

#####################################################
#   6. close out connections
cur.close()
con.close()