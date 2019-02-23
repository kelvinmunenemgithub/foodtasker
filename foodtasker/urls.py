from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from foodtaskerapp import views, apis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # Restaurant Owners Sign Up, In, Out
    path('restaurant/sign-in/', auth_views.LoginView.as_view(
        template_name='restaurant/sign_in.html'), name='restaurant-sign-in'),
    path('restaurant/sign-out', auth_views.LogoutView.as_view(next_page='/'),
         name='restaurant-sign-out'),
    path('restaurant/sign-up/', views.restaurant_sign_up, name='restaurant-sign-up'),
    path('restaurant/', views.restaurant_home, name='restaurant-home'),

    # Restaurant Order, Meal, Report, Account
    path('restaurant/account/', views.restaurant_account, name='restaurant-account'),
    path('restaurant/meal/', views.restaurant_meal, name='restaurant-meal'),
    path('restaurant/meal/add/', views.restaurant_add_meal, name='restaurant-add-meal'),
    path('restaurant/meal/edit/<int:meal_id>/', views.restaurant_edit_meal, name='restaurant-edit-meal'),
    path('restaurant/order/', views.restaurant_order, name='restaurant-order'),
    path('restaurant/report/', views.restaurant_report, name='restaurant-report'),

    # Customer/Driver Sign in Sign up
    # /convert-token (sign in/ sign up)
    # /revoke-token (sign out)
    path('api/social/', include('rest_framework_social_oauth2.urls')),

    # ajax order notification
    path('api/restaurant/order/notification/<str:last_request_time>/', apis.restaurant_order_notification),


    # APIs for customers
    # Get list of Restaurants
    path('api/customer/restaurants/', apis.customer_get_restaurants),

    # Get list of meals for restaurant
    path('api/customer/meals/<int:restaurant_id>/', apis.customer_get_meals),

    # Add the customer order to server
    path('api/customer/order/add/', apis.customer_add_order),

    # Get customer latest order
    path('api/customer/order/latest/', apis.customer_get_latest_order),

    # Send driver location to customer
    path('api/customer/driver/location/', apis.customer_driver_location),


    # APIs for DRIVERS
    path('api/driver/orders/ready/', apis.driver_get_ready_orders),
    path('api/driver/order/pick/', apis.driver_pick_order),
    path('api/driver/order/latest/', apis.driver_get_latest_order),
    path('api/driver/order/complete/', apis.driver_complete_order),
    path('api/driver/revenue/', apis.driver_get_revenue),
    path('api/driver/location/update/', apis.driver_update_location),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
