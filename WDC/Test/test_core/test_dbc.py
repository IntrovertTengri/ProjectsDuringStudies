import unittest
from unittest.mock import MagicMock, patch
from WDC.helper.util.wrappers import network_wrapper
import requests


class TestDbc(unittest.TestCase):
    @patch("requests.post")
    def test_success_network_wrapper(self, mock_request):
        # Mocking successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"Successful response"
        mock_request.return_value = mock_response

        # call request.post with endpoint to see results of wrapper function
        def testNetworkCall(): return requests.post(
            "https://ows.rasdaman.org/rasdaman/ows")
        # result of the wrapper function will be another function that we have to call
        wrapper = network_wrapper(testNetworkCall)
        # assert that result of the called wrapper function the correct content
        networkCallResult = wrapper()
        self.assertEqual(networkCallResult, b"Successful response")

    @patch("requests.post")
    def test_timeout_network_wrapper(self, mock_request):
        # Mocking unsuccessful response (timeout)
        mock_response = MagicMock()
        mock_response.status_code = 408
        mock_response.raise_for_status.side_effect = requests.exceptions.Timeout
        mock_request.return_value = mock_response

        # call request.post with endpoint to see results of wrapper function
        def testNetworkCall(): return requests.post(
            "https://ows.rasdaman.org/rasdaman/ows")
        # result of the wrapper function will be another function that we have to call
        wrapper = network_wrapper(testNetworkCall)
        # assert that result of the called wrapper function is the correct dictionary response
        networkCallResult = wrapper()
        self.assertDictEqual(networkCallResult, {
            "success": False,
            "error": {
                "code": 408,
                "message": "Request Failed",
                "exceptionDetail": "Request Timeout Error"
            }
        })

    @patch('requests.post')
    def test_request_exception_network_wrapper(self, mock_request):
        # get httperor instance
        mockedHTTPError = requests.HTTPError()
        # Mocking unsuccessful response (HTTPError) and also include xml to parse
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.raise_for_status.side_effect = mockedHTTPError
        mock_response.text = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<ows:ExceptionReport version="2.0.1"\n    xsi:schemaLocation="http://www.opengis.net/ows/2.0 http://schemas.opengis.net/ows/2.0/owsExceptionReport.xsd"\n    xmlns:ows="http://www.opengis.net/ows/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink">\n    <ows:Exception exceptionCode="InvalidRequest" >\n        <ows:ExceptionText>Coverage result must use encode() as it is non-scalar value.</ows:ExceptionText>\n    </ows:Exception>\n</ows:ExceptionReport>\n'''
        mock_request.return_value = mock_response

        # call request.post with endpoint to see results of wrapper function
        def testNetworkCall(): return requests.post(
            "https://ows.rasdaman.org/rasdaman/ows")
        # result of the wrapper function will be another function that we have to call
        wrapper = network_wrapper(testNetworkCall)
        # assert that result of the called wrapper function is the correct dictionary response
        networkCallResult = wrapper()
        self.assertDictEqual(networkCallResult, {
            "success": False,
            "error": {
                "code": 400,
                "message": "Request Failed",
                "exceptionDetail": {'exceptionText': 'Coverage result must use encode() as it is non-scalar value.', 'exceptionCode': 'InvalidRequest'},
                'extra': mockedHTTPError
            }
        })
