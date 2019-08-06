def run_first_monday():
	''' calmonthrange returns a tupe of the first weekday of the month
		we will do a simple comparison of the numeric value of the current
		day to determine if it is a run date '''
	import calendar as cal
	from datetime import datetime, date, time
	d = int(datetime.now().strftime("%d"))
	m = int(datetime.now().strftime("%m"))
	y = int(datetime.now().strftime("%Y"))
	x = cal.monthrange(y,m)
	if x[0] == d:
		print('It is time to run!')
		pass
	else:
		print('It is not time to run.')
		raise SystemExit


run_first_monday()



