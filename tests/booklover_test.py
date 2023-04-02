import pandas as pd
import unittest

from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        """
        PURPOSE: add a book and test if it is in `book_list`.
        """
        bl = BookLover('Shawn', 'shawnsfeng@gmail.com', 'Scifi')
        book_name = "The art of Titanfall"
        book_rating = 3

        bl.add_book(book_name, book_rating)

        book_name_found = book_name in bl.book_list.book_name.values
        self.assertTrue(book_name_found)  # Or simply reuse the existing 
                                          # function to check book existence
                                          # self.assertTrue(bl.has_read(book_name))

    def test_2_add_book(self):
        """
        PURPOSE: add the same book twice. Test if it's in `book_list` only once.
        """
        bl = BookLover('Shawn', 'shawnsfeng@gmail.com', 'Scifi')
        book_name = "The art of Titanfall"
        book_rating = 3

        bl.add_book(book_name, book_rating)
        bl.add_book(book_name, book_rating)

        expected_num_books_read = 1

        self.assertEqual(bl.num_books_read(), expected_num_books_read)

    def test_3_has_read(self): 
        """
        PURPOSE: pass a book in the list and test if the answer is `True`.
        """
        bl = BookLover('Shawn', 'shawnsfeng@gmail.com', 'Scifi')
        book_name = "The art of Titanfall"
        book_rating = 3

        bl.book_list = pd.DataFrame({
            'book_name': [book_name],
            'book_rating': [book_rating]
        })  # Or simply call 
            # bl.add_book(book_name, book_rating)

        self.assertTrue(bl.has_read(book_name))

    def test_4_has_read(self): 
        """
        PURPOSE: pass a book NOT in the list and use `assert False` to test the answer is `True`
        """
        bl = BookLover('Shawn', 'shawnsfeng@gmail.com', 'Scifi')
        book_name = "The art of Titanfall"
        book_name_has_not_read = "Twin Cities"
        book_rating = 3

        bl.add_book(book_name, book_rating)

        self.assertFalse(bl.has_read(book_name_has_not_read))
        
    def test_5_num_books_read(self): 
        """
        PURPOSE: add some books to the list, and test num_books matches expected.
        """
        bl = BookLover('Shawn', 'shawnsfeng@gmail.com', 'Scifi')
        book_name_1 = "The art of Titanfall"
        book_rating_1 = 5

        book_name_2 = "Twin Cities"
        book_rating_2 = 2

        book_name_3 = "The Wonder Earth"
        book_rating_3 = 4

        bl.add_book(book_name_1, book_rating_1)
        bl.add_book(book_name_2, book_rating_2)
        bl.add_book(book_name_3, book_rating_3)

        expected_num_book_read = 3

        self.assertEqual(bl.num_books_read(), expected_num_book_read)

    def test_6_fav_books(self):
        """
        PURPOSE: add some books with ratings to the list, making sure some of them have rating > 3. 
        Your test should check that the returned books have rating  > 3
        """
        bl = BookLover('Shawn', 'shawnsfeng@gmail.com', 'Scifi')
        book_name_1 = "The art of Titanfall"
        book_rating_1 = 5  # Fav book

        book_name_2 = "Twin Cities"
        book_rating_2 = 2  # Not fav book

        book_name_3 = "The Wonder Earth"
        book_rating_3 = 4  # Fav book

        bl.add_book(book_name_1, book_rating_1)
        bl.add_book(book_name_2, book_rating_2)
        bl.add_book(book_name_3, book_rating_3)

        # Validate fav books length
        expected_num_fav_books = 2
        self.assertEqual(bl.fav_books().shape[0], expected_num_fav_books)

        # Validate fav books content
        expected_fav_books = pd.DataFrame({
            'book_name': [book_name_1, book_name_3],
            'book_rating': [book_rating_1, book_rating_3]
        }).reset_index(drop=True)

        self.assertTrue(
            bl.fav_books().reset_index(drop=True)\
                .equals(expected_fav_books))  # Ignore index during comparison


if __name__ == '__main__':
    unittest.main(verbosity=3)
