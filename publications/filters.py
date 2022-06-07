import django_filters

from .models import Data, Category

def categoies(request):
    if request is None:
        return Category.objects.none()

    return Category.objects.all()

class DataFilter(django_filters.FilterSet):
    sub_category = django_filters.ModelChoiceFilter(queryset=categoies)

    class Meta:
        model = Data
        fields = ["sub_category", "publication_date"]