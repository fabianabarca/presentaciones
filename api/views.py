from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import random
import numpy as np
from scipy import stats
from datetime import datetime

# Create your views here.


class DataView(APIView):
    def get(self, request):
        # Verificar parámetros
        if request.query_params.get("grupo"):
            group = int(request.query_params.get("grupo"))
        else:
            return Response(
                {
                    "error": "Es necesario especificar el número del grupo como parámetros de la solicitud al API."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if group == 0:
            # Datos de ejemplo
            timestamp = datetime.now()
            seed = group + int(timestamp.timestamp())
            size = 4
            noise = stats.norm.rvs(size=size, random_state=seed)
            colors = ["negro", "azul", "café", "gris", "verde", "naranja", "rosado", "morado", "rojo", "blanco", "amarillo"]
            variable_1 = np.random.randint(0, 100, size)
            variable_2 = transform(variable_1) + noise
            variable_3 = random.sample(colors, size)
            
            return Response(
                {
                    "group": group,
                    "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "sample_size": size,
                    "variable_1": variable_1,
                    "variable_2": variable_2,
                    "variable_3": variable_3,
                }
            )
        else:
            # Datos del proyecto
            return Response(
                {"error": "El grupo especificado no tiene datos disponibles todavía."},
                status=status.HTTP_404_NOT_FOUND,
            )


def transform(x):
    return np.log(x) + 1
