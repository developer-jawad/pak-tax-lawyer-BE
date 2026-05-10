from allauth.account.adapter import DefaultAccountAdapter

from config.env import BASE_URL


class AccountAdapter(DefaultAccountAdapter):

    def render_mail(self, template_prefix, email, context):
        """
        Renders an email template with context and returns the email message.
        This method is called for all emails, including password reset emails.
        """
        if template_prefix == "account/email/password_reset_key":

            uid = context["uid"]
            token = context["token"]
            request = context.get("request")
            base_url = BASE_URL or request.build_absolute_uri("/")

            # since we are using Django AllAuth templates for reset password and other auth stuff, so we need to override the url
            # TODO[Abdurrehman]: Use the allauth view name here instead of hardcoding the url. This is not a good practice.
            context["password_reset_url"] = (
                f"{base_url}/account/password/reset/key/{uid}-{token}"
            )

        return super().render_mail(template_prefix, email, context)
