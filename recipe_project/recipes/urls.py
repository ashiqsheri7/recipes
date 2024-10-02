

from django.urls import path
from .views import recipe_list, recipe_create, recipe_update, recipe_delete
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('recipe/new/', recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit/', recipe_update, name='recipe_update'),
    path('recipe/<int:pk>/delete/', recipe_delete, name='recipe_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
