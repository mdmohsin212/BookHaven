# Generated by Django 5.1.4 on 2024-12-15 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_rename_book_comment_book_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='createdate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]