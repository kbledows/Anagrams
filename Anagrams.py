#Program written to solve Anagram

validWords = set()
validAnagrams = set()

#Takes input from user and calls findValidWords and recursiveAnagrams
def main():
	print("Please enter the 6 letters to begin generating words.")
	print("SEPERATE LETTERS WITH SPACES")

	letters = input().split() #list of letters
	print("Your chosen letters are: " + str(letters))
	findValidWords()
	recursiveAnagrams(letters,"")
	num = len(validAnagrams)
	print("Program found " + str(num) + " valid anagrams.")
	validAnagramsList = list(validAnagrams)
	validAnagramsList.sort(key=len)
	print(str(list(validAnagramsList)))

#Populates the set with valid words (len 3 to 6)
def findValidWords():
	words = open("letters10.txt","r")
	for word in words:
		if (3 <= len(word.rstrip()) <= 6):
			validWords.add(word.rstrip())

#recusrive function to check validity of possible anagram
def recursiveAnagrams(letters, possibleAnagram):
	#If anagram is valid, add to validAnagrams (base case)
	if possibleAnagram in validWords:
		validAnagrams.add(possibleAnagram)

	for letter in letters:
		temp = letters.copy()
		strTemp = possibleAnagram + letter
		temp.remove(letter)
		recursiveAnagrams(temp,strTemp)

if __name__ == '__main__':
	main()

