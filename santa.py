#! /usr/bin/env python
import yagmail
import json
import sys
import csv
from random import shuffle

with open('data.json') as f_data:
	data = json.load(f_data)

YAG = yagmail.SMTP(str(data["email"]), str(data["password"]))

def sendMail(name, otherName, email):
	txt="Hi %s,\nThis is Dan's secret santa script. Your assignment is %s. Try not to get something shitty!\n\nLove,\nRobot" % (name, otherName)
	YAG.send(email, "Secret santa assignment!!!111!!!", txt)

def csvParse(fName):
	with open(fName, 'r') as csvFile:
		reader = csv.reader(csvFile, delimiter=",")
		return [(row[1], row[2]) for row in reader]

def assign(users):
	shuf = list(users)
	shuffle(shuf)
	l = []
	for i in range(len(shuf)):
		nxt = i + 1 if i < len(shuf) - 1 else 0
		(name, email) = shuf[i]
		(nxtName, _) = shuf[nxt]
		l.append((name, nxtName, email))
	return l

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "How about you give me a CSV File"
		exit(1)
	users = csvParse(sys.argv[1])
	assignments = assign(users)
	for data in assignments:
		sendMail(*data)
