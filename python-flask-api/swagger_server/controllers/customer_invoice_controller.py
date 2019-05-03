import connexion
import six

from swagger_server.models.invoice import Invoice  # noqa: E501
from swagger_server import util


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
