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
	highestNum = 0
	highestInfo = ""
	for row in reader:
		if row[2].lower().find(className) != -1 and row[4].lower().find(profe) != -1:
			print row[2]  + " taught by " + row[4][:row[4].find(",")] + " had an average grade of " + row[19] + " for the quarter of " + row[1][7:len(row[1])-1] + " out of " + row[5] + " students"
			print
			print
			if row[19] > highestNum:
				print "hihi"
				highestNum = row[19]
				highestInfo = row[2] + " in " + row[1][7:len(row[1])-1]
			totAvg = totAvg + float(row[19])
			numAvg = numAvg + 1

	s = "%3.2f" % (totAvg/numAvg)
	print "The class with the highest average of those you searched is " + highestInfo + " with an average grade of " + highestNum
	print "The average grade for this data is " + s
