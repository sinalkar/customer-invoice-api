import connexion
import six

from swagger_server.models.invoice import Invoice  # noqa: E501
from swagger_server import util


def get_customer_invoice_list(iCustomerId):  # noqa: E501
    """Get Customer invoice list of given customer id

    Logged In customer get own invoice list # noqa: E501

    :param iCustomerId: Status values that need to be considered for filter
    :type iCustomerId: List[str]

    :rtype: List[Invoice]
    """
    return 'do some magic!'
