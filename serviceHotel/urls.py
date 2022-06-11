from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hotels', HotelViewSet)
router.register('rooms', RoomViewSet)


urlpatterns = [
	path('', include(router.urls)),

    # path('calc-rvenders/', CalcRevendeursStat.as_view(), name="calculate-revendeurs"),

]