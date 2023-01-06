import strawberry
from clientLib import Atm
from decimal import Decimal

host = "localhost"
port = 5672


@strawberry.type
class AtmAccount:
    balance: Decimal


@strawberry.type
class AtmMutation:
    amountChanged: Decimal


def get_account(token: str) -> AtmAccount:
    atm = Atm(host, port)
    response = atm.balance(token)
    if response == "False" or response == "Invalid message":
        return AtmAccount(balance=Decimal(0))
    return AtmAccount(balance=Decimal(response))


def get_token(username: str, pin: str) -> str:
    atm = Atm(host, port)
    response = atm.auth(username, pin)
    if response == "False" or response == "Invalid message":
        return ""
    return response


@strawberry.type
class Query:
    token: str = strawberry.field(resolver=get_token)
    account: AtmAccount = strawberry.field(resolver=get_account)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def withdraw(self, token: str, amount: Decimal) -> AtmMutation:
        if amount <= 0:
            return AtmMutation(amountChanged=Decimal(0))
        atm = Atm(host, port)
        response = atm.withdraw(token, amount)
        if response == "False" or response == "Invalid message":
            return AtmMutation(amountChanged=Decimal(0))
        return AtmMutation(amountChanged=Decimal(response))

    @strawberry.mutation
    def deposit(self, token: str, amount: Decimal) -> AtmMutation:
        if amount <= 0:
            return AtmMutation(amountChanged=Decimal(0))
        atm = Atm(host, port)
        response = atm.deposit(token, amount)
        if response == "False" or response == "Invalid message":
            return AtmMutation(amountChanged=Decimal(0))
        return AtmMutation(amountChanged=Decimal(response))


schema = strawberry.Schema(query=Query, mutation=Mutation)
