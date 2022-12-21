from django.urls import path
from .import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:task_id>/',views.update,name='update'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>', views.TaskDeleteView.as_view(), name='cbvdelete'),
    # path('detail/',views.details,name='details'),
]
