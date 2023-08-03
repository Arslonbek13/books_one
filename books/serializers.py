from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title',  'subtitle', 'content', 'author', 'isbn', 'price')


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'The title of the book must consist of letters.'
                }
            )

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'You cannot upload a book with the same title and author.'
                }
            )
        return data


    def validate_price(self, price):
        if price < 0:
            raise ValidationError(
                {
                    'status': False,
                    'message': 'The price is incorrect.'
                }
            )
        return price