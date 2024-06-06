def acomodar(lista:list[str]) -> list[str]:
    res:list[str] = [];
    lla:list[str] = [];
    up:list[str] = [];

    for element in lista:
        if (element == "LLA"):
            lla.append(element);
        elif (element == "UP"):
            up.append(element);
    
    for element in up:
        res.append(element);
    for element in lla:
        res.append(element);
    return res;


#print(acomodar(["LLA", "UP", "LLA", "LLA", "UP"]))



## 2) Posición umbral [2 puntos] ##

def pos_umbral(s:list[int], umbral:int) -> int:
    res:int = -1;
    acumulacion: int = 0;

    for i in range(len(s)):
        if (s[i] > 0 and acumulacion <= umbral):
            acumulacion += s[i];

            if (acumulacion > umbral):
                res = i;
    return res;

#print(pos_umbral([1,-2,0,5,-7,3], 5));


## 3) Columnas repetidas [3 puntos] ##
def columnas_repetidas(matriz:list[list[int]]) -> bool:
    long_matriz:int = len(matriz[0]) / 2;
    res:bool = True;

    for fila in matriz:
        primera_mitad:list[int] = [];
        segunda_mitad:list[int] = [];
        for i in range(len(fila)):
            if (i < long_matriz):
                primera_mitad.append(fila[i]);
            else:
                segunda_mitad.append(fila[i]);

        if (primera_mitad != segunda_mitad):
            res = False;
    return res;

#print(columnas_repetidas([[1,4,1,4],[-5,6,-5,6],[0,1,0,1]]));


## 4) Rugby 4 naciones [3 puntos] ##

def posiciones_por_nacion(naciones:list[str], torneos:dict[int,list[str]]) -> dict[str,list[int]]:
    res:dict[str,list[int]] = {};

    for year, paises in torneos.items():
        for i in range(len(paises)):
            if not paises[i] in res.keys():
                res[paises[i]] = [0,0,0,0]
            res[paises[i]][i] = 1;
    return res;

naciones= ["arg", "aus", "nz", "sud"]
torneos= {2023:["nz", "sud", "arg", "aus"],
                 2022:["nz", "sud", "aus", "arg"]}
#se debería devolver res = {"arg": [0,0,1,1], "aus": [0,0,1,1], "nz": [2,0,0,0], "sud": [0,2,0,0]}

print(posiciones_por_nacion(naciones, torneos));