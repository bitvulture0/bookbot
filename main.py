#!/usr/bin/env python3

from stats import get_num_words, get_num_characters, sort_num_characters
import sys

def get_book_text(file_path):
	with open(file_path) as file:
		file_contents = file.read()
		return file_contents

def main():
	if len(sys.argv) == 1:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	if len(sys.argv) > 1:
		path_to_book = sys.argv[1]

	book_text = get_book_text(path_to_book)
	num_cha = get_num_characters(book_text)
	sorted_num_cha = sort_num_characters(num_cha)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path_to_book}...")
	print("----------- Word Count ----------")
	get_num_words(book_text)
	print("--------- Character Count -------")
	for c in sorted_num_cha:
		print(f"{c["char"]}: {c["num"]}")
	print("============= END ===============")


main()
