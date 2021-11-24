from django.db import models


class Bookshelf(models.Model):
    name = models.CharField(max_length=100)

    def get_books(self):
        #print(self.id, self.name)
        books = Book.objects.filter(shelf=self).order_by('title')
        return books

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    shelf = models.ForeignKey(Bookshelf, on_delete=models.SET_NULL, null=True)

    def assign_to(self, shelf):
        self.shelf = shelf
        self.save()

    def get_shelf(self):
        if self.shelf:
            return self.shelf
        else:
            return None

    def __str__(self):
        return self.title

    
