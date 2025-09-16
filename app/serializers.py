from rest_framework import serializers
from .models import Student   # better to import explicitly

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student       # ✅ lowercase 'model'
        fields = "__all__"


# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     email = serializers.EmailField()
#     roll_no = serializers.CharField(max_length=20)
#     grade = serializers.CharField(max_length=10)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#      instance.name = validated_data.get('name', instance.name)
#      instance.age = validated_data.get('age', instance.age)
#      instance.email = validated_data.get('email', instance.email)
#      instance.roll_no = validated_data.get('roll_no', instance.roll_no)
#      instance.grade = validated_data.get('grade', instance.grade)
#      instance.save()
#      return instance
