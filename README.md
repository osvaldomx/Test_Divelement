## Environment:
- Python version: 3.7
- Django version: 3.0.6

## Read-Only Files:
- app/tests.py
- manage.py

## Requirements:


In this challenge, your task is to implement two models, Book and Bookshelf, which allow for organizing books.

1. Each book must have the following fields:

- `id`: a unique autoincrement integer ID of the book
- `title`: a string denoting the title of the book

2. Each bookshelf must have the following fields:

- `id`: a unique autoincrement integer ID of the bookshelf
- `name`: a string denoting the name of the bookshelf

3. A book must be able to be created in the following way:

   `book = Book(title='Hamlet')`

4. A bookshelf must be able to be created in the following way:

   `bookshelf = Bookshelf(name='To Read')`

5. The Book model implements the `assign_to(shelf)` method, which assigns the Book to the given shelf. A book can be assigned to at most one shelf, which means that it is either assigned to one shelf or not assigned to any shelf. By default, it is not assigned to any shelf.

6. The Book model implements the `get_shelf()` method, which returns the Bookshelf the book is assigned to. If the book is not assigned to any Bookshelf, it returns None.

7. The Bookshelf model implements the `get_books()` method, which returns a `Queryset` of all Books assigned to the Bookshelf, sorted by their titles alphabetically in ascending order. You may assume that no two books have the same title.

8. When a bookshelf is deleted, all books that were assigned to it become not assigned to any shelf but are not deleted.

## Example Usage:

```python
>>> hamlet = Book(title='Hamlet')
>>> hamlet.save()

>>> read = Bookshelf(name='Read')
>>> read.save()

>>> print(hamlet.get_shelf())
None

>>> read.get_books()
<QuerySet []>

>>> hamlet.assign_to(read)

>>> hamlet.get_shelf()
<Bookshelf: Bookshelf object (1)>

>>> read.get_books()
<QuerySet [<Book: Book object (1)>]>

>>> read.delete()
(1, {'app.Bookshelf': 1})

>>> hamlet = Book.objects.get(pk=hamlet.id)
>>> print(hamlet.get_shelf())
None
```

## Commands

+ run:
```source env1/bin/activate; pip3 install -r requirements.txt; python3 manage.py makemigrations && python3 manage.py migrate --run-syncdb && python3 manage.py runserver 0.0.0.0:8000```

+  install:
```bash python_install.sh;source env1/bin/activate; pip3 install -r requirements.txt;```

+ test:
```rm -rf unit.xml;source env1/bin/activate; python3 manage.py test```
