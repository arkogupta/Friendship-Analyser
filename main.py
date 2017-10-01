import pandas as pd
import matplotlib.pyplot as plt
import math
import random


#normalize the dataset
def normalize(z):
    z_exp = [math.exp(i) for i in z]
    #print([round(i, 2) for i in z_exp])
    sum_z_exp = sum(z_exp)
    #print(round(sum_z_exp, 2))
    softmax = [round(i / sum_z_exp, 6) for i in z_exp]
    n = len(z)
    softmax =[random.randint(0,100) for x in range(n)]
    return  softmax

def calc_friendship_score(row):
    #multiply by corresponding weight
    val = row['Call']*10 + row['SMS']*8 +row['Whatsapp']*5
    val = val/2300
    #2300 is the max possible score
    return  val


#def calc_group_score():


def pie_chart():
    slices = [68,77,71]
    cols = ['calls','sms','whatsapp']
    plt.pie(slices,labels=cols)
    plt.legend()
    plt.show()

def main():
    table = pd.read_excel('Proj.xlsx')

    calls = [x for x in table['Call']]
    sms = [x for x in table['SMS']]
    whatsapp = [x for x in table['Whatsapp']]

    table['Call'] = normalize(calls)
    table['SMS'] = normalize(sms)
    table['Whatsapp'] = normalize(whatsapp)

    #print(table.head(30))
    table['Score'] = table.apply (lambda row: calc_friendship_score(row),axis=1)
    pie_chart()
    #print(table.head(30))


if __name__ == '__main__':
    main()
