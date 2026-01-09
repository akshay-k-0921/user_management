from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    attachment_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ['user', 'created_at', 'modified_at']

    def get_attachment_url(self, obj):
        if obj.attachment:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.attachment.url)
            return obj.attachment.url
        return None
