import datetime

import factory

from children.models import Child


class ChildFactory(factory.django.DjangoModelFactory):

    name = 'Иван'
    surname = 'Иванов'
    patronymic = 'Иванович'
    sex = Child.MALE
    birthday = datetime.date(2014, 12, 22)
    room = 'A1'
    is_study = True

    class Meta:
        model = Child
