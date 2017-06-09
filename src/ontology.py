import nltk
import percolation as p

skos = p.rdf.ns.skos
owl = p.rdf.ns.owl
rdf = p.rdf.ns.rdf
rdfs = p.rdf.ns.rdfs
void = p.rdf.ns.void
# http://purl.org/audiovisualanalytics/
aao = p.rdf.ns.aa # Audiovisual Analytics (Ontology and Vocabulary)
# http://purl.org/audiovisualanalytics/ontology/
aao = p.rdf.ns.aao # Audiovisual Analytics Ontology
# http://purl.org/audiovisualanalytics/vocabulary/
aav = p.rdf.ds.aav # Audiovisual Analytics Vocabulary
# http://purl.org/socialparticipation/po
po = p.rdf.ns.po # Participation Ontology

# http://purl.org/socialparticipation/ a void.DataSet
sp = p.rdf.ns.sp
# sp includes other ontologies such as sp.opa, sp.ocd, sp.ops, sp.aa, obs
# and vocabularies such as obv or derived from the ontologies
 

# ISSUES: TTM
# - When to use class and property from OWL, RDFS and RDF?
# - What really does rdf:type entails? When is the subject an instance/individual?
# - Where should void, dq and 
# - read https://www.w3.org/DesignIssues/
# - Directions on when to use new definitions or use external URIs (i.e. use the mapping based approach)? Prov-O avoids the mappeing solution to enhance precision of definitions even when concepts are potentially equivalent.
# - A graph should be described by which RDF structures?

# RECOMMENDATIONS: TTM
# - Use ACL for user authentication and I/O priviledges: https://www.w3.org/wiki/WebAccessControl
# - prov:definition for definitions on OWL which will be skos.definition
# - use prov-o for provenance of data and AA sessions: https://www.w3.org/TR/prov-o/
# - see the entought videos for analyses routines and visualizations.
# - make a chatbot for the visual analytics interface. It should:
# # * give tips on relating data, analysis, audiovisualizations and visual interfaces (with controls for settings).
# # * direct users to documentation, including (AA, SP) ontologies and vocabularies.
# # * make random associations of concepts by template sentences.
# # * keep track of users annotations and sessions.
# # * suggest interactions between users, sessions, session states, analyses, etc.
# # * make comments about the used ontological structures in current session.
# # * provide a bot-bot talk about current session or sets of sessions, about visualizations and set of visualizations etc.
# # * incorporate user vocabulary by specific commands and by means of analyzing user annotations and messages to the bot.
# # * be configurable by the user to include or exclude terms, sentence structures, sessions, etc.
# # * be mergeable, forlkable and have its state saved.
# # * be contained in a specific Python or Javascript Library (LinkedBot? AABot?)
# # * write in toki pona by means of a toki pona ontology linked to wordnet
# # * make its own AA session by means of annotated steps in using the interface.
# # * play a session (both users and bots sessions) giving comments on each step.
# # * record aa shouts and sessions inside a session.
# # * summarize conclusions that can be derived from current session
# # # - best fitted curve
# # # - is power law or not
# # # - most probable probability distribution
# # # - presence or absence of outliers
# # # - PCA dispersion concentrated in first principal components
# # # - Difference or equivalence between data units or subsets
# # # - Important visualizations and interfaces for presenting and deepening results
# # # - Other data, analyses and visualizations that can enhance results

# - Understand Pandas, Sympy and other python data-related libraries.


# - Javascript interface should focus in d3.js
# # * Limits to which d3 might be used. When should ccNetViz, bootstrap and other libraries be used?
# # * Should it be written in Meteor.js?
# # * Should AAInterface be implemented only in d3.js, with all the python backend as javascript.
# # # - https://www.npmjs.com/browse/keyword/scipy , https://www.npmjs.com/search?q=numpy do not reveal complete numpy/scipy integration
# # # - 

# - The Percolation package should download:
# # * AA library as a dependence and synthesize ontology and vocabulary
# # * Social Participation library. It should instantiate the ontology (and sub-ontologies) and vocabulary.
# # 

# - New python libraries:
# # * Article: for deriving articles from RDF text; for synthesizing (scientific, summary) articles from RDF text
# # * Audiovisual Analytics: for the synthesis of the ontology and vocabulary, for deriving relations (e.g. between Data, Analysis and Visualization)
# # * Social Participation: and umbrella void.Dataset for social participation ontologies and vocabularies in LOSD.

# - Make the Scientific Article Ontology and allow for automated writing of article sketches from RDF data.
# # * Article shoud include text, figures, references (including links to audio, video and interfaces).
# # * Article sections might be linked to specific kinds of comments. Figures should mainly be in data and methods or results and discussion sections.
# # * Which templates to use?
# # * How to decide in which section and order should a comment or a figure appear?
# # * Make also a Supporting Information document with futher texts, images, tables of links used as references with metadata. and relations between RDF resources and Article sections.
# # * Also, use sentence templates for making text from ontological relations.
# # * Derive first article for describing AA (ontology and vocabulary).

# relations between external namespaces
# are ontologies and skos vocabularies already subClasses of Dataset?
# void.Linkset
triples = [
        (void.Dataset, owl.superClassOf, owl.Ontology),
        (void.Dataset, owl.superClassOf, skos.ConceptScheme),
]

# new classes and properties for general use
# How to give precedence to a rdf.comment over other comments? TTM
# Any better way for linking resources with properties without axioms (including range and domain) and restrictions? TTM
triles = [
        (pe.possibleDomain, a, rdf.Property), # any other URI already in usage by the community?
        (pe.possibleDomain, rdf.comment, "a non-restricitve version of the rdfs.domain"),
        (pe.possibleDomain, rdf.comment, "useful for making images for the ontology and depicting the ontology"),
        (pe.recommendedDomain, owl.subPropertyOf, pe.possibleDomain),

        (pe.possibleRange, a, rdf.Property), # any other URI already in usage by the community?
        (pe.possibleRange, rdf.comment, "a non-restricitve version of the rdfs.range"),
        (pe.possibleRange, rdf.comment, "useful for making images for the ontology and depicting the ontology"),
        (pe.recommendedRange, owl.subPropertyOf, pe.possibleRange),

        (pe.possibleDomain, owl.subClassOf, pe.relatedResource), # any other URI already in usage by the community?
        (pe.possibleRange, owl.subClassOf, pe.relatedResource),
]

# preambule of the AA namespace
triples = [
           (aa, a, void.Dataset),
           (aao, a, owl.Ontolgy),
           (aav, a, skos.ConceptScheme),
           (aav, skos.note, "All concepts and skos relations are derived automatically from Audiovisual Analytics Ontology: " + aao),
           (aa, rdf.subGraph, aav),
           (aa, rdf.subGraph, aao),
           (aao, rdf.label, "Audiovisual Analytics Ontology"),
           (aav, rdf.label, "Audiovisual Analytics Vocabulary"),
           (aa, rdf.label, "Audiovisual Analytics Conceptualizations: vocabulary and ontology"),
           (po.LOSD, a, void.Dataset),
           (p.rdf.ns.AudiovisualAnalytics, a, void.Dataset), # include vocabulary and ontology
           (p.rdf.ns.AudiovisualAnalytics, rdf.comment, "The current specification does not assign a normative formal semantics. However, an intended meaning of the conceptualization is described."),
]
# use wikimedia, BabelNet, WordNet, DBPedia, Data World, LOSD

# triples defining the items in each ontology or vocabulary
triples = [
        (aao.PCA, rdfs.isDefinedBy, db),
        (aao.PCA, rdfs.isDefinedBy, aa),
        (aao.DistributionComparison, rdfs.isDefinedBy, aao),
        (aao.KolmogorovSmirnovTest, rdfs.isDefinedBy, aao)
        (aao.ErdosSectorialization, rdfs.isDefinedBy, aao)
        (aao.CurveFitting, rdfs.isDefinedBy, aao)
        (aao.Visualization, rdfs.isDefinedBy, aao)
        (aao.Analysis, rdfs.isDefinedBy, aao)
        (aao.Analysis, rdfs.isDefinedBy, aao)
]

# each aao class should link to aav concept by the triple:
# (aao.XXX, skos.relatedConcept, aav.XXX)

# For visualization of ontologies:
# - table for classes URIS (or after last "/") with meaning (rdfs:comment) and maybe more information (e.g. labels, restrictions)
# - table for properties, meanings, rdfs.domain, rdfs.range, axioms
# - table for restrictions and axioms.
# - tabular visualization of any class or property (or data value). With linking to other resources, internal (opens new visualization) and external (opens the URI as an HTTP link in a new tab).
# - graph and taxonomic tree.
# - number of triples, different subjects, objects, predicates.
# - facilities for annotating and changing the ontology
# - Summarizes the number of links related to each resource, total size of texts related by dataProperty, etc.
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
restriction = BNode()
rdfDeque = [
    (aao.Deque, rdfs.subClassOf, rdf.List),
    (aao.Deque, rdfs.restriction, owl.Restriction),
    (aao.Deque, owl.ExistentialRestriction, restriction)
    (restriction, owl.Restrictionproperty, rdfs.first),
    (aao.Deque, pe.recommendedProperty, rdfs.last),
    (aao.Deque, pe.recommendedProperty, aao.current),
    (aao.Deque, pe.recommendedProperty, aao.isEmpty),
]
turtle = P.rdf.turtle(rdfDeque)

# relations from datatype specifications
triples = [
    (aao.Deque, owl.note, "labels: deque, doubly linked queue, double queue"), #  will be processed as (pref)(alt)labels for skos. 
    (aao.Deque, aao.rdfImplentation, turtle),
]




