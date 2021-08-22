from django.urls import path

from .views import ReferralView


urlpatterns = [
	path("<uuid:identifier>", ReferralView.as_view(), name="gift_ref_reflink"),
]
