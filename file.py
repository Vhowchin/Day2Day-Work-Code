import pandas as pd
from tqdm import tqdm

input_path = r""
output_path = r""

df = pd.read_csv(input_path, sep=';', encoding='utf-8-sig', engine='python', on_bad_lines='skip')
df.columns = df.columns.str.strip()

article_counts = df['articles'].value_counts()

tqdm.pandas(desc="Counting occurrences")

df['Count'] = df['articles'].progress_apply(lambda x: article_counts.get(x, 0))

df_unique = df.drop_duplicates(subset='articles', keep='first')

df_unique.to_csv(output_path, index=False, encoding='utf-8-sig')

print("Done")
