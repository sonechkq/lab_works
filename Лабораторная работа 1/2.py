disk_size_mb = 1.44
pages_per_book = 100.0
lines_per_page = 50.0
chars_per_line = 25.0
size_per_char = 4.0

disk_size_bytes = disk_size_mb * 1024.0 * 1024.0

book_size_bytes = pages_per_book * lines_per_page * chars_per_line * size_per_char

number_of_books = disk_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", number_of_books)
