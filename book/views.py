from django.shortcuts import render
from .models import Books,Author
from django.views import generic


class BookView(generic.TemplateView):
    template_name = 'book/book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_data'] = Books.objects.all()
        context['title_publish'] = Books.objects.values('title', 'published_date')
        context['new_authors'] = Author.objects.filter(popularity_score=0).values('firstname')

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)