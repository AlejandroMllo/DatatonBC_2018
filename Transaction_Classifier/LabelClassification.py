
categories = ["Servicios bancarios", "Gobierno", "Valor agregado", "Administración central", "Educación", "Electricidad",
            "Tecnología y comunicaciones","Construcción","Servicios sociales","Servicios a empresas","Transporte",
            "Salud","Comercio","Servicios financieros","Servicios a personas","Seguros","Comida", "DEFAULT LABEL",
            "Turismo","Otros"]


def label_for(category):

    if category == "bancos":
        return categories[0]
    elif category == "municipios" or category == "departamentos":
        return categories[1]
    elif category == "valor agregado":
        return categories[2]
    elif category == "administración central":
        return categories[3]
    elif category == "establecimientos educativos":
        return categories[4]
    elif category == "electricidad":
        return categories[5]
    elif category == "telefonia fija" or category == "procesamiento de datos"\
            or category == "medios" or category == "programación":
        return categories[6]
    elif category == "obras de infraestructura" or category == "edificaciones" or category ==  "fabricación de cemento"\
            or category == "materiales de construcción y maquinaría":
        return categories[7]
    elif category == "cajas de compensación" or category == "culturales y otros servicios sociales"\
            or category == "fondos de pensiones":
        return categories[8]
    elif category == "servicios a empresas":
        return categories[9]
    elif category == "transporte terrestre" or category == "transporte aereo":
        return categories[10]
    elif category == "eps y salud prepagada (salud)" or category == "ips"\
            or category == "comercio al por menor de productos farmacéuticos y medicinales"\
            or category == "actividades de hospitales y clínicas"\
            or category == "fabricación de productos farmacéuticos" or category == "medicinales"\
            or category == "actividades de la práctica médica":
        return categories[11]
    elif category == "comercio de variedades y vestuario"\
            or category == "comercio al por mayor de computadores" or category == "automotores"\
            or category == "distribuidores productos consumo masivo"\
            or category == "comercio al por menor de artículos de ferretería" or category == "comercio de partes"\
            or category == "fabricación de partes y piezas de madera" or category == "equipos periféricos"\
            or category == "productos ceramicos" or category == "productos de vidrio"\
            or category == "confección de artículos con materiales textiles" or category == "textiles"\
            or category == "muebles y computadores" or category == "comercio al por mayor de productos textiles"\
            or category == "comercio al por menor de electrodomésticos y gasodomésticos de uso doméstico"\
            or category == "comercio de motocicletas y de sus partes"\
            or category == "comercio al por mayor de equipo" or category == "productos metalicos"\
            or category == "comercio de repuestos" or category == "madera y muebles"\
            or category == "materiales y artículos de papelería y escritorio" or category == "aseo"\
            or category == "otros manufactura" or category == "plastico" or category == "agroquimicos"\
            or category == "fabricación de jabones y detergentes" or category == "confección de prendas de vestir":
        return category[12]
    elif category == "otros servicios financieros" or category == "otras actividades de servicio financiero" \
            or category ==  "companías de financiamiento comercial" or category == "fideicomisos":
        return categories[13]
    elif category == "servicios a personas" or category ==  "personas":
        return categories[14]
    elif category == "servicios a personas" or category == "personas":
        return categories[15]
    elif category == "seguros":
        return categories[16]
    elif category == "alimentos concentrados"\
            or category == "líquidos"\
            or category == "con surtido compuesto principalmente por productos diferentes de alimentos (víveres en general)"\
            or category == "aliños y salsas"\
            or category == "comercio al por menor en establecimientos no especializados con surtido compuesto principalmente por alimentos"\
            or category == "arroz" or category == "elaboración de bebidas no alcohólicas":
        return categories[17]
    elif category == "DEFAULT_LABEL":
        return categories[18]
    elif category == "turismo y agencias de turismo" or category == "otras actividades mineras"\
            or category == "imprentas y edicion" or  category == "edición de periódicos"\
            or category == "otras actividades profesionales" or category == "comisionistas de bolsa":
        return categories[19]
