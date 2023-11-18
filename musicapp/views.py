from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import MusicModForm, UpdateForm, CommentForm
from .models import MusicMod

from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import CommentMod
# from django.urls import reverse_lazy


from django.shortcuts import render, get_object_or_404


class AllCommentsView(DetailView):
    model = MusicMod
    template_name = 'comments/all_comments.html'
    context_object_name = 'music'

    def get_object(self, queryset=None):
        music_id = self.kwargs.get('music_id')
        return get_object_or_404(MusicMod, pk=music_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context





class SongListView(ListView):
    model = MusicMod
    template_name = "musicapp/song_list.html"
    context_object_name = "songs"


class SongCreateView(CreateView):
    model = MusicMod
    form_class = MusicModForm
    template_name = "musicapp/song_form.html"
    success_url = reverse_lazy("song_list")

    def form_valid(self, form):
        messages.success(
            self.request,
            f"Successfully added {form.instance.artist_name} - {form.instance.song_title} to the database.",
        )
        return super().form_valid(form)


class SongUpdateView(UpdateView):
    model = MusicMod
    form_class = UpdateForm
    template_name = "musicapp/song_update.html"
    success_url = reverse_lazy("song_list")

    def form_valid(self, form):
        messages.success(
            self.request,
            f"Successfully updated {form.instance.artist_name} - {form.instance.song_title}.",
        )
        return super().form_valid(form)


class SongDeleteView(DeleteView):
    model = MusicMod
    template_name = "musicapp/song_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("song_list")

    def delete(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            messages.error(self.request, "Sorry, only administrators can delete songs.")
            return self.handle_no_permission()

        messages.success(
            self.request,
            f"Successfully deleted {self.get_object().artist_name} - {self.get_object().song_title}.",
        )
        return super().delete(request, *args, **kwargs)



# ################################

