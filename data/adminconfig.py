from django.contrib.admin.apps import AdminConfig

class DataAdminConfig(AdminConfig):
    default_site = 'degree_checklist.admin.DataAdminSite'