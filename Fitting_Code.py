import lmfit
import numpy as np
import matplotlib.pyplot as plt

class Fitting:
    
    '''
    Deve ser definida uma função (a que se deseja realizar o fitting)
    e executar o comando 'Fitting(model)'
    
    model -> função com a qual se deseja realizar o fitting
    
    OBS. A função deve ser criada na forma func(x,a,b,c,...)
    OBRIGATORIAMENTE sendo x sua primeira variável e correspondente
    aos valores do eixo X
    '''
    
    def __init__(self, model):
        self.model = model
        
    '''
    Ao se executar a instância Fitting.fit(), devem ser incluidos os dados em
    que se deseja realizar o curve fitting (eixos X e Y), bem como os
    valores iniciais para os parâmetros cujos valores serão encontrados
    
    x -> dados do eixo X (list, numpy array, etc)
    y -> dados do eixo Y (list, numpy array, etc)
    **kwargs -> valores iniciais para os parâmetros a serem encontrados
    
    OBS. A função .fit() retorna ainda os valores encontrados para os
    parâmetros após o fitting
    '''
    
    def fit(self, x, y, **kwargs):
        model = lmfit.Model(self.model)
        params = model.make_params(**kwargs)
        result = model.fit(y, params, x=x)
        self.result_ = result
        return result.params
    
    '''
    A instância Fitting.plot() deve ser executada após a instância Fitting.fit(), isto é,
    será retornado o gráfico com os dados dos eixos X e Y, bem como a curva ajustada em 
    cima desses valores
    
    x -> dados do eixo X (list, numpy array, etc)
    y -> dados do eixo Y (list, numpy array, etc)
    
    Os demais argumentos têm configurações 'default' e não precisam ser
    definidos obrigatoriamente
    
    xlabel -> título do eixo X (string); default: 'None'
    ylabel -> título do eixo Y (string); default: 'None'
    title -> título no topo do gráfico (string); default: 'None'
    data_label -> nome na legenda para os dados (string); default: 'Data'
    color_data -> cor da curva dos dados (string); default: 'blue'
    color_fitting -> cor da curva de fitting (string); default: 'red'
    figsize -> tamanho da figura do gráfico (tuple); defaut: (8,5)
    grid -> aparecimento das grades no gráfico (boolean); default: False
    '''
    
    def plot(self, x, y, xlabel=None, ylabel=None, title=None, data_label = 'Data', color_data='blue',
             color_fitting='red',figsize=(8,5), grid=False):
        plt.rcParams['axes.facecolor'] = 'white'
        plt.figure(figsize=figsize)
        plt.plot(x,y, color=color_data, label=data_label, linewidth=1.5)
        plt.plot(x, self.result_.best_fit, c=color_fitting, label='Curve Fitting',linewidth=1.5)
        plt.plot([],[],' ',label=f'R² = {np.round(self.result_.rsquared,5)}')
        plt.plot([],[],' ',label=f'Chi² = {np.round(self.result_.chisqr,5)}')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(grid)
        plt.legend(loc='best',fontsize=10)
        
    '''
    A instância Fitting.scatter() deve ser executada após a instância Fitting.fit(),
    isto é, será retornado o gráfico de scatter (dos pontos)com os dados dos eixos X e Y,
    bem como a curva ajustada em cima desses valores
    
    x -> dados do eixo X (list, numpy array, etc)
    y -> dados do eixo Y (list, numpy array, etc)
    
    Os demais argumentos têm configurações 'default' e não precisam ser
    definidos obrigatoriamente
    
    xerr -> erro para os pontos em X (float, array, etc); default: 'None'
    yerr -> erro para os pontos em Y (float, array, etc); default: 'None'
    xlabel -> título do eixo X (string); default: 'None'
    ylabel -> título do eixo Y (string); default: 'None'
    title -> título no topo do gráfico (string); default: 'None'
    data_label -> nome na legenda para os dados (string); default: 'Data'
    edgecolor_data -> cor da borda dos pontos (string); default: 'blue'
    facecolor_data -> cor do interior dos pontos (string); default: 'cornflowerblue'
    color_fitting -> cor da curva de fitting (string); default: 'red'
    figsize -> tamanho da figura do gráfico (tuple); defaut: (8,5)
    grid -> aparecimento das grades no gráfico (boolean); default: False
    '''
        
    def scatter(self, x, y, xerr=None, yerr=None, xlabel=None, ylabel=None, title=None, data_label='Data', edgecolor_data='blue',
                facecolor_data = 'cornflowerblue', color_fitting='red', figsize=(8,5),grid=False):
        
        plt.rcParams['axes.facecolor'] = 'white'
        plt.figure(figsize=figsize)
        plt.scatter(x,y,s=50, alpha=0.8, marker='o', edgecolor=edgecolor_data, 
                    label=data_label, facecolors=facecolor_data,linewidths=1.4)
        plt.plot(x, self.result_.best_fit, c=color_fitting, label='Curve Fitting',linewidth=1.5)
        plt.errorbar(x,y,xerr=xerr,yerr=yerr,capsize=2.2,fmt=' ',ecolor='black',elinewidth=1)
        plt.plot([],[],' ',label=f'R² = {np.round(self.result_.rsquared,5)}')
        plt.plot([],[],' ',label=f'Chi² = {np.round(self.result_.chisqr,5)}')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(grid)
        plt.legend(loc='best',fontsize=10)
        
    '''
    a instância Fitting.get_params() deve ser executada após o Fitting.fit(), uma vez
    que esta retornará os resultados obtidos para os parâmetros estimados, bem como o
    erro associado a eles
    
    parametro -> parâmetro que se deseja obter o valor (string); default: 'None'
    
    OBS. Se o parâmetro não for especificado, a função retornará o resultado para
    todos os parâmetros calculados
    '''
        
    def get_params(self,parametro=None):
        resultado = self.result_
        if parametro == None:
            return resultado.params

        else:
            return resultado.params[parametro].value

    '''
    a instância Fitting.result() deve ser executada após o Fitting.fit(), uma vez
    que esta retornará os resultados obtidos para os parâmetros estimados de maneira
    mais completa, incluindo variáveis estatísticas quanto aos dados analisados
    
    Não apresenta nenhum parâmetro
    '''

        
    def result(self):
        resultado = self.result_
        return resultado
    
    '''
    A instância Fitting.conc() serve para obter a concordância de um determinado valor
    encontrado em relação a um determinado valor conhecido
    
    x_exp -> valor encontrado
    x_teorico -> valor conhecido
    '''
    
    def conc(self, x_exp, x_teorico):
        return 1 - abs(x_teorico - x_exp)/x_teorico