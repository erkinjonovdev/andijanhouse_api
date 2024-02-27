from django.contrib import admin
from .models import Information, Banner, PaymentOptions, Advertising, ContactUs, Company, Category, TypeHouse, \
    District, ComplexFeature, NearbyPlaces, ComplexImages, Complex, Services, WhyRealtor, Realtors, HowWorks

admin.site.register(Information)
admin.site.register(Banner)
admin.site.register(PaymentOptions)
admin.site.register(Advertising)
admin.site.register(ContactUs)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(TypeHouse)
admin.site.register(District)
admin.site.register(ComplexFeature)
admin.site.register(NearbyPlaces)
admin.site.register(ComplexImages)
admin.site.register(Complex)
admin.site.register(Services)
admin.site.register(WhyRealtor)
admin.site.register(Realtors)
admin.site.register(HowWorks)
