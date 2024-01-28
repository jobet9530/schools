from django.http import JsonResponse
from django.shortcuts import render

def submit_data(request):
  if request.method == 'POST':
    data = request.POST.get('')
    return JsonResponse(data)
  else:
    return JsonResponse({'error': 'Invalid request method'})