from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    """
    Account adapter to set custom fields on user creation
    """

    def save_user(self, request, user, form, commit=True):
        super().save_user(request, user, form, commit=False)

        data = form.cleaned_data
        # set the user custom fields
        user.phone = data.get('phone')
        user.website = data.get('website')
        user.address = data.get('address')
        user.city = data.get('city')
        user.state = data.get('state')
        user.country = data.get('country')
        user.zip_code = data.get('zip_code')

        if commit:
            user.save()
        return user