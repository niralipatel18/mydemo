# Generated by Django 3.1.5 on 2021-02-08 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='p_file',
            new_name='image',
        ),
    ]