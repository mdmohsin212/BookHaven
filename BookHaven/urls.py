from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from BookHaven.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('', include('author.urls')),
    path('', include('books.urls')),
    path('category/<slug:category_slug>/', Home, name='category_slug'),
    path('category/', include('categories.urls')),
    path('', include('transactions.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)