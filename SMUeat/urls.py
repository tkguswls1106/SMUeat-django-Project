from django.urls import path

from . import views

urlpatterns = [
    path('', views.place_list, name="place-list"),
    path('place/<int:place_id>/review/list/', views.review_list, name='review-list'),
    path('place/<int:place_id>/delete/', views.place_delete, name='place-delete'),
    path('place/<int:place_id>/review/<int:review_id>/update/', views.review_update, name='review-update'),
    path('place/<int:place_id>/review/<int:review_id>/delete/', views.review_delete, name='review-delete'),
    path('place/create/', views.place_create, name="place-create"),
    path('place/<int:place_id>/review/create/', views.review_create, name="review-create"),
    path('search/', views.search, name='search'),

    path('place/<int:place_id>/review/list/<str:sorting_name>/', views.review_sorting, name='review-sorting'),
    path('place/<str:category_link>/list/<str:sorting_name>/', views.place_sorting, name='place-sorting'),
]