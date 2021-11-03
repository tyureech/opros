from django.core.management.base import BaseCommand

from opros.models import OprosModel, MatterModel


def term_text(data, object_d):
    print(object_d, data)


def create_data_test_opros():
    opros = OprosModel.objects.get_or_create(
        name='Покупательское поведение потребителя',
        description='Здравствуйте, потратьте, пожалуйста, несколько минут своего времени на заполнение следующей '
                    'анкеты.',
        defaults={
            'name': 'Покупательское поведение потребителя',
            'description': 'Здравствуйте, потратьте, пожалуйста, несколько минут своего времени на заполнение '
                           'следующей анкеты.',
        }
    )
    if opros[1]:
        data_matters = [
        {
            'opros': opros[0],
            'text_matter': 'Где Вы покупаете одежду?(можно выбрать несколько вариантов)',
            'number_matter': 1,
            'text_answer': None,
            'option_answer1': 'В торговых центрах',
            'option_answer2': 'В бакалее',
            'option_answer3': 'В специализированных магазинах',
            'option_answer4': 'В интернетах своих)',
            'type_matter': 'МН',
        },
        {
            'opros': opros[0],
            'text_matter': 'Каким образом Вы обычно оплачиваете товар?',
            'number_matter': 2,
            'text_answer': None,
            'option_answer1': 'Наличными деньгами',
            'option_answer2': 'Платежной картой',
            'option_answer3': 'Смартфоном(NFC)',
            'option_answer4': 'Онлайн переводом',
            'type_matter': 'ОД',
        },
        {
            'opros': opros[0],
            'text_matter': 'Напишите минимум 3 товара, которые Вы чаще всего покупаете?',
            'number_matter': 3,
            'text_answer': None,
            'option_answer1': None,
            'option_answer2': None,
            'option_answer3': None,
            'option_answer4': None,
            'type_matter': 'ТК',
        },
    ]

        for matter in data_matters:
            reviews_data = MatterModel.objects.create(**matter)
            term_text(reviews_data, 'Вопрос добавлен')
        term_text(opros, 'Опрос добавлен')


class Command(BaseCommand):

    def handle(self, *args, **options):
        if options['test_opros']:
            create_data_test_opros()

    def add_arguments(self, parser):
        parser.add_argument(
            '-to',
            '--test_opros',
            action='store_true',
            default=False,
            help='Создает тестовый опрос в базе'
        )
