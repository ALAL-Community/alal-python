# Alal

---

A PHP sdk to interact with Alal's API

## Getting started

### Requirements

This package requires Python 3.6+

### Installation

- `pip install alal-python`

### Usage

This SDK can be used both for Alal Sandbox and Production API.

### Setting ENV KEYS

For sucessfully running of the SDK; the `Alal_API_KEY` must be set.

Now this will throw a `AlalBadKeyError` error, if you do not set it as an environment variable, when initiatizing a function.

By default the SDK assumes that you are currently working on production, and your `Alal_API_KEY` must be a production-grade secret key.

To run on sandbox(development mode), set `Alal_PRODUCTION="false"` as an environment variable.

## Example

```python
from alal import (
    CardService,
    CardUserService,
    TransactionService,
    DisputeService
)
import os

os.environ['ALAL_API_KEY'] = 'RCIWTSqXa.........NXCcOEUJJ1R'
os.environ['ALAL_PRODUCTION'] = "false"


# Helpers used just for example

def card_printer(card):
    print(card.balance)
    print(card.last_four)
    print(card.reference)
    print(card.card_brand)
    print(card.card_type)
    print(card.card_user_reference)
    print(card.status)


def card_user_printer(card_user):
    print(card_user.address)
    print(card_user.created_at)
    print(card_user.email)
    print(card_user.first_name)
    print(card_user.last_name)
    print(card_user.id_no)
    print(card_user.phone)
    print(card_user.reference)
    print(card_user.status)


def transaction_printer(transaction):
    print(transaction.amount)
    print(transaction.card_reference)
    print(transaction.created_at)
    print(transaction.kind)
    print(transaction.merchant)
    print(transaction.reference)
    print(transaction.status)
    print(transaction.slug)


def dispute_printer(dispute):
    print(dispute.explanation)
    print(dispute.reason)
    print(dispute.reference)
    print(dispute.kind)
    print(dispute.status)
    print(dispute.transaction_reference)


# Initiate CardService, CardService allow you to interact with cards
card_service = CardService()

# Show Card
card = card_service.show_card("7cf32da1-6ef2-4d96-bd09-0a527541bef4")

card_printer(card)

# Get Access Token
access_data = card_service.get_access_token(
    {'reference': '7cf32da1-6ef2-4d96-bd09-0a527541bef4'})

print(access_data)
print(access_data['access_token'])
print(access_data['embedded_ui'])

# Freeze Card
card = card_service.freeze_card('7cf32da1-6ef2-4d96-bd09-0a527541bef4')
card_printer(card)

# Unfreeze Card
card = card_service.unfreeze_card('7cf32da1-6ef2-4d96-bd09-0a527541bef4')
card_printer(card)

# List Cards
cards = card_service.list_card(page=3, per_page=5)

for card in cards:
    card_printer(card)

# Create Card

card = card_service.create_card({
    'card_brand': 'visa',
    'card_type': 'virtual',
    'card_user_reference': '22d2a86f-39ac-49ab-807a-2e364c59adde'
})

card_printer(card)

# Initiate CardUserService, CardUserService allow you to interact with cardUsers data

card_user_service = CardUserService()

# Show CardUser
card_user = card_user_service.show_card_user(
    'edca6bca-bcf4-4855-a4df-3eb8102cd840')

print(card_user)

# List CardUser

card_users = card_user_service.list_card_user(page=3, per_page=5)

for card_user in card_users:
    card_user_printer(card_user)

# Create CardUser
card_user = card_user_service.create_card_user({
    'address': 'rue 5 argentin',
    'email': 'tuel@mail.com',
    'first_name': 'tuel',
    'last_name': 'tual',
    'id_no': '123981231231232',
    'phone': '778909878',
    'id_image': 'https://paydunya.com/',
    'selfie_image': 'https://paydunya.com/',
    'back_id_image': 'https://paydunya.com/',
})

card_user_printer(card_user)


# Initiate TransactionService, TransactionService allow you to interact with transaction data

transaction_service = TransactionService()

# Show Transaction
transaction = transaction_service.show_transaction(
    '714a2054-4364-4f03-b597-8cb405b4b24a')

transaction_printer(transaction)

# List Transactions
transactions = transaction_service.list_transaction(page=3, per_page=1)

for transaction in transactions:
    transaction_printer(transaction)


# Initiate DisputeService, DisputeService allow you to interact with dispute data
dispute_service = DisputeService()

# List Disputes
disputes = dispute_service.list_dispute(page=1, per_page=1)

for dispute in disputes:
    dispute_printer(dispute)

```

## Contributing

Bug reports and pull requests are welcome on GitHub at [https://github.com/ALAL-Community/alal-python](https://github.com/ALAL-Community/alal-python). This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the code of conduct. Simply create a new branch and raise a Pull Request, we would review and merge.

## License

The package is available as open source under the terms of the [BSD License](https://opensource.org/licenses/BSD-3-Clause)
