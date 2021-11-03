from django.http import QueryDict
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse

from django import forms

from .models import OprosModel, MatterModel, IDUser, ResultOpros
from .forms import MatterForm, OprosForm, MatterChoicesForm
from .utils import create_choice


class UpdateMatter(View):
    def get(self, request, pk, kp):
        matters_list = MatterModel.objects.filter(opros__id=pk)
        matter = matters_list.get(id=kp)
        form = MatterForm(instance=matter)
        context = {
            'form': form,
            'matters': matters_list,
            'number_matter': matter.number_matter,
            'pk': pk,
            'update_id': kp
        }
        return render(request, 'create_matter.html', context)

    def post(self, request, pk, kp):
        matter = MatterForm(request.POST)
        if matter.is_valid():
            if matter.cleaned_data['type_matter'] == 'ТК' and matter.cleaned_data['option_answer1'] and \
                    matter.cleaned_data['option_answer2'] \
                    and matter.cleaned_data['option_answer3'] and matter.cleaned_data['option_answer4']:
                matter.add_error('option_answer1', 'Поле должно быть пустым!')
                matter.add_error('option_answer2', 'Поле должно быть пустым!')
                matter.add_error('option_answer3', 'Поле должно быть пустым!')
                matter.add_error('option_answer4', 'Поле должно быть пустым!')
            MatterModel.objects.filter(id=kp).update(opros=OprosModel.objects.get(id=pk), **matter.cleaned_data)

        return redirect('update_matter', pk, kp)


class CreateMatter(View):

    def get(self, request, pk):
        matters_list = MatterModel.objects.filter(opros__id=pk)
        context = {
            'form': MatterForm,
            'matters': matters_list,
            'number_matter': len(matters_list) + 1,
            'pk': pk,
        }
        return render(request, 'create_matter.html', context)

    def post(self, request, pk):
        matter = MatterForm(request.POST)
        if matter.is_valid():
            if matter.cleaned_data['type_matter'] == 'ТК' and matter.cleaned_data['option_answer1'] and \
                    matter.cleaned_data['option_answer2'] \
                    and matter.cleaned_data['option_answer3'] and matter.cleaned_data['option_answer4']:
                matter.add_error('option_answer1', 'Поле должно быть пустым!')
                matter.add_error('option_answer2', 'Поле должно быть пустым!')
                matter.add_error('option_answer3', 'Поле должно быть пустым!')
                matter.add_error('option_answer4', 'Поле должно быть пустым!')
            print(matter.cleaned_data)
            matter = matter.save(commit=False)
            print(matter)
            matter.opros_id = pk
            matter.save()
        return redirect('create_matter', pk=pk)


def delete_matter(request, pk, kp):
    opros = MatterModel.objects.get(id=kp)
    opros.delete()
    return redirect('create_matter', pk)


def list_opros(request):
    return render(request, 'list_opros.html', {'content': OprosModel.objects.all()})


class UpdateOpros(UpdateView):
    model = OprosModel
    template_name = 'create_opros.html'
    form_class = OprosForm
    success_url = reverse_lazy('list_opros')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        print(kwargs)
        data['pk'] = self.kwargs['pk']

        return data


class CreateOpros(CreateView):
    model = OprosModel
    template_name = 'create_opros.html'
    form_class = OprosForm

    def get_success_url(self):
        return reverse('create_matter', kwargs={'pk': self.object.id})


def delete_opros(request, pk):
    opros = OprosModel.objects.get(id=pk)
    opros.delete()
    return redirect('list_opros')


def list_start_opros(request):
    return render(request, 'list_opros.html', {'content': OprosModel.objects.all(), 'start': True})


class StartOpros(View):

    def get(self, request, pk):
        opros = OprosModel.objects.get(id=pk)
        try:
            user = IDUser.objects.get(session=True)
        except:
            user = IDUser.objects.create(session=True)

        context = {
            'user_id': user.id,
            'opros': opros,
        }
        return render(request, 'start_opros.html', context)


class MatterOpros(View):
    def get(self, request, pk, user_id, kp):
        matters = MatterModel.objects.filter(opros__id=pk)
        opros = OprosModel.objects.get(id=pk)
        choices = None
        text = None
        matter = None
        if kp <= len(matters):
            choices = MatterChoicesForm()
            matter = matters[kp - 1]
            if matter.type_matter != 'ТК':
                if matter.type_matter == 'МН':
                    widget = forms.CheckboxSelectMultiple
                if matter.type_matter == 'ОД':
                    widget = forms.RadioSelect
                choices.fields['Варианты'] = forms.MultipleChoiceField(
                    required=False,
                    widget=widget,
                    choices=create_choice(
                        matter.option_answer1,
                        matter.option_answer2,
                        matter.option_answer3,
                        matter.option_answer4,
                    )
                )
            else:
                choices = None
                text = matter.type_matter
            ResultOpros.objects.get_or_create(
                opros=opros,
                user=IDUser.objects.get(id=user_id),
                number_matter=kp,
                text_matter=matter.text_matter,
                defaults={
                    'opros': opros,
                    'user': IDUser.objects.get(id=user_id),
                    'number_matter': kp,
                    'text_matter': matter.text_matter,
                },
            )
        context = {
            'opros': opros,
            'matter': matter,
            'choices': choices,
            'pk': pk,
            'kp': kp,
            'TK': text,
            'user_id': user_id,
        }
        return render(request, 'matter_opros.html', context)

    def post(self, request, pk, user_id, kp):
        req = request.POST
        data_dict = {}
        if req.get('description'):
            data_dict['text_answer'] = req['description']
        if req.get('Варианты'):
            if len(req['Варианты']) == 1:
                data_dict['option_answer1'] = req['Варианты']
            else:
                req_list = req.getlist('Варианты')
                for i in range(4):
                    if i < len(req_list):
                        data_dict['option_answer' + str(i + 1)] = req_list[i]
                    else:
                        data_dict['option_answer' + str(i + 1)] = None
        ResultOpros.objects.filter(
            opros=OprosModel.objects.get(id=pk),
            user=IDUser.objects.get(id=user_id),
            number_matter=kp,
        ).update(**data_dict)
        return redirect('matter_opros', pk, user_id, kp + 1)


def list_result(request, pk, user_id):
    opros = OprosModel.objects.get(id=pk)
    result = ResultOpros.objects.filter(
        opros=opros,
        user=IDUser.objects.get(id=user_id),
    )
    return render(request, 'list_result.html', context={'result': result, 'opros': opros})


def home(request):
    return render(request, 'home.html')
