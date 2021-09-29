
from django.shortcuts import redirect, render
from .models import post
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# from .forms import contactform
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

# def index(request):
#     posts = post.objects.all().order_by('-created_at')
#     return render(request, 'index.html', {'posts': posts})
def about(request):
    return render(request, 'about.html')
def contact(request):
    # if request.method == 'POST':
    #     form = contactform(request.POST)
    #     if form.is_valid():
    #         subject = "Website Inquiry"
    #         body ={
    #             'name' : form.cleaned_data['name'],
    #             'email_address' : form.cleaned_data['email_address'],
    #             'message':form.cleaned_data['message']
    #         }
    #         message = "\n".join(body.values())

    #         try:
    #             send_mail(subject, message, 'ghada.a.a.alrajhi@gmail.com', ['ghada.a.a.alrajhi@gmail.com'])
    #         except:
    #             return HttpResponse('Invalid header found')
    #         return redirect('/')
    # form = contactform()
    return render(request, 'contact.html')

# def posts(request, pk):
#     Post= post.objects.get(id = pk)
#     return render(request, 'posts.html', {'Post': Post})
class HomeView(ListView):
    model = post
    template_name = 'index.html'
class ArticaleDetailView(DetailView):
    model = post
    template_name = 'Article.html'

class AddPostView(CreateView):
    model = post
    template_name = 'post_form.html'
    fields = '__all__'
    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return super(AddPostView, self).form_valid(form)

class UpdatePostView(UpdateView):
    model = post
    template_name = 'update_post.html'
    fields = ['title', 'content', 'image']
class DeletePost(DeleteView):
    model = post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')
