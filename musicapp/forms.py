from crispy_forms.helper import FormHelper

from crispy_forms.layout import Layout, Row, Column, Submit


from django import forms
from .models import MusicMod, CommentMod

class MusicModForm(forms.ModelForm):
    class Meta:
        model = MusicMod
        fields = ['artist_name', 'song_title', 'song_file', 'song_image']

    def __init__(self, *args, **kwargs):
        super(MusicModForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2 '
        self.helper.field_class = 'col-lg-8 '
        self.helper.layout = Layout(
            'artist_name',
            'song_title',
            'song_file',
            'song_image',
            Submit('submit', 'Save')
        )


# forms.py


class UpdateForm(forms.ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Column('artist_name', css_class='mb-3'),
            Column('song_title', css_class='mb-3'),
            css_class='mb-4'
        ),
        Row(
            Column('song_file--', css_class=''),
            Column('song_image', css_class='mb-3'),
            css_class='mb-4'
        ),
        Submit('submit', 'Save', css_class='btn btn-primary mt-5'),
    )
    
    class Meta:
        model = MusicMod
        fields = ['artist_name', 'song_title', 'song_file', 'song_image']
    



class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentMod
        fields = ['text']
