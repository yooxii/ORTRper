from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("checkouts", views.checkouts, name="checkouts"),
    path("import_checkouts", views.import_checkouts, name="import_checkouts"),
    path("export_checkouts", views.export_checkouts, name="export_checkouts"),
    path("add_checkouts", views.add_checkouts, name="add_checkouts"),
    path(
        "<int:checkout_id>/edit_checkouts", views.edit_checkouts, name="edit_checkouts"
    ),
    path(
        "<int:checkout_id>/delete_checkouts",
        views.delete_checkouts,
        name="delete_checkouts",
    ),
    path("schedules", views.schedules, name="schedules"),
    path("import_schedules", views.import_schedules, name="import_schedules"),
    path("export_schedules", views.export_schedules, name="export_schedules"),
    path("add_schedules", views.add_schedules, name="add_schedules"),
    path(
        "<int:schedule_id>/edit_schedules", views.edit_schedules, name="edit_schedules"
    ),
    path(
        "<int:schedule_id>/delete_schedules",
        views.delete_schedules,
        name="delete_schedules",
    ),
    path("technicians", views.technicians, name="technicians"),
]
urlpatterns += staticfiles_urlpatterns()
