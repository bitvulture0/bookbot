def get_num_words(book_text):
	words = book_text.split()
	num_words = 0
	for word in words:
		if True:
			num_words += 1
	print(f"Found {num_words} total words")

def get_num_characters(book_text):
	num_characters = {}

	for c in book_text.lower():
		if c.isalpha():
			num_characters[c] = num_characters.get(c, 0) + 1
	return num_characters

	# previous code
	#num_characters = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

	#for c in book_text.lower():
	#	if 'a' <= c <= 'z':
	#		num_characters[c] += 1

	#return num_characters

def sort_num_characters(num_characters):
	sorted_num_characters = [{"char": c, "num": n} for c, n in sorted(num_characters.items(), key=lambda x: x[1], reverse=True)]
	return sorted_num_characters

# def print_report():
	
