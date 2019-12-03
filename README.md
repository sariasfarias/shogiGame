# shogiGame
# INSTRUCCIONES

Ejecutar main.py en la terminal

Escibir las direcciones de las piezas en minúsula. ej: Peón -> p
Las piezas re insertadas se llaman con el numero adelate del nombre
Cuando un valor sea erróneo la maquina le pedirá reingresar los datos

# Implementación

Para la implementación del juego se importaron las librerias de numpy y colorama. 
En la realizacion del ejercicio no se tuvo en cuenta que tanto la torre como el alfil no pueden pasar sobre otras piezas. Por lo tanto se mueven libremente sobre el tablero.
La reinserción de fichas se lleva adelante sin conflicto, asi como el movimiento de piezas promocionadas.
En el último punto el jaque-mate se realiza cuando una ficha come al rey, dando por terminado el juego. El aviso de jaque esta desarrollado pero no se puedo implementar adecuadamente

# Metodologia de desarrollo.
+ Diseño de tablero
+ Movimiento del rey por el tablero
+ Movimiento de las piezas restantes
+ Promocion de las piezas
+ Movimiento de promoción de las piezas
+ Definición de jaque y jaque mate
