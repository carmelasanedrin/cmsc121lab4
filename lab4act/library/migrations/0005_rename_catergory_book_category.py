# Generated by Django 3.2.4 on 2021-06-21 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_book_pages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='catergory',
            new_name='category',
        ),
    ]
