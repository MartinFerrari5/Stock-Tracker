# <h1 style="text-align:center">Stock Tracker</h1>

<div style="height:50vh;" align='center'><img src="https://wealthface.com/blog/wp-content/uploads/2022/08/Blog-1-1.png"></div>
</div>

## Tabla de contenido
1. [Contexto](#-contexto)
2. [Herramientas y Librerias Utilizadas](#-herramientas-y-librerias-utilizadas)
3. [Estuctura del Proyecto](#-estructura-del-proyecto)
4. [Instrucciones](#-instrucciones)
5. [Pagina Web](#pagina-web) 
6. [Autor](#-autor) 

## 📖 Contexto

<div>En esta oportunidad, presento una pagina para visualizar las acciones donde se podrá:
    <li>Filtrar hasta 3 acciones a la vez</li>
    <li>Observar su desempeño a lo largo de: un dia, una semana, un año o 5 años</li>
    <li>Consultar las empresas disponibles</li>
<div>



## ⚙️ Herramientas y Librerias Utilizadas
Para el siguiente proyecto se hizo uso de las siguientes herramientas y librerias (el conocimiento sobre los mismos no require de un nivel avanzado para el entendimiento del proyecto):
1. ***Python***
2. ***Manejo de dataframes con `pandas`***
3. ***Creacion de pagina con `streamlit`***
4. ***Obtencion de datos de las acciones `yfinance`***


## 📁 Estructura del proyecto

-   *Stock-Tracker/* <br>
    ├── `Inicio.py`: Archivo que contiene el codigo de inicio de la pagina <br>
    ├── `pages/`: Carpeta que contiene las paginas del proyecto <br>
    │    └── `Acciones.py`: Archivo que contiene el codigo para consultar las empresas disponibles <br>
    ├── `datasets/` <br>
    │   └── `companies.csv`: Archivo estatico con los nombres de las acciones<br>
    ├── `functions` <br>
    │     └── `stock_functions.py`: Archivo con las funciones utilizadas en todos el programa <br>
    └── `README.md`: Documentacion del proyecto <br>

## 🖊️ Instrucciones

#### 1) Clona el repositorio:
```
git clone https://github.com/MartinFerrari5/Stock-Tracker.git
```

- Es recomendado usar un entorno virtual (venv):
### Crea entorno virtual.
```bash
python -m venv environment_name
```

- Activar: <br>

 ``Windows``: venv\Scripts\activate

 ``Mac/Linux``: venv/bin/activate

#### 2) Instalar librerias.
```bash
python -m pip install -r requirements.txt
```
#### 3) En la terminal ejecute.
```bash
streamlit run Inicio.py
```

## Pagina Web
- Puedes ver la pagina en el siguiente <a href='https://stock-tracker-aprmcywjeq.streamlit.app/Acciones'>enlace </a>

## 👤 Autor
Este proyecto fue realizado por Martin Ferrari. Muchas gracias a todos por leer, no dudes en contactarme a mi <a href="https://www.linkedin.com/in/martin-ferrari-bb0547219/">LinkedIn</a> ante cualquier duda.