from django.urls import path
from users.infraestructure.entrypoint.api import views

urlpatterns = [
    path('', views.create_user, name="create"),
    path('all', views.get_all, name="get_all"),
    path('<int:uid>', views.get_one, name="get_one"),
    path('<int:uid>/update', views.update_user, name="update"),
    path('<int:uid>/delete', views.delete_user, name="delete"),
]
