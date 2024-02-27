from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ComplexFilterOne, ComplexFilterTwo
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from .models import Information, Banner, PaymentOptions, Advertising, ContactUs, Company, Complex, Services, \
    WhyRealtor, Realtors, HowWorks

from .serializer import InformationSerializer, BannerSerializer, PaymentOptionsSerializer, AdvertisingSerializer, \
    ContactUsSerializer, CompanySerializer, ComplexSerializer, ServicesSerializer, \
    WhyRealtorSerializer, RealtorsSerializer, HowWorksSerializer


class InformationList(ListAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().last()
        return Response(InformationSerializer(queryset).data, status=status.HTTP_200_OK)


class BannerList(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().last()
        return Response(BannerSerializer(queryset).data, status=status.HTTP_200_OK)


class ComplexFilter(ListAPIView):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ComplexFilterOne


class PopularComplexList(ListAPIView):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-viewed')
        return Response(ComplexSerializer(queryset, many=True).data, status=status.HTTP_200_OK)


class PaymentOptionsList(ListAPIView):
    queryset = PaymentOptions.objects.all()
    serializer_class = PaymentOptionsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-id')[:3]
        return Response(PaymentOptionsSerializer(queryset, many=True).data, status=status.HTTP_200_OK)


class AdvertisingList(ListAPIView):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().last()
        return Response(AdvertisingSerializer(queryset).data, status=status.HTTP_200_OK)


class CreateContact(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class CompanyList(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-id')
        return Response(CompanySerializer(queryset, many=True).data, status=status.HTTP_200_OK)


class ComplexDetail(RetrieveAPIView):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        complex = self.get_object()
        complex.viewed += 1
        complex.save()
        complex.company.viewed += 1
        complex.company.save()
        serializer = self.get_serializer(complex)
        return Response(serializer.data)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PopularCompanyList(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-viewed')
        pagination_class = LargeResultsSetPagination
        paginator = pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        return paginator.get_paginated_response(CompanySerializer(result_page, many=True).data)


class ComplexFilterLast(ListAPIView):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ComplexFilterTwo


class ServicesList(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-id')[:4]
        return Response(ServicesSerializer(queryset, many=True).data, status=status.HTTP_200_OK)


class WhyRealtorsList(ListAPIView):
    queryset = WhyRealtor.objects.all()
    serializer_class = WhyRealtorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-id')[:3]
        return Response(WhyRealtorSerializer(queryset, many=True).data, status=status.HTTP_200_OK)


class RealtorsList(ListAPIView):
    queryset = Realtors.objects.all()
    serializer_class = RealtorsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-id')[:8]
        return Response(RealtorsSerializer(queryset, many=True).data, status=status.HTTP_200_OK)


class HowWorksList(ListAPIView):
    queryset = HowWorks.objects.all()
    serializer_class = WhyRealtorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-id')[:3]
        return Response(HowWorksSerializer(queryset, many=True).data, status=status.HTTP_200_OK)
