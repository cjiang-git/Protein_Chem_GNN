# Define the files
file1="/farmshare/user_data/khoang99/cs224w/chemical_of_interest.txt"
file2="/farmshare/user_data/khoang99/cs224w/chemicals.v5.0.tsv"

# Use grep to search for each chemical in file1 within file2
grep -F -f "$file1" "$file2" > "/farmshare/user_data/khoang99/cs224w/chemicals.v5.0.filtered.tsv"