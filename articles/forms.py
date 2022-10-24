from django import forms

from articles.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data  # dictionary
    #     title = cleaned_data.get('title')

    #     if title.lower().strip() == 'cachula':
    #         raise forms.ValidationError('Ponete las pilas y elegí otro')

    #     return title

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     content = cleaned_data.get('content')

    #     if 'office' in content:
    #         # raise forms.ValidationError('Nada de trabajo aquí') # Hace un error con referencia a todo el formulario
    #         self.add_error('content', 'Nada de trabajo aquí')  # Hace que sea un error más en la lista, de la
    #         # misma forma que trabaja cada clean_... independiente

    #     return cleaned_data


class ExArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data  # dictionary
        title = cleaned_data.get('title')

        if title.lower().strip() == 'cachula':
            raise forms.ValidationError('Ponete las pilas y elegí otro')

        return title

    def clean(self):
        cleaned_data = self.cleaned_data
        content = cleaned_data.get('content')

        if 'office' in content:
            # raise forms.ValidationError('Nada de trabajo aquí') # Hace un error con referencia a todo el formulario
            self.add_error('content', 'Nada de trabajo aquí')  # Hace que sea un error más en la lista, de la
            # misma forma que trabaja cada clean_... independiente

        return cleaned_data
