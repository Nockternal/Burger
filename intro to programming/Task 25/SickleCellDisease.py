origin_file = "DNA.txt"         # t
mute_file = "mutatedDNA.txt"    # u
normal_file = "normalDNA.txt"   # v
mute_orgin = "a"                # w
mute_new = "T"                  # x
norm_orginal = "a"              # y
norm_new = "A"                  # z
outputlist = []
sequence = []
aminos = {
"I":("ATT","ATC","ATA"),
"L":("CTT","CTC","CTA","CTG","TTA","TTG"),
"V":("GTT","GTC","GTA","GTG"),
"F":("TTT","TTC"),
"M":("ATG"),
"C":("TGT","TGC"),
"A":("GCT","GCC","GCA","GCG"),
"G":("GGT","GGC","GGA","GGG"),
"P":("CCT","CCC","CCA","CCG"),
"T":("ACT","ACC","ACA","ACG"),
"S":("TCT","TCC","TCA","TCG","AGT","AGC"),
"Y":("TAT","TAC"),
"W":("TGG"),
"Q":("CAA","CAG"),
"N":("AAT","AAC"),
"H":("CAT","CAC"),
"E":("GAA","GAG"),
"D":("GAT","GAC"),
"K":("AAA","AAG"),
"R":("CGT","CGC","CGA","CGG","AGA","AGG")
}

def split_by_n( seq, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]


def translate(f):
    def compare():
        for i in sequence:
            if ("ATT") == i:
                outputlist.append("I")
            elif ("ATC") == i:
                outputlist.append("I")
            elif ("ATA") == i:
                outputlist.append("I")

            elif ("CTT") == i:
                outputlist.append("L")
            elif ("CTC") == i:
                outputlist.append("L")
            elif ("CTA") == i:
                outputlist.append("L")
            elif ("CTG") == i:
                outputlist.append("L")
            elif ("TTA") == i:
                outputlist.append("L")
            elif ("TTG") == i:
                outputlist.append("L")

            elif ("GTT") == i:
                outputlist.append("V")
            elif ("GTC") == i:
                outputlist.append("V")
            elif ("GTA") == i:
                outputlist.append("V")
            elif ("GTG") == i:
                outputlist.append("V")

            elif ("TTT") == i:
                outputlist.append("F")
            elif ("TTC") == i:
                outputlist.append("F")

            elif ("ATG") == i:
                outputlist.append("M")

            elif ("TGT") == i:
                outputlist.append("C")
            elif ("TGC") == i:
                outputlist.append("C")

            elif ("GCT") == i:
                outputlist.append("A")
            elif ("GCC") == i:
                outputlist.append("A")
            elif ("GCA") == i:
                outputlist.append("A")
            elif ("GCG") == i:
                outputlist.append("A")

            elif ("GGT") == i:
                outputlist.append("G")
            elif ("GGC") == i:
                outputlist.append("G")
            elif ("GGA") == i:
                outputlist.append("G")
            elif ("GGG") == i:
                outputlist.append("G")

            elif ("CCT") == i:
                outputlist.append("P")
            elif ("CCC") == i:
                outputlist.append("P")
            elif ("CCA") == i:
                outputlist.append("P")
            elif ("CCG") == i:
                outputlist.append("P")

            elif ("ACT") == i:
                outputlist.append("T")
            elif ("ACC") == i:
                outputlist.append("T")
            elif ("ACA") == i:
                outputlist.append("T")
            elif ("ACG") == i:
                outputlist.append("T")

            elif ("TCT") == i:
                outputlist.append("S")
            elif ("TCC") == i:
                outputlist.append("S")
            elif ("TCA") == i:
                outputlist.append("S")
            elif ("TCG") == i:
                outputlist.append("S")
            elif ("AGT") == i:
                outputlist.append("S")
            elif ("AGC") == i:
                outputlist.append("S")

            elif ("TAT") == i:
                outputlist.append("Y")
            elif ("TAC") == i:
                outputlist.append("Y")

            elif ("TGG") == i:
                outputlist.append("W")

            elif ("CAA") == i:
                outputlist.append("Q")
            elif ("CAG") == i:
                outputlist.append("Q")

            elif ("AAT") == i:
                outputlist.append("N")
            elif ("AAC") == i:
                outputlist.append("N")

            elif ("CAT") == i:
                outputlist.append("H")
            elif ("CAC") == i:
                outputlist.append("H")

            elif ("GAA") == i:
                outputlist.append("E")
            elif ("GAG") == i:
                outputlist.append("E")

            elif ("GAT" or "GAC") == i:
                outputlist.append("D")
            elif ("GAT" or "GAC") == i:
                outputlist.append("D")

            elif ("AAA") == i:
                outputlist.append("K")
            elif ("AAG") == i:
                outputlist.append("K")

            elif ("CGT") == i:
                outputlist.append("R")
            elif ("CGC") == i:
                outputlist.append("R")
            elif ("CGA") == i:
                outputlist.append("R")
            elif ("CGG") == i:
                outputlist.append("R")
            elif ("AGA") == i:
                outputlist.append("R")
            elif ("AGG") == i:
                outputlist.append("R")

            else:
                outputlist.append("X")
    with open(f,"r") as dnafile:
        fread = dnafile.read()
        sequence = list(split_by_n(fread, 3))

    compare()
    final = "".join(outputlist)
    return final

def mutate(t,u,v,w,x,y,z):
    desfnorm = open(v,"w+")
    with open(t,"r") as dnanorm:
        stringread = dnanorm.read()
        newnorm = stringread.replace(y,z)
        desfnorm.write(newnorm)
    desfnorm.close()

    desfmut = open(u, "w+")
    with open(t,"r") as dnamut:
        reader = dnamut.read()
        newmut = reader.replace(w,x)
        desfmut.write(newmut)
    desfmut.close()



mutate(origin_file,mute_file,normal_file,mute_orgin,mute_new,norm_orginal,norm_new)

print("++++++++++++++++++++++++++++++++")
print(origin_file)
print(translate(origin_file))
print("++++++++++++++++++++++++++++++++")
print(mute_file)
print(translate(mute_file))
print("++++++++++++++++++++++++++++++++")
print(normal_file)
print(translate(normal_file))
print("++++++++++++++++++++++++++++++++")

