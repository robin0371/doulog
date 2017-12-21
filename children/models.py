from django.db import models


class Child(models.Model):
    """Ребенок."""

    MALE = 0
    FEMALE = 1
    SEX_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    photo = models.ImageField('Фото', upload_to='children/photo')

    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    patronymic = models.CharField('Отчество', max_length=20)

    sex = models.PositiveSmallIntegerField('Пол', choices=SEX_CHOICES)
    birthday = models.DateField('Дата рождения')

    room = models.CharField('Класс', max_length=10)
    is_study = models.BooleanField('Учится или нет', default=False)

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'

    def fio(self):
        return '{0} {1} {2}'.format(self.surname, self.name, self.patronymic)

    def __str__(self):
        return '{0} {1} {2}'.format(self.fio(), self.birthday, self.room)
