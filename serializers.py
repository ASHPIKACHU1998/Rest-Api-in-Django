from rest_framework import serializers
from first.models import blog

class blogSerializer(serializers.ModelSerializer):
    url  = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = blog
        fields = [
            'url',
            'pk',
            'user',
            'title',
            'content',
            'timestamp',
        ]
        read_only_fields = ['user']
    #Validation area
    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request = request)    
    
    def validate_title(self, value):
        obj = blog.objects.filter(title__iexact = value)
        if self.instance:
            obj = obj.exclude(pk = self.instance.pk)
        if obj.exists():
            raise serializers.ValidationError("Please provide a unique title")
        return value



    #converts to JSON
    #Validations for data passed
    