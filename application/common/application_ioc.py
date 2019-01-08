import abc


class IApplicationIOC:
    """
    Inversion of Control (i.e. Dependency Injection) interface for the Repertoire App
    """
    @classmethod
    @abc.abstractmethod
    def get_logger(self):
        """
        Get the logger
        :return:
        """
        raise NotImplementedError()


class ApplicationIOC(IApplicationIOC):

    def __init__(self):
        import logging
        self._logger = logging

    def get_logger(self):
        return self._logger

