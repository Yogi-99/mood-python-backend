from django.urls import path
from apis import views

urlpatterns = [
    path('rest-get/', views.RestAPIView.as_view())
]
