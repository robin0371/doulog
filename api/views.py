from rest_framework.viewsets import ModelViewSet

from children.models import Child

from api.serializers import ChildSerializer


class ChildViewSet(ModelViewSet):

    serializer_class = ChildSerializer
    queryset = Child.objects.filter(is_study=True)
