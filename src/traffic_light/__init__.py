from config import use_fake_traffic_light
from .fake_traffic_light import FakeTrafficLight
from .traffic_light import TrafficLight


def get_traffic_light() -> TrafficLight:
    print(use_fake_traffic_light)
    if use_fake_traffic_light:
        return FakeTrafficLight()
    return TrafficLight()
