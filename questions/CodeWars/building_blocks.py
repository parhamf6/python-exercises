# https://www.codewars.com/kata/55b75fcf67e558d3750000a3/python
class Block:

    def __init__(self, dimensions):
        self._width, self._length, self._height = dimensions

    def get_width(self):
        return self._width

    def get_length(self):
        return self._length

    def get_height(self):
        return self._height

    def get_volume(self):
        return self._height * self._length * self._width

    def get_surface_area(self):
        return 2 * (self._width*self._length + self._width*self._height + self._length*self._height)