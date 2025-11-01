from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess, json

@csrf_exempt
def chat_with_model(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompt = data.get("prompt", "")

            # اجرای مدل از طریق Ollama
            result = subprocess.run(
                ["ollama", "run", "phi3local", "--", prompt],
                capture_output=True, text=True
            )
            return JsonResponse({"response": result.stdout})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Only POST method allowed"}, status=405)

