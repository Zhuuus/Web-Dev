from django.shortcuts import render
from django.http import JsonResponse
from .models import Company, Vacancy

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CompanySerializer, VacancySerializer
from rest_framework import generics

class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class VacancyListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyDetailAPIView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyTopTenAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.order_by('-salary')[:10]
    serializer_class = VacancySerializer


def list_companies(request):
    companies = Company.objects.all()
    data = [{'id': company.id, 'name': company.name, 'description': company.description, 'city': company.city, 'address': company.address} for company in companies]
    return JsonResponse(data, safe=False)

def get_company(request, id):
    try:
        company = Company.objects.get(id=id)
        data = {'id': company.id, 'name': company.name, 'description': company.description, 'city': company.city, 'address': company.address}
        return JsonResponse(data)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company does not exist'}, status=404)

def list_vacancies_by_company(request, id):
    vacancies = Vacancy.objects.filter(company_id=id)
    data = [{'id': vacancy.id, 'name': vacancy.name, 'description': vacancy.description, 'salary': vacancy.salary} for vacancy in vacancies]
    return JsonResponse(data, safe=False)

def list_vacancies(request):
    vacancies = Vacancy.objects.all()
    data = [{'id': vacancy.id, 'name': vacancy.name, 'description': vacancy.description, 'salary': vacancy.salary} for vacancy in vacancies]
    return JsonResponse(data, safe=False)

def get_vacancy(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
        data = {'id': vacancy.id, 'name': vacancy.name, 'description': vacancy.description, 'salary': vacancy.salary}
        return JsonResponse(data)
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': 'Vacancy does not exist'}, status=404)

def list_top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = [{'id': vacancy.id, 'name': vacancy.name, 'description': vacancy.description, 'salary': vacancy.salary} for vacancy in vacancies]
    return JsonResponse(data, safe=False)

