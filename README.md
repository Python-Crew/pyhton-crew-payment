# Python crew payment


## Instalation
''' pip intall '''

Edit your settings.py
Add to INATALLED_APPS:
'''  "django_prices",
    "enmerkar",
    "user",
    "payment",
    "order", '''

Add this to your settings.py:

'''
CALLBACK_URL = "your callback url"

BANK_CLASS = {
    "Zibal": "payment.banks.zibal.Zibal",
    "Stripe": "payment.banks.stripe.Stripe",
}

BANK_SETTINGS = {
    "zibal": {
        "merchant_code": "zibal",
        "token_api_url": "https://gateway.zibal.ir/v1/request",
        "payment_url": "https://gateway.zibal.ir/start/{}",
        "verify_api_url": "https://gateway.zibal.ir/v1/verify",
    },
    "stripe": {
        "api_key": os.environ.get(
            "STRIPE_API_KEY",
            "set your key",
        ),
    },
    "DEFAULT": "Zibal",
}

BANK_TYPE = "payment.banks.paymentstatuses.BankType"

'''