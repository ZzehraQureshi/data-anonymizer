import pandas as pd
from strategies.differential_privacy import apply_differential_privacy
from strategies.k_anonymity import apply_k_anonymity

def main():
    file_path = input("Enter path to CSV file: ")
    df = pd.read_csv(file_path)

    print("\n📊 Columns in dataset:", list(df.columns))

    # Numerical columns and epsilon
    num_cols = input("Enter numerical columns (comma-separated): ").split(',')
    epsilons = [float(e) for e in input("Enter corresponding epsilon values (comma-separated): ").split(',')]

    for col, eps in zip(num_cols, epsilons):
        df[col] = apply_differential_privacy(df[col].astype(float), eps)

    # String columns and strategies
    str_cols = input("Enter string columns (comma-separated): ").split(',')
    strategies = input("Enter corresponding strategies (suppress, generalize, synthetic): ").split(',')

    for col, strat in zip(str_cols, strategies):
        df = apply_k_anonymity(df, col.strip(), strat.strip())

    output_path = input("Enter output CSV filename: ")
    df.to_csv(output_path, index=False)
    print(f"\n✅ Anonymized data saved to: {output_path}")

if __name__ == "__main__":
    main()
