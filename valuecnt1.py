#!/usr/bin/python

import csv
import datetime
#reader = csv.reader( open( 'sample.csv', 'rb'), delimiter=',' )
with open('sample.csv', 'rb') as f:
	reader = csv.reader(f)
	mylist = list(reader)
	
for row in mylist:
    print row
#print "Count for Mastercard : ", reader.count('Mastercard')
#print "Count for Visa : ", reader.count('Visa')