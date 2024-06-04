import pyautogui as posicaoMouse
import pyautogui as tempoEspera

tempoEspera.sleep(5)
print(posicaoMouse.position())

#move ao menu
posicaoMouse.moveTo(x=192, y=860)
#clica no menu
posicaoMouse.click(x=192, y=860)

posicaoMouse.moveTo(x=688, y=36)
posicaoMouse.click(x=688, y=36)
#escreve no campo
posicaoMouse.typewrite('calc')

#move e abr a calculadora
posicaoMouse.moveTo(x=729, y=96)
tempoEspera.sleep(2)
posicaoMouse.click(x=729, y=96)