import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server import util


def create_account(body):  # noqa: E501
    """Create new customer

     # noqa: E501

    :param body: Customer object that needs to be added to the customer table
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(iCustomerId):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param iCustomerId: The name that needs to be deleted
    :type iCustomerId: str

    :rtype: None
    """
    return 'do some magic!'


def get_customer_by_id(iCustomerId):  # noqa: E501
    """Get customer profile information by given Customer id

     # noqa: E501

    :param iCustomerId: Customer Id needed to fetch all profile related information of given customer
    :type iCustomerId: str

    :rtype: Customer
    """
    return 'do some magic!'


def update_customer(iCustomerId, body):  # noqa: E501
    """Updated user

    This can only be done by the logged in user. # noqa: E501

    :param iCustomerId: name that need to be updated
    :type iCustomerId: str
    :param body: Updated customer object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
