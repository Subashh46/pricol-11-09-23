from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import redirect
from .models import Machine, Status, Scan
from .utils import scan, time_now


# Create your views here.
class HomePageView(ListView):
    model = Machine
    template_name = 'home.html'


class StatusPageView(ListView):
    model = Status
    template_name = 'status.html'


class MachineDetailView(DetailView):
    model = Machine
    template_name = 'machine_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status"] = Status.objects.all()
        return context


class NewStatusView(CreateView):
    model = Status
    template_name = "new.html"
    fields = ['machine', 'is_working', 'description', 'document', 'document_name']


class DocumentListView(ListView):
    model = Status
    template_name = 'documents_view.html'


class ScanPageView(CreateView):
    model = Scan
    template_name = 'scan.html'
    fields = []


class HistoryPageView(ListView):
    model = Scan
    template_name = 'history.html'

    def get_context_data(self, **kwargs):
        mydata = Scan.objects.all().values()
        context = {
            'events': mydata,
        }
        return context


def scan_view(request):
        a = scan()
        b = time_now()
        if a:
            for i in a:
                new_instance = Scan(time=b, tag=i)
                new_instance.save()
            return redirect('history')
        else:
            return redirect('scan')
# class UpdateStatusView(UpdateView):
#     model = Status
#     template_name = "update.html"
#     fields = ['machine', 'is_working', 'description', 'document', 'document_name']
#
#
# class DeleteStatusView(DeleteView):
#     model = Status
#     template_name = 'delete_status.html'
#     success_url = reverse_lazy("home")
