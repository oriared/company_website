from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from cooperation.models import Cooperation
from cooperation.utils import email_from_form


class CooperationCreateView(CreateView):

    model = Cooperation
    fields = ('company', 'person', 'phone', 'email', 'city', 'text', 'file')
    success_url = reverse_lazy('core:home')

    def get_template_names(self):
        name = self.kwargs.get('type')
        return f'cooperation/{name}.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs.get('type')
        return context

    def form_valid(self, form):
        form.instance.subject = self.kwargs.get('type')
        self.object = form.save()
        email_from_form(form)
        return super().form_valid(form)
