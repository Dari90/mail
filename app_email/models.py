from django.db import models
from django.core.mail import send_mail
from email1.settings import EMAIL_HOST_USER
import time, threading


class Email(models.Model):
    interval = models.PositiveSmallIntegerField()
    message = models.CharField(max_length=255)
    sent = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.sent == False:
            threads = []
            t = threading.Thread(target=mail_send, args=(self, ))
            threads.append(t)
            t.start()
            t.join()

def mail_send(self):
    time.sleep(self.interval)
    ts = send_mail('Dz', self.message, EMAIL_HOST_USER, ['veonnika39@gmail.com'], fail_silently=False)
    if ts == 1:
        self.sent = True
        self.save()