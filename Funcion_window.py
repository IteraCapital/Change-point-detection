def window(data):
    '''
    data: Valores del activo EURUSD.
    
    '''
        
    data = np.array(data.Close) #De los datos del activo, selecciona la columna Close y la hace un array.
    
    n = len(data) #Tamaño de el array de datos.
    sigma = data.std() #Desviación estandar de los datos.
    p = np.log(n)*sigma**2 #Penalización que tiene el modelo.
    
    #Pasos a realizar para el metodo de window-based.
    algo = rpt.Window(width=32, jump=24).fit(data)
    my_bkps = algo.predict(pen=p)
    senal = pd.DataFrame(my_bkps)
    
    mean = np.array(senal) #Datos generados del metodo, traidos a un array.
    changes = mean.astype(int) #Hacer que el array contenga solo valores numericos enteros.
    
    fecha = [] #Lista vacia para introducir fechas donde el cambio ocurrio.
    #For para introducir los valores de la fechas en donde ocurrieron los changepoints.
    for i in range (0, len(my_bkps)-1):
        fecha += df_pe.index[changes[i]]
    
    #La función regresa las fechas y los valores numericos en donde ocurrieron los cambios.
    return fecha, changes
