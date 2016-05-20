from django import forms
from .models import Aluno


class AlunoForm(forms.ModelForm):
    dt_nasc = forms.DateField(label=u'Data de Nascimento',
                              widget=forms.TextInput(attrs={
                                  'id': 'datepicker'}))

    class Meta:
        model = Aluno
        fields = ('nome', 'dt_nasc', 'rg', 'endereco', 'obs',)
