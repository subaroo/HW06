#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body

def has_no_e(word):
	'''
	Test if a word contains the letter "e"
	'''
	if 'e' in word:
		return False
	else:
		return True



def read_text_file():
	'''
	In a given set of words find all words that do not contain 'e'.
	Calculate that percentage of words as a part of the given set.
	'''
	count_no_e = 0
	total_words = 0
	fin = open("words.txt")
	for line in fin:
		total_words += 1
		word = line.strip()
		if has_no_e(word):
			print(word + "\n")
			count_no_e += 1
	fin.close
	percentage = (float(count_no_e)/total_words) * 100
	print("The percentage of words with no 'e' is: " + str(percentage))

		




##############################################################################
def main():
    read_text_file()

if __name__ == '__main__':
    main()


