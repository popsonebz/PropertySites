from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AgentForm, AddListingForm, SearchPage, ContactForm
from .models import Agent, HouseDetails, Lead

from django.core.mail import EmailMessage

from django.shortcuts import render, get_object_or_404


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


"""Renders the home page for the general client-side."""


def home(request):

    listings = HouseDetails.objects.all()[:2]  # Select the first two entries in the listing table called HouseDetails
    return render(
        request,
        'propdata/index.html', {'listings': listings}  # Pass the result of the select (listings) to the home page (index.html) and render the page

    )

# Admin home page


def admin(request):
    """Renders the admin home page."""
    return render(
        request,
        'propDataAdmin/index.html',

    )

# Adding agent details


def agent(request):
    if request.method == "POST":
        form = AgentForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('admin')

    else:
        form = AgentForm()
    return render(request, 'propDataAdmin/newAgent.html', {'form': form})

# Display all agents (pagination added)


def showallagents(request):

    agents = Agent.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(agents, 5)
    try:
        agents = paginator.page(page)
    except PageNotAnInteger:
        agents = paginator.page(1)
    except EmptyPage:
        agents = paginator.page(paginator.num_pages)

    return render(
        request,
        'propDataAdmin/displayAgents.html', {'agents': agents}

    )

# Add listing


def addlisting(request):
    if request.method == "POST":
        form = AddListingForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('admin')


    else:
        form = AddListingForm()
    return render(request, 'propDataAdmin/addListing.html', {'form': form})


# Show Listing and use pagination

def showlisting(request):

    listings = HouseDetails.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(listings, 5)
    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(paginator.num_pages)
    return render(
        request,
        'propDataAdmin/showListing.html', {'listings': listings}

    )

# Show Lead (pagination added)


def showleads(request):

    lead = Lead.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(lead, 5)
    try:
        lead = paginator.page(page)
    except PageNotAnInteger:
        lead = paginator.page(1)
    except EmptyPage:
        lead = paginator.page(paginator.num_pages)
    return render(
        request,
        'propDataAdmin/showLeads.html', {'leads': lead}

    )

# Search Page


def search(request):
    """Renders the home page."""
    if request.method == "POST":
        form = SearchPage(request.POST, request.FILES)

        if form.is_valid():

            content = request.POST

            listings = HouseDetails.objects.filter(suburb=content['suburb'], bedrooms=content['bedrooms'],
                                                 price__gte=content['price_from'], price__lte=content['price_to'])

            page = request.GET.get('page', 1)
            paginator = Paginator(listings, 5)
            try:
                listings = paginator.page(page)
            except PageNotAnInteger:
                listings = paginator.page(1)
            except EmptyPage:
                listings = paginator.page(paginator.num_pages)
            return render(
                request, 'propdata/resultPage.html', {'listings': listings}
            )


    else:
        form = SearchPage()
    return render(
        request,
        'propdata/searchPage.html', {'form': form}

    )

# Get the details of a listing, save the information in the database and send an email to the agent


def detail(request, pk):
    # get the full name of the agent based on the foreign key in the HouseDetails table
    house_details = get_object_or_404(HouseDetails, pk=pk)
    agent_full_name = house_details.associated_agent

    # split the fullname into first name and last name so we can search the Agent table for more information based on the names
    full_name = str(agent_full_name).split()
    firstName = full_name[0]
    lastName = full_name[1]
    agent_details = Agent.objects.get(first_name=firstName, last_name=lastName) # Search the Agent table based on firstname and last name to get his full details

    if request.method == "POST":
        house_details = get_object_or_404(HouseDetails, pk=pk)
        xx = request.POST

        xx['property'] = house_details.pk

        form = ContactForm(xx, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # Email sending
            email = EmailMessage('Potential Buyer For ' + house_details.owners_Ref_Number,
                                 'Dear ' + str(agent_full_name) +
                                 ',\n I am interested in buying this house with reference number '
                                 + house_details.owners_Ref_Number + '. \n You can contact me with the details below.\n'+
                                 xx['first_name'] +' '+ xx['last_name'] +
                                 '\n Email Address: ' + xx['email'] +
                                 '\n Address : ' + xx['address'], to=[str(agent_details.email)])
            email.send()
            return render(request, 'propdata/email_sent.html')

    else:

        form = ContactForm()
        # modifying the properties of the form on the fly
        form.fields['property'].widget.attrs['hidden'] = True
        form.fields['first_name'].widget.attrs['placeholder'] = 'First Name *'
        form.fields['last_name'].widget.attrs['placeholder'] = 'Last Name *'
        form.fields['email'].widget.attrs['placeholder'] = 'Email Address *'
        form.fields['address'].widget.attrs['placeholder'] = 'Please enter your message *'

    return render(request, 'propdata/details.html', {'house_details': house_details, 'Agent_info':agent_details,
                                                         'contact_agent': form})
