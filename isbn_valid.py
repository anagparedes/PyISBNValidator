from isbnlib import canonical, is_isbn10, is_isbn13

isbn = canonical("978-0446310789")

def is_valid_isbn(isbn):
if is_isbn13(isbn):
  print("is a 13 digit")

elif is_isbn10(isbn):
  print("it's a 10 digit")

else:
  print("it's not a valid code!")

