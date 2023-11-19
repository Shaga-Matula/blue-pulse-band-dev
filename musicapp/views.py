from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CommentForm, MusicModForm
from .models import CommentMod, MusicMod


class CommentDeleteView(DeleteView):
    model = CommentMod
    success_url = reverse_lazy("song_all_comments")

    def get_object(self, queryset=None):
        return get_object_or_404(CommentMod, pk=self.kwargs["pk"])

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.delete()
        success_message = f"Comment has been successfully deleted."
        messages.success(self.request, success_message)
        return redirect(self.success_url)


class SongCommentEditView(DeleteView):
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
            success_message = f"Comment has been successfully edited ."
            messages.success(self.request, success_message)
            form.save()
            return redirect("song_all_comments")
        return render(
            request, "comments/comment_edit.html", {"form": form, "comment": comment}
        )


class AddCommentToSongView(CreateView):
    model = CommentMod  # Specify the model
    template_name = "comments/comment_add.html"
    form_class = CommentForm

    def form_valid(self, form):
        song = get_object_or_404(MusicMod, pk=self.kwargs["pk"])
        form.instance.music = song
        form.instance.user_profile = self.request.user.userprofile
        return super().form_valid(form)

    def get_success_url(self):
        success_message = f"Comment has been created successfully."
        messages.success(self.request, success_message)
        return reverse("song_all_comments")


class SongListCommentView(ListView):
    model = MusicMod
    template_name = "comments/all_songs_comments.html"
    context_object_name = "songs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = CommentMod.objects.all()
        return context


###########
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
    form_class = MusicModForm
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
