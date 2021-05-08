from django.shortcuts import render, redirect, get_object_or_404
from .forms import DirectionForm, HelpsReceivedForm, CancelOrderForm, FinishOrderForm
from .utils import get_googlemaps_direction_url
from django.contrib.auth.models import User

from home.models import UserProfile, Feedback
from customer.models import helps_received
from .models import need_help, helps_finished

from django.contrib.auth.decorators import login_required
import folium

# Create your views here.

@login_required
def index(request):
    try:
        user_obj = get_object_or_404(UserProfile, pk = request.user.id, user=request.user)
        if not user_obj.isMech:
            return redirect('/customer')
    except:
        return redirect('/mechanic')

    try:
        pending_requests = helps_received.objects.get(mechanic_name=get_object_or_404(User, pk=request.user.id).username)
        return redirect('pending_order/')
        print('------>   Having pending orders!')
    except:
        pending_requests = None
        print('------>   No pending orders!')

    direction_form = DirectionForm(request.POST or None)

    if request.method == 'POST' and not direction_form.is_valid():
        print(request.POST)
        helps_received_instance = helps_received()
        helps_received_instance.customer_name = request.POST['customer_name']
        helps_received_instance.mechanic_name = request.POST['mechanic_name']
        helps_received_instance.email = request.POST['email']
        helps_received_instance.customer_email = request.POST['customer_email']
        helps_received_instance.contact_no = request.POST['contact_no']
        helps_received_instance.customer_contact_no = request.POST['customer_contact_no']
        helps_received_instance.customer_description = request.POST['customer_description']
        helps_received_instance.latitude = request.POST['latitude']
        helps_received_instance.longitude = request.POST['longitude']
        helps_received_instance.customer_latitude = request.POST['customer_latitude']
        helps_received_instance.customer_longitude = request.POST['customer_longitude']
        feedbacks = Feedback.objects.all().filter(mechanic_name=request.user.username)
        count = Feedback.objects.all().filter(mechanic_name=request.user.username).count()
        avg_rating = 0.0
        if count > 0:
            for i in range(count):
                avg_rating += float(feedbacks[i].rating)
            avg_rating = avg_rating/count
        helps_received_instance.avg_rating = avg_rating
        helps_received_instance.save()

        # incase the customer was able to give more than one request, delete remaing too
        request_obj_count = need_help.objects.filter(user_name=request.POST['customer_name']).count()
        if request_obj_count > 0:
            for i in range(0, request_obj_count):
                request_obj =  need_help.objects.filter(user_name=request.POST['customer_name']).first()
                request_obj.delete()

        return redirect('pending_order/')


    name = get_object_or_404(UserProfile, pk = request.user.id, user=request.user)
    fullname = get_object_or_404(UserProfile, pk = request.user.id, user=request.user).firstname + ' ' + get_object_or_404(UserProfile, pk = request.user.id, user=request.user).lastname
    email = get_object_or_404(UserProfile, pk = request.user.id, user=request.user).email
    phone = get_object_or_404(UserProfile, pk = request.user.id, user=request.user).phone
    userName = get_object_or_404(User, pk=request.user.id).username

    direction_form = DirectionForm(request.POST or None)
    help_form = HelpsReceivedForm(request.POST or None)
    maps_url = None

    if direction_form.is_valid():
        m_lat = float(direction_form.cleaned_data.get('m_lat'))
        m_lon = float(direction_form.cleaned_data.get('m_lon'))
        # c_lat = float(direction_form.cleaned_data.get('c_lat'))
        # c_lon = float(direction_form.cleaned_data.get('c_lon'))
        c_lat = float(request.POST['cust_lat_dir'])
        c_lon = float(request.POST['cust_lon_dir'])
        maps_url = str(get_googlemaps_direction_url(m_lat, m_lon, c_lat, c_lon))
        print(m_lat)
        print(m_lon)
        print(c_lat)
        print(c_lon)
        print(maps_url)

    feedbacks = Feedback.objects.all().filter(mechanic_name=request.user.username)
    count = Feedback.objects.all().filter(mechanic_name=request.user.username).count()
    avg_rating = 0.0
    if count > 0:
        for i in range(count):
            avg_rating += float(feedbacks[i].rating)
        avg_rating = avg_rating/count


    context = {
        'avg_rating': avg_rating,
        'name': name,
        'fullname': fullname,
        'userName': userName,
        'email': email,
        'phone': phone,
        'direction_form': direction_form,
        'maps_url': maps_url,
        'help_form': help_form,
    }

    return render(request, 'mechanic/index.html', context)

@login_required
def pending_order(request):
    try:
        is_order_finished = request.POST['is_order_finished']
    except:
        is_order_finished = 'NO'

    try:
        user_obj = get_object_or_404(UserProfile, pk = request.user.id, user=request.user)
        if not user_obj.isMech:
            return redirect('/customer')
    except:
        return redirect('/mechanic')

    try:
        pending_requests = helps_received.objects.get(mechanic_name=get_object_or_404(User, pk=request.user.id).username)
    except:
        pending_requests = None
        return redirect('/mechanic')

    m = None
    maps_url = None

    if pending_requests:
        o_lat = pending_requests.latitude
        o_lon = pending_requests.longitude
        d_lat = pending_requests.customer_latitude
        d_lon = pending_requests.customer_longitude

        m = folium.Map(width=800, height=500, location=[d_lat, d_lon], zoom_start=8)

        folium.Marker([d_lat, d_lon], tooltip="customer's current location", popup=[d_lat, d_lon],
                        icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([o_lat, o_lon], tooltip="your location", popup=[o_lat, o_lon],
                        icon=folium.Icon(color='purple')).add_to(m)
        m = m._repr_html_()


    direction_form = DirectionForm(request.POST or None)
    if direction_form.is_valid():
        m_lat = float(direction_form.cleaned_data.get('m_lat'))
        m_lon = float(direction_form.cleaned_data.get('m_lon'))
        c_lat = float(direction_form.cleaned_data.get('c_lat'))
        c_lon = float(direction_form.cleaned_data.get('c_lon'))
        maps_url = str(get_googlemaps_direction_url(m_lat, m_lon, c_lat, c_lon))

    cancel_order_form = CancelOrderForm(request.POST or None)

    if cancel_order_form.is_valid() and not is_order_finished == 'YES':
        print("---->  INSIDE CANCEL ORDER FORM")


        need_help_instance = need_help()
        need_help_instance.name = request.POST['customer_name']
        need_help_instance.user_name = request.POST['customer_name']
        need_help_instance.email = request.POST['customer_email']
        need_help_instance.description = request.POST['customer_description']
        need_help_instance.contact_no = request.POST['customer_contact_no']
        need_help_instance.latitude = request.POST['customer_latitude']
        need_help_instance.longitude = request.POST['customer_longitude']
        need_help_instance.save()

    finish_order_form = FinishOrderForm(request.POST or None)

    if finish_order_form.is_valid() and is_order_finished == 'YES':

        print("---->  INSIDE FINISH ORDER FORM")

        helps_finished_instance = helps_finished()
        helps_finished_instance.customer_name = request.POST['customer_name']
        helps_finished_instance.mechanic_name = request.POST['mechanic_name']
        helps_finished_instance.customer_email = request.POST['customer_email']
        helps_finished_instance.email = request.POST['email']
        helps_finished_instance.customer_description = request.POST['customer_description']
        helps_finished_instance.customer_contact_no = request.POST['customer_contact_no']
        helps_finished_instance.contact_no = request.POST['contact_no']
        helps_finished_instance.customer_latitude = request.POST['customer_latitude']
        helps_finished_instance.customer_longitude = request.POST['customer_longitude']
        helps_finished_instance.latitude = request.POST['latitude']
        helps_finished_instance.longitude = request.POST['longitude']
        helps_finished_instance.save()

    try:
        customer_obj = helps_received.objects.filter(customer_name=request.POST['customer_name']).first()
        customer_obj.delete()
        return redirect('/mechanic')
    except:
        customer_obj = None

    fullname = get_object_or_404(UserProfile, pk = request.user.id, user=request.user).firstname + ' ' + get_object_or_404(UserProfile, pk = request.user.id, user=request.user).lastname
    context = {
        'fullname': fullname,
        'pending_requests': pending_requests,
        'map': m,
        'direction_form': direction_form,
        'maps_url': maps_url,
        'cancel_order_form': cancel_order_form,
        'finish_order_form': finish_order_form,
    }

    return render(request, 'mechanic/pending_order.html', context)
