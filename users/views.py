from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib.messages import success, error
from django.contrib.auth import authenticate, login, logout
from .forms import Register, Login, ProfileEdit
from .models import ProfileModel,UserModel
# Create your views here.


class RegisterView(View):

    def get(self, request):

        reg_form = Register()
        return render(request, 'users/register.html', {'reg_form': reg_form})

    def post(self, request):

        reg_form = Register(request.POST)

        if reg_form.is_valid():
            try:
                reg_form.save()
            except:
                print("something went wrong")
                return HttpResponse("Something went wrong!")

        success(request, 'Your account created with successfully!', extra_tags='success')
        return redirect('index_url')


class LoginView(View):

    def get(self, request):
        form = Login()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = Login(request.POST)
        if form.is_valid():
            instance = form.cleaned_data
            user = authenticate(username=instance['username'], password=instance['password'])
            if user:
                login(request, user=user)
                success(request, 'You logged in with successfully!', extra_tags='success')
                return redirect('index_url')
            else:
                error(request, 'username or passsword is wrong!', extra_tags='danger')
                return redirect('login_url')    

def LogoutView(request):
    logout(request)
    success(request, "You've logged out with successfully!", extra_tags="success")
    return redirect("index_url")


def FollowOpView(request, id):

    if request.user.is_authenticated:

        target_user = UserModel.objects.get(id=id)
        target_user_profile = ProfileModel.objects.get(id=id)
        user_profile = get_object_or_404(ProfileModel, id=request.user.id)

        if request.user == target_user:
            error(request, "You can't follow yourself!", extra_tags="danger")
            return redirect(request.META.get("HTTP_REFERER"))

        if not request.user in target_user_profile.followers.all():
            target_user_profile.followers.add(request.user)
            user_profile.followings.add(target_user)
            print("followed")
            success(request, "Followed with successfully!", extra_tags="secondary")
            return redirect(request.META.get("HTTP_REFERER"))

        else:
            target_user_profile.followers.remove(request.user)
            user_profile.followings.remove(target_user)
            print("unfollowed")
            success(request, "Unfollowed with successfully!", extra_tags="secondary")
            return redirect(request.META.get("HTTP_REFERER"))

    else:
        error(request, "You should login into site first", extra_tags="danger")
        return redirect(request.META.get("HTTP_REFERER"))

class ProfileView(View):
    def get(self, request, username):
        user = UserModel.objects.get(username=username)
        user_profile = ProfileModel.objects.get(user=user)
        if request.user.username == username:
            profile_form = ProfileEdit()
            return render(request, "users/profile.html", {"user_profile": user_profile, "user": user, "profile_form": profile_form})
        return render(request, "users/profile.html", {"user_profile": user_profile, "user": user})

    def post(self,request, username):
        profile = request.user.profile
        form = ProfileEdit(data=request.POST, files=request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            success(request, "your profile updated with successfully")
            return redirect(request.META.get("HTTP_REFERER"))
