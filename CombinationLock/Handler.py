from abc import ABC, abstractmethod


class Handler:
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, password):
        if self._next_handler:
            return self._next_handler.handle(password)

        return None
