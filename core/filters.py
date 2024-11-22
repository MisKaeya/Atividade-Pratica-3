from django_filters import rest_framework as filters
from core.models import Book, Author

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    autor = filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    categoria = filters.AllValuesFilter(field_name='categoria__name')
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'categoria']
        
class AuthorFilter(filters.FilterSet):

    name = filters.CharFilter(lookup_expr='icontains')
  
    # Para um filtro de data maior que
    #birth_date_after = filters.DateFilter(field_name='birth_date', lookup_expr='gte')
    
    # Para um filtro de data menor que
   # birth_date_before = filters.DateFilter(field_name='birth_date', lookup_expr='lte')
    
    # Para um filtro entre duas datas
    birth_date_range = filters.DateFromToRangeFilter(field_name='birth_date')

    class Meta:
        model = Author
        fields = ['name', 'birth_date_range']