# Generated by Django 3.2.3 on 2021-07-23 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0007_titanic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='titanic',
            old_name='parents',
            new_name='parch',
        ),
    ]