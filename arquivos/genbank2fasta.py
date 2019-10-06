from Bio import SeqIO
gbk_filename = "/media/ribamar/Arquivos/cefet/arquivos/fiocruz/CCBH4851.gb"
faa_filename = "/media/ribamar/Arquivos/cefet/arquivos/fiocruz/CCBH4851_p0.fasta"
input_handle  = open(gbk_filename, "r")
output_handle = open(faa_filename, "w")

for seq_record in SeqIO.parse(input_handle, "genbank") :
    print "Dealing with GenBank record %s" % seq_record.id
    for seq_feature in seq_record.features :
        if seq_feature.type=="CDS" and str(seq_feature.qualifiers['translation'][0]).find('*')==-1:
            assert len(seq_feature.qualifiers['translation'])==1
            output_handle.write(">%s|%s|%s\n%s\n" % (
                   seq_feature.qualifiers['locus_tag'][0],
                   seq_feature.qualifiers['product'][0],
                   seq_feature.qualifiers['inference'][0],
                   seq_feature.qualifiers['translation'][0]))

output_handle.close()
input_handle.close()