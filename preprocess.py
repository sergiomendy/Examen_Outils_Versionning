import argparse
import pandas as pd
import warnings


warnings.filterwarnings("ignore")


def main(input_file, output_file):
    data = pd.read_csv(input_file)
    data.dropna(inplace=True)
    data.to_csv(output_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prétraitement de données")
    parser.add_argument("--input_file", type=str, help="Chemin vers le fichier d'entrée")
    parser.add_argument("--output_file", type=str, help="Chemin vers le fichier de sortie pour le dataset")

    args = parser.parse_args()
    main(args.input_file, args.output_file)
