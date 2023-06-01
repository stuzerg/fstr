from .models import *
from rest_framework import serializers


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


class PerevalAddedSerializer(serializers.ModelSerializer):
   point = CoordsSerializer(many=False)
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
        print(point_obj.instance)
        validated_data['point']=point_obj.instance

        images_obj = ImgSerializer(data=validated_data['images'])
        images_obj.is_valid(raise_exception=True)
        images_obj.save()
        print(images_obj.instance)
        validated_data['images'] = images_obj.instance

        user_obj = UzersSerializer(data=validated_data['user'])
        print("""validated_data["user"]""", validated_data['user'])
        user_obj.is_valid(raise_exception=True)
        user_obj.save()
        print(user_obj.instance)
        validated_data['user'] = user_obj.instance
        validated_data['status'] = 'new'
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
       for _field in validated_data.get('point',instance.point):
           setattr(current_point, _field, validated_data.get('point', instance.point)[_field])
           setattr(instance.point, _field, validated_data.get('point', instance.point)[_field])
       current_point.save()

       current_img = Img.objects.get(pk=instance.images_id)
       for _field in validated_data.get('images', instance.images):
           setattr(current_img,_field, validated_data.get('images', instance.images)[_field])
           setattr(instance.images, _field, validated_data.get('images', instance.images)[_field])
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











