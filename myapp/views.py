
from django.shortcuts import render
from .forms import resumeForm
from django.views import View
from .models import resume



class HomeView(View):
    def get(self, request):
        form = resumeForm()
        candidates = resume.objects.all()
        return render(request, 'home.html', {'candidates':candidates, 'form':form})

    def post(self, request):
        form = resumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'home.html', {'form':form})
class CandidateView(View):
    def get(self, request, pk):
        candidate = resume.objects.get(pk=pk)
        return render(request, 'candidate.html', {'candidate':candidate})

