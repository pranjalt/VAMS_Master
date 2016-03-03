from rest_framework import serializers

from models import *

class GenderSerializer(serializers.ModelSerializer):
     gender = serializers.CharField(read_only=True)
     class Meta:
        model = Gender
        fields = ('gender_id','gender')

class RoleSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)
    class Meta:
        model = Role
        fields = ('role_id','role')
        
class SecurityQuestionsSerializer(serializers.ModelSerializer):
    sec_ques = serializers.CharField(read_only=True)
    class Meta:
        model = SecurityQuestions
        fields = ('sec_ques_id','sec_ques')

class CitySerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(read_only=True)
    class Meta:
        model = City
        fields = ('city_id','city_name')


class CountrySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(read_only=True)
    class Meta:
        model = Country
        fields = ('country_id','country_name')
    
class ProvinceSerializer(serializers.ModelSerializer):
    province_name = serializers.CharField(read_only=True)
    class Meta:
        model = Province
        fields = ('province_id','province_name')
        
class SportsSerializer(serializers.ModelSerializer):
    sports_name = serializers.CharField(read_only=True)
    class Meta:
        model = Sports
        fields = ('sports_id','sports_name')
    
class PlayerListSerializer(serializers.ModelSerializer):
    sports_name = serializers.CharField(source='sports.sports_name', read_only=True)
    class Meta:
        model = PlayerOnboarding
        fields = ('player_id','first_name', 'middle_name', 'last_name','email_id','contact_no','date_of_birth','sports_name','total_yrs_exp')

class CoachListSerializer(serializers.ModelSerializer):
    sports_name = serializers.CharField(source='sports.sports_name', read_only=True)
    class Meta:
        model = CoachOnboarding
        fields = ('coach_id','first_name', 'middle_name', 'last_name','email_id','contact_no','date_of_birth','sports_name','total_yrs_exp')

                

class SportListSerializer(serializers.HyperlinkedModelSerializer):

    players = PlayerListSerializer(many = True , read_only = True)
    player_count = serializers.IntegerField()
    print player_count
    class Meta:
        model = Sports
        fields = ('sports_name','players','player_count')

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = ('country', 'province','city','street1','street2','zipcode')
    
class OnboardingSerializer(serializers.ModelSerializer): 
    address=AddressSerializer()
    
    class Meta:
        model = Onboarding
        fields = ('first_name', 'middle_name','last_name','gender','email_id','contact_no','date_of_birth','sports','total_yrs_exp','sec_ques','sec_ans1','sec_ques','sec_ans2','role','address')
        #fields = ('first_name', 'middle_name','last_name','gender','email_id','contact_no','date_of_birth','sports','total_yrs_exp','sec_ques','sec_ans1','sec_ques','sec_ans2','role')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        validated_data['address'] = address
        training = Training.objects.create(**validated_data)
        return training
class AddSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.country_name', read_only=True)
    province = serializers.CharField(source='province.province_name', read_only=True)
    city = serializers.CharField(source='city.city_name', read_only=True)
    class Meta:
        model = Address
        fields = ('country', 'province','city','street1','street2','zipcode')    
    
class CoachSerializer(serializers.ModelSerializer): 
   # address=AddressSerializer()
    
    class Meta:
        model = CoachOnboarding
        fields = ('first_name', 'middle_name','last_name','gender','email_id','contact_no','date_of_birth','sports','total_yrs_exp','sec_ques','sec_ans1','sec_ques','sec_ans2')
        #fields = ('first_name', 'middle_name','last_name','gender','email_id','contact_no','date_of_birth','sports','total_yrs_exp','sec_ques','sec_ans1','sec_ques','sec_ans2','address')
        #fields = ('first_name', 'middle_name','last_name','gender','email_id','contact_no','date_of_birth','sports','total_yrs_exp','sec_ques','sec_ans1','sec_ques','sec_ans2','role')

    """ def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        validated_data['address'] = address
        coach_onboarding = CoachOnboarding.objects.create(**validated_data)
        return coach_onboarding"""
    
class PlayerSerializer(serializers.ModelSerializer): 
    #address=AddressSerializer()
    
    class Meta:
        model = PlayerOnboarding
        #fields = ('first_name', 'middle_name','last_name','gender','email_id','contact_no','date_of_birth','sports','total_yrs_exp','sec_ques','sec_ans1','sec_ques','sec_ans2','address')
        fields = ('first_name', 'middle_name','last_name','gender','email_id','contact_no','date_of_birth','sports','total_yrs_exp','sec_ques','sec_ans1','sec_ques','sec_ans2')
