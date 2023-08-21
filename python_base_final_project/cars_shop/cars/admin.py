from django.contrib import admin

from cars.models import ModelsGeneration, CarsModel, Car


@admin.register(ModelsGeneration)
class ModelsGenerationAdmin(admin.ModelAdmin):
    list_display = "name",  "body_type", "engine_volume", "engine_type",


@admin.register(CarsModel)
class CarsModelsAdmin(admin.ModelAdmin):
    list_display = "name", "generation",


@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
    list_display = ("manufacturer",
                    "model",
                    "year_of_manufacture",
                    "transmission",
                    "steering_wheel_position",
                    "Color",)

