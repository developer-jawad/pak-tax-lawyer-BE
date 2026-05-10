from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.backends.console import EmailBackend as ConsoleEmailBackend
from django.utils import timezone

from core.helpers.email import send_email
from email_logs.choices import EmailStatus

from .models import EmailLog


class LoggingEmailBackendMixin:
    """
    A mixin to add email logging functionality to an email backend.
    """

    def send_messages(self, email_messages):
        """
        Overrides the send_messages method to log each email to the EmailLog model.
        This method assumes the subclass implements the actual sending logic.
        """
        if not email_messages:
            return 0

        sent_count = 0
        for message in email_messages:
            email_log = EmailLog.objects.create(
                recipient=", ".join(message.to),
                subject=message.subject,
                body=message.body,
                status=EmailStatus.PENDING,
            )

            try:
                result = self._send_single_message(message)
                if result:
                    email_log.status = EmailStatus.SENT
                    email_log.sent_at = timezone.now()
                    sent_count += result
                else:
                    email_log.status = EmailStatus.FAILED
                    email_log.error_message = "Failed to send email (unknown error)"
            except Exception as e:
                email_log.status = EmailStatus.FAILED
                email_log.error_message = str(e)
            finally:
                email_log.save()

        return sent_count

    def _send_single_message(self, message):
        """
        Send a single email message. Subclasses should override this method.
        """
        return super().send_messages([message])


class LoggingConsoleEmailBackend(LoggingEmailBackendMixin, ConsoleEmailBackend):
    """
    A custom email backend that logs emails to the EmailLog model before sending via console.
    """

    pass


class LoggingSMTPEmailBackend(LoggingEmailBackendMixin, BaseEmailBackend):
    """
    A custom email backend that logs emails to the EmailLog model and sends them via Resend API.
    """

    def _send_single_message(self, email_message):
        """
        Send an EmailMessage using Resend.
        """
        try:
            response = send_email(email_message)
            if response:
                return 1
            return 0
        except Exception as e:
            if not self.fail_silently:
                raise
            return 0
