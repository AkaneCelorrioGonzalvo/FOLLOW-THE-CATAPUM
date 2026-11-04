modo_prueba = True
log_visibilidad = True

# El formato era: acc_x;acc_y;acc_z;pitch;roll;yaw;vel;vel_max;latitud;longitud;altura;altura_max;temperatura;estado;flag

numero_de_variables_emitidas = 15

listado_nombre_variables = ["acc_x", "acc_y", "acc_z", "pitch", "roll", "yaw", "vel", "vel_max", "latitud", "longitud", "altura", "altura_max", "temperatura", "estado", "flag"]

# Para las variables aleatorias. Rango inferior, rango superior y número de decimales.

rangos_variables_aleatorias = [
        ((-16, 16), 3),       # acc_x [G]
        ((-16, 16), 3),       # acc_y [G]
        ((-16, 16), 3),       # acc_z [G]
        ((-180, 180), 2),     # pitch [°]
        ((-180, 180), 2),     # roll [°]
        ((0, 360), 2),        # yaw [°]
        ((0, 250), 2),        # vel [m/s]
        ((0, 300), 2),        # vel_max [m/s]
        ((-90, 90), 6),       # latitud [°]
        ((-180, 180), 6),     # longitud [°]
        ((0, 3000), 2),       # altura [m]
        ((0, 5000), 2),       # altura_max [m]
        ((-20, 80), 1),       # temperatura [°C]
        ((0, 10), 0),         # estado
        ((0, 255), 0),        # flag
    ]

# Diccionario

SENSORES_TELEMETRIA = [
    {
        "clave": "acc_x",
        "texto": "ACC X [G]",
        "ruta_icono": None,
        "tipo_variable": "float",
        "valor_inicial": 0.0,
        "decimales": 3,
    },
    {
        "clave": "acc_y",
        "texto": "ACC Y [G]",
        "ruta_icono": None,
        "tipo_variable": "float",
        "valor_inicial": 0.0,
        "decimales": 3,
    },
    {
        "clave": "acc_z",
        "texto": "ACC Z [G]",
        "ruta_icono": None,
        "tipo_variable": "float",
        "valor_inicial": 0.0,
        "decimales": 3,
    },
    {
        "clave": "pitch",
        "texto": "PITCH [°]",
        "ruta_icono": None,
        "tipo_variable": "float",
        "valor_inicial": 0.0,
        "decimales": 2,
    },
    {
        "clave": "roll",
        "texto": "ROLL [°]",
        "ruta_icono": None,
        "tipo_variable": "float",
        "valor_inicial": 0.0,
        "decimales": 2,
    },
    {
        "clave": "yaw",
        "texto": "YAW [°]",
        "ruta_icono": None,
        "tipo_variable": "float",
        "valor_inicial": 0.0,
        "decimales": 2,
    },
    {
        "clave": "vel",
        "texto": "VEL [m/s]",
        "ruta_icono": None,
        "tipo_variable": "float",
        "valor_inicial": 0.0,
        "decimales": 2,
    },
    {
        "clave": "vel_max",
        "texto": "VEL MAX [m/s]",
        "ruta_icono": None,
        "tipo_variable": "float",
        "valor_inicial": 0.0,
        "decimales": 2,
    },
    {
        "clave": "latitud",
        "texto": "LAT [°]",
        "ruta_icono": None,
        "tipo_variable": "float",
        "valor_inicial": 0.0,
        "decimales": 6,
    },
    {
        "clave": "longitud",
        "texto": "LON [°]",
        "ruta_icono": None,
        "tipo_variable": "float",
        "valor_inicial": 0.0,
        "decimales": 6,
    },
    {
        "clave": "altura",
        "texto": "ALTURA [m]",
        "ruta_icono": None,
        "tipo_variable": "float",
        "valor_inicial": 0.0,
        "decimales": 2,
    },
    {
        "clave": "altura_max",
        "texto": "ALTURA MAX [m]",
        "ruta_icono": None,
        "tipo_variable": "float",
        "valor_inicial": 0.0,
        "decimales": 2,
    },
    {
        "clave": "temperatura",
        "texto": "TEMP [°C]",
        "ruta_icono": None,
        "tipo_variable": "float",
        "valor_inicial": 0.0,
        "decimales": 1,
    },
    {
        "clave": "estado",
        "texto": "ESTADO",
        "ruta_icono": None,
        "tipo_variable": "int",
        "valor_inicial": 0,
        "decimales": 0,
    },
    {
        "clave": "flag",
        "texto": "FLAG",
        "ruta_icono": None,
        "tipo_variable": "int",
        "valor_inicial": 0,
        "decimales": 0,
    },
]


CLAVES_SENSORES_TELEMETRIA = [sensor["clave"] for sensor in SENSORES_TELEMETRIA]