# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCustomerController(BaseTestCase):
    """CustomerController integration test stubs"""

    def test_create_customer(self):
        """Test case for create_customer

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

    def test_customer_login(self):
        """Test case for customer_login

        Customer Login to System
        """
        response = self.client.open(
            '/joinet/customer/1.0.0/customer/login',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_customer_logout(self):
        """Test case for customer_logout

        Logs out current logged in customer session
        """
        response = self.client.open(
            '/joinet/customer/1.0.0/customer/logout',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        Delete user
        """
        response = self.client.open(
            '/joinet/customer/1.0.0/customer/{vUsername}'.format(vUsername='vUsername_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_customer_by_user_name(self):
        """Test case for get_customer_by_user_name

        Get user by user name
        """
        response = self.client.open(
            '/joinet/customer/1.0.0/customer/{vUsername}'.format(vUsername='vUsername_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_customer(self):
        """Test case for update_customer

        Updated user
        """
        body = Customer()
        response = self.client.open(
            '/joinet/customer/1.0.0/customer/{vUsername}'.format(vUsername='vUsername_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
