from django.urls import path
from .views import *

urlpatterns = [
    path('todos/', todos.as_view(), name='todos'),
    path('mytodos/', Mytodos.as_view(), name='mytodos'),
    path('mytodosdetail/<int:id>', MytodosDetail.as_view(), name='mytodosdetail'),
    path('todosdetail/<title>', todosDetail.as_view(), name='todosdetail'),
    path('todosquery/', todosQuery.as_view(), name='todosquery')
    # path('film/', film.as_view(), name='film'),
    # path('myfilm/', Myfilm.as_view(), name='myfilm')
]
