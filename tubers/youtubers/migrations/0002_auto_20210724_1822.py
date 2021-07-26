# Generated by Django 3.2.5 on 2021-07-24 18:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtuber',
            name='height',
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('Canon', 'Canon'), ('Nikon', 'Nikon'), ('Sony', 'Sony'), ('Fuji', 'Fuji'), ('Red', 'Red'), ('Panasonic', 'Panasonic'), ('Other', 'Other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('Vlogs', 'Vlogs'), ('Gaming', 'Gaming'), ('Music', 'Music'), ('Sports', 'Sports'), ('Entertainment', 'Entertainment'), ('Education', 'Education'), ('Science & Technology', 'Science & Technology'), ('Style & grooming', 'Style & grooming'), ('Health & Fitness', 'Health & Fitness'), ('News & Politics', 'News & Politics'), ('Wellness', 'Wellness'), ('Travel & Explore', 'Travel & Explore'), ('Vechicles & Automobiles', 'Vechicles & Automobiles'), ('Religious & Spiritual', 'Religious & Spiritual'), ('Podcasts', 'Podcasts'), ('Coding', 'coding'), ('Animals & Nature', 'Animals & Nature'), ('Food & Cooking', 'Food & Cooking'), ('Others', 'Others')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('Solo', 'Solo'), ('Small', 'Small'), ('Large', 'Large')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]