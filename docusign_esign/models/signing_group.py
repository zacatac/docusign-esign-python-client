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

from docusign_esign.client.configuration import Configuration


class SigningGroup(object):
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
        'created': 'str',
        'created_by': 'str',
        'error_details': 'ErrorDetails',
        'group_email': 'str',
        'group_name': 'str',
        'group_type': 'str',
        'modified': 'str',
        'modified_by': 'str',
        'signing_group_id': 'str',
        'users': 'list[SigningGroupUser]'
    }

    attribute_map = {
        'created': 'created',
        'created_by': 'createdBy',
        'error_details': 'errorDetails',
        'group_email': 'groupEmail',
        'group_name': 'groupName',
        'group_type': 'groupType',
        'modified': 'modified',
        'modified_by': 'modifiedBy',
        'signing_group_id': 'signingGroupId',
        'users': 'users'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """SigningGroup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._created_by = None
        self._error_details = None
        self._group_email = None
        self._group_name = None
        self._group_type = None
        self._modified = None
        self._modified_by = None
        self._signing_group_id = None
        self._users = None
        self.discriminator = None

        setattr(self, "_{}".format('created'), kwargs.get('created', None))
        setattr(self, "_{}".format('created_by'), kwargs.get('created_by', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('group_email'), kwargs.get('group_email', None))
        setattr(self, "_{}".format('group_name'), kwargs.get('group_name', None))
        setattr(self, "_{}".format('group_type'), kwargs.get('group_type', None))
        setattr(self, "_{}".format('modified'), kwargs.get('modified', None))
        setattr(self, "_{}".format('modified_by'), kwargs.get('modified_by', None))
        setattr(self, "_{}".format('signing_group_id'), kwargs.get('signing_group_id', None))
        setattr(self, "_{}".format('users'), kwargs.get('users', None))

    @property
    def created(self):
        """Gets the created of this SigningGroup.  # noqa: E501

          # noqa: E501

        :return: The created of this SigningGroup.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SigningGroup.

          # noqa: E501

        :param created: The created of this SigningGroup.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this SigningGroup.  # noqa: E501

          # noqa: E501

        :return: The created_by of this SigningGroup.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this SigningGroup.

          # noqa: E501

        :param created_by: The created_by of this SigningGroup.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def error_details(self):
        """Gets the error_details of this SigningGroup.  # noqa: E501

        This object describes errors that occur. It is only valid for responses and ignored in requests.  # noqa: E501

        :return: The error_details of this SigningGroup.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this SigningGroup.

        This object describes errors that occur. It is only valid for responses and ignored in requests.  # noqa: E501

        :param error_details: The error_details of this SigningGroup.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def group_email(self):
        """Gets the group_email of this SigningGroup.  # noqa: E501

          # noqa: E501

        :return: The group_email of this SigningGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_email

    @group_email.setter
    def group_email(self, group_email):
        """Sets the group_email of this SigningGroup.

          # noqa: E501

        :param group_email: The group_email of this SigningGroup.  # noqa: E501
        :type: str
        """

        self._group_email = group_email

    @property
    def group_name(self):
        """Gets the group_name of this SigningGroup.  # noqa: E501

        The name of the group.  # noqa: E501

        :return: The group_name of this SigningGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this SigningGroup.

        The name of the group.  # noqa: E501

        :param group_name: The group_name of this SigningGroup.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def group_type(self):
        """Gets the group_type of this SigningGroup.  # noqa: E501

          # noqa: E501

        :return: The group_type of this SigningGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this SigningGroup.

          # noqa: E501

        :param group_type: The group_type of this SigningGroup.  # noqa: E501
        :type: str
        """

        self._group_type = group_type

    @property
    def modified(self):
        """Gets the modified of this SigningGroup.  # noqa: E501

          # noqa: E501

        :return: The modified of this SigningGroup.  # noqa: E501
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this SigningGroup.

          # noqa: E501

        :param modified: The modified of this SigningGroup.  # noqa: E501
        :type: str
        """

        self._modified = modified

    @property
    def modified_by(self):
        """Gets the modified_by of this SigningGroup.  # noqa: E501

          # noqa: E501

        :return: The modified_by of this SigningGroup.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this SigningGroup.

          # noqa: E501

        :param modified_by: The modified_by of this SigningGroup.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def signing_group_id(self):
        """Gets the signing_group_id of this SigningGroup.  # noqa: E501

        When set to **true** and the feature is enabled in the sender's account, the signing recipient is required to draw signatures and initials at each signature/initial tab ( instead of adopting a signature/initial style or only drawing a signature/initial once).  # noqa: E501

        :return: The signing_group_id of this SigningGroup.  # noqa: E501
        :rtype: str
        """
        return self._signing_group_id

    @signing_group_id.setter
    def signing_group_id(self, signing_group_id):
        """Sets the signing_group_id of this SigningGroup.

        When set to **true** and the feature is enabled in the sender's account, the signing recipient is required to draw signatures and initials at each signature/initial tab ( instead of adopting a signature/initial style or only drawing a signature/initial once).  # noqa: E501

        :param signing_group_id: The signing_group_id of this SigningGroup.  # noqa: E501
        :type: str
        """

        self._signing_group_id = signing_group_id

    @property
    def users(self):
        """Gets the users of this SigningGroup.  # noqa: E501

          # noqa: E501

        :return: The users of this SigningGroup.  # noqa: E501
        :rtype: list[SigningGroupUser]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this SigningGroup.

          # noqa: E501

        :param users: The users of this SigningGroup.  # noqa: E501
        :type: list[SigningGroupUser]
        """

        self._users = users

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
        if issubclass(SigningGroup, dict):
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
        if not isinstance(other, SigningGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SigningGroup):
            return True

        return self.to_dict() != other.to_dict()
