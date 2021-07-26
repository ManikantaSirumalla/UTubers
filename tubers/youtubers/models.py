from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.

class Youtuber(models.Model):

        crew_choices = (
                ('Solo','Solo'),
                ('Small', 'Small'),
                ('Large', 'Large'),
        )

        camera_choices = (
                ('Canon', 'Canon'),
                ('Nikon', 'Nikon'),
                ('Sony', 'Sony'),
                ('Fuji', 'Fuji'),
                ('Red', 'Red'),
                ('Panasonic', 'Panasonic'),
                ('Other', 'Other'),

        )

        category_choices = (
                ('Vlogs', 'Vlogs'),
                ('Gaming', 'Gaming'),
                ('Music', 'Music'),
                ('Sports', 'Sports'),
                ('Entertainment', 'Entertainment'),
                ('Education', 'Education'),
                ('Science & Technology', 'Science & Technology'),
                ('Style & grooming', 'Style & grooming'),
                ('Health & Fitness', 'Health & Fitness'),
                ('News & Politics', 'News & Politics'),
                ('Wellness', 'Wellness'),
                ('Travel & Explore', 'Travel & Explore'),
                ('Vechicles & Automobiles', 'Vechicles & Automobiles'),
                ('Religious & Spiritual', 'Religious & Spiritual'),
                ('Podcasts', 'Podcasts'),
                ('Coding', 'coding'),
                ('Animals & Nature', 'Animals & Nature'),
                ('Food & Cooking', 'Food & Cooking'),
                ('Others', 'Others'),
        )
        language_choices = (

                ('Hindi', 'Hindi'),
                ('Bengali', 'Bengali'),
                ('Marathi', 'Marathi'),
                ('Telugu', 'Telugu'),
                ('Tamil', 'Tamil'),
                ('Gujarathi', 'Gujarathi'),
                ('Urdu', 'Urdu'),
                ('Kannada', 'Kannada'),
                ('Odia', 'Odia'),
                ('Malayalam', 'Malayalam'),
                ('Punjabi', 'Punjabi'),
                ('Assamese', 'Assamese'),
                ('Arabic', 'Arabic'),
                ('Chinese', 'Chinese'),
                ('English', 'English'),
                ('French', 'French'),
                ('German', 'German'),
                ('Italian', 'Italian'),
                ('Indonesian', 'Indonesian'),
                ('Japanese', 'Japanese'),
                ('Korean', 'Korean'),
                ('Polish', 'Polish'),
                ('Portuguese','Portuguese'),
                ('Russian', 'Russian'),
                ('Spanish', 'Spanish'),
                ('Thai', 'Thai'),
                ('Turkish', 'Turkish'),
                ('Vietnamese', 'Vietnamese'),
        )

        name = models.CharField(max_length=255)
        price = models.IntegerField()
        photo = models.ImageField(upload_to='media/ytubers/%y/%m')
        video_url = models.CharField(max_length=255)
        description  = RichTextField()
        city = models.CharField(max_length=255)
        age = models.IntegerField()
        language = models.CharField(choices=language_choices,max_length=255, default= False)
        crew  = models.CharField(choices=crew_choices,max_length=255)
        camera_type = models.CharField(choices=camera_choices,max_length=255)
        category = models.CharField(choices=category_choices,max_length=255)
        subs_count = models.CharField(max_length=255)
        is_featured = models.BooleanField(default=False)
        created_date = models.DateTimeField(default=datetime.now, blank=True)