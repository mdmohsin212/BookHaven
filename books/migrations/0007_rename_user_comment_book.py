# Generated by Django 5.1.4 on 2024-12-15 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='Book',
        ),
    ]