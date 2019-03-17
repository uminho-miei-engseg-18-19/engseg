# TP  Class Assignment - 18/Mar/2019

Each group must answer the questions of the following exercises in the Github area of their group until the end of 18/Apr/2019\. For each day of delay, 0.15 points will be deducted from the grade of this assignment.



## Exercises

### 1\. GDPR (General Data Protection Regulation)

Among others, the following documents are available in the Aula7 directory:
+ Regulation (UE) 2016/679 (GDPR), in [portuguese](Aula7/UE_2016_679.RGPD.PT.pdf) and [english](Aula7/UE_2016_679.GDPR.ENG.pdf);
+ [Draft of the ISO 27552](Aula7/Draft.PIM_PbD.pdf) (_Security techniques - Extension to ISO/IEC 27001 and to ISO/IEC 27002 for privacy management — Requirements and guidelines_);
+ [_Standard	Data	Protection	Model_](Aula7/Germany.SDM-Methodology_V1.0.pdf) published by the german DPA (_Data Protection Atuhority_);
+ [_Handbook on European data protection law_](Aula7/EDPS-2018-handbook-data-protection_en.pdf), published by the [_European Data Protection Supervisor_](https://edps.europa.eu/);
+ Several documents provided by ENISA (_European Union Agency for Network and Information Security_) from its [Data Protecion](https://www.enisa.europa.eu/topics/data-protection) web page.


#### Question P1.1

In this question each group will perform a short review of the Regulation (UE) 2016/679 (RGPD) or the ISO 27552 (_Security techniques - Extension to ISO/IEC 27001 and to ISO/IEC 27002 for privacy management — Requirements and guidelines_) or the _Handbook on European data protection law_, in accordance with the following rules:

+ If the group chooses the GDPR, it should review the following article of the regulation and write a short text (between 1/2 and 1 page A4) that reflects on how this regulation article can influence the development of the software. Note that the document has 173 initial recitals, some of which may be relevant to this reflection.
  - Article 5º - Groups 1, 5, 9, 13
  - Article 25º - Groups 2, 6, 10, 14
  - Article 32º - Groups 3, 7, 11
  - Section 4 (Data Protection Officer) - Groups 4, 8, 12


+ If the group chooses the ISO 27552 draft, it should review the following section and write a short text (between 1/2 and 1 A4 page) that reflects on the implications that this point has on software development and / or operation.
  - 6.4 (_Human resource security_) e 6.5 (_Asset management_) - Groups 1, 5, 9, 13
  - 6.9 (_Operations Security_) - Groups 2, 6, 10, 14
  - 6.13 (_Information security incident management_) -  Groups 3, 7, 11
  - 6.15 (_Compliance_) - Groups 4, 8, 12


+ If the group chooses the _Handbook on European data protection law_, it should review the following section and write a short text (between 1/2 and 1 A4 page) reflecting on the implications of this subject for software development:
  + _Lawfulness, fairness and transparency of processing principles_ - section 3.1 - Group 1, 13;
  + _Principle of purpose limitation_ - section 3.2 - Group 2, 14;
  + _Data minimisation principle_ - section 3.3 - Group 3;
  + _Data accuracy principle_ - section 3.4 - Group 4;
  + _Storage limitation principle_ - section 3.5 - Group 5;
  + _Data security principle_ - section 3.6 - Group 6;
  + _Accountability principle_ - section 3.7 - Group 7;
  + _Right to be informed_ - section 6.1.1 - Group 8;
  + _Right to rectification_  - section 6.1.2 - Group 9;
  + _Right to erasure_ - section 6.1.3 - Group 10;
  + _Right to restriction of processing_ - section 6.1.4 - Group 11;
  + _Right to data portability_ - section 6.1.5 - Group 12;


Note that the analysis should only be done to one of the documents, and the group should choose which one it prefers, according to the previous rules.



#### Question P1.2

ENISA (European Union Agency for Network and Information Security) has done an excellent job in producing relevant documentation for data protection.


In the document  [_Recommendations on shaping technology according to GDPR provisions - An overview on data pseudonymisation_](Aula7/ENISA.WP2018-O.2.2.5-Recomendations-on-shaping-technology-according-to-GDPR-provisions-Part1.pdf) analyze the _Pseudonymisation techniques_ (section 3), and summarize them (between 1/2 and 1 page A4) -  Groups 1, 2, 3, 4 or 5.


In the document [_Recommendations on shaping technology according to GDPR provisions - Exploring the notion of data protection by default_](Aula7/ENISA.WP2018-O.2.2.5-Recommendations-on-shaping-technology-according-to-GDPR-provisions-Part2.pdf) analyze the _Data protection by default in practice_ (section 3), and summarize them (between 1/2 and 1 page A4) -  Groups 6, 7, 8, 9 ou 10.

In the document [_Privacy and Data Protection by Design – from policy to engineering_](Aula7/ENISA.Privacy-and-Data-Protection-by-Design.pdf) analyze the eight strategies of _privacy design_ (section 3.2), and summarize them (between 1/2 and 1 page A4) -  Groups  11, 12, 13 ou 14.


#### Experience 1.1

Table 1 of document  [_Online privacy tools for the general public - Towards a methodology for the evaluation of PETs for internet & mobile users_](Aula7/ENISA.Study-on-the-availability-of-trustworthy-online-privacy-tools-for-the-general-public.pdf) identifies
the most relevant web portals in promoting the use of tools that guarantee the privacy of the data (and / or the user).

Based on the web portals identified, carry out the following experiments:
+ Use the Panopticlick tool from _Electronic Frontier Foundation_ (EFF) to check if your browser is safe against _tracking_ - https://panopticlick.eff.org/
+ On _PRISM Break_ check which applications to avoid and which ones you should prefer on your platform - https://prism-break.org/en/
+ In _Security in-a-box_ check the tactic to protect sensitive files on your computer - https://securityinabox.org/en/guide/secure-file-storage/
+ Privacytools.io provides information on a broad set of privacy-preserving tools - https://www.privacytools.io/



#### Question P1.3

_ARTICLE 29 DATA PROTECTION WORKING PARTY_ published the [_Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is “likely to result in a high risk” for the purposes of Regulation 2016/679_](Aula7/EU.20171013_wp248_rev01_enpdf.pdf). These guidelines include the nine criteria that should be considered in order to assess whether the processing of personal data will result in a high risk - a DPIA should be performed whenever the processing meets two of these criteria.

1. Identify the nine criteria
2. Imagine that you are initiating a project that involves the use of personal data whose processing results in a high risk. Briefly explain the project and the processing, as well as the criteria that the processing satisfies.
3. Fill in the [DPIA template](Aula7/ICO.dpia-template.pdf).



#### Question P1.4

CNIL (_Commission Nationale de l'Informatique et des Libertés_) provided an open-source tool to help with the _Data Protection Impact Assessment_ (DPIA) at https://www.cnil.fr/en/open-source-pia-software-helps-carry-out-data-protection-impact-assesment.

1. Install the DPIA tool (available for Linux, Windows and MacOS) - https://www.cnil.fr/en/open-source-pia-software-helps-carry-out-data-protection-impact-assesment
2. Use the DPIA tool for the project you explained in the previous question, briefly filling in all the required components.
3. At the end of the validation, go to the dashboard and choose the list presentation, select "Display PIA" and print to PDF file. Put it in your group space in github, as a response to this question.

----

##  Engenharia de Segurança course - Project

You can use the rest of the class for the Engenharia de Segurança project.
