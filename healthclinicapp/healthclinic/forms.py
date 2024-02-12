from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, UserChangeForm
from healthclinic.models import CustomUser, Appointment


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class AppointmentForm(UserCreationForm):
    class Meta:
        model = Appointment
        fields = ['booking_date', 'booking_time']  # Thêm các trường khác nếu cần

    def clean_booking_time(self):
        booking_date = self.cleaned_data.get('booking_date')
        booking_time = self.cleaned_data.get('booking_time')

        if booking_date and booking_time:
            # Tính số lượng bệnh nhân đã đặt lịch cho time slot
            num_appointments = Appointment.objects.filter(booking_date=booking_date, booking_time=booking_time).count()

            # Kiểm tra số lượng bệnh nhân đã đặt lịch
            if num_appointments >= 3:
                raise forms.ValidationError("Số lượng bệnh nhân đã đặt lịch cho time slot này đã đạt tới giới hạn.")

        return booking_time
"""
class UserCreationForm2():
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY', 'class': 'datepicker'}), input_formats=['%d-%m-%Y'], required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'date_of_birth')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'date_of_birth')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
"""