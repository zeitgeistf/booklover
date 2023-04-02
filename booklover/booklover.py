import pandas as pd


class BookLover:

    def __init__(self, 
                 name: str, 
                 email: str, 
                 fav_genre: str, 
                 num_books: int = 0, 
                 book_list: pd.DataFrame = pd.DataFrame({'book_name': [], 'book_rating': []})):

        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name: str, rating: int) -> None:
        if not self.has_read(book_name):
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)\
                .astype({'book_name': 'str', 'book_rating': 'int64'})
            self.num_books_read()  # Increment read books count
        else:
            print(f'Book {book_name} is already in the book list, no operation will be performed.')

    def has_read(self, book_name: str) -> bool:
        return False if book_name not in self.book_list.book_name.values.astype(str) else True

    def num_books_read(self) -> int:
        num_books_read = self.book_list.shape[0]
        self.num_books = num_books_read  # Update the class object attribute
        return num_books_read

    def fav_books(self) -> pd.DataFrame:
        return self.book_list[self.book_list.book_rating > 3]


if __name__ == '__main__':
    # Run some initial testings
    bl = BookLover(name='Shawn Feng', email='shawnsfeng@gmail.com', fav_genre='Scifi')

    book_name_1 = "War of the Worlds"  # Has read, high score
    book_name_2 = "Twin Cities"  # Has read, low score
    book_name_3 = "Judge"  # Has not read

    bl.add_book(book_name_1, 4)
    bl.add_book(book_name_2, 2)

    print(f'Book list: {bl.book_list}')
    print(f'Has read book {book_name_1}: {bl.has_read(book_name_1)}')  # True
    print(f'Has read book {book_name_3}: {bl.has_read(book_name_3)}')  # False
    print(f'Has read {bl.num_books_read()} books.')
    print(f'Favorite books: \n{bl.fav_books()}')
