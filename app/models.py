from django.db import models

# Create your models here.

class HitCount(models.Model):
    count = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Hits: {self.count}"

class AboutMe(models.Model):
    title = models.CharField(max_length=22, default = "JR Portfolio")
    helloMessage = models.CharField(max_length=55, default="Olá, Sou João Roberto")
    welcomeText = models.CharField(max_length=255,default="Sou um desenvolvedor de software com experiência em transformar ideias em" \
    " soluções tecnológicas eficientes, sempre focado em melhorar a performance e a experiência do utilizado")
    welcomeMessage = models.CharField(max_length=55, default = "Bem-vindo ao meu portfólio!")
    
    description1 = models.CharField(max_length=500, default = "")
    description2 = models.CharField(max_length=255, default = "")
    description3 = models.CharField(max_length=355, default = "")

    def __str__(self):
        return self.title

class MyProject(models.Model):
    project_Name = models.CharField(max_length = 30, default = "")
    project_Description = models.CharField(max_length=255, default = "")
    project_Tools = models.CharField(max_length = 255, default = "")
    project_Link = models.CharField(max_length=255, default = "", blank=True, null=True) # ver se tem bug quando clicar o btn ver project enquanto naotem link 

    def __str__(self):
        return self.project_Name

class MySkill(models.Model):
    skill_Name = models.CharField(max_length = 30, default = "")
    skill_Items = models.CharField(max_length = 255, default = "")

    def __str__(self):
        return self.skill_Name

class MyAward(models.Model):
    award_Name = models.CharField(max_length = 255, default = "")
    award_Year = models.CharField(max_length = 45, default = "")
    award_Description = models.CharField(max_length = 255, default = "")
    
    def __str__(self):
        return self.award_Name

class MyInformation(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=18)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=60)

class MySocial(models.Model):
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.linkedin

class ContactFormLog(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null=True, blank=True)
    is_success = models.BooleanField(default=False)
    error_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email

