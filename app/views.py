from datetime import datetime
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from app.models import AboutMe, MyProject, MySkill, MyAward, MyInformation, MySocial, ContactFormLog, HitCount
# Create your views here.

def index(request):
    descriptions = AboutMe.objects.first()
    myProject = MyProject.objects.all()
    mySkill = MySkill.objects.all()
    myAward = MyAward.objects.all()
    myInformation = MyInformation.objects.first() #só vou usar um unico dado e não há necessidade de percorrer lista para ter 1 dado
    mysocial = MySocial.objects.first()

    # Cria/pega o contador
    hit, created = HitCount.objects.get_or_create(id=1)

    # Checa se o usuário já contou nesta sessão
    if not request.session.get('hitcount_session'):
        hit.count += 1
        hit.save()
        request.session['hitcount_session'] = True

    # Divide as tecnologias por vírgula e salva como uma nova variável em cada projeto
    for proj in myProject:
        proj.project_Tools_list = [tool.strip() for tool in proj.project_Tools.split(",")]

    for skill in mySkill:
        skill.skill_Item_list = [item.strip() for item in skill.skill_Items.split(",")]

    context = {
        "aboutMe": descriptions,#invés de retornar none vair retornar string vazia...
        "myProject": myProject,
        "mySkill": mySkill,
        "myAward": myAward,
        "myInfo": myInformation,
        "mysocial": mysocial,
        "hitcount": hit.count,
    }

    return render(request, "index.html", context)

def contact_form(request):
    if request.method == 'POST':
        print("\n\n  Utilizizador submeteu um formulário. \n\n")
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        context = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
        }

        html_content = render_to_string('email.html', context) #O texto esta com o estilo do email 
       
        is_success = False
        error_message = ""

        try:
            send_mail(
                subject=subject,
                message=None,# se ntiver irá dar erro. agora usamos o email.html para mandar com a estrutura e style
                html_message=html_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False, #.default is True
            )
        except Exception as e:
            error_message = str(e)
            messages.error(request, "Ocorreu um erro, não foi possível enviar o email")
        else:
            is_success = True
            messages.success(request, "Email enviado com sucesso!!!")

        ContactFormLog.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            action_time=timezone.now(),
            is_success=is_success,
            error_message=error_message
        )
    return redirect('home')