from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Advertisements(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name="пользователь", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="advertisemenets/")

    def __str__(self):
        return f"Advertisements(id={self.id}, title={self.title}, price={self.price})"

    def get_absolute_url(self):
        return reverse('adv-detail', kwargs={'pk': self.id})

    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            create_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color:green; font-weight: bold;'>"
                "Сегодня в {}</span>",create_time
            )
        return self.created_at.strftime("%d.%m.%y в %H:%M:%S")

    @admin.display(description="Дата обновления")
    def update_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color:green; font-weight: bold;'>"
                "Сегодня в {}</span>",update_time
            )
        return self.created_at.strftime("%d.%m.%y в %H:%M:%S")

    @admin.display(description="фото")
    def get_html_image(self):
        from django.utils.html import format_html
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;">', url=self.image.url
            )
class Meta:
    db_table = "Advertisements"
# Create your models here.


