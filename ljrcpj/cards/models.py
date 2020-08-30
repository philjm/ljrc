from django.conf import settings
from django.db import models
from django.utils import timezone
from gsheets import mixins
from uuid import uuid4
from django.urls import reverse


class Cardpost(mixins.SheetPullableMixin, models.Model):
    
    spreadsheet_id = '1tMJCzkZolMfqLs7WoVaG4asMDfjwKveVl-868hDVcwo'
    model_id_field = 'guid'
    sheet_name = 'Models'
    data_range = 'A1:AI'

    guid = models.CharField(primary_key=True, max_length=255, default=uuid4)    
    season = models.CharField(max_length=127, null=True, blank=True, default=None)

    title = models.CharField(max_length=127, null=True, blank=True, default=None)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, default=None)
    cardnumber = models.CharField(max_length=127, null=True, blank=True, default=None)
    serialnumbered = models.CharField(max_length=127, null=True, blank=True, default=None)
    brand = models.CharField(max_length=127, null=True, blank=True, default=None)  
    text = models.CharField(max_length=127, null=True, blank=True, default=None)
    image = models.ImageField(upload_to='images', null=True, blank=True, default=None)
    psapopulationurl = models.CharField(max_length=127, null=True, blank=True, default=None)
    psatenpopulationid = models.CharField(max_length=127, null=True, blank=True, default=None)
    psaninepopulationid = models.CharField(max_length=127, null=True, blank=True, default=None)
    psaeightpopulationid = models.CharField(max_length=127, null=True, blank=True, default=None)
    rsslink = models.CharField(max_length=127, null=True, blank=True, default=None)
    team = models.CharField(max_length=127, null=True, blank=True, default=None)
    tag1 = models.CharField(max_length=127, null=True, blank=True, default=None)
    imagelink = models.CharField(max_length=127, null=True, blank=True, default=None)
    ebayafflink = models.CharField(max_length=127, null=True, blank=True, default=None)
    changepercent = models.CharField(max_length=127, null=True, blank=True, default=None)
    salesvolume = models.CharField(max_length=127, null=True, blank=True, default=None)
    average = models.CharField(max_length=127, null=True, blank=True, default=None)
    transactionvolume = models.CharField(max_length=127, null=True, blank=True, default=None)
    low = models.CharField(max_length=127, null=True, blank=True, default=None)
    high = models.CharField(max_length=127, null=True, blank=True, default=None)
    variations = models.CharField(max_length=127, null=True, blank=True, default=None)
    tag2 = models.CharField(max_length=127, null=True, blank=True, default=None)
    tag3 = models.CharField(max_length=127, null=True, blank=True, default=None)
    bgs8 = models.CharField(max_length=127, null=True, blank=True, default=None)
    bgs85 = models.CharField(max_length=127, null=True, blank=True, default=None)
    bgs9 = models.CharField(max_length=127, null=True, blank=True, default=None)
    bgs95 = models.CharField(max_length=127, null=True, blank=True, default=None)
    bgs10 = models.CharField(max_length=127, null=True, blank=True, default=None)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('slugs', kwargs={'slug': self.slug})


class Stats(mixins.SheetPullableMixin, models.Model):
    
    spreadsheet_id = '1tMJCzkZolMfqLs7WoVaG4asMDfjwKveVl-868hDVcwo'
    model_id_field = 'guid'
    sheet_name  = 'stats'
    guid = models.CharField(primary_key=True, max_length=255, default=uuid4)    

    cardcount = models.CharField(max_length=127, null=True, blank=True, default=None)
    changepercent = models.CharField(max_length=127, null=True, blank=True, default=None)
    salesvolume = models.CharField(max_length=127, null=True, blank=True, default=None)
    average = models.CharField(max_length=127, null=True, blank=True, default=None)
    transactionvolume = models.CharField(max_length=127, null=True, blank=True, default="N/A")
    low = models.CharField(max_length=127, null=True, blank=True, default=None)
    high = models.CharField(max_length=127, null=True, blank=True, default=None)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.cardcount

