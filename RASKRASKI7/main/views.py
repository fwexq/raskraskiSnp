from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *
from .models import *
from .utils import *
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .services import open_file


def get_list_video(request):
    return render(request, 'main/home.html', {'video_list': picture.objects.all()})


class get_video(DataMixin, DetailView):
    model = picture
    template_name = 'main/video.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'video'

def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response

class create(DataMixin, CreateView):
    form_class = pictureForm
    template_name = 'main/create.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Создание поста')
        return context | c_def


class show_category(DataMixin, ListView):
    model = picture
    template_name = 'main/category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return picture.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                                                  cat_selected=context['posts'][0].cat_id)
        return context | c_def



class Search(ListView):
    model = picture
    template_name = 'main/search_results.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return picture.objects.filter(title__icontains=self.request.GET['q'])


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.request.GET['q']
        return context



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Создание поста')
        return context | c_def


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'


    def get_user_context(self, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return c_def | context

    def get_success_url(self):
        return reverse_lazy('home')



def logoutuser(request):
    logout(request)
    return redirect('login')

