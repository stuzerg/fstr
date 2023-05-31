from django.db import models

class Uzers(models.Model):
    family = models.CharField(max_length=20, verbose_name='Фамилия', blank=False)
    name = models.CharField(max_length=20, verbose_name='Имя', blank=False)
    patronymic = models.CharField(max_length=20, verbose_name='Отчество', blank=False)
    email = models.EmailField(max_length=50, verbose_name='эл.почта', blank=False, unique=True)
    cell = models.IntegerField(help_text='в формате 7903ххххххх', blank=False, verbose_name='сотовый', unique=True)
    def __str__(self):
        return self.email

class Coords(models.Model):
    longitude = models.FloatField(blank=False, verbose_name='долгота')
    latitude = models.FloatField(blank=False, verbose_name='широта')
    height = models.IntegerField(blank=False, verbose_name='высота')
    def __str__(self):
        return f'{self.longitude}° широты, {self.latitude}° долготы'


class Img(models.Model):
    about_1 = models.CharField(help_text='обязательное поле', max_length=100, verbose_name='описание фото_1', blank=False)
    pic_1 = models.URLField(help_text='обязательное поле', verbose_name='ссылка на фото_1', blank=False)
    about_2 = models.CharField(max_length=100, verbose_name='описание фото_2', blank=True)
    pic_2 = models.URLField(verbose_name='ссылка на фото_2', blank=True)
    about_3 = models.CharField(max_length=100, verbose_name='описание фото_3', blank=True)
    pic_3 = models.URLField(verbose_name='ссылка на фото_3', blank=True)


class PerevalAdded(models.Model):

    status_list = ( ('new', 'новый'),('pending', 'в работе'), ('accepted', 'принят'), ('rejected', 'отклонён'))
    difficult_list = (('1a', '1А'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'),
                      ('4a', '4А'),('4b', '4Б'), ('5a', '5А'), ('5b', '5Б'), ('6a', '6А'), ('6b', '6Б'))

    status = models.CharField( default='new', choices=status_list, verbose_name='статус модерации')
    point = models.OneToOneField(Coords, verbose_name='Координаты',related_name= 'xyz', on_delete=models.CASCADE)
    images = models.OneToOneField(Img, on_delete=models.CASCADE )
    beautyTitle = models.CharField(max_length=200, verbose_name='тип объекта', blank=False)
    title = models.CharField(max_length=200, verbose_name='название', blank=False)
    other_titles = models.CharField(max_length=200, verbose_name='альтернативное название', blank=False)
    connect_other_titles = models.CharField(max_length=200, verbose_name='что соединяет', blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Uzers, on_delete=models.CASCADE)
    level_winter = models.CharField(choices=difficult_list, blank=True, verbose_name='зима')
    level_summer = models.CharField(choices=difficult_list, blank=True, verbose_name='лето')


