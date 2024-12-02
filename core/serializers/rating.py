from rest_framework import serializers

from .user import UserSerializer
from ..models import Rating


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Rating
        fields = ['book', 'user', 'rating']
        read_only_fields = ['user']

    @staticmethod
    def validate_rating(value):
        if value < 0 or value > 10:
            raise serializers.ValidationError('Рейтинг должен быть в пределах от 0 до 10.')
        return value

    def create(self, validated_data):
        rating, created = Rating.objects.update_or_create(
            book=validated_data.get('book'),
            user=self.context['request'].user,
            defaults={'rating': validated_data.get('rating')}
        )
        return rating
