# Generated by Django 5.1.4 on 2024-12-12 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_bookmodel_user'),
        ('categories', '0003_rename_categories_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.categorie'),
        ),
    ]
