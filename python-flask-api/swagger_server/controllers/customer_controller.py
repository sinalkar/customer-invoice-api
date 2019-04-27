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


def customer_login():  # noqa: E501
    """Customer Login to System

     # noqa: E501


    :rtype: str
    """
    return 'do some magic!'


def customer_logout():  # noqa: E501
    """Logs out current logged in customer session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def delete_user(vUsername):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param vUsername: The name that needs to be deleted
    :type vUsername: str

    :rtype: None
    """
    return 'do some magic!'


def get_customer_by_user_name(vUsername):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param vUsername: The name that needs to be fetched. Use user1 for testing.
    :type vUsername: str

    :rtype: Customer
    """
    return 'do some magic!'


def update_customer(vUsername, body):  # noqa: E501
    """Updated user

    This can only be done by the logged in user. # noqa: E501

    :param vUsername: name that need to be updated
    :type vUsername: str
    :param body: Updated customer object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
