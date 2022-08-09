from django.urls import path
from . import views

urlpatterns = [
    # GET
    path('', views.get_users),
    # POST
    path('post', views.post_user),
    # DELETE
    path('delete/<str:id>', views.delete_user),
    # PUT
    path('put/<str:id>', views.update_user),
]
