# Generated by Django 4.1.7 on 2023-03-23 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='name',
        ),
    ]
