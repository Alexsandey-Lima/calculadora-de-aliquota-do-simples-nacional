from PySimpleGUI import PySimpleGUI as sg
import Processador as pc
import Metodos
#Layout
class Interface():
    try:
        def __init__(self):
            sg.theme('Reddit')
            Layout = [
                [sg.Text('RBT12:', size=(6,1)), sg.Input(key='RBT12', size=(20,3))],
                [sg.Text('Para qual anexo deseja calcular?')],
                [sg.Checkbox('Anexo I',key = 'AnexoI'),sg.Checkbox('Anexo II',key = 'AnexoII'),sg.Checkbox('Anexo III',key = 'AnexoIII'),sg.Checkbox('Anexo IV',key = 'AnexoIV'),sg.Checkbox('Anexo V',key = 'AnexoV')],
                [sg.Button('Calcular')],
                [sg.Output(size=(100,60))]
            ]


            #Janela
            self.janela = sg.Window('Informando dados',size = (800,500)).layout(Layout)


            #Ler dados


        def iniciar(self):

            while True:
                # Extrair dados
                self.button, self.values = self.janela.Read()
                RBT12 = float(self.values['RBT12'])
                Anexos= [self.values['AnexoI'],self.values['AnexoII'], self.values['AnexoIII'],self.values['AnexoIV'],self.values['AnexoV']]
                anexo = Metodos.Anexo(Anexos)
                for i in range(5):
                    if (anexo[i - 1] == 'I' or anexo[i - 1] == 'II' or anexo[i - 1] == 'III' or anexo[i - 1] == 'IV' or anexo[i - 1] == 'V'):
                        pc.Processador(RBT12, anexo[i - 1])
                    elif (anexo[i] == False):
                        continue



                    for i in range(3):
                        if (anexo[i-1] == 'III' or anexo[i-1] == 'IV' or anexo[i-1] == 'V' ):
                            pc.Processador(RBT12, anexo[i-1])
                        elif (anexo[i] == False):
                          continue

    except:
        print('Erro: entre em contato com o administrador')


interface = Interface()
interface.iniciar()
