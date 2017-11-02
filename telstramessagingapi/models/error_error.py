# -*- coding: utf-8 -*-

"""
    telstramessagingapi.models.error_error

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class ErrorError(object):

    """Implementation of the 'Error_Error' model.

    TODO: type model description here.

    Attributes:
        status (string): A short error code
        message (string): Message describing the error.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status" : "status",
        "message" : "message"
    }

    def __init__(self,
                 status=None,
                 message=None):
        """Constructor for the ErrorError class"""

        # Initialize members of the class
        self.status = status
        self.message = message


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        status = dictionary.get("status")
        message = dictionary.get("message")

        # Return an object of this model
        return cls(status,
                   message)

