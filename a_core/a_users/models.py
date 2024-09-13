from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete = models.CASCADE)
    image = models.ImageField(upload_to='avatars/', blank=True ,null=True)
    displayname = models.CharField(max_length=20 ,null=True ,blank=True)
    info = models.TextField(blank=True , null=True)

    def __str__(self):
        return str(self.name)
    
    @property   #by using this @property decorator we can use the method name like "name" no use of writing like this "name()"
    def name(self):
        if self.displayname : # If a display name is provided, use it; otherwise, fall back to the username.
            name=self.displayname

         # Assuming the User model's username field is 'username' (note: in your original code, 
        # 'user_name' was used, which may be a typo unless you've customized the User model).
        else:      
            name= self.user.username
        return name

    @property
    def avatar(self):
        try:
            avatar=self.image.url
        except:
            avatar=static('images/avatar.svg')
        return avatar