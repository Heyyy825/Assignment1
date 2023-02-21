import pandas as pd


def clean(contact_info_file, other_info_file, ):
    contact_info_file = pd.read_csv(contact_info_file)
    other_info_file = pd.read_csv(other_info_file)

    respondent = pd.merge(contact_info_file, other_info_file, left_on="respondent_id", right_on="id")
    respondent.drop("id", axis=1, inplace=True)
    respondent.dropna(inplace=True)
    respondent = respondent[~(respondent.job.str.contains("insurance|Insurance"))]

    print(respondent.shape)

    return respondent


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Path")
    parser.add_argument('contact_info_file', help='The path to the respondent_contact.csv file')
    parser.add_argument('other_info_file', help='The path to the respondent_other.csv file')
    parser.add_argument('output_file', help='The path to the output file', default="")

    args = parser.parse_args()

    cleaned = clean(args.contact_info_file, args.other_info_file)

    cleaned.to_csv(args.output_file)