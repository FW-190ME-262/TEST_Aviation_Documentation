from datetime import datetime
from .forms import PhoneLoginForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .forms import UserProfileForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Object, SiteVisitor

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Object  # Предполагается, что ваша модель называется Object
import random
from django.shortcuts import render, redirect
from .models import Praktic_avariem_play
from .forms import PhoneLoginForm


from .utils import generate_verification_code

from django.shortcuts import render, get_object_or_404
from .models import Praktic_avariem_play, Object
from django.shortcuts import render, redirect
from .forms import PhoneLoginForm
from django.contrib.auth import login
from .models import User
from twilio.rest import Client
import random

from django.shortcuts import render, redirect
from .forms import PhoneLoginForm
from .utils import generate_verification_code  # если эта функция определена в utils.py
from twilio.rest import Client

def send_sms(phone_number, code):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Your verification code is {code}",
        from_='+1234567890',  # ваш Twilio номер
        to=phone_number
    )

def phone_login(request):
    if request.method == 'POST':
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            code = generate_verification_code()
            send_sms(phone_number, code)
            return redirect('verify_code')  # переадресация на страницу проверки кода
    else:
        form = PhoneLoginForm()
    return render(request, 'login.html', {'form': form})



def top_up_balance(request):
    if request.method == 'POST':
        # Use payment gateway API to process payment
        amount_rub = request.POST['amount']
        coins = int(amount_rub) * 1000
        request.user.profile.balance += coins
        request.user.profile.save()
        return redirect('profile')
    return render(request, 'top_up.html')




def phone_login(request):
    if request.method == 'POST':
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            # Process the phone login
            phone_number = form.cleaned_data['phone_number']
            # Generate and send SMS code
            code = generate_verification_code()
            send_sms(phone_number, code)
            return redirect('verify_code')  # redirect to a code verification page
    else:
        form = PhoneLoginForm()
    return render(request, 'login.html', {'form': form})



def play_game(request, aircraft_id):
    # Get the specific aircraft
    aircraft = get_object_or_404(Object, id=aircraft_id)

    # Retrieve the emergency situations for the specific aircraft
    emergency_set = Praktic_avariem_play.objects.filter(aircraft=aircraft)

    if not emergency_set.exists():
        return render(request, 'no_emergencies.html', {'aircraft': aircraft})

    questions = list(emergency_set)

    # Check if it's the first question
    if 'question_index' not in request.session:
        request.session['question_index'] = 0
        request.session['score'] = 0
        random.shuffle(questions)  # Shuffle the emergency situations
        request.session['questions'] = [q.id for q in questions]

    # Fetch the current question
    question_id = request.session['questions'][request.session['question_index']]
    current_question = Praktic_avariem_play.objects.get(id=question_id)

    # Randomly select two other wrong answers from the same aircraft's set
    other_questions = Praktic_avariem_play.objects.filter(aircraft=aircraft).exclude(id=current_question.id)
    wrong_answers = random.sample(list(other_questions), 2)

    # Combine the correct answer with wrong ones
    answers = [
        {"text": current_question.avariem_situation1, "correct": True},
        {"text": wrong_answers[0].avariem_situation1, "correct": False},
        {"text": wrong_answers[1].avariem_situation1, "correct": False},
    ]
    random.shuffle(answers)

    # Process the player's answer
    if request.method == "POST":
        selected_answer = request.POST.get('answer')
        if selected_answer == current_question.avariem_situation1:
            request.session['score'] += 1
        request.session['question_index'] += 1

        # Check if the game is over
        if request.session['question_index'] >= len(request.session['questions']):
            return redirect('game_over')

        return redirect('play_game', aircraft_id=aircraft.id)

    return render(request, 'play_game.html', {
        'question': current_question,
        'answers': answers,
        'question_index': request.session['question_index'] + 1,
        'total_questions': len(request.session['questions']),
        'aircraft': aircraft,
    })


def game_over(request):
    score = request.session.get('score', 0)
    request.session.flush()  # Clear the session data
    return render(request, 'game_over.html', {'score': score})


def aircraft_detail(request, id):
    aircraft = get_object_or_404(Object, id=id)
    return render(request, 'aircraft_detail.html', {'aircraft': aircraft})

def aircraft_details(request, id):
    aircraft = get_object_or_404(Object, id=id)
    return render(request, 'aircraft_details.html', {'aircraft': aircraft})


def search_objects(request):
    query = request.GET.get('query', '')
    if query:
        objects = Object.objects.filter(name__icontains=query)
        results = [
            {'name': obj.name, 'photo_url': obj.photo.url if obj.photo else ''}
            for obj in objects
        ]
    else:
        results = []
    return JsonResponse({'results': results})


# Create your views here.

def index(request):
    objects = Object.objects.all()  # Извлекаем все объекты из модели
    return render(request, 'index.html', {'objects': objects})


def aircraft_detail(request, id):
    obj = Object.objects.get(id=id)
    return render(request, 'aircraft_detail.html', {'object': obj})


# name = Object.objects.all()
# date = Object.objects.all()
# specifications = Object.objects.all()
# historik = Object.objects.all()
# avariem_situation = Object.objects.all()
# return render(request, 'index.html',
#               {'name': name, 'date': date, 'specifications': specifications, 'historik': historik,
#                'avariem_situation': avariem_situation})


def otziv(request):
    return render(request, 'otziv.html')

class MyDetailView(DetailView):
    model = Object
    template_name = 'detail.html'
    template_nama = 'detail.html'
    context_object_name = 'test'


def set_cookie(request):
    html = HttpResponse("<h1>Мой сайт</h1><p><h3>Delete my cooke</h3></p>")
    if request.COOKIES.get('visit_count'):
        visit_count = int(request.COOKIES.get('visit_count')) + 1
        html.set_cookie('visit_count', str(visit_count))

    else:
        visit_count = 1
        html.set_cookie('visit_count', str(visit_count))
    return html


def del_cookie(request):
    html = redirect('home_page')
    if request.COOKIES.get('visit_count'):
        html.delete_cookie('visit_count')
    return html


def home(request):
    objects = Object.objects.order_by('-date_publication')[:3]
    return render(request, 'index.html', {'objects': objects})


def aircraft_details(request, id):
    obj = Object.objects.get(id=id)
    return render(request, 'aircraft_detail.html', {'object': obj})


def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserProfileForm()
    return render(request, 'register.html', {'form': form})


@login_required
def role_redirect(request):
    return render(request, '__all__')


def search_aircraft(request):
    query = request.GET.get('q')
    if query:
        try:
            aircraft = Object.objects.get(name__iexact=query)
            return redirect('aircraft_poisk', pk=aircraft.pk)
        except Object.DoesNotExist:
            return render(request, 'search_results.html', {'message': 'Такой модели самолета нет.'})
    return redirect('home')


def aircraft_poisk(request, pk):
    aircraft = get_object_or_404(Object, pk=pk)
    return render(request, 'aircraft_poisk.html', {'aircraft': aircraft})


name = (' Я люблю и принемаю себя даже если я хочу...'
        ' даже если я хочу концентрировать своё внемание сабытие в соей жизни на 100% сейчас на всегда без всяких условий. вдох выдох . '
        'Я люблю и принемаю себя даже если я не хочу... Вдох выдох')


class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get('has_visited'):
            today = datetime.today().date()
            visitor, created = SiteVisitor.objects.get_or_create(date=today)
            visitor.count += 1
            visitor.save()
            request.session['has_visited'] = True
        return self.get_response(request)