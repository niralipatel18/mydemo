# Generated by Django 3.1.5 on 2021-01-12 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fnm', models.CharField(max_length=50)),
                ('lnm', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip1', models.IntegerField()),
                ('unm', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
