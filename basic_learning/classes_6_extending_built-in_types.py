class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, item):
        print('Append called')
        super().append(item)


list1 = TrackableList()
list1.append('1')
