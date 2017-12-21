import datetime

import factory

from children.tests.factories import ChildFactory
from register.models import Register


class RegisterFactory(factory.django.DjangoModelFactory):

    child = factory.SubFactory(ChildFactory)
    time = datetime.datetime.now().time()
    delegate_type = Register.MOTHER
    date = datetime.datetime.now().date()

    class Meta:
        model = Register
