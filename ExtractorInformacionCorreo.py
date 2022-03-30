dominios_populares = {"gmail":"Google","hotmail":"Microsoft","yahoo":"Yahoo","outlook":"Microsoft"}

usuario_correo = input("Ingrese su correo electrónico: ")

correo = usuario_correo.split("@")  #correo = [username, gmail.com]

nombre_usuario = correo[0]

dominio_correo = correo[1].split(".") #dominio_correo = [gmail, com]

dominio = dominio_correo[0]

if dominio in dominios_populares.keys():
    print(f"Hola {nombre_usuario}, tu dominio de correo es {dominio} que está registrado en {dominios_populares[dominio]}.")
else:
    print(f"Hola {nombre_usuario}, tu dominio de correo personalizado es {dominio}.")