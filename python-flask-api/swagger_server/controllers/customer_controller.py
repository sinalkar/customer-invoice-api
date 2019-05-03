import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server.models.invoice import Invoice  # noqa: E501
from swagger_server.models.invoice_product import InvoiceProduct  # noqa: E501
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


def get_customer_by_id(iCustomerId):  # noqa: E501
    """Get customer profile information by given Customer id

     # noqa: E501

    :param iCustomerId: Customer Id needed to fetch all profile related information of given customer
    :type iCustomerId: str

    :rtype: Customer
    """
    return 'do some magic!'


def get_customer_invoice_by_id(iCustomerId, iInvoiceId):  # noqa: E501
    """Get Customer invoice detail of given customer id

    Logged In customer get own invoice list # noqa: E501

    :param iCustomerId: Customer Id of logged In user
    :type iCustomerId: str
    :param iInvoiceId: Invoice id to be fetch from 
    :type iInvoiceId: str

    :rtype: object
    """
    return 'do some magic!'


def get_customer_invoice_list(iCustomerId):  # noqa: E501
    """Get Customer invoice list of given customer id

    Logged In customer get own invoice list # noqa: E501

    :param iCustomerId: Customer Id needed to fetch all profile related information of given customer
    :type iCustomerId: str

    :rtype: List[Invoice]
    """
    return 'do some magic!'


def get_customer_product_detail_by_product_id(iProductId, iCustomerId):  # noqa: E501
    """Get product detail for logged in customer

    Logged In customer get product details by ProductId of related regional  # noqa: E501

    :param iProductId: iProductId Id of logged In user
    :type iProductId: str
    :param iCustomerId: iProductId Id of logged In user
    :type iCustomerId: str

    :rtype: object
    """
    return 'do some magic!'


def get_customers_product_list(iCustomerId):  # noqa: E501
    """Get product list for logged in customer

    Logged In customer get product list of related region # noqa: E501

    :param iCustomerId: Customer Id of logged In user
    :type iCustomerId: str

    :rtype: List[InvoiceProduct]
    """
    return 'do some magic!'


def update_customer_by_id(iCustomerId, body):  # noqa: E501
    """Update customer profile details

    Update customer profile details # noqa: E501

    :param iCustomerId: name that need to be updated
    :type iCustomerId: str
    :param body: Updated customer object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
