from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, JsonResponse

from django.urls import reverse_lazy
from .models import LuckyDay, NotePost
from .forms import PostForm

# Create your views here.

def homePageView(request):
    return render(request, 'home.html')

def aboutPageView(request):
    return render(request, 'about.html')

class Cal1PageView(TemplateView):
    model = LuckyDay
    template_name = 'cal_1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['data'] = [
            {
                'id': obj.id,
                'rnk': obj.rnk,
                'datex': obj.datex.isoformat()
            }
            for obj in LuckyDay.objects.all()
        ]

        return context

class ShowDataPageView(ListView):
    model = LuckyDay
    template_name = 'alldata.html'        

class BlogListView(ListView):
    model = NotePost
    template_name = 'manage.html'
    

class BlogDetailView(DetailView):
    model = NotePost
    template_name = 'manage_detail.html'


class AddDisView(CreateView):
    model = NotePost
    form_class = PostForm
    template_name = 'add_dis.html'


class UpdateDisView(UpdateView):
    model = NotePost
    form_class = PostForm
    template_name = 'edit_dis.html'
    #fields = ['is_good_day', 'reason']

class DeleteDisView(DeleteView):
    model = NotePost
    template_name = 'delete_dis.html'
    success_url = reverse_lazy('removesuc')

def delPageView(request):
    return render(request, 'removesuc.html')
    

# New
#class SomeTemplateView(TemplateView):
 #   template_name = 'cal_1.html'

  #  def get_context_data(self, **kwargs):
   #     context = super().get_context_data(**kwargs)

   #     context['data'] = [
    #        {
   #             'id': LuckyDay.id,
   #             'date_rec': LuckyDay.date.isoformat()
                
  #          }
   #         for LuckyDay in LuckyDay.objects.all()
   #     ]
  #      return context