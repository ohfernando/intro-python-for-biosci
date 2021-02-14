#from ete3 import NCBITaxa
import sys
import taxopy
#from taxonomy_ranks import TaxonomyRanks
#try:
    #ncbi = NCBITaxa()
    #ncbi.update_taxonomy_database()
#except:
#    print('ncbi error')


def getlin(org):
    rank_taxon = TaxonomyRanks(org)
    a=rank_taxon.get_lineage_taxids_and_taxanames()
    print(a)


def printfunc(x,a):
    print(x + ' is ' +a[x])

def finalout(d,orgid):
    list1=['family','order','genus']
    print(orgid + ":")
    for i in list1:
        print(str(i) + "-" + str(d[i]))
    

try:
    taxdb = taxopy.TaxDb(nodes_dp="taxdb/nodes.dmp", names_dmp="taxdb/names.dmp", keep_files=True)
except:
    #try:
    taxdb = taxopy.TaxDb()
    #except:
        #print('taxopy error, try again!')

#taxaidfile=open(sys.argv[1],"r")
#for line in taxaidfile:
 #   stringoftaxids=str(line)
#taxaids=stringoftaxids.split()
taxaids=['3702','3712']


org1= taxopy.Taxon(taxaids[0], taxdb)
org2 = taxopy.Taxon(taxaids[1], taxdb)
print(str(taxopy.find_lca([org1, org2], taxdb)) + ' is LCA')
org1dict=org1.rank_name_dictionary
org2dict=org2.rank_name_dictionary
finalout(org1dict,taxaids[0])
finalout(org2dict,taxaids[1])
