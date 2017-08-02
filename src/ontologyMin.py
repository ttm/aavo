import percolation as p

owl =  p.rdf.NS.owl
xsd =  p.rdf.NS.xsd
aao = p.rdf.NS.aao # Audiovisual Analytics Ontology
a =  p.rdf.NS.rdf.type

triples = [
        (aao.Data, aao.type, aao.Datatype),

        (aao.Processing, aao.input, aao.Data),
        (aao.Processing, aao.output, aao.Data),
        (aao.Processing, aao.suitableFor, aao.Datatype),

        (aao.PreProcessing, owl.subClassOf, aao.Processing),

        (aao.Visualization, aao.uses, aao.Processing), # better term than uses?
        (aao.Visualization, aao.suitableFor, aao.Processing),
        (aao.Visualization, aao.suitableFor, aao.Datatype),
        (aao.Visualization, aao.input, aao.Data),
        (aao.Visualization, aao.numberOfDimensions, xsd.double),

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
o.render(path, "aavo0.01_minimum")





# Notes:
# * Include Audio(visualization)
# * Make an even simpler core
# * Main concepts: Visualization, Analysis*, Data, Datatype, Processing, PreProcessing, Hypothesis, Task/Purpose/Application
# * Consider existential and universal restrictions
