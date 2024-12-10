import xml.etree.ElementTree as ET
import requests
from typing import Callable
import xml.etree.ElementTree as ET


def network_wrapper(postRequest: Callable[[str, dict, dict], requests.models.Response]):
    def wrapper(*args, **kwargs):
        try:
            response = postRequest(*args, **kwargs)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": {
                    "code": response.status_code,
                    "message": "Request Failed",
                    "exceptionDetail": "Request Timeout Error"
                }
            }
        except requests.exceptions.HTTPError as e:
            root = ET.fromstring(response.text)
            exceptionDetail = {}
            for child in root:
                for subChild in child:
                    exceptionDetail["exceptionText"] = subChild.text
                if child.attrib.get("exceptionCode"):
                    exceptionDetail["exceptionCode"] = child.attrib.get(
                        "exceptionCode")
            return {
                "success": False,
                "error": {
                    "code": response.status_code,
                    "message": "Request Failed",
                    "exceptionDetail": exceptionDetail,
                    "extra": e
                }
            }
        else:
            return response.content
    return wrapper
