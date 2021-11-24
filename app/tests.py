from django.test import TestCase

from django.db.models import QuerySet

from app.models import Book
from app.models import Bookshelf


class BookCreationTestCase(TestCase):
    def test_create_book(self):
        book = Book(title='Hamlet')
        book.save()

        self.assertEqual(book.title, 'Hamlet')
        self.assertEqual(book.get_shelf(), None)


class BookshelfCreationTestCase(TestCase):
    def test_create_bookshelf(self):
        shelf = Bookshelf(name='Important')
        shelf.save()

        self.assertEqual(shelf.name, 'Important')


class BookToBookshelfAssignmentTestCase(TestCase):
    def test_assign_single_book_to_bookshelf(self):
        book = Book(title='Hamlet')
        book.save()

        shelf = Bookshelf(name='Important')
        shelf.save()

        self.assertEqual(book.get_shelf(), None)
        self.assertEqual(list(shelf.get_books()), [])

        book.assign_to(shelf)

        self.assertEqual(book.get_shelf(), shelf)
        self.assertIsInstance(shelf.get_books(), QuerySet)
        self.assertEqual(list(shelf.get_books()), [book])

    def test_reassign_book_from_shelf_to_other_shelf(self):
        hamlet = Book(title='Hamlet')
        hamlet.save()

        important = Bookshelf(name='Important')
        important.save()

        read = Bookshelf(name='Read')
        read.save()

        self.assertEqual(hamlet.get_shelf(), None)
        self.assertEqual(list(important.get_books()), [])
        self.assertEqual(list(read.get_books()), [])

        hamlet.assign_to(important)

        self.assertEqual(hamlet.get_shelf(), important)
        self.assertEqual(list(important.get_books()), [hamlet])
        self.assertEqual(list(read.get_books()), [])

        hamlet.assign_to(read)

        self.assertEqual(hamlet.get_shelf(), read)
        self.assertEqual(list(important.get_books()), [])
        self.assertEqual(list(read.get_books()), [hamlet])

    def test_with_many_books_assigned_to_shelf(self):
        zorro = Book(title='Zorro')
        zorro.save()

        hamlet = Book(title='Hamlet')
        hamlet.save()

        lolita = Book(title='Lolita')
        lolita.save()

        read = Bookshelf(name='Read')
        read.save()

        zorro.assign_to(read)
        hamlet.assign_to(read)
        lolita.assign_to(read)

        self.assertEqual(zorro.get_shelf(), read)
        self.assertEqual(hamlet.get_shelf(), read)
        self.assertEqual(lolita.get_shelf(), read)

        self.assertEqual(list(read.get_books()), [hamlet, lolita, zorro])

    def test_with_delete_shelf(self):
        zorro = Book(title='Zorro')
        zorro.save()

        hamlet = Book(title='Hamlet')
        hamlet.save()

        lolita = Book(title='Lolita')
        lolita.save()

        read = Bookshelf(name='Read')
        read.save()

        zorro.assign_to(read)
        hamlet.assign_to(read)
        lolita.assign_to(read)

        self.assertEqual(zorro.get_shelf(), read)
        self.assertEqual(hamlet.get_shelf(), read)
        self.assertEqual(lolita.get_shelf(), read)

        self.assertEqual(list(read.get_books()), [hamlet, lolita, zorro])

        read.delete()

        # retrieve objects again because delete() makes changes only to
        # the database, not to objects in Django memory
        zorro = Book.objects.get(pk=zorro.id)
        hamlet = Book.objects.get(pk=hamlet.id)
        lolita = Book.objects.get(pk=lolita.id)

        self.assertEqual(zorro.get_shelf(), None)
        self.assertEqual(hamlet.get_shelf(), None)
        self.assertEqual(lolita.get_shelf(), None)
