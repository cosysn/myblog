from weakref import WeakSet
from functools import update_wrapper

from django.apps import apps
from django.http import Http404, HttpResponseRedirect
from django.urls import NoReverseMatch, reverse
from django.utils.functional import LazyObject
from django.utils.module_loading import import_string
from django.utils.translation import gettext as _, gettext_lazy
from django.urls import include, path, re_path
from django.http import HttpResponse

all_sets = WeakSet()


class BlogAdmin:
    blog_title = gettext_lazy('Blog admin')
    blog_url = '/'

    def __init__(self, name='Admin'):
        self._registry = {}
        self.name = name
        all_sets.add(self)

    def admin_view(self, view, cacheable=False):
        def inner(request, *args, **kwargs):
            return view(request, *args, **kwargs)

        return update_wrapper(inner, view)

    def get_urls(self):
        def wrap(view, cacheable=False):
            def wrapper(*args, **kwargs):
                return self.admin_view(view, cacheable)(*args, **kwargs)
            wrapper.blog_admin = self
            return update_wrapper(wrapper, view)

        urlpatterns = [
            path('', wrap(self.index), name='index'),
            path('login/', self.login, name='login')
        ]

        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), 'admin', self.name

    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff

    def index(self, request, extra_context=None):
        return HttpResponse("Hello, world. You're at the admin index")

    def login(self, request, extra_context=None):
        if request.method == 'GET' and self.has_permission(request):
            index_path = reverse('admin:index', current_app=self.name)
            return HttpResponseRedirect(index_path)

        from django.contrib.auth.views import LoginView

        defaults = {
            'template_name': 'admin/login.html'
        }
        
        return LoginView.as_view(**defaults)(request)


class DefaultBlogAdmin(LazyObject):
    def _setup(self):
        blog_admin_class = import_string(apps.get_app_config('admin').default_site)
        self._wrapped = blog_admin_class()


blog_admin = DefaultBlogAdmin()
