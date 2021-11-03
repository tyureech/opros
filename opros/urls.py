from django.urls import path
from .views import home, list_opros, CreateMatter, UpdateOpros, CreateOpros, delete_opros, UpdateMatter, delete_matter, \
    list_start_opros, StartOpros, MatterOpros, list_result


urlpatterns = [
    path('', home, name='home'),
    path('list_opros', list_opros, name='list_opros'),
    path('create_opros/', CreateOpros.as_view(), name='create_opros'),
    path('update_opros/<int:pk>', UpdateOpros.as_view(), name='update_opros'),
    path('delete_opros/<int:pk>', delete_opros, name='delete_opros'),
    path('delete_matter/<int:pk>/<int:kp>', delete_matter, name='delete_matter'),
    path('create_matter/<int:pk>', CreateMatter.as_view(), name='create_matter'),
    path('update_mater/<int:pk>/<int:kp>', UpdateMatter.as_view(), name='update_matter'),
    path('list_start_opros', list_start_opros, name='list_start_opros'),
    path('start_opros/<int:pk>', StartOpros.as_view(), name='start_opros'),
    path('matter_opros/<int:pk>/<int:user_id>/<int:kp>', MatterOpros.as_view(), name='matter_opros'),
    path('result_opros/<int:pk>/<int:user_id>/', list_result, name='list_result'),
]
