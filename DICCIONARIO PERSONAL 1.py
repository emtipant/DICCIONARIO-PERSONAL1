informacion_personal = {
    "NOMBRE": "ERIKA MARIBEL TIPAN TIPANTUÑA",
   # "EDAD": 23,
    "CIUDAD": "PUJILI",
    "PROFECION": "AUXILIAR DE FARMACIA",
    "DIRECCION": {
        "CALLE": "VIA LA MERCED",
        "N°": 56,
        "BARRIO": "SAN NICOLAS"
    },
    "CONTACTO": {
        "TELEFONO": "+593 958945628",
        "CORREO": "erika123@gmail.com"
    },
    "EXPERIENCIA_LABORAL": [
        {
            "EMPRESA": "FARMACIA CRUZ AZUL",
            "PUESTO": "ATENCION AL CLIENTE",
            "FECHA_INICIO": "2020-01-05",
            "FECHA_FIN": "2021-04-21"
        },
        {
            "EMPRESA": "FARMACIA SANASANA",
            "PUESTO": "VENTAS",
            "FECHA_INICIO": "2022-01-026",
            "FECHA_FIN": "actualidad"
        }
    ],
    "EDUCACION": {
        "TITULO": "BACHILLER",
        "COLEGIO": "UNIDAD EDUCATIVA PROVINCIA DE COTOPAXI",
        "FECHA_GRADUACION": "2019-07-28" ,
        "CURSO":"AUXILIAR DE FARMACIA"
    }
}

# Imprimir la información en columna
print("INFORMACION PERSONAL")
print(" ")
print("NOMBRE:", informacion_personal["NOMBRE"])
#print("EDAD:", informacion_personal["EDAD"])
print("CIUDAD:", informacion_personal["CIUDAD"])
print("PROFECION:", informacion_personal["PROFECION"])
print()
print("DIRECCION")
print("  CALLE:", informacion_personal["DIRECCION"]["CALLE"])
print("  N°:", informacion_personal["DIRECCION"]["N°"])
print("  BARRIO:", informacion_personal["DIRECCION"]["BARRIO"])
print()
print("CONTACTO")
print("  TELEFONO:", informacion_personal["CONTACTO"]["TELEFONO"])
print("  CORREO:", informacion_personal["CONTACTO"]["CORREO"])
print()
print("EXPERIENCIA LABORAL")
for experiencia in informacion_personal["EXPERIENCIA_LABORAL"]:
    print("  EMPRESA:", experiencia["EMPRESA"])
    print("  PUESTO:", experiencia["PUESTO"])
    print("  FECHA INICIO:", experiencia["FECHA_INICIO"])
    print("  FECHA FIN:", experiencia["FECHA_FIN"])
    print()
print("EDUCACION")
print("  TITULO:", informacion_personal["EDUCACION"]["TITULO"])
print("  COLEGIO:", informacion_personal["EDUCACION"]["COLEGIO"])
print("  FECHA DE GRADUACION:", informacion_personal["EDUCACION"]["FECHA_GRADUACION"])
print("  CURSO:",informacion_personal["EDUCACION"]["CURSO"])
