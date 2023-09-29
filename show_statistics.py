import argparse
import pandas as pd
import warnings


warnings.filterwarnings("ignore")


def main(input_file):
    data = pd.read_csv(input_file) 
    summary_stats = data.describe()
    print(summary_stats)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Affichage des statistiques sommaires")
    parser.add_argument("--input_file", type=str, help="Chemin vers le fichier d'entrée")

    args = parser.parse_args()
    main(args.input_file)
