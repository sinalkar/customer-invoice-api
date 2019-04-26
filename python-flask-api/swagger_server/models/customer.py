# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.customer_billing_address import CustomerBillingAddress  # noqa: F401,E501
from swagger_server.models.customer_category import CustomerCategory  # noqa: F401,E501
from swagger_server.models.customer_shipping_address import CustomerShippingAddress  # noqa: F401,E501
from swagger_server import util


class Customer(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, i_customer_id: int=None, v_first_name: str=None, v_last_name: str=None, e_gender: str=None, e_title: str=None, i_caf_numer: int=None, v_username: str=None, v_password: str=None, v_password_hash: str=None, v_gst_number: str=None, v_mobile_number: str=None, v_email: str=None, o_billing_address: CustomerBillingAddress=None, o_installation_address: CustomerShippingAddress=None, v_category: CustomerCategory=None, dt_created: datetime=None, dt_updated: datetime=None, e_status: str=None):  # noqa: E501
        """Customer - a model defined in Swagger

        :param i_customer_id: The i_customer_id of this Customer.  # noqa: E501
        :type i_customer_id: int
        :param v_first_name: The v_first_name of this Customer.  # noqa: E501
        :type v_first_name: str
        :param v_last_name: The v_last_name of this Customer.  # noqa: E501
        :type v_last_name: str
        :param e_gender: The e_gender of this Customer.  # noqa: E501
        :type e_gender: str
        :param e_title: The e_title of this Customer.  # noqa: E501
        :type e_title: str
        :param i_caf_numer: The i_caf_numer of this Customer.  # noqa: E501
        :type i_caf_numer: int
        :param v_username: The v_username of this Customer.  # noqa: E501
        :type v_username: str
        :param v_password: The v_password of this Customer.  # noqa: E501
        :type v_password: str
        :param v_password_hash: The v_password_hash of this Customer.  # noqa: E501
        :type v_password_hash: str
        :param v_gst_number: The v_gst_number of this Customer.  # noqa: E501
        :type v_gst_number: str
        :param v_mobile_number: The v_mobile_number of this Customer.  # noqa: E501
        :type v_mobile_number: str
        :param v_email: The v_email of this Customer.  # noqa: E501
        :type v_email: str
        :param o_billing_address: The o_billing_address of this Customer.  # noqa: E501
        :type o_billing_address: CustomerBillingAddress
        :param o_installation_address: The o_installation_address of this Customer.  # noqa: E501
        :type o_installation_address: CustomerShippingAddress
        :param v_category: The v_category of this Customer.  # noqa: E501
        :type v_category: CustomerCategory
        :param dt_created: The dt_created of this Customer.  # noqa: E501
        :type dt_created: datetime
        :param dt_updated: The dt_updated of this Customer.  # noqa: E501
        :type dt_updated: datetime
        :param e_status: The e_status of this Customer.  # noqa: E501
        :type e_status: str
        """
        self.swagger_types = {
            'i_customer_id': int,
            'v_first_name': str,
            'v_last_name': str,
            'e_gender': str,
            'e_title': str,
            'i_caf_numer': int,
            'v_username': str,
            'v_password': str,
            'v_password_hash': str,
            'v_gst_number': str,
            'v_mobile_number': str,
            'v_email': str,
            'o_billing_address': CustomerBillingAddress,
            'o_installation_address': CustomerShippingAddress,
            'v_category': CustomerCategory,
            'dt_created': datetime,
            'dt_updated': datetime,
            'e_status': str
        }

        self.attribute_map = {
            'i_customer_id': 'iCustomerId',
            'v_first_name': 'vFirstName',
            'v_last_name': 'vLastName',
            'e_gender': 'eGender',
            'e_title': 'eTitle',
            'i_caf_numer': 'iCAFNumer',
            'v_username': 'vUsername',
            'v_password': 'vPassword',
            'v_password_hash': 'vPasswordHash',
            'v_gst_number': 'vGSTNumber',
            'v_mobile_number': 'vMobileNumber',
            'v_email': 'vEmail',
            'o_billing_address': 'oBillingAddress',
            'o_installation_address': 'oInstallationAddress',
            'v_category': 'vCategory',
            'dt_created': 'dtCreated',
            'dt_updated': 'dtUpdated',
            'e_status': 'eStatus'
        }

        self._i_customer_id = i_customer_id
        self._v_first_name = v_first_name
        self._v_last_name = v_last_name
        self._e_gender = e_gender
        self._e_title = e_title
        self._i_caf_numer = i_caf_numer
        self._v_username = v_username
        self._v_password = v_password
        self._v_password_hash = v_password_hash
        self._v_gst_number = v_gst_number
        self._v_mobile_number = v_mobile_number
        self._v_email = v_email
        self._o_billing_address = o_billing_address
        self._o_installation_address = o_installation_address
        self._v_category = v_category
        self._dt_created = dt_created
        self._dt_updated = dt_updated
        self._e_status = e_status

    @classmethod
    def from_dict(cls, dikt) -> 'Customer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The customer of this Customer.  # noqa: E501
        :rtype: Customer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def i_customer_id(self) -> int:
        """Gets the i_customer_id of this Customer.


        :return: The i_customer_id of this Customer.
        :rtype: int
        """
        return self._i_customer_id

    @i_customer_id.setter
    def i_customer_id(self, i_customer_id: int):
        """Sets the i_customer_id of this Customer.


        :param i_customer_id: The i_customer_id of this Customer.
        :type i_customer_id: int
        """

        self._i_customer_id = i_customer_id

    @property
    def v_first_name(self) -> str:
        """Gets the v_first_name of this Customer.


        :return: The v_first_name of this Customer.
        :rtype: str
        """
        return self._v_first_name

    @v_first_name.setter
    def v_first_name(self, v_first_name: str):
        """Sets the v_first_name of this Customer.


        :param v_first_name: The v_first_name of this Customer.
        :type v_first_name: str
        """
        if v_first_name is None:
            raise ValueError("Invalid value for `v_first_name`, must not be `None`")  # noqa: E501

        self._v_first_name = v_first_name

    @property
    def v_last_name(self) -> str:
        """Gets the v_last_name of this Customer.


        :return: The v_last_name of this Customer.
        :rtype: str
        """
        return self._v_last_name

    @v_last_name.setter
    def v_last_name(self, v_last_name: str):
        """Sets the v_last_name of this Customer.


        :param v_last_name: The v_last_name of this Customer.
        :type v_last_name: str
        """
        if v_last_name is None:
            raise ValueError("Invalid value for `v_last_name`, must not be `None`")  # noqa: E501

        self._v_last_name = v_last_name

    @property
    def e_gender(self) -> str:
        """Gets the e_gender of this Customer.

        Customer gender information  # noqa: E501

        :return: The e_gender of this Customer.
        :rtype: str
        """
        return self._e_gender

    @e_gender.setter
    def e_gender(self, e_gender: str):
        """Sets the e_gender of this Customer.

        Customer gender information  # noqa: E501

        :param e_gender: The e_gender of this Customer.
        :type e_gender: str
        """
        allowed_values = ["Male", "Female"]  # noqa: E501
        if e_gender not in allowed_values:
            raise ValueError(
                "Invalid value for `e_gender` ({0}), must be one of {1}"
                .format(e_gender, allowed_values)
            )

        self._e_gender = e_gender

    @property
    def e_title(self) -> str:
        """Gets the e_title of this Customer.

        Customer title information  # noqa: E501

        :return: The e_title of this Customer.
        :rtype: str
        """
        return self._e_title

    @e_title.setter
    def e_title(self, e_title: str):
        """Sets the e_title of this Customer.

        Customer title information  # noqa: E501

        :param e_title: The e_title of this Customer.
        :type e_title: str
        """
        allowed_values = ["Mr", "Ms", "Mrs", "Miss"]  # noqa: E501
        if e_title not in allowed_values:
            raise ValueError(
                "Invalid value for `e_title` ({0}), must be one of {1}"
                .format(e_title, allowed_values)
            )

        self._e_title = e_title

    @property
    def i_caf_numer(self) -> int:
        """Gets the i_caf_numer of this Customer.


        :return: The i_caf_numer of this Customer.
        :rtype: int
        """
        return self._i_caf_numer

    @i_caf_numer.setter
    def i_caf_numer(self, i_caf_numer: int):
        """Sets the i_caf_numer of this Customer.


        :param i_caf_numer: The i_caf_numer of this Customer.
        :type i_caf_numer: int
        """
        if i_caf_numer is None:
            raise ValueError("Invalid value for `i_caf_numer`, must not be `None`")  # noqa: E501

        self._i_caf_numer = i_caf_numer

    @property
    def v_username(self) -> str:
        """Gets the v_username of this Customer.

        Customer unique Username  # noqa: E501

        :return: The v_username of this Customer.
        :rtype: str
        """
        return self._v_username

    @v_username.setter
    def v_username(self, v_username: str):
        """Sets the v_username of this Customer.

        Customer unique Username  # noqa: E501

        :param v_username: The v_username of this Customer.
        :type v_username: str
        """

        self._v_username = v_username

    @property
    def v_password(self) -> str:
        """Gets the v_password of this Customer.

        Customer encrypted password  # noqa: E501

        :return: The v_password of this Customer.
        :rtype: str
        """
        return self._v_password

    @v_password.setter
    def v_password(self, v_password: str):
        """Sets the v_password of this Customer.

        Customer encrypted password  # noqa: E501

        :param v_password: The v_password of this Customer.
        :type v_password: str
        """

        self._v_password = v_password

    @property
    def v_password_hash(self) -> str:
        """Gets the v_password_hash of this Customer.

        Customer encrypted password  hash or salt  # noqa: E501

        :return: The v_password_hash of this Customer.
        :rtype: str
        """
        return self._v_password_hash

    @v_password_hash.setter
    def v_password_hash(self, v_password_hash: str):
        """Sets the v_password_hash of this Customer.

        Customer encrypted password  hash or salt  # noqa: E501

        :param v_password_hash: The v_password_hash of this Customer.
        :type v_password_hash: str
        """

        self._v_password_hash = v_password_hash

    @property
    def v_gst_number(self) -> str:
        """Gets the v_gst_number of this Customer.

        Customer GST Number  # noqa: E501

        :return: The v_gst_number of this Customer.
        :rtype: str
        """
        return self._v_gst_number

    @v_gst_number.setter
    def v_gst_number(self, v_gst_number: str):
        """Sets the v_gst_number of this Customer.

        Customer GST Number  # noqa: E501

        :param v_gst_number: The v_gst_number of this Customer.
        :type v_gst_number: str
        """

        self._v_gst_number = v_gst_number

    @property
    def v_mobile_number(self) -> str:
        """Gets the v_mobile_number of this Customer.

        Customer mobile Number  # noqa: E501

        :return: The v_mobile_number of this Customer.
        :rtype: str
        """
        return self._v_mobile_number

    @v_mobile_number.setter
    def v_mobile_number(self, v_mobile_number: str):
        """Sets the v_mobile_number of this Customer.

        Customer mobile Number  # noqa: E501

        :param v_mobile_number: The v_mobile_number of this Customer.
        :type v_mobile_number: str
        """

        self._v_mobile_number = v_mobile_number

    @property
    def v_email(self) -> str:
        """Gets the v_email of this Customer.

        Customer email id  # noqa: E501

        :return: The v_email of this Customer.
        :rtype: str
        """
        return self._v_email

    @v_email.setter
    def v_email(self, v_email: str):
        """Sets the v_email of this Customer.

        Customer email id  # noqa: E501

        :param v_email: The v_email of this Customer.
        :type v_email: str
        """

        self._v_email = v_email

    @property
    def o_billing_address(self) -> CustomerBillingAddress:
        """Gets the o_billing_address of this Customer.


        :return: The o_billing_address of this Customer.
        :rtype: CustomerBillingAddress
        """
        return self._o_billing_address

    @o_billing_address.setter
    def o_billing_address(self, o_billing_address: CustomerBillingAddress):
        """Sets the o_billing_address of this Customer.


        :param o_billing_address: The o_billing_address of this Customer.
        :type o_billing_address: CustomerBillingAddress
        """

        self._o_billing_address = o_billing_address

    @property
    def o_installation_address(self) -> CustomerShippingAddress:
        """Gets the o_installation_address of this Customer.


        :return: The o_installation_address of this Customer.
        :rtype: CustomerShippingAddress
        """
        return self._o_installation_address

    @o_installation_address.setter
    def o_installation_address(self, o_installation_address: CustomerShippingAddress):
        """Sets the o_installation_address of this Customer.


        :param o_installation_address: The o_installation_address of this Customer.
        :type o_installation_address: CustomerShippingAddress
        """

        self._o_installation_address = o_installation_address

    @property
    def v_category(self) -> CustomerCategory:
        """Gets the v_category of this Customer.


        :return: The v_category of this Customer.
        :rtype: CustomerCategory
        """
        return self._v_category

    @v_category.setter
    def v_category(self, v_category: CustomerCategory):
        """Sets the v_category of this Customer.


        :param v_category: The v_category of this Customer.
        :type v_category: CustomerCategory
        """

        self._v_category = v_category

    @property
    def dt_created(self) -> datetime:
        """Gets the dt_created of this Customer.


        :return: The dt_created of this Customer.
        :rtype: datetime
        """
        return self._dt_created

    @dt_created.setter
    def dt_created(self, dt_created: datetime):
        """Sets the dt_created of this Customer.


        :param dt_created: The dt_created of this Customer.
        :type dt_created: datetime
        """

        self._dt_created = dt_created

    @property
    def dt_updated(self) -> datetime:
        """Gets the dt_updated of this Customer.


        :return: The dt_updated of this Customer.
        :rtype: datetime
        """
        return self._dt_updated

    @dt_updated.setter
    def dt_updated(self, dt_updated: datetime):
        """Sets the dt_updated of this Customer.


        :param dt_updated: The dt_updated of this Customer.
        :type dt_updated: datetime
        """

        self._dt_updated = dt_updated

    @property
    def e_status(self) -> str:
        """Gets the e_status of this Customer.

        Customer account status  # noqa: E501

        :return: The e_status of this Customer.
        :rtype: str
        """
        return self._e_status

    @e_status.setter
    def e_status(self, e_status: str):
        """Sets the e_status of this Customer.

        Customer account status  # noqa: E501

        :param e_status: The e_status of this Customer.
        :type e_status: str
        """
        allowed_values = ["Active", "Inactive", "Suspended", "Terminated"]  # noqa: E501
        if e_status not in allowed_values:
            raise ValueError(
                "Invalid value for `e_status` ({0}), must be one of {1}"
                .format(e_status, allowed_values)
            )

        self._e_status = e_status
