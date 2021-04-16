class PointOfSaleError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class MalformedCommand(PointOfSaleError):
    pass


class UnknownBarcode(PointOfSaleError):
    pass


class InvalidOperation(PointOfSaleError):
    pass
