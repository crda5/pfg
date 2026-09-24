import random


class DataSimulator:

    def __init__(self):

        self.joints = {}

        for joint in range(1, 7):

            self.joints[joint] = {
                "angulo": random.uniform(20, 80),
                "velocidad": random.uniform(10, 50),
                "corriente": random.uniform(0.4, 1.2),
                "torque": random.uniform(0.5, 2.0),
                "temperatura": random.uniform(28, 35),

                # Provisionales
                "vibracion": random.uniform(0.05, 0.20),
                "errorPosicion": random.uniform(0, 1.0),
                "ciclos": 0,
                "tiempoOperacion": 0.0
            }


    def update(self):

        for joint in self.joints.values():

            # Ángulo
            joint["angulo"] += random.uniform(-2, 2)

            joint["angulo"] = max(
                0,
                min(joint["angulo"], 180)
            )

            # Velocidad
            joint["velocidad"] += random.uniform(-10, 10)

            joint["velocidad"] = max(
                0,
                min(joint["velocidad"], 180)
            )

            # Corriente
            joint["corriente"] += random.uniform(-0.05, 0.05)

            joint["corriente"] = max(
                0,
                joint["corriente"]
            )

            # Torque
            joint["torque"] += random.uniform(-0.08, 0.08)

            joint["torque"] = max(
                0,
                joint["torque"]
            )

            # Temperatura
            joint["temperatura"] += random.uniform(-0.2, 0.3)

            # Vibración simulada
            joint["vibracion"] += random.uniform(-0.02, 0.02)

            joint["vibracion"] = max(
                0,
                joint["vibracion"]
            )

            # Error de posición
            joint["errorPosicion"] += random.uniform(-0.1, 0.1)

            joint["errorPosicion"] = max(
                0,
                joint["errorPosicion"]
            )

            # Ciclos provisionales
            joint["ciclos"] += 1

            # Nuestro timer corre cada 0.5 s
            joint["tiempoOperacion"] += 0.5

        return self.joints