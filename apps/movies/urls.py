
from django.conf.urls import url, include
from apps.movies import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'movies'

movies_patterns = [
    url(r'^inicio/$', views.movie_list, name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.movie_detail, name='movies-detail'),
    url(r'^crear/$', views.movie_create, name='movies-create'),
    url(r'^(?P<pk>[0-9]+)/editar/$', views.movie_update, name='movies-edit'),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', views.movie_delete, name='movies-delete')
]

urlpatterns = [
    url(r'^$', views.log_in, name='log-in'),
    url(r'^log-out/$', views.log_out, name='log-out'),
    url(r'^categorias/$', views.category_list, name='category-list'),
    url(r'^peliculas/', include(movies_patterns))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)