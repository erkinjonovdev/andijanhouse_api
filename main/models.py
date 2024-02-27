from django.db import models


class Information(models.Model):
    comp_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="InfoImg")
    tg = models.URLField()
    insta = models.URLField()
    youtube = models.URLField()
    fb = models.URLField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.comp_name


class Banner(models.Model):
    title = models.CharField(max_length=255)
    bg_img = models.ImageField(upload_to="BannerImg")

    def __str__(self):
        return self.title


class PaymentOptions(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to="PaymentOptionImg")

    def __str__(self):
        return self.title


class Advertising(models.Model):
    title = models.CharField(max_length=255)
    bg_img = models.ImageField(upload_to="AdImg")
    text = models.TextField()
    bonus = models.IntegerField()
    bonus_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Company(models.Model):
    comp_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="CompanyImg")
    viewed = models.IntegerField(default=0)

    def __str__(self):
        return self.comp_name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TypeHouse(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ComplexFeature(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="ComplexFeatureImg")

    def __str__(self):
        return self.title


class NearbyPlaces(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="NearbyPlaceImg")

    def __str__(self):
        return self.title


class ComplexImages(models.Model):
    img = models.ImageField(upload_to="ComplexImg")

    def __str__(self):
        return self.img.url


class Complex(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    complex_name = models.CharField(max_length=255)
    img = models.ManyToManyField(ComplexImages)
    lifetime = models.DateField()
    apartments = models.IntegerField(default=0)
    floor = models.IntegerField(default=0)
    ceilings = models.IntegerField(default=0)
    type_of_house = models.ForeignKey(TypeHouse, on_delete=models.CASCADE)
    installment_period = models.CharField(max_length=255)
    parking = models.CharField(max_length=255)
    decoration = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    balcony = models.CharField(max_length=255)
    heating = models.CharField(max_length=255)
    territory = models.CharField(max_length=255)
    desc = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=6)
    num_rooms = models.IntegerField(choices=(
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4+"),
    ))
    square = models.FloatField(default=0)
    complex_features = models.ManyToManyField(ComplexFeature)
    nearby_places = models.ManyToManyField(NearbyPlaces)
    viewed = models.IntegerField(default=0)

    def __str__(self):
        return self.company.comp_name


class Services(models.Model):
    icon = models.ImageField(upload_to='ServiceImg')
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class WhyRealtor(models.Model):
    icon = models.ImageField(upload_to='WhyRealtorImg')
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class Realtors(models.Model):
    full_name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='RealtorImg')
    rating = models.IntegerField()
    comments = models.IntegerField()

    def __str__(self):
        return self.full_name


class HowWorks(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.text
