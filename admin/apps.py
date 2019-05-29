from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpleAdminConfig(AppConfig):
    default_site = 'admin.admin.BlogAdmin'
    name = 'admin'
    verbose_name = _("Administrator")

    def ready(self):
        pass


class AdminConfig(SimpleAdminConfig):
    def ready(self):
        super().ready()
        # self.module.autodiscover
