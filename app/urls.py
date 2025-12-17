from django.urls import path
from .views import ProductAPIView,AuthorAPIView,AuthorDetailDestroyUpdateAPIView,ProductDetailDestroyUpdateAPIView

urlpatterns = [
    path('',ProductAPIView.as_view()),
    path('pr/<int:pk>/', ProductDetailDestroyUpdateAPIView.as_view()),
    path('author/',AuthorAPIView.as_view()),
    path('',AuthorAPIView.as_view())
]
