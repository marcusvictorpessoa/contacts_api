from rest_framework import viewsets
from .serializers import ContactsSerializer
from .models import Contacts

class ContactsViewSet(viewsets.ModelViewSet):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()