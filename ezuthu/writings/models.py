from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    language = models.CharField(
        max_length=50,
        default="Malayalam"
    )

    def __str__(self):
        return self.name

class Writing(models.Model):
    WRITING_TYPE_CHOICES = (
        ('poem', 'Poem'),
        ('story', 'Story'),
        ('essay', 'Essay'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.ForeignKey(
        Writer,
        on_delete=models.CASCADE,
        related_name='writings'
    )
    writing_type = models.CharField(
        max_length=20,
        choices=WRITING_TYPE_CHOICES,
        default='poem'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title