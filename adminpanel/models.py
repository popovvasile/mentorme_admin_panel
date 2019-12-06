# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django_model_changes import ChangesMixin

from django.core.mail import EmailMultiAlternatives
from mentorme_admin import settings

from django.utils.html import strip_tags
from django.db import models


def send_approved_as_mentor(email):
    subject = "Confirmarea statutului de mentor"
    html_content = EmailTemplates.objects.get(name="ApproveMentor").text
    text_content = strip_tags(html_content)  # Strip the html tag. So people can see the pure text at least.
    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email], )
    msg.content_subtype = "html"
    msg.send()


def send_rejected_as_mentor(email):
    subject = "Informatii privind acordarea statutului de mentor"
    text_content = EmailTemplates.objects.get(name="RejectMentor").text
    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email])
    msg.content_subtype = "html"
    msg.send()


class Career(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('UserMentorMe', models.DO_NOTHING, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    companyname = models.CharField(db_column='companyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fieldofwork = models.CharField(db_column='fieldOfWork', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(max_length=255, blank=True, null=True)
    iscurrent = models.NullBooleanField(db_column='isCurrent')  # Field name made lowercase.
    inserted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    jobtitle = models.CharField(db_column='jobTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = "Career item"
        verbose_name_plural = "Career items"
        db_table = 'career'

class AdminNotes(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('UserMentorMe', models.DO_NOTHING, blank=True, null=True)
    text_notes = models.TextField(blank=True, null=True)
    admin_name = models.CharField(max_length=255, blank=True, null=True)
    inserted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Admin Note"
        verbose_name_plural = "Admin Notes"
        db_table = 'admin_notes'

class Education(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('UserMentorMe', models.DO_NOTHING, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    schoolcategory = models.CharField(db_column='schoolCategory', max_length=255, blank=True, null=True)  # Field name made lowercase.
    institutiontype = models.CharField(db_column='institutionType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    degreetype = models.CharField(db_column='degreeType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    matriculationdate = models.DateField(db_column='matriculationDate', blank=True, null=True)  # Field name made lowercase.
    graduationdate = models.DateField(db_column='graduationDate', blank=True, null=True)  # Field name made lowercase.
    iscurrent = models.NullBooleanField(db_column='isCurrent')  # Field name made lowercase.
    domainofstudy = models.CharField(db_column='domainOfStudy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inserted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    institutionname = models.CharField(db_column='institutionName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = "Education item"
        verbose_name_plural = "Education items"
        db_table = 'education'


class EmailTemplates(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Email template"
        verbose_name_plural = "Email templates"
        db_table = 'email_templates'


class UserMentorMe(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    password_hash = models.CharField(max_length=255, blank=True, null=True)
    inserted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mentorapprovalrequest = models.BooleanField(db_column='mentorApprovalRequest')  # Field name made lowercase.
    approvedasmentor = models.BooleanField(db_column='approvedAsMentor')  # Field name made lowercase.
    bio = models.TextField(blank=True, null=True)
    currentlocation = models.CharField(db_column='currentLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avatarlink = models.CharField(db_column='avatarLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email_verified = models.NullBooleanField()
    cvlink = models.CharField(db_column='cvLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locationoforigin = models.CharField(db_column='locationOfOrigin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'user'
        verbose_name = "User"
        verbose_name_plural = "Users"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):


        if self.id:
            old_instance = UserMentorMe.objects.get(pk=self.id)
            if old_instance.approvedasmentor == False and self.approvedasmentor == True:
                send_approved_as_mentor(email = old_instance.email)
            if old_instance.approvedasmentor == False \
                    and old_instance.mentorapprovalrequest == True \
                    and self.approvedasmentor == False and self.mentorapprovalrequest == False:
                send_rejected_as_mentor(email=old_instance.email)
        super(UserMentorMe, self).save()


class UserContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    contactvalue = models.CharField(db_column='contactValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contacttype = models.CharField(db_column='contactType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey(UserMentorMe, models.DO_NOTHING, blank=True, null=True)
    inserted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    preferedtype = models.NullBooleanField(db_column='preferedType')  # Field name made lowercase.

    class Meta:
        db_table = 'user_contact'
