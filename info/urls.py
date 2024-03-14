from django.urls import path

from info import views

urlpatterns = [
    path('', views.main, name="main"),
    path('all', views.read_pizza, name="read_pizza"),
    path('contest', views.contest, name="contest"),
    # path('test', views.MarksView.as_view(), name="test"),
    path('marks/', views.MarkListView.as_view(), name='mark-list'),
    path('marks/<int:pk>', views.MarkDetailView.as_view(), name="mark-detail"),
    path('marks/create', views.MarkUpdateView.as_view(), name="mark-create"),
    path('marks/<int:pk>/update', views.MarkCreateView.as_view(), name="mark-update"),
    path('marks/<int:pk>/delete', views.MarkDeleteView.as_view(), name="mark-delete"),
]
