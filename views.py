from django.db.models import Q
from rest_framework import generics, mixins
from first.models import blog
from .serializers import blogSerializer
from .permissions import IsOwnerOrReadOnly
class BlogCreateView(mixins.CreateModelMixin ,generics.ListAPIView): 
    lookup_field = 'pk'
    serializer_class = blogSerializer
    def get_queryset(self):
        qs = blog.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|Q(content__icontains=query))
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}

class BlogRUDView(generics.RetrieveUpdateDestroyAPIView): #DetailView
    lookup_field = 'pk'
    serializer_class = blogSerializer
    queryset = blog.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
  
    def get_queryset(self):
        return blog.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}
 