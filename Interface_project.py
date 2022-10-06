from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def show_entering_message(self):
        pass


class Show(Interface):
    """Interface for getting values input of user."""
    def show_entering_message(self):
        messsage = input('Entering message >>> ').strip()
        return messsage


if __name__ == '__main__':
    interface = Show()

    print('Enter command: ')
    messsage = interface.show_entering_message()
    print(messsage)