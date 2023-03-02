from django.db import IntegrityError
from django.test import TestCase
from catalog.models import Author, Book

class AuthorModelTest(TestCase):
    
        @classmethod
        def setUpTestData(cls):
            #Set up non-modified objects used by all test methods
            Author.objects.create(first_name='Big', last_name='Bob')
    
        def test_first_name_label(self):
            author=Author.objects.get(id=1)
            field_label = author._meta.get_field('first_name').verbose_name
            self.assertEquals(field_label,'first name')

        def test_last_name_label(self):
            author=Author.objects.get(id=1)
            field_label = author._meta.get_field('last_name').verbose_name
            self.assertEquals(field_label,'last name')

        def test_date_of_birth_label(self):
            author=Author.objects.get(id=1)
            field_label = author._meta.get_field('date_of_birth').verbose_name
            self.assertEquals(field_label,'date of birth')
    
        def test_date_of_death_label(self):
            author=Author.objects.get(id=1)
            field_label = author._meta.get_field('date_of_death').verbose_name
            self.assertEquals(field_label,'died')
    
        def test_first_name_max_length(self):
            author=Author.objects.get(id=1)
            max_length = author._meta.get_field('first_name').max_length
            self.assertEquals(max_length,100)
    
        def test_object_name_is_last_name_comma_first_name(self):
            author=Author.objects.get(id=1)
            expected_object_name = f'{author.last_name}, {author.first_name}'
            self.assertEquals(expected_object_name, str(author))
    
        def test_get_absolute_url(self):
            author=Author.objects.get(id=1)
            #This will also fail if the urlconf is not defined.
            self.assertEquals(author.get_absolute_url(), '/catalog/author/1')

class BookModelTest(TestCase):
        
            @classmethod
            def setUpTestData(cls):
                #Set up non-modified objects used by all test methods
                Author.objects.create(first_name='Big', last_name='Bob')
                Book.objects.create(title='Big Book', author=Author.objects.get(id=1), isbn='1234567890123', summary='This is a summary of the book')
        
            # Title test section
            def test_title_label(self):
                book=Book.objects.get(id=1)
                field_label = book._meta.get_field('title').verbose_name
                self.assertEquals(field_label,'title')

            def test_title_max_length(self):
                book=Book.objects.get(id=1)
                max_length = book._meta.get_field('title').max_length
                self.assertEquals(max_length,200)

            # Author test section
            def test_author_label(self):
                book=Book.objects.get(id=1)
                field_label = book._meta.get_field('author').verbose_name
                self.assertEquals(field_label,'author')

            # Summary test section
            def test_summary_label(self):
                book=Book.objects.get(id=1)
                field_label = book._meta.get_field('summary').verbose_name
                self.assertEquals(field_label,'summary')

            def test_summary_max_length(self):
                book=Book.objects.get(id=1)
                max_length = book._meta.get_field('summary').max_length
                self.assertEquals(max_length,1000)

            def test_summary_help_text(self):
                book=Book.objects.get(id=1)
                help_text = book._meta.get_field('summary').help_text
                self.assertEquals(help_text,'Enter a brief description of the book')

            # ISBN test section
            def test_isbn_label(self):
                book=Book.objects.get(id=1)
                field_label = book._meta.get_field('isbn').verbose_name
                self.assertEquals(field_label,'ISBN')
            
            def test_isbn_max_length(self):
                book=Book.objects.get(id=1)
                max_length = book._meta.get_field('isbn').max_length
                self.assertEquals(max_length,13)
            
            def test_isbn_help_text(self):
                book=Book.objects.get(id=1)
                help_text = book._meta.get_field('isbn').help_text
                self.assertEquals(help_text,'13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

            def test_isbn_unique(self):
                # Try adding another book with the same ISBN and assert that it raises an error
                book=Book.objects.get(id=1)
                try:
                    book2 = Book.objects.create(title='Big Book 2', author=Author.objects.get(id=1), isbn=book.isbn)
                    self.assertRaises(IntegrityError, book2.save())
                except IntegrityError:
                    pass

            # Genre test section
            def test_genre_label(self):
                book=Book.objects.get(id=1)
                field_label = book._meta.get_field('genre').verbose_name
                self.assertEquals(field_label,'genre')

            def test_genre_help_text(self):
                book=Book.objects.get(id=1)
                help_text = book._meta.get_field('genre').help_text
                self.assertEquals(help_text,'Select a genre for this book')
            
            # Functions test section
            def test_object_name_is_title(self):
                book=Book.objects.get(id=1)
                expected_object_name = book.title
                self.assertEquals(expected_object_name, str(book))
        
            def test_get_absolute_url(self):
                book=Book.objects.get(id=1)
                #This will also fail if the urlconf is not defined.
                self.assertEquals(book.get_absolute_url(), '/catalog/book/1')