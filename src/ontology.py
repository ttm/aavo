import nltk
import percolation as p

skos = p.rdf.ns.skos
owl = p.rdf.ns.owl
rdf = p.rdf.ns.rdf
rdfs = p.rdf.ns.rdfs
aao = p.rdf.ns.aao # Audiovisual Analytics Ontology
aav = p.rdf.ds.aav # Audiovisual Analytics Vocabulary
po = p.rdf.ns.po # Participation Ontology

           (aav.AudiovisualAnalytics, skos.note, "All concepts and skos "
           "relations are derived automatically from Audiovisual"
           "Analytics Ontology: " + aao),
           ("Audiovisual Analytics Ontology", a, skos.Concept),
           (aao.AudiovisualAnalytics, a, owl.Ontolgy),
]

def makeLabels(triples):
    """Make labels to properties and classes from their names
    
    ToDo:
    Strings are not allowed in the subject (first element of each triple).
    To the first step is to write them as camelCase with the prefix.
    so for classes and properties without labels,
    use the xx.CamelCase (class) and xx.headlessCamelCase
    # if triple[0] == str: # for allowing strings to classes and properties
    # if triple does not have a label property
    for triple in triples:
        # get last name (after last /) of URI,
        # make word for each uppercase letter on to last lower case
        # for both subject and predicate.
        # For object if URI.
        # Exclude URIs that has skos, owl, rdf and other known
        # namespaces

        
    return) and 
    """

# RDF uses pointers as standars # a=1; b=a; b=2; a==2
# So we dont distinguish the reference names and ponters
rdfDeque = [ ()


triples = [
    (aao.Deque, owl.note, "labels: deque, doubly linked queue, double queue"), #  will be processed as (pref)(alt)labels for skos. 
    (aao.Deque, aav.rdfImplentation, rdfDeque)
]




