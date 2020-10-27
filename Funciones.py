def window(data):
    '''
    data: Valores del activo EURUSD.
    
    '''
    data = np.array(data.Close) #De los datos del activo, selecciona la columna Close y la hace un array.
    
    n = len(data) #Tamaño de el array de datos.
    sigma = data.std() #Desviación estandar de los datos.
    p = np.log(n)*sigma**2 #Penalización que tiene el modelo.
    suma = []
    #Pasos a realizar para el metodo de window-based.
    for i in range (0,100):
        algo = rpt.Window(width=i+10).fit(data)
        my_bkps = algo.predict(pen=p)
        senal = pd.DataFrame(my_bkps)
        suma.append(my_bkps)
    suma = pd.DataFrame(suma)
    suma = suma.dropna()

    width = list(suma.index)
    width = width[0]

    for i in range (0,100):
        algo = rpt.Window(width=width, jump=i+1).fit(data)
        my_bkps = algo.predict(pen=p)
        senal = pd.DataFrame(my_bkps)
        suma.append(my_bkps)
    suma = pd.DataFrame(suma)
    suma = suma.dropna()

    jump = list(suma.index)
    jump = jump[0]

    algo = rpt.Window(width=width, jump=jump).fit(data)
    my_bkps = algo.predict(pen=p)
    senal = pd.DataFrame(my_bkps)

    mean = senal.drop(len(my_bkps)-1) #Quitamos de la serie el último valor ya que no es correcto. 
    mean = np.array(mean) #Datos generados del metodo, traidos a un array.
    changes = mean.astype(int) #Hacer que el array contenga solo valores numericos enteros.

    fecha = [] #Lista vacia para introducir fechas donde el cambio ocurrio.
    #For para introducir los valores de la fechas en donde ocurrieron los changepoints.
    for i in range (0, len(my_bkps)-1):
        fecha += df_pe.index[changes[i]]

    #Esta variable sirve para crear el feature que se utilizará en el modelo.
    feature = boolean_change_point(df_pe, changes)
    
    #La función regresa las fechas y los valores numericos en donde ocurrieron los cambios.
    return fecha, changes, feature

def binary(data):
    '''
    data: Valores del activo EURUSD.
    
    '''
    data = np.array(df_pe.Close)

    n = len(data) #Tamaño de los datos dentro del array.
    sigma = data.std() #Desviación estandar de los datos.
    p = np.log(n)*sigma**2 #Penalización utilizada dentro del modelo.

    #Pasos a realizar dentro del modelo de Binary segmentation.
    algo = rpt.Binseg().fit(data)
    my_bkps = algo.predict(pen=p)
    senal = pd.DataFrame(my_bkps)

    mean = senal.drop([len(my_bkps)-1]) #Quitamos de la serie el último valor ya que no es correcto.
    mean = np.array(mean) #Valores obtenidos del modelo traidos a un array.

    changes = mean.astype(int) #Valores del array anterior convertidos a numeros enteros.

    fecha = [] #Lista vacia para introducir fechas deseadas.
    #For para introducir las fechas en donde ocurrio un cambio.
    for i in range (0, len(my_bkps)-1):
        fecha += df_pe.index[changes[i]]
        
    feature = boolean_change_point(df_pe, changes)
    
    #La función regresa las fechas y los cambios numericos. 
    return fecha, changes, feature


def zerolistmaker(n):
    list_zeros = [0] * n #Multiplica 0's por la dimensión 'n'.

    #Regresa una lista de zeros de dimensión n.
    return list_zeros

def boolean_change_point(data, changes):
    
    data = np.array(data.Close) #De los datos del activo, selecciona la columna Close y la hace un array.
    #Uso de la función de 'zerolistmaker'.
    zero = zerolistmaker(len(data)) #Crea una lista de zeros del tamaño de tus datos.

    change = [int(x) for x in changes] #Cuenta cuantos cambios haras dentro de tu lista.
    
    #For para cambiar los datos en donde haya un cambio.
    for i in range (0, len(change)):
        zero[change[i]] = 1
        
    #Regresa una lista en donde se encuentran los cambios como 1 y los no cambios como 0. 
    return zero

def graph_changepoint(data, changes):
    '''
    data: Información del activo EURUSD.
    changes: Variable obtenida de algún modelo de change point. 
    '''
    data = np.array(data.Close) #De los datos del activo, selecciona la columna Close y la hace un array.

    #Pasos para graficar la información obtenida del modelo y de los datos.
    #Esta función regresa una gráfica para hacer visuales los resultados obtenidos del modelo.
    plt.figure(figsize=(16,8))
    plt.title('Change points detected.', size=20)
    plt.plot(data, label='Close price' ,color='darkorange', alpha = 0.7)
    plt.rc('xtick', labelsize=20) 
    plt.rc('ytick', labelsize=20) 
    plt.xlabel('Días transcurridos desde 2001',size=20)
    plt.ylabel('Precios de cierre',size=20)
    plt.legend(loc='upper left', fontsize=(18))
    for i in range (len(changes)):
        plt.axvline(x=changes[i], ymin=0,ymax=1.6, color='dimgray', linestyle='--')
