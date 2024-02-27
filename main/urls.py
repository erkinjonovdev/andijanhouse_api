from django.urls import path
from .views import InformationList, BannerList, ComplexFilter, PopularComplexList, PaymentOptionsList, \
    AdvertisingList, CreateContact, CompanyList, ComplexDetail, PopularCompanyList, ComplexFilterLast, \
    ServicesList, WhyRealtorsList, RealtorsList, HowWorksList

urlpatterns = [
    path('info/', InformationList.as_view()),
    path('banner/', BannerList.as_view()),
    path('filter-complex/', ComplexFilter.as_view()),
    path('filter-complex2/', ComplexFilterLast.as_view()),
    path('popular-complex/', PopularComplexList.as_view()),
    path('payment-options/', PaymentOptionsList.as_view()),
    path('advertising/', AdvertisingList.as_view()),
    path('create-contact/', CreateContact.as_view()),
    path('company/', CompanyList.as_view()),
    path('complex-detail/<int:pk>/', ComplexDetail.as_view()),
    path('popular-company/', PopularCompanyList.as_view()),
    path('services/', ServicesList.as_view()),
    path('whyrealtors/', WhyRealtorsList.as_view()),
    path('realtors/', RealtorsList.as_view()),
    path('howworks/', HowWorksList.as_view()),
]
