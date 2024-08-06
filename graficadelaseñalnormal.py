
# importar paquete wfdb para leer "records" de 
# physionet 
import wfdb
import matplotlib.pyplot as plt 
  
# cargar la informacion (hay que tener todos los archivos . dat y .net)
 
signal = wfdb.rdrecord ("fetal_PCG_p06_GW_36")
# obtener valores y de la señal 
valores = signal.p_signal 
tamaño =  signal.sig_len # numero de muestras

print (valores)
plt.plot (valores)

