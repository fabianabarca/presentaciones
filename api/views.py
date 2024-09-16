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
            try:
                group = int(request.query_params.get("grupo"))
                if group > 300 or (group < 100 and group != 0):
                    return Response(
                        {
                            "error": "El número del grupo debe ser un número entero entre 100 y 300."
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            except ValueError:
                return Response(
                    {
                        "error": "El número del grupo debe ser un número entero."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            timestamp = datetime.now()
            if group == 0:
                # Datos de ejemplo
                seed = group + int(timestamp.timestamp())
                sample_size = 4
                noise = stats.norm.rvs(size=sample_size, random_state=seed)
                colors = [
                    "negro",
                    "azul",
                    "café",
                    "gris",
                    "verde",
                    "naranja",
                    "rosado",
                    "morado",
                    "rojo",
                    "blanco",
                    "amarillo",
                ]
                variable_1 = np.random.randint(0, 100, sample_size)
                variable_2 = transform(variable_1) + noise
                variable_3 = random.sample(colors, sample_size)

                return Response(
                    {
                        "group": group,
                        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                        "sample_size": sample_size,
                        "variable_1": variable_1,
                        "variable_2": variable_2,
                        "variable_3": variable_3,
                    }
                )
            else:
                # Datos del proyecto
                distributions = [
                    "burr12",
                    "cauchy",
                    "chi2",
                    "expon",
                    "f",
                    "fisk",
                    "gamma",
                    "gompertz",
                    "johnsonsb",
                    "johnsonsu",
                    "laplace",
                    "levy",
                    "logistic",
                    "lognorm",
                    "nakagami",
                    "pareto",
                    "rayleigh",
                    "rice",
                    "t",
                    "uniform",
                ]
                params = {
                    "burr12": (3, 2),
                    "cauchy": (),
                    "chi2": (4,),
                    "expon": (),
                    "f": (5, 2),
                    "fisk": (4,),
                    "gamma": (3,),
                    "gompertz": (1,),
                    "johnsonsb": (0.5, 0.5),
                    "johnsonsu": (0.5, 0.5),
                    "laplace": (),
                    "levy": (),
                    "logistic": (),
                    "lognorm": (1,),
                    "nakagami": (3.24,),
                    "pareto": (2),
                    "rayleigh": (),
                    "rice": (2,),
                    "t": (5,),
                    "uniform": (),
                }

                random.seed(group)
                dist_name = random.sample(distributions, 1)[0]
                dist_class = getattr(stats, dist_name)
                X = dist_class(*params[dist_name])
                sample_size = 100
                variable_1 = X.rvs(size=sample_size, random_state=group)
                variable_2 = transform(variable_1)

                return Response(
                    {
                        "group": group,
                        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                        "sample_size": sample_size,
                        "variable_1": variable_1,
                        "variable_2": variable_2,
                    }
                )
        else:
            return Response(
                {
                    "error": "Es necesario especificar el número del grupo como parámetros de la solicitud al API."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )



def transform(x):
    return np.power(x, 2) + 1
