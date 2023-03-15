from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BlogPost, Blogger, BlogComment

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

class BlogListView(generic.ListView):
    model = BlogPost
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = BlogPost

class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 10

class BloggerDetailView(generic.DetailView):
    model = Blogger

class BlogCommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = BlogComment
    fields = ['comment']

    def form_valid(self, form):
        """
        Add blogger and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.commenter = self.request.user
        #Associate comment with blog based on passed id
        form.instance.post=get_object_or_404(BlogPost, pk = self.kwargs['pk'])
        return super(BlogCommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blogpost-detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogCommentCreateView, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['post'] = get_object_or_404(BlogPost, pk = self.kwargs['pk'])
        return context