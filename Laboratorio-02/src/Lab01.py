import numpy as np
import matplotlib.pyplot as plt
import time
import psutil

'''  PROGRAMA 1  '''

### CUANTOS RECURSOS CONSUME EL PROGRAMA ###
def get_resource_info(code_to_measure):
    resources_save_data = get_resource_usage(code_to_measure=code_to_measure)
    print(f"Tiempo de CPU: {resources_save_data['tiempo_cpu']} segundos")
    print(f"Uso de memoria virtual: {resources_save_data['memoria_virtual']} MB")
    print(f"Uso de memoria residente: {resources_save_data['memoria_residente']} MB")
    print(f"Porcentaje de uso de CPU: {resources_save_data['%_cpu']} %")

def get_resource_usage(code_to_measure):
    process = psutil.Process()
    #get cpu status before running the code
    cpu_percent = psutil.cpu_percent()
    start_time = time.time()
    code_to_measure()
    end_time = time.time()
    end_cpu_percent = psutil.cpu_percent() 
    cpu_percent = end_cpu_percent - cpu_percent
    cpu_percent = cpu_percent / psutil.cpu_count()
    
    return {
        'tiempo_cpu': end_time - start_time,
        'memoria_virtual': process.memory_info().vms / (1024 * 1024),  # Convertir a MB
        'memoria_residente': process.memory_info().rss / (1024 * 1024),  # Convertir a MB
        '%_cpu': cpu_percent # Porcentaje de uso de CPU
    }

def mi_programa():

    #Extraer lineas y separarlas por espacio
    f = open('UNI_CORR_500_01.txt', 'r')
    
    crd = []
    coordenadas =[]
    for line in f.readlines():
        extraer = line[0:29]
        aux = extraer.split()
        crd.append(aux)
    f.close()


    #Identificar las coordenadas y agregarlas a las listas requeridas más adelante
    for n in range (4, len(crd)):
        ListAux = crd[n]
        a = []
        tup = []
        X = ListAux[2]
        Y = ListAux[3]
        Z = ListAux[4]
   
        #agregar las coordenadas X, Y y Z a una lista auxiliar a (PARTE 1)
        a.append(float(X))
        a.append(float(Y))
        a.append(float(Z))
        #agregar la lista auxiliar a como sublista (PARTE 1)
        coordenadas.append(a)
        #print(X, Y, Z, sep=' ')


    ### PARTE 1 ###

    #Coordenadas X,Y que mas se repiten
    FrecuenciasXY = {tuple(coord[0:2]): 0 for coord in (coordenadas)}

    for coord in coordenadas:
        coordenadaXY = tuple(coord[0:2])
        FrecuenciasXY[coordenadaXY]+=1

    max_frecuencia_XY = max(FrecuenciasXY.values())
    tupla_mas_repetida = [numero for numero, frecuencia in FrecuenciasXY.items() if frecuencia == max_frecuencia_XY]


    ### PARTE 2 ###

    ix = 320
    iy = 480
    mx = (640-ix)/9
    my = (0-iy)/5
    Xpixel = []
    Ypixel = []

    print(my)
    #Conversion coordenada metro a pixel
    def Conversion(CoordenadaM):
        Xmetro, Ymetro = CoordenadaM
        Xpixel = int(mx * Xmetro + ix)
        Ypixel = int(my * Ymetro + iy)
        return Xpixel , Ypixel


    #Diccionario frecuencia de posiciones en pixel
    FrecuenciaPixel = {(ValX, ValY): 0 for ValX in range(641)for ValY in range (481)}


    #Pasar metro a pixel en el diccionario
    for coordenada, frecuencia in FrecuenciasXY.items():
        CoordenadaPixel = Conversion(coordenada)
        Xpixel.append(CoordenadaPixel[0])
        Ypixel.append(CoordenadaPixel[1])
        #print(f'La coordenada metrica: {coordenada} pasa a pixel {CoordenadaPixel}' )
        FrecuenciaPixel[CoordenadaPixel] = frecuencia
    print('')


    #Coordenadas X, Y que mas se repiten en pixel
    max_FrecuPixelXY = max(FrecuenciaPixel.values())
    XYPixel_mas_repetida = [CordXY for CordXY, frecuenciaXY in FrecuenciaPixel.items() if frecuenciaXY == max_FrecuPixelXY]
    print(f"La(s) coordenadas X,Y en pixel que más se repite(n): {XYPixel_mas_repetida} con un recuento de {max_FrecuPixelXY} oportunidades")

    print('')

    ### GRAFICAR MAPA DE CALOR ###

    bins = 350

    heatmap, xedges, yedges = np.histogram2d(Xpixel, Ypixel, bins=bins)

    heatmap = heatmap.T

    x_extent = [0, 640]
    y_extent = [480, 0]

    plt.imshow(heatmap, extent=[x_extent[0], x_extent[1], y_extent[0], y_extent[1]], cmap='RdBu')
    plt.colorbar(label='Frecuencia')
    plt.show()



### CUANTOS RECURSOS CONSUME EL PROGRAMA 1 ###

if __name__ == "__main__":
    get_resource_info(mi_programa)