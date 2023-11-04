from django.contrib import admin
import os

class DataAdminSite(admin.AdminSite):
    #title_header = 'Bookr Admin'
    #site_header = 'Bookr administration'
    #index_title = 'Bookr site admin'
    #ROOT_PATH =  #os.path.dirname(__file__).pardir
    #T_PATH = os.path.join(os.pardir, 'data' ,'templates' ,'admin', 'change_list.html')
    #index_template = Path(__file__).resolve().parent.parent + 'data/templates/admin/change_list.html'
    index_template = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates/admin/custom_index.html') #'/admin/custom_index.html' #os.path.join(os.path.dirname(__file__) ,'templates' ,'admin', 'change_list.html')