# Generated by Django 3.2.12 on 2022-02-23 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_book_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='count',
            new_name='amount',
        ),
    ]