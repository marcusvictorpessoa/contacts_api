from .views import ContactsViewSet
from rest_framework.routers import SimpleRouter

ContactsRouter = SimpleRouter()
ContactsRouter.register('contacts', ContactsViewSet)