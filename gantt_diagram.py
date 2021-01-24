import matplotlib.pyplot as plt
from datetime import datetime, timedelta
plt.style.use('seaborn')

taches = [
'Avoir l\'approbation\n de l\'université​',
'Réaliser un formulaire\n pour avoir l\'avis\n des étudiant',
'Acheter les droits \net tester le matériel \nde diffusion',
'Réservation de \nl’amphithéâtre et des \nterrains de foot​',
'Acquérir le materiel\n necessaire au \ntournoi e-sport',
'Promotion de \nl’événement',
'Système de génération\n et vérification de tickets \n(Système Code QR)​',
'Vente des tickets ',
'Trouver un sponsors',]

letters = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi','Dimanche']

fig, ax = plt.subplots(figsize=(13,6))

predecessors = [('',1),('A',1),('A',2),('A',1),('A,D',2),('A,C',4),('A',2),('C,D,G',4),('A',6)]
start_date = datetime(2020, 2, 23)

start = 0
predecessors_start = []
x_ticks = [start]
xtick_labels = [days[start_date.weekday()]+'({}, {}, {})'.format(start_date.day, start_date.month, start_date.year)]
number_activities= len(predecessors)
for i in range(number_activities):
    number_i_letters = len(predecessors[i][0])
    if number_i_letters==0:
        current_task_start = start
    elif number_i_letters==1:
        predecessor_index = letters.index(predecessors[i][0])
        predecessor_periode = predecessors[predecessor_index][1]
        predecessor_start = predecessors_start[predecessor_index] #assuming that it exists
        current_task_start = predecessor_start + predecessor_periode
    else:
        all_predecessors = predecessors[i][0] #'B,D', 'A,F'
        long_periode = 0
        for k in range(len(all_predecessors)):
            if k%2==0:
                potential_predecessor_index = letters.index(all_predecessors[k]) #getting the index of letter 'B' and 'D'
                if predecessors[potential_predecessor_index][1]+predecessors_start[potential_predecessor_index] > long_periode:
                    long_periode = predecessors[potential_predecessor_index][1]+predecessors_start[potential_predecessor_index]

        current_task_start = long_periode

    
    ax.broken_barh([(current_task_start, predecessors[i][1])], (i,1), facecolors='tab:blue')
    final_date = start_date + timedelta(days=current_task_start+predecessors[i][1])
    rest_in_date = final_date - datetime.now()
    predecessors_start.append(current_task_start)
    x_ticks.append(current_task_start+predecessors[i][1])
    xlabel_text = days[final_date.weekday()]+'({}, {}, {})'.format(final_date.day, final_date.month, final_date.year)
    xtick_labels.append(xlabel_text)

    print('i:', i, predecessors_start)




ax.set_xticks(x_ticks)
ax.set_xticklabels(xtick_labels, rotation=7)

ax.set_yticks([i for i in range(0, number_activities+1)]) #10 //////
ytick_labels = ['{}({}js)'.format(taches[i], predecessors[i][1]) for i in range(number_activities) ] #letters[i] <-> taches[i]
ax.set_yticklabels(ytick_labels, va="top")#, rotation=-45)
ax.grid(True)
ax.xaxis.tick_top()
ax.invert_yaxis()
ax.set(title='Diagramme De GANTT')
plt.show()
