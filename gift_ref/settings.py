from django.conf import settings


DJANGO_REFERRALS_SETTINGS = {
	"COOKIE_KEY": "gift-reflinks__rk",
	"COOKIE_HTTPONLY": True,
	"COOKIE_MAX_AGE": 60 * 60 * 24 * 365,
	"URL_PARAM": "ref",
}


DJANGO_REFERRALS_SETTINGS.update(
	getattr(settings, "DJANGO_REFERRALS_SETTINGS", {})
)


COOKIE_KEY = DJANGO_REFERRALS_SETTINGS["COOKIE_KEY"]
COOKIE_HTTPONLY = DJANGO_REFERRALS_SETTINGS["COOKIE_HTTPONLY"]
COOKIE_MAX_AGE = DJANGO_REFERRALS_SETTINGS["COOKIE_MAX_AGE"]
URL_PARAM = DJANGO_REFERRALS_SETTINGS["URL_PARAM"]
