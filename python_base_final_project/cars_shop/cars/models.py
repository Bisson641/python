from django.db import models


class ModelsGeneration(models.Model):
    BODY_TYPE = (
        ('City car', "City car"),
        ('Hatchback', "Hatchback"),
        ('MPV', "MPV"),
        ('Saloon', "Saloon"),
        ('Coupe', "Coupe"),
        ('Crossover', "Crossover")
    )

    name = models.CharField(max_length=50)
    body_type = models.CharField(max_length=20, choices=BODY_TYPE)
    engine_volume = models.DecimalField(max_digits=2, decimal_places=1)
    engine_type = models.CharField(max_length=20, choices=[('gasoline', "gasoline"),
                                                           ('diesel', "diesel"),
                                                           ('electric', "electric")
                                                           ])

    def __str__(self):
        return f"Generation {self.name!r}"


class CarsModel(models.Model):
    name = models.CharField(max_length=50)
    generation = models.ForeignKey(ModelsGeneration, related_name="models_generation", on_delete=models.PROTECT,)

    def __str__(self):
        return f"Model {self.name!r}"


class Car(models.Model):
    manufacturer = models.CharField(max_length=50)
    year_of_manufacture = models.IntegerField()
    model = models.ForeignKey(CarsModel, related_name="cars_models", on_delete=models.PROTECT,)
    transmission = models.CharField(max_length=20, choices=[('manual', "manual"),
                                                            ('automatic', "automatic"),
                                                            ('robotic', "robotic")
                                                            ])
    steering_wheel_position = models.CharField(max_length=20, choices=[('left', "left"),
                                                                       ('right', "right")
                                                                       ])
    Color = models.CharField(max_length=30,)

    def __str__(self):
        return f"Manufacture {self.manufacturer!r}"




#
# class Advert(models.Model):
#     class Status(models.IntegerChoices):
#         DEACTIVATED = 0
#         ACTIVE = 1
#
#     name = models.CharField(db_index=True, max_length=100)
#     photo = models.ImageField(blank=True, upload_to='images',)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     # category = models.ForeignKey(AdvertCategory, on_delete=models.PROTECT, related_name="adverts",)
#     status = models.IntegerField(
#         choices=Status.choices,
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"Advert  {self.name!r}"


# class Cars(models.Model):
#     pass
