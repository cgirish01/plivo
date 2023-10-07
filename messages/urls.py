
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, create_message, get_messages, lol, search_messages

router = DefaultRouter()
router.register(r'get/messages/(?P<account_id>\d+)', MessageViewSet)
router.register(r'search', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', create_message),
    path('get/messages/<str:account_id>/', get_messages, name='get_messages'),
    path('search/', search_messages, name='search_messages'),
]
