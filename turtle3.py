from turtle import *

def trispiral(f):
	while f < 96:
		forward(f)
		left(120)
		return trispiral(f = f + 5)
	return raw_input("Press enter to terminate")

trispiral(10)