from django.urls import path, include, re_path
from . import views


urlpatterns = [
    # API paths
    path('sensors/list', views.list_of_sensors),
    path('sensors/add', views.add_sensors),
    path('sensors/detail/<int:pk>', views.sensor_detail),
    path('sensors/update/<int:pk>', views.update_sensor),
    path('sensors/delete/<int:pk>', views.delete_sensor),
    path('sensors_data/list', views.list_of_sensors_data),
    path('sensors_data/list/<int:pk>', views.list_of_sensors_data_from_one_sensor),
    path('sensors_data/add', views.add_sensor_data),
    path('sensors_data/frequency/<int:pk>', views.change_frequency_data),
    path('sensors_data/latest_value/<int:pk>', views.get_last_data),
    path('sensors/ip', views.add_sensor_ip_address)
]