





# Correct columns dtype ----------------------------------------

#-------- contract_df --------
contract_df['begin_date'] = pd.to_datetime(contract_df['begin_date'])
#contract_df['end_date'] = pd.to_datetime(contract_df['end_date'])
contract_df = pd.get_dummies(contract_df, columns=['type'], prefix='type', drop_first=True)
contract_df = pd.get_dummies(contract_df, columns=['paperless_billing'], prefix='paperless_billing', drop_first=True)
contract_df = pd.get_dummies(contract_df, columns=['payment_method'], prefix='payment_method', drop_first=True)
contract_df['total_charges'] = pd.to_numeric(contract_df['total_charges'], errors='coerce')
contract_df.info()

#-------- internet_df --------
cols_to_encode = [col for col in internet_df.columns if col not in ['customer_id']]
internet_df = pd.get_dummies(internet_df, columns=cols_to_encode, drop_first=True)