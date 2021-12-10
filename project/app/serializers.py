from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, get_user_model


# user = get_user_model()

class UserSerializer(serializers.ModelSerializer): #Serializer
    password = serializers.CharField(max_length=65, min_length=8, write_only=True,style={'input_type': 'password'})
    email = serializers.EmailField(max_length=255, min_length=4)
  
    class Meta:
    	model = User
    	fields = ['email','password']

    def validate(self, attrs):
        if User.objects.filter(email=attrs["email"]): #.exist()
            raise serializers.ValidationError({"email",("email is already in use")})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(validated_data)



class LoginSerializer(serializers.ModelSerializer):
	email = serializers.CharField(max_length=255)
	password = serializers.CharField(max_length=128,write_only=True,label="Password",
		style={'input_type': 'password'},trim_whitespace=False)

	class Meta:
		model = User
		fields = ['email','password']


	def validate(self,data):
		email = data.get('email',None)
		password = data.get('password',None)
		user = authenticate(email=email, password=password)	

		if user is None:
			raise serializers.ValidationError('A User with this email and Password is not found')

		else:
			msg = 'Must include "email" and "password".'
			raise serializers.ValidationError(msg)

				














"""
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )

    def validate(self, data):
        #username = data.get('email')
        email = data.get('email')
        password = data.get('password')

        #if username and password:
        if email and password:
            
            # user = authenticate(request=self.context.get('request'),
            #                     username=username, password=password)
            
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            #msg = 'Must include "username" and "password".'
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data

"""        