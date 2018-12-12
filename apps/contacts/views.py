from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail


def contact(req):
    if req.method == 'POST':
        # print(req)
        listing_id = req.POST['listing_id']
        listing = req.POST['listing']
        name = req.POST['name']
        email = req.POST['email']
        phone = req.POST['phone']
        message = req.POST['message']
        user_id = req.POST['user_id']
        realtor_email = req.POST['email']

        # Check if user has already made an inquiry
        if req.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    req, "You have already made an inquiry for this listing")
                return redirect('/listing/'+listing_id)  # concatenating

        # if passed checked or not logged in
        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # Send mail
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
            'Youremail',
            [realtor_email, 'extraemail@mail.com'],
            fail_silently=False

        )

        messages.success(
            req, "Your request have been submitted, a realtor will get back to you soon!")
        # using namespace and assignment
        return redirect('listing', listing_id=listing_id)
