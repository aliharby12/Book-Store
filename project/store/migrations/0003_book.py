# Generated by Django 3.2.12 on 2022-02-23 08:35

from django.db import migrations, models
import project.store.utils.image_save


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220222_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=project.store.utils.image_save.PathAndRename('book/images/'))),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
