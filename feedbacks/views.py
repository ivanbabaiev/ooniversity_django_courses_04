# -*- coding: utf-8 -*-

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins

from feedbacks.models import Feedback

# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives


class FeedbackView(CreateView):
    model = Feedback
    template_name = "feedback.html"
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        message = super(FeedbackView, self).form_valid(form)
        messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        mail_admins(self.object.subject, self.object.message)
        # mail = EmailMultiAlternatives(
        #     subject="Your Subject",
        #     body="This is a simple text email body.",
        #     from_email="Yamil Asusta <hello@yamilasusta.com>",
        #     to=["ivanbabaiev@gmail.com"],
        # #    headers={"Reply-To": "support@sendgrid.com"}
        # )
        # mail.attach_alternative("<p>This is a simple HTML email body</p>", "text/html")
        #
        # mail.send()
        return message

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Feedback"

        return context
