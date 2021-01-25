# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Revision(object):
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
        'end_data': 'str',
        'field_name': 'str',
        'max_signature_length': 'str',
        'signature_properties': 'SignatureProperties',
        'signature_type': 'str',
        'start_data': 'str'
    }

    attribute_map = {
        'end_data': 'endData',
        'field_name': 'fieldName',
        'max_signature_length': 'maxSignatureLength',
        'signature_properties': 'signatureProperties',
        'signature_type': 'signatureType',
        'start_data': 'startData'
    }

    def __init__(self, end_data=None, field_name=None, max_signature_length=None, signature_properties=None, signature_type=None, start_data=None):  # noqa: E501
        """Revision - a model defined in Swagger"""  # noqa: E501

        self._end_data = None
        self._field_name = None
        self._max_signature_length = None
        self._signature_properties = None
        self._signature_type = None
        self._start_data = None
        self.discriminator = None

        if end_data is not None:
            self.end_data = end_data
        if field_name is not None:
            self.field_name = field_name
        if max_signature_length is not None:
            self.max_signature_length = max_signature_length
        if signature_properties is not None:
            self.signature_properties = signature_properties
        if signature_type is not None:
            self.signature_type = signature_type
        if start_data is not None:
            self.start_data = start_data

    @property
    def end_data(self):
        """Gets the end_data of this Revision.  # noqa: E501

          # noqa: E501

        :return: The end_data of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._end_data

    @end_data.setter
    def end_data(self, end_data):
        """Sets the end_data of this Revision.

          # noqa: E501

        :param end_data: The end_data of this Revision.  # noqa: E501
        :type: str
        """

        self._end_data = end_data

    @property
    def field_name(self):
        """Gets the field_name of this Revision.  # noqa: E501

          # noqa: E501

        :return: The field_name of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this Revision.

          # noqa: E501

        :param field_name: The field_name of this Revision.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

    @property
    def max_signature_length(self):
        """Gets the max_signature_length of this Revision.  # noqa: E501

          # noqa: E501

        :return: The max_signature_length of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._max_signature_length

    @max_signature_length.setter
    def max_signature_length(self, max_signature_length):
        """Sets the max_signature_length of this Revision.

          # noqa: E501

        :param max_signature_length: The max_signature_length of this Revision.  # noqa: E501
        :type: str
        """

        self._max_signature_length = max_signature_length

    @property
    def signature_properties(self):
        """Gets the signature_properties of this Revision.  # noqa: E501


        :return: The signature_properties of this Revision.  # noqa: E501
        :rtype: SignatureProperties
        """
        return self._signature_properties

    @signature_properties.setter
    def signature_properties(self, signature_properties):
        """Sets the signature_properties of this Revision.


        :param signature_properties: The signature_properties of this Revision.  # noqa: E501
        :type: SignatureProperties
        """

        self._signature_properties = signature_properties

    @property
    def signature_type(self):
        """Gets the signature_type of this Revision.  # noqa: E501

          # noqa: E501

        :return: The signature_type of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        """Sets the signature_type of this Revision.

          # noqa: E501

        :param signature_type: The signature_type of this Revision.  # noqa: E501
        :type: str
        """

        self._signature_type = signature_type

    @property
    def start_data(self):
        """Gets the start_data of this Revision.  # noqa: E501

          # noqa: E501

        :return: The start_data of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._start_data

    @start_data.setter
    def start_data(self, start_data):
        """Sets the start_data of this Revision.

          # noqa: E501

        :param start_data: The start_data of this Revision.  # noqa: E501
        :type: str
        """

        self._start_data = start_data

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
        if issubclass(Revision, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Revision):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
