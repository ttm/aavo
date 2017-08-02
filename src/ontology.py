import nltk
import percolation as p

owl =  p.rdf.NS.owl
xsd =  p.rdf.NS.xsd
aao = p.rdf.NS.aao # Audiovisual Analytics Ontology
a =  p.rdf.NS.rdf.type

triples = [
        (aao.Datatype, aao.type, aao.Datatype),
        (aao.Audio, owl.subClassOf, aao.TemporalSeries),
        (aao.TemporalSeries, owl.subClassOf, aao.Datatype),
        (aao.RelationalData, owl.subClassOf, aao.Datatype),
        (aao.Network, owl.subClassOf, aao.RelationalData),
        (aao.Graph,   owl.subClassOf, aao.Network),

        (aao.Data, aao.type, aao.Datatype),
        (aao.Data, aao.availability, aao.Availability),
        (aao.StaticAvailability,  owl.subClassOf, aao.Availability),
        (aao.DynamicAvailability, owl.subClassOf, aao.Availability),

        (aao.Processing, aao.input, aao.Data),
        (aao.Processing, aao.output, aao.Data),
        (aao.Processing, aao.processes, aao.Data),
        (aao.Processing, aao.suitableFor, aao.Datatype),

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
        (aao.Visualization, aao.suitableFor, aao.Datatype),
        (aao.Visualization, aao.input, aao.Data),
        (aao.Visualization, aao.numberOfDimensions, xsd.double),
        (aao.HeatMap, owl.subClassOf, aao.Visualization),
        (aao.Histogram, owl.subClassOf, aao.Visualization),
        (aao.Histogram, aao.suitableFor, aao.StatisticalTest),
        (aao.ScatterPlot, owl.subClassOf, aao.Visualization),
        (aao.Timeline, owl.subClassOf, aao.ScatterPlot), # Ok?? Enhance this
        (aao.ScatterPlot, aao.suitableFor, aao.MDS),

        (aao.Visualization, aao.output, aao.VisualRepresentation), # put Visual Representation as a subclass of Data?
        (aao.Image, owl.subClassOf, aao.VisualRepresentation),
        (aao.Animation, owl.subClassOf, aao.VisualRepresentation),
        ]

terms = {
        "ZScore": "Z-Score",
        "ZTest": "Z-Test",
        "PreProcessing": "Pre-Processing",
        }

o = p.rdf.publishing.Ontology(triples, {"owl": owl, "aao": aao}, terms)
import os
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, os.pardir)
o.render(path)

# Notes:
# * Include Audio(visualization)
# * Make an even simpler core
# * Main concepts: Visualization, Analysis*, Data, Datatype, Processing, PreProcessing, Hypothesis, Task/Purpose/Application
# * Consider existential and universal restrictions
