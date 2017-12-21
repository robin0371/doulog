from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from children.models import Child
from register.models import Register


class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Child


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Register

    def validate(self, attrs):
        attrs = super().validate(attrs)
        child = attrs['child']

        if not child.is_study:
            raise ValidationError(
                'Ребенок {}, не является учащимся'.format(child))

        return attrs