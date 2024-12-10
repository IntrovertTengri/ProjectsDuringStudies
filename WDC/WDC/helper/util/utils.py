from typing_extensions import Unpack

from .types import RequestType
from WDC.helper.error_handling.err import InvalidRequestError


def remove_singles(param: str):
    return param.replace("'", "")


def getSubSets(kwargs: Unpack[RequestType]):
    """Extracts the subsetting parameters from the request"""
    subsets = []
    for key, value in kwargs.items():
        match key:
            case "Lat" | "Lon":
                if type(value) is tuple:
                    subsets.append(f"{key}({value[0]}, {value[1]})")
                else:
                    subsets.append(f"{key}({value})")
            case "ansi":
                if type(value) is tuple:
                    subsets.append(f'ansi("{value[0]}":"{value[1]}")')
                else:
                    subsets.append(f'ansi("{value}")')

    return subsets


def getRequestParams(endpoint: str, currentParams: dict, kwargs: Unpack[RequestType]) -> tuple[str, dict]:
    match currentParams.get("request"):
        case 'GetCapabilities':
            params = {**currentParams}
        case 'DescribeCoverage':
            coverageId = kwargs.get("coverageId")
            if coverageId is None:
                raise InvalidRequestError(
                    "Missing coverageId parameter for DescribeCoverage")
            params = {**currentParams, "coverageId": coverageId}
        case 'GetCoverage':
            coverageId = kwargs.get("coverageId")
            if coverageId is None:
                raise InvalidRequestError(
                    "Missing coverageId parameter for GetCoverage")
            subsets = getSubSets(kwargs)
            if len(subsets):
                endpoint = endpoint + \
                    f"?subset={'&subset='.join(subsets)}"
            params = {**currentParams, "coverageId": coverageId}
    return endpoint, params


def concat_coverage_names(list_of_coverages: list):
    """
    Concatenates a list of coverage names into a single string separated by commas.

    Args:
        list_of_coverages (list of str): A list containing coverage names.

    Returns:
        str: A single string consisting of all coverage names separated by commas.
    """
    return ", ".join(list_of_coverages)
