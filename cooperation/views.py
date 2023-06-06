from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from cooperation.models import Cooperation
from cooperation.utils import send_email_cooperation


class CooperationCreateView(CreateView):

    model = Cooperation
    fields = ('company', 'name', 'phone', 'email', 'city', 'text', 'file')
    success_url = reverse_lazy('core:home')

    def get_template_names(self):
        name = self.kwargs.get('type')
        return f'cooperation/{name}.html'

    def form_valid(self, form):
        form.instance.subject = self.kwargs.get('type')
        self.object = form.save()
        send_email_cooperation(self.object)
        return super().form_valid(form)
