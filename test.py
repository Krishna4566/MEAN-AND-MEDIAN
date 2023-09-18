import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt


xy = [
    ["Ut-1",99,90,100],
    ["Ut-2",100,100,100],
      ]

collabel = [x[0] for x in xy]
header = ["exam","english","science","math",]
y_offset = np.zeros(len(header[1:]))
text = []
for i in range(len(xy)):
    text.append([x for x in y_offset])
text.reverse()

fig, ax =plt.subplots(1,1)
ax.axis('tight')
ax.axis('off')

the_table = plt.table(cellText=text,
                      rowLabels=collabel,
                      colLabels=header[1:],
                      loc='best'
)

plt.savefig("output.jpeg")