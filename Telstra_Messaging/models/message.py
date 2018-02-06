# coding: utf-8

"""
    Telstra Messaging API

     The Telstra SMS Messaging API allows your applications to send and receive SMS text messages from Australia's leading network operator.  It also allows your application to track the delivery status of both sent and received SMS messages.   # noqa: E501

    OpenAPI spec version: 2.2.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Message(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'to': 'str',
        'delivery_status': 'str',
        'message_id': 'str',
        'message_status_url': 'str'
    }

    attribute_map = {
        'to': 'to',
        'delivery_status': 'deliveryStatus',
        'message_id': 'messageId',
        'message_status_url': 'messageStatusURL'
    }

    def __init__(self, to=None, delivery_status=None, message_id=None, message_status_url=None):  # noqa: E501
        """Message - a model defined in Swagger"""  # noqa: E501

        self._to = None
        self._delivery_status = None
        self._message_id = None
        self._message_status_url = None
        self.discriminator = None

        self.to = to
        self.delivery_status = delivery_status
        self.message_id = message_id
        self.message_status_url = message_status_url

    @property
    def to(self):
        """Gets the to of this Message.  # noqa: E501

          # noqa: E501

        :return: The to of this Message.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Message.

          # noqa: E501

        :param to: The to of this Message.  # noqa: E501
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def delivery_status(self):
        """Gets the delivery_status of this Message.  # noqa: E501

          # noqa: E501

        :return: The delivery_status of this Message.  # noqa: E501
        :rtype: str
        """
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, delivery_status):
        """Sets the delivery_status of this Message.

          # noqa: E501

        :param delivery_status: The delivery_status of this Message.  # noqa: E501
        :type: str
        """
        if delivery_status is None:
            raise ValueError("Invalid value for `delivery_status`, must not be `None`")  # noqa: E501

        self._delivery_status = delivery_status

    @property
    def message_id(self):
        """Gets the message_id of this Message.  # noqa: E501

          # noqa: E501

        :return: The message_id of this Message.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this Message.

          # noqa: E501

        :param message_id: The message_id of this Message.  # noqa: E501
        :type: str
        """
        if message_id is None:
            raise ValueError("Invalid value for `message_id`, must not be `None`")  # noqa: E501

        self._message_id = message_id

    @property
    def message_status_url(self):
        """Gets the message_status_url of this Message.  # noqa: E501

          # noqa: E501

        :return: The message_status_url of this Message.  # noqa: E501
        :rtype: str
        """
        return self._message_status_url

    @message_status_url.setter
    def message_status_url(self, message_status_url):
        """Sets the message_status_url of this Message.

          # noqa: E501

        :param message_status_url: The message_status_url of this Message.  # noqa: E501
        :type: str
        """
        if message_status_url is None:
            raise ValueError("Invalid value for `message_status_url`, must not be `None`")  # noqa: E501

        self._message_status_url = message_status_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other