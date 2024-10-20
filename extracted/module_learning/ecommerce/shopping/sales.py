# absolute import statment prefered by pep8
from ecommerce.customer import contact
# related import statment
from ..customer import contact


contact.contact_customer()


def calc_tax():
    pass


def calc_shipping():
    pass


if __name__ == '__main__':
    print('sales started')
    calc_tax()
