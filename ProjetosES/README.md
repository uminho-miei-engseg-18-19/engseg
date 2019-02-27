# Projetos para a cadeira de Engenharia de Segurança

Tal como referido na primeira aula, o "Projeto de desenvolvimento de software" / "Investigação sobre um
tópico" é uma componente de avaliação da cadeira de Engenharia de Segurança (componente B2) que vale
45% da nota final e para a qual os alunos têm de ter uma nota mínima de 8 valores.

Estes projetos são feitos por um grupo de trabalho com o máximo de 3 elementos.

Os projetos têm que se inserir na temática da cadeira e/ou do Perfil de Especialização CSI (Criptografia e Segurança da Informação), podendo ser propostos
+ pelo grupo e aceites pelo docente, ou
+ pelo docente e escolhidos pelo grupo.

As **reuniões de projeto** ocorrerão sempre que os alunos as pedirem (por favor enviem um mail prévio a marcar um slot de reunião), às segundas-feiras a seguir à UC de Engenharia de Segurança.

Existe também um *workspace* da UC no slack para ser utilizado no âmbito da UC de  Engenharia de Segurança.
Para se juntar, utilize o convite em
https://join.slack.com/t/engenhariadeseguranca/shared_invite/enQtNTU1Mzk4MTc2NjE1LTc2NTExY2U5Y2RiNmZkY2I4MGFlOTZkZGMyMTEzZTc0Y2UzM2VhMTczZjU4ZWI5YzY4N2JiNWVhZjVmMTk1MDM



## 1. Projetos propostos pelo docente

Os projetos propostos pelo docente para escolha pelo grupo de trabalho são os seguintes:
+ [Técnicas de intrusão](Intrusao.pdf) - até dois grupos - Grupo 8 e Grupo 7;
+ [mDL (mobile Driving License)](mDL.pdf) - até dois grupos - Grupo 5 e Grupo 4;
+ [Self-sovereign identity](SelfSoverID.pdf) - até dois grupos - Grupo 9 e Grupo SSI (Joana Cunha, João Fernandes, Pedro Silva, Ili Karim);
+ [Assinaturas eIDAS com web service REST/SOAP](Sign.eIDAS.1.pdf) - até cinco grupos - Grupo 12;
+ [Assinaturas eIDAS com Java](Sign.eIDAS.2.pdf) - até dois grupos - Grupo 13, Grupo 14;
+ [Assinaturas eIDAS em Javascript](Sign.eIDAS.3.pdf) - um grupo - Grupo 2;
+ [Esteganografia](Esteganografia.pdf) - até dois grupos - Grupo 1 (caso de uso 2) e Grupo 3 (caso de uso 1);
+ [Segurança IoT](IoT.pdf) - um grupo - Grupo 11.

Relembra-se que os grupos que escolherem algum dos [projetos propostos para a cadeira de "Laboratório de Engenharia Informática"](../LabEI) deverão falar com o docente para estabelecer que parte do projeto é que pode também ser utilizado para a componente B2 da cadeira de Engenharia de Segurança. Relembramos que o projeto poderá ser o mesmo, mas como os objetivos são diferentes, existirão relatórios e apresentações distintas para cada uma das cadeiras.

### 1.1 Escolha do projeto

Os grupos devem enviar um mail ao docente até ao dia 18/Fevereiro com indicação de qual o projeto que escolhem.

O modo de atribuição dos projetos será "_First in First served_". Nessa perspetiva, o grupo pode indicar vários projetos e ordem de prioridade de preferência.

De notar que o projeto [Técnicas de intrusão](Intrusao.pdf) foi pedido por um grupo na aula do dia 11/Fevereiro, pelo que se encontra reservado para esse grupo.

## 1.2 Considerações adicionais sobre os projetos propostos

### 1.2.1 Projetos eIDAS

Para a utilização do DSS (**objetivo 1**) podem começar por https://ec.europa.eu/cefdigital/wiki/pages/viewpage.action?pageId=46992515.

Para o **objetivo 2** do eIDAS.1 (REST/SOAP) e eIDAS.2 (Java) aconselho que escolham o comando linha ou a aplicação desktop - por favor indiquem-me qual das duas alternativas escolhem -.

Ainda para o eIDAS.1 (REST/SOAP) e eIDAS.2 (Java), no objetivo 2 centrem-se na parte de disponibilizar funcionalidade de extensão de assinatura e validação de assinatura de documento. A assinatura inicial do documento, para não terem que andar a fazer o interface com o Cartão de Cidadão ou com a CMD (Chave Móvel Digital), pode ser feita no DSS.

De notar que a **funcionalidade de extensão de assinatura** tem a ver com a preservação long-term de assinaturas digitais (que é um serviço qualificado de confiança, de acordo com o regulamento eIDAS). Para perceberem melhor o trabalho que está a ser feito em termos de standardização deste tipo de serviços, devem ler o  draft ETSI TS 119 511 V0.0.5 (2018-12) - Electronic Signatures and Infrastructures (ESI); Policy and security requirements for trust service providers providing long-term preservation of digital signatures or
general data using digital signature techniques - disponível em https://docbox.etsi.org/ESI/Open/Latest_Drafts/TS_119_511_v0.0.5_preservation-policy.pdf

No que diz respeito à **validação de assinaturas**, as mesmas tb são serviços qualificados de confiança de acordo com o regulamento eIDAS. Embora já exista um documento ETSI de políticas e práticas para o qual pode ser interessante olharem - ETSI TS 119 441 V1.1.1 (2018-08) Electronic Signatures and Infrastructures (ESI); Policy requirements for TSP providing signature validation services (https://www.etsi.org/deliver/etsi_ts/119400_119499/119441/01.01.01_60/ts_119441v010101p.pdf) -, o documento que define as regras para os trust service providers ainda está numa fase que parece demasiado incipiente - Draft ETSI TS 119 442 V0.0.5 (2017-11) Electronic Signatures and Infrastructures (ESI); Protocol profiles for trust service providers providing AdES digital signature validation services (https://upcommons.upc.edu/bitstream/handle/2117/112541/ESI-0019442v005(1).pdf).


### 1.2.2 Projeto Esteganografia

Um primer sobre estagonagrafia, em português, pode ser encontrado em https://www.gta.ufrj.br/grad/09_1/versao-final/stegano/index.html, enquanto que pode encontrar um _complete guide_ em inglês em https://www.edureka.co/blog/steganography-tutorial.

Em https://www-users.cs.umn.edu/~hoppernj/tc-stego.pdf encontra um paper (_Provably Secure Steganography_) sobre _computational indistinguishability_.

Outras leituras interessantes em:
+ https://www.secplicity.org/2017/06/22/steganography-primer-daily-security-byte/ podem encontrar um video introdutório, assim como alguma informação sobre a técnica de _least significant bit_, assim como apontadores para algumas ferramentas;
+ https://arxiv.org/abs/1806.03618 - Steganography Security: Principle and Practice
+ https://arxiv.org/abs/1901.03892 - SteganoGAN: High Capacity Image Steganography with GANs
+ Digital Watermarking and Steganography: Fundamentals and Techniques - https://www.researchgate.net/publication/281863589_Digital_Watermarking_and_Steganography_Fundamentals_and_Techniques
+ Steganographic Watermarking for Documents - https://www.cnc.una.py/publicaciones/1_73.pdf
+ A Robust Watermarking Scheme for Online Multimedia Copyright Protection Using New Chaotic Map - https://www.hindawi.com/journals/scn/2018/1840207/
+ https://null-byte.wonderhowto.com/how-to/introduction-steganography-its-uses-0155310/
+ https://null-byte.wonderhowto.com/how-to/steganography-hide-secret-data-inside-image-audio-file-seconds-0180936/

### 1.2.3 Projeto Intrusão

Para a fase de _Pre-engagement_, o exemplo de texto pode ser o seguinte:

> Para a execução do teste de intrusão foi estabelecido o seguinte contrato com a empresa:
+ o teste de intrusão não terá execução de ataques nem exploração de ataques, antes de se ter a
concordância explícita da empresa, a ser definida em próxima interacção com a mesma;
+ a identificação de vulnerabilidades não pode causar disrupção/indisponibilidade nos serviços da empresa;
+ todos os testes deverão ser feitos a partir da Internet, não estando no âmbito a realização de testes a partir da rede interna ou da rede Wifi da empresa;
+ não está no âmbito dos testes a execução de testes de engenharia social, nem testes de phishing (ou similares);
+ não existe limitação horária para realizar os testes;
+ não está no âmbito dos testes a verificação de controlos físicos e humanos das instalações impresa, i.e., testes de intrusão física;
+ não foram indicados IPs ou domínios detidos pela empresa, sendo essa também uma das informações a obter durante a fase de recolha de informação;
+	não foram indicados quais os mecanismos de segurança utilizados pela empresa nem como era protegido o perímetro (firewall, intrusion detection/prevention system, web application firewall, ou load balancer);
+ não foi indicada qual a estrutura para resposta a incidentes;
+ a comunicação (e o contacto de emergência para relato de incidentes/vulnerabilidades graves, caso existam) deve ser efetuada com o gestor de infraestrutura, seguido do Diretor Geral, tendo sido fornecido os contactos de email e telemóvel;
+ caso alguma vulnerabilidade seja encontrada, deverá ser comunicada ao gestor de infraestrutura, de imediato;
+ caso alguma vulnerabilidade seja encontrada que permita aceder a documentos, informação ou dados privados/confidenciais, os mesmos não podem ser acedidos. A equipa de testes deve documentar essa vulnerabilidade através de evidências que não divulguem essa informação, como por exemplo a listagem de uma diretoria ou a estrutura das tabelas da base de dados;
+ toda a informação obtida, que não seja pública, deve ser considerada como restrita e utilizada apenas no âmbito deste trabalho;
+	toda a informação sobre eventuais vulnerabilidades encontradas deve ser considerada confidencial até à vulnerabilidade ser resolvida;
+	o relatório deve ter a menção “Confidencial” expressa em todas as páginas do mesmo;
+	o relatório não deve ser transmitido em claro, através de canais eletrónicos;
+	no final da elaboração do relatório, o mesmo deve ser fornecido à empresa;
+	a equipa de testes não deve efetuar qualquer ação que possa violar a lei em vigor;
+	o teste de intrusão não terá qualquer custo para a empresa.
>
> De modo a existir evidência deste contrato, a equipa enviou uma mensagem de correio eletrónico ao Diretor Geral da empresa no dia 9 de Maio pelas 14h11, em que pedia autorização para a execução do teste de intrusão.
>
> Após conversa por telemóvel, que redundou nos pontos do contrato  acima, a resposta foi positiva, no mesmo dia pelas 16h05.


Notas:
1. O texto é apenas um exemplo, não cobre todos os pontos identificados no PTES e pode haver alguns pontos em que refere que não são feitos e vocês optarem por os fazer.
2. Quando tiverem o vosso texto pronto, o mesmo deverá ser revisto com o docente da UC que vos colocará em contacto eletrónico com os responsáveis das empresas.
3. Se acharem necessário podem fazer um texto de _Pre-engagement_ diferente para cada empresa.


### 1.2.4 Projeto mDL

Para o projeto mDL vão necessitar dos ISO/IEC CD 18013, em particular o _ISO/IEC CD 18013-5 Information technology -- Personal identification -- ISO compliant
driving licence -- Part 5: Mobile driving licence application (mDL)_.

Como estes documentos não são públicos, por favor contactem-me para vo-los poder fornecer, fazendo notar desde já que não os podem disponibilizar a terceiros.

### 1.2.5 Projeto Self-sovereign identity

Para além da bibliografia já fornecida no enunciado do projeto, é ainda relevante referir o seguinte:
+ The Basics of Decentralized Identity - https://medium.com/uport/the-basics-of-decentralized-identity-d1ff01f15df1
+ The Self-sovereign Identity Stack - https://medium.com/decentralized-identity/the-self-sovereign-identity-stack-8a2cc95f2d45
+ Three Self-Sovereign Identity Platforms to Watch - https://www.newamerica.org/future-property-rights/reports/nail-finds-hammer/three-self-sovereign-identity-platforms-to-watch/
+ Decentralized Identity Foundation - https://identity.foundation/



## 2. Projetos propostos pelos grupos

Os grupos que desejarem propor projetos deverão enviar uma descrição do mesmo ao docente da cadeira, até ao dia 18/Fevereiro, podendo o mesmo ser ou não aceite (ou ser aceite com alterações).

Projetos aceites:
+ [Vulnerabilities Mapping](VulnMapping.pdf) - Raphael Pinheiro
