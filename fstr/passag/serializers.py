from .models import *
from rest_framework import serializers
import json



class CoordsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Coords
       fields = '__all__'
   def create(self, validated_data):

       return Coords.objects.create(**validated_data)

class UzersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Uzers
       fields ='__all__' #['name']

   def create(self, validated_data):

        return Uzers.objects.create(**validated_data)


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = '__all__'

    def create(self, validated_data):
        return Img.objects.create(**validated_data)

class PerevalTestSerializer(serializers.ModelSerializer):

   point = (serializers.StringRelatedField(many=False))
   user = (serializers.StringRelatedField(many=False))
   images = (serializers.StringRelatedField(many=False))
   # status = serializers.ReadOnlyField()


   class Meta:
       model = PerevalAdded
       exclude =['status', 'id', 'add_time']



class PerevalAddedSerializer(serializers.ModelSerializer):
   point = CoordsSerializer()
   user = UzersSerializer()
   images = ImgSerializer()
   status = serializers.ReadOnlyField()


   class Meta:
       model = PerevalAdded
       fields =  '__all__'



   def create(self, validated_data):
        point_obj = CoordsSerializer(data=validated_data['point'])
        point_obj.is_valid(raise_exception=True)
        point_obj.save()
        print('объект географической точки:  ', point_obj.instance)
        validated_data['point']=point_obj.instance

        images_obj = ImgSerializer(data=validated_data['images'])
        images_obj.is_valid(raise_exception=True)
        images_obj.save()
        print('объект фотографий:  ',images_obj.instance)
        validated_data['images'] = images_obj.instance

        user_obj = UzersSerializer(data=validated_data['user'])
        user_obj.is_valid(raise_exception=True)
        user_obj.save()
        print('объект пользователя:  ',user_obj.instance)
        validated_data['user'] = user_obj.instance
        validated_data['status'] = 'new'
        if validated_data['level_winter'] is None or validated_data['level_winter'] == 'null':
            print('level_winter', validated_data['level_winter'])
            validated_data['level_winter'] = '1a'
        if validated_data['level_summer'] is None or validated_data['level_summer'] == 'null':
            print('level_summer', validated_data['level_summer'])
            validated_data['level_summer'] = '1a'
        return PerevalAdded.objects.create(**validated_data)



class PerevalPatchSerializer(serializers.ModelSerializer):
   point = CoordsSerializer(many=False)
   #user = UzersSerializer()
   images = ImgSerializer()

   class Meta:
       model = PerevalAdded
       fields =  '__all__'
       read_only_fields = ('user',)



   def update(self, instance, validated_data):

       current_point = Coords.objects.get(pk=instance.point_id)
       print(validated_data.get('point', instance.point))
       point = validated_data.get('point')
       if point:
           current_point.longitude = point.get('longitude', instance.point.longitude)
           current_point.latitude = point.get('point', instance.point.latitude)
           current_point.height = point.get('point', instance.point.height)
           current_point.save()

       current_img = Img.objects.get(pk=instance.images_id)
       print(validated_data.get('images', instance.images))
       imago = validated_data.get('images')
       if imago:
           current_img.about_1 = imago.get('about_1', instance.images.about_1)
           current_img.pic_1 = imago.get('pic_1', instance.images.pic_1)
           current_img.about_2 = imago.get('about_2', instance.images.about_2)
           current_img.pic_2 = imago.get('pic_2', instance.images.pic_2)
           current_img.about_3 = imago.get('about_3', instance.images.about_3)
           current_img.pic_3 = imago.get('pic_3', instance.images.pic_3)
           current_img.save()


       instance.beautyTitle = validated_data.get('beautyTitle', instance.beautyTitle)
       instance.title = validated_data.get('title', instance.title)
       instance.other_titles = validated_data.get('other_titles', instance.other_titles)
       instance.connect_other_titles = validated_data.get('connect_other_titles', instance.connect_other_titles)
       instance.add_time = validated_data.get('add_time', instance.add_time)
       #instance.user = validated_data.get('user', instance.user)
       instance.level_winter = validated_data.get('level_winter', instance.level_winter)
       instance.level_summer = validated_data.get('level_summer', instance.level_summer)
       instance.status = validated_data.get('status', instance.status)

       instance.save()

       return instance











