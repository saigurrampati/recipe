from django.urls import path
from . import views

app_name = "recipe"
urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('register_page/', views.register_page, name='register_page'),
    path('login_status/', views.login_status, name='login_status'),
    path('save_data/', views.save_data, name='save_data'),
    path('create/', views.create, name="create"),
    path('save/', views.save, name="save"),
    path('recipe_list/', views.recipe_list, name="recipe_list"),
    path('<int:recipe_id>/details/', views.details, name="details"),
    path('<int:recipe_id>/delete/', views.delete, name="delete"),
    path('logout/', views.logout_user, name='logout_user')
]
