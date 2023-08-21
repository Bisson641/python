from django.urls import path

from cars.views import cars_index

app_name = "cars"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', cars_index, name="cars_index"),

]
