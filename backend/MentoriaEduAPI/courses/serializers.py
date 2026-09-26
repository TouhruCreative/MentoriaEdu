from rest_framework import serializers

from .models import Course, Module, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            "id",
            "title",
            "content",
            "order",
        ]


class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = [
            "id",
            "course",
            "title",
            "description",
            "order",
            "lessons",
        ]
        read_only_fields = [
            "id",
            "lessons",
        ]

    def update(self, instance, validated_data):
        validated_data.pop("course", None)

        return super().update(instance, validated_data)


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "author",
            "created_at",
            "updated_at",
            "modules",
        ]
        read_only_fields = [
            "id",
            "author",
            "created_at",
            "updated_at",
        ]