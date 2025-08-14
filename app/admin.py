from django.contrib import admin
from app.models import HitCount, AboutMe, MyProject, MySkill, MyAward, MyInformation, MySocial, ContactFormLog

# Register your models here.
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'helloMessage',
        'welcomeText',
        'welcomeMessage',
        'description1',
        'description2',
        'description3',    
    ]

    # #nao tem permicao para adicionar
    def has_add_permission(self, request, obj = None):
        return False
    
    # #nao tem permicao para deletar
    def has_delete_permission(self, request, obj = None):
        return False
    
@admin.register(MyProject)
class MyProjectAdmin(admin.ModelAdmin):
    list_display = [
        'project_Name',
        'project_Description',
        'project_Tools',
        'project_Link',
    ]

@admin.register(MySkill)
class MySkill(admin.ModelAdmin):
    list_display = [
        'skill_Name',
        'skill_Items',
    ]

@admin.register(MyAward)
class MyAward(admin.ModelAdmin):
    list_display = [
        'award_Name',
        'award_Year',
        'award_Description',
    ]

@admin.register(MyInformation)
class MyInformation(admin.ModelAdmin):
    list_display = [
        'email',
        'phone',
        'location',
        'description',
    ]

    # Nao tem permisao para adicionar
    def has_add_permission(self, request, obj = None):
        return False
    
    # #o admin nao tem permissao para deletar
    def has_delete_permission(self, request, obj = None):
        return False

@admin.register(MySocial)
class MySocial(admin.ModelAdmin):
    list_display = [
        'linkedin',
        'github',
        'instagram',
    ]

    # Nao tem permisao para adicionar
    def has_add_permission(self, request, obj = None):
        return False
    
    # #o admin nao tem permissao para deletar
    def has_delete_permission(self, request, obj = None):
        return False

@admin.register(ContactFormLog)
class ContactFormLog(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'subject',
        'message',
        'action_time',
        'is_success',
        'error_message',
    ]
    # Nao tem permisao para adicionar
    def has_add_permission(self, request, obj = None):
        return False

    # #nao tem permicao para alterar
    def has_change_permission(self, request, obj = None):
        return False
    
    # #o admin nao tem permissao para deletar
    def has_delete_permission(self, request, obj = None):
        return False

@admin.register(HitCount)
class HitCount(admin.ModelAdmin):
    list_display = [
        'count',
        'last_updated',
    ]

    # Nao tem permisao para adicionar
    def has_add_permission(self, request, obj = None):
        return False

    # #nao tem permicao para alterar
    def has_change_permission(self, request, obj = None):
        return False
    
    # #o admin nao tem permissao para deletar
    def has_delete_permission(self, request, obj = None):
        return False