import pandas as pd

dataframe = pd.read_csv("data/wars.csv")
data_specific = dataframe.drop(columns = ["TransFrom", "TransTo", "WhereFought", "WarNum", "WarType", "ccode", "StartMonth1", "StartDay1", "StartYear2", "EndMonth1", "EndDay1", "StartMonth2", "StartDay2", "EndMonth2", "EndDay2", "EndYear2", "Version", "Initiator"])
data_specific = data_specific.rename(columns={"StartYear1": "StartYear", "EndYear1": "EndYear"})
print(data_specific.head())

result = data_specific.groupby(['WarName', 'Side']).agg(
    StartYear=('StartYear', 'min'),
    EndYear=('EndYear', 'max'),
    StateName=('StateName', list),
    BatDeath = ('BatDeath', 'sum')
).reset_index()

data = [
    ["Gaza-Israel conflict", "Israel", 1, 2006, -7, 42763],
    ["Gaza-Israel conflict", "Palestine", 2, 2006, -7, 42763],
    ["Russo-Georgian War", ['Russia', 'South Ossetia', 'Abkhazia'], 1, 2008, 2008, 734],
    ["Russo-Georgian War", "Georgia", 2, 2008, 2008, 734],
    ["2011 military intervention in Libya Part of the First Libyan Civil War", ['NATO', 'Qatar', 'Sweden', 'United Arab Emirates'], 1, 2011, 2011, 238],
    ["2011 military intervention in Libya Part of the First Libyan Civil War", "Libya", 2, 2011, 2011, 238],
    ["Heglig Crisis", "Sudan", 1, 2012, 2012, 900],
    ["Heglig Crisis", "South Sudan", 2, 2012, 2012, 900]
]
print(result.columns)
df_new = pd.DataFrame(data, columns=result.columns)
final_df = pd.concat([result, df_new], ignore_index=True)
final_df = final_df[final_df["StartYear"] >= 1894]
print(final_df)
print(final_df.tail())

final_df.set_index("WarName", inplace=True)
counts = []
for war in final_df.index:
    start_year = final_df.loc[war, "StartYear"].min()
    end_year = final_df.loc[war, "EndYear"].max()
    print(start_year, end_year)
    movies_war = data[data['Year'].between(start_year-2, end_year+2)]
    print(f"Movies about {war}: {len(movies_war)}")
    counts.append(len(movies_war))
final_df["Movies"] = counts
final_df=final_df[final_df["Movies"]>500]
data = pd.read_csv("data/movies_with_summaries.csv")

print(final_df.tail())
print(final_df.shape)
