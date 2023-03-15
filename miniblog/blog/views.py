from django.shortcuts import get_object_or_404, render
from django.views import generic

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

class BlogCommentCreate(generic.CreateView):
    model = BlogComment
    fields = ['content', 'blogpost']

    def form_valid(self, form):
        """
        Add blogger and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.commenter = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog=get_object_or_404(BlogPost, pk = self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)