# Generated by Django 3.2.12 on 2022-02-23 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_count_book_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
    ]
