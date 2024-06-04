import pyautogui as position

position.sleep(2)
#Consultar position
print(position.position())

#Abrindo icone
position.moveTo(x=363, y=869)
position.rightClick(x=363, y=869)

#Abrindo guia separada do navegador
position.moveTo(x=387, y=664)
position.click(x=387, y=664)

position.moveTo(x=218, y=88)
position.click(x=218, y=88)
position.typewrite('valor atual do dolar')
#pressionar tecla
position.press('enter')