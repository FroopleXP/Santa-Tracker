import time

class ScrollingText:
    
    def __init__(self, text, window_size=13, interval=2):
        self.__text_buff = list(text)
        self.__window_size = window_size
        self.__interval = interval / 1000
        self.__animate = True
        self.__update_last_poll()

        if (len(self.__text_buff) <= self.__window_size):
            self.__animate = False

        if self.__animate:
            for _ in range(0, self.__window_size):
                self.__text_buff.append(" ")

    def __update_last_poll(self):
        self.__last_poll = time.time()

    def __list_to_str(_, l):
        return "".join(l)

    def render(self):
        if self.__animate:
            diff = time.time() - self.__last_poll

            if (diff >= self.__interval):
                self.__text_buff.append(self.__text_buff[0])
                self.__text_buff.pop(0)
                self.__update_last_poll()

            return self.__list_to_str(self.__text_buff[:self.__window_size])

        else:
            return self.__list_to_str(self.__text_buff)
