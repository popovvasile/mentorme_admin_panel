# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Career(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    companyname = models.CharField(db_column='companyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fieldofwork = models.CharField(db_column='fieldOfWork', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(max_length=255, blank=True, null=True)
    iscurrent = models.NullBooleanField(db_column='isCurrent')  # Field name made lowercase.
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'career'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Education(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    schoolcategory = models.CharField(db_column='schoolCategory', max_length=255, blank=True, null=True)  # Field name made lowercase.
    institutiontype = models.CharField(db_column='institutionType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    degreetype = models.CharField(db_column='degreeType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    matriculationdate = models.DateField(db_column='matriculationDate', blank=True, null=True)  # Field name made lowercase.
    graduationdate = models.DateField(db_column='graduationDate', blank=True, null=True)  # Field name made lowercase.
    iscurrent = models.NullBooleanField(db_column='isCurrent')  # Field name made lowercase.
    domainofstudy = models.CharField(db_column='domainOfStudy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'education'


class SchemaMigrations(models.Model):
    version = models.BigIntegerField(primary_key=True)
    inserted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    password_hash = models.CharField(max_length=255, blank=True, null=True)
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    currentcountry = models.CharField(db_column='currentCountry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    educationdomain = models.CharField(db_column='educationDomain', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mentorapprovalrequest = models.BooleanField(db_column='mentorApprovalRequest')  # Field name made lowercase.
    approvedasmentor = models.BooleanField(db_column='approvedAsMentor')  # Field name made lowercase.
    fullname = models.CharField(db_column='fullName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactvalue = models.CharField(db_column='contactValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contacttype = models.CharField(db_column='contactType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(max_length=255, blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    currentlocation = models.CharField(db_column='currentLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fieldofstudy = models.CharField(db_column='fieldOfStudy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    avatarlink = models.CharField(db_column='avatarLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email_verified = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'user'

class AdminNotes(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    text_notes = models.TextField(blank=True, null=True)
    admin_name = models.CharField(max_length=255, blank=True, null=True)
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'admin_notes'