from rest_framework import serializers

from opros.models import MatterModel, OprosModel


class MatterSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatterModel
        fields = [
            'id',
            'opros',
            'text_matter',
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
