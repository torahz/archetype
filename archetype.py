import requests
from bs4 import BeautifulSoup
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crie o chatbot
archetype_bot = ChatBot('Archetype')

# Crie o treinador
trainer = ChatterBotCorpusTrainer(archetype_bot)

# Treine o chatbot com dados de exemplo em inglês
trainer.train('chatterbot.corpus.english')

# Treine o chatbot com dados específicos de arquitetura (adapte conforme necessário)
# Treinamento com informações sobre tipos de revestimento de parede e piso
trainer.train([
    'Quais são os tipos comuns de revestimento para pisos em ambientes residenciais?',
    'Pisos laminados, porcelanatos, cerâmicas, carpetes e pisos de madeira são opções comuns para ambientes residenciais, cada um com suas características de durabilidade, estética e manutenção.',

    'Como escolher o revestimento de parede adequado para uma cozinha?',
    'Azulejos, pastilhas e pintura lavável são escolhas populares para cozinhas devido à facilidade de limpeza. A escolha também pode depender do estilo desejado, sendo azulejos de metrô e pastilhas comuns em designs modernos.',

    'Quais são os benefícios do uso de porcelanato em pisos?',
    'O porcelanato é conhecido por sua durabilidade, resistência a manchas e baixa absorção de água. Ele é uma opção popular para áreas de alto tráfego, como salas de estar e cozinhas.',

    'Como escolher um revestimento de piso para ambientes externos?',
    'Para áreas externas, como varandas e jardins, opções como porcelanato antiderrapante, pedras naturais, madeira tratada e deck de composite são adequadas, proporcionando resistência às condições climáticas.',

    'Quais são as tendências atuais em revestimentos de parede para salas de estar?',
    'Tendências incluem o uso de revestimentos 3D, papéis de parede decorativos, painéis de madeira e o retorno de materiais naturais, como pedras e tijolos aparentes.',

    'Como escolher o revestimento de parede adequado para um banheiro?',
    'Azulejos, pastilhas de vidro e porcelanatos são escolhas comuns para banheiros devido à resistência à umidade. O uso de revestimentos de parede impermeáveis é crucial para prevenir problemas de infiltração.',

    'Quais são as opções de revestimento sustentável para pisos?',
    'Pisos de bambu, cortiça, linóleo e revestimentos cerâmicos reciclados são exemplos de opções sustentáveis para pisos, proporcionando durabilidade e considerações ambientais.',

    'O que considerar ao escolher revestimento de parede para um escritório?',
    'Em escritórios, a escolha do revestimento de parede pode depender da imagem da empresa, do estilo de design e da funcionalidade. Pinturas neutras, painéis acústicos e revestimentos vinílicos são opções comuns.',

    'Quais são os tipos de revestimento vinílico para pisos?',
    'Pisos vinílicos podem ser em forma de mantas, placas ou réguas, oferecendo versatilidade em estilos e padrões. São conhecidos por serem duráveis, resistentes à umidade e fáceis de limpar.',

    'O que é cerâmica de alta temperatura e como ela difere de outras cerâmicas?',
    'Cerâmica de alta temperatura é uma opção resistente e durável, produzida em temperaturas mais elevadas durante a queima. Isso resulta em um material mais denso e menos poroso, adequado para aplicações exigentes.',

    # Adicione mais perguntas e respostas específicas sobre revestimento de parede e piso
])

# Treinamento com informações sobre concreto
trainer.train([
    'O que é concreto?',
    'O concreto é um material composto feito de cimento, água, agregados (como areia e pedra) e, às vezes, aditivos para melhorar suas propriedades.',

    'Quais são os tipos comuns de concreto?',
    'Os tipos comuns de concreto incluem concreto convencional, concreto de alta resistência, concreto leve, concreto pré-moldado e concreto pré-esforçado.',

    'Explique o processo de cura do concreto.',
    'A cura do concreto é o processo de manter a umidade e temperatura adequadas após o despejo para garantir uma resistência e durabilidade ideais.',

    'Quais são as propriedades importantes do concreto?',
    'As propriedades importantes do concreto incluem resistência à compressão, durabilidade, permeabilidade, resistência ao desgaste e capacidade de suportar cargas.',

    'Como o concreto é utilizado na construção?',
    'O concreto é amplamente utilizado na construção para fundações, lajes, pilares, vigas, pavimentos, paredes e outras estruturas.',

    'Quais são os fatores que afetam a resistência do concreto?',
    'Fatores como a proporção de água-cimento, qualidade dos materiais, método de cura e tempo de cura afetam a resistência do concreto.',

    'Explique a diferença entre concreto armado e concreto pré-esforçado.',
    'No concreto armado, o aço é adicionado para resistir à tração, enquanto no concreto pré-esforçado, o aço é pré-tensionado ou pós-tensionado para melhorar a resistência.',

    'O que é concreto protendido?',
    'Concreto protendido é um tipo de concreto pré-esforçado no qual o aço é tensionado antes da concretagem para melhorar a resistência e reduzir a deformação.',

    'Como evitar fissuras no concreto?',
    'Para evitar fissuras no concreto, é importante controlar a proporção água-cimento, utilizar aditivos apropriados e aplicar métodos adequados de cura.',

    'Quais são os benefícios do concreto sustentável?',
    'O concreto sustentável utiliza materiais reciclados, consome menos energia na produção e pode contribuir para a certificação de edifícios verdes.',

    # Adicione mais perguntas e respostas específicas sobre concreto
])

# Treinamento com informações sobre iluminação técnica
trainer.train([
    'O que é iluminotécnica?',
    'Iluminotécnica é a disciplina que trata do projeto e aplicação da iluminação em espaços internos e externos, levando em consideração aspectos estéticos e funcionais.',

    'Quais são os principais objetivos da iluminotécnica?',
    'Os objetivos da iluminotécnica incluem proporcionar iluminação adequada para a realização de tarefas, criar atmosferas específicas e destacar elementos arquitetônicos.',

    'Explique a diferença entre iluminação direta e indireta.',
    'A iluminação direta é aquela que ilumina diretamente uma área específica, enquanto a iluminação indireta é direcionada para superfícies que refletem a luz para criar um ambiente mais suave.',

    'O que é temperatura de cor na iluminação?',
    'A temperatura de cor refere-se à aparência visual da luz emitida por uma fonte de iluminação e é medida em kelvins (K). Temperaturas mais baixas parecem mais quentes, enquanto temperaturas mais altas parecem mais frias.',

    'Como escolher a temperatura de cor adequada para um ambiente?',
    'A escolha da temperatura de cor depende do uso do espaço. Temperaturas de cor mais quentes são adequadas para ambientes acolhedores, enquanto temperaturas mais frias são ideais para ambientes de trabalho.',

    'Quais são os benefícios da iluminação LED?',
    'A iluminação LED oferece benefícios como eficiência energética, longa vida útil, controle de intensidade, e a capacidade de criar uma variedade de cores e temperaturas.',

    'Explique o índice de reprodução de cor (IRC) na iluminação.',
    'O IRC é uma medida da capacidade de uma fonte de luz reproduzir cores com precisão em comparação com uma fonte de luz natural. Quanto maior o IRC, melhor a reprodução de cores.',

    'O que é um projeto luminotécnico?',
    'Um projeto luminotécnico é a criação de um plano para a distribuição de luz em um ambiente, considerando as necessidades específicas do espaço e as características das fontes de luz.',

    'Como a iluminação pode afetar o conforto visual?',
    'A iluminação adequada pode reduzir o desconforto visual, prevenir ofuscamento, proporcionar contraste adequado e garantir uma distribuição uniforme de luz.',

    'Quais são as tendências atuais em iluminação arquitetônica?',
    'Tendências atuais incluem o uso de tecnologias inteligentes, designs personalizados, integração de sistemas de automação e a busca por soluções mais sustentáveis.',

    # Adicione mais perguntas e respostas específicas sobre iluminotécnica
])

# Treinamento com informações sobre iluminação de ambientes
trainer.train([
    'Como escolher a iluminação ideal para uma sala de estar?',
    'Para uma sala de estar, opte por uma combinação de iluminação geral, como lustres ou luminárias de teto, e iluminação de tarefa, como luminárias de mesa ou arandelas, para criar uma atmosfera aconchegante e funcional.',

    'Quais são as melhores opções de iluminação para um quarto?',
    'Em um quarto, considere a inclusão de iluminação ambiente suave, como abajures ou arandelas, para criar uma atmosfera relaxante. Além disso, adicione opções de iluminação de leitura junto à cama.',

    'Como iluminar uma cozinha de forma eficiente?',
    'Na cozinha, priorize a iluminação de tarefa sobre as áreas de trabalho, como balcões e fogão, usando luzes embutidas ou pendentes. Certifique-se também de ter uma boa iluminação geral para evitar sombras indesejadas.',

    'Quais são as melhores luminárias para um banheiro?',
    'Para o banheiro, escolha luminárias que proporcionem uma luz branca e brilhante para facilitar atividades como maquiagem e barbear. Considere também iluminação ao redor do espelho.',

    'Como criar iluminação para destaque em um ambiente?',
    'Para destacar elementos específicos, como obras de arte ou plantas, utilize spots direcionados ou luzes embutidas. Isso cria focos de luz que atraem a atenção para áreas específicas.',

    'O que considerar ao iluminar um escritório em casa?',
    'Em um escritório em casa, busque uma iluminação de tarefa eficaz para a área de trabalho, evitando reflexos na tela do computador. Combine isso com uma boa iluminação ambiente para manter o ambiente agradável.',

    'Como criar uma iluminação aconchegante em espaços comerciais?',
    'Em espaços comerciais, como restaurantes ou cafés, use iluminação ambiente suave para criar uma atmosfera acolhedora. Adicione elementos decorativos, como luminárias pendentes, para um toque visual.',

    'O que é iluminação de acentuação?',
    'A iluminação de acentuação destaca elementos específicos em um espaço, como uma peça de arte ou uma arquitetura única. Utilize spots, trilhos ou luminárias direcionadas para esse fim.',

    'Como criar uma iluminação eficaz em espaços externos?',
    'Em espaços externos, use iluminação de destaque para realçar características paisagísticas. Considere também a iluminação de caminhos e áreas de estar para segurança e funcionalidade.',

    'Quais são as tendências atuais em design de iluminação de ambientes?',
    'Tendências incluem o uso de tecnologia LED, luminárias com designs contemporâneos e a integração de sistemas de automação para controle personalizado.',

    # Adicione mais perguntas e respostas específicas sobre iluminação de ambientes
])

# Treinamento com informações sobre medidas de circulação
trainer.train([
    'Quais são as medidas padrão para corredores em uma residência?',
    'Em residências, corredores geralmente têm entre 80 cm e 1,20 m de largura para permitir uma circulação confortável. A largura ideal pode variar dependendo do espaço disponível e do estilo de design.',

    'Como dimensionar escadas de forma adequada em uma casa?',
    'As escadas em uma casa devem ter degraus com altura entre 17 cm e 18 cm e profundidade entre 28 cm e 32 cm. O cálculo da inclinação (passo + 2 vezes a altura do espelho) é crucial para garantir uma subida confortável.',

    'Quais são as medidas recomendadas para portas em ambientes residenciais?',
    'Portas em ambientes residenciais geralmente têm uma altura padrão de 2,10 m e larguras variando de 60 cm a 80 cm. Portas principais e de acessibilidade podem ser mais largas, entre 80 cm e 1,20 m.',

    'Como dimensionar corretamente os corredores em um espaço comercial?',
    'Em espaços comerciais, corredores devem ser mais amplos do que em residências, geralmente com larguras entre 1,20 m e 2,40 m, dependendo do fluxo de pessoas e das regulamentações locais.',

    'Quais são as diretrizes para a circulação em áreas de trabalho em um escritório?',
    'Para áreas de trabalho em escritórios, as passagens devem ter larguras suficientes para permitir o tráfego de pessoas sem congestionamento, com medidas que variam entre 1,20 m e 1,50 m ou mais, dependendo do layout.',

    'Qual a altura padrão para bancadas em cozinhas residenciais?',
    'A altura padrão para bancadas de cozinha é geralmente em torno de 90 cm, mas isso pode variar com base na estatura dos usuários e nas preferências ergonômicas.',

    'Quais são as medidas ideais para corredores em um shopping center?',
    'Em shopping centers, os corredores são geralmente amplos para acomodar grandes fluxos de pessoas. As medidas podem variar de 3 m a 6 m, dependendo do tamanho do espaço e da quantidade de visitantes esperados.',

    'Como dimensionar corretamente as entradas em um estabelecimento comercial?',
    'Entradas de estabelecimentos comerciais devem ser largas o suficiente para acomodar o fluxo de clientes. As dimensões recomendadas variam, mas 2,40 m a 3 m podem ser consideradas padrão.',

    'Quais são as medidas típicas para corredores em um hotel?',
    'Corredores de hotéis devem permitir uma circulação suave para hóspedes e pessoal de serviço. Larguras entre 1,50 m e 2,40 m são comuns, dependendo do padrão do hotel.',

    'Como dimensionar as portas de acessibilidade em ambientes comerciais?',
    'Portas de acessibilidade em ambientes comerciais devem ter larguras mínimas de 80 cm a 90 cm para garantir a entrada confortável de cadeiras de rodas e carrinhos de bebê.',

    # Adicione mais perguntas e respostas específicas sobre medidas de circulação
])

# Treinamento com informações sobre medidas padrão para janelas e portas
trainer.train([
    'Quais são as medidas padrão para uma porta de entrada residencial?',
    'Portas de entrada residenciais geralmente têm uma altura padrão de 2,10 metros. A largura pode variar, mas 80 centímetros a 1 metro são comuns. Portas principais podem ser mais largas, até 1,20 metros.',

    'Como dimensionar corretamente uma janela para um quarto?',
    'As medidas de uma janela para um quarto dependem do estilo e do tamanho da abertura. Janelas com alturas entre 1,20 metros e 1,50 metros e larguras entre 60 centímetros e 1 metro são comuns.',

    'Quais são as medidas típicas para janelas de banheiro?',
    'Janelas de banheiro geralmente são menores para garantir privacidade. Alturas entre 60 centímetros e 1 metro e larguras entre 30 centímetros e 60 centímetros são comuns.',

    'Como escolher a altura ideal para portas internas em uma casa?',
    'Portas internas em uma casa geralmente têm uma altura padrão de 2,10 metros. A largura varia de 60 centímetros a 80 centímetros, dependendo do local de instalação.',

    'Quais são as medidas recomendadas para janelas de cozinha?',
    'Janelas de cozinha devem permitir boa ventilação e luz. Alturas entre 1,20 metros e 1,50 metros e larguras entre 80 centímetros e 1,20 metros são comuns, dependendo do espaço disponível.',

    'Como dimensionar corretamente uma porta de correr para um ambiente interno?',
    'Portas de correr internas podem ter alturas padrão de 2,10 metros e larguras entre 70 centímetros e 1 metro. Certifique-se de considerar o espaço necessário para o movimento da porta.',

    'Quais são as medidas típicas para janelas de salas de estar?',
    'Janelas de salas de estar podem variar em tamanho, mas alturas entre 1,50 metros e 2 metros e larguras entre 1 metro e 2 metros são comuns, proporcionando uma boa entrada de luz e uma vista agradável.',

    'Como escolher a altura ideal para portas de armários embutidos?',
    'Portas de armários embutidos geralmente têm uma altura padrão de 2,10 metros e larguras variáveis, dependendo do tamanho do armário. Considere o acesso conveniente ao interior do armário.',

    'Quais são as medidas comuns para portas externas de um estabelecimento comercial?',
    'Portas externas de estabelecimentos comerciais podem ter alturas padrão de 2,10 metros e larguras entre 80 centímetros e 1,20 metros, dependendo da entrada e do tráfego de pessoas.',

    'Como dimensionar corretamente uma janela panorâmica para um ambiente moderno?',
    'Janelas panorâmicas são projetadas para proporcionar uma visão ampla. Alturas entre 2 metros e 3 metros e larguras entre 3 metros e 6 metros são comuns, dependendo da arquitetura e do design.',

    # Adicione mais perguntas e respostas específicas sobre medidas de janelas e portas
])

# Treinamento com informações sobre tipos de revestimento de parede e piso
trainer.train([
    'Quais são os tipos comuns de revestimento para pisos em ambientes residenciais?',
    'Pisos laminados, porcelanatos, cerâmicas, carpetes e pisos de madeira são opções comuns para ambientes residenciais, cada um com suas características de durabilidade, estética e manutenção.',

    'Como escolher o revestimento de parede adequado para uma cozinha?',
    'Azulejos, pastilhas e pintura lavável são escolhas populares para cozinhas devido à facilidade de limpeza. A escolha também pode depender do estilo desejado, sendo azulejos de metrô e pastilhas comuns em designs modernos.',

    'Quais são os benefícios do uso de porcelanato em pisos?',
    'O porcelanato é conhecido por sua durabilidade, resistência a manchas e baixa absorção de água. Ele é uma opção popular para áreas de alto tráfego, como salas de estar e cozinhas.',

    'Como escolher um revestimento de piso para ambientes externos?',
    'Para áreas externas, como varandas e jardins, opções como porcelanato antiderrapante, pedras naturais, madeira tratada e deck de composite são adequadas, proporcionando resistência às condições climáticas.',

    'Quais são as tendências atuais em revestimentos de parede para salas de estar?',
    'Tendências incluem o uso de revestimentos 3D, papéis de parede decorativos, painéis de madeira e o retorno de materiais naturais, como pedras e tijolos aparentes.',

    'Como escolher o revestimento de parede adequado para um banheiro?',
    'Azulejos, pastilhas de vidro e porcelanatos são escolhas comuns para banheiros devido à resistência à umidade. O uso de revestimentos de parede impermeáveis é crucial para prevenir problemas de infiltração.',

    'Quais são as opções de revestimento sustentável para pisos?',
    'Pisos de bambu, cortiça, linóleo e revestimentos cerâmicos reciclados são exemplos de opções sustentáveis para pisos, proporcionando durabilidade e considerações ambientais.',

    'O que considerar ao escolher revestimento de parede para um escritório?',
    'Em escritórios, a escolha do revestimento de parede pode depender da imagem da empresa, do estilo de design e da funcionalidade. Pinturas neutras, painéis acústicos e revestimentos vinílicos são opções comuns.',

    'Quais são os tipos de revestimento vinílico para pisos?',
    'Pisos vinílicos podem ser em forma de mantas, placas ou réguas, oferecendo versatilidade em estilos e padrões. São conhecidos por serem duráveis, resistentes à umidade e fáceis de limpar.',

    'O que é cerâmica de alta temperatura e como ela difere de outras cerâmicas?',
    'Cerâmica de alta temperatura é uma opção resistente e durável, produzida em temperaturas mais elevadas durante a queima. Isso resulta em um material mais denso e menos poroso, adequado para aplicações exigentes.',

    # Adicione mais perguntas e respostas específicas sobre revestimento de parede e piso
])

# Treinamento com informações sobre diferenças entre tipos de revestimento
trainer.train([
    'Qual é a diferença entre granito e porcelanato?',
    'Granito é uma pedra natural, enquanto porcelanato é um material cerâmico feito de argila, feldspato e outros minerais. O porcelanato é mais resistente a manchas e riscos, além de ter uma gama mais ampla de designs.',

    'Quais são as principais distinções entre cerâmica e porcelanato?',
    'A principal diferença entre cerâmica e porcelanato está na composição. O porcelanato é mais denso e menos poroso, tornando-o mais resistente à umidade e a manchas. A cerâmica é mais leve e pode ser menos durável em certos contextos.',

    'O que diferencia piso laminado de piso vinílico?',
    'Piso laminado é feito de camadas de material composto, enquanto piso vinílico é feito de PVC. O piso laminado tem uma camada de imagem decorativa, enquanto o vinílico tem maior resistência à umidade e é mais silencioso.',

    'Quais são as características distintivas entre piso laminado e piso de madeira maciça?',
    'O piso laminado é uma camada fina de material composto sobre uma base de fibra, enquanto o piso de madeira maciça é feito de madeira sólida. O piso laminado é mais acessível, enquanto o de madeira maciça oferece a autenticidade da madeira natural.',

    'Quais são as vantagens do piso vinílico sobre o carpete?',
    'O piso vinílico é mais durável, resistente a manchas, fácil de limpar e é uma opção mais hipoalergênica em comparação com carpetes. Além disso, o vinílico oferece mais opções de design e é resistente à umidade.',

    'Como o mármore se diferencia do granito?',
    'Mármore é uma pedra metamórfica, enquanto granito é uma pedra ígnea. O mármore é conhecido por sua textura suave e cores mais claras, enquanto o granito tem uma textura mais granulada e cores variadas.',

    'Quais são as diferenças entre piso vinílico e piso de linóleo?',
    'Ambos são revestimentos de piso resilientes, mas o piso vinílico é feito de PVC, enquanto o linóleo é produzido a partir de materiais naturais como óleo de linhaça, resinas e farinha de madeira. O linóleo é mais ecológico, mas o vinílico oferece maior resistência à umidade.',

    'Quais são as distinções entre piso de cerâmica e piso de porcelanato?',
    'Porcelanato é uma cerâmica mais refinada, sendo mais denso e menos poroso que a cerâmica comum. O porcelanato é geralmente mais caro, mas oferece maior durabilidade e resistência a manchas e umidade.',

    'O que diferencia o piso de cimento queimado de outros revestimentos?',
    'O cimento queimado é um revestimento de concreto polido, conhecido por sua aparência contemporânea e minimalista. Ele difere de outros revestimentos devido à sua composição de cimento, areia e pigmentos, proporcionando uma superfície única e resistente.',

    'Como escolher entre granito e mármore para bancadas de cozinha?',
    'Granito é mais durável e resistente a manchas, tornando-se uma escolha prática para bancadas de cozinha. Mármore, embora mais poroso e suscetível a manchas, oferece uma estética luxuosa e atemporal.',

    # Adicione mais perguntas e respostas específicas sobre diferenças entre tipos de revestimento
])

# Treinamento com informações sobre tipos de construção
trainer.train([
    'O que é alvenaria?',
    'Alvenaria é um método de construção que utiliza blocos de materiais como tijolos ou blocos de concreto, unidos por argamassa. É uma técnica tradicional e durável comum em muitos tipos de construções.',

    'Quais são as vantagens do steelframe na construção?',
    'O steelframe, ou estrutura de aço, é leve, resistente e permite construções mais rápidas. Ele é amplamente utilizado em construções comerciais e industriais, oferecendo flexibilidade de design e eficiência energética.',

    'Como funciona o woodframe na construção de edifícios?',
    'Woodframe, ou estrutura de madeira, envolve o uso de elementos de madeira como vigas e colunas para criar a estrutura do edifício. É comum em construções residenciais e pode ser uma opção sustentável dependendo das práticas florestais.',

    'Quais são os benefícios da construção com contêineres?',
    'A construção com contêineres envolve o uso de contêineres de transporte reciclados para criar estruturas habitáveis. Essa abordagem é sustentável, rápida e pode ser mais acessível em comparação com métodos tradicionais.',

    'Como funciona a construção com bloco de concreto?',
    'Blocos de concreto são usados para criar paredes estruturais em construções. Eles oferecem resistência, durabilidade e isolamento térmico. A construção com blocos de concreto é comum em edifícios residenciais e comerciais.',

    'Quais são as características do tijolo na construção?',
    'O tijolo é um material de construção tradicional feito de argila. Ele é conhecido por sua durabilidade, isolamento térmico e capacidade de ser utilizado em diversos estilos arquitetônicos. A construção com tijolos é comum em muitas regiões do mundo.',

    'O que define a construção modular?',
    'A construção modular envolve a fabricação de componentes de construção em uma fábrica e sua montagem no local. Isso permite construções mais rápidas e eficientes. Módulos podem ser utilizados em diversas configurações.',

    'Quais são as vantagens da construção em steel deck?',
    'Steel deck refere-se à construção com placas de aço perfuradas que servem como formas para concreto. Essa técnica é usada em pisos e telhados de edifícios, proporcionando durabilidade e resistência.',

    'Como funciona a construção em adobe?',
    'A construção em adobe envolve a moldagem e secagem ao sol de tijolos de barro. Essa técnica é tradicional em algumas regiões e é conhecida pela sua eficiência térmica e sustentabilidade.',

    'Quais são as características da construção em estrutura metálica?',
    'A construção em estrutura metálica utiliza aço como elemento principal da estrutura. É comum em edifícios industriais e comerciais devido à sua resistência e capacidade de vãos livres maiores.',

    # Adicione mais perguntas e respostas específicas sobre tipos de construção
])

# Treinamento com informações sobre tipos de telhado e custo-benefício
trainer.train([
    'Quais são os tipos comuns de telhados para residências?',
    'Telhados inclinados com telhas cerâmicas, telhas de concreto, telhas de metal, telhas asfálticas, e telhas de fibrocimento são comuns em residências. Cada tipo tem suas próprias características estéticas e de desempenho.',

    'Quais são as vantagens do telhado de telha cerâmica?',
    'O telhado de telha cerâmica é conhecido pela sua durabilidade, resistência ao fogo e estética tradicional. Embora possa ter um custo inicial mais alto, oferece um bom custo-benefício a longo prazo.',

    'Como o telhado de metal se compara a outros tipos em termos de custo e benefício?',
    'Telhados de metal são duráveis, leves e de baixa manutenção. Embora o custo inicial possa ser mais alto, o baixo custo de manutenção e a longa vida útil geralmente resultam em um bom custo-benefício ao longo do tempo.',

    'Quais são as características do telhado de telha de concreto?',
    'O telhado de telha de concreto é resistente, durável e pode ter uma variedade de estilos. Embora o custo inicial seja moderado, sua longa vida útil e baixa manutenção podem proporcionar um bom custo-benefício.',

    'O telhado de fibrocimento é uma opção econômica?',
    'Telhados de fibrocimento são econômicos, leves e resistentes a intempéries. Eles oferecem um bom custo-benefício, sendo uma opção popular para residências e construções comerciais.',

    'Quais são as considerações de custo-benefício do telhado asfáltico?',
    'Telhados asfálticos são acessíveis, fáceis de instalar e vêm em uma variedade de estilos. Embora possam ter uma vida útil menor em comparação com alguns materiais, o custo inicial mais baixo pode compensar esse aspecto.',

    'Como o telhado verde se encaixa em termos de custo e benefício?',
    'Telhados verdes podem ter custos iniciais mais altos, mas oferecem benefícios ambientais, isolamento térmico e uma vida útil estendida. Dependendo das prioridades do proprietário, pode ser considerado um investimento de longo prazo com benefícios ambientais.',

    'Quais são as opções de telhados de baixo custo?',
    'Telhas de fibrocimento, telhas asfálticas e algumas opções de telhados metálicos são geralmente consideradas de baixo custo. No entanto, é crucial considerar fatores como durabilidade e eficiência energética ao avaliar o custo-benefício.',

    'O que diferencia o telhado de policarbonato?',
    'Telhados de policarbonato são transparentes e oferecem iluminação natural. Embora o custo inicial possa ser moderado, a eficiência energética e a estética única podem ser consideradas benefícios que agregam valor.',

    'Quais são as vantagens do telhado de duas águas em termos de custo-benefício?',
    'Telhados de duas águas, ou em forma de A, são eficazes na drenagem da água e oferecem uma área útil adicional no sótão. Eles são eficientes e podem ter um bom custo-benefício dependendo das necessidades do projeto.',

    # Adicione mais perguntas e respostas específicas sobre tipos de telhado e custo-benefício
])

# Função para realizar a busca no DuckDuckGo
def search_duckduckgo(query):
    url = f'https://duckduckgo.com/html?q={query}'

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraindo e imprimindo os resultados (modifique conforme necessário)
        results = soup.find_all('a', {'class': 'result__a'})
        for result in results:
            title = result.text
            link = result['href']
            print(f'Título: {title}')
            print(f'Link: {link}\n')

    except Exception as e:
        print(f'Erro: {str(e)}')

# Interação com o usuário
while True:
    user_input = input("Você: ")

    # Se o usuário quiser sair, encerre o loop
    if user_input.lower() == 'sair':
        break

    # Obtém a resposta do chatbot
    response = archetype_bot.get_response(user_input)
    print("Archetype:", response)

    # Se a resposta do chatbot não for suficiente, realiza uma busca na web
    if 'Desculpe, eu não sei a resposta.' in str(response):
        print("Realizando busca na web...")
        search_duckduckgo(user_input)
