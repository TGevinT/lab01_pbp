from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_xml #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import show_json #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import show_json_by_id_json
from wishlist.views import show_json_by_id_xml

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_json, name='show_json'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/<int:id>', show_json_by_id_json, name='show_json_by_id_json'), #sesuaikan dengan nama fungsi yang dibuat
    path('xml/<int:id>', show_json_by_id_xml, name='show_json_by_id_xml'), #sesuaikan dengan nama fungsi yang dibuat

]