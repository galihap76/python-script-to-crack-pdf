import pikepdf, argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--crack', type=str, help='to crack PDF')
args = parser.parse_args()

passwords = [ line.strip() for line in open("wordlist.txt") ]

if args.crack:
    for password in tqdm(passwords, 'Crack PDF'):
        try:
            with pikepdf.open(args.crack, password=password) as pdf:
                print(' [+] Password found :', password)
                break
        except pikepdf._qpdf.PasswordError as e:
            continue