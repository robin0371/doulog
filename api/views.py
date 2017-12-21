from rest_framework.viewsets import ModelViewSet

from children.models import Child

from api.serializers import ChildSerializer, RegisterSerializer
from register.models import Register


class ChildViewSet(ModelViewSet):

    serializer_class = ChildSerializer
    queryset = Child.objects.filter(is_study=True)


class RegisterViewSet(ModelViewSet):

    serializer_class = RegisterSerializer
    queryset = Register.objects.all()
