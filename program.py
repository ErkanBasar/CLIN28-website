
####### EMAIL #########

registration_email_sbj = "ATILA2016 - Registration"

registration_email_msg = 'Dear Madam/Sir\n\nThank you for registering for ATILA 2016.\n\nPlease check the information listed below and in any case of a problem please do not hesitate to contact us.'


########## SCHEDULE/PROGRAM #########

# To find various icons please visit http://fontawesome.io/icons/
# To apply them, please write the icon codes to the 'icon' field in the dictionaries

# 'uniqueID' field can be even random, but should be unique no matter what, otherwise dropdown buttons would open wrong panels

programDay1 = [
               { 'time':'9:30 - 10:00',
               'icon': 'fa-registered',
               'name':'Registration',
               },
               { 'time':'10:30 - 11:00',
				  'icon': 'fa-comment',
                  'name':'Session 1: Social Media',
				  'presentations' : [
										 {
											'title': 'Social media Analytics',
											'speakers':['Ali Hurriyetoglu', 'Florian Kunneman', 'Eric Sanders [LaMas]'],
											'uniqueID':'AliFloEric',
											'abstract':'In this talk we present the latest results in several social media mining projects.'
										},
									]
				},

               { 'time':'11:00 - 11:30',
               'icon': 'fa-coffee',
               'name':'Coffee Break',
               },
               { 'time':'11:30 - 13:00',
                'name': 'Session 2: Social Media',
				  'icon': 'fa-comment',
				  'presentations' : [
                                     {
                                     'title': 'Monday mornings are my fave :) #not - Exploring the Automatic Recognition of Irony in English tweets',
                                     'speakers':['Cynthia Van Hee', 'Els Lefever', 'Véronique Hoste [LT3]'],
                                     'uniqueID':'CynthiaElsVéronique',
                                     'abstract':'Recognising and understanding irony is crucial for the improvement of natural language understanding tasks including sentiment analysis. In this study, we describe the construction of an English Twitter corpus and its annotation for irony based on fine-grained guidelines we developed. We also explore the feasibility of automatic irony recognition by exploiting a varied feature set including lexical, syntactic, sentiment and semantic (Word2Vec) information. Experiments on a held-out test corpus show that our irony classifier benefits from this combined information, yielding an F1-score of 67.66%. When hashtag information like #irony is included in the data, the system even obtains an F1-score of 92.77%. A qualitative analysis reveals that recognising ironic instances based on a polarity clash appears to be (much) more feasible than recognising other forms of ironic utterances (e.g., situational irony).'
                                     },
                                     {
                                     'title': 'Classifier optimization for cyberbully detection: finding the needle in the haystack',
                                     'speakers':['Gilles Jacobs [LT3]'],
                                     'uniqueID':'Gilles',
                                     'abstract':'We approach automatic detection of cyberbullying in social media as a text classification task. Because instances of cyberbullying are far and few between we are dealing with an imbalanced dataset where the positive class is notably smaller than the negative class. The inclusion of a plethora of linguistic features and the amount of document instances make for a high dimensional dataset. Feature filtering methods determine the most relevant features of the dataset and help reduce dimensionality and in some cases imbalance. Resampling rearranges the classes by downsampling the majority class and upsampling the minority class. We investigate several combinations of feature selection (both filter and wrapper approaches), resampling, and classifier optimizations to treat imbalance and high dimensionality issues in text classification.'
                                     },
                                     {
                                     'title': 'Party Politics and Personality',
                                     'speakers':['Ben Verhoeven', 'Guy De Pauw', 'Barbara Plank', 'Marcel Hanegraaff', 'Bert Fraussen', 'Tom De Smedt', 'Walter Daelemans [CLiPS]'],
                                     'uniqueID':'BenGuyBarbara',
                                     'abstract':'Twitter is the most open and immediate channel through which politicians can interact with one another. An important question in this regard is whether these online interactions are mostly shaped by party politics or if there are other factors at play, such as age, gender and ideology. To study these effects, we have monitored twitter interactions in a closed set of Flemish and Dutch politicians (n=345) for over two years. We will start off this presentation by showing the effect of various known variables on how these interactions take shape. As public figures, most relevant features of politicians, such as age and gender, are known and their discovery does not require author profiling techniques. Except for personality, which is arguably an essential factor in how social interactions are shaped. The second part of the presentation therefore focuses on the TwiSty Corpus which allows us to develop techniques that can further add this metadata field to tweets. We finish up the presentation by presenting the result of applying TwiSty to the political tweets data set. We present party-specific personality profiles, as well as an analysis of how personality shapes online interactions in the political arena.'
                                     }
									]
				},
               { 'time':'13:00 - 14:00',
               'icon': 'fa-cutlery',
               'name':'Lunch',
               },
               { 'time':'14:00 - 15:00',
               'name': 'Session 3: Text Generation',
               'icon': 'fa-comment',
               'presentations' : [
                                  {
                                  'title': 'Towards more variation in text generation systems: Developing and evaluating model for referring expression generation',
                                  'speakers':['Thiago Castro Ferreira [TiCC]'],
                                  'uniqueID':'Thiago',
                                  'abstract':'Automatic text generation is the process of converting non-linguistic data into coherent and comprehensible text. Even though computers these days are perfectly capable of automatically producing text, the results are arguably often rather rigid, always producing the same kind and style of text, which makes them somewhat “boring” to read, especially when reading multiple texts in succession. We aim to fill this gap by introducing non-deterministic methods for referring expression generation, specially for the choice of referential form (whether a reference is a proper name, a description, a pronoun, etc) and for the generation of proper names. We will show that these methods enables us to generate varied references in texts, which did not yield significant differences from human-produced references according to human judges.'
                                  },
                                  {
                                  'title': 'A translation robot for each translator? A comparative study of manual translation and post-editing of machine translations: process, quality and translator attitude',
                                  'speakers':['Joke Daems [LT3]'],
                                  'uniqueID':'Joke',
                                  'abstract':'A comparative study of the traditional way of translating and translation on the basis of machine translations to translate general (non-technical) texts for the English-Dutch language pair. Translation expertise is taken into account as an additional parameter. We have observed the behaviour of 13 professional translators and 10 students using keystroke logging and eyetracking. The machine translation output, manually translated and post-edited texts have been annotated for quality to allow for a diagnostic comparative analysis. Participant surveys before and after the experiment allow us to take participants\' attitude into account as well.'
                                  },
                                ]
               },
               { 'time':'15:00 - 15:30',
               'icon': 'fa-thumbs-o-up',
               'name': 'Discussion on potential joint project proposals',
               },
               { 'time':'15:30-15:40',
               'icon': 'fa-files-o',
               'name':'Slides Introduction <h4>(1 minute - 1 slide intro)</h4>',
               },
               { 'time':'15.40-17.30',
               'name': 'Poster and Demonstration Session <h4>(accompanied with coffee)</h4>',
               'icon': 'fa-files-o',
               'presentations' : [
                                  {
                                  'title': ' A crowdsourcing annotation interface for Wikification in 11 language pairs',
                                  'speakers':['Iris Hendrickx', 'Eirini Takoulidou', 'Katia Kermanidis [LaMas]'],
                                  'uniqueID':'IrisEiriniKatia',
                                  'abstract':''
                                  },
                                  {
                                  'title': 'Relevancer: Finding and Labeling Relevant Information in Tweet Collections',
                                  'speakers':['Ali Hurriyetoglu [LaMas]'],
                                  'uniqueID':'Ali',
                                  'abstract':''
                                  },
                                  {
                                  'title': 'Symptom Severity Identification from Psychiatric Evaluation Notes',
                                  'speakers':['Akos Kadar [TiCC]'],
                                  'uniqueID':'Akos',
                                  'abstract':''
                                  },
                                  {
                                  'title': 'Structuring the visual world through language learning',
                                  'speakers':['Madhumita [UZA, CLiPS]'],
                                  'uniqueID':'Madhumita',
                                  'abstract':''
                                  },
                                  {
                                  'title': 'AHA: Anagram Hashing Application',
                                  'speakers':['Martin Reynaert [TiCC, LaMas]'],
                                  'uniqueID':'Martin',
                                  'abstract':''
                                  },
                                  {
                                  'title': 'Collection, Annotation, Evaluation: A Gold Standard for Automatic Terminology Extraction',
                                  'speakers':['Ayla Rigouts Terryn [LT3]'],
                                  'uniqueID':'Ayla',
                                  'abstract':''
                                  },
                                  {
                                  'title': 'Data-to-text system for soccer reports',
                                  'speakers':['Chris van der Lee', 'Emiel Krahmer', 'Sander Wubben [TiCC]'],
                                  'uniqueID':'ChrisEmielSander',
                                  'abstract':''
                                  },
                                  {
                                  'title': 'Classifier setups for predicting clinical codes.',
                                  'speakers':['Elyne Scheurwegs', 'Kim Luyckx', 'Walter Daelemans [ADReM, CLiPS, UZA]'],
                                  'uniqueID':'ElyneKimWalter',
                                  'abstract':''
                                  },
                                  {
                                  'title': 'FLAT - A linguistic annotation tool for FoLiA',
                                  'speakers':['Maarten van Gompel [LaMas]'],
                                  'uniqueID':'Maarten',
                                  'abstract':''
                                  },
                                  {
                                  'title': 'WhiteLab 2.0.',
                                  'speakers':['Matje van der Camp', 'Martin Reynaert [LaMas]'],
                                  'uniqueID':'MatjeMartin',
                                  'abstract':''
                                  },
                                  {
                                  'title': 'Taalmonsters Metadata Editor',
                                  'speakers':['Matje van der Camp [LaMas]'],
                                  'uniqueID':'Matje',
                                  'abstract':''
                                  },
                                  {
                                  'title': 'Identifying mood of songs using musical and linguistic information',
                                  'speakers':['Bram Willemsen', 'Menno van Zaanen [TiCC]'],
                                  'uniqueID':'BramMenno',
                                  'abstract':''
                                  },
                                  {
                                  'title': 'Reddit Reply generation with RNNs',
                                  'speakers':['Sander Wubben', 'Bram Willemsen [TiCC]'],
                                  'uniqueID':'gsgfsg',
                                  'abstract':''
                                  }
                                  ]
               },
                { 'time':'17:48-18:06',
                'icon': 'fa-train',
                'name':'Train to Nijmegen',
                },
                { 'time':'18:10-18:45',
                'icon': 'fa-street-view',
                'name':'Walk through Nijmegen city centre',
                },
               { 'time':'18:45',
               'icon': 'fa-users',
               'name':'Social activity',
               },
               { 'time':'20:15',
               'icon': 'fa-cutlery',
               'name':'Dinner',
               },
               { 'time':'',
               'icon': 'fa-clock-o',
               'name':'Return to the workshop location: be aware of the train schedule! <h4>22:53 Train option 1: departure at Spoor 4b at Nijmegen</h4><h4>23.53 Train option 2: departure at Spoor 4b at Nijmegen</h4><h4>00:23 The very last train of the night!</h4>',
               },
			  ]

programDay2 = [

               { 'time':'9.30-11.00',
               'name': 'Session 4: Language Learning',
               'icon': 'fa-comment',
               'presentations' : [
                                  {
                                  'title': 'Word learning and categorization: distributional factors in word learning and lexical category acquisition',
                                  'speakers':['Robert Grimm', 'Giovanni Cassani', 'Steven Gillis', 'Walter Daelemans [CLiPS]'],
                                  'uniqueID':'RobertGiovanniStevenWalter',
                                  'abstract':'In this talk we use computational methods to investigate word learning and lexical category acquisition from a distributional perspective. Several studies have shown that the distributional context in which words occur is important for children to acquire words and the lexical categories to which they belong. Concerning word learning, we investigate the role of multi-word units (MWUs). Correlating the number of MWUs per target word with (1) its age of first production and (2) adult reaction times in a lexical decision task, we find a stronger impact of MWUs on the former -- suggesting that MWUs are more important for word learning than for adult processing. Turning to lexical category acquisition, we ran a supervised PoS tagging experiment to analyse what distributional properties of contexts make them useful for categorising words into lexical categories and which distributional properties of a word make it easy to be categorised. Preliminary results suggest that occurring frequently and with many different words makes a context more useful; on the contrary, contexts that are more predictable given the words they occur with are less useful, like contexts with higher entropy. Bigrams are better than trigrams, and left, or preceding, contexts are the most useful. Words appear to be easier to categorize when they have low entropy and are on average difficult to predict given the contexts they occur with.'
                                  },
                                  {
                                  'title': 'From phonemes to images: levels of representation in a recurrent neural model of visually-grounded language learning',
                                  'speakers':['Lieke Gelderloos [TiCC]'],
                                  'uniqueID':'Lieke',
                                  'abstract':'The presented model of visually-grounded language learning is based on stacked gated recurrent neural networks and learns to predict features of the visual context, given an image description in the form of a sequence of phonemes. The learning task resembles that faced by human language learners who need to discover both structure and meaning from noisy and ambiguous data across modalities. The trained model represents linguistic information in a hierarchy of levels: lower layers in the stack are comparatively more sensitive to form, whereas higher layers are more sensitive to meaning.'
                                  },
                                  {
                                  'title': 'Mapping lexical, syntactical and phonological information processing in the brain using probabilistic language models',
                                  'speakers':['Alessandro Lopopolo [LaMas]'],
                                  'uniqueID':'Alessandro',
                                  'abstract':'Probabilistic measures computed from language model have been successfully used as predictors of several behavioral and neural correlates of language processing From a narrative text that was given as a stimulus to 24 participants to an fMRI experiment, we computed surprisal from transitional probabilities between words and between their POS tags, and perplexity on their phoneme transcriptions. We used these measures to establish neural correlates of lexical, syntactic and phonological processing. A novelty of our approach is that we characterize three important streams of information processing during language comprehension within the same experiment, using the same stimulus and the same information extraction procedure.'
                                  }
                                  ]
               },
               { 'time':'11:00 - 11:30',
               'icon': 'fa-coffee',
               'name':'Coffee Break',
               },
               { 'time':'11:30 - 12:30',
               'name': 'Invited Talk',
               'icon': 'fa-comment',
               'presentations' : [
                                  {
                                  'title': 'Never Ending Language Learning: Lessons and What Next?',
                                  'speakers':['Tom Mitchell'],
                                  'uniqueID':'InvitedTalk',
                                  'abstract':''
                                  },
                                  ]
               },
               { 'time':'12:30 - 14:00',
               'icon': 'fa-cutlery',
               'name':'Lunch',
               },
               { 'time':'14:00 - 15:30',
               'name': 'Session 5: Text Mining',
               'icon': 'fa-comment',
               'presentations' : [
                                  {
                                  'title': 'Extractive summarization for discussion forum threads',
                                  'speakers':['Suzan Verberne [LaMas]'],
                                  'uniqueID':'Suzan',
                                  'abstract':'In this talk I present our work extractive summarization of long threads in online discussion fora. We conducted a user evaluation study to determine human preferences in forum summarization and to create a reference data set. We study the agreement between human raters on the summarization task, and we show how multiple reference summaries can be combined to develop a successful model for automatic summarization. We found that although the inter-rater agreement for the summarization task was slight, the automatic summarizer obtained reasonable results in terms of precision and recall. Moreover, when human raters were asked to choose between the summary created by another human and the summary created by our model in a blind side-by-side comparison, they judged the model’s summary equal to or better than the human summary in over half of the cases. This shows that even for a summarization task with low inter-rater agreement, a model can be trained that generates sensible summaries.'
                                  },
                                  {
                                  'title': 'Influence of course characteristics, student characteristics, and behavior in learning management systems on student performance',
                                  'speakers':['Rianne Conijn', 'Menno van Zaanen', 'Chris Snijders [TiCC]'],
                                  'uniqueID':'RianneMennoChris',
                                  'abstract':'The use of learning management systems (LMS) in education make it possible to track students’ online behavior. This data can be used for educational data mining and learning analytics, for example by predicting student performance. Although LMS data might contain useful predictors, course characteristics and student characteristics have shown to influence student performance as well. However, these different sets of features are rarely combined or compared. Therefore, in the current study we classify student performance using information from course characteristics, student characteristics, past performance, and LMS data. Three classifiers (decision tree, rule-based, and SVM) are trained and compared with the majority class baseline. Overall, SVM is the best classifier to identify pass/fail. However, for more interpretable results, the decision tree or the rule-based algorithm with course characteristics, student characteristics, and midterm data are good second bests. Additionally, it is shown that the different feature sets all have a positive influence on predicting pass/fail. In particular, student characteristics and the midterm grade have a large influence. Compared to these feature sets, LMS data seems less important. Yet, a more fine-grained analysis of the specific metrics found in the learning management system may still yield useful information.'
                                  },
                                  {
                                  'title': 'Towards clinical-language understanding',
                                  'speakers':['Simon Šuster', 'Stéphan Tulkens', 'Walter Daelemans [CLiPS]'],
                                  'uniqueID':'gsgfsg',
                                  'abstract':'We introduce the Accumulate project, in which we are developing technology for analyzing clinical reports in English and Dutch. We give an overview of the characteristics of the clinical domain using examples from doctor\'s medical notes. We then describe our approach to concept disambiguation, in which we use distributed representations together with a large knowledge base to link word occurrences to clinical concepts. In addition, we touch upon higher-level semantic analysis, where the goal is to develop a method to predict predicate-argument structure assuming minimal linguistic preprocessing.'
                                  }
                                  ]
               },
               { 'time':'15.30-17.00',
               'icon': 'fa-beer ',
               'name':'Drinks',
               }
               ]
