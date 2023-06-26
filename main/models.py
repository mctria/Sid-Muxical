from pyexpat import model
from django.db import models

# Create your models here.

Tags = [
    ('Lifestyle','Lifestyle'),
    ('Romance','Romance'),
    ('Jazz','Jazz'),
    ('Rock','Rock'),
    ('Traditional','Traditional'),
    ('Sad','Sad'),
]

currencys = [
    ('INR','Rs'),
    ('USD','$'),
    ('BTC','btc'),
    ('TRX','tron'),
]


class Home(models.Model):
    name = models.CharField("Music Tittle",max_length=150)
    date = models.DateField('Created Date')
    tag = models.CharField("Enter Keyword",max_length=200,choices=Tags)
    image = models.FileField("Upload Your Image")
    Total_min = models.FloatField("Total Time for ur Music")
    desc = models.CharField("description",max_length=250)
    audio = models.FileField("Upload ur Audio",upload_to='audio/')
    video_link = models.CharField("Yt Video Link", max_length=150,blank=True)

    def __str__(self) -> str:
        return self.name

    def video(self):
        if self.video_link != "":
            return self.video_link 
        else:
            video_link = 'https://www.youtube.com/results?search_query='+{self.name}
            self.video_link = video_link
            return self.video_link


class Latest_Episode(models.Model):
    Episode = models.ForeignKey(Home,on_delete=models.CASCADE,related_name="epi_1")

    def __str__(self) -> str:
        return self.Episode.name

class Home_Edit(models.Model):
    Title = models.CharField("Edit Title",max_length=100)
    Image = models.ImageField("Update Background Image")
    quots = models.CharField("Update Quots",max_length=250)
    author_name = models.CharField("Update Author",max_length=100,blank=True)

    def __str__(self) -> str:
        return self.Title

class donation(models.Model):
    name = models.CharField("Name",max_length=50)
    amount = models.FloatField("Amount",max_length=20)
    currency = models.CharField("Currency",max_length=5,choices=currencys)

    def __str__(self) -> str:
        return self.name

# class contact(models.Model):
    

class email(models.Model):
    name = models.CharField("Name",max_length=100,null=True,blank=True)
    email = models.EmailField("Email",blank=True,null=True)

    def __str__(self) -> str:
        return self.email

class payment(models.Model):
    name = models.CharField("Owner Name",max_length=100)
    paypal = models.CharField("Paypal",max_length=100)
    upi = models.CharField("UPI", max_length=100)
    qr = models.ImageField("QR")


    def __str__(self) -> str:
        return self.name