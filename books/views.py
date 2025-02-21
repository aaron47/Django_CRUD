from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"

class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'publication_date']
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Book "{self.object.title}" was successfully added!')
        return response

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'publication_date']
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Book "{self.object.title}" was successfully updated!')
        return response


class BookDeleteView(SuccessMessageMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

    def get_success_message(self, cleaned_data):
        return f'Book "{self.object.title}" was successfully deleted!'