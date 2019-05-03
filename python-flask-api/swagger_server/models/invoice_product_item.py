# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.invoice_item_billing_cycle import InvoiceItemBillingCycle  # noqa: F401,E501
from swagger_server import util


class InvoiceProductItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, i_product_item_id: int=None, i_product_id: int=None, v_product_item_name: str=None, v_product_item_description: str=None, f_product_item_basic_amount: float=None, f_product_item_offer_amount: float=None, o_billing_cycle: InvoiceItemBillingCycle=None, b_is_taxable: bool=None, e_product_item_type: str=None, dt_created: datetime=None, dt_updated: datetime=None):  # noqa: E501
        """InvoiceProductItem - a model defined in Swagger

        :param i_product_item_id: The i_product_item_id of this InvoiceProductItem.  # noqa: E501
        :type i_product_item_id: int
        :param i_product_id: The i_product_id of this InvoiceProductItem.  # noqa: E501
        :type i_product_id: int
        :param v_product_item_name: The v_product_item_name of this InvoiceProductItem.  # noqa: E501
        :type v_product_item_name: str
        :param v_product_item_description: The v_product_item_description of this InvoiceProductItem.  # noqa: E501
        :type v_product_item_description: str
        :param f_product_item_basic_amount: The f_product_item_basic_amount of this InvoiceProductItem.  # noqa: E501
        :type f_product_item_basic_amount: float
        :param f_product_item_offer_amount: The f_product_item_offer_amount of this InvoiceProductItem.  # noqa: E501
        :type f_product_item_offer_amount: float
        :param o_billing_cycle: The o_billing_cycle of this InvoiceProductItem.  # noqa: E501
        :type o_billing_cycle: InvoiceItemBillingCycle
        :param b_is_taxable: The b_is_taxable of this InvoiceProductItem.  # noqa: E501
        :type b_is_taxable: bool
        :param e_product_item_type: The e_product_item_type of this InvoiceProductItem.  # noqa: E501
        :type e_product_item_type: str
        :param dt_created: The dt_created of this InvoiceProductItem.  # noqa: E501
        :type dt_created: datetime
        :param dt_updated: The dt_updated of this InvoiceProductItem.  # noqa: E501
        :type dt_updated: datetime
        """
        self.swagger_types = {
            'i_product_item_id': int,
            'i_product_id': int,
            'v_product_item_name': str,
            'v_product_item_description': str,
            'f_product_item_basic_amount': float,
            'f_product_item_offer_amount': float,
            'o_billing_cycle': InvoiceItemBillingCycle,
            'b_is_taxable': bool,
            'e_product_item_type': str,
            'dt_created': datetime,
            'dt_updated': datetime
        }

        self.attribute_map = {
            'i_product_item_id': 'iProductItemId',
            'i_product_id': 'iProductId',
            'v_product_item_name': 'vProductItemName',
            'v_product_item_description': 'vProductItemDescription',
            'f_product_item_basic_amount': 'fProductItemBasicAmount',
            'f_product_item_offer_amount': 'fProductItemOfferAmount',
            'o_billing_cycle': 'oBillingCycle',
            'b_is_taxable': 'bIsTaxable',
            'e_product_item_type': 'eProductItemType',
            'dt_created': 'dtCreated',
            'dt_updated': 'dtUpdated'
        }

        self._i_product_item_id = i_product_item_id
        self._i_product_id = i_product_id
        self._v_product_item_name = v_product_item_name
        self._v_product_item_description = v_product_item_description
        self._f_product_item_basic_amount = f_product_item_basic_amount
        self._f_product_item_offer_amount = f_product_item_offer_amount
        self._o_billing_cycle = o_billing_cycle
        self._b_is_taxable = b_is_taxable
        self._e_product_item_type = e_product_item_type
        self._dt_created = dt_created
        self._dt_updated = dt_updated

    @classmethod
    def from_dict(cls, dikt) -> 'InvoiceProductItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The invoice_product_item of this InvoiceProductItem.  # noqa: E501
        :rtype: InvoiceProductItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def i_product_item_id(self) -> int:
        """Gets the i_product_item_id of this InvoiceProductItem.


        :return: The i_product_item_id of this InvoiceProductItem.
        :rtype: int
        """
        return self._i_product_item_id

    @i_product_item_id.setter
    def i_product_item_id(self, i_product_item_id: int):
        """Sets the i_product_item_id of this InvoiceProductItem.


        :param i_product_item_id: The i_product_item_id of this InvoiceProductItem.
        :type i_product_item_id: int
        """

        self._i_product_item_id = i_product_item_id

    @property
    def i_product_id(self) -> int:
        """Gets the i_product_id of this InvoiceProductItem.


        :return: The i_product_id of this InvoiceProductItem.
        :rtype: int
        """
        return self._i_product_id

    @i_product_id.setter
    def i_product_id(self, i_product_id: int):
        """Sets the i_product_id of this InvoiceProductItem.


        :param i_product_id: The i_product_id of this InvoiceProductItem.
        :type i_product_id: int
        """

        self._i_product_id = i_product_id

    @property
    def v_product_item_name(self) -> str:
        """Gets the v_product_item_name of this InvoiceProductItem.


        :return: The v_product_item_name of this InvoiceProductItem.
        :rtype: str
        """
        return self._v_product_item_name

    @v_product_item_name.setter
    def v_product_item_name(self, v_product_item_name: str):
        """Sets the v_product_item_name of this InvoiceProductItem.


        :param v_product_item_name: The v_product_item_name of this InvoiceProductItem.
        :type v_product_item_name: str
        """

        self._v_product_item_name = v_product_item_name

    @property
    def v_product_item_description(self) -> str:
        """Gets the v_product_item_description of this InvoiceProductItem.


        :return: The v_product_item_description of this InvoiceProductItem.
        :rtype: str
        """
        return self._v_product_item_description

    @v_product_item_description.setter
    def v_product_item_description(self, v_product_item_description: str):
        """Sets the v_product_item_description of this InvoiceProductItem.


        :param v_product_item_description: The v_product_item_description of this InvoiceProductItem.
        :type v_product_item_description: str
        """

        self._v_product_item_description = v_product_item_description

    @property
    def f_product_item_basic_amount(self) -> float:
        """Gets the f_product_item_basic_amount of this InvoiceProductItem.


        :return: The f_product_item_basic_amount of this InvoiceProductItem.
        :rtype: float
        """
        return self._f_product_item_basic_amount

    @f_product_item_basic_amount.setter
    def f_product_item_basic_amount(self, f_product_item_basic_amount: float):
        """Sets the f_product_item_basic_amount of this InvoiceProductItem.


        :param f_product_item_basic_amount: The f_product_item_basic_amount of this InvoiceProductItem.
        :type f_product_item_basic_amount: float
        """

        self._f_product_item_basic_amount = f_product_item_basic_amount

    @property
    def f_product_item_offer_amount(self) -> float:
        """Gets the f_product_item_offer_amount of this InvoiceProductItem.


        :return: The f_product_item_offer_amount of this InvoiceProductItem.
        :rtype: float
        """
        return self._f_product_item_offer_amount

    @f_product_item_offer_amount.setter
    def f_product_item_offer_amount(self, f_product_item_offer_amount: float):
        """Sets the f_product_item_offer_amount of this InvoiceProductItem.


        :param f_product_item_offer_amount: The f_product_item_offer_amount of this InvoiceProductItem.
        :type f_product_item_offer_amount: float
        """

        self._f_product_item_offer_amount = f_product_item_offer_amount

    @property
    def o_billing_cycle(self) -> InvoiceItemBillingCycle:
        """Gets the o_billing_cycle of this InvoiceProductItem.


        :return: The o_billing_cycle of this InvoiceProductItem.
        :rtype: InvoiceItemBillingCycle
        """
        return self._o_billing_cycle

    @o_billing_cycle.setter
    def o_billing_cycle(self, o_billing_cycle: InvoiceItemBillingCycle):
        """Sets the o_billing_cycle of this InvoiceProductItem.


        :param o_billing_cycle: The o_billing_cycle of this InvoiceProductItem.
        :type o_billing_cycle: InvoiceItemBillingCycle
        """

        self._o_billing_cycle = o_billing_cycle

    @property
    def b_is_taxable(self) -> bool:
        """Gets the b_is_taxable of this InvoiceProductItem.


        :return: The b_is_taxable of this InvoiceProductItem.
        :rtype: bool
        """
        return self._b_is_taxable

    @b_is_taxable.setter
    def b_is_taxable(self, b_is_taxable: bool):
        """Sets the b_is_taxable of this InvoiceProductItem.


        :param b_is_taxable: The b_is_taxable of this InvoiceProductItem.
        :type b_is_taxable: bool
        """

        self._b_is_taxable = b_is_taxable

    @property
    def e_product_item_type(self) -> str:
        """Gets the e_product_item_type of this InvoiceProductItem.


        :return: The e_product_item_type of this InvoiceProductItem.
        :rtype: str
        """
        return self._e_product_item_type

    @e_product_item_type.setter
    def e_product_item_type(self, e_product_item_type: str):
        """Sets the e_product_item_type of this InvoiceProductItem.


        :param e_product_item_type: The e_product_item_type of this InvoiceProductItem.
        :type e_product_item_type: str
        """
        allowed_values = ["Goods", "Service"]  # noqa: E501
        if e_product_item_type not in allowed_values:
            raise ValueError(
                "Invalid value for `e_product_item_type` ({0}), must be one of {1}"
                .format(e_product_item_type, allowed_values)
            )

        self._e_product_item_type = e_product_item_type

    @property
    def dt_created(self) -> datetime:
        """Gets the dt_created of this InvoiceProductItem.


        :return: The dt_created of this InvoiceProductItem.
        :rtype: datetime
        """
        return self._dt_created

    @dt_created.setter
    def dt_created(self, dt_created: datetime):
        """Sets the dt_created of this InvoiceProductItem.


        :param dt_created: The dt_created of this InvoiceProductItem.
        :type dt_created: datetime
        """

        self._dt_created = dt_created

    @property
    def dt_updated(self) -> datetime:
        """Gets the dt_updated of this InvoiceProductItem.


        :return: The dt_updated of this InvoiceProductItem.
        :rtype: datetime
        """
        return self._dt_updated

    @dt_updated.setter
    def dt_updated(self, dt_updated: datetime):
        """Sets the dt_updated of this InvoiceProductItem.


        :param dt_updated: The dt_updated of this InvoiceProductItem.
        :type dt_updated: datetime
        """

        self._dt_updated = dt_updated
