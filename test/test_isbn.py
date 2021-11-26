import isbnlib as iv

def test_isbn_valid_code(isbn):
  iv.is_valid_isbn("978-0-71-67-0344-0")
  iv.is_valid_isbn("0-7176-0344-0")
  iv.is_valid_isbn("42-3345-6532-99999")

  def test_isbn_10digit(isbn):
    iv.is_isbn10("978-0-4587-2388-1")
    iv.is_isbn10("978-044631078")
    iv.is_isbn10("817525766-0")

     def test_isbn_13digit(isbn):
    iv.is_isbn13("978-0-4587-2388-1")
    iv.is_isbn13("978-0-71-67-0344-0")
    iv.is_isbn13("817525766-0")

