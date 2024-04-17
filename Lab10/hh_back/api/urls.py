# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.list_companies, name='list_companies'),
    path('companies/<int:id>/', views.get_company, name='get_company'),
    path('companies/<int:id>/vacancies/', views.list_vacancies_by_company, name='list_vacancies_by_company'),
    path('vacancies/', views.list_vacancies, name='list_vacancies'),
    path('vacancies/<int:id>/', views.get_vacancy, name='get_vacancy'),
    path('vacancies/top_ten/', views.list_top_ten_vacancies, name='list_top_ten_vacancies'),
]
