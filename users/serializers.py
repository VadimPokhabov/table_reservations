from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """
    Сериализатор для модели User
    """
    #
    # payment_history = PaymentsSerializer(
    #     source="payment_set", many=True, read_only=True
    # )

    class Meta:
        model = User
        fields = "__all__"
