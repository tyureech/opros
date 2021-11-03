from rest_framework import serializers

from opros.models import MatterModel, OprosModel, ResultOpros


class MatterSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatterModel
        fields = [
            'id',
            'opros',
            'text_matter',
            'type_matter',
            'number_matter',
            'text_answer',
            'option_answer1',
            'option_answer2',
            'option_answer3',
            'option_answer4',
        ]


class OprosSerializer(serializers.ModelSerializer):

    class Meta:
        model = OprosModel
        fields = [
            'id',
            'name',
            'start_date',
            'end_date',
            'description',
        ]


class ResultOprosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultOpros
        fields = [
            'id',
            'user',
            'opros',
            'text_matter',
            'number_matter',
            'text_answer',
            'option_answer1',
            'option_answer2',
            'option_answer3',
            'option_answer4',
        ]
