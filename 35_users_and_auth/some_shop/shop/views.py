from celery.result import AsyncResult
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin,
                                        )
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import (HttpRequest,
                         HttpResponse,
                         JsonResponse,
                         HttpResponseRedirect,
                         )
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (TemplateView,
                                  ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView, DeleteView,
                                  )

from .models import Product
from .models import Category
from .models import Order
from .forms import CategoryForm
from .tasks import notify_order_saved
# from .forms import CategoryForm


# Create your views here.


class CategoriesListView(ListView):
    # model = Category
    queryset = (
        Category
        .objects
        .filter(~Q(archived=True))
        .all()
    )


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    # fields = "name", "description"
    # success_url = reverse
    success_url = reverse_lazy("shop:categories")


class CategoryUpdateView(UpdateView):
    template_name_suffix = "_update_form"
    model = Category
    form_class = CategoryForm

    # def get_success_url(self):
    #     return reverse("shop:category", kwargs={"pk": self.object.pk})


class CategoryDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "shop.delete_category"
    # model = Category
    success_url = reverse_lazy("shop:categories")
    queryset = (
        Category
        .objects
        .filter(~Q(archived=True))
        .all()
    )

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        # return HttpResponseRedirect(success_url)
        return redirect(success_url)


class ShopIndexView(TemplateView):
    template_name = "shop/index.html"


class ProductsView(View):
    template_name = "shop/products.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        products = (Product.objects
                    .filter(~Q(status=Product.Status.ARCHIVED))
                    .order_by("id")
                    .defer(
                        "description",
                        "created_at",
                        "updated_at",
                        "category__description",
                    )
                    .select_related("category").all())
        return render(request=request, template_name=self.template_name, context={"products": products}, )


class OrdersListView(UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.is_staff

    template_name = 'shop/orders.html'
    context_object_name = "orders"
    queryset = (Order
                .objects
                .select_related("user", "payment_details")
                .prefetch_related("products")
                .order_by("id")
                .all()
                )


class CategoriesWithProductsTree(LoginRequiredMixin, TemplateView):
    template_name = "shop/categories_with_products_tree.html"
    extra_context = {"categories":  Category.objects.order_by("id").prefetch_related("products").all()}
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     categories = Category.objects.order_by("id").prefetch_related("products").all()
    #     context.update(categories=categories)
    #     return context

@login_required
def get_task_info(request: HttpRequest, task_id: str) -> HttpResponse:
    task_result: AsyncResult = notify_order_saved.AsyncResult(task_id)
    return JsonResponse({
        "task_id": task_result.id,
        "status": task_result.status,
        "name": task_result.name,
        # "backend": str(task_result.backend),
    })
