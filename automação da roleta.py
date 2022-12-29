#função de clicar em numero especifico da mesa de uma roleta

import pyautogui
import time
#Clicar 16 vezes em cada numero vermelho ( 0 ao 30)

pyautogui.click(74,476,duration=0.1)
'''1'''pyautogui.click(121,514,duration=0.1)
'''3'''pyautogui.click(121,444,duration=0.1)
'''5'''pyautogui.click(171,482,duration=0.1)
pyautogui.click(214,511,duration=0.1)
pyautogui.click(216,446,duration=0.1)
pyautogui.click(267,445,duration=0.1)
pyautogui.click(316,478,duration=0.1)
pyautogui.click(361,445,duration=0.1)
pyautogui.click(362,512,duration=0.1)
pyautogui.click(408,513,duration=0.1)
pyautogui.click(406,447,duration=0.1)
pyautogui.click(453,482,duration=0.1)
pyautogui.click(506,514,duration=0.1)
pyautogui.click(502,446,duration=0.1)
'''32'''pyautogui.click(599,480,duration=0.1)
'''34'''pyautogui.click(646,446,duration=0.1)
'''36'''pyautogui.click(644,514,duration=0.1)

#Clicar 16 vezes no preto

c = 0
for c in range(0,16): 
    pyautogui.click(433,575,duration=0.1)      
print('fim')
