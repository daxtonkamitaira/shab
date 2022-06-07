import django_tables2 as tables

from .models import Data

class DataTable(tables.Table):
    class Meta:
        model = Data
        order_by = '-id'
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {
            'class': 'table table-bordered',
            'thead': {
                'class': 'thead-light'
            },
        }