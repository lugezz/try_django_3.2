from django import forms

class ArticleForm (forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data #dictionary
        title = cleaned_data.get('title')
        
        if title.lower().strip() == 'cachula':
            raise forms.ValidationError('Ponete las pilas y elegí otro')

        return title

    def clean (self):
        cleaned_data = self.cleaned_data

        return cleaned_data