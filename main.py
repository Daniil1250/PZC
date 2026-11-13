from enum import Enum


print("MIET")


class Role(Enum):
    """Роли пользователей умного дома."""
    ADMIN = "admin"
    GUEST = "guest"


class Device:
    """Базовый класс для всех устройств."""

    def __init__(self, device_id, name):
        self._device_id = device_id
        self._name = name
        self._status = "off"

    @property
    def device_id(self):
        return self._device_id

    @property
    def name(self):
        return self._name

    @property
    def status(self):
        return self._status

    def turn_on(self):
        self._status = "on"

    def turn_off(self):
        self._status = "off"

    def __str__(self):
        return f"{self._name} ({self._device_id}): {self._status}"


class Light(Device):
    """Умная лампа."""

    def __init__(self, device_id, name, brightness=100):
        super().__init__(device_id, name)
        self._brightness = brightness

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Яркость должна быть от 0 до 100")
        self._brightness = value

    def turn_on(self):
        super().turn_on()
        print(f"Лампа {self._name} включена. Яркость: {self._brightness}%")


class Thermostat(Device):
    """Умный термостат."""

    def __init__(self, device_id, name, current=20):
        super().__init__(device_id, name)
        self._current_temp = current

    @property
    def current_temp(self):
        return self._current_temp

    def set_temperature(self, value):
        if not (10 <= value <= 30):
            raise ValueError("Температура должна быть от 10 до 30 градусов")
        self._current_temp = value
        print(f"Термостат {self._name} установлен на {self._current_temp}°C")


class User:
    """Пользователь системы."""

    def __init__(self, name, role):
        self.name = name
        self.role = role


class SmartHome:
    """Система управления умным домом."""

    def __init__(self):
        self._devices = {}

    def add_device(self, device):
        if device.device_id in self._devices:
            raise ValueError("Устройство с таким ID уже существует")
        self._devices[device.device_id] = device

    def control_device(self, user, device_id, action, **kwargs):
        if device_id not in self._devices:
            print(f"Ошибка: Устройство {device_id} не найдено")
            return

        if user.role == Role.GUEST and action == "set_temperature":
            print(f"Доступ запрещен: Пользователь {user.name} не имеет прав на изменение температуры")
            return

        device = self._devices[device_id]

        if action == "turn_on":
            device.turn_on()
        elif action == "turn_off":
            device.turn_off()
        elif action == "set_temperature":
            if hasattr(device, 'set_temperature'):
                device.set_temperature(kwargs.get('value'))
            else:
                print("Ошибка: Это устройство не поддерживает установку температуры")
        else:
            print(f"Неизвестное действие: {action}")


home = SmartHome()
lamp = Light("L1", "Лампа в гостиной", brightness=50)
thermostat = Thermostat("T1", "Термостат в спальне", current=22)

admin = User("Аня", Role.ADMIN)
guest = User("Иван", Role.GUEST)

home.add_device(lamp)
home.add_device(thermostat)

home.control_device(admin, "L1", "turn_on")
home.control_device(guest, "T1", "set_temperature", value=25)
