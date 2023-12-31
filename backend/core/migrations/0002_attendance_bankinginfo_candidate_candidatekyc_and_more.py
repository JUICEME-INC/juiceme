# Generated by Django 4.2.4 on 2023-08-14 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('JAN', 'January'), ('FEB', 'February'), ('MAR', 'March'), ('APR', 'April'), ('MAY', 'May'), ('JUN', 'June'), ('JUL', 'July'), ('AUG', 'August'), ('SEP', 'September'), ('OCT', 'October'), ('NOV', 'November'), ('DEC', 'December')], max_length=50)),
                ('days', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='BankingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banking_system', models.CharField(choices=[('MM', 'Mobile Money'), ('TB', 'Traditional Bank')], max_length=120)),
                ('bank_name', models.CharField(max_length=120)),
                ('account_number', models.CharField(max_length=15)),
                ('account_name', models.CharField(max_length=120)),
                ('mobile_network', models.CharField(max_length=120)),
                ('banking_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('middle_name', models.CharField(blank=True, max_length=120, null=True)),
                ('last_name', models.CharField(max_length=120)),
                ('dob', models.DateField(max_length=8)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('D', 'Different')], max_length=15)),
                ('maritual_status', models.CharField(choices=[('SINGLE', 'Single'), ('MARRIED', 'Married'), ('DIVORCE', 'Divorced'), ('WIDOW', 'Widow')], max_length=15)),
                ('prefered_industry', models.CharField(max_length=120)),
                ('salary_expectation', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('education_level', models.CharField(blank=True, choices=[('A', 'Primary School'), ('B', 'Less than high School or O-Level'), ('C', 'High School or A-Level'), ('D', 'Diploma'), ('E', 'Certificates of Completion'), ('F', "Bachelor's Degree"), ('G', "Master's Degree"), ('H', 'Professional Degree (LLB, JB, ThD, PharmD)'), ('I', 'Doctorate (PhD,EdD)'), ('J', 'Medical Degree (MD, DVM, DDS)')], max_length=50, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('Experience', models.TextField(blank=True, null=True)),
                ('language', models.CharField(choices=[('SW', 'Swahili'), ('ENG', 'English'), ('AFK', 'Afrikana')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateKYC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity_type', models.CharField(max_length=20)),
                ('identity_issuer', models.CharField(max_length=120)),
                ('identity_number', models.CharField(max_length=120)),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('id_type', models.CharField(max_length=30)),
                ('id_number', models.CharField(max_length=64)),
                ('sector', models.CharField(max_length=120)),
                ('registration_date', models.DateField()),
                ('ownership', models.CharField(choices=[('Private', 'Private'), ('Public', 'Public'), ('Partnership', 'Partnership'), ('NGO', 'NGO')], max_length=64)),
                ('owners_name', models.CharField(max_length=120)),
                ('owners_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('owner_email', models.EmailField(max_length=254, verbose_name='Owners Email Address')),
                ('contact_person_name', models.CharField(max_length=120)),
                ('contact_person_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('contact_person_email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('region', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeWage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('total_paid_ewa', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='EmployerHR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(max_length=20, unique=True)),
                ('dob', models.DateField()),
                ('designation', models.CharField(choices=[('Team Leader', 'Team Leader'), ('Project Manager', 'Project Manager'), ('Senior Developer', 'Senior Developer'), ('Junior Developer', 'Junior Developer'), ('Intern', 'Intern'), ('QA Tester', 'QA Tester')], max_length=50)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employement_type', models.CharField(choices=[('C', 'Contractor'), ('F', 'Fixed Term'), ('P', 'Permanent')], max_length=15)),
                ('designation', models.CharField(choices=[('Team Leader', 'Team Leader'), ('Project Manager', 'Project Manager'), ('Senior Developer', 'Senior Developer'), ('Junior Developer', 'Junior Developer'), ('Intern', 'Intern'), ('QA Tester', 'QA Tester')], max_length=50)),
                ('net_salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('hired_date', models.DateField()),
                ('terminated_date', models.DateField(blank=True, null=True)),
                ('is_terminated', models.BooleanField(default=False)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.candidate')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.company')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('publish_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('request_reason', models.TextField()),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('destination_wallet', models.CharField(max_length=50)),
                ('employee_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requesterId', to='core.employment')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('whatsapp_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('home_address', models.CharField(max_length=120)),
                ('region', models.CharField(max_length=120)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='RequestStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', models.DateTimeField()),
                ('hr_status', models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=13)),
                ('hr_status_update_time', models.DateTimeField(auto_now_add=True)),
                ('juice_dispursed_status', models.CharField(choices=[('A', 'Settled'), ('B', 'Juice Pending To Be Complete'), ('C', 'HR approval Waiting'), ('E', 'Was Rejected'), ('F', 'Incomplete Request')], max_length=12)),
                ('juice_status_time', models.DateTimeField()),
                ('request_Id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.paymentrequest')),
            ],
        ),
        migrations.CreateModel(
            name='WorkAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.TextField()),
                ('assign_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('assigner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignerId', to='core.employment')),
                ('tasker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskerId', to='core.employment')),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
        migrations.AddField(
            model_name='employeewage',
            name='employeeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.employment'),
        ),
        migrations.AddField(
            model_name='bankinginfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.candidate'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='employeeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.candidate'),
        ),
    ]
