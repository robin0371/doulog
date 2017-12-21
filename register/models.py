from django.db import models

from children.models import Child


class Register(models.Model):
    """Журнал привода/забирания детей из сада."""

    MOTHER = 0
    FATHER = 1
    DELEGATE_CHOICES = (
        (MOTHER, 'Мать'),
        (FATHER, 'Отец'),
    )

    child = models.ForeignKey(Child)

    delegate_type = models.PositiveSmallIntegerField('Кто привел/забрал')
    date = models.DateField('Дата', auto_now_add=True)
    time = models.TimeField('Время когда привели/забрали', auto_now_add=True)

    class Meta:
        verbose_name = 'Запись журнала привода/забирания детей из сада'
        verbose_name_plural = 'Записи журнала привода/забирания детей из сада'

    def __str__(self):
        return '{0} {1} {2}'.format(self.date, self.time, self.child)
