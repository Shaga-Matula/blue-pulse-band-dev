from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CommentForm, MusicModForm, UpdateForm
from .models import CommentMod, MusicMod

# from django.urls import reverse_lazy


class CommentDeleteView(View):
    def get(self, request, pk):
        comment = get_object_or_404(CommentMod, pk=pk)
        return render(request, "comments/comment_delete.html", {"comment": comment})

    def post(self, request, pk):
        comment = get_object_or_404(CommentMod, pk=pk)
        comment.delete()
        return redirect("song_all_comments")


class SongCommentEditView(View):
    def get(self, request, pk):
        comment = get_object_or_404(CommentMod, pk=pk)
        form = CommentForm(instance=comment)
        return render(
            request, "comments/comment_edit.html", {"form": form, "comment": comment}
        )

    def post(self, request, pk):
        comment = get_object_or_404(CommentMod, pk=pk)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("song_all_comments")
        return render(
            request, "comments/comment_edit.html", {"form": form, "comment": comment}
        )


class AddCommentToSongView(View):
    def get(self, request, pk):
        song = get_object_or_404(MusicMod, pk=pk)
        form = CommentForm()
        return render(
            request, "comments/add_comment.html", {"form": form, "song": song}
        )

    def post(self, request, pk):
        song = get_object_or_404(MusicMod, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.music = song
            comment.user_profile = (
                request.user.userprofile
            )  # Associate the user profile with the comment
            comment.save()
            return redirect("song_all_comments")
        return render(
            request, "comments/add_comment.html", {"form": form, "song": song}
        )


class SongListCommentView(ListView):
    model = MusicMod
    template_name = "comments/all_songs_comments.html"
    context_object_name = "songs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = CommentMod.objects.all()
        return context


#############################################


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
