from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import MusicMod

class MusicModForm(forms.ModelForm):
    class Meta:
        model = MusicMod
        fields = ['artist_name', 'song_title', 'song_file', 'song_image']

    def __init__(self, *args, **kwargs):
        super(MusicModForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal text-white'
        self.helper.label_class = 'col-lg-2 form_color_music'
        self.helper.field_class = 'col-lg-8 '
        self.helper.layout = Layout(
            'artist_name',
            'song_title',
            'song_file',
            'song_image',
            Submit('submit', 'Save')
        )