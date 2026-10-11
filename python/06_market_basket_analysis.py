# Market Basket Analysis using Association Rules (Apriori)
# In Colab: !pip install -q mlxtend   (usually already installed)
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

data = {'Tea':      [1, 1, 0, 1, 1, 1],
        'Sugar':    [1, 1, 1, 0, 1, 1],
        'Biscuits': [0, 1, 1, 1, 0, 1]}
df = pd.DataFrame(data)
print("Shopping Transactions:")
print(df)

frequent_items = apriori(df.astype(bool), min_support=0.5, use_colnames=True)
print("\nFrequent Itemsets:")
print(frequent_items)

rules = association_rules(frequent_items, metric="confidence", min_threshold=0.6,
                          num_itemsets=len(df))
print("\nAssociation Rules:")
if rules.empty:
    print("No association rules found.")
else:
    print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
