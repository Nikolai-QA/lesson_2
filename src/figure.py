from abc import ABC, abstractmethod



class Figure(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise TypeError('The object is not a figure!')
        return self.area + figure.area