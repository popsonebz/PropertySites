from django import forms

from .models import Lead, Agent, HouseDetails

# Form for adding a contact sidebar
class ContactForm(forms.ModelForm):
    class Meta:
        model = Lead

        fields = ('first_name', 'last_name','email', 'address','property')

# Form for adding new agent
class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent

        fields = ('first_name','last_name','cellPhone','email', 'picture', )

# Form for adding new Listing
class AddListingForm(forms.ModelForm):
    class Meta:
        model = HouseDetails
        fields = ('suburb', 'bedrooms', 'price', 'picture', 'marketing_Heading','description', 'associated_agent', 'owners_Ref_Number')

# Form for search page
class SearchPage(forms.ModelForm):
    price_from = forms.DecimalField(min_value=0.00,label="Price From :")
    price_to = forms.DecimalField(min_value=0.00, label="Price To :")

    class Meta:
        model = HouseDetails

        fields = ('suburb', 'bedrooms')

        labels = {
            "suburb": "Suburb",
            "bedrooms": "Bedrooms"
        }
