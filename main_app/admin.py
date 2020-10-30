from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin
from .models import *

# Register your models here.


""" Форма для проверки загруженных изображений """


class SmartphoneAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if not instance.sd:
            self.fields['sd_volume_max'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgray;'
            })

    def clean(self):
        if not self.cleaned_data['sd']:
            self.cleaned_data['sd_volume_max'] = None
            return self.cleaned_data


# class NotebookAdminForm(ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['image'].help_text = mark_safe(
#             """<span style="color:red; font-size:15px;">При загрузке изображения с разрешением больше {}x{} оно будет обрезано!</span>
#             """.format(
#                 *Product.MIN_RESOLUTION
#             ))
#
#     def clean_image(self):
#         image = self.cleaned_data['image']
#         img = Image.open(image)
#         min_width, min_height = Product.MIN_RESOLUTION
#         max_width, max_height = Product.MAX_RESOLUTION
#         if image.size > Product.MAX_IMAGE_SIZE:
#             raise ValidationError('Размер изображения не должен превышать 3MB!')
#         if img.width < min_width or img.height < min_height:
#             raise ValidationError('Разрешения изображение меньше минимального!')
#         if img.width > max_width or img.height > max_height:
#             raise ValidationError('Разрешения изображение больше максимального!')
#         return image


class NotebookAdmin(admin.ModelAdmin):

    # form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    # form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Order)