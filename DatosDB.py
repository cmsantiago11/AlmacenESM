import sqlite3


# Conectar a la base de datos (o crearla si no existe)

def ConsultarDiametrosUnicos():
    conn = sqlite3.connect('ESM_DB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Diametros FROM AlmacenESM")
    diametro_unicos = sorted([row[0] for row in cursor.fetchall()])
    conn.close()

    return diametro_unicos

def ConsultarLargosUnicos():
    conn = sqlite3.connect('ESM_DB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT largos FROM AlmacenESM")
    largos_unicos = sorted([row[0] for row in cursor.fetchall()])
    conn.close()

    return largos_unicos

def ConsultarTiposDeTornillos():
    conn = sqlite3.connect('ESM_DB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Tipodetornillo FROM AlmacenESM")
    tiposDeTornillo = sorted([row[0] for row in cursor.fetchall()])
    conn.close()

    return tiposDeTornillo

def ConsultarTiposDeCabeza():
    conn = sqlite3.connect('ESM_DB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Cabezadetornillo FROM AlmacenESM")
    cabezaDeTornillo = sorted([row[0] for row in cursor.fetchall()])
    conn.close()

    return cabezaDeTornillo

def ConsultarMaterial():
    conn = sqlite3.connect('ESM_DB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Material FROM AlmacenESM")
    materialDeTornillo = sorted([row[0] for row in cursor.fetchall()])
    conn.close()

    return materialDeTornillo

def ConsultarRosca():
    conn = sqlite3.connect('ESM_DB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT TipoDeRosca FROM AlmacenESM")
    roscaDeTornillo = sorted([row[0] for row in cursor.fetchall()])
    conn.close()

    return roscaDeTornillo

def ConsultarTornillo(tor):
    conn = sqlite3.connect('ESM_DB.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT SAP_CODE FROM AlmacenESM  WHERE New_Name='{tor}'")
    busqueda =[row for row in cursor.fetchall()]
    conn.close()
    if len(busqueda)>0:
        return f"El tornillo existe con el código SAP: {busqueda[0][0]}"
    else:
        return "El tornillo que buscas no existe en la base de datos"
 
