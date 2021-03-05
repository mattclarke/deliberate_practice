class PointOfSaleError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class UnrecognisedCommand(PointOfSaleError):
    pass


class MalformedCommand(PointOfSaleError):
    pass


class UnknownBarcode(PointOfSaleError):
    pass


class InvalidOperation(PointOfSaleError):
    pass
