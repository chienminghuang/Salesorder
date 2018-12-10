from import_export import resources
from .models import Salesorder

class PersonResource(resources.ModelResource):
    class Meta:
        model = Salesorder