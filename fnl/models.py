from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

class LuckyDay(models.Model):
    rnk = models.IntegerField()
    yearx = models.IntegerField()
    monthx = models.IntegerField()
    dayx = models.IntegerField()
    datex = models.DateField(default=timezone.now)


class NotePost(models.Model):
    DAY_CHOICES = (
        ('1', 'Best'),
        ('2', 'Great'),
        ('3', 'Good'),
        ('4', 'Neutral'),
        ('5', 'Not OK'),
        ('6', 'Bad'),
        ('7', 'Worst'),
    )
    is_good_day = models.CharField(max_length=1, choices=DAY_CHOICES)
    reason = models.CharField(max_length=500)
    date_rec = models.DateField(default=timezone.now)

    def __str__(self):
        return self.pk
    
    def get_absolute_url(self):
        return reverse('manage_detail', args=[str(self.id)])

#('Best', 'Great', 'Good', 'Neutral', 'Not OK', 'Bad', 'Worst')