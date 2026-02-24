from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# 1. View الخاص بالحجوزات (تم دمج التكرار وتصحيح اسم المتغير)
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # ملاحظة: الاسم الصحيح للمتغير هو permission_classes (بالجمع s)
    permission_classes = [IsAuthenticated] 

# 2. View الخاص بالمنيو (ليستة وعرض)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# 3. View الخاص بصنف واحد (تعديل وحذف وعرض)
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer