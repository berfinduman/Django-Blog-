from django import forms

class Register(forms.Form):
    username=forms.CharField(max_length=50, label="Kullanıcı Adı  ")
   
    name=forms.CharField(max_length=50, label="AD  ")
    surname=forms.CharField(max_length=50, label="Soyad: ")
    
    password=forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    
    confirm=forms.CharField(max_length=20, label="Parola Doğrula", widget=forms.PasswordInput)
    def clean(self):
        username=self.cleaned_data.get("username")
        name=self.cleaned_data.get("name")
        surname=self.cleaned_data.get("surname")
          
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")
        if password and confirm and (password!= confirm):
            raise forms.ValidationError("Parolalar Eşleşmiyor.")

        values={
            "username": username,
            "name": name,
            "surname": surname,
            
            "password": password,
            "confirm": confirm
        }
        return values

class Login(forms.Form):
    username=forms.CharField(max_length=50, label="Kullanıcı Adı  ")
    password=forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    