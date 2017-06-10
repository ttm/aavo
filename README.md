# audiovisual analytics vocabulary and ontology (AAVO)
This repository holds:
* a SKOS vocabulary;
* an OWL ontology;
* Python code to synthesize them both.
* This README.md with directions on the implementation
and intended uses.

In summary, audiovisual analytics (AA) is an extension of visual analytics
to encompass both visualizing and hearing data.
It is a broad subject which related data structures and provenance,
analysis techniques and methods, audiovisualization of data and
visual interfaces.
Therefore, AAVO should strive to use already existing vocabularies
and ontologies (e.g. DBpedia and Wordnet).

AAVO systematizes the knowledge involved in AA
and gives context by relations to external vocabularies and ontologies.

Check the documentation in this README.md and in the [][wiki]
for further directions on how AAVO is being implemented.

# intended use
AAVO is intended for conceptual organization and discussion
and for obtaining relations by machine inference
(e.g. what analysis and visualizations might be useful for a given dataset).
Other and minor intended uses are described at the end of this README
(includes Portuguese text for now).



It is also conceived as an audiovisual analytics framework
in which the following components are foreseen:
* Visuals: useful routines for generating images, videos.
* Percolation: linked data and data analysis facilities.
* Social/Participation/Gmane: routines for representing data
from diverse provenance as linked data.
* Music: routines useful for rendering sound and music.
* AAVO: the conceptualization linked data/semantic web.
* AAI: a gluing component for providing audiovisual analytics interfaces.
Should include a web frontend using D3.js and ccNetViz.

All implementations should be done in Python (backend)
and Javascript (frontend).

# implementation details
Each concept is related both to an OWL class and a SKOS
concept for [allowing OWL DL inference to be made in the ontology][1].
Otherwise it is OWL Full.

The conceptualization is formalized in OWL (as an ontology)
from which the SKOS vocabulary is automatically derived.
SKOS is less formal then OWL so a small set of conventions
allows the percolate to output the vocabulary
from the ontology.

The ontology rdf/audiovisualAnalyticsOntology.owl is synthesized by the src/ontology.py file.
The vocabulary rdf/audiovisualAnalytics.rdf is then obtained from rdf/audiovisualAnalytics.owl
by means of src/vocabulary.py.
Example usages of AAVO for reasoning and extracting knowledge
should be in src/sparql.py.

Visualization of RDF code involves:
* multiple RDF text formats (Turtle, n3, Manchester, XML, etc).
* diagram view (nodes are classes or concepts or raw data).
* Tree view for the taxonomic relations.

These files should be in the rdf/ and img/ directories.

Notes on the implementation of the full AA framework should be in the wiki
of this repository while other components are incipient.

# conceptualization issues
* Text and numbers are considered visualization.
* Some analysis methods involve visualization.
  - We keep under analysis methods only what involves data processing
and arbitrary consultation.
  - Under visualization are kept only methods for representing data visually.
  - Example: PCA in an analysis. The scatter plot is a visualization
  (which might be useful for plotting data with respect to the first principal components).
  - Relations between analysis and visualization concepts are defined in the ontology and vocabulary.
  - If for an analysis technique this distinction is not possible,
  we can use the concept of (audio)visual analysis.

# core and extended AAVO
Both the ontology and vocabulary have core and extended versions.
Extended includes core.
Core is meant to keep a very simple representation of the knowledge.
* Core includes: data, analysis, audiovisualization and interface concepts as OWL classes and properties,
and as SKOS concepts. Some sub classes and properties.
* Extended also includes: knowledge from other fields such as statistics, complex networks,
text mining, audio and music, visual design, HCI, UI, etc.
When necessary to better account for the Visual Analytics field.
Definition of further sub classes and properties of the main classes.

# deriving the vocabulary from the ontology
By standard, each OWL class and property is a subclass of SKOS skos:Concept.
subClassOf and subPropertyOf are subProperties of skos:broader.
OWL properties also yield skos:related.
OWL properties can be annotated to yield vocabulary relations and not concepts.

What should we use to yield a vocabulary with relations such as meronymy
and hyponymy?

# further notes
* Maybe start from this linking to Wordnet and DBPedia and LOSD
and then grow from them.
* Revisit Pandas, Sympy, other python data-related libraries
and the Entoght videos for obtaining a solid conceptualization
of the analysis (and visualizations).
* Defining classes as of owl:type another class and rdfs:subClassOf skos:Concept
allows for annotating instances of the class with SKOS properties.
This does not enable the annotations to be directly annotated in the classes,
reason why we did not choose this approach.
* Pseudocodes for data structures and algorithms are written as RDF Schema (RDFS).
RDF collections, RDFS containers, and SparQL queries.
- Each OWL class has a related SKOS concept.
Annotations are made in each class
and inherited by the concept.
  * super classes are maped to broader relations.
  * definitions and notes are inherited in related fields.
  * OWL properties have skos properties as superproperties (broader, related concept, etc)
  * If needed, define ontology annotation properties that can be mapped or inherited by the vocabulary. Another approach is to use textual tags in the string.
  The first approach leads to better defined ontological structures while the second might involve in simples structures and less coding (an maybe to less clear and less clean comments).
  * How to map OWL meronyms to SKOS?

# Issues
* Find the [difference between using an inference process
or a model-driven transformation][1].
* Find the difference between skos Collection and Concept Scheme.
* Define the set of external properties and classes that will be used.
* Distinguish between array and matrix?
* What is the difference between method and technique?

[1]: https://www.w3.org/2006/07/SWD/SKOS/skos-and-owl/master.html

# drafts in English:
Should include subfields like data visualization,
information and scientific visualization,
HCI, visual design, UI.
Should include visualization methods including other
senses, at least hearing
(for the blind to have information of the visual environment,
such as location and colors. Michel Hospital (FEE/UFSCar).

# drafts in a English and Portuguese mix
Há intuitos menores do AAVO:
  * permitir consulta e rápida assimilação de aspectos da analítica audiovisual
  tanto para o especialista quanto para outros interessados.
  * sustentar possíveis software de analítica visual através de relações
  entre dados, métodos de análise e visualizações específicas:
      - 1D: histograms, medians, cumulativas, ajuste de curva ou distribuição).
      - 2D: scatter plot com ajuste de curva 2d histogram, 1d histogram of a measure over other measure, curve and distribution fitting
      - 3D: scatter plot com ajuste de curva, componentes principais, histograma 3d?, curve and distribution fitting
      - 4-XD: PCA, MDS, outro?
      - Riemmanian manifolds: circular statistics (circular histgrams?).
      - temporal/sequencial: timeline, 1D methods, other?
      - PCA: plot 1D, 2D, 3D. Visualização como tabela. (analíse -> visualização)
      - Histogram and derivatives (e.g. cumulative distribution): bar graph, timeline, other?
      - Suitable analysis and visualization for basic data types (linked list, set, dictionary, homogeneus and eterogeneous arrays).
	
A obtenção de cumulativa é uma técnica para análise de distribuições,
então ela é um item dentre as técnicas e métodos de processamento:
PCA e curve fitting é uma técnica de análise de distribuições
que resultam em boas visualizações de dados.
O curve fitting pode ser parametrizado e escrutinizado
através de uma interface visual.

a interface visual serve para:
  * a escolha de visualizações
  * a parametrização de visualizações
  * a audiovisualização de resultados, seja via texto, números, imagens, números, video ou música.
  * Download any of the information in any visualization or visualization interface.

Each visualization, datatype or analysis method should have a standard visualization interface.

- Concept: Interface
  * narrower: Analysis, Visualization, Datatype, Widget
 
- Concept: Analysis
  * subClass: PCA, curve fitting, histogram, 1D method, 2D method, 3D method
  * necessaryAudiovisualization: class Visulization Interface
  * necessaryAudiovisualization: subPropertyOf skos:related
  * note: the analysis method might be tightly linked to a visualization Interface
 
- Concept: AudioVisualization
  * subClass: 1D visualizaton, 2D visualization, 3D visualization, audio
 
- Concept: Datatype
  * type: linked list, homogeneous and heterogeneous set, homogeneous array, heterogeneous array, dictionary with numbers or other datatypes, compound
  * datatypeChildren: same values as type
  * child: DataType Instance 
  * childs: set, array or dictionary of DataTypes
 
- Concept: Data
  * provenance: audio, social network, temporal/sequential, etc.
  * type: Data Type
  * data: the specific data structure

The interface uses Data, Analysis and Visualization
compatibilities for rendering itself.
An interface might be related to them by:
- dedicatedInterfaceOf
- possibleInterfaceOf
- isInterfaceOf

An interface has sessions, which are subInterfaces (?).

Outras notas:
- Olho mágico para visualizações.
- DoIn sonoro e sons binaurais para audio de acompanhamento.
- https://datadotworld.gitbooks.io/sparql/content/ para aprender SparQL.
- Reler a documentação de RDF(s), SKOS e OWL.
- Encontrar outros trabalhos interessantes e fazer uma lista das classes
e propriedades que usam.

## Data, Analysis and Visualization compatibility
- Data and analysis:
the analysis method has to be compatible
with the "Data type ?" triple.

- Analysis and AudioVisualization:
an analysis method also generates data,
and for a visualization to be compatible
the "Analysis output ?data. ?data type ?"
should be compatible with visualization input.
"Visualization input ?data.
?data type ?".

- Data and AudioVisualizations.
Visualizations also might generate data.
"AudioVisualization output ?data".
Any data might be directly visualized without
any analysis (e.g. scatter plot). In which
The datatype of both data and
of the input of the visualization should be compatible
"select ?compatible where {
  Data type ?DataType1 .
  ?Datatype1 type ?dt1.
  AudioVisualization input ?DataType2 .
  ?Datatype2 type ?dt2.
  compare( ?d1, ?d2) as ?compatible.
  }

Data is a URI of an instance of the Data class.
Visualization and ?DataTypeX are classes/concepts.
?dt1, ?dt2 are data values, strings in this case.
?compatible is also a data value, a boolean.

- Visualization and Visualization:
The Visualization output might be compatible
with another visualization's input.
Other relation among visualizations
are if they are often used for the same type of
analysis or data.

- Analysis and Analysis:
An analysis output might be compatible with
another analysis's input.
Other relation among analysis methods
are if they are often used for the same type of
data or visualization.

- Data and Data:
Data can always be merged together.
They are said compatible if their datatypes
match.
Other relations among data types and instances
are if they are often used for the same type of
analysis or visualization.


