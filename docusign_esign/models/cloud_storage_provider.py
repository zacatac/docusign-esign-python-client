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


class CloudStorageProvider(object):
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
        'authentication_url': 'str',
        'error_details': 'ErrorDetails',
        'redirect_url': 'str',
        'service': 'str',
        'service_id': 'str'
    }

    attribute_map = {
        'authentication_url': 'authenticationUrl',
        'error_details': 'errorDetails',
        'redirect_url': 'redirectUrl',
        'service': 'service',
        'service_id': 'serviceId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """CloudStorageProvider - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._authentication_url = None
        self._error_details = None
        self._redirect_url = None
        self._service = None
        self._service_id = None
        self.discriminator = None

        setattr(self, "_{}".format('authentication_url'), kwargs.get('authentication_url', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('redirect_url'), kwargs.get('redirect_url', None))
        setattr(self, "_{}".format('service'), kwargs.get('service', None))
        setattr(self, "_{}".format('service_id'), kwargs.get('service_id', None))

    @property
    def authentication_url(self):
        """Gets the authentication_url of this CloudStorageProvider.  # noqa: E501

        The authentication URL used for the cloud storage provider. This information is only included in the response if the user has not passed authentication for the cloud storage provider. If the redirectUrl query string is provided, the returnUrl is appended to the authenticationUrl.   # noqa: E501

        :return: The authentication_url of this CloudStorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._authentication_url

    @authentication_url.setter
    def authentication_url(self, authentication_url):
        """Sets the authentication_url of this CloudStorageProvider.

        The authentication URL used for the cloud storage provider. This information is only included in the response if the user has not passed authentication for the cloud storage provider. If the redirectUrl query string is provided, the returnUrl is appended to the authenticationUrl.   # noqa: E501

        :param authentication_url: The authentication_url of this CloudStorageProvider.  # noqa: E501
        :type: str
        """

        self._authentication_url = authentication_url

    @property
    def error_details(self):
        """Gets the error_details of this CloudStorageProvider.  # noqa: E501

        This object describes errors that occur. It is only valid for responses and ignored in requests.  # noqa: E501

        :return: The error_details of this CloudStorageProvider.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this CloudStorageProvider.

        This object describes errors that occur. It is only valid for responses and ignored in requests.  # noqa: E501

        :param error_details: The error_details of this CloudStorageProvider.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def redirect_url(self):
        """Gets the redirect_url of this CloudStorageProvider.  # noqa: E501

        The URL the user is redirected to after the cloud storage provider authenticates the user. Using this will append the redirectUrl to the authenticationUrl.  The redirectUrl is restricted to URLs in the docusign.com or docusign.net domains.  # noqa: E501

        :return: The redirect_url of this CloudStorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this CloudStorageProvider.

        The URL the user is redirected to after the cloud storage provider authenticates the user. Using this will append the redirectUrl to the authenticationUrl.  The redirectUrl is restricted to URLs in the docusign.com or docusign.net domains.  # noqa: E501

        :param redirect_url: The redirect_url of this CloudStorageProvider.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def service(self):
        """Gets the service of this CloudStorageProvider.  # noqa: E501

        The service name for the cloud storage provider.  # noqa: E501

        :return: The service of this CloudStorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this CloudStorageProvider.

        The service name for the cloud storage provider.  # noqa: E501

        :param service: The service of this CloudStorageProvider.  # noqa: E501
        :type: str
        """

        self._service = service

    @property
    def service_id(self):
        """Gets the service_id of this CloudStorageProvider.  # noqa: E501

        The DocuSign generated ID for the cloud storage provider  # noqa: E501

        :return: The service_id of this CloudStorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this CloudStorageProvider.

        The DocuSign generated ID for the cloud storage provider  # noqa: E501

        :param service_id: The service_id of this CloudStorageProvider.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

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
        if issubclass(CloudStorageProvider, dict):
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
        if not isinstance(other, CloudStorageProvider):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudStorageProvider):
            return True

        return self.to_dict() != other.to_dict()
