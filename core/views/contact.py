from django.views.generic import ListView

from core.models import Contact


class ContactListView(ListView):
    template_name = 'core/contact-list.html'
    model = Contact
    context_object_name = 'contacts'
