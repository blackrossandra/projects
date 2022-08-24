Dim Message, Speak  
do  
Message = "En Pep Gonella te un ca de bou. El va baratar amb un ou de xoriguer. El va dar an es porquer de son Caliu. que era somo mes viu de dins son Serra. sabia tocar guitarra i castanyetes, i feia ballar pessetes dins un garbell. Somo de na portell era un cabrit, se va tallar un dit, fent un llaut. El va curar es puput felanitxer, que feia de barber davant can Pau. El tio Nicolau va matar sase, li va clavar sespasa arran des cul."
Set Speak=CreateObject("sapi.spvoice")  
Speak.Speak Message 
loop