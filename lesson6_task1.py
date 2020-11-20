from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 4:
            if i == 0:
                print(f"\033[31m{'Светофор переключается на Красный'}")
                sleep(7)
            elif i == 1:
                print(f"\033[33m{'Светофор переключается на Желтый'}")
                sleep(2)
            elif i == 2:
                print(f"\033[32m{'Светофор переключается на Зеленый'}")
                sleep(7)
            elif i == 3:
                print(f"\033[33m{'Светофор переключается на Желтый'}")
                sleep(2)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
