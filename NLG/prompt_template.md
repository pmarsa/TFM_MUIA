Extrae todas las entidades nombradas de la siguiente factura o albarán y clasifícalas según las siguientes etiquetas, cuyos criterios debes consultar a continuación:

1. NOMBRE_EMPRESA
2. NUMERO_FACTURA
3. FECHA
4. EAN
5. SKU
6. NOMBRE_PRODUCTO
7. CANTIDAD
8. PRECIO_COSTE_UNIDAD


Debes tener en cuenta los siguientes factores:
- Siempre debes procesar los datos fila por fila. 
- Cada fila está compuesta por NOMBRE_PRODUCTO, CANTIDAD, PRECIO_COSTE_UNIDAD. En ocasiones también se añade el dato SKU, en otras EAN, a veces están los dos: SKU y EAN. Añade el número de ID de fila de forma incremental, partiendo siempre desde 0.
- Bajo ningún concepto puedes alterar el texto de la factura que te sea dado. No corrijas ningún tipo de fallo ortográfico, carácter mal introducido o errores de OCR en el texto de la factura.
- No obstante, cuando identifiques una entidad cuyo contenido (especialmente en NOMBRE_PRODUCTO) sea completamente ilegible e ilógico, por errores en el reconocimiento de caracteres, OMITE la fila entera. Ejemplo de un producto que no debes anotar: "ORacitdoopua tRhe tmraavsetelerre d0: -M PySs5tery Soulless Army - PS5 31 4206,,4986 €€ 12261,,9464 €€ 2211%% 255,,6560 €€\n5055277055579"
- Si no encuentras el dato esperado en una fila debes asignar un valor nulo, pero busca el resto de datos de esa misma fila antes de pasar a la siguiente.


Finalmente, debes ir almacenando estos datos en formato JSON de la siguiente forma:

```
{
  "ID_FACTURA": null,
  "NOMBRE_EMPRESA": "EMPRESA MASTER",
  "NUMERO_FACTURA": "FAC000123",
  "FECHA": "01/01/2025",
  "PRODUCTOS": [
    {
      "ID": 0,
      "SKU": "SKU0001",
      "EAN": "1234567890123",
      "NOMBRE_PRODUCTO": "PRODUCTO 1",
      "CANTIDAD": 10,
      "PRECIO_COSTE_UNIDAD": 9.99
    },
    {
      "ID": 1,
      "SKU": "SKU0002",
      "EAN": "9876543210987",
      "NOMBRE_PRODUCTO": "PRODUCTO 2",
      "CANTIDAD": 5,
      "PRECIO_COSTE_UNIDAD": 14.50
    }
  ]
}
```

{text}

Solo puedes devolver el resultado en formato JSON. No devuelvas nada más que el JSON.

A continuación tienes el listado de entidades que debes anotar:


### ENTIDAD: 1. NOMBRE_EMPRESA

**Descripción:**  
- Nombre de la empresa que emite la factura o el albarán.

**Instrucciones:**  
Cuando encuentres la entidad "empresa", debes normalizarla con la string correspondiente de este listado:

- ALFA
- beta
- gamma
- DELTA
- EPSILON
- Zeta

**Ejemplos:**

- <ins>ALFA</ins> - xxx xxxxx xx xxxx xxxxx → ALFA [NOMBRE_EMPRESA]  
- <ins>BETA</ins> Tel : xxx/xx.xx.xx → BETA [NOMBRE_EMPRESA]  
- <ins>gamma</ins> xxxx• xxxx xxxxx x • xxxxx xxxxxxxx • xxxxxxxx → gamma [NOMBRE_EMPRESA]  
- <ins>Delta Venta de Merchandising</ins> x.x Cliente: → Delta Venta de Merchandising [NOMBRE_EMPRESA]  
- <ins>EPSILON</ins> xxxxxxxx, x.x → EPSILON [NOMBRE_EMPRESA]  
- <ins>Zeta</ins> xxxxx, x.x. | c/ xxxxxxxx, xxx, xx. xxxxxx | xxxxx xxxxxxxxx (xxxxx) | xxx xxxxxxxxxx | https://xxxxxxxxxxxxx.xx/ → Zeta [NOMBRE_EMPRESA]


### ENTIDAD: 2. NUMERO_FACTURA

Descripción:
- Número único de la factura o albarán.

Instrucciones:
- Se encuentra en el encabezado del texto, antes de la lista de items.
- Es una secuencia única de números o bien números + letras.

Ejemplos:
- 10/09/2025 <ins>FD696678</ins> xxxxx xxx xxxxxx &rarr; FD696678 [NUMERO_FACTURA]
- Facture n° <ins>2025004980</ins> &rarr; 2025004980 [NUMERO_FACTURA]
- xxxxxxx xxxxxx xx (xxxxxxxx) xxx xxxxx xxxxxxx xxxxxx xx (xxxxxxxxx) xxx xxxx xxxxxxx -<ins>1277087</ins> &rarr; 1277087 [NUMERO_FACTURA]
- Número de factura: <ins>2025-0109</ins> &rarr; 2025-0109 [NUMERO_FACTURA]
- <ins>179082</ins> 09/12/2025 09/12/2025 xxxxxx xxxxxxxxx &rarr; 179082 [NUMERO_FACTURA]
- Número de Factura: <ins>11079837</ins> &rarr; 11079837 [NUMERO_FACTURA]


### ENTIDAD: 3. FECHA

Descripción:
- Fecha de emisión de la factura o albarán.

Instrucciones:
- Siempre debes almacenar el dato en este formato: DD/MM/YYYY

Ejemplos:
- <ins>10/09/2025</ins> FD696678 xxxxxx xxx xxxxxxx &rarr; 10/09/2025 [FECHA]
- <ins>18/09/2025</ins> 1201559 &rarr; 18/09/2025 [FECHA]
- xxxxxxx xxxxxxxxx xxxxxxxxxx xxxxxxx xxxxxxx xxxxx <ins>14.01.2026</ins> &rarr; 14.01.2026 [FECHA]
- Fecha: <ins>19/07/2025</ins> &rarr; 19/07/2025 [FECHA]
- xxxxxx 09/12/2025 <ins>09/12/2025</ins> xxxxxx xxxxxxxxxx &rarr; 09/12/2025 [FECHA]
- N/ ALB. xxxxxxxxx de Fecha 14/03/2025 &rarr; 14/03/2025 [FECHA]


### ENTIDAD: 4. EAN

Descripción:
- Código de barras del producto.

Instrucciones:
- Generalmente es una secuencia de 13 dígitos.
- En ocasiones este dato puede no aparecer en el texto. Si no aparece, anótalo como valor nulo.

Ejemplos:
- ALFPCK283 30,00 ONE PIECE - Pck Mug320ml + Acryl® + Postcards "Luffy"* <ins>3665361131908</ins> 12,49 € 50,0% 6,25 € 187,35 &rarr; 3665361131908 [EAN]
- <ins>0889698679268</ins> 215924 : ATTACK ON TITAN S5 - POP Animation N° 1321 - Eren Jeager MIX FIG 36 - 5.40 194.40 CEE &rarr; 0889698679268 [EAN]
- <ins>8713439246186</ins> PVP 9,90 &rarr; 8713439246186 [EAN]
- <ins>9788467926552</ins> MAN 00012699 EL BARRIO DE LA LUZ 2 8,50 8,17 40,00 % 4,00 9,80 &rarr; 9788467926552 [EAN]
- 22020053 <ins>0849803076160</ins> HARRY POTTER - POP KEYCHAIN HARRY POTTER 3,0 7,4000€ 44 4,14€ 12,43€ &rarr; 0849803076160 [EAN]


### ENTIDAD: 5. SKU

Descripción:
- Número de identificación interna del producto.

Instrucciones:
- Puede aparecer en distintos formatos. Generalmente es una secuencia alfanumérica.
- En ocasiones este dato puede no aparecer en el texto. Si no aparece, anótalo como valor nulo.

Ejemplos:
- <ins>ALFPCK283</ins> 30,00 ONE PIECE - Pck Mug320ml + Acryl® + Postcards "Luffy"* 3665361131908 12,49 € 50,0% 6,25 € 187,35 &rarr; ALFPCK283 [SKU]
- 0889698679268 <ins>215924</ins> : ATTACK ON TITAN S5 - POP Animation N° 1321 - Eren Jeager MIX FIG 36 5.40 194.40 CEE &rarr; 215924 [SKU]
- 1 <ins>CR2383</ins> Stranger Things Bolso Logo 5 0,104 kg 4,48 € 6,00 % 4,21 € 21,06 € &rarr; CR2383 [SKU]
- 9788467926552 <ins>MAN 00012699</ins> EL BARRIO DE LA LUZ 2 8,50 8,17 40,00 % 4,00 9,80 &rarr; MAN 00012699 [SKU]
- <ins>22020053</ins> 0849803076160 HARRY POTTER - POP KEYCHAIN HARRY POTTER 3,0 7,4000€ 44 4,14€ 12,43€ &rarr; 22020053 [SKU]


### ENTIDAD: 6. NOMBRE_PRODUCTO

Descripción:
Nombre completo del producto.

Instrucciones:
- Debes incluir el nombre completo del producto. En ocasiones puede ser muy largo e incluir detalles del empaquetado.

Ejemplos:
ALFPCK283 30,00 <ins>ONE PIECE - Pck Mug320ml + Acryl® + Postcards "Luffy"* </ins> 3665361131908 12,49 € 50,0% 6,25 € 187,35 &rarr; ONE PIECE - Pck Mug320ml + Acryl® + Postcards "Luffy"* [NOMBRE_PRODUCTO]
0889698679268 215924 : <ins>ATTACK ON TITAN S5 - POP Animation N° 1321 - Eren Jeager MIX FIG</ins> 36 5.40 194.40 CEE &rarr; ATTACK ON TITAN S5 - POP Animation N° 1321 - Eren Jeager MIX FIG [NOMBRE_PRODUCTO]
1 CR2383 <ins>Stranger Things Bolso Logo</ins> 5 0,104 kg 4,48 € 6,00 % 4,21 € 21,06 € &rarr; Stranger Things Bolso Logo [NOMBRE_PRODUCTO]
<ins>TRUST RATON GXT105X IZZA</ins> 10 5,77 € 57,70 € 21% 12,12 € &rarr; TRUST RATON GXT105X IZZA [NOMBRE_PRODUCTO]
9788467926552 MAN 00012699 <ins>EL BARRIO DE LA LUZ</ins> 2 8,50 8,17 40,00 % 4,00 9,80 &rarr; EL BARRIO DE LA LUZ [NOMBRE_PRODUCTO]
22020053 0849803076160 <ins>HARRY POTTER - POP KEYCHAIN HARRY POTTER</ins> 3,0 7,4000€ 44 4,14€ 12,43€ &rarr; HARRY POTTER - POP KEYCHAIN HARRY POTTER [NOMBRE_PRODUCTO]


### ENTIDAD: 7. CANTIDAD

Descripción:
- Cantidad de unidades del producto.

Instrucciones:
- Debes almacenar la cantidad como un número entero. Ejemplo: 3,0 &rarr; 3

Ejemplos:
- ALFPCK283 <ins>30</ins>,00 ONE PIECE - Pck Mug320ml + Acryl® + Postcards "Luffy"* 3665361131908 12,49 € 50,0% 6,25 € 187,35 &rarr; 30 [CANTIDAD]
- 0889698679268 215924 : ATTACK ON TITAN S5 - POP Animation N° 1321 - Eren Jeager MIX FIG <ins>36</ins> 5.40 194.40 CEE &rarr; 36 [CANTIDAD]
- 1 CR2383 Stranger Things Bolso Logo <ins>5</ins> 0,104 kg 4,48 € 6,00 % 4,21 € 21,06 € &rarr; 5 [CANTIDAD]
- TRUST RATON GXT105X IZZA <ins>10</ins> 5,77 € 57,70 € 21% 12,12 € &rarr; 10 [CANTIDAD]
- 9788467926552 MAN 00012699 EL BARRIO DE LA LUZ <ins>2</ins> 8,50 8,17 40,00 % 4,00 9,80 &rarr; 2 [CANTIDAD]
- 22020053 0849803076160 HARRY POTTER - POP KEYCHAIN HARRY POTTER <ins>3,0</ins> 7,4000€ 44 4,14€ 12,43€ &rarr; 3,0 [CANTIDAD]


### ENTIDAD: 8. PRECIO_COSTE_UNIDAD

Descripción:
- Precio de coste unitario del producto.

Instrucciones:
- Debes anotar el precio de coste por unidad como valor decimal, separado por un punto.

Ejemplos:
- ALFPCK283 30,00 ONE PIECE - Pck Mug320ml + Acryl® + Postcards "Luffy"* 3665361131908 12,49 € 50,0% <ins>6,25</ins> € 187,35 &rarr; 6,25 [PRECIO_COSTE_UNIDAD]</br>
- 0889698679268 215924 : ATTACK ON TITAN S5 - POP Animation N° 1321 - Eren Jeager MIX FIG 36 <ins>5.40</ins> 194.40 CEE &rarr; 5.40 [PRECIO_COSTE_UNIDAD]</br>
- 1 CR2383 Stranger Things Bolso Logo 5 0,104 kg 4,48 € 6,00 % <ins>4,21</ins> € 21,06 € &rarr; 4,21 [PRECIO_COSTE_UNIDAD]</br>
- TRUST RATON GXT105X IZZA 10 <ins>5,77</ins> € 57,70 € 21% 12,12 € &rarr; 5,77 [PRECIO_COSTE_UNIDAD]</br>
- 9788467926552 MAN 00012699 EL BARRIO DE LA LUZ 2 8,50 8,17 40,00 % 4,00 <ins>9,80</ins> &rarr; 9,80 [PRECIO_COSTE_UNIDAD] (Éste es el formato de Épsilon. IMPORTANTE: en Épsilon, el PRECIO_COSTE_UNIDAD SIEMPRE es el último dato de la fila)</br>
- 22020053 0849803076160 HARRY POTTER - POP KEYCHAIN HARRY POTTER 3,0 7,4000€ 44 <ins>4,14</ins>€ 12,43€ &rarr; 4,14 [PRECIO_COSTE_UNIDAD]</br>
