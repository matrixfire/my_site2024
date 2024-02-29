from django import views
from django.urls import path, include
from . import views

app_name = "core"

urlpatterns = [

    # Homepage
    path("", views.index, name="index"),
    # path("products/", views.product_list_view, name="product_list"),
    # path("product/<pid>/", views.product_detail_view, name="product_detail"),

    path('products/', views.product_list, name='product_list'), # product-list -> product_list
    path('products/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    # path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('product/<pid>/<slug:slug>/', views.product_detail, name='product_detail'),


    # Category
    path("category/", views.category_list_view, name="category_list"),
    path("category/<cid>/", views.category_product_list__view, name="category_product_list"),

    # Vendor
    path("vendors/", views.vendor_list_view, name="vendor_list"),
    path("vendor/<vid>/", views.vendor_detail_view, name="vendor_detail"),

    # Tags
    path("products/tag/<slug:tag_slug>/", views.tag_list, name="tags"),

    # Add Review
    path("ajax_add_review/<int:pid>/", views.ajax_add_review, name="ajax_add_review"),

    # Search
    path("search/", views.search_view, name="search"),

    # Filter product URL
    path("filter_products/", views.filter_product, name="filter_product"),

    # Add to cart URL
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),

    # Cart Page URL
    path("cart/", views.cart_view, name="cart"),

    # Delete Item from Cart
    path("delete_from_cart/", views.delete_item_from_cart, name="delete_from_cart"),

    # Update Cart
    path("update_cart/", views.update_cart, name="update_cart"),

    # Checkout URL
    path("checkout/", views.checkout_view, name="checkout"),

    # Paypal URL
    path('paypal/', include('paypal.standard.ipn.urls')),

    # Payment Successful
    path("payment_completed/", views.payment_completed_view, name="payment_completed"),

    # Payment Failed
    path("payment_failed/", views.payment_failed_view, name="payment_failed"),

    # Dashboard URL
    path("dashboard/", views.customer_dashboard, name="dashboard"),

    # Order Detail URL
    path("dashboard/order/<int:id>", views.order_detail, name="order_detail"),

    # Making address default
    path("make_default_address/", views.make_address_default, name="make_default_address"),

    # Wishlist page
    path("wishlist/", views.wishlist_view, name="wishlist"),

    # Adding to wishlist
    path("add_to_wishlist/", views.add_to_wishlist, name="add_to_wishlist"),

    # Removing from wishlist
    path("remove_from_wishlist/", views.remove_wishlist, name="remove_from_wishlist"),

    path("contact/", views.contact, name="contact"),
    path("ajax_contact_form/", views.ajax_contact_form, name="ajax_contact_form"),

    path("about_us/", views.about_us, name="about_us"),
    path("purchase_guide/", views.purchase_guide, name="purchase_guide"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path("terms_of_service/", views.terms_of_service, name="terms_of_service"),
]
