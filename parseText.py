import re
import operator

# Could add code to allow user to choose file

f = open('frankenstein.txt', encoding='utf-8')
contents = f.read()
parsed_file = re.findall(r"[-\w']+", contents)

# Dictionary for the words found in the file, as well as a count of how many times they appear
words = {}

for word in parsed_file:
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

# itemgetter(1) gets the second piece from each item, in this case the value		
sorted_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
print('\nThe three most common words are: ')
for term in range(0,3):
	print(sorted_words[term])
print('\n')

# Find the number of times the search term appears in the text
search_term = input('Please enter a search term from the text: ')
if search_term in words:
	print(words[search_term])
else:
	print(search_term + ' not found')