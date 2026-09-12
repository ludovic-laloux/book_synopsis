"""
Published synopses from a random sample of fiction books.

This dataset is based on the "Books Dataset" by Abdallah Wagih, originally
licensed under the Apache License 2.0:
https://www.kaggle.com/datasets/abdallahwagih/books-dataset

Data has been modified to extract only the description field from a small
sample of books.

For more details, see the full Apache License text:  
https://www.apache.org/licenses/LICENSE-2.0
"""

book_summaries = [
    ("Joe and his parents are enjoying a summer holiday by the sea "
     "at the Ocean Star Hotel. The sky is bright blue, the sun shines "
     "and Joe loves all that the seaside has to offer. But when the fog "
     "rolls in and rain falls Joe begins to wish that he was back at "
     "home again. Things change, however, when the owner of the hotel "
     "invites Joe to share in a magical world, only a few steps away. "
     "The loft is black as night but then above Joe's head a thousand "
     "tiny stars begin to sparkle and in the distance he hears the "
     "chug-chug-chug of a model train. A whole world is soon to open "
     "up before Joe's eyes, a world of snow-capped mountains, great "
     "deserts, and rocking fishing boats."),

    ("After twelve-year-old Johnny Maxwell suddenly starts seeing and "
     "talking to ghosts, he and his friends become involved in a battle "
     "to save the local cemetery."),

    ("During a scarlet fever outbreak in 1906, thirteen-year-old "
     "Lizabeth must decide whether it is more important to be "
     "Strawberry Queen or to be at the bedside of her younger sister, "
     "who is ill."),

    ("A young widow raising two boys, Sarah Laden is struggling to "
     "keep her family together. But when a shocking revelation rips "
     "apart the family of her closest friend, Sarah finds herself "
     "welcoming yet another troubled young boy into her already "
     "tumultuous life. Jordan, a quiet, reclusive elementary school "
     "classmate of Sarah's son Danny, has survived a terrible ordeal. "
     "By agreeing to become Jordan's foster mother, Sarah will be "
     "forced to question the things she has long believed. And as the "
     "delicate threads that bind their family begin to unravel, all "
     "the Ladens will have to face difficult truths about themselves "
     "and one another - and discover the power of love necessary to "
     "forgive and to heal."),

    ("Jess Aarons' greatest ambition is to be the fastest runner in "
     "his grade. He's been practicing all summer and can't wait to "
     "see his classmates' faces when he beats them all. But on the "
     "first day of school, a new girl boldly crosses over to the boys' "
     "side and outruns everyone. That's not a very promising beginning "
     "for a friendship, but Jess and Leslie Burke become inseparable. "
     "Together they create Terabithia, a magical kingdom in the woods "
     "where the two of them reign as king and queen, and their "
     "imaginations set the only limits. Then one morning a terrible "
     "tragedy occurs. Only when Jess is able to come to grips with "
     "this tragedy does he finally understand the strength and courage "
     "Leslie has given him."),

    ("When Digory and Polly try to return the wicked witch Jadis to "
     "her own world, the magic gets mixed up and they all land in "
     "Narnia where they witness Aslan blessing the animals with human "
     "speech."),

    ("The trials of Dr. Daniel Waterhouse and the Natural Philosophers "
     "increase one hundredfold in an England plagued by the impending "
     "war and royal insecurities - as the beautiful and ambitious "
     "Eliza plays a most dangerous game as double agent and confidante "
     "of enemy kings."),

    ("Growing up in the suburbs in post-war Japan, it seemed to Hajime "
     "that everyone but him had brothers and sisters. His sole "
     "companion was Shimamoto, also an only child. Together they spent "
     "long afternoons listening to her father's record collection. But "
     "when his family moved away, the two lost touch. Now Hajime is in "
     "his thirties. After a decade of drifting he has found happiness "
     "with his loving wife and two daughters, and success running a "
     "jazz bar. Then Shimamoto reappears. She is beautiful, intense, "
     "enveloped in mystery. Hajime is catapulted into the past, putting "
     "at risk all he has in the present."),

    ("Alex-Li Tandem sells autographs. He hunts for names on paper in "
     "a huge network of desire, collecting them, selling them and "
     "occasionally faking them; offering people a little piece of "
     "fame. To him, enlightenment is some part of himself that cannot "
     "be signed, celebrated or sold."),

    ("After a brilliant and fulfilling career, Charles Arrowby revels "
     "in his perfect refuge, an isolated home by the sea, but soon "
     "his complex past makes unbidden visits."),

    ("The eccentric behavior of a stranger brings excitement to a "
     "quiet Norwegian town."),

    ("Third grade is a sad time for Amber because her best friend "
     "Justin is getting ready to move to a distant state."),

    ("Recently inheriting his deceased dad's job as a dragon "
     "catcher/exterminator, Robert's new job creates conflicting "
     "issues for him because he actually likes the creatures that "
     "inhabit Bellemontagne and he has always dreamed of transcending "
     "his humble origin to someday become a prince's valet."),

    ("In 1620, a boy and his dog are rescued from the doomed ship, "
     "Flying Dutchman, by an angel who guides them in traveling the "
     "world, eternally helping those in great need."),

    ("Jessie Sullivan is summoned home to tiny Egret Island, where she "
     "meets Brother Thomas, a monk who is about to take his final "
     "vows, and encounters the legend of a mysterious chair dedicated "
     "to a saint who had originally been a mermaid."),

    ("Jeremy Jacob joins Braid Beard and his pirate crew and finds "
     "out about pirate language, pirate manners, and other aspects "
     "of their life."),

    ("Informed that his clay pots and jugs are no longer needed, "
     "elderly potter Cipriano applies his craft to the making of "
     "ceramic dolls, but his family's subsequent successes are "
     "compromised by a terrible discovery."),

    ("Clennen and his family make their living as travelling "
     "musicians. A danger deepens around them, Moril is chosen to "
     "receive the mysterious musical instrument - the ancient "
     "cwidder."),

    ("Sixteen-year-old Zoey Redbird is Marked as a fledging vampyre "
     "and joins the House of Night where she will train to become "
     "an adult vampyre."),

    ("At Dupont University, an innocent college freshman named "
     "Charlotte Simmons learns that her intellect alone will not "
     "help her survive."),

    ("Retired life insurance salesman Nathan Glass moves to Brooklyn "
     "to find anonymity and solitude through his declining years, "
     "but a chance meeting with Tom Wood, his long-lost nephew, "
     "forces him to come to terms with his past."),

    ("Darren begins the Trials of Initiation to prove himself worthy "
     "of being a half-vampire, even as the clan's blood foes, the "
     "vampaneze, gather near Vampire Mountain."),

    ("There are new evils, new dangers to threaten Roland's little "
     "band in the devastated city of Lud and the surrounding "
     "wastelands, as well as horrific confrontations with Blaine "
     "the Mono, the piratical Gasher, and the frightening Tick-Tock "
     "Man."),

    ("While working in her father's tavern one evening, Maggie "
     "Nightingale overhears a dark plan which compels her to join "
     "a smuggler and flee on a ship to the New World in an attempt "
     "to escape the threats that haunt her."),

    ("Shocking revelations challenge the beliefs of the Druids and "
     "their comrades as they continue to battle the unspeakable "
     "forces of darkness that threaten to engulf them."),

    ("Twenty years after Grianne Ohmsford abandoned her life as the "
     "evil Ilse Witch to lead the Druid Council protecting the Four "
     "Lands, she disappears, and it is up to her nephew Pen and his "
     "comrades to go to her rescue."),

    ("Twenty-seven-year-old Mark Schluter, suffering from a rare brain "
     "disorder that causes him to believe his sister to be an impostor, "
     "endeavors to discover the cause of the motor vehicle accident that "
     "resulted in his head injury."),

    ("Autograph trader Alex-Li Tandem embarks on an odyssey that takes him "
     "from London to New York in pursuit of the only autograph that has ever "
     "really mattered to him, dealing with con men and fellow collectors who "
     "would hinder his quest."),

    ("When a young woman threatens to expose a damaging secret from his "
     "former life, Axel Vander, an elderly scholar and master liar, is forced "
     "to examine his past to uncover the truths that he has so carefully "
     "hidden."),

    ("Two birds unwittingly hatch an alligator egg, which has been accidently "
     "placed in their nest, and then try to teach their 'son' to fly."),

    ("For Milo, everything's a bore. When a tollbooth mysteriously appears in "
     "his room, he drives through only because he's got nothing better to do. "
     "But on the other side, things seem different. Milo visits the island of "
     "Conclusions (you get there by jumping), learns about time from a tick "
     "watchdog named Tock, and even embarks on a quest to rescue Rhyme and "
     "Reason! Somewhere along the way, Milo realizes something astonishing. "
     "Life is far from dull. In fact, it's exciting beyond his wildest "
     "dreams!"),

    ("Having escaped to the Unknown Regions, Lina and the others seek help "
     "from the village people of Sparks."),

    ("Lucy hears sneaking, creeping, crumpling noises coming from inside the "
     "walls. She is sure there are wolves living in the walls of her house."),

    ("When teenager Carmen and her three friends discover that a pair of worn "
     "jeans from a thrift shop provides an uncanny fit for all four of them, "
     "they decide to form a sisterhood, with the pants as the symbolic bond "
     "of friendship among them, and embark on a sweet-sixteen summer."),

    ("Fearing that her psychic abilities have damaged her chances of having a "
     "healthy relationship, Clare Lancaster travels to California to assist "
     "her father's business and meets financial consultant Jake Salter, with "
     "whom she shares an unlikely chemistry."),

    ("Sorcery is the legacy of Gillian and Sally Owens, a legacy they both "
     "try to escape until they realize their magic is a gift, not an "
     "affliction."),

    ("Underwater adventurer Dirk Pitt and the NUMA crew investigate a black "
     "tide infesting the ocean off Nicaragua, a study complicated by the "
     "discovery of a mysterious artifact, a powerful storm, and a "
     "conspiracy."),

    ("Bitten by a vampire after being mistaken for her Goth twin sister, "
     "Rayne, sixteen-year-old Sunny is in a race against time as she tries "
     "to prevent herself from becoming a vampire permanently."),

    ("Two discarded toy mice survive perilous adventures in a hostile world "
     "before finding security and happiness with old friends and new."),

    ("Abby enjoys writing the advice column for the fifth-grade newspaper "
     "until people become upset with some of her answers, but then the "
     "opportunity comes along to use her writing skills to help a friend."),

    ("When young Elana unexpectedly joins the team leaving the spaceship "
     "to study the planet Andrecia, she becomes an integral part of an "
     "adventure involving three very different civilizations, each one "
     "centered on the third planet from the star in its own solar system."),

    ("Soren has been reunited with his sister, Eglantine, but now he must "
     "deal with the mysterious disappearance of his mentor, Ezylryb, and "
     "in his attempt to save his teacher must fight a formidable foe."),

    ("Tal has spent his whole life in the darkness. He knows nothing else "
     "of the world. Far below the Castle, there lives an Icecarl warrior "
     "named Milla. Her fate and Tal's are irreversibly linked. Together "
     "they will discover the secrets behind the veil and the forces "
     "desperately trying to tear it apart."),

    ("A young scientist's adventures with refractions of light bring terror "
     "to the residents of Burdock."),

    ("Rapunzel is jealous when Prince Val begins ignoring her in favor of "
     "Rose, and she faces trouble when witch Madame Gothel discovers that "
     "she has been sneaking out of the tower to attend Princess School."),

    ("There are some pretty weird grown-ups living in Bailey City. But could "
     "the presidential candidate visiting town really be a werewolf? The "
     "Bailey School kids are going to find out!"),

    ("Rachel and Kirsty follow a trail of sparkly yellow dust to try and "
     "rescue Sunny, one of the colorful rainbow fairy sisters."),

    ("Briar Rose lands the role of Princess Perfecta in the school play and "
     "Nettle, who plays opposite Rose, seems almost too perfect as the evil "
     "fairy."),

    ("When strange things start happening and eight-year-old Mabel, who is "
     "very sensible, cannot figure them out, she discovers a family secret "
     "that affects her younger sister Violet."),

    ("When Violet conjures a pool for their yard and refuses to make it "
     "disappear, Mabel, who is not magical, does not know how to explain "
     "this to their parents."),

    ("Follows the adventures of Soren, an orphaned barn owl that is "
     "captured and taken to St. Aegolius Academy where he becomes caught "
     "up in a battle between good and evil."),

    ("Thirteen-year-old J.D. struggles to understand who she is, where she "
     "came from, and why she has nightmares."),

    ("The time is 1771 and the colony of North Carolina teeters on an "
     "uneasy edge. Jamie Fraser is a man of worth but he has a lot to "
     "lose. His wife, Claire, is known notoriously as a wisewoman or a "
     "witch. They both know they have to survive."),

    ("Seventeen-year-old Jessica Allodola discovers that the vampire world "
     "of her fiction is real when she develops relationships with an "
     "alluring vampire named Aubrey and the teenage witch who is trying "
     "to save Jessica from his clutches."),

    ("Unhappy about his baby sister's illness and the chaos of moving into "
     "a dilapidated old house, Michael retreats to the garage and finds a "
     "mysterious stranger who is something like a bird and something like "
     "an angel."),

    ("Determined to become a doctor like her father when she grows up, "
     "Katy has a good sense for people and their sicknesses, so when she "
     "befriends Jacob, she sees that there is something in him that needs "
     "to be revealed."),

    ("Merlin must find his stolen sword in order to repel an encroaching "
     "evil intent on destroying the magic isle of Fincayra. But first he "
     "must confront a magical mirror that alters one's destiny."),

    ("Ellie's first term at the Royal Ballet School is filled with "
     "excitement, hard work, homesickness, an unexpected chance to perform, "
     "and new friendships, tainted only by the rude and hateful behavior of "
     "Lara, the girl she crashed into during their audition."),

    ("In their second term at the Royal Ballet School, Ellie and her friends "
     "prepare for an important appraisal of their dancing while also trying "
     "to get along with Isabelle, an unfriendly new girl."),

    ("Ten years ago, the American spy satellite Medusa malfunctioned and "
     "crashed - but not before its sensors revealed a secret buried deep in "
     "the Earth, hidden for thousands of years from the eyes of man. It's a "
     "priceless discovery that some will die to find - and kill to possess."),

    ("Dr. Philip Mercer, a wealthy geologist charged with overseeing the "
     "installation of a temporary nuclear waste holding tank at Nevada's "
     "infamous Area 51, discovers a secret group called the Order and their "
     "plans for world domination."),

    ("The dramatic eruption of a volcano in the Pacific Ocean results in a "
     "world-wide battle for domination when it becomes obvious that Vulcan's "
     "Forge can provide a limitless supply of clean nuclear energy."),

    ("After Weather Warden Joanne Baldwin prevents Mother Earth from "
     "destroying the planet, she struggles to recover her identity after "
     "losing her memories at the hands of a vengeful jinn."),

    ("A man seeking to destroy the werewolf who bit him comes across a "
     "strange beauty who takes him to the Canadian Northwest and shows him "
     "the way of the wolf."),

    ("As the powerful vampire Lilith prepares to quench her thirst for "
     "destruction by unleashing her fury in battle, a medieval sorcerer, one "
     "the circle of six charged by the goddess Morrigan, must travel through "
     "time to stop her."),

    ("Follows the circle of six as they protect the world - and their hearts "
     "- from a vampire who is determined to rule the earth."),

    ("The twins graduate-and say goodbye to SVH for good. Elizabeth can't "
     "believe she's finally turning 18 and graduating high school. She's been "
     "waiting for this moment her entire life. She can't wait to say good-bye "
     "to the past and start a new life. And the best part of it all-she gets "
     "to do it with her twin sister. But for Jessica, the only thing worse "
     "than turning 18 is turning 18 and graduating the same week. What if "
     "she's not ready for her entire life to change? And what if it means "
     "losing her sister?"),

    ("Molly and Neil Sloan and their neighbors in a small California mountain "
     "town encounter a threat that transforms their peaceful streets into a "
     "ghostly labyrinth as they discover the horrifying reality of what is "
     "happening around them."),

    ("Just as the Headmaster of Macdonald Hall is on the verge of retirement, "
     "a wave of practical jokes hits the school, and roommates Bruno and "
     "Boots become prime suspects."),

    ("In northern England in 1842, fourteen-year-old Lucas leads a lonely, "
     "monotonous existence in the house of his unpleasant guardian until the "
     "unexpected arrival of an unusual little girl presages a series of "
     "events that completely change his life."),

    ("On his way to town to have some fun, a lazy but clever young man faces "
     "a terrible demon, who declares that his time has come."),

    ("A fantasy adventure saga set in the early days of Middle-Earth features "
     "humans and elves, dwarves and dragons, orcs and dark sorcerers clashing "
     "in an epic battle between good and evil."),

    ("Follows the adventures of young Fabrizio del Dongo as he joins "
     "Napoleon's army just before the Battle of Waterloo, and struggles to "
     "keep hidden his love for Clelia amid the intrigues and secrets of the "
     "small court of Parma."),

    ("The magic tree house takes Jack and Annie to San Francisco in 1906, in "
     "time for them to experience one of the biggest earthquakes the United "
     "States had ever known."),

    ("Pandora the cat becomes a lighthouse keeper and saves the life of "
     "Seabold the dog, and together the two of them create a family with "
     "three young mice rescued from the sea."),

    ("Menolly flees her home, because she is not permitted to make music "
     "there, and is taken by the Masterharper himself to Harpershall, where "
     "she learns that only her own self-doubt stands in her way."),

    ("Two mice that live in a lighthouse along with a dog, a cat, and another "
     "mouse, lose their compass while exploring the forest, and learn to use "
     "their instincts before being rescued by an eagle."),

    ("In a future society that has decided it would 'rather be safe than "
     "free,' sixteen-year-old Bo's anger control problems land him in a "
     "tundra jail where he survives with the help of his running skills and "
     "an artificial intelligence program named Bork."),

    ("Problems arise for Amelia when she starts sixth grade at the same "
     "middle school where her older sister Cleo is an eighth-grader, and she "
     "gets the school's meanest teacher for three of her classes."),

    ("Three girls with three agendas and the ultimate destination: the "
     "Hamptons. Summer in the city? Way overrated. Everybody who's anybody in "
     "New York City summers in the Hamptons. Mara, Eliza, and Jacqui all want "
     "a piece of the action, all for different reasons. So the girls answer a "
     "classified ad to become au pairs. How bad can it be, watching a couple "
     "of kids on the beach all day? They've got the swank address, the sweet "
     "ride, and an all-access pass to the hottest social scene on the East "
     "Coast. It's shaping up to be the summer of their lives."),

    ("PopTV is going to follow Star around for twenty-four hours and her team "
     "is very excited, but everything begins to go wrong once the cameras "
     "start rolling."),

    ("Relates how the barnyard collie and pups rescue Jemima Puddle-Duck from "
     "the fox's cooking pot."),

    ("When the evil wizard Destiny kidnaps Pixel, Score and Helaine must "
     "rescue him from the planet Zarathan, where nightmares come true and "
     "those who fall asleep die."),

    ("Sabriel and Lirael must battle against ancient evils in order to "
     "protect the Old Kingdom and learn of their own destinies."),

    ("Still maintaining her guise as her deceased brother Noble, Celeste "
     "struggles to raise Baby Celeste, a child she is forced to deny as her "
     "own, but when her mother marries a kindly neighbor, vicious enemies "
     "threaten to reveal the truth."),

    ("On a fantastic island populated by unusual animals, a pirate captain "
     "finds a trustworthy companion in the little 'Yellow Creature.'"),

    ("When a third grade classmate gets her picture in the paper for winning "
     "a spelling bee, Judy is determined to find a way to become famous "
     "herself."),

    ("When twelve-year-old Daniel Cook and his sister, Beatrice, spend the "
     "summer at a special school run by their parents' eccentric former "
     "tutor, they are introduced to the secret study of dragonology and find "
     "themselves caught up in an evil plot."),

    ("In her first year at a New Jersey high school, Mary Elizabeth Cep, who "
     "now calls herself 'Lola,' sets her sights on the lead in the annual "
     "drama production, and finds herself in conflict with the most popular "
     "girl in school."),

    ("Ella has no interest in running for class president at her suburban New "
     "Jersey high school, but her offbeat friend Lola tricks her into "
     "challenging the rich and overbearing Carla Santini in a "
     "less-than-friendly race."),

    ("Judy Moody's new friendship with Amy Namey causes problems with her old "
     "friends and the school project they are working on together."),

    ("A case involving a trolley accident pits Kit against powerful railway "
     "men, all of whom have something to hide. The truth may blow the lid off "
     "a conspiracy, so will her enemies find a way to keep her silenced "
     "forever?"),

    ("Vicky's disappointment in the antique dollhouse she receives for her "
     "birthday gives way to curiosity as she is literally drawn into the "
     "lives of its unusual inhabitants."),

    ("In 1878, two young stage magicians clash in a darkened salon during the "
     "course of a fraudulent seance, and from this moment they try to expose "
     "and outwit each other at every turn."),

    ("After learning that he is the son of a mortal woman and Poseidon, god "
     "of the sea, twelve-year-old Percy is sent to a summer camp for demigods "
     "like himself, and joins his new friends on a quest to prevent a war "
     "between the gods."),

    ("When Odysseus must leave his home to fight the Trojan War, he never "
     "imagines that he'll be away from his family for so many years. Now, at "
     "long last, he is leading his men home across the seas. But many dangers "
     "await them - and none is more terrifying than Polyphemus, the one-eyed "
     "giant."),

    ("Eleven-year-old Oliver, an American boy residing in Paris, discovers, "
     "much to his astonishment, that phantoms live within the windowpanes and "
     "have selected Oliver to lead a war against the 'soul-stealers' that "
     "inhabit mirrors."),

    ("Follows the adventures and exploits of the minotaurs as they become "
     "caught up in the chaos, fallout, and changing destinies that resulted "
     "from the War of Souls."),

    ("During the forty years in which a rural southwestern backwater is "
     "transformed into a boomtown and industrial mecca, the townspeople try "
     "to adjust to their loss of land and heritage."),

    ("Named after a character in a Shakespeare play, misfit sixth-grader Hero "
     "becomes interested in exploring this unusual connection because of a "
     "valuable diamond supposedly hidden in her new house, an intriguing "
     "neighbor, and the unexpected attention of the most popular boy in "
     "school."),

    ("If Ruby Gloom's friends seem somewhat unusual, well then, welcome to "
     "Gloomsville, where being different IS normal."),

    ("Famed Hollywood actor Dayne Matthews struggles to deal with the "
     "shocking discoveries he has made about his past and to find the "
     "strength to forgive."),

    ("When Mr. Jelly, who is scared of everything, is kidnapped by pirates, "
     "the pirates quickly learn about his fears."),

    ("After a decade of spending a delightful summer week at their country "
     "house in New Hampshire, the members of the extended Seton family are "
     "confronted by a terrible accident, testing the values and relationships "
     "that hold them together."),

    ("Precious Ramotswe and her assistant, Grace Makutsi, investigate local "
     "advice columnist Aunty Emang, who may be linked to trouble at a local "
     "medical clinic and the cobra that somehow ended up in Precious's "
     "office."),

    ("Instead of remaining out of sight during her assignment to a forlorn "
     "outpost, spaceship commander Honor Harrington, along with her vessel, "
     "the Fearless, performs incredible flying maneuvers to stop a foreign "
     "takeover of a major space station."),

    ("During a dire battle against the fearsome Skinners, Daine and her mage "
     "teacher Numair are swept into the Divine Realms. Though happy to be "
     "alive, they are not where they want to be. They are desperately needed "
     "back home, where their old enemy, Ozorne, and his army of strange "
     "creatures are waging war against Tortall. Trapped in the mystical "
     "realms, Daine discovers her mysterious parentage. And as these secrets "
     "of her past are revealed, so is the treacherous way back to Tortall. So "
     "they embark on an extraordinary journey home, where the fate of all "
     "Tortall rests with Daine and her wild magic."),

    ("While visiting his grandmother on Cape Cod, nine-year-old Thomas "
     "encounters a ship's cabin boy from centuries past."),

    ("Eliza, Jacqui, and Mara are just beginning their new careers, but find "
     "themselves all together in the Hamptons once again since Eliza's new "
     "stepmother needs a nanny."),

    ("When the Elric brothers travel to an old mining town and encounter "
     "powerful alchemists, sparks fly in this paradise they have discovered."),

    ("Still on a mission to find the legendary Sword of Cortes, the crew of "
     "the Barnacle becomes entranced by an ethereal song that pulls them away "
     "from their mission, leaving Captain Jack Sparrow to have to find the "
     "source behind the dark spell."),

    ("This is it! Jack and his crew have found the Sword of Cortes, but along "
     "with it, they've also found Cortes himself. And he's not the kind ruler "
     "they thought he'd be. Jack and his crew have defeated a storm king, "
     "escaped sirens, defeated the notorious pirate Left Foot Louis, but can "
     "they possibly conquer a conquistador with god-like powers?"),

    ("Sally looked contentedly down the long table. She felt happy at last. "
     "Everybody was talking and laughing now, and her party, rallying after "
     "an uncertain start, was plainly the success she had hoped it would be."),

    ("On her first day of first grade, despite the objections of her older "
     "sisters, Suki chooses to wear her beloved Japanese kimono to school "
     "because it holds special memories of her grandmother's visit last "
     "summer."),

    ("A trunk that Nancy receives from her father for a trip to Buenos Aires "
     "becomes the center of a mystery."),

    ("Continues the adventures of the Flash as he battles evil foes and helps "
     "justice to prevail."),

    ("Sunita and her fellow volunteers at the Wild at Heart veterinary clinic "
     "become involved in efforts to save a bunch of feral and abandoned cats "
     "with the help of Dr. Mac."),

    ("The overman named Garth sought immortal fame. The oracle told him to "
     "serve the Forgotten King to get that fame. But this King sent Garth "
     "after a basilisk whose gaze could turn men to stone. What sane use "
     "could anyone have for a monster like that?"),

    ("In 1166 the Saxon knight Ivanhoe returns from the Crusades to a chaotic "
     "England ruled by the enemies of the absent King Richard the "
     "Lion-Hearted  and finds himself disowned and dishonored, forced to "
     "fight for his name and the people he loves."),

    ("When his father relocates the family to Paradise to work for the "
     "mysterious Eden Corporation, Jack Barrett uncovers a sinister plot that "
     "threatens everyone he loves."),

    ("When Kendra and Seth go to stay at their grandparents' estate, they "
     "discover that it is a sanctuary for magical creatures and that a battle "
     "between good and evil is looming."),

    ("Two sisters, one practical and conventional and the other emotional and "
     "sentimental, find that only through compromise of their mutual "
     "differences can they get along."),

    ("Sherlock Holmes and Dr. Watson travel to the bleak wastes of Dartmoor "
     "to solve the mystery surrounding the late Sir Charles Baskerville and a "
     "ghostly hound."),

    ("Sent to stay with their uncle in a ship-like home called Drift House, "
     "twelve-year-old Susan and her stepbrothers embark on an adventure "
     "involving duplicitous mermaids, pirates, and an attempt to stop time "
     "forever."),

    ("In the year 2100, mankind on Earth, settlers in a lunar colony and "
     "aliens from the para-universe, a strange universe parallel in time to "
     "our own, are faced with a race against time to prevent total "
     "destruction of the Earth. The invention of the Inter-Universe Electron "
     "Pump has threatened the rate of hydrogen fusion in the sun, leading, "
     "inevitably, to the possibility of a vast explosion - and the "
     "vapourisation of the Earth exactly eight minutes later."),

    ("Emma Watson a research physician has been training for the mission of a "
     "lifetime: to study living organisms in the microgravity of space. But "
     "the true and lethal nature of the experiment has not been revealed to "
     "NASA and once aboard the space station things start to go wrong. A "
     "culture of single-celled Archaeons, gathered from the deep sea, begin "
     "to rapidly multiply and infect the crew - with deadly and agonizing "
     "results. As her estranged husband and ground crew at NASA work against "
     "the clock to launch a rescue, Emma struggles to contain the lethal "
     "microbe. But with the contagion threatening Earth's population, there "
     "are those who would leave the astronauts stranded in orbit, quarantined "
     "aboard the station."),

    ("Four English school children enter the magic land of Narnia through the "
     "back of a wardrobe and assist Aslan, the golden lion, in defeating the "
     "White Witch who has cursed the land with eternal winter."),

    ("A nightmarish danger threatens from the other side of reality. Armed "
     "with only a frying pan and her common sense, young witch-to-be Tiffany "
     "Aching must defend her home against the monsters of Fairyland. Luckily "
     "she has some very unusual help: the local Nac Mac Feegle - aka the Wee "
     "Free Men - a clan of fierce, sheep-stealing, sword-wielding, "
     "six-inch-high blue men. Together they must face headless horsemen, "
     "ferocious grimhounds, terrifying dreams come true, and ultimately the "
     "sinister Queen of the Elves herself."),

    ("Working as a secretary at the British Embassy on Crete, Nicola Ferris "
     "is enjoying a day off when she meets up with two hiking companions who "
     "accidentally stumbled into the middle of a terrifying act of "
     "vengeance."),

    ("Drafted into the ranks of Earth's interstellar warriors, private "
     "William Mandella finds his fight against the Taurans secondary to the "
     "side effects of faster-than-light space travel, which affects the rate "
     "at which he ages."),

    ("Former pop star Heather Wells has left behind hordes of screaming fans, "
     "to settle into a new adult life, but when strange things start "
     "happening at her college, she finds herself once again in the "
     "spotlight, this time starring as a spunky female detective."),

    ("In Echo Falls you never know what's coming next - and everyone has a "
     "secret. Things are amiss at 99 Maple Lane: Ingrid's dad's job is in "
     "jeopardy, but he won't explain why. Ingrid's brother, Ty, is getting "
     "buff - really buff - but when Ty starts getting moody, Ingrid wonders "
     "if there's more to his physical fitness than lifting weights. "
     "Meanwhile, Ingrid's beloved soccer coach is replaced by an icy newcomer "
     "named Julia LeCaine, who seems a little too savvy to be in it for the "
     "postgame pizza. True to her hero, Sherlock Holmes, Ingrid begins "
     "fishing around to find out who's really pulling the strings in Echo "
     "Falls. But one morning, while en route to the dreaded MathFest, Ingrid "
     "is kidnapped and locked in the trunk of a car. Even if she escapes, "
     "will anyone believe her story?"),

    ("After pitched battle, The White - the avatars of the Five Gods - have "
     "briefly turned back the vicious invaders. And now, the priestess "
     "Auraya is sent on an urgent mission to reconcile with the powerful, "
     "outcast Dreamweavers, for their magical healing abilities may be the "
     "key to saving the land. But as a deadly plague devastates their allies "
     "and old adversaries resurface, a dreadful surprise may ruin the chance "
     "for peace. For Auraya's terrible discovery will force her into a "
     "desperate choice - one whose consequences will change the world "
     "forever."),

    ("Sixteen-year-old Steph Landry finds an old book on how to be popular "
     "and decides to change her social status by following its advice, much "
     "to the bafflement of her two best friends."),

    ("During their first four years of marriage, Laura and Almanzo Wilder "
     "have a child and fight a losing battle in their attempts to succeed at "
     "farming on the South Dakota prairie."),

    ("Novelist George Webber is driven from his hometown when his successful "
     "autobiographical novel infuriates the family and friends he has "
     "depicted in it."),

    ("Gurgeh, a champion game player, travels a hundred thousand light years "
     "to the Empire of Azad, where the winner of their complex game becomes "
     "emperor."),

    ("When Jessica marries David, he is everything she wants in a family man: "
     "brilliant, attentive, ever youthful. Yet she still feels something "
     "about him is just out of reach. Soon, as people close to Jessica begin "
     "to meet violent, mysterious deaths, David makes an unimaginable "
     "confession: More than 400 years ago, he and other members of an "
     "Ethiopian sect traded their humanity so they would never die, a secret "
     "he must protect at any cost. Now, his immortal brethren have decided "
     "David must return and leave his family in Miami. Instead, David vows "
     "to invoke a forbidden ritual to keep Jessica and his daughter with "
     "him forever."),

    ("It's been quite a week for Joe Grey. First the large, powerful feline "
     "discovers that, through some strange, inexplicable phenomenon, he now "
     "has the ability to understand human language. Then he discovers he can "
     "speak it as well! It's a nightmare for a cat who'd prefer to sleep the "
     "day away carefree, but Joe can handle it. That is, until he has the "
     "misfortune to witness a murder in the alley behind Jolly's Deli - and "
     "worse, to be seen witnessing it. With all of his nine lives suddenly "
     "at risk, Joe's got no choice but to get to the bottom of the heinous "
     "crime - because his mouse-hunting days are over for good unless he can "
     "help bring a killer to justice."),

    ("In Coraline's family's new flat there's a locked door. On the other "
     "side is a brick wall - until Coraline unlocks the door ... and finds a "
     "passage to another flat in another house just like her own. Only "
     "different. The food is better there. Books have pictures that writhe "
     "and crawl and shimmer. And there's another mother and father there who "
     "want Coraline to be their little girl. They want to change her and keep "
     "her with them. Forever."),

    ("Young Tristran Thorn will do anything to win the cold heart of "
     "beautiful Victoria - even fetch her the star they watch fall from the "
     "night sky. But to do so, he must enter the unexplored lands on the "
     "other side of the ancient wall that gives their tiny village its name. "
     "Beyond that old stone wall, Tristran learns, lies Faerie - where "
     "nothing, not even a fallen star, is what he imagined."),

    ("When a strange little man comes to the Coven Tree Church Social "
     "promising he can give people exactly what they ask for, three young "
     "believers-in-magic each make a wish that comes true in the most "
     "unexpected way."),

    ("In the land of Ingary, such things as spells, invisible cloaks, and "
     "seven-league boots were everyday things. The Witch of the Waste was "
     "another matter. After fifty years of quiet, it was rumored that the "
     "Witch was about to terrorize the country again. So when a moving black "
     "castle, blowing dark smoke from its four thin turrets, appeared on the "
     "horizon, everyone thought it was the Witch. The castle, however, "
     "belonged to Wizard Howl, who, it was said, liked to suck the souls of "
     "young girls. The Hatter sisters - Sophie, Lettie, and Martha - and all "
     "the other girls were warned not to venture into the streets alone. But "
     "that was only the beginning. In this giant jigsaw puzzle of a fantasy, "
     "people and things are never quite what they seem. Destinies are "
     "intertwined, identities exchanged, lovers confused. The Witch has "
     "placed a spell on Howl. Does the clue to breaking it lie in a famous "
     "poem? And what will happen to Sophie Hatter when she enters Howl's "
     "castle?"),

    ("Strange things happen at Hexwood Farm. From her window, Ann Stavely "
     "watches person after person disappear through the farm's gate - and "
     "never come out again. Later, in the woods nearby, she meets a "
     "tormented sorcerer, who seems to have arisen from a centuries-long "
     "sleep. But Ann knows she saw him enter the farm just that morning. "
     "Meanwhile, time keeps shifting in the woods, where a small boy - or "
     "perhaps a teenager - has encountered a robot and a dragon. Long before "
     "the end of their adventure, the strangeness of Hexwood has spread from "
     "Earth right out to the center of the galaxy."),

    ("Retired literary agent Joe Allston passes through life as a spectator "
     "until he discovers the journals of a trip he took to his mother's "
     "birthplace years before."),

    ("Max finds himself in possession of a time travel device which is "
     "eagerly sought by two desperate men, the scientist who invented it and "
     "the scientist's alter ego from a different timeline."),

    ("Sixteen-year-old David, finding a strange machine that creates replicas "
     "of living organisms, duplicates himself and suffers the horrible "
     "consequences when the duplicate turns against him."),

    ("In a world where one can literally get lost in literature, Thursday "
     "Next, a Special Operative in literary detection, tries to stop the "
     "world's Third Most Wanted criminal from kidnapping characters, "
     "including Jane Eyre, from works of literature."),

    ("A young girl from an advanced civilization is sent as an observer to a "
     "planet whose people have not yet learned to control their use of atomic "
     "power."),

    ("After dreaming that they must leave their isolated home of Riverworld, "
     "Kyreol and Terje travel beyond what they believe to be end of the "
     "world, where they discover new planets and new ways of life."),

    ("Each of five children lucky enough to discover an entry ticket into Mr. "
     "Willy Wonka's mysterious chocolate factory takes advantage of the "
     "situation in his own way."),

    ("Pete, a talented musician intent on putting the music first, faces a "
     "tough decision when he joins a popular but uninspiring band on the "
     "verge of stardom."),

    ("When a young man in the Uplands blinds himself rather than use his gift "
     "of \"unmaking\" - a violent talent shared by members of his family - he "
     "upsets the precarious balance of power among rival, feuding families, "
     "each of which has a strange and deadly talent of its own."),

    ("A classic science fiction novel features humanoids spreading throughout "
     "the galaxy, threatening to stifle all human endeavor, and the hidden "
     "group of rebels who try to stem the humanoid tide, if it is not already "
     "too late."),

    ("When Bill comes home with a strange guest, it proves to be the "
     "beginning of an adventure involving a travelling circus and a castle "
     "with secret passages."),

    ("Raised on a planet at the remote edge of the universe, the daughter of "
     "Arthur Dent sets out on a transgalactic quest to find the planet of her "
     "ancestors."),

    ("Twelve-year-old Jack Sawyer braves the mysterious dangers of the "
     "Territories, a surreal parallel world, in his cross-country quest "
     "through the U.S. for the Talisman, the only hope for his dying mother "
     "and for his own survival."),

    ("As a Great Darkness threatens to engulf the entire universe, Flinx and "
     "his mini-dragon companion Pip may finally get the chance to face down "
     "the ultimate evil."),

    ("The factions in the embattled Commonwealth must come together to battle "
     "not only the predatory alien species, the Prime, but also the "
     "Starflyer, a mysterious and undetectable alien with irresistible "
     "mind-control abilities.")
]
