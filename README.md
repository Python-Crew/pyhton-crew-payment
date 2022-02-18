# Python crew payment

Python crew payment is a Python library for dealing with payment and bank gateways

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pythoncrewpayment.

```bash
pip install python-crew-payment
```

## Usage

Edit your settings.py
Add to INATALLED_APPS:

```python
"django_prices",
"enmerkar",
"user",
"payment",
"order",
```

Add this to your settings.py:

```python
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
```

## License
[MIT](https://choosealicense.com/licenses/mit/)