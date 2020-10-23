def binary(data):
    '''
    data: array[], de valores Close del activo EURUSD.
    
    '''
    
    n = len(data) #Tamaño de los datos dentro del array.
    sigma = data.std() #Desvación estandar de los datos.
    p = np.log(n)*sigma**2 #Penalización utilizada dentro del modelo.
    
    #Pasos a realizar dentro del modelo de Binary segmentation.
    algo = rpt.Binseg().fit(data)
    my_bkps = algo.predict(pen=p)
    senal = pd.DataFrame(my_bkps)

    mean = np.array(senal) #Valores obtenidos del modelo traidos a un array.
    changes = mean.astype(int) #Valores del array anterior convertidos a numeros enteros.
    
    fecha = [] #Lista vacia para introducir fechas deseadas.
    #For para introducir las fechas en donde ocurrio un cambio.
    for i in range (0, len(my_bkps)-1):
        fecha += df_pe.index[changes[i]]
    
    #La función regresa las fechas y los cambios numericos. 
    return fecha, changes
