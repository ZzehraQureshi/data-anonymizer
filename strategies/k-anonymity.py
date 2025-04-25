from faker import Faker

fake = Faker()

def suppress(column):
    """Replaces values with asterisks."""
    return ['*' * len(str(val)) for val in column]

def generalize(column):
    """Replaces all values with their first character + stars."""
    return [val[0] + '***' if isinstance(val, str) and len(val) > 0 else val for val in column]

def synthetic(column):
    """Replaces values with synthetic (fake) words."""
    return [fake.word() for _ in column]

def apply_k_anonymity(df, column_name, strategy):
    """Applies the selected K-anonymity strategy to the string column."""
    col = df[column_name].astype(str)
    if strategy.lower() == 'suppress':
        df[column_name] = suppress(col)
    elif strategy.lower() == 'generalize':
        df[column_name] = generalize(col)
    elif strategy.lower() == 'synthetic':
        df[column_name] = synthetic(col)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")
    return df
