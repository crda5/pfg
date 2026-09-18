import random


class DataSimulator:
    def __init__(self):
        self.angulo = 30.0
        self.velocidad = 20.0
        self.corriente = 0.8
        self.torque = 1.2
        self.temperatura = 32.0

        self.desgaste = 0.0100
        self.vida_util = 90.0

    def update(self):
        # Movimiento suave del ángulo
        self.angulo += random.uniform(-2.0, 2.0)

        if self.angulo < 0:
            self.angulo = 0

        if self.angulo > 180:
            self.angulo = 180

        # Velocidad
        self.velocidad += random.uniform(-1.5, 1.5)
        self.velocidad = max(0, self.velocidad)

        # Corriente
        self.corriente += random.uniform(-0.05, 0.05)
        self.corriente = max(0, self.corriente)

        # Torque
        self.torque += random.uniform(-0.08, 0.08)
        self.torque = max(0, self.torque)

        # Temperatura
        self.temperatura += random.uniform(-0.2, 0.3)

        # Simulación de desgaste acumulativo
        self.desgaste += random.uniform(
            0.00001,
            0.00005
        )

        # Vida útil simulada
        self.vida_util -= random.uniform(
            0.001,
            0.005
        )

        self.vida_util = max(
            0,
            self.vida_util
        )

        return {
            "angulo": self.angulo,
            "velocidad": self.velocidad,
            "corriente": self.corriente,
            "torque": self.torque,
            "temperatura": self.temperatura,
            "desgaste": self.desgaste,
            "vida_util": self.vida_util
        }