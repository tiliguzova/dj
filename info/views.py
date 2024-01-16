from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from fda.form import InfoForm
from info.models import Info


# Create your views here.
def main(request):
    return render(request, 'index.html')


def read_pizza(request):
    return render(request, 'all.html')


def contest(request):
    return render(request, 'contest.html')


# class MarksView(View):
#     def get(self, request, id=None):
#         marks = Info.objects.filter(is_buy=True)
#         if id:
#             mark = Info.objects.filter(id=id, is_buy=True).first()
#             return render(request, "mark.html", context={
#                 'mark': mark
#             })
#         return render(request, "marks.html", context={
#             'marks': marks
#         })

class MarkListView(generic.ListView):
    # model = Info
    template_name = 'info_mark/mark_list.html'
    context_object_name = 'marks'
    queryset = Info.objects.filter(is_buy=True)
    # ordering = 'price'
    #
    # def get_queryset(self):
    #     return self.queryset.order_by('price', 'rating')


class MarkCreateView(generic.CreateView):
    # model = Info
    template_name = 'info_mark/mark_create.html'
    form_class = InfoForm
    # fields = ('name', 'text', 'rating', 'price')
    # success_url = '/'

    def get_success_url(self):
        return reverse('mark-list')


class MarkDetailView(generic.DetailView):
    model = Info
    template_name = 'info_mark/mark_detail.html'
    context_object_name = 'mark'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Info.objects.filter(is_buy=True)
        return context


class MarkUpdateView(generic.UpdateView):
    model = Info
    template_name = 'info_mark/mark_update.html'
    form_class = InfoForm

    # fields = ('name', 'text', 'rating', 'price')
    # success_url = '/'
    def get_success_url(self):
        return reverse('mark-list')


class MarkDeleteView(generic.DeleteView):
    model = Info
    template_name = 'info_mark/mark_delete.html'

    def get_success_url(self):
        return reverse('mark-list')
