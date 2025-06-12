from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("checkouts", views.checkouts, name="checkouts"),
    path("import_checkouts", views.import_checkouts, name="import_checkouts"),
    path("export_checkouts", views.export_checkouts, name="export_checkouts"),
    path("edit_checkouts", views.edit_checkouts, name="edit_checkouts"),
    path("delete_checkouts", views.delete_checkouts, name="delete_checkouts"),
]
urlpatterns += staticfiles_urlpatterns()
