import json

from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND)
from rest_framework.test import APITransactionTestCase

from children.models import Child
from children.tests.factories import ChildFactory
from register.models import Register

from api.tests.utils import gen_image


class ChildViewSetCreateTestCase(APITransactionTestCase):

    reset_sequences = True

    def test_create_child_is_ok(self):
        new_child_data = {
            'photo': gen_image(),
            'name': 'Иван',
            'surname': 'Иванов',
            'patronymic': 'Иванович',
            'sex': Child.MALE,
            'birthday': '2014-12-22',
            'room': '1А',
            'is_study': True,
        }

        response = self.client.post(reverse('api:child'), data=new_child_data)

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Child.objects.all().count(), 1)

    def test_create_without_name(self):
        new_child_data = {
            'photo': gen_image(),
            'surname': 'Иванов',
            'patronymic': 'Иванович',
            'sex': Child.MALE,
            'birthday': '2014-12-22',
            'room': '1А',
            'is_study': True,
        }

        response = self.client.post(reverse('api:child'), data=new_child_data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Child.objects.all().count(), 0)

    def test_create_without_surname(self):
        new_child_data = {
            'photo': gen_image(),
            'name': 'Иван',
            'patronymic': 'Иванович',
            'sex': Child.MALE,
            'birthday': '2014-12-22',
            'room': '1А',
            'is_study': True,
        }

        response = self.client.post(reverse('api:child'), data=new_child_data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Child.objects.all().count(), 0)

    def test_create_without_patronymic(self):
        new_child_data = {
            'photo': gen_image(),
            'name': 'Иван',
            'surname': 'Иванов',
            'sex': Child.MALE,
            'birthday': '2014-12-22',
            'room': '1А',
            'is_study': True,
        }

        response = self.client.post(reverse('api:child'), data=new_child_data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Child.objects.all().count(), 0)

    def test_create_without_photo(self):
        new_child_data = {
            'name': 'Иван',
            'surname': 'Иванов',
            'patronymic': 'Иванович',
            'sex': Child.MALE,
            'birthday': '2014-12-22',
            'room': '1А',
            'is_study': True,
        }

        response = self.client.post(reverse('api:child'), data=new_child_data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Child.objects.all().count(), 0)

    def test_create_without_sex(self):
        new_child_data = {
            'photo': gen_image(),
            'name': 'Иван',
            'surname': 'Иванов',
            'patronymic': 'Иванович',
            'birthday': '2014-12-22',
            'room': '1А',
            'is_study': True,
        }

        response = self.client.post(reverse('api:child'), data=new_child_data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Child.objects.all().count(), 0)

    def test_create_without_birthday(self):
        new_child_data = {
            'photo': gen_image(),
            'name': 'Иван',
            'surname': 'Иванов',
            'patronymic': 'Иванович',
            'sex': Child.MALE,
            'room': '1А',
            'is_study': True,
        }

        response = self.client.post(reverse('api:child'), data=new_child_data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Child.objects.all().count(), 0)

    def test_create_without_room(self):
        new_child_data = {
            'photo': gen_image(),
            'name': 'Иван',
            'surname': 'Иванов',
            'patronymic': 'Иванович',
            'sex': Child.MALE,
            'birthday': '2014-12-22',
            'is_study': True,
        }

        response = self.client.post(reverse('api:child'), data=new_child_data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Child.objects.all().count(), 0)

    def test_create_without_is_study(self):
        new_child_data = {
            'photo': gen_image(),
            'name': 'Иван',
            'surname': 'Иванов',
            'patronymic': 'Иванович',
            'sex': Child.MALE,
            'birthday': '2014-12-22',
            'room': '1А',
        }

        response = self.client.post(reverse('api:child'), data=new_child_data)

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Child.objects.all().count(), 1)


class ChildViewSetListTestCase(APITransactionTestCase):

    reset_sequences = True

    def test_exists_one_child(self):
        child = ChildFactory()

        expected_data = [
            {
                'id': 1,
                'photo': None,
                'birthday': '2014-12-22',
                'surname': 'Иванов',
                'sex': 0,
                'is_study': True,
                'patronymic': 'Иванович',
                'name': 'Иван',
                'room': 'A1'
            }
        ]

        response = self.client.get(reverse('api:child'))
        response_data = json.loads(response.content.decode('utf8'))

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response_data, expected_data)

    def test_child_not_exists(self):
        response = self.client.get(reverse('api:child'))
        response_data = json.loads(response.content.decode('utf8'))

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response_data, [])

    def test_exists_only_no_study_child(self):
        child = ChildFactory(is_study=False)
        response = self.client.get(reverse('api:child'))
        response_data = json.loads(response.content.decode('utf8'))

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response_data, [])


class ChildViewSetUpdateTestCase(APITransactionTestCase):

    reset_sequences = True

    def test_update_child(self):
        child = ChildFactory()

        data = {
            'photo': gen_image(),
            'name': 'Мария',
            'surname': 'Сергеева',
            'patronymic': 'Ивановна',
            'sex': Child.FEMALE,
            'birthday': '2014-12-23',
            'room': 'A1',
            'is_study': True,
        }

        response = self.client.put(
            reverse('api:child-detail', kwargs={'pk': child.id}), data=data)
        response_data = json.loads(response.content.decode('utf8'))

        child.refresh_from_db()

        expected_data = {
            'sex': 1,
            'room': 'A1',
            'birthday': '2014-12-23',
            'id': 1,
            'photo': 'http://testserver{}'.format(child.photo.url),
            'surname': 'Сергеева',
            'name': 'Мария',
            'patronymic': 'Ивановна',
            'is_study': True
        }

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response_data, expected_data)

    def test_update_no_study_child(self):
        child = ChildFactory(is_study=False)

        data = {
            'birthday': '2015-11-26',
        }

        response = self.client.patch(
            reverse('api:child-detail', kwargs={'pk': child.id}), data=data)

        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)


class ChildViewSetPatchTestCase(APITransactionTestCase):

    reset_sequences = True

    def test_patch_birthday_child(self):
        child = ChildFactory()

        data = {
            'birthday': '2015-11-26',
        }

        expected_data = {
            'birthday': '2015-11-26',
            'surname': 'Иванов',
            'is_study': True,
            'photo': None,
            'sex': 0,
            'id': 1,
            'patronymic': 'Иванович',
            'room': 'A1',
            'name': 'Иван'
        }

        response = self.client.patch(
            reverse('api:child-detail', kwargs={'pk': child.id}), data=data)
        response_data = json.loads(response.content.decode('utf8'))

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response_data, expected_data)

    def test_patch_no_study_child(self):
        child = ChildFactory(is_study=False)

        data = {
            'birthday': '2015-11-26',
        }

        response = self.client.patch(
            reverse('api:child-detail', kwargs={'pk': child.id}), data=data)

        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)


class RegisterViewSetCreateTestCase(APITransactionTestCase):

    reset_sequences = True

    def test_create_register_is_ok(self):
        child = ChildFactory()
        data = {
            'child': child.id,
            'delegate_type': Register.MOTHER
        }

        response = self.client.post(reverse('api:register'), data=data)

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Register.objects.all().count(), 1)

    def test_create_without_delegate_type(self):
        child = ChildFactory()
        data = {
            'child': child.id,
        }

        response = self.client.post(reverse('api:register'), data=data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Register.objects.all().count(), 0)

    def test_create_with_not_existed_child(self):
        data = {
            'child': 99,
            'delegate_type': Register.FATHER
        }

        response = self.client.post(reverse('api:register'), data=data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Register.objects.all().count(), 0)

    def test_create_with_child_not_study(self):
        child = ChildFactory(is_study=False)
        data = {
            'child': child.id,
            'delegate_type': Register.FATHER
        }

        response = self.client.post(reverse('api:register'), data=data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Register.objects.all().count(), 0)
