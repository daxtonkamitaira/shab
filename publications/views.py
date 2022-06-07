from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django_tables2.export.views import ExportMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Data
from .tables import DataTable
from .filters import DataFilter

class DataListView(LoginRequiredMixin, ExportMixin, SingleTableMixin, FilterView):
    model = Data
    table_class = DataTable
    template_name: str = 'data.html'
    filterset_class = DataFilter
