
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from .models import Category
from .serializers import CategorySerializer

class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess
import json

@csrf_exempt
def chat_with_model(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get("prompt", "")

        # اجرای مدل به‌صورت local با ollama
        result = subprocess.run(
            ["ollama", "run", "phi3local", "--", prompt],
            capture_output=True, text=True
        )

        return JsonResponse({"response": result.stdout})
    else:
        return JsonResponse({"error": "Only POST method allowed"}, status=405)
