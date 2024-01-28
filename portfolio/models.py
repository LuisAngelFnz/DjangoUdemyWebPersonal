from django.db import models

# Create your models here.
class Project(models.Model):
    title       = models.CharField(verbose_name='Titulo',max_length=200)
    description = models.TextField(verbose_name='Descripción')
    image       = models.ImageField(verbose_name='Imagen', upload_to='projects')
    url         = models.URLField(verbose_name='Dirección Web', null=True, blank=True)
    created     = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated     = models.DateTimeField(verbose_name='Fecha de edición', auto_now=True)

    class Meta:
        verbose_name        = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering            = ['-created']
    
    def __str__(self):
        return self.title
    
