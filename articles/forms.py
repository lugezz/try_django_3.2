from django import forms


class ArticleForm(forms.Form):
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
