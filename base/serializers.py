"""This is a class provided by DRF that allows you to easily create serializers for your Django models. 
It automatically generates serializer fields based on the model's fields.
"""
from rest_framework.serializers import ModelSerializer, SerializerMethodField
"""This is a field provided by DRF that allows you to define custom methods to include additional data in your serialized output.
It's useful when you need to include calculated or derived data in your API responses."""
from .models import Advocate, Company


# Company
"""CompanySerializer is a serializer for the Company model."""
class CompanySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)
    """employee_count is a custom field that's not a direct attribute of the Company model. It uses SerializerMethodField to define 
    a custom method get_employee_count that calculates and returns the count of employees associated with the company."""
    class Meta:
        model = Company
        fields = '__all__'
        """The Meta class specifies the metadata for the serializer.
        In this case, it's configured to use the Company model and include all fields ('__all__') in the serialized output."""
      
      
    # count of employee  in compony
    def get_employee_count(self, obj):
        count = obj.advocate_set.count()
        return count
        
        
class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocate
        fields =['username', 'bio', 'company']
        """The Meta class specifies the metadata for the serializer. 
        It's configured to use the Advocate model and include specific fields ('username', 'bio', 'company') in the serialized output."""