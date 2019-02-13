from django.shortcuts import render
from django.views.generic import DetailView
from django.http import Http404

from .models import Product
# Create your views here.


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


def get_modified_name(filename):
    ...


class ProductDetailView(DetailView):
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        # TODO: Remove below line:
        print(context)
        return(context)

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance
