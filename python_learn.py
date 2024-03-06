def main():
	n = int(input("What's n? "))
	for s in sheep(n):
		print(s)

def sheep(n):
	flock = []
	for i in range(n):
		flock.append("O"*i)
	return flock

def sheep2(n):
	for i in range(n):
		yield "O"*i




if __name__ == '__main__':
	# main()
	pass