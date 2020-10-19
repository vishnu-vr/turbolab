def find_sum(inp):
	if len(inp) % 2 != 0:
		return 0

	inp = inp.lower()

	# alpha - number dictionary
	alpha = dict(zip([i for i in "abcdefghijklmnopqrstuvwxyz"],[i for i in range(26)]))

	mid = int(len(inp)/2)

	first = inp[:mid]
	first = first[::-1]


	second = inp[mid:]
	second = second[::-1]

	s1 = 0
	s2 = 0
	for i in range(len(first)):
		encoding = alpha[first[i]]
		s1 += encoding * pow(26,i)


	for i in range(len(second)):
		encoding = alpha[second[i]]
		s2 += encoding * pow(26,i)

	return (s1+s2)

if __name__ == '__main__':
	inp = input()
	print(find_sum(inp))


