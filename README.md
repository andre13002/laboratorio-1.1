Estos códigos creados nos ayudan a visualizar una señal de un electrocardiograma fetal, que lo que muestra básicamente es la señal eléctrica del corazón del feto durante el embarazo.
1.⁠ ⁠Lo primero que se realizó fue descargar la señal del software physionet. En  github podemos evidenciar los dos archivos del mismo: .dat y .hea 
2.⁠ ⁠Lo segundo que se hizo fue graficar dicha señal en spyder este sería el archivo de nombre gráficadelaseñalnormal donde vemos la señal fetal 
3.⁠ ⁠Luego queríamos calcular la media de la señal, la desviación estándar y el coeficiente de variacion para tener un mejor análisis de esta,  llamamos el archivo de la señal normal, y codificamos los cálculos, para luego en la consola de spyder visualizar lo dicho previamente. Posterior a esto creamos un histograma y la curva de densidad en forma de gráfico que nos enseña el centro, la extensión, y la forma de los datos de esta señal. Todo esto lo evidenciamos en el archivo llamado: fórmulas estadísticas desde cero.
4.⁠ ⁠Luego realizamos lo mismo pero con el método de las funciones de Python y esto lo podemos visualizar en el archivo: fórmulas estadísticas con funciones de Python. 
5.⁠ ⁠Por último queríamos contaminar la señal con diferentes tipos de ruidos esto se hizo llamando nuevamente la señal normal, generando el ruido y agregándolo a la señal normal, luego analizamos el SRN que es la señal a ruido para así medir la calidad de nuestra señal.-RUIDO GAUSSIANO, RUIDO  IMPULSIVO, RUIDO TIPO ARTEFACTO: estos ruidos los agregamos con la intención de analizar la simulación en condiciones reales debido a que ayudan a simular las interferencias de dichas condiciones, ayuda a analizar la capacidad de precisión de la señal y su sensibilidad con relación a las perturbaciones. Esto lo podemos visualizar en el archivo llamado: Ruidos