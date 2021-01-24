import pandas as pd
import altair as alt
from PIL import Image
import streamlit as st

#################################################
# Page Title
#################################################

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

#################################################
# Input Text Box
#################################################

st.header('Enter DNA sequence')

sequence_input = """GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG
ATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC
TGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"""

sequence = st.text_area("Sequence_input", "".join(sequence_input.splitlines()), height=150)

st.write("""
***
""")

## Prints the input DNA sequencce
st.header('INPUT (DNA Query)')
sequence_input

DNA_NUCLEOTIDES = dict(A="adenie (A)",
                       T="thymin (T)",
                       G="guanine (G)",
                       C="cytosine (C)")

## DNA nucleotide count
st.header('Output (DNA Nucleotide Count)')

### 1. Print drictionary
st.subheader('1 Print dictionary')
def DNA_nucleotide_count(seq):
    seq = "".join(seq.splitlines()) if "\n" in seq else seq
    return dict([
        (key, seq.count(key))
        for key in sorted(set(seq))
    ])

X = DNA_nucleotide_count(sequence)
X

### 2. Print text
st.subheader('2. Print text')
for dna_nucleotide, count in X.items():
    st.write(f"There're {count} {DNA_NUCLEOTIDES[dna_nucleotide]}")

### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'counts'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotides'})
st.write(df)

### 4. Display Bar Char using Altair
st.subheader('4. Display Bar Char')
p = alt.Chart(df).mark_bar().encode(
    x="nucleotides",
    y="counts"
).properties(
    width=alt.Step(80) # controls width of bar.
)
st.write(p)