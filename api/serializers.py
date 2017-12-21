from rest_framework import serializers

from children.models import Child


class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Child
