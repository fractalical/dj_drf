from django.urls import path

from measurement.views import SensorsViewCreate, MeasurementCreate, SensorEdit, \
    SensorInfo

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты

    path('sensors/', SensorsViewCreate.as_view()),
    path('sensor_info/<pk>/', SensorInfo.as_view()),
    path('sensor_edit/<pk>/', SensorEdit.as_view()),
    path('measure_add/', MeasurementCreate.as_view()),
]
