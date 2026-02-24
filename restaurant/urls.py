from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]

# بنضيف روابط الـ router لليستة الـ urlpatterns
urlpatterns += router.urls