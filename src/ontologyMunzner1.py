import percolation as p


rdf =  p.rdf.NS.rdf
rdfs = p.rdf.NS.rdfs
owl =  p.rdf.NS.owl
xsd =  p.rdf.NS.xsd
aao = p.rdf.NS.aao # Audiovisual Analytics Ontology
a =  p.rdf.NS.rdf.type

triples = [
        (aao.Visualization, rdfs.comment, 'augment human capabilities'),
        (aao.Visualization, rdfs.comment, 'envolves discovery and enjoyment'),
        (aao.Visualization, rdfs.comment, 'aka. vis'),

        (aao.Visualization, aao.has, aao.Limitation),
        (aao.HumanLimitation, owl.subClassOf, aao.Limitation),
        (aao.ComputationLimitation, owl.subClassOf, aao.Limitation),
        (aao.DisplayLimitation, owl.subClassOf, aao.Limitation),

        (aao.Visualization, aao.has, aao.Use),
        (aao.TransitionalUse, owl.subClassOf, aao.Use),
        (aao.LastingUse, owl.subClassOf, aao.Use),
        (aao.HypothesisHandling,     owl.subClassOf, aao.LastingUse),
        (aao.HypothesisTesting,      owl.subClassOf, aao.HypothesisHandling),
        (aao.HypothesisAttainment,   owl.subClassOf, aao.HypothesisHandling),
        (aao.HypothesisPresentation, owl.subClassOf, aao.HypothesisHandling),

        (aao.analyses, rdfs.subPropertyOf, aao.has),
        (aao.performs, rdfs.subPropertyOf, aao.has),
        (aao.what, rdfs.subPropertyOf, aao.has),
        (aao.how, rdfs.subPropertyOf, aao.has),
        (aao.why, rdfs.subPropertyOf, aao.has),

        (aao.VisualizationTool, aao.performs, aao.Visualization),
        (aao.Instance, aao.analyses, aao.VisualizationTool),

        (aao.Instance, aao.what, aao.Data),
        (aao.Instance, aao.why, aao.Task),
        (aao.Instance, aao.how, aao.Idiom),

        (aao.Task, aao.has, aao.Goal),

        (aao.Visualization, aao.has, aao.Data),
        (aao.Visualization, aao.has, aao.Goal),
        (aao.Visualization, aao.has, aao.Idiom),
        ]


o = p.rdf.publishing.Ontology(triples, {"owl": owl, "aao": aao})
import os
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, os.pardir)
o.render(path, "aavoMunzne1.01b")





# Notes:
# * Include Audio(visualization)
# * Make an even simpler core
# * Main concepts: Visualization, Analysis*, Data, DatasetType, Processing, PreProcessing, Hypothesis, Task/Purpose/Application
# * Consider existential and universal restrictions

