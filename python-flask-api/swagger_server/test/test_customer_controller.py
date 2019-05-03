# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCustomerController(BaseTestCase):
    """CustomerController integration test stubs"""

    def test_create_account(self):
        """Test case for create_account

        Create new customer
        """
        body = Customer()
        response = self.client.open(
            '/joinet/customer/1.0.0/customer',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_customer_by_id(self):
        """Test case for get_customer_by_id

        Get customer profile information by given Customer id
        """
        response = self.client.open(
            '/joinet/customer/1.0.0/customer/{iCustomerId}/profile'.format(iCustomerId='iCustomerId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_customer_by_id(self):
        """Test case for update_customer_by_id

        Update customer profile details
        """
        body = Customer()
        response = self.client.open(
            '/joinet/customer/1.0.0/customer/{iCustomerId}/profile'.format(iCustomerId='iCustomerId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
