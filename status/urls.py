from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('schedule',views.ScheduleViewSet, basename='schedule')
router.register('status',views.StatusViewSet,basename='status')
urlpatterns = router.urls
print(urlpatterns)