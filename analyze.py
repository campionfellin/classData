import csv
import sys


if len(sys.argv) == 1:
	print 'You\'re missing an argument...'
	print 'You need to give me either a class name or a class name and a teacher'
	print 'Here\'s an example command!'
	print 'python analyze.py \'CSE 142\' \'Reges\''
	quit()

className = sys.argv[1].lower()
if len(sys.argv) == 3:
	profe = sys.argv[2].lower()
else:
	profe = ''

with open('dataclasses.csv', 'rb') as f:
	reader = csv.reader(f)
	totAvg = 0
	numAvg = 0
	for row in reader:
		if row[2].lower().find(className) != -1 and row[4].lower().find(profe) != -1:
			print row[3] + "(" + row[2]  + ") taught by " + row[4] + " had an average grade of " + row[19] + " for the quarter of " + row[1][7:len(row[1])-1]
			print
			print
			totAvg = totAvg + float(row[19])
			numAvg = numAvg + 1

	s = "%3.2f" % (totAvg/numAvg)
	print "The average grade for this data is " + s