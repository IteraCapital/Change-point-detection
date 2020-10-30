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
