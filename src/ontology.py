import nltk
import percolation as p

skos = p.rdf.ns.skos
owl = p.rdf.ns.owl
rdf = p.rdf.ns.rdf
rdfs = p.rdf.ns.rdfs
void = p.rdf.ns.void
xsd = p.rdf.ns.xsd
# http://purl.org/audiovisualanalytics/
aa = p.rdf.ns.aa # Audiovisual Analytics (Ontology and Vocabulary)
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

a = rdf.type

triples = [
        (aao.DataType, aao.type, aao.DataType),
        (aao.Audio, owl.subClassOf, aao.TemporalSeries),
        (aao.TemporalSeries, aao.subClassOf, aao.DataType),
        (aao.RelationalData, aao.subClassOf, aao.DataType),
        (aao.Network, aao.subClassOf, aao.RelationalData),
        (aao.Graph, aao.subClassOf, aao.Network),

        (aao.Data, aao.type, aao.DataType),
        (aao.Data, aao.availability, aao.Availability),
        (aao.StaticAvailability,  owl.subClassOf, aao.Availability),
        (aao.DynamicAvailability, owl.subClassOf, aao.Availability),

        (aao.Processing, aao.input, aao.Data),
        (aao.Processing, aao.output, aao.Data),
        (aao.Processing, aao.processes, aao.Data),
        (aao.Processing, aao.suitableFor, aao.DataType),

        (aao.MDS, owl.subClassOf, aao.Processing),
        (aao.PCA, owl.subClassOf, aao.MDS),
        (aao.StatisticalTest, owl.subClassOf, aao.Processing),
        (aao.StatisticalTest, owl.subClassOf, aao.Processing),
        (aao.KolmogorovSmirnovTest, owl.subClassOf, aao.StatisticalTest),
        (aao.ZTest, owl.subClassOf, aao.StatisticalTest),
        (aao.PreProcessing, owl.subClassOf, aao.Processing),
        (aao.ZScore, owl.subClassOf, aao.PreProcessing),
        (aao.Cleaning, owl.subClassOf, aao.PreProcessing),

        (aao.Visualization, aao.uses, aao.Processing), # better term than uses?
        (aao.Visualization, aao.suitableFor, aao.Processing),
        (aao.Visualization, aao.suitableFor, aao.DataType),
        (aao.Visualization, aao.input, aao.Data),
        (aao.Visualization, aao.numberOfDimensions, xsd.double),
        (aao.HeatMap, owl.subClassOf, aao.Visualization),
        (aao.Histogram, owl.subClassOf, aao.Visualization),
        (aao.Histogram, aao.suitableFor, aao.StatisticalTest),
        (aao.ScatterPlot, owl.subClassOf, aao.Visualization),
        (aao.TimeLine, owl.subClassOf, aao.ScatterPlot), # Ok?? Enhance this
        (aao.ScatterPlot, aao.suitableFor, aao.MDS),

        (aao.Visualization, aao.output, aao.VisualRepresentation), # put Visual Representation as a subclass of Data?
        (aao.Image, owl.subClassOf, aao.VisualRepresentation),
        (aao.Animation, owl.subClassOf, aao.VisualRepresentation),
        ]
# Notes:
# * Include Audio(visualization)
# * Make an even simpler core
# * Main concepts: Visualization, Analysis*, Data, DataType, Processing, PreProcessing, Hypothesis, Task/Purpose/Application
# * Consider existential and universal restrictions
