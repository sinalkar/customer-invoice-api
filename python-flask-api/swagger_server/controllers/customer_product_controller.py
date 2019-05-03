import connexion
import six

from swagger_server.models.invoice_product import InvoiceProduct  # noqa: E501
from swagger_server import util


def get_customers_product_list(iCustomerId):  # noqa: E501
    """Get product list for logged in customer

    Logged In customer get product list of related region # noqa: E501

    :param iCustomerId: Customer Id of logged In user
    :type iCustomerId: str

    :rtype: List[InvoiceProduct]
    """
    return 'do some magic!'
