# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.invoice_product import InvoiceProduct  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCustomerProductController(BaseTestCase):
    """CustomerProductController integration test stubs"""

    def test_get_customers_product_list(self):
        """Test case for get_customers_product_list

        Get product list for logged in customer
        """
        response = self.client.open(
            '/joinet/customer/1.0.0/customer/{iCustomerId}/product'.format(iCustomerId='iCustomerId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
