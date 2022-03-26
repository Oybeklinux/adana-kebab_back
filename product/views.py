from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import FilterSet, DateFilter, NumberFilter


# sana va sonni ikki oraliq bo'yicha qidirish
class OrderFilter(FilterSet):
    min_price = NumberFilter(field_name="total", lookup_expr="gte")
    max_price = NumberFilter(field_name="total", lookup_expr="lte")
    start_date = DateFilter(field_name="created", lookup_expr="gte")
    end_date = DateFilter(field_name="created", lookup_expr="lte")


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('id')
    serializer_class = MenuSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    # @ -fts PostgreSQL o'rnatgandan keyin ishlatilsin
    # search_fields = ['^name_uz', '^name_en', '^name_ru']
    search_fields = ['^name_uz', '^definition_uz']
    ordering_fields = ['name_uz', 'definition_uz', 'price']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination
    queryset = Order.objects.filter()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = OrderFilter
    search_fields = ['^phone']
    ordering_fields = ['created']


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class GalaryViewSet(viewsets.ModelViewSet):
    queryset = Galary.objects.all()
    serializer_class = GalarySerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
