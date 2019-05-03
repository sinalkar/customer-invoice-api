# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.invoice import Invoice  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInvoiceController(BaseTestCase):
    """InvoiceController integration test stubs"""

    def test_get_customer_invoice_list(self):
        """Test case for get_customer_invoice_list

        Get Customer invoice list of given customer id
        """
        response = self.client.open(
            '/joinet/customer/1.0.0/customer/{iCustomerId}/invoice'.format(iCustomerId='iCustomerId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
