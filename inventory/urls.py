from django.urls import path
from .views import (
    SignupView, LoginView,
    MechanicalPartListCreateView, MechanicalPartDetailView,
    RawMaterialListCreateView, RawMaterialDetailView,
    ElectricalPartListCreateView, ElectricalPartDetailView,
    AllInventoryItemsView
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('mechanical-parts/', MechanicalPartListCreateView.as_view(), name='mechanical_parts'),
    path('mechanical-parts/<int:pk>/', MechanicalPartDetailView.as_view(), name='mechanical_part_detail'),
    path('raw-materials/', RawMaterialListCreateView.as_view(), name='raw_materials'),
    path('raw-materials/<int:pk>/', RawMaterialDetailView.as_view(), name='raw_material_detail'),
    path('electrical-parts/', ElectricalPartListCreateView.as_view(), name='electrical_parts'),
    path('electrical-parts/<int:pk>/', ElectricalPartDetailView.as_view(), name='electrical_part_detail'),
    path('all-items/', AllInventoryItemsView.as_view(), name='all_inventory_items'),  # New endpoint for all items

]
