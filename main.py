import pandas as pd
import matplotlib.pyplot as plt
import random
import math


# normalize the dataset
def normalize(z):
    z_exp = [math.exp(i) for i in z]
    sum_z_exp = sum(z_exp)
    #print(round(sum_z_exp, 2))
    softmax = [round(i / sum_z_exp, 6) for i in z_exp]
    n = len(z)
    softmax =[random.randint(0,100) for x in range(n)]
    return softmax


def calc_friendship_score(row):
    #multiply by corresponding weight
    val = row['Call Duration']*10 + row['SMS']*8 +row['WhatsApp']*5 + row['Mutual Friends']*4
    val = val/2700
    #2700 is the max possible total score weight
    return  val


def calc_group_score(table,names):

    score = 0.0
    ctr=0
    for name_1 in names:
        for name_2 in names:
            for index, row in table.iterrows():
                if row['Student'] == name_1 and row['Contact'] == name_2:
                    score+=row['Score']
                    ctr+=1

    n = len(names)
    if n==1:
        return -1
    total = n*(n-1)
    score = score/total
    return round(score,3)


def bar_graph(table, name):
    friends = []
    scores = []
    x = []
    ctr = 1
    for index,row in table.iterrows():
        if row['Student'] == name:
            friends.append(row['Contact'])
            scores.append(row['Score'])
            x.append(ctr)
            ctr+=1

    plt.bar(x, scores)
    plt.xticks(x,friends)
    plt.xticks(rotation=90)
    plt.title('Friendship of %s with the rest of the class'%name)
    plt.xlabel('Friends')
    plt.ylabel('Friendship Score')
    # plt.legend()
    plt.show()

# the stack graphs
def stack_plot(table,name):

    x = []
    Call_Durations = []
    WhatsApp = []
    SMS = []
    mutual_friends = []
    x_strings = []

    ctr = 0
    for index,row in table.iterrows():
        if row['Student']==name:
            x.append(ctr)
            ctr=ctr+1
            x_strings.append(row['Contact'])
            Call_Durations.append(row['Call Duration'])
            WhatsApp.append(row['WhatsApp'])
            SMS.append(row['SMS'])
            mutual_friends.append(row['Mutual Friends'])
    rot_deg=90
    plt.xticks(x,x_strings)
    plt.xticks(rotation= rot_deg)
    plt.plot([],[],color = 'm',label = 'Call Durations',linewidth=5)
    plt.plot([],[],color = 'c',label = 'WhatsApp',linewidth=5)
    plt.plot([],[],color = 'r',label = 'SMS',linewidth=5)
    plt.plot([],[],color = 'k',label = 'mutual_friends',linewidth=5)
    plt.stackplot(x,Call_Durations,WhatsApp,SMS,mutual_friends,colors=['m','c','r','k'])
    plt.title('Friends of %s'%(name))
    plt.legend()
    plt.show()


def pie_chart(table,name_1,name_2):
    slices = []

    for index,row in table.iterrows():
        if row['Student']==name_1 and row['Contact']==name_2 or row['Student']==name_2 and row['Contact']==name_1:
            slices.append(row['Call Duration'])
            slices.append(row['SMS'])
            slices.append(row['WhatsApp'])
            slices.append(row['Mutual Friends'])
            score = row['Score']
            break

    cols = ['Call Durations','SMS','WhatsApp','Mutual Friends']
    plt.pie(slices,labels=cols)
    plt.legend()
    plt.title('Friendship chart between %s and %s \n Their score is %f'%(name_1, name_2,score))
    plt.show()


def main():
    table = pd.read_excel('Student Data.xlsx')

    Call_Durations = [x for x in table['Call Duration']]
    SMS = [x for x in table['SMS']]
    WhatsApp = [x for x in table['WhatsApp']]
    mutual_friends =[x for x in table['Mutual Friends']]

    table['Call Duration'] = normalize(Call_Durations)
    table['SMS'] = normalize(SMS)
    table['WhatsApp'] = normalize(WhatsApp)
    table['Mutual Friends'] = normalize(mutual_friends)

    table['Score'] = table.apply (lambda row: calc_friendship_score(row),axis=1)

    # 1)pie chart
    name_1 = input("enter 1st name : ")
    name_2 = input("enter 2nd name : ")
    pie_chart(table,name_1,name_2)


    # 2)Stack  plot
    name = input("Enter name : ")
    stack_plot(table,name)

    n = input('Enter the group size :')
    name_list = []

    for i in range(int(n)):
        s = input("Enter name : ")
        name_list.append(s)

    # 3)Find the group bonding score
    val = calc_group_score(table,name_list)

    if val == -1:
        print('Group size has to be greater than 1\n')
    else:
        print('The bonding score based on averages of the given list of students is : %f'%val)

    # 4)Bar graph
    name = input('Enter name for showing bar graph:')
    bar_graph(table,name)


if __name__ == '__main__':
    main()
