# Generated by Django 3.0.8 on 2020-07-13 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Authors',
        ),
    ]
