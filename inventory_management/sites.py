from django.contrib.admin import sites
from django.utils.translation import gettext_lazy as _


class HumanitarianAdminSite(sites.AdminSite):
    site_title = _("Humanitarian Admin")
    site_header = _("Humanitarian Admin Portal")
    index_title = _("Dashboard")
    # index_template = "Humanitarian_admin/admin/index.html"


admin_site = HumanitarianAdminSite()
