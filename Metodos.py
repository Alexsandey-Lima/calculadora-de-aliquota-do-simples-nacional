import pandas as pd
import Metodos
def Anexo(Anexos):
 for i in range (5):
    if (Anexos[4] == True):
        Anexos[4] = 'V'
        continue
    if (Anexos[3] == True):
        Anexos[3] = 'IV'
        continue
    if (Anexos[2] == True):
        Anexos[2] = 'III'
    if (Anexos[1] == True):
        Anexos[1] = 'II'
        continue
    if (Anexos[0] == True):
        Anexos[0] = 'I'

        continue

    return Anexos

def Faixa(RBT12):
    if ( RBT12>=0 ) and ( RBT12 <= 180000 ):
        faixa = 0
        return (faixa)
    elif( RBT12>=180000.01 ) and ( RBT12 <= 360000 ):
        faixa = 1
        return (faixa)
    elif ( RBT12 >= 360000.01 ) and ( RBT12 <= 720000 ):
        faixa = 2
        return (faixa)
    elif( RBT12>= 720000.01 ) and ( RBT12 <= 1800000 ):
        faixa = 3
        return (faixa)
    elif( RBT12 >= 1800000.01 ) and ( RBT12 <= 3600000 ):
        faixa = 4
        return (faixa)
    elif( RBT12 >= 3600000.01 ) and ( RBT12 <= 4800000 ):
        faixa = 5
        return (faixa)
    elif( RBT12 > 4800000 ):
        print('Contribuinte ultapassou o limite de faturamento anual para o simples nacional')
    else :
        print('Valor invalido tente novamente')

def Leitor(Anexo,coluna,Faixa):
    if Anexo == 'I' or Anexo == 'II' or Anexo == 'III' or Anexo == 'IV' or Anexo == 'V':
        tabela = pd.read_excel(f'Anexo{Anexo}.xlsx')
        return (tabela.iloc[Faixa,coluna])


def Dados(RBT12, Anexo):
    "DECLARAÇÃO DE VARIAVEIS"

    Faixa = Metodos.Faixa(RBT12)
    Aliquota_nominal = Metodos.Leitor(Anexo, 1, Faixa)
    Parcela_deduzir = Metodos.Leitor(Anexo, 2, Faixa)
    percentual_reparticao_CSLL = Metodos.Leitor(Anexo, 5, Faixa)
    percentual_reparticao_IRPJ = Metodos.Leitor(Anexo, 6, Faixa)
    percentual_reparticao_Cofins = Metodos.Leitor(Anexo, 7, Faixa)
    percentual_reparticao_PIS_PASEP = Metodos.Leitor(Anexo, 8, Faixa)
    percentual_reparticao_CPP = 0
    percentual_reparticao_ISS = 0
    percentual_reparticao_IPI= 0
    percentual_reparticao_ICMS = 0
    Aliquota_efetiva = Metodos.Calcular_Aliquota_efetiva(RBT12, Aliquota_nominal, Parcela_deduzir)
    Aliquota_ISS_arredondada = 0
    Aliquota_CPP_arredondada = 0
    Aliquota_IPI_arredondada = 0
    Aliquota_ICMS_arredondada = 0
    Aliquota_CSLL_arredondada = Metodos.Calcular_Aliquota_CSLL(Aliquota_efetiva, percentual_reparticao_CSLL)
    Aliquota_IRPJ_arredondada = Metodos.Calcular_Aliquota_IRPJ(Aliquota_efetiva, percentual_reparticao_IRPJ)
    Aliquota_Cofins_arredondada = Metodos.Calcular_Aliquota_Cofins(Aliquota_efetiva, percentual_reparticao_Cofins)
    Aliquota_PIS_PASEP_arredondada = Metodos.Calcular_Aliquota_PIS_PASEP(Aliquota_efetiva,percentual_reparticao_PIS_PASEP)

    "TRATAMENTO POR ANEXO"

    if (Anexo == 'IV' or Anexo == 'V'):
        if (Faixa == 5):
            Aliquota_ISS_arredondada = 0.05
        else:
             percentual_reparticao_ISS = Metodos.Leitor(Anexo, 4, Faixa)
             Aliquota_ISS_arredondada = Metodos.Calcular_Aliquota_ISS(Aliquota_efetiva, percentual_reparticao_ISS)
        return (Faixa, Aliquota_nominal, Parcela_deduzir ,percentual_reparticao_ISS ,
                percentual_reparticao_CSLL, percentual_reparticao_IRPJ,percentual_reparticao_Cofins,
                percentual_reparticao_PIS_PASEP,percentual_reparticao_CPP,percentual_reparticao_IPI,percentual_reparticao_ICMS,Aliquota_efetiva,
                Aliquota_ISS_arredondada,Aliquota_CSLL_arredondada,Aliquota_IRPJ_arredondada,
                 Aliquota_Cofins_arredondada,Aliquota_PIS_PASEP_arredondada,Aliquota_CPP_arredondada,
                Aliquota_IPI_arredondada,Aliquota_ICMS_arredondada)
    if (Anexo == 'III'):

        percentual_reparticao_ISS = Metodos.Leitor(Anexo, 4, Faixa)
        Aliquota_ISS_arredondada = Metodos.Calcular_Aliquota_ISS(Aliquota_efetiva, percentual_reparticao_ISS)
        percentual_reparticao_CPP = Metodos.Leitor(Anexo, 9, Faixa)
        Aliquota_CPP_arredondada = Metodos.Calcular_Aliquota_CPP(Aliquota_efetiva, percentual_reparticao_CPP)

        return (Faixa, Aliquota_nominal, Parcela_deduzir ,percentual_reparticao_ISS ,
                percentual_reparticao_CSLL, percentual_reparticao_IRPJ,percentual_reparticao_Cofins,
                percentual_reparticao_PIS_PASEP,percentual_reparticao_CPP,percentual_reparticao_IPI,percentual_reparticao_ICMS,Aliquota_efetiva,
                Aliquota_ISS_arredondada,Aliquota_CSLL_arredondada,Aliquota_IRPJ_arredondada,
                 Aliquota_Cofins_arredondada,Aliquota_PIS_PASEP_arredondada,Aliquota_CPP_arredondada,
                Aliquota_IPI_arredondada,Aliquota_ICMS_arredondada)

    if (Anexo == 'I'):
        percentual_reparticao_ICMS = Metodos.Leitor(Anexo, 4, Faixa)
        Aliquota_ICMS_arredondada = Metodos.Calcular_Aliquota_ICMS(Aliquota_efetiva, percentual_reparticao_ICMS)
        return (Faixa, Aliquota_nominal, Parcela_deduzir ,percentual_reparticao_ISS ,
                percentual_reparticao_CSLL, percentual_reparticao_IRPJ,percentual_reparticao_Cofins,
                percentual_reparticao_PIS_PASEP,percentual_reparticao_CPP,percentual_reparticao_IPI,percentual_reparticao_ICMS,Aliquota_efetiva,
                Aliquota_ISS_arredondada,Aliquota_CSLL_arredondada,Aliquota_IRPJ_arredondada,
                 Aliquota_Cofins_arredondada,Aliquota_PIS_PASEP_arredondada,Aliquota_CPP_arredondada,
                Aliquota_IPI_arredondada,Aliquota_ICMS_arredondada)
    if (Anexo == 'II'):
        percentual_reparticao_ICMS = Metodos.Leitor(Anexo, 4, Faixa)
        Aliquota_ICMS_arredondada = Metodos.Calcular_Aliquota_ICMS(Aliquota_efetiva, percentual_reparticao_ICMS)

        percentual_reparticao_CPP = Metodos.Leitor(Anexo, 9, Faixa)
        Aliquota_CPP_arredondada = Metodos.Calcular_Aliquota_CPP(Aliquota_efetiva,percentual_reparticao_CPP)
        percentual_reparticao_IPI = Metodos.Leitor(Anexo, 10, Faixa)
        Aliquota_IPI_arredondada = Metodos.Calcular_Aliquota_IPI(Aliquota_efetiva, percentual_reparticao_IPI)

        return (Faixa, Aliquota_nominal, Parcela_deduzir ,percentual_reparticao_ISS ,
                percentual_reparticao_CSLL, percentual_reparticao_IRPJ,percentual_reparticao_Cofins,
                percentual_reparticao_PIS_PASEP,percentual_reparticao_CPP,percentual_reparticao_IPI,percentual_reparticao_ICMS,Aliquota_efetiva,
                Aliquota_ISS_arredondada,Aliquota_CSLL_arredondada,Aliquota_IRPJ_arredondada,
                 Aliquota_Cofins_arredondada,Aliquota_PIS_PASEP_arredondada,Aliquota_CPP_arredondada,
                Aliquota_IPI_arredondada,Aliquota_ICMS_arredondada)

def Calcular_Aliquota_efetiva(RBT12,Aliquota_nominal,Parcela_deduzir):
    Aliquota_efetiva = float(((( RBT12 * Aliquota_nominal )- Parcela_deduzir ) / RBT12 )*100)
    return (Aliquota_efetiva)
def Calcular_Aliquota_ISS(Aliquota_efetiva,percentual_reparticao_ISS ):
    Aliquota_ISS = float((percentual_reparticao_ISS * Aliquota_efetiva))
    Aliquota_ISS_arredondada = round(Aliquota_ISS, 5)
    Diferença_Aliquota_ISS = 0
    if(Aliquota_ISS_arredondada>5):
        Aliquota_ISS_MAX = 5
        Diferença_Aliquota_ISS = Aliquota_ISS_arredondada - Aliquota_ISS_MAX
        Aliquota_ISS_arredondada = Aliquota_ISS_MAX
    return (Aliquota_ISS_arredondada)
def Calcular_Aliquota_CSLL(Aliquota_efetiva,percentual_reparticao_CSLL ):
    Aliquota_CSLL = float((percentual_reparticao_CSLL * Aliquota_efetiva))
    Aliquota_CSLL_arredondada = round(Aliquota_CSLL, 5)
    return (Aliquota_CSLL_arredondada)
def Calcular_Aliquota_IRPJ(Aliquota_efetiva,percentual_reparticao_IRPJ ):
    Aliquota_IRPJ = float((percentual_reparticao_IRPJ * Aliquota_efetiva))
    Aliquota_IRPJ_arredondada = round(Aliquota_IRPJ, 5)
    return (Aliquota_IRPJ_arredondada)
def Calcular_Aliquota_Cofins(Aliquota_efetiva,percentual_reparticao_Cofins ):
    Aliquota_Cofins = float((percentual_reparticao_Cofins * Aliquota_efetiva))
    Aliquota_Cofins_arredondada = round(Aliquota_Cofins, 5)
    return (Aliquota_Cofins_arredondada)
def Calcular_Aliquota_PIS_PASEP(Aliquota_efetiva,percentual_reparticao_PIS_PASEP ):
    Aliquota_PIS_PASEP = float((percentual_reparticao_PIS_PASEP * Aliquota_efetiva))
    Aliquota_PIS_PASEP_arredondada = round(Aliquota_PIS_PASEP, 5)
    return (Aliquota_PIS_PASEP_arredondada)
def Calcular_Aliquota_CPP(Aliquota_efetiva,percentual_reparticao_CPP):
    Aliquota_CPP = float((percentual_reparticao_CPP * Aliquota_efetiva))
    Aliquota_CPP_arredondada = round(Aliquota_CPP, 5)
    return (Aliquota_CPP_arredondada)
def Calcular_Aliquota_ICMS(Aliquota_efetiva,percentual_reparticao_ICMS):
    Aliquota_ICMS = float((percentual_reparticao_ICMS * Aliquota_efetiva))
    Aliquota_ICMS_arredondada = round(Aliquota_ICMS, 5)
    return (Aliquota_ICMS_arredondada)
def Calcular_Aliquota_IPI(Aliquota_efetiva,percentual_reparticao_IPI ):
    Aliquota_IPI = float((percentual_reparticao_IPI * Aliquota_efetiva))
    Aliquota_IPI_arredondada = round(Aliquota_IPI, 5)
    return (Aliquota_IPI_arredondada)

def Exibir(RBT12, Anexo, Faixa, Aliquota_nominal,Parcela_deduzir,percentual_reparticao_ISS,
           percentual_reparticao_CSLL,percentual_reparticao_IRPJ,percentual_reparticao_Cofins,
           percentual_reparticao_PIS_PASEP,percentual_reparticao_CPP,percentual_reparticao_IPI,percentual_reparticao_ICMS,Aliquota_efetiva,
           Aliquota_ISS_arredondada,Aliquota_CSLL_arredondada,Aliquota_IRPJ_arredondada,Aliquota_Cofins_arredondada,
           Aliquota_PIS_PASEP_arredondada,Aliquota_CPP_arredondada,Aliquota_IPI_arredondada,Aliquota_ICMS_arredondada):

    memoria_de_calculo = True
    print(rf''' ======================================================================================
    Informações do mês
        O faturamento dos ultimos 12 meses foi de:  {RBT12}
        Anexo : {Anexo}
    ======================================================================================
Informações da receita Federal com base no faturamento e na atividade da empresa :
    
        Faixa : {Faixa + 1}º
        Alíquota nominal: {Aliquota_nominal}
        Parcela à deduzir: {Parcela_deduzir}
        Percentual de repartição do CSLL: {percentual_reparticao_CSLL*100}%
        Percentual de repartição do IRPJ: {percentual_reparticao_IRPJ*100}%
        Percentual de repartição do Cofins: {percentual_reparticao_Cofins*100}%
        Percentual de repartição do PIS/PASEP: {percentual_reparticao_PIS_PASEP*100}%''')
    if(Anexo == 'IV' or Anexo == 'V'):
        print(rf'''===========================================================================================
       
        Alíquotas
        Aliquota efetiva : {Aliquota_efetiva}%
        Aliquota do ISS: {Aliquota_ISS_arredondada}%
        Aliquota do CSLL: {Aliquota_CSLL_arredondada}% 
        Aliquota do IRPJ: {Aliquota_IRPJ_arredondada}% 
        Aliquota do Cofins: {Aliquota_Cofins_arredondada}% 
        Aliquota do PIS/PASEP: {Aliquota_PIS_PASEP_arredondada}%''')
    if (Anexo == 'III'):
       print(rf'''        Percentual de repartição do ISS: {percentual_reparticao_ISS*100}%
        Percentual de repartição do CPP: {percentual_reparticao_CPP*100}%
       
       ===========================================================================================
       
       Alíquotas
       Aliquota efetiva : {Aliquota_efetiva}%
       Aliquota do ISS: {Aliquota_ISS_arredondada}%
       Aliquota do CSLL: {Aliquota_CSLL_arredondada}% 
       Aliquota do IRPJ: {Aliquota_IRPJ_arredondada}% 
       Aliquota do Cofins: {Aliquota_Cofins_arredondada}% 
       Aliquota do PIS/PASEP: {Aliquota_PIS_PASEP_arredondada}% 
       Aliquota do CPP: {Aliquota_CPP_arredondada}%''')
    if (Anexo == 'II'):
        print(rf'''        Percentual de repartição do ICMS: {percentual_reparticao_ICMS*100}%
        Percentual de repartição do IPI: {percentual_reparticao_IPI*100}%
        ===========================================================================================
        
        Alíquotas
               Aliquota efetiva : {Aliquota_efetiva}%
               Aliquota do CSLL: {Aliquota_CSLL_arredondada}% 
               Aliquota do IRPJ: {Aliquota_IRPJ_arredondada}% 
               Aliquota do Cofins: {Aliquota_Cofins_arredondada}% 
               Aliquota do PIS/PASEP: {Aliquota_PIS_PASEP_arredondada}% 
               Aliquota do IPI: {Aliquota_IPI_arredondada}%
               Aliquota do ICMS: {Aliquota_ICMS_arredondada}%''')
    if (Anexo == 'I'):
        print(rf'''        Percentual de repartição do ICMS: {percentual_reparticao_ICMS*100}%
        ===========================================================================================
        
        Alíquotas
               Aliquota efetiva : {Aliquota_efetiva}%
               Aliquota do CSLL: {Aliquota_CSLL_arredondada}% 
               Aliquota do IRPJ: {Aliquota_IRPJ_arredondada}% 
               Aliquota do Cofins: {Aliquota_Cofins_arredondada}% 
               Aliquota do PIS/PASEP: {Aliquota_PIS_PASEP_arredondada}% 
               Aliquota do ICMS: {Aliquota_ICMS_arredondada}%''')

''' print(rf
    Memoria de calculo
    
    Alíquota efetiva = (( Receita Bruta dos últimos 12 meses * Alíquota nominal )- Parcela deduzir ) / RBT12 )*100
    
    Alíquota efetiva = (( {RBT12} * {Aliquota_nominal} )- {Parcela_deduzir} ) / {RBT12} )*100
    Alíquota efetiva = {Aliquota_efetiva}%
    
    Alíquota do ISS = (Alíquota efetiva * Percentual de repartição do ISS) * 100
    Alíquota do ISS = ({percentual_reparticao_ISS} * {Aliquota_efetiva})*100
    Alíquota do ISS =  {Aliquota_ISS_arredondada}%
    
    Alíquota da CSLL = (Alíquota efetiva * Percentual de repartição da CSLL) * 100
    Alíquota da CSLL = ({percentual_reparticao_CSLL} * {Aliquota_efetiva})*100
    Alíquota da CSLL = {Aliquota_CSLL_arredondada}%
    
    Alíquota do IRPJ = (Alíquota efetiva * Percentual de repartição do IRPJ) * 100
    Alíquota do IRPJ = ({percentual_reparticao_IRPJ} * {Aliquota_efetiva})*100
    Alíquota do IRPJ = {Aliquota_IRPJ_arredondada}%
    
    Alíquota da COFINS = (Alíquota efetiva * Percentual de repartição da COFINS) * 100
    Alíquota da COFINS = ({percentual_reparticao_Cofins} * {Aliquota_efetiva})*100
    Alíquota da COFINS = {Aliquota_Cofins_arredondada}%
    
    Alíquota do PIS ou PASEP = (Alíquota efetiva * Percentual de repartição do PIS ou PASEP) * 100
    Alíquota do PIS ou PASEP = ({percentual_reparticao_PIS_PASEP} * {Aliquota_efetiva})*100
    Alíquota do PIS ou PASEP = {Aliquota_PIS_PASEP_arredondada}%
    
    Alíquota do CPP = (Alíquota efetiva * Percentual de repartição do CPP) * 100
    Alíquota do CPP = ({percentual_reparticao_CPP} * {Aliquota_efetiva})*100
    Alíquota do CPP = {Aliquota_CPP_arredondada}%
    
    Alíquota do IPI = (Alíquota efetiva * Percentual de repartição do IPI) * 100
    Alíquota do IPI = ({percentual_reparticao_IPI} * {Aliquota_efetiva})*100
    Alíquota do IPI = {Aliquota_IPI_arredondada}%
    
    Alíquota do ICMS = (Alíquota efetiva * Percentual de repartição do ICMS) * 100
    Alíquota do ICMS = ({percentual_reparticao_ICMS} * {Aliquota_efetiva})*100
    Alíquota do ICMS = {Aliquota_ICMS_arredondada}%
===============================================================================================
)'''
