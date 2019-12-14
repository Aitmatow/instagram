from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from webapp.forms import ImageForm
from webapp.models import Image, Comment


class ImageList(ListView):
    template_name = 'images/images_list.html'
    model = Image
    paginate_by = 5
    paginate_orphans = 1
    page_kwarg = 'page'
    ordering = ['-created']


class ImageDetail(DetailView):
    template_name = 'images/images_detail.html'
    model = Image

    def get_context_data(self, **kwargs):
        context = super(ImageDetail, self).get_context_data(**kwargs)
        image = Image.objects.get(id=self.kwargs.get('pk'))
        context['comments'] = Comment.objects.filter(image=image)
        return context

class ImageCreate(CreateView):
    template_name = 'images/images_form.html'
    model = Image
    fields = ['image', 'text']
    success_url = reverse_lazy('images_list')
    # form_class = ImageForm

    # def get_form(self, form_class=None):
    #     form = super(ImageCreate,self).get_form()
    #     form.fields['author'].queryset = User.objects.filter(username=self.request.user)
    #     return form

    def form_valid(self, form):
        """If the form is valid, save the associated model."""

        Image.objects.create(
            image=form.cleaned_data.get('image'),
            text=form.cleaned_data.get('text'),
            author=self.request.user
        )
        return redirect('images_list')


class ImageUpdate(UpdateView):
    template_name = 'images/images_form.html'
    model = Image
    fields = ['image', 'text', 'likes', 'author']
    success_url = reverse_lazy('images_list')

class ImageDelete(DeleteView):
    template_name = 'images/images_delete.html'
    model = Image
    success_url = reverse_lazy('images_list')