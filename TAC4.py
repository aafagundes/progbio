
#  1-  Escreva um programa Python que peça ao usuário uma sequência de DNA e imprima a sequência de mRNA e a sequência de proteína correspondentes
stringSeq=input('Digite uma sequencia de DNA').upper()
sequencia=Seq(stringSeq)

rna=sequencia.transcribe()
print(f'O mRNA da sequencia é:{rna}')

proteinas=rna.translate()
print(f'A sequencia de proteinas é: {proteinas}')












#   3-   Considerando o arquivo FASTA sequenciaDesconhecida.fasta, faça um código em Python que:
# Lê do usuário o caminho para o arquivo FASTA sequenciaDesconhecida.fasta;


arquivo = input('Digite o caminho do arquivo fasta:')

# Lê do usuário o caminho para o arquivo multi-fasta de proteínas de Trypanosoma cruzi cepa CL Brener Esmeraldo-like
# TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta;
baseDeDados = input('Digite o caminho para o arquivo multi-fasta:')

meuOutput = "output.csv"
# Executa BLAST da sequência desconhecida de DNA contra as sequências de aminoácidos usando
# formato de saída nº 6 e e-valor igual à 0,05

blastx_path = "C:\\Program Files\\NCBI\\blast-2.11.0+\\bin\\blastx"

linha_de_comando_blastx = NcbiblastxCommandline(query=arquivo,  ## o que quero buscar
                                                subject=baseDeDados,  ##  onde quero buscar
                                                outfmt=6,  ## formato do arquivo de saida
                                                out=meuOutput,  ## arquivo de saida
                                                evalue=0.05,  ## e-valor
                                                cmd=blastx_path)  ## caminho para o executável
print("Executando busca local:")

stdout, stderr = linha_de_comando_blastx()
comCabeçalho = pd.read_csv(meuOutput,sep='\t',names=["Seq_ID",
                                        "Amno_ID",
                                        "pident",
                                        "length",
                                        "mismatch",
                                        "gapopen",
                                        "qstart",
                                        "qend",
                                        "sstart",
                                        "send",
                                        "E-value",
                                        "Bitscore"])

print("Fim da busca local...")

# Abrindo o arquivo de output que armazena o resultado
blast_result = open(meuOutput, "r")

maiorScore= comCabeçalho['Bitscore'].max()

print('Somente o hit com o maior score: %.2f' %(maiorScore))


