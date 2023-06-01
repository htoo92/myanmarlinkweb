from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
# from django.utils.html import format_html
# from django.utils.translation import gettext_lazy as _


# Create your models here.


TOWNSHIP_CHOICES = (
    ("NORTH DAGON", "north dagon"),
    ("SOUTH DAGON", "south dagon"),
    ("EAST DAGON", "east dagon"),
    ("NORTH OAKALAPA", "north oakalapa"),
    ("SOUTH OAKALAPA", "south oakalapa"),
    ("THINGANGYUN", "thingangyun"),
    ("HLAING", "hlaing"),
    ("MINGALADONE", "mingaladone"),
    ("THAKETA", "thaketa"),
    ("DAWBON", "dawbon"),
    ("MAYANGONE", "mayangone"),
    ("SHWEPAUKKAN", "shwepaukkan"),
    ("YANKIN", "yankin"),
    ("INSEIN", "insein"),
    ("OTHER", "other"),
    )


ROUTER_LIGHT_CHOICES = (
		("RED", "red_light"),
		("GREEN", "green_light"),
		("OTHER", "other")
		)



STATUS = (
    ('Read', 'Read'),
    ('Unread', 'Unread')
    )
class Complain(models.Model):
	
    name = models.CharField(max_length=255, blank=True)
    # slug = models.SlugField(unique=True)
    customer_id = models.CharField(max_length=255)
    router = models.CharField(max_length=255, 
        choices=ROUTER_LIGHT_CHOICES, default="RED"
        
        )
    phone_number = models.IntegerField(blank=True)
    address = models.TextField(blank=True)
    # house_number = models.IntegerField()
    # floor = models.IntegerField()
    # street = models.CharField(max_length=255)
    # near_street = models.CharField(max_length=255)
    # ward = models.CharField(max_length=255)
    # township = models.CharField(max_length=255, choices=TOWNSHIP_CHOICES, default="EAST DAGON")
    # latlong = models.IntegerField() 
    comment = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS, default="Unread")
    # update_at = models.DateField(default=timezone.now)
    # read_user = models.ManyToMany(auth.User)


    def __str__(self):
    	return self.customer_id



class ComplainStatus(models.Model):
    pass






class Internetplan(models.Model):
    BANDWIDTH_CHOICES =(
        ("15mbps", ("15Mbps")),
        ("25mbps", ("25Mbps")),
        ("35mbps", ("35Mbps")),
        ("55mbps", ("55Mbps")),
        ("75mbps", ("75Mbps")),
        ("95mbps", ("95Mbps")),
       
    )
    PRICE_CHOICES = (("28,500", ("28,500MMks")),
                     ("36,000", ("36,000MMks")),
                     ("52,000", ("52,000MMks")),
                     ("72,000", ("72,000MMks")),
                     ("92,000", ("92,000MMks")),
                     ("122,000", ("122,000MMks")),
                     )
    name = models.CharField(max_length=100, choices=BANDWIDTH_CHOICES, default="15Mbps")
    price = models.CharField(max_length=100, choices=PRICE_CHOICES, default="28,500")
    create_date = models.DateField(default=timezone.now)
    update_date = models.DateField(default=timezone.now)


    def __str__(self):
        return self.name





MONTH_CHOICES = (
	("1MONTH", "1month"),
	("2MONTH", "2month"),
	("3MONTH", "3month"),
	("4MONTH", "4month"),
	("5MONTH", "5month"),
	("6MONTH", "6month"),
	("12MONTH", "12month"),
	)

class NewInstallation(models.Model):

    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    # plan = models.ForeignKey(Internetplan, on_delete=models.CASCADE, null=True)
    # month = models.CharField(max_length=255, choices=MONTH_CHOICES, default="1month")
    
    # house_number = models.IntegerField()
    # floor = models.IntegerField()
    # street = models.CharField(max_length=255)
    # # near_street = models.CharField(max_length=255)
    # ward = models.CharField(max_length=255)
    # township = models.CharField(max_length=255, choices=TOWNSHIP_CHOICES, default="EAST DAGON")
    # latlong = models.IntegerField()
    # nrc_num = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    about = models.TextField()
    create_at = models.DateField(default=timezone.now)
    # update_at = models.DateField(default=timezone.now)

    def __str__(self):
    	return self.name



class NewinstallationStatus(models.Model):
    name = models.ForeignKey(NewInstallation, on_delete=models.CASCADE, null=True)
    full_box = models.BooleanField(default=False)
    no_box = models.BooleanField(default=False)
    customer_cancel = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    create_at = models.DateField(default=timezone.now)


    def __str__(self):
        return self.name.name





STATUS_CHOICES = (
    ('Read', 'Read'),
    ('Unread', 'Unread'),
    )
class Billing(models.Model):
    name= models.CharField(max_length=255)
    customer_id = models.CharField(max_length=255)
    bill_screenshot = models.ImageField(upload_to="img/upload", null=True)
    remark = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Unread')

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


    def image_tag(self):
        return mark_safe('<img src="%s" width="520px" height="1400px" />'%(self.image.url))
    image_tag.short_description = 'Image'



class Billingstatus(models.Model):
    name = models.ForeignKey(Billing, on_delete=models.CASCADE, null=True)
    # customer_id = models.ForeignKey('web.Billing.customer_id', on_delete=models.CASCADE, null=True)
    error_status = models.BooleanField(default=False)
    pending_status = models.BooleanField(default=False)
    finishing_status = models.BooleanField(default=False)
    remark = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.name


    # def create_at(self):
    #     if self.create_at > date():
    #         return format_html('<span style="color: #cc0033; font-weight:bold;">{0}</span>', self.create_at.strftime('%b. %d, %Y'))
    #     else:
    #         return format_html('<span style="color:#000; ">{0}</span>', self.create_at.strftime('%b. %d, %Y'))


    #     create_at.allow_tag = True




        

