import sys


def read_data(input_file):
    with open("dane/" + input_file) as in_file:
        data = in_file.read().splitlines()
    return data

def clean_data(data):
    cleaned_emails = set()
    for email in data:
        if email.count("@") == 1:
            cleaned_emails.add(email.strip().lower())

    # cleaned_emails = list(cleaned_emails)
    # cleaned_emails.sort()
    # return cleaned_emails
    return sorted(cleaned_emails)


def save_data(output_file, cleaned_emails):
    with open("wyniki/"+output_file, "w") as f:
        for email in cleaned_emails:
            f.write(email + "\n")

def main():
    try:
        input_file = sys.argv[1]
    except IndexError:
        input_file = None

    try:
        output_file = sys.argv[2]
    except IndexError:
        output_file = None

    if input_file and output_file:
        data = read_data(input_file)
        data = clean_data(data)
        save_data(output_file, data)

print(__name__)

if __name__ == "__main__":
    main()