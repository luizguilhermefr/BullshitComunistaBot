"""
    Todas as frases usurpadas, ou melhor,
     socializadas de https://github.com/asgunzi/BullshitComunista
"""
import random

tab0 = [
    "Certos serviços ou os valores de uso resultantes de certas atividades ou trabalhos corporificam-se em mercadorias",
    "Ainda que as circunstâncias tenham mudado muito nos últimos vinte e cinco anos",
    "Infere-se daí que a mera troca de dinheiro por trabalho não transforma este ",
    "Compro o trabalho de alfaiate em virtude do serviço que presta como trabalho de alfaiate",
    "Que partido de oposição não foi acusado de comunista por seus adversários no poder? Que partido de oposição",
    "É tempo de os comunistas exporem",
    "O Homem livre e escravo",
    "Nas primeiras épocas históricas",
    "A sociedade burguesa moderna",
    "A descoberta da América",
    "A antiga organização feudal da indústria",
    "A grande industria criou o mercado mundial preparado pela descoberta da América. O mercado mundial acelerou prodigiosamente o desenvolvimento do comércio",
    "Cada etapa da evolução percorrida pela burguesia era acompanhada de um progresso político correspondente. Classe oprimida pelo despotismo feudal",
    "Onde quer que tenha conquistado o Poder",
    "A burguesia despojou de sua auréola todas as atividades até então reputadas veneráveis e encaradas com piedoso respeito. ",
    "A burguesia revelou como a brutal manifestação de força na Idade Média",
    "A burguesia só pode existir com a condição de revolucionar incessantemente os instrumentos de produção",
    "Impelida pela necessidade de mercados sempre novos",
    "Pela exploração do mercado mundial a burguesia imprime um caráter cosmopolita à produção e ao consumo em todos os países. Para desespero dos reacionários",
    "Devido ao rápido aperfeiçoamento dos instrumentos de produção e ao constante progresso dos meios de comunicação",
    "A burguesia submeteu o campo à cidade. Criou grandes centros urbanos; aumentou prodigiosamente a população das cidades em relação à dos campos e",
    "A burguesia suprime cada vez mais a dispersão dos meios de produção",
    "Vemos pois: os meios de produção e de troca",
    "Assistimos hoje a um processo semelhante. As relações burguesas de produção e de troca",
    "O crescente emprego de máquinas e a divisão do trabalho",
    "A indústria moderna transformou a pequena oficina do antigo mestre da corporação patriarcal na grande fábrica do industrial capitalista. Massas de operários",
    "Quanto menos o trabalho exige habilidade e força",
    "Depois de sofrer a exploração do fabricante e de receber seu salário em dinheiro",
    "As camadas inferiores da classe média de outrora",
    "Os operários triunfam às vezes; mas é um triunfo efêmero. O verdadeiro resultado de suas lutas não é o êxito imediato",
    "A organização do proletariado em classe e",
    "De todas as classes que ora enfrentam a burguesia",
    "As classes médias - pequenos comerciantes",
    "O lumpen-proletariado e suas relações com a mulher e os filhos nada têm de comum com as relações familiares burguesas. O trabalho industrial moderno",
    "Nas condições de existência do proletariado já estão destruídas as da velha sociedade. O proletariado não tem propriedade; ",
    "Todas as classes que no passado conquistaram o Poder",
    "Todos os movimentos históricos têm sido",
    "A luta do proletariado contra a burguesia e as lumpen autoridades ",
    "Esboçando em linhas gerais as fases do desenvolvimento proletário",
    "A condição essencial da existência e da supremacia da classe burguesa é a acumulação da riqueza nas mãos dos particulares",
    "Não proclamam princípios particulares",
    "Os comunistas só se distinguem dos outros partidos operários em dois pontos: 1) Nas diversas lutas nacionais dos proletários",
    "O objetivo imediato dos comunistas é o mesmo que o de todos os demais partidos proletários: constituição dos proletários em classe",
    "As concepções teóricas dos comunistas não se baseiam",
    "Ser capitalista significa ocupar não somente uma posição pessoal",
    "O preço médio que se paga pelo trabalho assalariado é o mínimo de salário",
    "É a abolição de semelhante estado de coisas que a burguesia verbera como a abolição da individualidade e da liberdade. E com razão. Porque se trata efetivamente de abolir a individualidade burguesa",
    "Horrorizai-vos porque queremos abolir a propriedade privada. Mas em vossa sociedade a propriedade privada está abolida para nove décimos de seus membros. E é precisamente porque não existe para estes nove décimos que ela existe para vós. Acusai-nos",
    "Desde o momento em que o trabalho não mais pode ser convertido em capital",
    "As acusações feitas contra o modo comunista de produção",
    "Mas não discutais conosco enquanto aplicardes à abolição da propriedade burguesa o critério de vossas noções burguesas de liberdade",
    "A falsa concepção interesseira que vos leva a erigir em leis eternas da natureza e da razão as relações sociais oriundas do vosso modo de produção e de propriedade - relações transitórias que surgem e desaparecem no curso da produção - a compartilhais com todas as classes dominantes já desaparecidas. O que admitis; para a propriedade antiga",
    "Sobre que fundamento repousa a família atual",
    "E vossa educação não é também determinada pela sociedade",
    "As declamações burguesas sobre a família e a educação",
    "Toda a burguesia grita em coro, ",
    "Os operários não têm pátria. Não se lhes pode tirar aquilo que não possuem. Como",
    "As demarcações e os antagonismos nacionais entre os povos desaparecem cada vez mais com o desenvolvimento da burguesia",
    "A supremacia do proletariado fará com que tais demarcações e antagonismos desapareçam ainda mais depressa. A ação comum do proletariado",
    "Quanto às acusações feitas aos comunistas em nome da religião",
    "Será preciso grande perspicácia para compreender que as idéias",
    "Quando se fala de idéias que revolucionam uma sociedade inteira",
    "Quando o mundo antigo declinava",
    "Mas qualquer que tenha sido a forma desses antagonismos",
    "A revolução comunista é a ruptura mais radical com as relações tradicionais de propriedade; nada de estranho",
    "O proletariado utilizará sua supremacia política para arrancar pouco a pouco todo capital à burguesia",
    "Isto naturalmente só poderá realizar-se",
    "Multiplicação das fábricas e dos instrumentos de produção pertencentes ao Estado",
    "Trabalho obrigatório para todos",
    "Uma vez desaparecidos os antagonismos de classe no curso do desenvolvimento",
    "Em lugar da antiga sociedade burguesa",
    "Devido à sua posição histórica",
    "Assim nasceu o socialismo feudal",
    "Quando os campeões do feudalismo demonstram que o modo de exploração feudal era diferente do da burguesia",
    "Nada é mais fácil que recobrir o ascetismo cristão com um verniz socialista. Não se ergueu também o cristianismo contra a propriedade privada",
    "Não é a aristocracia feudal a única classe arruinada pela burguesia",
    "Nos países onde a civilização moderna está florescente",
    "Esse socialismo analisou com muita penetração as contradições inerentes às relações de produção modernas. Pôs a nu as hipócritas apologias dos economistas. Demonstrou de um modo irrefutável os efeitos mortíferos das máquinas e da divisão do trabalho",
    "Sabe-se que os monges recobriam os manuscritos das obras clássicas da antigüidade pagã com absurdas lendas sabre santos católicos. Os literatos alemães agiram em sentido inverso a respeito da literatura francesa profana. Introduziram suas insanidades filosóficas no original francês. Por exemplo",
    "A esta interpolação da fraseologia filosófica nas teorias francesas deram o nome de filosofia da ação",
    "Esse socialismo alemão que tão solenemente levava a sério  seus desajeitados exercícios de escolar e que os apregoava tão charlatanescamente",
    "A luta da burguesia alemã e especialmente da burguesia prussiana contra os feudais e a monarquia absoluta",
    "Para os governos absolutos da Alemanha",
    "Se o verdadeiro socialismo se tomou assim uma arma nas mãos dos governos contra a burguesia alemã",
    "Mantê-la é manter na Alemanha o regime estabelecido. A supremacia industrial e política da burguesia ameaça a pequena burguesia de destruição certa",
    "A roupagem tecida com os fios Imateriais da especulação",
    "Proclamou que a nação alemã era a nação tipo e o filisteu alemão",
    "Nessa categoria enfileiram-se os economistas",
    "Os socialistas burgueses querem as condições de vida ela sociedade moderna sem as lutas e os perigos que dela decorrem fatalmente. Querem a sociedade atual",
    "Não se trata aqui da literatura que",
    "As primeiras tentativas diretas do proletariado para fazer prevalecer seus próprios interesses de classe",
    "Os sistemas socialistas e comunistas propriamente ditos",
    "Os fundadores desses sistemas compreendem bem o antagonismo das classes",
    "Como o desenvolvimento dos antagonismos de classes marcha de par com o desenvolvimento da indústria",
    "A atividade social substituem sua própria imaginação pessoal; às condições históricas da emancipação",
    "Quando a mercadoria chega ao lugar de destino",
    "Aqui nos limitamos apenas a tratar do capital produtivo",
    "Com o desenvolvimento do modo de produção especificamente capitalista",
    "É mesmo peculiar ao modo de produção capitalista separar os diferentes trabalhos",
    "Processo de produção do capital. Já vimos: esse processo de produção não é só processo de produção de mercadorias"
]

tab1 = [
    "adquire um caráter tão violento e agudo",
    "o que admitis para a propriedade feudal",
    "em todas as grandes ,evoluções modernas",
    "essa fantástica oposição que se lhe faz",
    "transforma o modo de produção; do outro",
    "mas o valor da força de trabalho. Dá-se",
    "apropriação de trabalho alheio não pago",
    "não é esse caráter concreto do trabalho",
    "podem ser ou apenas parecer necessários",
    "essa tendência se realiza cada vez mais",
    "o trabalho se corporifica na mercadoria",
    "a se tomarem burguesas. Em uma palavra",
    "empenham-se na luta operários isolados",
    "descrevemos a história da guerra civil",
    "onde se mesclavam jeremiadas e libelos",
    "por experiências em pequena escala que",
    "feita numa época em que o proletariado",
    "se personificam no capitalista. Eis aí",
    "o que diretamente se troca por capital",
    "de condições existentes em Roma Antiga",
    "diversa da característica determinante",
    "distinta dos produtores e consumidores",
    "em virtude da natureza dessa atividade",
    "constrangidos a vender-se diariamente",
    "que têm o mesmo caráter em toda parte",
    "compreende-se a liberdade de comércio",
    "com a abolição da propriedade privada",
    "a despeito de sua pomposa fraseologia",
    "amor e fidelidade pelo comércio de lã",
    "que se volta a atenção dos comunistas",
    "e é trabalho produtivo o trabalho que",
    "objeto de consumo pessoal. O dinheiro",
    "embora permaneça proprietário nominal",
    "os trabalhadores que produzem capital",
    "mesmo quando se dedica apenas à troca",
    "pedra angular das grandes monarquias",
    "satisfeitas pelos produtos nacionais",
    "a exploração de continentes inteiros",
    "sobre cuja base se ergue a burguesia",
    "frações inteiras da classe dominante",
    "a camada inferior da sociedade atual",
    "conseguia tornar-se membro da comuna",
    "da mesma forma que o pequeno burguês",
    "substitui o isolamento dos operários",
    "da filosofia e da ideologia em geral",
    "organização de exércitos industriais",
    "diretamente um interesse reacionário",
    "o fantástico afã de abstrair-se dela",
    "de apropriação de trabalho excedente",
    "uma como força produtiva do trabalho",
    "de ficar ela acrescida de mais-valia",
    "mas apenas se destinem a ser capital",
    "de fato portanto o próprio trabalho",
    "pois o uso dessa força é a ação dela",
    "transforma-se de imediato em capital",
    "não é a circunstância de representar",
    "dada quantidade desse trabalho geral",
    "serviço que transforma pano em calça",
    "de todo apagada ou mesmo inexistente",
    "fetiche na forma de metais preciosos",
    "estabeleceu-se a livre concorrência",
    "desenvolve-se também o proletariado",
    "a sujeição do operário pelo capital",
    "ao desaparecimento de toda produção",
    "em lugar de lhes dar uma nova forma",
    "que no curso de seu desenvolvimento",
    "se constitui forçosamente em classe",
    "a combinação na divisão do trabalho",
    "fora do relacionamento capitalista",
    "as condições materiais de trabalho)",
    "o professor tenha sucesso no ensino",
    "quando trabalha com capital próprio",
    "na sua aplicação elas envelheceram",
    "tudo o que era sagrado é profanado",
    "um só interesse nacional de classe",
    "mais fácil de aprender. Desse modo",
    "ligando-se à classe revolucionária",
    "tanto na Inglaterra como na França",
    "o capital é independente e pessoal",
    "as condições objetivas de trabalho",
    "na maquinaria para fins produtivos",
    "ao reproduzir o salário - portanto",
    "pelo tempo de trabalho de 12 horas",
    "a utilidade particular do trabalho",
    "sem fornecer mais-valia ao capital",
    "são eles produtores de mercadorias",
    "que também explora trabalho alheio",
    "decrescem os salários. Mais ainda",
    "mesmo no quadro de sua escravidão",
    "sem falar da prostituição oficial",
    "pelo menos nos países civilizados",
    "os organizadores de beneficências",
    "em valor adicionado de mais-valia",
    "consumada no processo de produção",
    "compra-se o trabalho como serviço",
    "são eles trabalhadores produtivos",
    "do ângulo da produção capitalista",
    "e o próprio produtor se biparte e",
    "demasiados meios de subsistência",
    "mas os inimigos de seus inimigos"
]

tab2 = [
    "meras relações de dinheiro em que não há vestígio de serviços pessoais mútuos entre suserano e vassalos. Ficção",
    "independentemente da nacionalidade. Nas diferentes fases por que passa a luta entre proletários e burgueses",
    "a finalidade real desse socialismo pequeno-burguês é ou restabelecer os antigos meios de produção e de troca e",
    "sejam quais forem às combinações sociais de que participem esses trabalhadores no processo de produção. Assim",
    "nem mercadoria para transformar primeiro em dinheiro e depois em valor de uso. Seu objetivo é o enriquecimento",
    "é o trabalhador que produz mercadoria vendável - mas só até o montante correspondente a sua força de trabalho",
    "é a última e mais perfeita expressão do modo de produção e de apropriação baseado nos antagonismos de classe",
    "o passado domina o presente; na sociedade comunista é o presente que domina o passado. Na sociedade burguesa",
    "a classe que traz em si o futuro. Do mesmo modo que outrora uma parte da nobreza passou-se para a burguesia",
    "do mesmo modo que a forma social geral do trabalho aparece no dinheiro como propriedade de uma coisa. Assim",
    "de lugar. Quanto ao transporte de  pessoas temos aí apenas serviço que lhes é prestado pelo empresário. Mas",
    "é incessantemente destruída pela concorrência que fazem entre si os próprios operários. Mas renasce sempre",
    "que deve nutri-lo em lugar de se fazer nutrir por ele. A sociedade não pode mais existir sob sua dominação",
    "todas as forças produtivas do trabalho social passam a desempenhar o papel de forças produtivas do capital",
    "uma relação que nada tem a ver com o autêntico modo de produção capitalista e não lhe está ainda subsumida",
    "essa roupagem na qual os socialistas alemães envolveram o miserável esqueleto das suas verdades eternas",
    "em conseqüência também à ciência e as forças naturais aparecem como forças produtivas do capital. De fato",
    "exigindo a produção de uma jarda de tecido por tear mecânico metade apenas do tempo requerido pelo manual",
    "os meios de produção e os meios de subsistência do trabalhador - só se torne capital por meio do processo",
    "podemos designar de trabalho produtivo o que se troca diretamente por dinheiro na qualidade de capital ou",
    "a exploração de uma parte da sociedade por outra é um fato comum a todos os séculos anteriores. Portanto",
    "embora à parte que varia diretamente seja apenas a desembolsada em salário. O valor se era igual a c + v",
    "que passam a entravá-las; e todas as vezes que as forças produtivas sociais se libertam desses entraves",
    "contra o burguês 'que os explora diretamente. Não se limitam a atacar as relações burguesas de produção",
    "por meio de vossas escolas etc.? Os comunistas não inventaram essa intromissão da sociedade na educação",
    "essa alteração ocorrida no valor de uso desapareceu e se expressa apenas no valor de troca mais elevado",
    " não afetam as  realizadas sobre a base das próprias relações entre o capital e o trabalho assalariado",
    "a produtividade do capital consiste em contrapor-se ele ao trabalho convertido em trabalho assalariado",
    "o capital absorve também as combinações sociais do trabalho e o desenvolvimento dos meios de trabalho",
    "atacam os instrumentos de produção: destróem as mercadorias estrangeiras que lhes fazem concorrência",
    "camponeses - combatem a burguesia porque esta compromete sua existência como classes médias. Não são",
    "o proletariado tem por objetivo conquistar o poder político e erigir-se em classe dirigente da nação",
    "empregado pelo dono da alfaiataria presta a esse capitalista não consiste em converter pano em calça",
    "reveste-se contudo dessa forma nos primeiros tempos. É natural que o proletariado de cada país deva",
    "a soma dos meios de subsistência necessária para que o operário viva como operário. Por conseguinte",
    "desde o momento em que a propriedade individual não possa mais converter-se em propriedade burguesa",
    "na luta política participam ativamente de todas as medidas de repressão contra a classe operária. E",
    "a proclamação da harmonia social e a transformação do Estado numa simples administração da produção",
    "e por isso as forças produtivas do trabalho desenvolvidas a partir dessas formas do trabalho social",
    "o valor do capital variável -  e ainda gerar mais-valia; e por meio desse processo de transformação",
    "é evidente que a crítica da literatura socialista apresenta uma lacuna em relação ao momento atual",
    "por trabalho que até então só existe como poder; e o que é comprado e vendido é o uso desse poder",
    "convertê-lo nesse valor de uso particular. O  dinheiro aí não exerce portanto a função de capital",
    "a que tem menos comando sobre os serviços de trabalhadores improdutivos é o trabalhador produtivo",
    "a abolição das relações burguesas de produção - o que só é possível por via revolucionária - mas",
    "antagonismo que mal começa e que esses autores somente conhecem em suas formas imprecisas. Assim",
    "desce cada vez mais abaixo das condições de sua própria classe. O trabalhador cai no pauperismo",
    "mas apenas enquanto é capital; esse poderio é tão-só o do trabalho materializado sobre o vivo",
    "não se apropriar do excesso do valor do produto acima do preço médio de sua jornada de trabalho",
    "os comunistas apoiam o partido que vê numa revolução agrária a condição da libertação nacional",
    "das forças naturais e dos produtos do trabalho só aparece mesmo como meio de explorar trabalho",
    "justamente para escamotear a relação específica. Na troca de dinheiro por trabalho improdutivo",
    "de modo que a burguesia fornece aos proletários os elementos de sua própria educação política",
    "que são comuns a todos os regimes sociais. Mas o comunismo quer abolir estas verdades eternas",
    "declarando que pairava imparcialmente acima de todas as lutas de classes. Com poucas exceções",
    "se o que está em jogo é apenas obtê-la. Compro a calça da alfaiataria que vende roupas feitas",
    "a quantidade de trabalho cresce com o desenvolvimento do maquinismo e da divisão do trabalho",
    "etc. Vossas próprias idéias decorrem do regime burguês de produção e de propriedade burguesa",
    "que a consciência do homem se modifica com toda mudança sobrevinda em suas condições de vida",
    "conformam-se perfeitamente em colher os frutos de ouro da árvore da indústria e trocar honra",
    "embora o valor da mercadoria vendida não seja o valor do trabalho (uma expressão irracional)",
    "configurar-se num valor de uso. E por conseguinte só trabalho que se apresenta em mercadoria",
    "a circulação do meu sangue e meu processo respiratório são condições para me enriquecer. Mas",
    "por prestar determinado serviço. Ele o compra por fornecer mais valor de troca do que custa",
    "embora não lhe estejam ainda subordinadas todas as relações de produção. Na sociedade feudal",
    "as duras exigências do pagamento à vista. Afogou os fervores sagrados do êxtase religioso",
    "constitui o proletariado massa disseminada por todo o país e dispersa pela concorrência. Se",
    "e sendo concentrada toda a produção propriamente falando nas mãos dos indivíduos associados",
    "como simples forma de existência dos meios de trabalho deles independentes e que os dominam",
    "e destruindo-lhe a capacidade autônoma de produzir - e quanto mais as condições de trabalho",
    "pode confundir estas duas perguntas - que é trabalho produtivo do ponto de vista do capital",
    "estabelecimentos de diversão etc. O ator se relaciona com o público na qualidade de artista",
    "aos meios de manutenção que lhe são necessários para viver e perpetuar sua existência. Ora",
    "fracassaram necessariamente não só por causa do estado embrionário do próprio proletariado",
    "pois o uso de sua força de trabalho é seu próprio trabalho. Por meio da transação anterior",
    "o capitalista como capitalista) não é valor de uso imediato para o próprio consumo pessoal",
    "para mim tanto faz que o alfaiate trabalhe 8 ou 10 horas. Trata-se apenas do  valor de uso",
    "padres etc. Também aí o modo de produção capitalista só se verifica em extensão reduzida e",
    "todas as relações sociais. A conservação inalterada do antigo modo de produção constituía",
    "mas também uma grande parte das próprias forças produtivas já desenvolvidas. Uma epidemia",
    "o trabalho assalariado cria propriedade para o proletário? De nenhum modo. Cria o capital",
    "o trabalho vivo é sempre um meio de aumentar o trabalho acumulado. Na sociedade comunista",
    "por uma violação despótica do direito de propriedade e das relações de produção burguesas",
    "uma organização da sociedade pré-fabricada por eles. A história futura do mundo se resume",
    "tudo isso se opõe aos próprios trabalhadores individuais como algo estranho e coisificado",
    "aos quais pertence o trabalho e os quais incorporam a si o trabalho; junto com o trabalho",
    "não consiste em mera produção de mercadorias. É um processo que absorve trabalho não pago",
    "e nos dois casos trata-se para mim de utilizar o dinheiro como simples meio de circulação",
    "podem existir e circular no intervalo entre produção e consumo como mercadorias vendáveis",
    "que oscila entre o proletariado e a burguesia; fração complementar da sociedade burguesa",
    "não eram importadas ao mesmo tempo as condições sociais da França. Nas condições alemães",
    "enquanto o capital representa perante o trabalhador a força produtiva social do trabalho",
    "todas essas propostas apenas anunciam o desaparecimento do antagonismo entre as classes",
    "a destinação social que as torna capital e lhes dá o comando sobre o trabalho. Por isso",
    "é trabalho por que se permuta capital. Este é um pressuposto por si mesmo evidente. Mas",
    "numa forma em que desaparece por completo o caráter determinado do trabalho de alfaiate",
    "em riqueza material. E assim Ter-se-ia dado ao trabalho produtivo uma segunda definição",
    "seção Unidade do processo de trabalho e do processo de produzir mais-valia.",
    "fruto do trabalho do indivíduo propriedade que se declara ser a base de toda liberdade",
    "a qual o modo menos desenvolvido dessa produção tem em comum com o mais desenvolvido -"
]

tab3 = [
    "constitui a verdadeira base social do regime estabelecido.",
    "por conseguinte trabalho que produz o próprio produto como capital.",
    "como no processo de acrescer o valor de todas as demais mercadorias.",
    "enriquecer é melhorar cada vez mais a existência dos trabalhadores.",
    "o serviço que me proporciona a utilidade específica desse trabalho.",
    "tal ação só pode provir de uma cega falta de fé no novo evangelho.",
    "que nada tem a ver com o conteúdo do trabalho e dele não depende.",
    "não fez senão ativar a venda de sua mercadoria entre tal público.",
    "a variação na produtividade do trabalho influi no valor de troca.",
    "o pequeno camponês possuir sua terra por via de instituto feudal.",
    "como tampouco o tem a relação entre vendedor e comprador de fio.",
    "aboliu a propriedade feudal em proveito da propriedade burguesa.",
    "esta classe continua a vegetar ao lado da burguesia em ascensão.",
    "na propaganda e na prática de seus planos de organização social.",
    "decresce na proporção em que emprego trabalhadores improdutivos.",
    "como simples meio de permutar menos trabalho por mais trabalho.",
    "suas condições de vida o predispõem mais a vender-se à reação.",
    "atrás dos quais se ocultam outros tantos interesses burgueses.",
    "as seguintes medidas poderão geralmente ser postas em prática.",
    "só poderá ser o prelúdio imediato de uma revolução proletária.",
    "mas que exerce e efetiva de maneira mais favorável à produção.",
    "são tão insignificantes que podem ficar de todo despercebidas.",
    "o direito mantiveram-se sempre através dessas transformações.",
    "em contrapor-se aos meios de trabalho convertidos em capital.",
    "representar-se em quantidade maior de trabalho materializado.",
    "o proletariado é recrutado em todas as classes da população.",
    "e isso contradiz todo o desenvolvimento histórico anterior.",
    "Burgueses e Proletários conforme acima descrito.",
    "reagem respectivamente contra os cartistas e os reformistas",
    "o partido que desencadeou a insurreição de Crac6via em 1846.",
    "pelos esforços combinados de todos os membros da sociedade.",
    "já não vos atreveis; a admitir para a propriedade burguesa.",
    "embora não tenha deixado traço visível em seu valor de uso.",
    "de uma série de revoluções no modo de produção e de troca.",
    "das relações burguesas de produção e da própria burguesia.",
    "tornara-se impossível a velha fraseologia da Restauração.",
    "revelou-se valor que ao mesmo tempo se conserva e acresce.",
    "com a supremacia econômica e política da classe burguesa.",
    "a lei da jornada de dez horas de trabalho na Inglaterra.",
    "esse socialismo é ao mesmo tempo reacionário e utópico.",
    "a única pronunciada seriamente pelo socialismo burguês.",
    "subjugam e o tornam supérfluo nas formas independentes.",
    "e só por esse meio o dinheiro se transforma em capital.",
    "consigo mesmo se relaciona na qualidade de assalariado.",
    "do produto do trabalhador sobre o próprio trabalhador.",
    "apenas um adestramento que os transforma em máquinas.",
    "como capitalista emprega a si mesmo como assalariado.",
    "da marcha e dos fins gerais do movimento proletário.",
    "embora de nenhum modo no sentido burguês da palavra.",
    "desaparecerá a hostilidade entre as próprias nações.",
    "essas propostas têm um sentimento puramente utópico.",
    "possa ser travada a luta contra a própria burguesia.",
    "despender dinheiro em serviços médicos ou jurídicos.",
    "é uma das primeiras condições para sua emancipação.",
    "quando a outra se transforma em capital constante.",
    "a prostituição oficial e não oficial desaparecerá.",
    "para expressar a relação entre capital e trabalho.",
    "os radicais da França e os policiais da Alemanha.",
    "novas formas de luta às que existiram no passado.",
    "têm singular prazer em comerem-se uns aos outros.",
    "a propriedade rural feudal e a pequena burguesia.",
    "em valor maior que o valor da força de trabalho.",
    "declarais quê a individualidade está suprimida.",
    "quereis Introduzir a comunidade das mulheres!.",
    "nenhum movimento político que lhe seja próprio.",
    "conquista do poder político pelo proletariado.",
    "o regime patriarcal: eis a sua última palavra.",
    "ou pela destruição das suas classes em luta.",
    "que se chama por isso de trabalho produtivo.",
    "os interesses do movimento em seu conjunto.",
    "expresso no dobro daquela soma de dinheiro.",
    "do sábio fez seus servidores assalariados.",
    "cujo preço varia segundo a idade e o sexo.",
    "pretenderiam modelar o movimento operário.",
    "uma inércia geral apoderar-se-ia do mundo.",
    "portanto o valor da mercadoria que compra.",
    "da qual se assume a propriedade sem troca.",
    "e delas se apropriar (personificando-as).",
    "cria um mundo à sua imagem e semelhança.",
    "mais precisamente de meio de circulação.",
    "uma força pessoal; é uma força social.",
    "do ódio que ele vota a essa sociedade.",
    "são precondições na forma de capital.",
    "que não tivemos tempo de escrevê-la.",
    "o desaparecimento de toda a cultura.",
    "em simples instrumentos de trabalho.",
    "mas como capitalista puro e simples.",
    "serão diferentes nos vários países.",
    "particularmente para a agricultura.",
    "açúcar de beterraba e aguardente.",
    "que permitam criar essas condições.",
    "embora ele trabalhe 12 como dantes.",
    "na exploração de uns pelos outros.",
    "sua própria dominação como classe.",
    "da vontade verdadeiramente humana.",
    "e que em oposição a ele se exerce.",
    "embora se condicionem uma a outra.",
    "a todas as flutuações do mercado.",
    "de toda independência individual.",
    "não merecem um exame aprofundado."
]


def make_bullshit():
    global tab0, tab1, tab2, tab3
    return random.choice(tab0) + random.choice(tab1) + random.choice(tab2) + random.choice(tab3)
