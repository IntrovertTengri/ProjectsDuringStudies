from typing_extensions import NotRequired, TypedDict, Union


class RequestType(TypedDict):
    """Type representing the request type to the server"""
    coverageId: NotRequired[str]
    Lat: NotRequired[Union[float, tuple[int | float, int | float]]]
    Lon: NotRequired[Union[float, tuple[int | float, int | float]]]
    ansi: NotRequired[Union[str, tuple[str, str]]]
    format: NotRequired[str]
