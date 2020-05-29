import threading
from .ac_settings import acSettings, priority
# from .room_info import RoomInfo


class ServiceList:
    service_list = []
    mutex = threading.Lock()

    def __str__(self):
        s = '['
        for room in self.service_list:
            s += '(' + str(room.room_id) + ',' + str(room.ac_status) + ',' + str(room.online_time) + ')' + ' '
        s += ']'
        return s

    def append(self, room):
        self.mutex.acquire()
        room.set(online_time=0)
        self.service_list.append(room)
        self.service_list = sorted(self.service_list, key=lambda x: (priority[x.ac_status], -x.online_time))
        self.mutex.release()

    def look_up(self, room_id):
        for room in self.service_list:
            if room.room_id == room_id:
                return True
        return False

    def get_lowest_room(self):
        return self.service_list[0]

    def remove(self, room_id):
        self.mutex.acquire()
        for room in self.service_list:
            if room.room_id == room_id:
                self.service_list.remove(room)
                self.mutex.release()
                return
        self.mutex.release()

    def length(self):
        return len(self.service_list)


serviceList = ServiceList()
