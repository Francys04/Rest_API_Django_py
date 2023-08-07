# Generated by Django 4.2.3 on 2023-07-04 18:08
"""This model has three fields: id, username, and bio. 
The id field is an automatically incrementing primary key, the username field is a character field with 
a maximum length of 200 characters, and the bio field is a text field with a maximum length of 250 characters, 
allowing it to be blank and nullable.

This migration script represents the initial state of your Django database schema. 
It creates a table called Advocate with the specified fields."""

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
