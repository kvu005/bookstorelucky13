from django.db import models
# from django.contrib.auth.hashers import make_password

class User(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.EmailField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    home_address = models.CharField(max_length=200, null=True, blank=True)


    # def set_password(self, password: str) -> None:
    #     self.password = make_password(password)

    #     print("#" * 100)
    #     print(self.password)
    #     print("#" * 100)
    #     self.save()

    def __str__(self) -> str:
        return self.username