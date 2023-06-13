from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from django.urls import reverse
from passag.models import PerevalAdded, Coords, Uzers, Img
from passag.serializers import PerevalAddedSerializer, PerevalPatchSerializer, PerevalTestSerializer
import json



# Create your tests here.
class PassageTest(APITestCase):

    def setUp(self):
        user1 = Uzers.objects.create(family = 'don', name = 'serg',patronymic ='greg', email = 'user1@11.ee', cell = 111)
        user2 = Uzers.objects.create(family='clegg', name='eugen', patronymic='luther', email='user2@22.ee', cell=222)
        r1 = PerevalAdded.objects.create(

        point = Coords.objects.create(latitude = 11, longitude = 11, height =111),
        images = Img.objects.create(about_1= 'about site', pic_1 = 'https://ru.wikipedia.org/wiki/Mount_Elbrus_May_2008.jpg'),
        beautyTitle ='old name',
        title = '2nd name',
        other_titles = 'other name',

        user = user1)
        r1.save()
        r2 = PerevalAdded.objects.create(

            point=Coords.objects.create(latitude=22, longitude=22, height=222),
            images=Img.objects.create(about_1='kazbek',
                                      pic_1='https://upload.wikimedia.org/wikipedia/commons/2/2a/Mount._Mkin'
                                            'varcveri_%28Kazbek%29_5033_m.%2C_Stefancminda_district.jpg'),
            status = 'pending',
            beautyTitle='old name',
            title='2nd name',
            other_titles='other name',

            user=user2)
        r2.save()
        r3 = PerevalAdded.objects.create(

            point=Coords.objects.create(latitude=33, longitude=33, height=333),
            images=Img.objects.create(about_1='cheget',
                                      pic_1='https://kavtur.ru/content/tour_images/37c145640d875a2a324ee70db10d7868.jpg'),
            status='new',
            beautyTitle='чегет',
            title='мингитау',
            other_titles='ошхамахо',

            user=user2)
        r3.save()

    def test_one_record_view(self):
        pk = PerevalAdded.objects.all().first().pk
        response = self.client.get(reverse('one', kwargs={"pk":pk}))
        serialized = PerevalAddedSerializer(PerevalAdded.objects.get(pk=pk))
        print('тест вывода записи по ID = ', serialized.data == response.json())
        self.assertEqual(serialized.data,response.json())

    def test_one_record_create(self):
        new_data_for_record = {
       "point": {
       "longitude": 7.1525,
       "latitude": 45.3842,
       "height": 1200
     },
            "user": {
                "family": "Пупкин",
                "name": "Василий",
                "patronymic": "Иванович",
                "email": "user@email.tld",
                "cell": 79031234567
            },
     "images": {
       "about_1": "Седловина",
       "pic_1": "https://pibig.info/uploads/posts/2022-11/1669749986_1-pibig-info-p-pkhiya-krasivo-1.jpg",
       "about_2": "",
       "pic_2": "",
       "about_3": "",
       "pic_3": ""
     },
     "title": "Пхия",
     "beautyTitle": "перевал",
     "other_titles": "string",
     "connect_other_titles": "",
     "level_winter": "",
     "level_summer": "1a"
     }
        response = self.client.post(reverse('sub'), data=new_data_for_record, format='json')
        serialized = PerevalTestSerializer(PerevalAdded.objects.all().last())

        serialized_new = serialized.data
        serialized_new['point'] = json.loads(serialized_new['point'])
        serialized_new['user'] = json.loads(serialized_new['user'])
        serialized_new['images'] = json.loads(serialized_new['images'])

        print('тест создания новой записи = ', serialized_new == new_data_for_record)
        self.assertEqual(serialized_new, new_data_for_record)

    def test_all_records_view(self):
        response = self.client.get(reverse('all'))
        serialized = PerevalAddedSerializer(PerevalAdded.objects.all(), many=True)
        print('тест вывода всех записей = ', serialized.data == response.json())
        self.assertEqual(serialized.data,response.json())

    def test_tryin_editing_notnew_status(self):
        pk =  PerevalAdded.objects.filter(status="pending").first().pk
        resp = self.client.patch(reverse('one', kwargs={'pk':pk}), data={"beautyTitle":"new name"}, format='json')
        print('отказ изменения поля beautyTitle у записи со статусом не "new" =', PerevalAdded.objects.get(pk=pk).beautyTitle != "new name")
        print(resp.status_code, resp.data.get('message'))
        self.assertEqual(resp.status_code, 403)

    def test_email_sifted(self):
        eml = 'user1@11.ee'
        response = self.client.get(reverse('sub')+'?user__email='+eml)
        serialized = PerevalAddedSerializer(PerevalAdded.objects.filter(user__email=eml), many=True)
        print('тест вывода фильтра по email = ', serialized.data == response.json())
        self.assertEqual(serialized.data, response.json())








