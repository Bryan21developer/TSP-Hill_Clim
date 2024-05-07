import math
import random
from flask import Flask, render_template, request

app = Flask(__name__)

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def evalua_ruta(ruta):
    total = 0
    for i in range(len(ruta)-1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    ciudad1 = ruta[-1]  # Last city
    ciudad2 = ruta[0]   # First city to complete the loop
    total += distancia(coord[ciudad1], coord[ciudad2])
    return total

def i_hill_climbing():
    ruta = list(coord.keys())  # Initial random route
    mejor_ruta = ruta[:]  # Best route so far
    max_iteraciones = 10

    while max_iteraciones > 0:
        mejora = False
        random.shuffle(ruta)  # Generate a new random route
        for i in range(len(ruta)):
            for j in range(len(ruta)):
                if i != j:
                    ruta_tmp = ruta[:]  # Copy the route
                    ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]  # Swap cities
                    dist = evalua_ruta(ruta_tmp)
                    if dist < evalua_ruta(ruta):
                        mejora = True
                        ruta = ruta_tmp[:]  # Update route if improvement found
        max_iteraciones -= 1

        if evalua_ruta(ruta) < evalua_ruta(mejor_ruta):
            mejor_ruta = ruta[:]
    
    return mejor_ruta

coord = {
    'Jiloyork' :(19.916012, -99.580580),
    'Toluca':(19.289165, -99.655697),
    'Atlacomulco':(19.799520, -99.873844),
    'Guadalajara':(20.677754472859146, -103.34625354877137),
    'Monterrey':(25.69161110159454, -100.321838480256),
    'QuintanaRoo':(21.163111924844458, -86.80231502121464),
    'Michohacan':(19.701400113725654, -101.20829680213464),
    'Aguascalientes':(21.87641043660486, -102.26438663286967),
    'CDMX':(19.432713075976878, -99.13318344772986),
    'QRO':(20.59719437542255, -100.38667040246602)
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    ruta = i_hill_climbing()
    distancia_total = evalua_ruta(ruta)
    return render_template('resultado.html', ruta=ruta, distancia_total=distancia_total)

if __name__ == "__main__":
    app.run(debug=True)
