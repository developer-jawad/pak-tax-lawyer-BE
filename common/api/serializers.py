from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `include` and `exclude` arguments
    to control which fields should be displayed.
    """
    
    def __init__(self, *args, **kwargs):
        # Don't pass the 'include' and 'exclude' args up to the superclass
        include = kwargs.pop('include', None)
        exclude = kwargs.pop('exclude', None)
        
        super().__init__(*args, **kwargs)
        
        if include is not None:
            # Drop any fields that are not specified in the `include` argument
            allowed = set(include)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        
        if exclude is not None:
            # Drop the fields that are specified in the `exclude` argument
            for field_name in exclude:
                self.fields.pop(field_name)
