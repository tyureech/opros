from django.db import models
# Create your models here.


class IDUser(models.Model):
    session = models.BooleanField(default=False)


class ResultOpros(models.Model):
    user = models.ForeignKey('IDUser', on_delete=models.CASCADE, verbose_name='Результат опороса')
    opros = models.ForeignKey('OprosModel', on_delete=models.CASCADE, verbose_name='Опрос')
    text_matter = text_matter = models.TextField(max_length=100, verbose_name='Вопрос')
    number_matter = models.IntegerField()
    text_answer = models.TextField(max_length=100, verbose_name='тесктовый вариант ответа', null=True, blank=True)
    option_answer1 = models.CharField(max_length=100, verbose_name='вариант ответа 1', null=True, blank=True)
    option_answer2 = models.CharField(max_length=100, verbose_name='вариант ответа 2', null=True, blank=True)
    option_answer3 = models.CharField(max_length=100, verbose_name='вариант ответа 3', null=True, blank=True)
    option_answer4 = models.CharField(max_length=100, verbose_name='вариант ответа 4', null=True, blank=True)
    def __str__(self):
        return self.text_matter

    class Meta:
        verbose_name_plural = 'Ответ на вопрос'


class MatterModel(models.Model):
    # user = models.ForeignKey('IDUser', on_delete=models.CASCADE, verbose_name='ID_USER', null=True, blank=True)
    opros = models.ForeignKey('OprosModel', on_delete=models.CASCADE, verbose_name='Опрос')
    text_matter = models.TextField(max_length=100, verbose_name='Вопрос')
    number_matter = models.IntegerField()
    text_answer = models.TextField(max_length=100, verbose_name='тесктовый вариант ответа', null=True, blank=True)
    option_answer1 = models.CharField(max_length=100, verbose_name='вариант ответа 1', null=True, blank=True)
    option_answer2 = models.CharField(max_length=100, verbose_name='вариант ответа 2', null=True, blank=True)
    option_answer3 = models.CharField(max_length=100, verbose_name='вариант ответа 3', null=True, blank=True)
    option_answer4 = models.CharField(max_length=100, verbose_name='вариант ответа 4', null=True, blank=True)

    ОДИНАРНЫЙ = 'ОД'
    МНОЖЕСТВЕННЫЙ = 'МН'
    ТЕКСТОВЫЙ = 'ТК'
    TYPE_MATTER = [
        (ОДИНАРНЫЙ, 'Один ответ на выбор'),
        (МНОЖЕСТВЕННЫЙ, 'Множественный ответ'),
        (ТЕКСТОВЫЙ, 'Текстовый ответ'),
    ]
    type_matter = models.CharField(
        max_length=2,
        choices=TYPE_MATTER,
        default=ОДИНАРНЫЙ,
        verbose_name='Тип ответа'
    )

    def __str__(self):
        return self.text_matter

    class Meta:
        verbose_name_plural = 'Вопрос'


class OprosModel(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название опроса')
    start_date = models.DateField(verbose_name='Дата начала опроса', null=True)
    end_date = models.DateField(verbose_name='Конечная дата опроса', null=True)
    description = models.TextField(verbose_name='Описание опроса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Опрос'


# class TypeMatter(models.Model):
#     ОДИНАРНЫЙ = 'ОД'
#     МНОЖЕСТВЕННЫЙ = 'МН'
#     ТЕКСТОВЫЙ = 'ТК'
#     TYPE_MATTER = [
#         (ОДИНАРНЫЙ, 'Один ответ на выбор'),
#         (МНОЖЕСТВЕННЫЙ, 'Множественный ответ'),
#         (ТЕКСТОВЫЙ, 'Текстовый ответ'),
#     ]
#     type_matter = models.CharField(
#         max_length=2,
#         choices=TYPE_MATTER,
#         default=ОДИНАРНЫЙ,
#         verbose_name='Тип ответа'
#     )
