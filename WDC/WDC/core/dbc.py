import requests
from typing_extensions import Unpack
from WDC.helper.util.wrappers import network_wrapper
from WDC.helper.error_handling.err import InvalidRequestError
from WDC.helper.util.types import RequestType 
from WDC.helper.util.utils import getRequestParams 


class Dbc:
    params = {}

    def __init__(self, server_url = "https://ows.rasdaman.org/rasdaman/ows", service="WCS", version="2.0.1", request=None):
        """Sets the service endpoint URL based on provided details.

        Args:
            service (str): The Rasdaman service name (e.g., WCS).
            version (str): The Rasdaman service version (e.g., 2.0.1).
            request (str): The Rasdaman request type (e.g., GetCapabilities).
        """
        self.params = {
            "service": service, "version": version, "request": request, "endpoint":server_url
        }

    @network_wrapper
    def post_query(self, query: str):
        """Sends a query request to the WCPS Server

        Args:
            query (str): A WCPS query string

        Returns: on success -> Response content
                on failure -> object containing information of the failed request
        """
        result = requests.post(
            self.params['endpoint'], params=self.params, data={"query": query})
        return result

    @network_wrapper
    def post_request(self, **kwargs: Unpack[RequestType]):
        """Sends a request to the WCPS Server

        Args:
            **kwargs: The key-value pairs of the request parameters

        Form: (lon: 80, lat: 80, ansi: ("2014-01", "2014-12"), coverage: "coverage_name")
            request params must be one of the following: ['GetCapabilities', 'DescribeCoverage', 'GetCoverage']

        Returns: on success -> Response content
                on failure -> object containing information of the failed request
        """
        if self.params.get("request") not in ['GetCapabilities', 'DescribeCoverage', 'GetCoverage']:
            raise InvalidRequestError
        self.endpoint, params = getRequestParams(
            self.endpoint, self.params, kwargs)
        return requests.post(self.endpoint, params=params)
