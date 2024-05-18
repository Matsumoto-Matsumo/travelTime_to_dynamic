#今回使用したネットワークデータはgithubからとってきた。
#https://github.com/bstabler/TransportationNetworks/tree/master
import pandas as pd
input = "SiouxFalls_net.csv"
file_split = input.split('.')
output = file_split[0]+"_dynamic.csv"
df = pd.read_csv(input)
df2 = pd.DataFrame(columns=["orig", "dest", "toll", "trav_time","linestr"])
for i in range(len(df)):
    orig = df['A'][i]
    dest = df['B'][i]
    toll = 0
    stdtime = df['a0'][i]
    trav_time = str(stdtime) + ":" +str(stdtime)+":"+str(stdtime)+":"+str(stdtime)+":"+str(stdtime)+":"+str(stdtime)+":"+str(stdtime*1.1)+":"+str(stdtime*1.2)+":"+str(stdtime*1.3)+":"+str(stdtime*1.2)+":"+str(stdtime*1.2)+":"+str(stdtime*1.2)+":"+str(stdtime*1.2)+":"+str(stdtime*1.2)+":"+str(stdtime*1.3)+":"+str(stdtime*1.3)+":"+str(stdtime*1.3)+":"+str(stdtime*1.3)+":"+str(stdtime*1.3)+":"+str(stdtime*1.1)+":"+str(stdtime*1.1)+ ":" +str(stdtime)+ ":" +str(stdtime)+ ":" +str(stdtime)+ ":" +str(stdtime)
    df2_item= pd.Series([orig, dest, toll, trav_time,""],index=["orig", "dest", "toll", "trav_time","linestr"],name=i).to_frame().T
    df2 = pd.concat([df2, df2_item])
print(df2)
df2.to_csv(output,index=False)