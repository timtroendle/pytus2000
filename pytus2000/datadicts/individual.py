"""This is a auto-generated data dictionary file of the UK Time Use Study 2000."""
from enum import Enum

from pytus2000.datadicts import OrderedEnum, VariableEnum


class Variable(VariableEnum):
    SN1 = (1, " SAMPLE POINT NUMBER")
    SN2 = (2, " HOUSHOLD NUMBER")
    SN3 = (3, "PERSON NUMBER")
    Q1A = (4, "Q1A. ANY PAID WORK IN 7 DAYS")
    PC1 = (5, "Under 16s only: paid job or work after school?")
    PC3 = (6, "Under 16s only: number of hours worked in last 7 days")
    Q1B = (7, "Q1B. GOVERNMENT SCHEME FOR EMPLOYMENT")
    Q1C = (8, "Q1C. ON GOVERNMENT SCHEME WERE THEY...")
    Q2A = (9, "Q2A JOB OR BUSINESS WERE AWAY FROM")
    Q2B = (10, "Q2B WHY WERE THEY AWAY")
    Q3A = (11, "Q3A ANY UNPAID WORK FOR BUSINESS THEY OWN?")
    Q3B = (12, "Q3B ANY UNPAID WORK FOR BUSINESS RELATIVE OWNS")
    Q3C = (13, "Ever had a paid job, apart from casual/holiday work?")
    Q3DD = (14, "Q3D WHEN LEFT LAST PAID JOB (DAY)")
    Q3DM = (15, "Q3D WHEN LEFT LAST PAID JOB (MONTH)")
    Q3DWK = (16, "Left last paid job in the last week?")
    Q3DY = (17, "Q3D WHEN LEFT LAST PAID JOB (YEAR)")
    Q5 = (18, "Q5 PRIVATE OR PUBLIC SECTOR?")
    Q7 = (19, "Q7 WORKING AS EMPLOYEE/SELF-EMPLOYED")
    Q8A = (20, "Q8A MANAGERIAL/SUPERVISOR DUTIES?")
    Q8B = (21, "Q8B NUMBER OF EMPLOYEES")
    Q8C = (22, "Q8C WORKING FULL/PART-TIME?")
    Q8D = (23, "Q8D ANY SHIFTWORK?")
    Q8E = (24, "Q8E TYPE OF SHIFT PATTERN")
    ATQ9A1 = (25, "Special working arrangements - flexitime?")
    ATQ9A2 = (26, "Special working arrangements - annualised hours contract?")
    ATQ9A3 = (27, "Special working arrangements - term time working?")
    ATQ9A4 = (28, "Special working arrangements - job sharing?")
    ATQ9A5 = (29, "Special working arrangements - 9 day fortnight?")
    ATQ9A6 = (30, "Special working arrangements - four & a half day week?")
    ATQ9A7 = (31, "Special working arrangements - zero hours contracted?")
    ATQ9A8 = (32, "Special working arrangements - none of these?")
    Q10 = (33, "Employee - take home pay after all deductions? POUNDS (period covered is given at Q11)")
    Q10X = (34, "Employee - q10 is 'missing'   - range estimate of take home pay?  (period covered is given at Q11)")
    Q11 = (35, "Employee - period covered by last take home pay (for figures given at Q10 and Q10x)")
    Q11A = (36, "Employee - q10 is 'dk/refuse' - range estimate of MONTHLY take home pay")
    Q11N = (37, "Employee - period covered by last take home pay IN HOURS (as written in)")
    Q12 = (38, "Employee - number of days paid holiday entitled to per year")
    Q12A = (39, "Employee - number of days paid holiday TAKEN last year")
    Q13A = (40, "Q13A ON OWN OR WITH EMPLOYEES?")
    Q13B = (41, "13B NUMBER PEOPLE AT THE PLACE WHERE WORKED?")
    Q13C = (42, "Self-employed - approximate net MONTHLY income - POUNDS")
    Q13D = (43, "Self-employed - q13c is 'dk/refuse' - estimated net MONTHLY income - BANDED")
    Q13E = (44, "Self-employed - full-time or part-time?")
    Q14A = (45, "Unpaid work for own/relative's business - hours worked per week")
    Q14B = (46, "All employees AND self-employed: Do you ever do any paid or unpaid OVERTIME?")
    Q14C = (47, "All employees AND self-employed: No overtime     - hours per week usually worked in MAIN JOB/business")
    Q14D = (48, "All employees AND self-employed: Work overtime - hours per week usually worked EXCLUDING overtime")
    Q14E = (49, "All employees AND self-employed: Work overtime - hours per week PAID OVERTIME usually worked")
    Q14F = (50, "All employees AND self-employed: Work overtime - hours per week UNPAID OVERTIME usually worked")
    Q15 = (51, "Q15:   Main place of work")
    Q15B = (52, "Q15B: Do you do any paid/ unpaid work at home for your main job?")
    Q15C = (53, "Q15C: Number of hours worked from home in last week")
    Q16A = (54, "Q16A ANY OTHER PAID WORK")
    Q16B = (55, "Q16B HOW MANY PAID JOBS IN OTHER PAID WORK")
    Q16F = (56, "Q16F HOURS/WEEK IN SECOND JOB")
    Q16G = (57, "Q16G ANY MANAGERIAL/SUPERVISOR DUTIES")
    Q16H = (58, "Q16H NUMBER OF EMPLOYEES")
    Q17 = (59, "Q17 LOOKING FOR JOB/SCHEME?")
    Q18A = (60, "Q18 VISIT A JOBCENTRE")
    Q18B = (61, "Q18 VISIT A CAREERS OFFICE")
    Q18C = (62, "Q18 VISIT A JOBCLUB")
    Q18D = (63, "Q18 PRIVATE EMPLOYMENT AGENCY")
    Q18E = (64, "Q18 ADVERTISE FOR JOBS NEWSPAPERS")
    Q18F = (65, "Q18 ANSWER ADVERTS IN NEWSPAPERS")
    Q18G = (66, "Q18 STUDY SIT. VAC. COLUMNS IN NEWSPAPERS")
    Q18H = (67, "Q18 APPLY DIRECTLY TO EMPLOYERS")
    Q18I = (68, "Q18 ASK FRIENDS/RELS/COLLEAGUES ABOUT JOBS")
    Q18J = (69, "Q18 WAIT FOR RESULTS OF APPLICATION")
    Q18K = (70, "Q18 DO ANYTHING ELSE TO FIND WORK?")
    Q19 = (71, "Q19 TAKEN JOB IF AVAILABLE LAST 2 WEEKS")
    Q20 = (72, "Q20 MAIN REASON DID NOT LOOK FOR WORK")
    ATQ21A1 = (73, "Q21A State benefits received - CHILD BENEFIT?")
    ATQ21A2 = (74, "Q21A State benefits received - GUARDIAN'S ALLOWANCE?")
    ATQ21A3 = (75, "Q21A State benefits received - INVALID CARE ALLOWANCE?")
    ATQ21A4 = (76, "Q21A State benefits received - RETIREMENT PENSION/ OLD PERSON'S PENSION?")
    ATQ21A5 = (77, "Q21A State benefits received - WIDOW'S PENSION/ WIDOWED MOTHER'S ALLOWANCE?")
    ATQ21A6 = (78, "Q21A State benefits received - WAR DISABLEMENT PENSION/ WAR WIDOW'S PENSION?")
    ATQ21A7 = (79, "Q21A State benefits received - SEVERE DISABLEMENT ALLOWANCE?")
    ATQ21A8 = (80, "Q21A State benefits received - DISABILITY WORKING ALLOWANCE?")
    ATQ21A9 = (81, "Q21A State benefits received - NONE OF THESE?")
    ATQ21A10 = (82, "Q21A State benefits received - DON'T KNOW")
    ATQ21A11 = (83, "Q21A State benefits received - REFUSE")
    ATQ21B1 = (84, "Q21B Other state benefits received - CARE COMPONENT OF DISABILITY LIVING ALLOWANCE?")
    ATQ21B2 = (85, "Q21B Other state benefits received - MOBILITY COMPONENT OF DISABILITY LIVING ALLOWANCE?")
    ATQ21B3 = (86, "Q21B Other state benefits received - ATTENDANCE ALLOWANCE?")
    ATQ21B4 = (87, "Q21B Other state benefits received - NONE OF THESE?")
    ATQ21B5 = (88, "Q21B Other state benefits received - DON'T KNOW")
    ATQ21B6 = (89, "Q21B Other state benefits received - REFUSE")
    Q21BA01 = (90, "Q21B RECEIVE CARE COMPONENT FOR PERSON 1")
    Q21BA02 = (91, "Q21B RECEIVE CARE COMPONENT FOR PERSON 2")
    Q21BA03 = (92, "Q21B RECEIVE CARE COMPONENT FOR PERSON 3")
    Q21BA04 = (93, "Q21B RECEIVE CARE COMPONENT FOR PERSON 4")
    Q21BA05 = (94, "Q21B RECEIVE CARE COMPONENT FOR PERSON 5")
    Q21BA06 = (95, "Q21B RECEIVE CARE COMPONENT FOR PERSON 6")
    Q21BA07 = (96, "Q21B RECEIVE CARE COMPONENT FOR PERSON 7")
    Q21BA08 = (97, "Q21B RECEIVE CARE COMPONENT FOR PERSON 8")
    Q21BA09 = (98, "Q21B RECEIVE CARE COMPONENT FOR PERSON 9")
    Q21BA10 = (99, "Q21B RECEIVE CARE COMPONENT FOR PERSON 10")
    Q21BA11 = (100, "Q21B CARE COMPONENT - DON'T KNOW")
    Q21BA12 = (101, "Q21B CARE COMPONENT - REFUSED")
    Q21BA13 = (102, "Q21B CARE COMPONENT - N/A")
    Q21BB01 = (103, "Q21B RECEIVE MOBILITY COMPONENT FOR PERSON 1")
    Q21BB02 = (104, "Q21B RECEIVE MOBILITY COMPONENT FOR PERSON 2")
    Q21BB03 = (105, "Q21B RECEIVE MOBILITY COMPONENT FOR PERSON 3")
    Q21BB04 = (106, "Q21B RECEIVE MOBILITY COMPONENT FOR PERSON 4")
    Q21BB05 = (107, "Q21B RECEIVE MOBILITY COMPONENT FOR PERSON 5")
    Q21BB06 = (108, "Q21B RECEIVE MOBILITY COMPONENT FOR PERSON 6")
    Q21BB07 = (109, "Q21B RECEIVE MOBILITY COMPONENT FOR PERSON 7")
    Q21BB08 = (110, "Q21B RECEIVE MOBILITY COMPONENT FOR PERSON 8")
    Q21BB09 = (111, "Q21B RECEIVE MOBILITY COMPONENT FOR PERSON 9")
    Q21BB10 = (112, "Q21B RECEIVE MOBILITY COMPONENT FOR PERSON 10")
    Q21BB11 = (113, "Q21B MOBILITY COMPONENT - DON'T KNOW")
    Q21BB12 = (114, "Q21B MOBILITY COMPONENT - REFUSED")
    Q21BB13 = (115, "Q21B MOBILITY COMPONENT - N/A")
    Q21BC01 = (116, "Q21B RECEIVE ATTENDANCE ALLOWANCE FOR PERSON 1")
    Q21BC02 = (117, "Q21B RECEIVE ATTENDANCE ALLOWANCE FOR PERSON 2")
    Q21BC03 = (118, "Q21B RECEIVE ATTENDANCE ALLOWANCE FOR PERSON 3")
    Q21BC04 = (119, "Q21B RECEIVE ATTENDANCE ALLOWANCE FOR PERSON 4")
    Q21BC05 = (120, "Q21B RECEIVE ATTENDANCE ALLOWANCE FOR PERSON 5")
    Q21BC06 = (121, "Q21B RECEIVE ATTENDANCE ALLOWANCE FOR PERSON 6")
    Q21BC07 = (122, "Q21B RECEIVE ATTENDANCE ALLOWANCE FOR PERSON 7")
    Q21BC08 = (123, "Q21B RECEIVE ATTENDANCE ALLOWANCE FOR PERSON 8")
    Q21BC09 = (124, "Q21B RECEIVE ATTENDANCE ALLOWANCE FOR PERSON 9")
    Q21BC10 = (125, "Q21B RECEIVE ATTENDANCE ALLOWANCE FOR PERSON 10")
    Q21BC11 = (126, "Q21B ATTENDANCE ALLOWANCE - DON'T KNOW")
    Q21BC12 = (127, "Q21B ATTENDANCE ALLOWANCE - REFUSED")
    Q21BC13 = (128, "Q21B ATTENDANCE ALLOWANCE - N/A")
    Q21C = (129, "Is attendance allowance paid as part of your retirement pensions or as a separate payment?")
    ATQ21D1 = (130, "Q21D Benefits received in own right - JOB SEEKERS ALLOWANCE?")
    ATQ21D2 = (131, "Q21D Benefits received in own right - INCOME SUPPORT?")
    ATQ21D3 = (132, "Q21D Benefits received in own right - INCAPACITY BENEFIT?")
    ATQ21D4 = (133, "Q21D Benefits received in own right - STATUTORY SICK PAY?")
    ATQ21D5 = (134, "Q21D Benefits received in own right - INDUSTRIAL INJURY DISABLEMENT BENEFIT?")
    ATQ21D6 = (135, "Q21D Benefits received in own right - NONE OF THESE?")
    ATQ21D7 = (136, "Q21D Benefits received in own right - DON'T KNOW")
    ATQ21D8 = (137, "Q21D Benefits received in own right - REFUSE")
    Q21E = (138, "Q21E Type of Job Seeker's Allowance")
    Q21F = (139, "Q21F Other benefits received in own right")
    ATQ21H1 = (140, "Q21H Benefits received in last 6 months - GRANT FROM SOCIAL FUND FOR FUNERAL EXPENSES?")
    ATQ21H2 = (141, "Q21H Benefits received in last 6 months - GRANT FOR MATERNITY EXPENSES?")
    ATQ21H3 = (142, "Q21H Benefits received in last 6 months - SOCIAL FUND LOAN OR COMMUNITY CARE GRANT?")
    ATQ21H4 = (143, "Q21H Benefits received in last 6 months - A BACK TO WORK BONUS?")
    ATQ21H5 = (144, "Q21H Benefits received in last 6 months - 'EXTENDED PAYMENT' OF HOUSING BENEFIT/ RENT REBATE, COUNCIL TAX?")
    ATQ21H6 = (145, "Q21H Benefits received in last 6 months - WIDOW'S PAYMENT LUMP SUM?")
    ATQ21H7 = (146, "Q21H Benefits received in last 6 months - CHILD MAINTENANCE BONUS?")
    ATQ21H8 = (147, "Q21H Benefits received in last 6 months - LONE PARENT'S BENEFIT RUN-ON")
    ATQ21H9 = (148, "Q21H Benefits received in last 6 months - ANY NAT INSURANCE OR STATE BENEFIT NOT MENTIONED EARLIER?")
    ATQ21H10 = (149, "Q21H Benefits received in last 6 months - NONE OF THESE?")
    ATQ21H11 = (150, "Q21H Benefits received in last 6 months - DON'T KNOW")
    ATQ21H12 = (151, "Q21H Benefits received in last 6 months - REFUSE")
    Q21HA = (152, "Q21Hi  For self-employed - tax credit payments received")
    Q21HB = (153, "Q21Hii For self-employed - LUMP SUM tax credit payments received")
    ATQ21HC1 = (154, "Q21Hiii  (For employees) Did last wage include.....  WORKING FAMILIIES TAX CREDIT?")
    ATQ21HC2 = (155, "Q21Hiii  (For employees) Did last wage include...... DISABLED PERSON'S TAX CREDIT?")
    ATQ21HC3 = (156, "Q21Hiii  (For employees) Did last wage include.......NONE OF THESE?")
    ATQ21HC4 = (157, "Q21Hiii  (For employees) Did last wage include........DON'T KNOW")
    ATQ21HC5 = (158, "Q21Hiii  (For employees) Did last wage include........REFUSE")
    Q22A = (159, "Q22A ANY QUALIFICATIONS")
    ATQ22B1 = (160, "Q22b Qualifications obtained - DEGREE?")
    ATQ22B2 = (161, "Q22b Qualifications obtained - DIPLOMA IN HIGHER EDUCATION?")
    ATQ22B3 = (162, "Q22b Qualifications obtained - HNC/ HND?")
    ATQ22B4 = (163, "Q22b Qualifications obtained - ONC/ OND?")
    ATQ22B5 = (164, "Q22b Qualifications obtained - BTEC, BEC OR TEC?")
    ATQ22B6 = (165, "Q22b Qualifications obtained - SCOTVEC, SCOTEC OR SCOTBEC?")
    ATQ22B7 = (166, "Q22b Qualifications obtained - TEACHING QUALIFICATION EXCLUDING PGCE?")
    ATQ22B8 = (167, "Q22b Qualifications obtained - NURSING OR OTHER MEDICAL QUALIFICATION?")
    ATQ22B9 = (168, "Q22b Qualifications obtained - OTHER HIGHER EDUCATION QUALIFICATION BELOW DEGREE LEVEL?")
    ATQ22B10 = (169, "Q22b Qualifications obtained - A LEVEL OR EQUIVALENT?")
    ATQ22B11 = (170, "Q22b Qualifications obtained - SCE HIGHERS?")
    ATQ22B12 = (171, "Q22b Qualifications obtained - NVQ/ SVQ?")
    ATQ22B13 = (172, "Q22b Qualifications obtained - GNVQ/ GSVQ?")
    ATQ22B14 = (173, "Q22b Qualifications obtained - AS LEVEL?")
    ATQ22B15 = (174, "Q22b Qualifications obtained - CERTIFICATE OF SIXTH YEAR STUDIES OR EQUIVALENT?")
    ATQ22B16 = (175, "Q22b Qualifications obtained - O LEVEL OR EQUIVALENT?")
    ATQ22B17 = (176, "Q22b Qualifications obtained - SCE STANDARD OR ORDINARY GRADE?")
    ATQ22B18 = (177, "Q22b Qualifications obtained - GCSE?")
    ATQ22B19 = (178, "Q22b Qualifications obtained - CSE?")
    ATQ22B20 = (179, "Q22b Qualifications obtained - RSA?")
    ATQ22B21 = (180, "Q22b Qualifications obtained - CITY & GUILDS?")
    ATQ22B22 = (181, "Q22b Qualifications obtained - YT CERTIFICATE/ YTP?")
    ATQ22B23 = (182, "Q22b Qualifications obtained - ANY OTHER QUALIFICATIONS (PROFESSIONAL/ VOCATIONAL/ FOREIGN)?")
    ATQ22B24 = (183, "Q22b Qualifications obtained - DON'T KNOW")
    ATQ22C1 = (184, "Q22c Type of degree - A HIGHER DEGREE (INCL PGCE)?")
    ATQ22C2 = (185, "Q22c Type of degree - A FIRST DEGREE?")
    ATQ22C3 = (186, "Q22c Type of degree - OTHER (EG CHARTERED ACCOUNTANT, GRADUATE MEMBER OF PROFESSIONAL INSTITUTE)?")
    ATQ22C4 = (187, "Q22c Type of degree - DON'T KNOW")
    ATQ22C5 = (188, "Q22c Type of degree - REFUSE")
    Q22D = (189, "Q22d Type of higher degree")
    Q22E = (190, "Q22e Highest BTEC qualification")
    Q22F = (191, "Q22F HIGHEST SCOTVEC QUALIFICATION....")
    ATQ22FI1 = (192, "Q22Fi Type of teaching qualification - for FURTHER EDUCATION?")
    ATQ22FI2 = (193, "Q22Fi Type of teaching qualification - for SECONDARY EDUCATION?")
    ATQ22FI3 = (194, "Q22Fi Type of teaching qualification - for PRIMARY EDUCATION?")
    ATQ22FI4 = (195, "Q22Fi Type of teaching qualification - DON'T KNOW type")
    ATQ22FI5 = (196, "Q22Fi Type of teaching qualification - REFUSED")
    Q22G = (197, "Q22g  Number of A levels")
    Q22H = (198, "Q22h  Number of Scottish Highers")
    Q22I = (199, "Q22I HIGHEST LEVEL OF FULL NVQ/SVQ")
    Q22J = (200, "Q22J HIGHEST GNVQ/GSVQ...")
    Q22K = (201, "Q22k  Number of AS Levels")
    Q22L = (202, "Q22L HIGHEST RSA....")
    Q22M = (203, "Q22M HIGHEST CITY AND GUILDS QUALIFICATION....")
    Q22N = (204, "Q22n  Any GCSEs at grade C or above, or SCEs at grade 1 - 3, or O levels grade C or above ?")
    Q22O = (205, "Q22o  Any CSEs at grade 1?")
    Q22P = (206, "Q22p  Number of passes at GCSEs grade C or above, or CSE grade 1, or O levels?")
    ATQ22Q1 = (207, "Q22Q  GCSE grade C/ CSE grade 1/ O level in English or mathematics  - IN ENGLISH?")
    ATQ22Q2 = (208, "Q22Q  GCSE grade C/ CSE grade 1/ O level in English or mathematics  - IN MATHEMATICS?")
    ATQ22Q3 = (209, "Q22Q  GCSE grade C/ CSE grade 1/ O level in English or mathematics  - NEITHER?")
    Q22R = (210, "Q22R  Are you doing/ have you completed a recognised trade apprenticeship?")
    Q23A = (211, "Q23a  Age left full-time education")
    Q23B = (212, "Q23b  Did you start any other full-time education within two years of that time?")
    Q23C = (213, "Q23c  How old were you when you finished that full-time education or training?")
    ATQ23D1 = (214, "Q23d  Are you studying for any of these qualifications now: DEGREE?")
    ATQ23D2 = (215, "Q23d  Are you studying for any of these qualifications now: DIPLOMA IN HIGHER EDUCATION?")
    ATQ23D3 = (216, "Q23d  Are you studying for any of these qualifications now: HNC/ HND?")
    ATQ23D4 = (217, "Q23d  Are you studying for any of these qualifications now: ONC/ OND?")
    ATQ23D5 = (218, "Q23d  Are you studying for any of these qualifications now: BTEC, BEC or BEC?")
    ATQ23D6 = (219, "Q23d  Are you studying for any of these qualifications now: SCOTVEC, SCOTEC or SCOTBEC?")
    ATQ23D7 = (220, "Q23d  Are you studying for any of these qualifications now: TEACHING QUALIFICATION EXCL PGCE?")
    ATQ23D8 = (221, "Q23d  Are you studying for any of these qualifications now: NURSING OR OTHER MEDICAL QUALIFICATION?")
    ATQ23D9 = (222, "Q23d  Are you studying for any of these qualifications now: OTHER HIGHER EDUCATIONAL QUALIFICATION?")
    ATQ23D10 = (223, "Q23d  Are you studying for any of these qualifications now: A LEVEL OR EQUIVALENT?")
    ATQ23D11 = (224, "Q23d  Are you studying for any of these qualifications now: SCE HIGHERS?")
    ATQ23D12 = (225, "Q23d  Are you studying for any of these qualifications now: NVQ/ SVQ?")
    ATQ23D13 = (226, "Q23d  Are you studying for any of these qualifications now: GNVQ/ GSVQ?")
    ATQ23D14 = (227, "Q23d  Are you studying for any of these qualifications now: AS LEVEL?")
    ATQ23D15 = (228, "Q23d  Are you studying for any of these qualifications now: CERTIFICATE OF 6TH YEAR STUDIES?")
    ATQ23D16 = (229, "Q23d  Are you studying for any of these qualifications now: O LEVEL OR EQUIVALENT")
    ATQ23D17 = (230, "Q23d  Are you studying for any of these qualifications now: SCE STANDARD/ ORDINARY GRADE?")
    ATQ23D18 = (231, "Q23d  Are you studying for any of these qualifications now: GCSE?")
    ATQ23D19 = (232, "Q23d  Are you studying for any of these qualifications now: CSE?")
    ATQ23D20 = (233, "Q23d  Are you studying for any of these qualifications now: RSA?")
    ATQ23D21 = (234, "Q23d  Are you studying for any of these qualifications now: CITY & GUILDS?")
    ATQ23D22 = (235, "Q23d  Are you studying for any of these qualifications now: YT CERTIFICATE?")
    ATQ23D23 = (236, "Q23d  Are you studying for any of these qualifications now: ANY OTHER QUALIFICATIONS (PROFESSIONAL/ VOCATIONAL/ FOREIGN)?")
    ATQ23D24 = (237, "Q23d  Are you studying for any of these qualifications now: DON'T KNOW")
    ATQ23D25 = (238, "Q23d  Are you studying for any of these qualifications now: REFUSED")
    Q23DI = (239, "Q23DI DEGREE STUDYING FOR...")
    Q23DII = (240, "Q23DII HIGHER DEGREE STUDYING FOR...")
    Q23E = (241, "Q23E LEVEL BTEC STUDYING FOR")
    Q23EI = (242, "Q23EI LEVEL SCOTVEC/SCOTEC STUDYING FOR")
    Q23F = (243, "Q23F LEVEL CITY AND GUILDS STUDYING FOR")
    Q23G = (244, "Q23G LEVEL RSA STUDYING FOR")
    Q23H = (245, "Q23H LEVEL NVQ/SVQ STUDYING FOR")
    Q23I = (246, "Q23I LEVEL GNVQ/GSVQ STUDYING FOR")
    Q23J = (247, "Q23J WHERE STUDYING")
    ATQ24A1 = (248, "Q24a  BEEN ON ANY TAUGHT COURSES IN LAST 4 WEEKS - a course meant to lead to qualifications?")
    ATQ24A2 = (249, "Q24a  BEEN ON ANY TAUGHT COURSES IN LAST 4 WEEKS - designed to develop job skills?")
    ATQ24A3 = (250, "Q24a  BEEN ON ANY TAUGHT COURSES IN LAST 4 WEEKS - driving, musical instruments, art, craft, skill?")
    ATQ24A4 = (251, "Q24a  BEEN ON ANY TAUGHT COURSES IN LAST 4 WEEKS - evening classes?")
    ATQ24A5 = (252, "Q24a  BEEN ON ANY TAUGHT COURSES IN LAST 4 WEEKS - working on own from a package of materials?")
    ATQ24A6 = (253, "Q24a  BEEN ON ANY TAUGHT COURSES IN LAST 4 WEEKS - other taught course/ tuition/ instruction?")
    ATQ24A7 = (254, "Q24a  BEEN ON ANY TAUGHT COURSES IN LAST 4 WEEKS - none of these")
    ATQ24A8 = (255, "Q24a  BEEN ON ANY TAUGHT COURSES IN LAST 4 WEEKS - Don't Know")
    ATQ24A9 = (256, "Q24a  BEEN ON ANY TAUGHT COURSES IN LAST 4 WEEKS - Refused")
    Q24B = (257, "24B HOW MANY TAUGHT COURSES IN PAST 4 WEEKS")
    Q24CA = (258, "Subject of course/ period of learning - FIRST COURSE")
    Q24CB = (259, "Subject of course/ period of learning - SECOND COURSE")
    Q24CC = (260, "Subject of course/ period of learning - THIRD COURSE")
    Q24CD = (261, "Subject of course/ period of learning - FOURTH COURSE")
    Q24CE = (262, "Subject of course/ period of learning - FIFTH COURSE")
    Q24CF = (263, "Subject of course/ period of learning - SIXTH COURSE")
    Q24CG = (264, "Subject of course/ period of learning - SEVENTH COURSE")
    Q24CH = (265, "Subject of course/ period of learning - EIGHTH COURSE")
    Q24CI = (266, "Subject of course/ period of learning - NINTH COURSE")
    Q24DA = (267, "Q24d  Was period of learning/ course designed to lead to a qualification? - 1st COURSE MENTIONED")
    Q24DB = (268, "Q24d  Was period of learning/ course designed to lead to a qualification? - 2nd COURSE MENTIONED")
    Q24DC = (269, "Q24d  Was period of learning/ course designed to lead to a qualification? - 3rd COURSE MENTIONED")
    Q24DD = (270, "Q24d  Was period of learning/ course designed to lead to a qualification? - 4th COURSE MENTIONED")
    Q24DE = (271, "Q24d  Was period of learning/ course designed to lead to a qualification? - 5th COURSE MENTIONED")
    Q24DF = (272, "Q24d  Was period of learning/ course designed to lead to a qualification? - 6th COURSE MENTIONED")
    Q24DG = (273, "Q24d  Was period of learning/ course designed to lead to a qualification? - 7th COURSE MENTIONED")
    Q24DH = (274, "Q24d  Was period of learning/ course designed to lead to a qualification? - 8th COURSE MENTIONED")
    Q24DI = (275, "Q24d  Was period of learning/ course designed to lead to a qualification? - 9th COURSE MENTIONED")
    ATQ24EA1 = (276, "Q24E  Qualifications studying for (on FIRST course mentioned): DEGREE?")
    ATQ24EA2 = (277, "Q24E  Qualifications studying for (on FIRST course mentioned): DIPLOMA IN HIGHER EDUCATION?")
    ATQ24EA3 = (278, "Q24E  Qualifications studying for (on FIRST course mentioned): HNC/ HND?")
    ATQ24EA4 = (279, "Q24E  Qualifications studying for (on FIRST course mentioned): ONC/ OND?")
    ATQ24EA5 = (280, "Q24E  Qualifications studying for (on FIRST course mentioned): BTEC, BEC or BEC?")
    ATQ24EA6 = (281, "Q24E  Qualifications studying for (on FIRST course mentioned): SCOTVEC, SCOTEC or SCOTBEC?")
    ATQ24EA7 = (282, "Q24E  Qualifications studying for (on FIRST course mentioned): TEACHING QUALIFICATION EXCL PGCE?")
    ATQ24EA8 = (283, "Q24E  Qualifications studying for (on FIRST course mentioned): NURSING OR OTHER MEDICAL QUALIFICATION?")
    ATQ24EA9 = (284, "Q24E  Qualifications studying for (on FIRST course mentioned): OTHER HIGHER EDUCATIONAL QUALIFICATION?")
    ATQ24EA10 = (285, "Q24E  Qualifications studying for (on FIRST course mentioned): A LEVEL OR EQUIVALENT?")
    ATQ24EA11 = (286, "Q24E  Qualifications studying for (on FIRST course mentioned): SCE HIGHERS?")
    ATQ24EA12 = (287, "Q24E  Qualifications studying for (on FIRST course mentioned): NVQ/ SVQ?")
    ATQ24EA13 = (288, "Q24E  Qualifications studying for (on FIRST course mentioned): GNVQ/ GSVQ?")
    ATQ24EA14 = (289, "Q24E  Qualifications studying for (on FIRST course mentioned): AS LEVEL?")
    ATQ24EA15 = (290, "Q24E  Qualifications studying for (on FIRST course mentioned): CERTIFICATE OF 6TH YEAR STUDIES?")
    ATQ24EA16 = (291, "Q24E  Qualifications studying for (on FIRST course mentioned): O LEVEL OR EQUIVALENT")
    ATQ24EA17 = (292, "Q24E  Qualifications studying for (on FIRST course mentioned): SCE STANDARD/ ORDINARY GRADE?")
    ATQ24EA18 = (293, "Q24E  Qualifications studying for (on FIRST course mentioned): GCSE?")
    ATQ24EA19 = (294, "Q24E  Qualifications studying for (on FIRST course mentioned): CSE?")
    ATQ24EA20 = (295, "Q24E  Qualifications studying for (on FIRST course mentioned): RSA?")
    ATQ24EA21 = (296, "Q24E  Qualifications studying for (on FIRST course mentioned): CITY & GUILDS?")
    ATQ24EA22 = (297, "Q24E  Qualifications studying for (on FIRST course mentioned): YT CERTIFICATE?")
    ATQ24EA23 = (298, "Q24E  Qualifications studying for (on FIRST course mentioned): ANY OTHER QUALIFICATIONS (PROFESSIONAL/ VOCATIONAL/ FOREIGN)?")
    ATQ24EB1 = (299, "Q24E  Qualifications studying for (on SECOND course mentioned): DEGREE?")
    ATQ24EB2 = (300, "Q24E  Qualifications studying for (on SECOND course mentioned): DIPLOMA IN HIGHER EDUCATION?")
    ATQ24EB3 = (301, "Q24E  Qualifications studying for (on SECOND course mentioned): HNC/ HND?")
    ATQ24EB4 = (302, "Q24E  Qualifications studying for (on SECOND course mentioned): ONC/ OND?")
    ATQ24EB5 = (303, "Q24E  Qualifications studying for (on SECOND course mentioned): BTEC, BEC or BEC?")
    ATQ24EB6 = (304, "Q24E  Qualifications studying for (on SECOND course mentioned): SCOTVEC, SCOTEC or SCOTBEC?")
    ATQ24EB7 = (305, "Q24E  Qualifications studying for (on SECOND course mentioned): TEACHING QUALIFICATION EXCL PGCE?")
    ATQ24EB8 = (306, "Q24E  Qualifications studying for (on SECOND course mentioned): NURSING OR OTHER MEDICAL QUALIFICATION?")
    ATQ24EB9 = (307, "Q24E  Qualifications studying for (on SECOND course mentioned): OTHER HIGHER EDUCATIONAL QUALIFICATION?")
    ATQ24EB10 = (308, "Q24E  Qualifications studying for (on SECOND course mentioned): A LEVEL OR EQUIVALENT?")
    ATQ24EB11 = (309, "Q24E  Qualifications studying for (on SECOND course mentioned): SCE HIGHERS?")
    ATQ24EB12 = (310, "Q24E  Qualifications studying for (on SECOND course mentioned): NVQ/ SVQ?")
    ATQ24EB13 = (311, "Q24E  Qualifications studying for (on SECOND course mentioned): GNVQ/ GSVQ?")
    ATQ24EB14 = (312, "Q24E  Qualifications studying for (on SECOND course mentioned): AS LEVEL?")
    ATQ24EB15 = (313, "Q24E  Qualifications studying for (on SECOND course mentioned): CERTIFICATE OF 6TH YEAR STUDIES?")
    ATQ24EB16 = (314, "Q24E  Qualifications studying for (on SECOND course mentioned): O LEVEL OR EQUIVALENT")
    ATQ24EB17 = (315, "Q24E  Qualifications studying for (on SECOND course mentioned): SCE STANDARD/ ORDINARY GRADE?")
    ATQ24EB18 = (316, "Q24E  Qualifications studying for (on SECOND course mentioned): GCSE?")
    ATQ24EB19 = (317, "Q24E  Qualifications studying for (on SECOND course mentioned): CSE?")
    ATQ24EB20 = (318, "Q24E  Qualifications studying for (on SECOND course mentioned): RSA?")
    ATQ24EB21 = (319, "Q24E  Qualifications studying for (on SECOND course mentioned): CITY & GUILDS?")
    ATQ24EB22 = (320, "Q24E  Qualifications studying for (on SECOND course mentioned): YT CERTIFICATE?")
    ATQ24EB23 = (321, "Q24E  Qualifications studying for (on SECOND course mentioned): ANY OTHER QUALIFICATIONS (PROFESSIONAL/ VOCATIONAL/ FOREIGN)?")
    Q24EC = (322, "Q24E  Qualifications studying for (on 3rd course mentioned)")
    Q24ED = (323, "Q24E  Qualifications studying for (on 4th course mentioned)")
    Q24EE = (324, "Q24E  Qualifications studying for (on 5th course mentioned)")
    Q24EF = (325, "Q24E  Qualifications studying for (on 6th course mentioned)")
    Q24EG = (326, "Q24E  Qualifications studying for (on 7th course mentioned)")
    Q24EH = (327, "Q24E  Qualifications studying for (on 8th course mentioned)")
    Q24EI = (328, "Q24E  Qualifications studying for (on 9th course mentioned)")
    Q24FA = (329, "Q24F  Where teaching took place (on FIRST course mentioned)")
    Q24FB = (330, "Q24F  Where teaching took place (on SECOND course mentioned)")
    Q24FC = (331, "Q24F  Where teaching took place (on THIRD course mentioned)")
    Q24FD = (332, "Q24F  Where teaching took place (on FOURTH course mentioned)")
    Q24FE = (333, "Q24F  Where teaching took place (on FIFTH course mentioned)")
    Q24FF = (334, "Q24F  Where teaching took place (on SIXTH course mentioned)")
    Q24FG = (335, "Q24F  Where teaching took place (on SEVENTH course mentioned)")
    Q24FH = (336, "Q24F  Where teaching took place (on EIGHTH course mentioned)")
    Q24FI = (337, "Q24F  Where teaching took place (on NINTH course mentioned)")
    Q24GA = (338, "Q24G  Number of occasions in past 4 weeks spent studying (for FIRST course mentioned)")
    Q24GB = (339, "Q24G  Number of occasions in past 4 weeks spent studying (for SECOND course mentioned)")
    Q24GC = (340, "Q24G  Number of occasions in past 4 weeks spent studying (for THIRD course mentioned)")
    Q24GD = (341, "Q24G  Number of occasions in past 4 weeks spent studying (for FOURTH course mentioned)")
    Q24GE = (342, "Q24G  Number of occasions in past 4 weeks spent studying (for FIFTH course mentioned)")
    Q24GF = (343, "Q24G  Number of occasions in past 4 weeks spent studying (for SIXTH course mentioned)")
    Q24GG = (344, "Q24G  Number of occasions in past 4 weeks spent studying (for SEVENTH course mentioned)")
    Q24GH = (345, "Q24G  Number of occasions in past 4 weeks spent studying (for EIGHTH course mentioned)")
    Q24GI = (346, "Q24G  Number of occasions in past 4 weeks spent studying (for NINTH course mentioned)")
    Q24HA = (347, "Q24H  Number of hours spent studying the last time studied (for FIRST course mentioned)")
    Q24HB = (348, "Q24H  Number of hours spent studying the last time studied (for SECOND course mentioned)")
    Q24HC = (349, "Q24H  Number of hours spent studying the last time studied (for THIRD course mentioned)")
    Q24HD = (350, "Q24H  Number of hours spent studying the last time studied (for FOURTH course mentioned)")
    Q24HE = (351, "Q24H  Number of hours spent studying the last time studied (for FIFTH course mentioned)")
    Q24HF = (352, "Q24H  Number of hours spent studying the last time studied (for SIXTH course mentioned)")
    Q24HG = (353, "Q24H  Number of hours spent studying the last time studied (for SEVENTH course mentioned)")
    Q24HH = (354, "Q24H  Number of hours spent studying the last time studied (for EIGHTH course mentioned)")
    Q24HI = (355, "Q24H  Number of hours spent studying the last time studied (for NINTH course mentioned)")
    ATQ25A1 = (356, "Q25a   Studying/ training NOT on a taught course in previous 4 weeks - STUDY FOR A QUALIFICATION?")
    ATQ25A2 = (357, "Q25a   Studying/ training NOT on a taught course in previous 4 weeks - SUPERVISED ON-THE-JOB TRAINING?")
    ATQ25A3 = (358, "Q25a   Studying/ training NOT on a taught course in previous 4 weeks - READ JOB-RELATED BOOKS, JOURNALS OR ATTEND SEMINARS?")
    ATQ25A4 = (359, "Q25a   Studying/ training NOT on a taught course in previous 4 weeks - ANY OTHER TIME SPENT IMPROVING KNOWLEDGE/ SKILLS?")
    ATQ25A5 = (360, "Q25a   Studying/ training NOT on a taught course in previous 4 weeks - NO, NONE OF THESE?")
    ATQ25A6 = (361, "Q25a   Studying/ training NOT on a taught course in previous 4 weeks - DON'T KNOW")
    ATQ25A7 = (362, "Q25a   Studying/ training NOT on a taught course in previous 4 weeks - REFUSED")
    Q25B = (363, "Q25b   SELF-DIRECTED training/studying: Number of hours spent in previous 4 weeks?")
    Q25C = (364, "Q25c   SELF-DIRECTED training/studying: Number of separate days spent?")
    Q25D = (365, "Q25d   SELF-DIRECTED training/studying: Over what period of time spent 3 or more days training?")
    Q25E = (366, "Q25e   Do you currently hold a full licence to drive a car?")
    Q26A = (367, "Q26a   Any voluntary work through GROUP or ORGANISATION in last 4 weeks?")
    Q26B1 = (368, "Q26b   FIRST voluntary group /organisation worked with")
    Q26B2 = (369, "Q26b   SECOND voluntary group /organisation worked with")
    Q26B3 = (370, "Q26b   THIRD voluntary group /organisation worked with")
    Q26B4 = (371, "Q26b   FOURTH voluntary group /organisation worked with")
    Q26B5 = (372, "Q26b   FIFTH voluntary group /organisation worked with")
    Q26B6 = (373, "Q26b   SIXTH voluntary group /organisation worked with")
    ATQ26CA1 = (374, "Q26c  Adult qstnre: FIRST voluntary group - type of work done - RAISING/ HANDLING MONEY?")
    ATQ26CA2 = (375, "Q26c  Adult qstnre: FIRST voluntary group - type of work done - MEMBER OF COMMITTEE?")
    ATQ26CA3 = (376, "Q26c  Adult qstnre: FIRST voluntary group - type of work done - ORGANISING OR HELPING RUN AN EVENT?")
    ATQ26CA4 = (377, "Q26c  Adult qstnre: FIRST voluntary group - type of work done - VISITING PEOPLE?")
    ATQ26CA5 = (378, "Q26c  Adult qstnre: FIRST voluntary group - type of work done - GIVING ADVICE, INFORMATION OR COUNSELING?")
    ATQ26CA6 = (379, "Q26c  Adult qstnre: FIRST voluntary group - type of work done - SECRETARIAL, ADMIN OR CLERICAL WORK?")
    ATQ26CA7 = (380, "Q26c  Adult qstnre: FIRST voluntary group - type of work done - PROVIDING TRANSPORT?")
    ATQ26CA8 = (381, "Q26c  Adult qstnre: FIRST voluntary group - type of work done - OTHER DIRECT SERVICES?")
    ATQ26CA9 = (382, "Q26c  Adult qstnre: FIRST voluntary group - type of work done - REPRESENTING?")
    ATQ26CA10 = (383, "Q26c  Child qstnre: FIRST voluntary group - type of work done - HELPING RAISE MONEY?")
    ATQ26CA11 = (384, "Q26c  Child qstnre: FIRST voluntary group - type of work done - HELPING TO RUN AN ACTIVITY?")
    ATQ26CA12 = (385, "Q26c  Child qstnre: FIRST voluntary group - type of work done - VISITING PEOPLE?")
    ATQ26CA13 = (386, "Q26c  Child qstnre: FIRST voluntary group - type of work done - CONSERVATION WORK?")
    ATQ26CA14 = (387, "Q26c  Adult & child qstnre: FIRST voluntary group - type of work done - OTHER?")
    ATQ26CA15 = (388, "Q26c  Adult & child qstnre: FIRST voluntary group - type of work done - DON'T KNOW?")
    ATQ26CA16 = (389, "Q26c  Adult & child qstnre: FIRST voluntary group - type of work done - REFUSED?")
    ATQ26CB1 = (390, "Q26c  Adult qstnre: SECOND voluntary group - type of work done - RAISING/ HANDLING MONEY?")
    ATQ26CB2 = (391, "Q26c  Adult qstnre: SECOND voluntary group - type of work done - MEMBER OF COMMITTEE?")
    ATQ26CB3 = (392, "Q26c  Adult qstnre: SECOND voluntary group - type of work done - ORGANISING OR HELPING RUN AN EVENT?")
    ATQ26CB4 = (393, "Q26c  Adult qstnre: SECOND voluntary group - type of work done - VISITING PEOPLE?")
    ATQ26CB5 = (394, "Q26c  Adult qstnre: SECOND voluntary group - type of work done - GIVING ADVICE, INFORMATION OR COUNSELING?")
    ATQ26CB6 = (395, "Q26c  Adult qstnre: SECOND voluntary group - type of work done - SECRETARIAL, ADMIN OR CLERICAL WORK?")
    ATQ26CB7 = (396, "Q26c  Adult qstnre: SECOND voluntary group - type of work done - PROVIDING TRANSPORT?")
    ATQ26CB8 = (397, "Q26c  Adult qstnre: SECOND voluntary group - type of work done - OTHER DIRECT SERVICES?")
    ATQ26CB9 = (398, "Q26c  Adult qstnre: SECOND voluntary group - type of work done - REPRESENTING?")
    ATQ26CB10 = (399, "Q26c  Child qstnre: SECOND voluntary group - type of work done - HELPING RAISE MONEY?")
    ATQ26CB11 = (400, "Q26c  Child qstnre: SECOND voluntary group - type of work done - HELPING TO RUN AN ACTIVITY?")
    ATQ26CB12 = (401, "Q26c  Child qstnre: SECOND voluntary group - type of work done - VISITING PEOPLE?")
    ATQ26CB13 = (402, "Q26c  Child qstnre: SECOND voluntary group - type of work done - CONSERVATION WORK?")
    ATQ26CB14 = (403, "Q26c  Adult & child qstnre: SECOND voluntary group - type of work done - OTHER?")
    ATQ26CB15 = (404, "Q26c  Adult & child qstnre: SECOND voluntary group - type of work done - DON'T KNOW?")
    ATQ26CB16 = (405, "Q26c  Adult & child qstnre: SECOND voluntary group - type of work done - REFUSED?")
    ATQ26CC1 = (406, "Q26c  Adult qstnre: THIRD voluntary group - type of work done - RAISING/ HANDLING MONEY?")
    ATQ26CC2 = (407, "Q26c  Adult qstnre: THIRD voluntary group - type of work done - MEMBER OF COMMITTEE?")
    ATQ26CC3 = (408, "Q26c  Adult qstnre: THIRD voluntary group - type of work done - ORGANISING OR HELPING RUN AN EVENT?")
    ATQ26CC4 = (409, "Q26c  Adult qstnre: THIRD voluntary group - type of work done - VISITING PEOPLE?")
    ATQ26CC5 = (410, "Q26c  Adult qstnre: THIRD voluntary group - type of work done - GIVING ADVICE, INFORMATION OR COUNSELING?")
    ATQ26CC6 = (411, "Q26c  Adult qstnre: THIRD voluntary group - type of work done - SECRETARIAL, ADMIN OR CLERICAL WORK?")
    ATQ26CC7 = (412, "Q26c  Adult qstnre: THIRD voluntary group - type of work done - PROVIDING TRANSPORT?")
    ATQ26CC8 = (413, "Q26c  Adult qstnre: THIRD voluntary group - type of work done - OTHER DIRECT SERVICES?")
    ATQ26CC9 = (414, "Q26c  Adult qstnre: THIRD voluntary group - type of work done - REPRESENTING?")
    ATQ26CC10 = (415, "Q26c  Child qstnre: THIRD voluntary group - type of work done - HELPING RAISE MONEY?")
    ATQ26CC11 = (416, "Q26c  Child qstnre: THIRD voluntary group - type of work done - HELPING TO RUN AN ACTIVITY?")
    ATQ26CC12 = (417, "Q26c  Child qstnre: THIRD voluntary group - type of work done - VISITING PEOPLE?")
    ATQ26CC13 = (418, "Q26c  Child qstnre: THIRD voluntary group - type of work done - CONSERVATION WORK?")
    ATQ26CC14 = (419, "Q26c  Adult & child qstnre: THIRD voluntary group - type of work done - OTHER?")
    ATQ26CC15 = (420, "Q26c  Adult & child qstnre: THIRD voluntary group - type of work done - DON'T KNOW?")
    ATQ26CC16 = (421, "Q26c  Adult & child qstnre: THIRD voluntary group - type of work done - REFUSED?")
    ATQ26CD1 = (422, "Q26c  Adult qstnre: FOURTH voluntary group - type of work done - RAISING/ HANDLING MONEY?")
    ATQ26CD2 = (423, "Q26c  Adult qstnre: FOURTH voluntary group - type of work done - MEMBER OF COMMITTEE?")
    ATQ26CD3 = (424, "Q26c  Adult qstnre: FOURTH voluntary group - type of work done - ORGANISING OR HELPING RUN AN EVENT?")
    ATQ26CD4 = (425, "Q26c  Adult qstnre: FOURTH voluntary group - type of work done - VISITING PEOPLE?")
    ATQ26CD5 = (426, "Q26c  Adult qstnre: FOURTH voluntary group - type of work done - GIVING ADVICE, INFORMATION OR COUNSELING?")
    ATQ26CD6 = (427, "Q26c  Adult qstnre: FOURTH voluntary group - type of work done - SECRETARIAL, ADMIN OR CLERICAL WORK?")
    ATQ26CD7 = (428, "Q26c  Adult qstnre: FOURTH voluntary group - type of work done - PROVIDING TRANSPORT?")
    ATQ26CD8 = (429, "Q26c  Adult qstnre: FOURTH voluntary group - type of work done - OTHER DIRECT SERVICES?")
    ATQ26CD9 = (430, "Q26c  Adult qstnre: FOURTH voluntary group - type of work done - REPRESENTING?")
    ATQ26CD10 = (431, "Q26c  Child qstnre: FOURTH voluntary group - type of work done - HELPING RAISE MONEY?")
    ATQ26CD11 = (432, "Q26c  Child qstnre: FOURTH voluntary group - type of work done - HELPING TO RUN AN ACTIVITY?")
    ATQ26CD12 = (433, "Q26c  Child qstnre: FOURTH voluntary group - type of work done - VISITING PEOPLE?")
    ATQ26CD13 = (434, "Q26c  Child qstnre: FOURTH voluntary group - type of work done - CONSERVATION WORK?")
    ATQ26CD14 = (435, "Q26c  Adult & child qstnre:  FOURTH voluntary group - type of work done - OTHER?")
    ATQ26CD15 = (436, "Q26c  Adult & child qstnre: FOURTH voluntary group - type of work done - DON'T KNOW?")
    ATQ26CD16 = (437, "Q26c  Adult & child qstnre: FOURTH voluntary group - type of work done - REFUSED?")
    ATQ26CE1 = (438, "Q26c  Adult qstnre: FIFTH voluntary group - type of work done - RAISING/ HANDLING MONEY?")
    ATQ26CE2 = (439, "Q26c  Adult qstnre: FIFTH voluntary group - type of work done - MEMBER OF COMMITTEE?")
    ATQ26CE3 = (440, "Q26c  Adult qstnre: FIFTH voluntary group - type of work done - ORGANISING OR HELPING RUN AN EVENT?")
    ATQ26CE4 = (441, "Q26c  Adult qstnre: FIFTH voluntary group - type of work done - VISITING PEOPLE?")
    ATQ26CE5 = (442, "Q26c  Adult qstnre: FIFTH voluntary group - type of work done - GIVING ADVICE, INFORMATION OR COUNSELING?")
    ATQ26CE6 = (443, "Q26c  Adult qstnre: FIFTH voluntary group - type of work done - SECRETARIAL, ADMIN OR CLERICAL WORK?")
    ATQ26CE7 = (444, "Q26c  Adult qstnre: FIFTH voluntary group - type of work done - PROVIDING TRANSPORT?")
    ATQ26CE8 = (445, "Q26c  Adult qstnre: FIFTH voluntary group - type of work done - OTHER DIRECT SERVICES?")
    ATQ26CE9 = (446, "Q26c  Adult qstnre: FIFTH voluntary group - type of work done - REPRESENTING?")
    ATQ26CE10 = (447, "Q26c  Child qstnre: FIFTH voluntary group - type of work done - HELPING RAISE MONEY?")
    ATQ26CE11 = (448, "Q26c  Child qstnre: FIFTH voluntary group - type of work done - HELPING TO RUN AN ACTIVITY?")
    ATQ26CE12 = (449, "Q26c  Child qstnre: FIFTH voluntary group - type of work done - VISITING PEOPLE?")
    ATQ26CE13 = (450, "Q26c  Child qstnre: FIFTH voluntary group - type of work done - CONSERVATION WORK?")
    ATQ26CE14 = (451, "Q26c  Adult & child qstnre:   FIFTH voluntary group - type of work done - OTHER?")
    ATQ26CE15 = (452, "Q26c  Adult & child qstnre: FIFTH voluntary group - type of work done - DON'T KNOW?")
    ATQ26CE16 = (453, "Q26c  Adult & child qstnre:   FIFTH voluntary group - type of work done - REFUSED?")
    ATQ26CF1 = (454, "Q26c  Adult qstnre: SIXTH voluntary group - type of work done - RAISING/ HANDLING MONEY?")
    ATQ26CF2 = (455, "Q26c  Adult qstnre: SIXTH voluntary group - type of work done - MEMBER OF COMMITTEE?")
    ATQ26CF3 = (456, "Q26c  Adult qstnre: SIXTH voluntary group - type of work done - ORGANISING OR HELPING RUN AN EVENT?")
    ATQ26CF4 = (457, "Q26c  Adult qstnre: SIXTH voluntary group - type of work done - VISITING PEOPLE?")
    ATQ26CF5 = (458, "Q26c  Adult qstnre: SIXTH voluntary group - type of work done - GIVING ADVICE, INFORMATION OR COUNSELING?")
    ATQ26CF6 = (459, "Q26c  Adult qstnre: SIXTH voluntary group - type of work done - SECRETARIAL, ADMIN OR CLERICAL WORK?")
    ATQ26CF7 = (460, "Q26c  Adult qstnre: SIXTH voluntary group - type of work done - PROVIDING TRANSPORT?")
    ATQ26CF8 = (461, "Q26c  Adult qstnre: SIXTH voluntary group - type of work done - OTHER DIRECT SERVICES?")
    ATQ26CF9 = (462, "Q26c  Adult qstnre: SIXTH voluntary group - type of work done - REPRESENTING?")
    ATQ26CF10 = (463, "Q26c  Child qstnre: SIXTH voluntary group - type of work done - HELPING RAISE MONEY?")
    ATQ26CF11 = (464, "Q26c  Child qstnre: SIXTH voluntary group - type of work done - HELPING TO RUN AN ACTIVITY?")
    ATQ26CF12 = (465, "Q26c  Child qstnre: SIXTH voluntary group - type of work done - VISITING PEOPLE?")
    ATQ26CF13 = (466, "Q26c  Child qstnre: SIXTH voluntary group - type of work done - CONSERVATION WORK?")
    ATQ26CF14 = (467, "Q26c  Adult & child qstnre: SIXTH voluntary group - type of work done - OTHER?")
    ATQ26CF15 = (468, "Q26c  Adult & child qstnre: SIXTH voluntary group - type of work done - DON'T KNOW?")
    ATQ26CF16 = (469, "Q26c  Adult & child qstnre: SIXTH voluntary group - type of work done - REFUSED?")
    Q26DA = (470, "Q26d   FIRST voluntary group - Number of times did voluntary work for them in last 4 weeks?")
    Q26DB = (471, "Q26d   SECOND voluntary group - Number of times did voluntary work for them in last 4 weeks?")
    Q26DC = (472, "Q26d   THIRD voluntary group - Number of times did voluntary work for them in last 4 weeks?")
    Q26DD = (473, "Q26d   FOURTH voluntary group - Number of times did voluntary work for them in last 4 weeks?")
    Q26DE = (474, "Q26d   FIFTH voluntary group - Number of times did voluntary work for them in last 4 weeks?")
    Q26DF = (475, "Q26d   SIXTH voluntary group - Number of times did voluntary work for them in last 4 weeks?")
    Q26EA = (476, "Q26E  FIRST voluntary group - Number of DAYS spent helping last time helped")
    Q26EB = (477, "Q26E  SECOND voluntary group - Number of DAYS spent helping last time helped")
    Q26EC = (478, "Q26E  THIRD voluntary group - Number of DAYS spent helping last time helped")
    Q26ED = (479, "Q26E  FOURTH voluntary group - Number of DAYS spent helping last time helped")
    Q26EE = (480, "Q26E  FIFTH voluntary group - Number of DAYS spent helping last time helped")
    Q26EF = (481, "Q26E  SIXTH voluntary group - Number of HOURS spent helping last time helped")
    Q26HA = (482, "Q26E  FIRST voluntary group - Number of HOURS spent helping last time helped")
    Q26HB = (483, "Q26E  SECOND voluntary group - Number of HOURS spent helping last time helped")
    Q26HC = (484, "Q26E  THIRD voluntary group - Number of HOURS spent helping last time helped")
    Q26HD = (485, "Q26E  FOURTH voluntary group - Number of HOURS spent helping last time helped")
    Q26HE = (486, "Q26E  FIFTH voluntary group - Number of HOURS spent helping last time helped")
    Q26HF = (487, "Q26HF HOURS WORKED AS A VOLUNTEER")
    Q26MA = (488, "Q26E  FIRST voluntary group - Number of MINUTES spent helping last time helped")
    Q26MB = (489, "Q26E  SECOND voluntary group - Number of MINUTES spent helping last time helped")
    Q26MC = (490, "Q26E  THIRD voluntary group - Number of MINUTES spent helping last time helped")
    Q26MD = (491, "Q26E  FOURTH voluntary group - Number of MINUTES spent helping last time helped")
    Q26ME = (492, "Q26E  FIFTH voluntary group - Number of MINUTES spent helping last time helped")
    Q26MF = (493, "Q26E  SIXTH voluntary group - Number of MINUTES spent helping last time helped")
    Q27A = (494, "Q27a   Have you helped someone who is not a member of your household in the last 4 weeks?")
    Q27B1 = (495, "Q27b   FIRST person helped")
    Q27B2 = (496, "Q26b   SECOND person helped")
    Q27B3 = (497, "Q26b   THIRD person helped")
    Q27B4 = (498, "Q26b   FOURTH person helped")
    Q27B5 = (499, "Q26b   FIFTH  person helped")
    Q27B6 = (500, "Q26b   SIXTH  person helped")
    Q27B7 = (501, "Q26b   SEVENTH  person helped")
    Q27B8 = (502, "Q26b   EIGHTH  person helped")
    ATQ27CA1 = (503, "Q27c   FIRST person helped - type of help - SLEEP?")
    ATQ27CA2 = (504, "Q27c   FIRST person helped - type of help - EATING?")
    ATQ27CA3 = (505, "Q27c   FIRST person helped - type of help - OTHER PERSONAL CARE?")
    ATQ27CA4 = (506, "Q27c   FIRST person helped - type of help - MAIN JOB?")
    ATQ27CA5 = (507, "Q27c   FIRST person helped - type of help - SECOND JOB?")
    ATQ27CA6 = (508, "Q27c   FIRST person helped - type of help - ACTIVITIES RELATED TO EMPLOYMENT?")
    ATQ27CA7 = (509, "Q27c   FIRST person helped - type of help - SCHOOL OR UNIVERSITY?")
    ATQ27CA8 = (510, "Q27c   FIRST person helped - type of help - FREE TIME STUDY?")
    ATQ27CA9 = (511, "Q27c   FIRST person helped - type of help - FOOD MANAGEMENT?")
    ATQ27CA10 = (512, "Q27c   FIRST person helped - type of help - HOUSEHOLD UPKEEP?")
    ATQ27CA11 = (513, "Q27c   FIRST person helped - type of help - MAKING & CARE FOR TEXTILES?")
    ATQ27CA12 = (514, "Q27c   FIRST person helped - type of help - GARDENING & PET CARE?")
    ATQ27CA13 = (515, "Q27c   FIRST person helped - type of help - CONSTRUCTION & REPAIR?")
    ATQ27CA14 = (516, "Q27c   FIRST person helped - type of help - SHOPPING & SERVICES?")
    ATQ27CA15 = (517, "Q27c   FIRST person helped - type of help - HOUSEHOLD MANAGEMENT?")
    ATQ27CA16 = (518, "Q27c   FIRST person helped - type of help - CHILDCARE (OWN HHLD MEMBERS)?")
    ATQ27CA17 = (519, "Q27c   FIRST person helped - type of help - HELP TO AN ADULT FAMILY MEMBER?")
    ATQ27CA18 = (520, "Q27c   FIRST person helped - type of help - ORGANISATIONAL WORK?")
    ATQ27CA19 = (521, "Q27c   FIRST person helped - type of help - INFORMAL HELP TO OTHER HOUSEHOLDS?")
    ATQ27CA20 = (522, "Q27c   FIRST person helped - type of help - PARTICIPATORY ACTIVITIES?")
    ATQ27CA21 = (523, "Q27c   FIRST person helped - type of help - SOCIAL LIFE?")
    ATQ27CA22 = (524, "Q27c   FIRST person helped - type of help - ENTERTAINMENT & CULTURE?")
    ATQ27CA23 = (525, "Q27c   FIRST person helped - type of help - RESTING/ TIME OUT?")
    ATQ27CA24 = (526, "Q27c   FIRST person helped - type of help - PHYSICAL EXERCISE?")
    ATQ27CA25 = (527, "Q27c   FIRST person helped - type of help - PRODUCTIVE EXERCISE?")
    ATQ27CA26 = (528, "Q27c   FIRST person helped - type of help - SPORTS RELATED ACTIVITIES?")
    ATQ27CA27 = (529, "Q27c   FIRST person helped - type of help - ARTS?")
    ATQ27CA28 = (530, "Q27c   FIRST person helped - type of help - HOBBIES?")
    ATQ27CA29 = (531, "Q27c   FIRST person helped - type of help - GAMES?")
    ATQ27CA30 = (532, "Q27c   FIRST person helped - type of help - READING?")
    ATQ27CA31 = (533, "Q27c   FIRST person helped - type of help - TV/ VIDEO?")
    ATQ27CA32 = (534, "Q27c   FIRST person helped - type of help - RADIO & MUSIC?")
    ATQ27CA33 = (535, "Q27c   FIRST person helped - type of help - TRAVEL?")
    ATQ27CA34 = (536, "Q27c   FIRST person helped - type of help - OTHER?")
    ATQ27CA35 = (537, "Q27c   FIRST person helped - type of help - DON'T KNOW/ NONE?")
    ATQ27CA36 = (538, "Q27c   FIRST person helped - type of help - NO ANSWER?")
    ATQ27CB1 = (539, "Q27c   SECOND person helped - type of help - SLEEP?")
    ATQ27CB2 = (540, "Q27c   SECOND person helped - type of help - EATING?")
    ATQ27CB3 = (541, "Q27c   SECOND person helped - type of help - OTHER PERSONAL CARE?")
    ATQ27CB4 = (542, "Q27c   SECOND person helped - type of help - MAIN JOB?")
    ATQ27CB5 = (543, "Q27c   SECOND person helped - type of help - SECOND JOB?")
    ATQ27CB6 = (544, "Q27c   SECOND person helped - type of help - ACTIVITIES RELATED TO EMPLOYMENT?")
    ATQ27CB7 = (545, "Q27c   SECOND person helped - type of help - SCHOOL OR UNIVERSITY?")
    ATQ27CB8 = (546, "Q27c   SECOND person helped - type of help - FREE TIME STUDY?")
    ATQ27CB9 = (547, "Q27c   SECOND person helped - type of help - FOOD MANAGEMENT?")
    ATQ27CB10 = (548, "Q27c   SECOND person helped - type of help - HOUSEHOLD UPKEEP?")
    ATQ27CB11 = (549, "Q27c   SECOND person helped - type of help - MAKING & CARE FOR TEXTILES?")
    ATQ27CB12 = (550, "Q27c   SECOND person helped - type of help - GARDENING & PET CARE?")
    ATQ27CB13 = (551, "Q27c   SECOND person helped - type of help - CONSTRUCTION & REPAIR?")
    ATQ27CB14 = (552, "Q27c   SECOND person helped - type of help - SHOPPING & SERVICES?")
    ATQ27CB15 = (553, "Q27c   SECOND person helped - type of help - HOUSEHOLD MANAGEMENT?")
    ATQ27CB16 = (554, "Q27c   SECOND person helped - type of help - CHILDCARE (OWN HHLD MEMBERS)?")
    ATQ27CB17 = (555, "Q27c   SECOND person helped - type of help - HELP TO AN ADULT FAMILY MEMBER?")
    ATQ27CB18 = (556, "Q27c   SECOND person helped - type of help - ORGANISATIONAL WORK?")
    ATQ27CB19 = (557, "Q27c   SECOND person helped - type of help - INFORMAL HELP TO OTHER HOUSEHOLDS?")
    ATQ27CB20 = (558, "Q27c   SECOND person helped - type of help - PARTICIPATORY ACTIVITIES?")
    ATQ27CB21 = (559, "Q27c   SECOND person helped - type of help - SOCIAL LIFE?")
    ATQ27CB22 = (560, "Q27c   SECOND person helped - type of help - ENTERTAINMENT & CULTURE?")
    ATQ27CB23 = (561, "Q27c   SECOND person helped - type of help - RESTING/ TIME OUT?")
    ATQ27CB24 = (562, "Q27c   SECOND person helped - type of help - PHYSICAL EXERCISE?")
    ATQ27CB25 = (563, "Q27c   SECOND person helped - type of help - PRODUCTIVE EXERCISE?")
    ATQ27CB26 = (564, "Q27c   SECOND person helped - type of help - SPORTS RELATED ACTIVITIES?")
    ATQ27CB27 = (565, "Q27c   SECOND person helped - type of help - ARTS?")
    ATQ27CB28 = (566, "Q27c   SECOND person helped - type of help - HOBBIES?")
    ATQ27CB29 = (567, "Q27c   SECOND person helped - type of help - GAMES?")
    ATQ27CB30 = (568, "Q27c   SECOND person helped - type of help - READING?")
    ATQ27CB31 = (569, "Q27c   SECOND person helped - type of help - TV/ VIDEO?")
    ATQ27CB32 = (570, "Q27c   SECOND person helped - type of help - RADIO & MUSIC?")
    ATQ27CB33 = (571, "Q27c   SECOND person helped - type of help - TRAVEL?")
    ATQ27CB34 = (572, "Q27c   SECOND person helped - type of help - OTHER?")
    ATQ27CB35 = (573, "Q27c   SECOND person helped - type of help - DON'T KNOW/ NONE?")
    ATQ27CB36 = (574, "Q27c   SECOND person helped - type of help - NO ANSWER?")
    ATQ27CC1 = (575, "Q27c   THIRD person helped - type of help - SLEEP?")
    ATQ27CC2 = (576, "Q27c   THIRD person helped - type of help - EATING?")
    ATQ27CC3 = (577, "Q27c   THIRD person helped - type of help - OTHER PERSONAL CARE?")
    ATQ27CC4 = (578, "Q27c   THIRD person helped - type of help - MAIN JOB?")
    ATQ27CC5 = (579, "Q27c   THIRD person helped - type of help - SECOND JOB?")
    ATQ27CC6 = (580, "Q27c   THIRD person helped - type of help - ACTIVITIES RELATED TO EMPLOYMENT?")
    ATQ27CC7 = (581, "Q27c   THIRD person helped - type of help - SCHOOL OR UNIVERSITY?")
    ATQ27CC8 = (582, "Q27c   THIRD person helped - type of help - FREE TIME STUDY?")
    ATQ27CC9 = (583, "Q27c   THIRD person helped - type of help - FOOD MANAGEMENT?")
    ATQ27CC10 = (584, "Q27c   THIRD person helped - type of help - HOUSEHOLD UPKEEP?")
    ATQ27CC11 = (585, "Q27c   THIRD person helped - type of help - MAKING & CARE FOR TEXTILES?")
    ATQ27CC12 = (586, "Q27c   THIRD person helped - type of help - GARDENING & PET CARE?")
    ATQ27CC13 = (587, "Q27c   THIRD person helped - type of help - CONSTRUCTION & REPAIR?")
    ATQ27CC14 = (588, "Q27c   THIRD person helped - type of help - SHOPPING & SERVICES?")
    ATQ27CC15 = (589, "Q27c   THIRD person helped - type of help - HOUSEHOLD MANAGEMENT?")
    ATQ27CC16 = (590, "Q27c   THIRD person helped - type of help - CHILDCARE (OWN HHLD MEMBERS)?")
    ATQ27CC17 = (591, "Q27c   THIRD person helped - type of help - HELP TO AN ADULT FAMILY MEMBER?")
    ATQ27CC18 = (592, "Q27c   THIRD person helped - type of help - ORGANISATIONAL WORK?")
    ATQ27CC19 = (593, "Q27c   THIRD person helped - type of help - INFORMAL HELP TO OTHER HOUSEHOLDS?")
    ATQ27CC20 = (594, "Q27c   THIRD person helped - type of help - PARTICIPATORY ACTIVITIES?")
    ATQ27CC21 = (595, "Q27c   THIRD person helped - type of help - SOCIAL LIFE?")
    ATQ27CC22 = (596, "Q27c   THIRD person helped - type of help - ENTERTAINMENT & CULTURE?")
    ATQ27CC23 = (597, "Q27c   THIRD person helped - type of help - RESTING/ TIME OUT?")
    ATQ27CC24 = (598, "Q27c   THIRD person helped - type of help - PHYSICAL EXERCISE?")
    ATQ27CC25 = (599, "Q27c   THIRD person helped - type of help - PRODUCTIVE EXERCISE?")
    ATQ27CC26 = (600, "Q27c   THIRD person helped - type of help - SPORTS RELATED ACTIVITIES?")
    ATQ27CC27 = (601, "Q27c   THIRD person helped - type of help - ARTS?")
    ATQ27CC28 = (602, "Q27c   THIRD person helped - type of help - HOBBIES?")
    ATQ27CC29 = (603, "Q27c   THIRD person helped - type of help - GAMES?")
    ATQ27CC30 = (604, "Q27c   THIRD person helped - type of help - READING?")
    ATQ27CC31 = (605, "Q27c   THIRD person helped - type of help - TV/ VIDEO?")
    ATQ27CC32 = (606, "Q27c   THIRD person helped - type of help - RADIO & MUSIC?")
    ATQ27CC33 = (607, "Q27c   THIRD person helped - type of help - TRAVEL?")
    ATQ27CC34 = (608, "Q27c   THIRD person helped - type of help - OTHER?")
    ATQ27CC35 = (609, "Q27c   THIRD person helped - type of help - DON'T KNOW/ NONE?")
    ATQ27CC36 = (610, "Q27c   THIRD person helped - type of help - NO ANSWER?")
    ATQ27CD1 = (611, "Q27c   FOURTH person helped - type of help - SLEEP?")
    ATQ27CD2 = (612, "Q27c   FOURTH person helped - type of help - EATING?")
    ATQ27CD3 = (613, "Q27c   FOURTH person helped - type of help - OTHER PERSONAL CARE?")
    ATQ27CD4 = (614, "Q27c   FOURTH person helped - type of help - MAIN JOB?")
    ATQ27CD5 = (615, "Q27c   FOURTH person helped - type of help - SECOND JOB?")
    ATQ27CD6 = (616, "Q27c   FOURTH person helped - type of help - ACTIVITIES RELATED TO EMPLOYMENT?")
    ATQ27CD7 = (617, "Q27c   FOURTH person helped - type of help - SCHOOL OR UNIVERSITY?")
    ATQ27CD8 = (618, "Q27c   FOURTH person helped - type of help - FREE TIME STUDY?")
    ATQ27CD9 = (619, "Q27c   FOURTH person helped - type of help - FOOD MANAGEMENT?")
    ATQ27CD10 = (620, "Q27c   FOURTH person helped - type of help - HOUSEHOLD UPKEEP?")
    ATQ27CD11 = (621, "Q27c   FOURTH person helped - type of help - MAKING & CARE FOR TEXTILES?")
    ATQ27CD12 = (622, "Q27c   FOURTH person helped - type of help - GARDENING & PET CARE?")
    ATQ27CD13 = (623, "Q27c   FOURTH person helped - type of help - CONSTRUCTION & REPAIR?")
    ATQ27CD14 = (624, "Q27c   FOURTH person helped - type of help - SHOPPING & SERVICES?")
    ATQ27CD15 = (625, "Q27c   FOURTH person helped - type of help - HOUSEHOLD MANAGEMENT?")
    ATQ27CD16 = (626, "Q27c   FOURTH person helped - type of help - CHILDCARE (OWN HHLD MEMBERS)?")
    ATQ27CD17 = (627, "Q27c   FOURTH person helped - type of help - HELP TO AN ADULT FAMILY MEMBER?")
    ATQ27CD18 = (628, "Q27c   FOURTH person helped - type of help - ORGANISATIONAL WORK?")
    ATQ27CD19 = (629, "Q27c   FOURTH person helped - type of help - INFORMAL HELP TO OTHER HOUSEHOLDS?")
    ATQ27CD20 = (630, "Q27c   FOURTH person helped - type of help - PARTICIPATORY ACTIVITIES?")
    ATQ27CD21 = (631, "Q27c   FOURTH person helped - type of help - SOCIAL LIFE?")
    ATQ27CD22 = (632, "Q27c   FOURTH person helped - type of help - ENTERTAINMENT & CULTURE?")
    ATQ27CD23 = (633, "Q27c   FOURTH person helped - type of help - RESTING/ TIME OUT?")
    ATQ27CD24 = (634, "Q27c   FOURTH person helped - type of help - PHYSICAL EXERCISE?")
    ATQ27CD25 = (635, "Q27c   FOURTH person helped - type of help - PRODUCTIVE EXERCISE?")
    ATQ27CD26 = (636, "Q27c   FOURTH person helped - type of help - SPORTS RELATED ACTIVITIES?")
    ATQ27CD27 = (637, "Q27c   FOURTH person helped - type of help - ARTS?")
    ATQ27CD28 = (638, "Q27c   FOURTH person helped - type of help - HOBBIES?")
    ATQ27CD29 = (639, "Q27c   FOURTH person helped - type of help - GAMES?")
    ATQ27CD30 = (640, "Q27c   FOURTH person helped - type of help - READING?")
    ATQ27CD31 = (641, "Q27c   FOURTH person helped - type of help - TV/ VIDEO?")
    ATQ27CD32 = (642, "Q27c   FOURTH person helped - type of help - RADIO & MUSIC?")
    ATQ27CD33 = (643, "Q27c   FOURTH person helped - type of help - TRAVEL?")
    ATQ27CD34 = (644, "Q27c   FOURTH person helped - type of help - OTHER?")
    ATQ27CD35 = (645, "Q27c   FOURTH person helped - type of help - DON'T KNOW/ NONE?")
    ATQ27CD36 = (646, "Q27c   FOURTH person helped - type of help - NO ANSWER?")
    ATQ27CE1 = (647, "Q27c   FIFTH person helped - type of help - SLEEP?")
    ATQ27CE2 = (648, "Q27c   FIFTH person helped - type of help - EATING?")
    ATQ27CE3 = (649, "Q27c   FIFTH person helped - type of help - OTHER PERSONAL CARE?")
    ATQ27CE4 = (650, "Q27c   FIFTH person helped - type of help - MAIN JOB?")
    ATQ27CE5 = (651, "Q27c   FIFTH person helped - type of help - SECOND JOB?")
    ATQ27CE6 = (652, "Q27c   FIFTH person helped - type of help - ACTIVITIES RELATED TO EMPLOYMENT?")
    ATQ27CE7 = (653, "Q27c   FIFTH person helped - type of help - SCHOOL OR UNIVERSITY?")
    ATQ27CE8 = (654, "Q27c   FIFTH person helped - type of help - FREE TIME STUDY?")
    ATQ27CE9 = (655, "Q27c   FIFTH person helped - type of help - FOOD MANAGEMENT?")
    ATQ27CE10 = (656, "Q27c   FIFTH person helped - type of help - HOUSEHOLD UPKEEP?")
    ATQ27CE11 = (657, "Q27c   FIFTH person helped - type of help - MAKING & CARE FOR TEXTILES?")
    ATQ27CE12 = (658, "Q27c   FIFTH person helped - type of help - GARDENING & PET CARE?")
    ATQ27CE13 = (659, "Q27c   FIFTH person helped - type of help - CONSTRUCTION & REPAIR?")
    ATQ27CE14 = (660, "Q27c   FIFTH person helped - type of help - SHOPPING & SERVICES?")
    ATQ27CE15 = (661, "Q27c   FIFTH person helped - type of help - HOUSEHOLD MANAGEMENT?")
    ATQ27CE16 = (662, "Q27c   FIFTH person helped - type of help - CHILDCARE (OWN HHLD MEMBERS)?")
    ATQ27CE17 = (663, "Q27c   FIFTH person helped - type of help - HELP TO AN ADULT FAMILY MEMBER?")
    ATQ27CE18 = (664, "Q27c   FIFTH person helped - type of help - ORGANISATIONAL WORK?")
    ATQ27CE19 = (665, "Q27c   FIFTH person helped - type of help - INFORMAL HELP TO OTHER HOUSEHOLDS?")
    ATQ27CE20 = (666, "Q27c   FIFTH person helped - type of help - PARTICIPATORY ACTIVITIES?")
    ATQ27CE21 = (667, "Q27c   FIFTH person helped - type of help - SOCIAL LIFE?")
    ATQ27CE22 = (668, "Q27c   FIFTH person helped - type of help - ENTERTAINMENT & CULTURE?")
    ATQ27CE23 = (669, "Q27c   FIFTH person helped - type of help - RESTING/ TIME OUT?")
    ATQ27CE24 = (670, "Q27c   FIFTH person helped - type of help - PHYSICAL EXERCISE?")
    ATQ27CE25 = (671, "Q27c   FIFTH person helped - type of help - PRODUCTIVE EXERCISE?")
    ATQ27CE26 = (672, "Q27c   FIFTH person helped - type of help - SPORTS RELATED ACTIVITIES?")
    ATQ27CE27 = (673, "Q27c   FIFTH person helped - type of help - ARTS?")
    ATQ27CE28 = (674, "Q27c   FIFTH person helped - type of help - HOBBIES?")
    ATQ27CE29 = (675, "Q27c   FIFTH person helped - type of help - GAMES?")
    ATQ27CE30 = (676, "Q27c   FIFTH person helped - type of help - READING?")
    ATQ27CE31 = (677, "Q27c   FIFTH person helped - type of help - TV/ VIDEO?")
    ATQ27CE32 = (678, "Q27c   FIFTH person helped - type of help - RADIO & MUSIC?")
    ATQ27CE33 = (679, "Q27c   FIFTH person helped - type of help - TRAVEL?")
    ATQ27CE34 = (680, "Q27c   FIFTH person helped - type of help - OTHER?")
    ATQ27CE35 = (681, "Q27c   FIFTH person helped - type of help - DON'T KNOW/ NONE?")
    ATQ27CE36 = (682, "Q27c   FIFTH person helped - type of help - NO ANSWER?")
    ATQ27CF1 = (683, "Q27c   SIXTH person helped - type of help - SLEEP?")
    ATQ27CF2 = (684, "Q27c   SIXTH person helped - type of help - EATING?")
    ATQ27CF3 = (685, "Q27c   SIXTH person helped - type of help - OTHER PERSONAL CARE?")
    ATQ27CF4 = (686, "Q27c   SIXTH person helped - type of help - MAIN JOB?")
    ATQ27CF5 = (687, "Q27c   SIXTH person helped - type of help - SECOND JOB?")
    ATQ27CF6 = (688, "Q27c   SIXTH person helped - type of help - ACTIVITIES RELATED TO EMPLOYMENT?")
    ATQ27CF7 = (689, "Q27c   SIXTH person helped - type of help - SCHOOL OR UNIVERSITY?")
    ATQ27CF8 = (690, "Q27c   SIXTH person helped - type of help - FREE TIME STUDY?")
    ATQ27CF9 = (691, "Q27c   SIXTH person helped - type of help - FOOD MANAGEMENT?")
    ATQ27CF10 = (692, "Q27c   SIXTH person helped - type of help - HOUSEHOLD UPKEEP?")
    ATQ27CF11 = (693, "Q27c   SIXTH person helped - type of help - MAKING & CARE FOR TEXTILES?")
    ATQ27CF12 = (694, "Q27c   SIXTH person helped - type of help - GARDENING & PET CARE?")
    ATQ27CF13 = (695, "Q27c   SIXTH person helped - type of help - CONSTRUCTION & REPAIR?")
    ATQ27CF14 = (696, "Q27c   SIXTH person helped - type of help - SHOPPING & SERVICES?")
    ATQ27CF15 = (697, "Q27c   SIXTH person helped - type of help - HOUSEHOLD MANAGEMENT?")
    ATQ27CF16 = (698, "Q27c   SIXTH person helped - type of help - CHILDCARE (OWN HHLD MEMBERS)?")
    ATQ27CF17 = (699, "Q27c   SIXTH person helped - type of help - HELP TO AN ADULT FAMILY MEMBER?")
    ATQ27CF18 = (700, "Q27c   SIXTH person helped - type of help - ORGANISATIONAL WORK?")
    ATQ27CF19 = (701, "Q27c   SIXTH person helped - type of help - INFORMAL HELP TO OTHER HOUSEHOLDS?")
    ATQ27CF20 = (702, "Q27c   SIXTH person helped - type of help - PARTICIPATORY ACTIVITIES?")
    ATQ27CF21 = (703, "Q27c   SIXTH person helped - type of help - SOCIAL LIFE?")
    ATQ27CF22 = (704, "Q27c   SIXTH person helped - type of help - ENTERTAINMENT & CULTURE?")
    ATQ27CF23 = (705, "Q27c   SIXTH person helped - type of help - RESTING/ TIME OUT?")
    ATQ27CF24 = (706, "Q27c   SIXTH person helped - type of help - PHYSICAL EXERCISE?")
    ATQ27CF25 = (707, "Q27c   SIXTH person helped - type of help - PRODUCTIVE EXERCISE?")
    ATQ27CF26 = (708, "Q27c   SIXTH person helped - type of help - SPORTS RELATED ACTIVITIES?")
    ATQ27CF27 = (709, "Q27c   SIXTH person helped - type of help - ARTS?")
    ATQ27CF28 = (710, "Q27c   SIXTH person helped - type of help - HOBBIES?")
    ATQ27CF29 = (711, "Q27c   SIXTH person helped - type of help - GAMES?")
    ATQ27CF30 = (712, "Q27c   SIXTH person helped - type of help - READING?")
    ATQ27CF31 = (713, "Q27c   SIXTH person helped - type of help - TV/ VIDEO?")
    ATQ27CF32 = (714, "Q27c   SIXTH person helped - type of help - RADIO & MUSIC?")
    ATQ27CF33 = (715, "Q27c   SIXTH person helped - type of help - TRAVEL?")
    ATQ27CF34 = (716, "Q27c   SIXTH person helped - type of help - OTHER?")
    ATQ27CF35 = (717, "Q27c   SIXTH person helped - type of help - DON'T KNOW/ NONE?")
    ATQ27CF36 = (718, "Q27c   SIXTH person helped - type of help - NO ANSWER?")
    ATQ27CG1 = (719, "Q27c   SEVENTH person helped - type of help - SLEEP?")
    ATQ27CG2 = (720, "Q27c   SEVENTH person helped - type of help - EATING?")
    ATQ27CG3 = (721, "Q27c   SEVENTH person helped - type of help - OTHER PERSONAL CARE?")
    ATQ27CG4 = (722, "Q27c   SEVENTH person helped - type of help - MAIN JOB?")
    ATQ27CG5 = (723, "Q27c   SEVENTH person helped - type of help - SECOND JOB?")
    ATQ27CG6 = (724, "Q27c   SEVENTH person helped - type of help - ACTIVITIES RELATED TO EMPLOYMENT?")
    ATQ27CG7 = (725, "Q27c   SEVENTH person helped - type of help - SCHOOL OR UNIVERSITY?")
    ATQ27CG8 = (726, "Q27c   SEVENTH person helped - type of help - FREE TIME STUDY?")
    ATQ27CG9 = (727, "Q27c   SEVENTH person helped - type of help - FOOD MANAGEMENT?")
    ATQ27CG10 = (728, "Q27c   SEVENTH person helped - type of help - HOUSEHOLD UPKEEP?")
    ATQ27CG11 = (729, "Q27c   SEVENTH person helped - type of help - MAKING & CARE FOR TEXTILES?")
    ATQ27CG12 = (730, "Q27c   SEVENTH person helped - type of help - GARDENING & PET CARE?")
    ATQ27CG13 = (731, "Q27c   SEVENTH person helped - type of help - CONSTRUCTION & REPAIR?")
    ATQ27CG14 = (732, "Q27c   SEVENTH person helped - type of help - SHOPPING & SERVICES?")
    ATQ27CG15 = (733, "Q27c   SEVENTH person helped - type of help - HOUSEHOLD MANAGEMENT?")
    ATQ27CG16 = (734, "Q27c   SEVENTH person helped - type of help - CHILDCARE (OWN HHLD MEMBERS)?")
    ATQ27CG17 = (735, "Q27c   SEVENTH person helped - type of help - HELP TO AN ADULT FAMILY MEMBER?")
    ATQ27CG18 = (736, "Q27c   SEVENTH person helped - type of help - ORGANISATIONAL WORK?")
    ATQ27CG19 = (737, "Q27c   SEVENTH person helped - type of help - INFORMAL HELP TO OTHER HOUSEHOLDS?")
    ATQ27CG20 = (738, "Q27c   SEVENTH person helped - type of help - PARTICIPATORY ACTIVITIES?")
    ATQ27CG21 = (739, "Q27c   SEVENTH person helped - type of help - SOCIAL LIFE?")
    ATQ27CG22 = (740, "Q27c   SEVENTH person helped - type of help - ENTERTAINMENT & CULTURE?")
    ATQ27CG23 = (741, "Q27c   SEVENTH person helped - type of help - RESTING/ TIME OUT?")
    ATQ27CG24 = (742, "Q27c   SEVENTH person helped - type of help - PHYSICAL EXERCISE?")
    ATQ27CG25 = (743, "Q27c   SEVENTH person helped - type of help - PRODUCTIVE EXERCISE?")
    ATQ27CG26 = (744, "Q27c   SEVENTH person helped - type of help - SPORTS RELATED ACTIVITIES?")
    ATQ27CG27 = (745, "Q27c   SEVENTH person helped - type of help - ARTS?")
    ATQ27CG28 = (746, "Q27c   SEVENTH person helped - type of help - HOBBIES?")
    ATQ27CG29 = (747, "Q27c   SEVENTH person helped - type of help - GAMES?")
    ATQ27CG30 = (748, "Q27c   SEVENTH person helped - type of help - READING?")
    ATQ27CG31 = (749, "Q27c   SEVENTH person helped - type of help - TV/ VIDEO?")
    ATQ27CG32 = (750, "Q27c   SEVENTH person helped - type of help - RADIO & MUSIC?")
    ATQ27CG33 = (751, "Q27c   SEVENTH person helped - type of help - TRAVEL?")
    ATQ27CG34 = (752, "Q27c   SEVENTH person helped - type of help - OTHER?")
    ATQ27CG35 = (753, "Q27c   SEVENTH person helped - type of help - DON'T KNOW/ NONE?")
    ATQ27CG36 = (754, "Q27c   SEVENTH person helped - type of help - NO ANSWER?")
    ATQ27CH1 = (755, "Q27c   EIGHTH person helped - type of help - SLEEP?")
    ATQ27CH2 = (756, "Q27c   EIGHTH person helped - type of help - EATING?")
    ATQ27CH3 = (757, "Q27c   EIGHTH person helped - type of help - OTHER PERSONAL CARE?")
    ATQ27CH4 = (758, "Q27c   EIGHTH person helped - type of help - MAIN JOB?")
    ATQ27CH5 = (759, "Q27c   EIGHTH person helped - type of help - SECOND JOB?")
    ATQ27CH6 = (760, "Q27c   EIGHTH person helped - type of help - ACTIVITIES RELATED TO EMPLOYMENT?")
    ATQ27CH7 = (761, "Q27c   EIGHTH person helped - type of help - SCHOOL OR UNIVERSITY?")
    ATQ27CH8 = (762, "Q27c   EIGHTH person helped - type of help - FREE TIME STUDY?")
    ATQ27CH9 = (763, "Q27c   EIGHTH person helped - type of help - FOOD MANAGEMENT?")
    ATQ27CH10 = (764, "Q27c   EIGHTH person helped - type of help - HOUSEHOLD UPKEEP?")
    ATQ27CH11 = (765, "Q27c   EIGHTH person helped - type of help - MAKING & CARE FOR TEXTILES?")
    ATQ27CH12 = (766, "Q27c   EIGHTH person helped - type of help - GARDENING & PET CARE?")
    ATQ27CH13 = (767, "Q27c   EIGHTH person helped - type of help - CONSTRUCTION & REPAIR?")
    ATQ27CH14 = (768, "Q27c   EIGHTH person helped - type of help - SHOPPING & SERVICES?")
    ATQ27CH15 = (769, "Q27c   EIGHTH person helped - type of help - HOUSEHOLD MANAGEMENT?")
    ATQ27CH16 = (770, "Q27c   EIGHTH person helped - type of help - CHILDCARE (OWN HHLD MEMBERS)?")
    ATQ27CH17 = (771, "Q27c   EIGHTH person helped - type of help - HELP TO AN ADULT FAMILY MEMBER?")
    ATQ27CH18 = (772, "Q27c   EIGHTH person helped - type of help - ORGANISATIONAL WORK?")
    ATQ27CH19 = (773, "Q27c   EIGHTH person helped - type of help - INFORMAL HELP TO OTHER HOUSEHOLDS?")
    ATQ27CH20 = (774, "Q27c   EIGHTH person helped - type of help - PARTICIPATORY ACTIVITIES?")
    ATQ27CH21 = (775, "Q27c   EIGHTH person helped - type of help - SOCIAL LIFE?")
    ATQ27CH22 = (776, "Q27c   EIGHTH person helped - type of help - ENTERTAINMENT & CULTURE?")
    ATQ27CH23 = (777, "Q27c   EIGHTH person helped - type of help - RESTING/ TIME OUT?")
    ATQ27CH24 = (778, "Q27c   EIGHTH person helped - type of help - PHYSICAL EXERCISE?")
    ATQ27CH25 = (779, "Q27c   EIGHTH person helped - type of help - PRODUCTIVE EXERCISE?")
    ATQ27CH26 = (780, "Q27c   EIGHTH person helped - type of help - SPORTS RELATED ACTIVITIES?")
    ATQ27CH27 = (781, "Q27c   EIGHTH person helped - type of help - ARTS?")
    ATQ27CH28 = (782, "Q27c   EIGHTH person helped - type of help - HOBBIES?")
    ATQ27CH29 = (783, "Q27c   EIGHTH person helped - type of help - GAMES?")
    ATQ27CH30 = (784, "Q27c   EIGHTH person helped - type of help - READING?")
    ATQ27CH31 = (785, "Q27c   EIGHTH person helped - type of help - TV/ VIDEO?")
    ATQ27CH32 = (786, "Q27c   EIGHTH person helped - type of help - RADIO & MUSIC?")
    ATQ27CH33 = (787, "Q27c   EIGHTH person helped - type of help - TRAVEL?")
    ATQ27CH34 = (788, "Q27c   EIGHTH person helped - type of help - OTHER?")
    ATQ27CH35 = (789, "Q27c   EIGHTH person helped - type of help - DON'T KNOW/ NONE?")
    ATQ27CH36 = (790, "Q27c   EIGHTH person helped - type of help - NO ANSWER?")
    Q27DA = (791, "Q27d   FIRST person helped - Number of times helped them in last 4 weeks?")
    Q27DB = (792, "Q27d   SECOND person helped - Number of times helped them in last 4 weeks?")
    Q27DC = (793, "Q27d   THIRD person helped - Number of times helped them in last 4 weeks?")
    Q27DD = (794, "Q27d   FOURTH person helped - Number of times helped them in last 4 weeks?")
    Q27DE = (795, "Q27d   FIFTH person helped - Number of times helped them in last 4 weeks?")
    Q27DF = (796, "Q27d   SIXTH person helped - Number of times helped them in last 4 weeks?")
    Q27DG = (797, "Q27d   SEVENTH person helped - Number of times helped them in last 4 weeks?")
    Q27DH = (798, "Q27d   EIGHTH person helped - Number of times helped them in last 4 weeks?")
    Q27EDA = (799, "Q27e   FIRST person helped - Number of DAYS spent helping them last time helped")
    Q27EDB = (800, "Q27e   SECOND person helped - Number of DAYS spent helping them last time helped")
    Q27EDC = (801, "Q27e   THIRD person helped - Number of DAYS spent helping them last time helped")
    Q27EDD = (802, "Q27e   FOURTH person helped - Number of DAYS spent helping them last time helped")
    Q27EDE = (803, "Q27e   FIFTH person helped - Number of DAYS spent helping them last time helped")
    Q27EDF = (804, "Q27e   SIXTH person helped - Number of DAYS spent helping them last time helped")
    Q27EDG = (805, "Q27e   SEVENTH person helped - Number of DAYS spent helping them last time helped")
    Q27EDH = (806, "Q27e   EIGHTH person helped - Number of DAYS spent helping them last time helped")
    Q27EHA = (807, "Q27e   FIRST person helped - Number of HOURS spent helping them last time helped")
    Q27EHB = (808, "Q27e   SECOND person helped - Number of HOURS spent helping them last time helped")
    Q27EHC = (809, "Q27e   THIRD person helped - Number of HOURS spent helping them last time helped")
    Q27EHD = (810, "Q27e   FOURTH person helped - Number of HOURS spent helping them last time helped")
    Q27EHE = (811, "Q27e   FIFTH person helped - Number of HOURS spent helpingv last time helped")
    Q27EHF = (812, "Q27e   SIXTH person helped - Number of HOURS spent helping them last time helped")
    Q27EHG = (813, "Q27e   SEVENTH person helped - Number of HOURS spent helping them last time helped")
    Q27EHH = (814, "Q27e   EIGHTH person helped - Number of HOURS spent helping them last time helped")
    Q27EMA = (815, "Q27e   FIRST person helped - Number of MINUTES spent helping them last time helped")
    Q27EMB = (816, "Q27e   SECOND person helped - Number of MINUTES spent helping them last time helped")
    Q27EMC = (817, "Q27e   THIRD person helped - Number of MINUTES spent helping them last time helped")
    Q27EMD = (818, "Q27e   FOURTH person helped - Number of MINUTES spent helping them last time helped")
    Q27EME = (819, "Q27e   FIFTH person helped - Number of MINUTES spent helping them last time helped")
    Q27EMF = (820, "Q27e   SIXTH person helped - Number of MINUTES spent helping them last time helped")
    Q27EMG = (821, "Q27e   SEVENTH person helped - Number of MINUTES spent helping them last time helped")
    Q27EMH = (822, "Q27e   EIGHTH person helped - Number of MINUTES spent helping them last time helped")
    Q27FA = (823, "Q27f   FIRST person helped - Were you paid for helping this person LAST TIME?")
    Q27FB = (824, "Q27f   SECOND person helped - Were you paid for helping this person LAST TIME?")
    Q27FC = (825, "Q27f   THIRD person helped - Were you paid for helping this person LAST TIME?")
    Q27FD = (826, "Q27f   FOURTH person helped - Were you paid for helping this person LAST TIME?")
    Q27FE = (827, "Q27f   FIFTH person helped - Were you paid for helping this person LAST TIME?")
    Q27FF = (828, "Q27f   SIXTH person helped - Were you paid for helping this person LAST TIME?")
    Q27FG = (829, "Q27f   SEVENTH person helped - Were you paid for helping this person LAST TIME?")
    Q27FH = (830, "Q27f   EIGHTH person helped - Were you paid for helping this person LAST TIME?")
    Q28A = (831, "Q28   Adults (16yrs or over) only asked:  Attitude towards...COOKING A MEAL")
    Q28B = (832, "Q28   Adults (16yrs or over) only asked:  Attitude towards...COOKING FOR A SPECIAL OCCASION")
    Q28C = (833, "Q28   Adults (16yrs or over) only asked:  Attitude towards...GARDENING")
    Q28D = (834, "Q28   Adults (16yrs or over) only asked:  Attitude towards...SHOPPING FOR FOOD")
    Q28E = (835, "Q28   Adults (16yrs or over) only asked:  Attitude towards...SHOPPING (NON-FOOD)")
    Q28F = (836, "Q28   Adults (16yrs or over) only asked:  Attitude towards...DECORATING")
    Q28G = (837, "Q28   Adults (16yrs or over) only asked:  Attitude towards...DIY REPAIR WORK")
    Q28H = (838, "Q28   Adults (16yrs or over) only asked:  Attitude towards...HELPING CHILDREN WITH HOMEWORK")
    Q28I = (839, "Q28   Adults (16yrs or over) only asked:  Attitude towards...TIDYINGTHE HOUSE")
    Q28J = (840, "Q28   Adults (16yrs or over) only asked:  Attitude towards...WASHING CLOTHES")
    Q28K = (841, "Q28   Adults (16yrs or over) only asked:  Attitude towards...IRONING CLOTHES")
    Q28L = (842, "Q28   Children (15yrs or less) only asked:  Attitude towards...(HELPING TO) COOK A MEAL")
    Q28M = (843, "Q28   Children (15yrs or less) only asked:  Attitude towards...WASHING UP")
    Q28N = (844, "Q28   Children (15yrs or less) only asked:  Attitude towards...HELPING IN THE GARDEN")
    Q28O = (845, "Q28   Children (15yrs or less) only asked:  Attitude towards...GOING TO THE SHOPS TO BUY FOOD")
    Q28P = (846, "Q28   Children (15yrs or less) only asked:  Attitude towards...TIDYING THE HOUSE/ YOUR ROOM")
    Q28Q = (847, "Q28   Children (15yrs or less) only asked:  Attitude towards...LOOKING AFTER YOUNGER BROTHERS OR SISTERS")
    Q29A = (848, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - THE CINEMA")
    Q29B = (849, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - THE MILLENNIUM DOME")
    Q29C = (850, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - ANY OTHER SPECIAL MILLENNIUM EVENT OR ACTIVITY")
    Q29D = (851, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - A SPORTS EVENT AS A SPECTATOR")
    Q29E = (852, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - A PLAY, MUSICAL OR PANTOMIME")
    Q29F = (853, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - THE OPERA")
    Q29G = (854, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - A CONCERT OR PERFORMANCE OF CLASSICAL MUSIC OF ANY KIND")
    Q29H = (855, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - ANY OTHER GIG OR OTHER LIVE MUSIC")
    Q29I = (856, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - THE BALLET OR TO MODERN/CONTEMPARY DANCE")
    Q29J = (857, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - A MUSEUM OR AN ART GALLERY")
    Q29K = (858, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - A HISTORIC HOUSE, CASTLE")
    Q29L = (859, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - A LIBRARY")
    Q29M = (860, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - EAT OR DRINK OUT AT A CAFE/PUB")
    Q29N = (861, "Q29   ACTIVITY DONE IN PAST 4 WEEKS - SHOPPING CENTRE OR MALL (NOT as part of regular food/ hhld shopping)?")
    Q29O = (862, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - A CAR-BOOT SALE, ANTIQUES FAIR OR SIMILAR")
    Q29P = (863, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - A THEME PARK, FAIRGROUND, FAIR OR CARNIVAL")
    Q29Q = (864, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - A ZOO,  WILDLIFE RESERVE, AQUARIUM, FARM-PARK")
    Q29R = (865, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - SOME OTHER PLACE OF ENTERTAINMENT")
    Q29S = (866, "Q29 ACTIVITY DONE IN THE PAST 4 WEEKS - ANY OTHER OUTDOOR TRIPS")
    Q30A = (867, "Q30 TIMES GOING TO THE CINEMA")
    Q30B = (868, "Q30 TIMES GOING TO THE MILLENNIUM DOME")
    Q30C = (869, "Q30 TIMES GOING TO ANY OTHER SPECIAL MILLENNIUM EVENT")
    Q30D = (870, "Q30 TIMES GOING TO A SPORTS EVENT AS A SPECTATOR")
    Q30E = (871, "Q30 TIMES GOING TO A PLAY, MUSICAL OR PANTOMIME")
    Q30F = (872, "Q30 TIMES GOING TO THE OPERA")
    Q30G = (873, "Q30 TIMES GOING TO A CONCERT OR PERFORMANCE")
    Q30H = (874, "Q30 TIMES GOING TO ANY OTHER GIG")
    Q30I = (875, "Q30 TIMES GOING TO THE BALLET OR TO MODERN DANCE")
    Q30J = (876, "Q30 TIMES GOING TO A MUSEUM OR AN ART GALLERY")
    Q30K = (877, "Q30 TIMES GOING TO A HISTORIC HOUSE, CASTLE")
    Q30L = (878, "Q30 TIMES GOING TO A LIBRARY")
    Q30M = (879, "Q30 TIMES GOING TO EAT OR DRINK OUT AT A CAFE")
    Q30N = (880, "Q30 TIMES GOING TO A SHOPPING CENTRE OR MALL")
    Q30O = (881, "Q30 TIMES GOING TO A CAR-BOOT SALE, ANTIQUES FAIR")
    Q30P = (882, "Q30 TIMES GOING TO A THEME PARK, FAIRGROUND")
    Q30Q = (883, "Q30 TIMES GOING TO A ZOO,  WILDLIFE RESERVE")
    Q30R = (884, "Q30 TIMES GOING TO SOME OTHER PLACE OF ENTERTAINMENT")
    Q30S = (885, "Q30 TIMES GOING ON ANY OTHER OUTDOOR TRIPS")
    Q31A01 = (886, "Q31   Sports/ physical activities took part in over last 4 weeks - SWIMMING OR DIVING INDOORS?")
    Q31A02 = (887, "Q31   Sports/ physical activities took part in over last 4 weeks - SWIMMING OR DIVING OUTDOORS?")
    Q31A03 = (888, "Q31   Sports/ physical activities took part in over last 4 weeks - CYCLING?")
    Q31A04 = (889, "Q31   Sports/ physical activities took part in over last 4 weeks - INDOOR BOWLS?")
    Q31A05 = (890, "Q31   Sports/ physical activities took part in over last 4 weeks - OUTDOOR (LAWN) BOWLS?")
    Q31A06 = (891, "Q31   Sports/ physical activities took part in over last 4 weeks - TENPIN BOWLING?")
    Q31A07 = (892, "Q31   Sports/ physical activities took part in over last 4 weeks - KEEPFIT, AEROBICS, YOGA, DANCE EXERCISE, EXERCISE BIKE ?")
    Q31A08 = (893, "Q31   Sports/ physical activities took part in over last 4 weeks - MARTIAL ARTS (INCL SELF-DEFENCE)?")
    Q31A09 = (894, "Q31   Sports/ physical activities took part in over last 4 weeks - WEIGHT TRAINING (INCL BODY BUILDING)?")
    Q31A10 = (895, "Q31   Sports/ physical activities took part in over last 4 weeks - WEIGHTLIFTING?")
    Q31A11 = (896, "Q31   Sports/ physical activities took part in over last 4 weeks - GYMNASTICS?")
    Q31A12 = (897, "Q31   Sports/ physical activities took part in over last 4 weeks - SNOOKER, POOL, BILLIARDS (EXCL BAR BILLIARS)?")
    Q31A13 = (898, "Q31   Sports/ physical activities took part in over last 4 weeks - DARTS?")
    Q31A14 = (899, "Q31   Sports/ physical activities took part in over last 4 weeks - RUGBY UNION OR LEAGUE?")
    Q31A15 = (900, "Q31   Sports/ physical activities took part in over last 4 weeks - AMERICAN FOOTBALL?")
    Q31A16 = (901, "Q31   Sports/ physical activities took part in over last 4 weeks - FOOTBALL INDOORS (INCL 5-A-SIDE)?")
    Q31A17 = (902, "Q31   Sports/ physical activities took part in over last 4 weeks - FOOTBALL OUTDOORS (INCL 5-A-SIDE)?")
    Q31A18 = (903, "Q31   Sports/ physical activities took part in over last 4 weeks - GAELIC SPORTS (EG GAELIC FOOTBALL, HURLING, CARNOGIE, SHINTY, IRISH HANDBALL)?")
    Q31A19 = (904, "Q31   Sports/ physical activities took part in over last 4 weeks - CRICKET?")
    Q31A20 = (905, "Q31   Sports/ physical activities took part in over last 4 weeks - HOCKEY (EXCL ICE, ROLLER OR STREET - SEE 'OTHER' BELOW)?")
    Q31A21 = (906, "Q31   Sports/ physical activities took part in over last 4 weeks - NETBALL?")
    Q31A22 = (907, "Q31   Sports/ physical activities took part in over last 4 weeks - TENNIS?")
    Q31A23 = (908, "Q31   Sports/ physical activities took part in over last 4 weeks - BADMINTON?")
    Q31A24 = (909, "Q31   Sports/ physical activities took part in over last 4 weeks - SQUASH?")
    Q31A25 = (910, "Q31   Sports/ physical activities took part in over last 4 weeks - BASKETBALL?")
    Q31A26 = (911, "Q31   Sports/ physical activities took part in over last 4 weeks - TABLE TENNIS?")
    Q31A27 = (912, "Q31   Sports/ physical activities took part in over last 4 weeks - TRACK OR FIELD ATHLETICS?")
    Q31A28 = (913, "Q31   Sports/ physical activities took part in over last 4 weeks - JOGGING, CROSS COUNTRY, ROAD RUNNING?")
    Q31A29 = (914, "Q31   Sports/ physical activities took part in over last 4 weeks - ANGLING/ FISHING?")
    Q31A30 = (915, "Q31   Sports/ physical activities took part in over last 4 weeks - YACHTING OT DINGHY SAILING?")
    Q31A31 = (916, "Q31   Sports/ physical activities took part in over last 4 weeks - CANOEING?")
    Q31A32 = (917, "Q31   Sports/ physical activities took part in over last 4 weeks - WINDSURFING/ BOARDSAILING?")
    Q31A33 = (918, "Q31   Sports/ physical activities took part in over last 4 weeks - ICE SKATING (EXCL ROLLER - SEE OTHER BELOW)?")
    Q31A34 = (919, "Q31   Sports/ physical activities took part in over last 4 weeks - CURLING?")
    Q31A35 = (920, "Q31   Sports/ physical activities took part in over last 4 weeks - GOLF, PITCH & PUTT, PUTTING, (EXCL CRAZY GOLF)?")
    Q31A36 = (921, "Q31   Sports/ physical activities took part in over last 4 weeks - SKIING (ON SNOW, ARTIFICIAL OR GRASS)?")
    Q31A37 = (922, "Q31   Sports/ physical activities took part in over last 4 weeks - HORSE RIDING (EXCL POLO - SEE OTHER BELOW)?")
    Q31A38 = (923, "Q31   Sports/ physical activities took part in over last 4 weeks - CLIMBING/ MOUNTAINEERING (INCL INDOORS)?")
    Q31A39 = (924, "Q31   Sports/ physical activities took part in over last 4 weeks - MOTOR SPORTS?")
    Q31A40 = (925, "Q31   Sports/ physical activities took part in over last 4 weeks - SHOOTING?")
    Q31A41 = (926, "Q31   Sports/ physical activities took part in over last 4 weeks - WALKING/ HIKING (RECREATIONAL) FOR 2 MILES OR MORE?")
    Q31A42 = (927, "Q31   Sports/ physical activities took part in over last 4 weeks - VOLLEYBALL?")
    Q31A43 = (928, "Q31   Sports/ physical activities took part in over last 4 weeks - OTHER?")
    Q31A44 = (929, "Q31   Sports/ physical activities took part in over last 4 weeks - NONE OF THESE?")
    Q31A45 = (930, "Q31   Sports/ physical activities took part in over last 4 weeks - DON'T KNOW?")
    Q31A46 = (931, "Q31   Sports/ physical activities took part in over last 4 weeks - REFUSED?")
    Q31C01 = (932, "Q31C NUMBER OF DAYS PLAYING SWIMMING OR DIVING INDOORS")
    Q31C02 = (933, "Q31C NUMBER OF DAYS PLAYING SWIMMING OR DIVING OUTDOORS")
    Q31C03 = (934, "Q31C NUMBER OF DAYS PLAYING CYCLING")
    Q31C04 = (935, "Q31C NUMBER OF DAYS PLAYING INDOOR BOWLS")
    Q31C05 = (936, "Q31C NUMBER OF DAYS PLAYING OUTDOOR (LAWN) BOWLS")
    Q31C06 = (937, "Q31C NUMBER OF DAYS PLAYING TENPIN BOWLING")
    Q31C07 = (938, "Q31C NUMBER OF DAYS PLAYING KEEPFIT, AEROBICS, YOGA, DANCE EXERCISE")
    Q31C08 = (939, "Q31C NUMBER OF DAYS PLAYING MARTIAL ARTS")
    Q31C09 = (940, "Q31C NUMBER OF DAYS PLAYING WEIGHT TRAINING")
    Q31C10 = (941, "Q31C NUMBER OF DAYS PLAYING WEIGHTLIFTING")
    Q31C11 = (942, "Q31C NUMBER OF DAYS PLAYING GYMNASTICS")
    Q31C12 = (943, "Q31C NUMBER OF DAYS PLAYING SNOOKER, POOL, BILLIARDS")
    Q31C13 = (944, "Q31C NUMBER OF DAYS PLAYING DARTS")
    Q31C14 = (945, "Q31C NUMBER OF DAYS PLAYING RUGBY UNION OR LEAGUE")
    Q31C15 = (946, "Q31C NUMBER OF DAYS PLAYING AMERICAN FOOTBALL")
    Q31C16 = (947, "Q31C NUMBER OF DAYS PLAYING FOOTBALL INDOORS")
    Q31C17 = (948, "Q31C NUMBER OF DAYS PLAYING FOOTBALL OUTDOORS")
    Q31C18 = (949, "Q31C NUMBER OF DAYS PLAYING GAELIC SPORTS")
    Q31C19 = (950, "Q31C NUMBER OF DAYS PLAYING CRICKET")
    Q31C20 = (951, "Q31C NUMBER OF DAYS PLAYING HOCKEY")
    Q31C21 = (952, "Q31C NUMBER OF DAYS PLAYING NETBALL")
    Q31C22 = (953, "Q31C NUMBER OF DAYS PLAYING TENNIS")
    Q31C23 = (954, "Q31C NUMBER OF DAYS PLAYING BADMINTON")
    Q31C24 = (955, "Q31C NUMBER OF DAYS PLAYING SQUASH")
    Q31C25 = (956, "Q31C NUMBER OF DAYS PLAYING BASKETBALL")
    Q31C26 = (957, "Q31C NUMBER OF DAYS PLAYING TABLE TENNIS")
    Q31C27 = (958, "Q31C NUMBER OF DAYS PLAYING TRACK AND FIELD ATHLETICS")
    Q31C28 = (959, "Q31C NUMBER OF DAYS PLAYING JOGGING,CROSS COUNTRY, ROAD RUNNING")
    Q31C29 = (960, "Q31C NUMBER OF DAYS PLAYING ANGLING/FISHING")
    Q31C30 = (961, "Q31C NUMBER OF DAYS PLAYING YACHTING OR DINGHY SAILING")
    Q31C31 = (962, "Q31C NUMBER OF DAYS PLAYING CANOEING")
    Q31C32 = (963, "Q31C NUMBER OF DAYS PLAYING WINDSURFING/BOARDSAILING")
    Q31C33 = (964, "Q31C NUMBER OF DAYS PLAYING ICE SKATING")
    Q31C34 = (965, "Q31C NUMBER OF DAYS PLAYING CURLING")
    Q31C35 = (966, "Q31C NUMBER OF DAYS PLAYING GOLF, PITCH AND PUTT, PUTTING")
    Q31C36 = (967, "Q31C NUMBER OF DAYS PLAYING SKIING")
    Q31C37 = (968, "Q31C NUMBER OF DAYS PLAYING HORSE RIDING")
    Q31C38 = (969, "Q31C NUMBER OF DAYS PLAYING CLIMBING/MOUNTAINEERING")
    Q31C39 = (970, "Q31C NUMBER OF DAYS PLAYING MOTOR SPORTS")
    Q31C40 = (971, "Q31C NUMBER OF DAYS PLAYING SHOOTING")
    Q31C41 = (972, "Q31C NUMBER OF DAYS PLAYING WALKING OR HIKING")
    Q31C42 = (973, "Q31C NUMBER OF DAYS PLAYING VOLLEYBALL")
    Q31C43 = (974, "Q31C NUMBER OF DAYS PLAYING OTHER")
    Q32A = (975, "Q32a  Have you (or someone else on your behalf) bought a lottery ticket/scratch card in the last 7 days?")
    Q32B = (976, "Q32b  Did you buy the lottery tickets/ scratch cards yourself ?")
    Q32C = (977, "Q32c  Were they purchased just for yourself or jointly with others?")
    Q32D = (978, "Q32d JOINTLY WITH OTHERS: Purchased jointly with other household members or with people outside your household?")
    Q33 = (979, "Q33  Do you have access to a car or van for transport?")
    Q34A = (980, "Q34a  How is your general health?")
    Q34B = (981, "Q34b  Have you CUT BACK on the things you do because of illness or injury?")
    Q34C = (982, "Q34c  How many DAYS cut back for (in the last 2 weeks)?")
    Q35A = (983, "Q35a  Any health problems/ disabilities that you expect will LAST FOR MORE THAN ONE YEAR?")
    Q35B = (984, "Q35b  Does this health problem affect the KIND OF PAID WORK that you might do?")
    Q35C = (985, "Q35c  Does this health problem affect the AMOUNT OF PAID WORK that you might do?")
    Q35D01 = (986, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - PROBLEMS WITH ARMS OR HANDS?")
    Q35D02 = (987, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - PROBLEMS WITH LEGS OR FEET?")
    Q35D03 = (988, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - PROBLEMS WITH BACK OR NECK?")
    Q35D04 = (989, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - DIFFICULTY IN SEEING (EVEN WITH GLASSES)?")
    Q35D05 = (990, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - DIFFICULTY IN HEARING?")
    Q35D06 = (991, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - A SPEECH IMPEDIMENT?")
    Q35D07 = (992, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - SEVERE DISFIGUREMENT, SKIN CONDITION, ALLERGIES?")
    Q35D08 = (993, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - CHEST OR BREATHING PROBLEMS, ASTHMA, BRONCHITIS?")
    Q35D09 = (994, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - HEART, BLOOD PRESSURE OR BLOOD CIRCULATION PROBLEMS?")
    Q35D10 = (995, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - STOMACH, LIVER, KIDNEY OR DIGESTIVE PROBLEMS?")
    Q35D11 = (996, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - DIABETES?")
    Q35D12 = (997, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - DEPRESSION, BAD NERVES OR ANXIETY?")
    Q35D13 = (998, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - EPILEPSY?")
    Q35D14 = (999, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - SEVERE OR SPECIFIC LEARNING DIFFICULTIES?")
    Q35D15 = (1000, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - MENTAL ILLNESS, PHOBIAS, PANICS OR OTHER NERVOUS DISORDERS?")
    Q35D16 = (1001, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - PROGRESSIVE ILLNESS (EG CANCER, MS, PARKINSONS, HIV, ...)?")
    Q35D17 = (1002, "Q35d (for 16yrs or over only): Type of health problems/ disabilities have - OTHER HEALTH PROBLEMS OR DISABILITIES?")
    ATQ35DC1 = (1003, "Q35d (for under 16s only): Type of health problems/ disabilities have - PROBLEMS WITH ARMS OR HANDS?")
    ATQ35DC2 = (1004, "Q35d (for under 16s only): Type of health problems/ disabilities have - PROBLEMS WITH LEGS OR FEET?")
    ATQ35DC3 = (1005, "Q35d (for under 16s only): Type of health problems/ disabilities have - PROBLEMS WITH BACK OR NECK?")
    ATQ35DC4 = (1006, "Q35d (for under 16s only): Type of health problems/ disabilities have - DIFFICULTY IN SEEING (EVEN WITH GLASSES)?")
    ATQ35DC5 = (1007, "Q35d (for under 16s only): Type of health problems/ disabilities have - DIFFICULTY IN HEARING?")
    ATQ35DC6 = (1008, "Q35d (for under 16s only): Type of health problems/ disabilities have - A SPEECH IMPEDIMENT?")
    ATQ35DC7 = (1009, "Q35d (for under 16s only): Type of health problems/ disabilities have - SEVERE DISFIGUREMENT, SKIN CONDITION, ALLERGIES?")
    ATQ35DC8 = (1010, "Q35d (for under 16s only): Type of health problems/ disabilities have - CHEST OR BREATHING PROBLEMS, ASTHMA, BRONCHITIS?")
    ATQ35DC9 = (1011, "Q35d (for under 16s only): Type of health problems/ disabilities have - HEART, BLOOD PRESSURE OR BLOOD CIRCULATION PROBLEMS?")
    ATQ35DC10 = (1012, "Q35d (for under 16s only): Type of health problems/ disabilities have - STOMACH, LIVER, KIDNEY OR DIGESTIVE PROBLEMS?")
    ATQ35DC11 = (1013, "Q35d (for under 16s only): Type of health problems/ disabilities have - DIABETES?")
    ATQ35DC12 = (1014, "Q35d (for under 16s only): Type of health problems/ disabilities have - DEPRESSION, BAD NERVES OR ANXIETY?")
    ATQ35DC13 = (1015, "Q35d (for under 16s only): Type of health problems/ disabilities have - EPILEPSY?")
    ATQ35DC14 = (1016, "Q35d (for under 16s only): Type of health problems/ disabilities have - SEVERE OR SPECIFIC LEARNING DIFFICULTIES?")
    ATQ35DC15 = (1017, "Q35d (for under 16s only): Type of health problems/ disabilities have - MENTAL ILLNESS, PHOBIAS, PANICS OR OTHER NERVOUS DISORDERS?")
    ATQ35DC16 = (1018, "Q35d (for under 16s only): Type of health problems/ disabilities have - PROGRESSIVE ILLNESS (EG CANCER, MS, PARKINSONS, HIV, ...)?")
    ATQ35DC17 = (1019, "Q35d (for under 16s only): Type of health problems/ disabilities have - OTHER HEALTH PROBLEMS OR DISABILITIES?")
    ATQ35DC18 = (1020, "Q35d (for under 16s only): Type of health problems/ disabilities have - UNUSED CODE")
    ATQ35DC19 = (1021, "Q35d (for under 16s only): Type of health problems/ disabilities have - DON'T KNOW?")
    ATQ35DC20 = (1022, "Q35d (for under 16s only): Type of health problems/ disabilities have - REFUSED?")
    ATQ35DC21 = (1023, "Q35d (for under 16s only): Type of health problems/ disabilities have - NOT ANSWERED?")
    Q35E = (1024, "Q35E MAIN HEALTH PROBLEM/DISABILITY?")
    Q35F = (1025, "Q35F DO ILLNESSES LIMIT ACTIONS?")
    Q36A = (1026, "Q36a: How rushed do you normally feel?")
    Q36B = (1027, "Q36b: What ONE activity would you spend more time on if you could?")
    Q38A = (1028, "Q38 PERSON 1 AT PRIMARY SCHOOL FULL TIME?")
    Q38B = (1029, "Q38 PERSON 2 AT PRIMARY SCHOOL FULL TIME?")
    Q38C = (1030, "Q38 PERSON 3 AT PRIMARY SCHOOL FULL TIME?")
    Q38D = (1031, "Q38 PERSON 4 AT PRIMARY SCHOOL FULL TIME?")
    Q38E = (1032, "Q38 PERSON 5 AT PRIMARY SCHOOL FULL TIME?")
    Q38F = (1033, "Q38 PERSON 6 AT PRIMARY SCHOOL FULL TIME?")
    Q38G = (1034, "Q38 PERSON 7 AT PRIMARY SCHOOL FULL TIME?")
    Q38H = (1035, "Q38 PERSON 8 AT PRIMARY SCHOOL FULL TIME?")
    Q38I = (1036, "Q38 PERSON 9 AT PRIMARY SCHOOL FULL TIME?")
    Q38J = (1037, "Q38 PERSON 10 AT PRIMARY SCHOOL FULL TIME?")
    Q38AA = (1038, "Q38A PERSON 1 TYPE OF PRIMARY SCHOOL")
    Q38AB = (1039, "Q38A PERSON 2 TYPE OF PRIMARY SCHOOL")
    Q38AC = (1040, "Q38A PERSON 3 TYPE OF PRIMARY SCHOOL")
    Q38AD = (1041, "Q38A PERSON 4 TYPE OF PRIMARY SCHOOL")
    Q38AE = (1042, "Q38A PERSON 5 TYPE OF PRIMARY SCHOOL")
    Q38AF = (1043, "Q38A PERSON 6 TYPE OF PRIMARY SCHOOL")
    Q38AG = (1044, "Q38A PERSON 7 TYPE OF PRIMARY SCHOOL")
    Q38AH = (1045, "Q38A PERSON 8 TYPE OF PRIMARY SCHOOL")
    Q38AI = (1046, "Q38A PERSON 9 TYPE OF PRIMARY SCHOOL")
    Q38AJ = (1047, "Q38A PERSON 10 TYPE OF PRIMARY SCHOOL")
    Q39A01 = (1048, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A02 = (1049, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A03 = (1050, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A04 = (1051, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A05 = (1052, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A06 = (1053, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A07 = (1054, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A08 = (1055, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A09 = (1056, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A10 = (1057, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A11 = (1058, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A12 = (1059, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A13 = (1060, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A14 = (1061, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A15 = (1062, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A16 = (1063, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A17 = (1064, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A18 = (1065, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A19 = (1066, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A20 = (1067, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A21 = (1068, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39A22 = (1069, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 1")
    Q39B01 = (1070, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B02 = (1071, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B03 = (1072, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B04 = (1073, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B05 = (1074, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B06 = (1075, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B07 = (1076, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B08 = (1077, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B09 = (1078, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B10 = (1079, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B11 = (1080, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B12 = (1081, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B13 = (1082, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B14 = (1083, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B15 = (1084, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B16 = (1085, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B17 = (1086, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B18 = (1087, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B19 = (1088, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B20 = (1089, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B21 = (1090, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39B22 = (1091, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 2")
    Q39C01 = (1092, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C02 = (1093, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C03 = (1094, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C04 = (1095, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C05 = (1096, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C06 = (1097, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C07 = (1098, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C08 = (1099, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C09 = (1100, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C10 = (1101, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C11 = (1102, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C12 = (1103, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C13 = (1104, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C14 = (1105, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C15 = (1106, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C16 = (1107, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C17 = (1108, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C18 = (1109, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C19 = (1110, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C20 = (1111, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C21 = (1112, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39C22 = (1113, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 3")
    Q39D01 = (1114, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D02 = (1115, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D03 = (1116, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D04 = (1117, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D05 = (1118, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D06 = (1119, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D07 = (1120, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D08 = (1121, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D09 = (1122, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D10 = (1123, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D11 = (1124, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D12 = (1125, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D13 = (1126, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D14 = (1127, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D15 = (1128, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D16 = (1129, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D17 = (1130, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D18 = (1131, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D19 = (1132, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D20 = (1133, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D21 = (1134, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39D22 = (1135, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 4")
    Q39E01 = (1136, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E02 = (1137, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E03 = (1138, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E04 = (1139, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E05 = (1140, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E06 = (1141, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E07 = (1142, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E08 = (1143, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E09 = (1144, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E10 = (1145, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E11 = (1146, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E12 = (1147, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E13 = (1148, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E14 = (1149, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E15 = (1150, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E16 = (1151, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E17 = (1152, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E18 = (1153, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E19 = (1154, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E20 = (1155, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E21 = (1156, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39E22 = (1157, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 5")
    Q39F01 = (1158, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F02 = (1159, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F03 = (1160, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F04 = (1161, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F05 = (1162, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F06 = (1163, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F07 = (1164, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F08 = (1165, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F09 = (1166, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F10 = (1167, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F11 = (1168, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F12 = (1169, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F13 = (1170, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F14 = (1171, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F15 = (1172, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F16 = (1173, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F17 = (1174, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F18 = (1175, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F19 = (1176, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F20 = (1177, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F21 = (1178, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39F22 = (1179, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 6")
    Q39G01 = (1180, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G02 = (1181, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G03 = (1182, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G04 = (1183, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G05 = (1184, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G06 = (1185, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G07 = (1186, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G08 = (1187, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G09 = (1188, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G10 = (1189, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G11 = (1190, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G12 = (1191, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G13 = (1192, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G14 = (1193, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G15 = (1194, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G16 = (1195, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G17 = (1196, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G18 = (1197, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G19 = (1198, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G20 = (1199, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G21 = (1200, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39G22 = (1201, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 7")
    Q39H01 = (1202, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H02 = (1203, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H03 = (1204, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H04 = (1205, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H05 = (1206, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H06 = (1207, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H07 = (1208, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H08 = (1209, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H09 = (1210, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H10 = (1211, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H11 = (1212, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H12 = (1213, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H13 = (1214, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H14 = (1215, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H15 = (1216, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H16 = (1217, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H17 = (1218, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H18 = (1219, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H19 = (1220, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H20 = (1221, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H21 = (1222, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39H22 = (1223, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 8")
    Q39I01 = (1224, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I02 = (1225, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I03 = (1226, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I04 = (1227, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I05 = (1228, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I06 = (1229, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I07 = (1230, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I08 = (1231, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I09 = (1232, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I10 = (1233, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I11 = (1234, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I12 = (1235, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I13 = (1236, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I14 = (1237, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I15 = (1238, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I16 = (1239, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I17 = (1240, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I18 = (1241, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I19 = (1242, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I20 = (1243, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I21 = (1244, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39I22 = (1245, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 9")
    Q39J01 = (1246, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J02 = (1247, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J03 = (1248, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J04 = (1249, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J05 = (1250, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J06 = (1251, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J07 = (1252, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J08 = (1253, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J09 = (1254, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J10 = (1255, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J11 = (1256, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J12 = (1257, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J13 = (1258, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J14 = (1259, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J15 = (1260, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J16 = (1261, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J17 = (1262, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J18 = (1263, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J19 = (1264, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J20 = (1265, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J21 = (1266, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q39J22 = (1267, "Q39 CHILDCARE RECEIVED IN LAST WEEK FOR PERSON 10")
    Q41AAT1AT = (1268, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A CHILDMINDER")
    Q41AAT2AT = (1269, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q41AAT3AT = (1270, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q41AAT4AT = (1271, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q41AAT5AT = (1272, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q41AAT6AT = (1273, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q41AAT7AT = (1274, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q41AAT8AT = (1275, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q41AAT9AT = (1276, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q41AAT10AT = (1277, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q41AAT11AT = (1278, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41AAT12AT = (1279, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41AAT13AT = (1280, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A FAMILY CENTRE")
    Q41AAT14AT = (1281, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q41AAT15AT = (1282, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH HOLIDAY/PLAY SCHEME")
    Q41AAT16AT = (1283, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q41AAT17AT = (1284, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q41AAT18AT = (1285, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q41AAT19AT = (1286, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH ANOTHER RELATIVE")
    Q41AAT20AT = (1287, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH FRIENDS OR NEIGHBOURS")
    Q41AAT21AT = (1288, "Q41 NUMBER OF DAYS PERSON 1 AT/WITH OTHER (SPECIFY)")
    Q41BAT1AT = (1289, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A CHILDMINDER")
    Q41BAT2AT = (1290, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q41BAT3AT = (1291, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q41BAT4AT = (1292, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q41BAT5AT = (1293, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q41BAT6AT = (1294, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q41BAT7AT = (1295, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q41BAT8AT = (1296, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q41BAT9AT = (1297, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q41BAT10AT = (1298, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q41BAT11AT = (1299, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41BAT12AT = (1300, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41BAT13AT = (1301, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A FAMILY CENTRE")
    Q41BAT14AT = (1302, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q41BAT15AT = (1303, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH HOLIDAY/PLAY SCHEME")
    Q41BAT16AT = (1304, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q41BAT17AT = (1305, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q41BAT18AT = (1306, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q41BAT19AT = (1307, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH ANOTHER RELATIVE")
    Q41BAT20AT = (1308, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH FRIENDS OR NEIGHBOURS")
    Q41BAT21AT = (1309, "Q41 NUMBER OF DAYS PERSON 2 AT/WITH OTHER (SPECIFY)")
    Q41CAT1AT = (1310, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A CHILDMINDER")
    Q41CAT2AT = (1311, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q41CAT3AT = (1312, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q41CAT4AT = (1313, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q41CAT5AT = (1314, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q41CAT6AT = (1315, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q41CAT7AT = (1316, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q41CAT8AT = (1317, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q41CAT9AT = (1318, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q41CAT10AT = (1319, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q41CAT11AT = (1320, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41CAT12AT = (1321, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41CAT13AT = (1322, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A FAMILY CENTRE")
    Q41CAT14AT = (1323, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q41CAT15AT = (1324, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH HOLIDAY/PLAY SCHEME")
    Q41CAT16AT = (1325, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q41CAT17AT = (1326, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q41CAT18AT = (1327, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q41CAT19AT = (1328, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH ANOTHER RELATIVE")
    Q41CAT20AT = (1329, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH FRIENDS OR NEIGHBOURS")
    Q41CAT21AT = (1330, "Q41 NUMBER OF DAYS PERSON 3 AT/WITH OTHER (SPECIFY)")
    Q41DAT1AT = (1331, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A CHILDMINDER")
    Q41DAT2AT = (1332, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q41DAT3AT = (1333, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q41DAT4AT = (1334, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q41DAT5AT = (1335, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q41DAT6AT = (1336, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q41DAT7AT = (1337, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q41DAT8AT = (1338, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q41DAT9AT = (1339, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q41DAT10AT = (1340, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q41DAT11AT = (1341, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41DAT12AT = (1342, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41DAT13AT = (1343, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A FAMILY CENTRE")
    Q41DAT14AT = (1344, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q41DAT15AT = (1345, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH HOLIDAY/PLAY SCHEME")
    Q41DAT16AT = (1346, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q41DAT17AT = (1347, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q41DAT18AT = (1348, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q41DAT19AT = (1349, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH ANOTHER RELATIVE")
    Q41DAT20AT = (1350, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH FRIENDS OR NEIGHBOURS")
    Q41DAT21AT = (1351, "Q41 NUMBER OF DAYS PERSON 4 AT/WITH OTHER (SPECIFY)")
    Q41EAT1AT = (1352, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A CHILDMINDER")
    Q41EAT2AT = (1353, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q41EAT3AT = (1354, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q41EAT4AT = (1355, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q41EAT5AT = (1356, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q41EAT6AT = (1357, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q41EAT7AT = (1358, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q41EAT8AT = (1359, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q41EAT9AT = (1360, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q41EAT10AT = (1361, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q41EAT11AT = (1362, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41EAT12AT = (1363, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41EAT13AT = (1364, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A FAMILY CENTRE")
    Q41EAT14AT = (1365, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q41EAT15AT = (1366, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH HOLIDAY/PLAY SCHEME")
    Q41EAT16AT = (1367, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q41EAT17AT = (1368, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q41EAT18AT = (1369, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q41EAT19AT = (1370, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH ANOTHER RELATIVE")
    Q41EAT20AT = (1371, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH FRIENDS OR NEIGHBOURS")
    Q41EAT21AT = (1372, "Q41 NUMBER OF DAYS PERSON 5 AT/WITH OTHER (SPECIFY)")
    Q41FAT1AT = (1373, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A CHILDMINDER")
    Q41FAT2AT = (1374, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q41FAT3AT = (1375, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q41FAT4AT = (1376, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q41FAT5AT = (1377, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q41FAT6AT = (1378, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q41FAT7AT = (1379, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q41FAT8AT = (1380, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q41FAT9AT = (1381, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q41FAT10AT = (1382, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q41FAT11AT = (1383, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41FAT12AT = (1384, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41FAT13AT = (1385, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A FAMILY CENTRE")
    Q41FAT14AT = (1386, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q41FAT15AT = (1387, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH HOLIDAY/PLAY SCHEME")
    Q41FAT16AT = (1388, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q41FAT17AT = (1389, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q41FAT18AT = (1390, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q41FAT19AT = (1391, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH ANOTHER RELATIVE")
    Q41FAT20AT = (1392, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH FRIENDS OR NEIGHBOURS")
    Q41FAT21AT = (1393, "Q41 NUMBER OF DAYS PERSON 6 AT/WITH OTHER (SPECIFY)")
    Q41GAT1AT = (1394, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A CHILDMINDER")
    Q41GAT2AT = (1395, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q41GAT3AT = (1396, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q41GAT4AT = (1397, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q41GAT5AT = (1398, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q41GAT6AT = (1399, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q41GAT7AT = (1400, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q41GAT8AT = (1401, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q41GAT9AT = (1402, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q41GAT10AT = (1403, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q41GAT11AT = (1404, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41GAT12AT = (1405, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41GAT13AT = (1406, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A FAMILY CENTRE")
    Q41GAT14AT = (1407, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q41GAT15AT = (1408, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH HOLIDAY/PLAY SCHEME")
    Q41GAT16AT = (1409, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q41GAT17AT = (1410, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q41GAT18AT = (1411, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q41GAT19AT = (1412, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH ANOTHER RELATIVE")
    Q41GAT20AT = (1413, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH FRIENDS OR NEIGHBOURS")
    Q41GAT21AT = (1414, "Q41 NUMBER OF DAYS PERSON 7 AT/WITH OTHER (SPECIFY)")
    Q41HAT1AT = (1415, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A CHILDMINDER")
    Q41HAT2AT = (1416, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q41HAT3AT = (1417, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q41HAT4AT = (1418, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q41HAT5AT = (1419, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q41HAT6AT = (1420, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q41HAT7AT = (1421, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q41HAT8AT = (1422, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q41HAT9AT = (1423, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q41HAT10AT = (1424, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q41HAT11AT = (1425, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41HAT12AT = (1426, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41HAT13AT = (1427, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A FAMILY CENTRE")
    Q41HAT14AT = (1428, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q41HAT15AT = (1429, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH HOLIDAY/PLAY SCHEME")
    Q41HAT16AT = (1430, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q41HAT17AT = (1431, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q41HAT18AT = (1432, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q41HAT19AT = (1433, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH ANOTHER RELATIVE")
    Q41HAT20AT = (1434, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH FRIENDS OR NEIGHBOURS")
    Q41HAT21AT = (1435, "Q41 NUMBER OF DAYS PERSON 8 AT/WITH OTHER (SPECIFY)")
    Q41IAT1AT = (1436, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A CHILDMINDER")
    Q41IAT2AT = (1437, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q41IAT3AT = (1438, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q41IAT4AT = (1439, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q41IAT5AT = (1440, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q41IAT6AT = (1441, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q41IAT7AT = (1442, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q41IAT8AT = (1443, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q41IAT9AT = (1444, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q41IAT10AT = (1445, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q41IAT11AT = (1446, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41IAT12AT = (1447, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41IAT13AT = (1448, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A FAMILY CENTRE")
    Q41IAT14AT = (1449, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q41IAT15AT = (1450, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH HOLIDAY/PLAY SCHEME")
    Q41IAT16AT = (1451, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q41IAT17AT = (1452, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q41IAT18AT = (1453, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q41IAT19AT = (1454, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH ANOTHER RELATIVE")
    Q41IAT20AT = (1455, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH FRIENDS OR NEIGHBOURS")
    Q41IAT21AT = (1456, "Q41 NUMBER OF DAYS PERSON 9 AT/WITH OTHER (SPECIFY)")
    Q41JAT1AT = (1457, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A CHILDMINDER")
    Q41JAT2AT = (1458, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q41JAT3AT = (1459, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q41JAT4AT = (1460, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q41JAT5AT = (1461, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q41JAT6AT = (1462, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q41JAT7AT = (1463, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q41JAT8AT = (1464, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q41JAT9AT = (1465, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q41JAT10AT = (1466, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q41JAT11AT = (1467, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41JAT12AT = (1468, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q41JAT13AT = (1469, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A FAMILY CENTRE")
    Q41JAT14AT = (1470, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q41JAT15AT = (1471, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH HOLIDAY/PLAY SCHEME")
    Q41JAT16AT = (1472, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q41JAT17AT = (1473, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q41JAT18AT = (1474, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q41JAT19AT = (1475, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH ANOTHER RELATIVE")
    Q41JAT20AT = (1476, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH FRIENDS OR NEIGHBOURS")
    Q41JAT21AT = (1477, "Q41 NUMBER OF DAYS PERSON 10 AT/WITH OTHER (SPECIFY)")
    Q42AAT1AT = (1478, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A CHILDMINDER")
    Q42AAT2AT = (1479, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q42AAT3AT = (1480, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q42AAT4AT = (1481, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q42AAT5AT = (1482, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q42AAT6AT = (1483, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q42AAT7AT = (1484, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q42AAT8AT = (1485, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q42AAT9AT = (1486, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q42AAT10AT = (1487, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q42AAT11AT = (1488, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42AAT12AT = (1489, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42AAT13AT = (1490, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A FAMILY CENTRE")
    Q42AAT14AT = (1491, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q42AAT15AT = (1492, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH HOLIDAY/PLAY SCHEME")
    Q42AAT16AT = (1493, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q42AAT17AT = (1494, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q42AAT18AT = (1495, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q42AAT19AT = (1496, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH ANOTHER RELATIVE")
    Q42AAT20AT = (1497, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH FRIENDS OR NEIGHBOURS")
    Q42AAT21AT = (1498, "Q42 NUMBER OF HOURS PERSON 1 AT/WITH OTHER (SPECIFY)")
    Q42BAT1AT = (1499, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A CHILDMINDER")
    Q42BAT2AT = (1500, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q42BAT3AT = (1501, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q42BAT4AT = (1502, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q42BAT5AT = (1503, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q42BAT6AT = (1504, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q42BAT7AT = (1505, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q42BAT8AT = (1506, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q42BAT9AT = (1507, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q42BAT10AT = (1508, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q42BAT11AT = (1509, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42BAT12AT = (1510, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42BAT13AT = (1511, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A FAMILY CENTRE")
    Q42BAT14AT = (1512, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q42BAT15AT = (1513, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH HOLIDAY/PLAY SCHEME")
    Q42BAT16AT = (1514, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q42BAT17AT = (1515, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q42BAT18AT = (1516, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q42BAT19AT = (1517, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH ANOTHER RELATIVE")
    Q42BAT20AT = (1518, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH FRIENDS OR NEIGHBOURS")
    Q42BAT21AT = (1519, "Q42 NUMBER OF HOURS PERSON 2 AT/WITH OTHER (SPECIFY)")
    Q42CAT1AT = (1520, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A CHILDMINDER")
    Q42CAT2AT = (1521, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q42CAT3AT = (1522, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q42CAT4AT = (1523, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q42CAT5AT = (1524, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q42CAT6AT = (1525, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q42CAT7AT = (1526, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q42CAT8AT = (1527, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q42CAT9AT = (1528, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q42CAT10AT = (1529, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q42CAT11AT = (1530, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42CAT12AT = (1531, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42CAT13AT = (1532, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A FAMILY CENTRE")
    Q42CAT14AT = (1533, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q42CAT15AT = (1534, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH HOLIDAY/PLAY SCHEME")
    Q42CAT16AT = (1535, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q42CAT17AT = (1536, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q42CAT18AT = (1537, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q42CAT19AT = (1538, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH ANOTHER RELATIVE")
    Q42CAT20AT = (1539, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH FRIENDS OR NEIGHBOURS")
    Q42CAT21AT = (1540, "Q42 NUMBER OF HOURS PERSON 3 AT/WITH OTHER (SPECIFY)")
    Q42DAT1AT = (1541, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A CHILDMINDER")
    Q42DAT2AT = (1542, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q42DAT3AT = (1543, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q42DAT4AT = (1544, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q42DAT5AT = (1545, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q42DAT6AT = (1546, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q42DAT7AT = (1547, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q42DAT8AT = (1548, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q42DAT9AT = (1549, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q42DAT10AT = (1550, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q42DAT11AT = (1551, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42DAT12AT = (1552, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42DAT13AT = (1553, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A FAMILY CENTRE")
    Q42DAT14AT = (1554, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q42DAT15AT = (1555, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH HOLIDAY/PLAY SCHEME")
    Q42DAT16AT = (1556, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q42DAT17AT = (1557, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q42DAT18AT = (1558, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q42DAT19AT = (1559, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH ANOTHER RELATIVE")
    Q42DAT20AT = (1560, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH FRIENDS OR NEIGHBOURS")
    Q42DAT21AT = (1561, "Q42 NUMBER OF HOURS PERSON 4 AT/WITH OTHER (SPECIFY)")
    Q42EAT1AT = (1562, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A CHILDMINDER")
    Q42EAT2AT = (1563, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q42EAT3AT = (1564, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q42EAT4AT = (1565, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q42EAT5AT = (1566, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q42EAT6AT = (1567, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q42EAT7AT = (1568, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q42EAT8AT = (1569, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q42EAT9AT = (1570, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q42EAT10AT = (1571, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q42EAT11AT = (1572, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42EAT12AT = (1573, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42EAT13AT = (1574, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A FAMILY CENTRE")
    Q42EAT14AT = (1575, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q42EAT15AT = (1576, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH HOLIDAY/PLAY SCHEME")
    Q42EAT16AT = (1577, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q42EAT17AT = (1578, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q42EAT18AT = (1579, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q42EAT19AT = (1580, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH ANOTHER RELATIVE")
    Q42EAT20AT = (1581, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH FRIENDS OR NEIGHBOURS")
    Q42EAT21AT = (1582, "Q42 NUMBER OF HOURS PERSON 5 AT/WITH OTHER (SPECIFY)")
    Q42FAT1AT = (1583, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A CHILDMINDER")
    Q42FAT2AT = (1584, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q42FAT3AT = (1585, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q42FAT4AT = (1586, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q42FAT5AT = (1587, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q42FAT6AT = (1588, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q42FAT7AT = (1589, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q42FAT8AT = (1590, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q42FAT9AT = (1591, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q42FAT10AT = (1592, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q42FAT11AT = (1593, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42FAT12AT = (1594, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42FAT13AT = (1595, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A FAMILY CENTRE")
    Q42FAT14AT = (1596, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q42FAT15AT = (1597, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH HOLIDAY/PLAY SCHEME")
    Q42FAT16AT = (1598, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q42FAT17AT = (1599, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q42FAT18AT = (1600, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q42FAT19AT = (1601, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH ANOTHER RELATIVE")
    Q42FAT20AT = (1602, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH FRIENDS OR NEIGHBOURS")
    Q42FAT21AT = (1603, "Q42 NUMBER OF HOURS PERSON 6 AT/WITH OTHER (SPECIFY)")
    Q42GAT1AT = (1604, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A CHILDMINDER")
    Q42GAT2AT = (1605, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q42GAT3AT = (1606, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q42GAT4AT = (1607, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q42GAT5AT = (1608, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q42GAT6AT = (1609, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q42GAT7AT = (1610, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q42GAT8AT = (1611, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q42GAT9AT = (1612, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q42GAT10AT = (1613, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q42GAT11AT = (1614, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42GAT12AT = (1615, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42GAT13AT = (1616, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A FAMILY CENTRE")
    Q42GAT14AT = (1617, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q42GAT15AT = (1618, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH HOLIDAY/PLAY SCHEME")
    Q42GAT16AT = (1619, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q42GAT17AT = (1620, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q42GAT18AT = (1621, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q42GAT19AT = (1622, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH ANOTHER RELATIVE")
    Q42GAT20AT = (1623, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH FRIENDS OR NEIGHBOURS")
    Q42GAT21AT = (1624, "Q42 NUMBER OF HOURS PERSON 7 AT/WITH OTHER (SPECIFY)")
    Q42HAT1AT = (1625, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A CHILDMINDER")
    Q42HAT2AT = (1626, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q42HAT3AT = (1627, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q42HAT4AT = (1628, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q42HAT5AT = (1629, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q42HAT6AT = (1630, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q42HAT7AT = (1631, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q42HAT8AT = (1632, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q42HAT9AT = (1633, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q42HAT10AT = (1634, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q42HAT11AT = (1635, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42HAT12AT = (1636, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42HAT13AT = (1637, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A FAMILY CENTRE")
    Q42HAT14AT = (1638, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q42HAT15AT = (1639, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH HOLIDAY/PLAY SCHEME")
    Q42HAT16AT = (1640, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q42HAT17AT = (1641, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q42HAT18AT = (1642, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q42HAT19AT = (1643, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH ANOTHER RELATIVE")
    Q42HAT20AT = (1644, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH FRIENDS OR NEIGHBOURS")
    Q42HAT21AT = (1645, "Q42 NUMBER OF HOURS PERSON 8 AT/WITH OTHER (SPECIFY)")
    Q42IAT1AT = (1646, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A CHILDMINDER")
    Q42IAT2AT = (1647, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q42IAT3AT = (1648, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q42IAT4AT = (1649, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q42IAT5AT = (1650, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q42IAT6AT = (1651, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q42IAT7AT = (1652, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q42IAT8AT = (1653, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q42IAT9AT = (1654, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q42IAT10AT = (1655, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q42IAT11AT = (1656, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42IAT12AT = (1657, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42IAT13AT = (1658, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A FAMILY CENTRE")
    Q42IAT14AT = (1659, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q42IAT15AT = (1660, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH HOLIDAY/PLAY SCHEME")
    Q42IAT16AT = (1661, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q42IAT17AT = (1662, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q42IAT18AT = (1663, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q42IAT19AT = (1664, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH ANOTHER RELATIVE")
    Q42IAT20AT = (1665, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH FRIENDS OR NEIGHBOURS")
    Q42IAT21AT = (1666, "Q42 NUMBER OF HOURS PERSON 9 AT/WITH OTHER (SPECIFY)")
    Q42JAT1AT = (1667, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A CHILDMINDER")
    Q42JAT2AT = (1668, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A DAILY NANNY WHO CAME TO OUR HOME")
    Q42JAT3AT = (1669, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A LIVE IN NANNY OR AU PAIR")
    Q42JAT4AT = (1670, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A BABY-SITTER WHO CAME TO OUR HOME")
    Q42JAT5AT = (1671, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL")
    Q42JAT6AT = (1672, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A PRIVATE CRECHE OR NURSERY SCHOOL")
    Q42JAT7AT = (1673, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A WORK PLACE CRECHE OR NURSERY")
    Q42JAT8AT = (1674, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL")
    Q42JAT9AT = (1675, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A PRIVATE PLAY GROUP OR PRE-SCHOOL")
    Q42JAT10AT = (1676, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL")
    Q42JAT11AT = (1677, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42JAT12AT = (1678, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL")
    Q42JAT13AT = (1679, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A FAMILY CENTRE")
    Q42JAT14AT = (1680, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH A TERM-TIME OUT OF SCHOOL CLUB")
    Q42JAT15AT = (1681, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH HOLIDAY/PLAY SCHEME")
    Q42JAT16AT = (1682, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH MY EX-SPOUSE OR PARTNER")
    Q42JAT17AT = (1683, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH THE CHILD'S GRANDPARENT(S)")
    Q42JAT18AT = (1684, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH THE CHILD'S OLDER BROTHER OR SISTER")
    Q42JAT19AT = (1685, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH ANOTHER RELATIVE")
    Q42JAT20AT = (1686, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH FRIENDS OR NEIGHBOURS")
    Q42JAT21AT = (1687, "Q42 NUMBER OF HOURS PERSON 10 AT/WITH OTHER (SPECIFY)")
    PQ43A1 = (1688, "Q43 CHILDMINDER PAID TO LOOK AFTER PERSON 1")
    PQ43A2 = (1689, "Q43 A DAILY NANNY WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 1")
    PQ43A3 = (1690, "Q43 A LIVE IN NANNY OR AU PAIR PAID TO LOOK AFTER PERSON 1")
    PQ43A4 = (1691, "Q43 A BABY-SITTER WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 1")
    PQ43A5 = (1692, "Q43 A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 1")
    PQ43A6 = (1693, "Q43 A PRIVATE CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 1")
    PQ43A7 = (1694, "Q43 A WORK PLACE CRECHE OR NURSERY PAID TO LOOK AFTER PERSON 1")
    PQ43A8 = (1695, "Q43 A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 1")
    PQ43A9 = (1696, "Q43 A PRIVATE PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 1")
    PQ43A10 = (1697, "Q43 A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 1")
    PQ43A11 = (1698, "Q43 A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 1")
    PQ43A12 = (1699, "Q43 A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 1")
    PQ43A13 = (1700, "Q43 A FAMILY CENTRE PAID TO LOOK AFTER PERSON 1")
    PQ43A14 = (1701, "Q43 A TERM TIME OUT OF SCHOOL CLUB")
    PQ43A15 = (1702, "Q43 A HOLIDAY PLAY SCHEME OR PLAY SCHEME")
    PQ43A16 = (1703, "Q43 MY EX-SPOUSE OR PARTNER PAID TO LOOK AFTER PERSON 1")
    PQ43A17 = (1704, "Q43 THE CHILD'S GRANDPARENT(S) PAID TO LOOK AFTER PERSON 1")
    PQ43A18 = (1705, "Q43 THE CHILD'S OLDER BROTHER OR SISTER PAID TO LOOK AFTER PERSON 1")
    PQ43A19 = (1706, "Q43 ANOTHER RELATIVE PAID TO LOOK AFTER PERSON 1")
    PQ43A20 = (1707, "Q43 FRIENDS OR NEIGHBOURS PAID TO LOOK AFTER PERSON 1")
    PQ43A21 = (1708, "Q43 OTHER (SPECIFY) PAID TO LOOK AFTER PERSON 1")
    PQ43B1 = (1709, "Q43 A CHILDMINDER PAID TO LOOK AFTER PERSON 2")
    PQ43B2 = (1710, "Q43 A DAILY NANNY WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 2")
    PQ43B3 = (1711, "Q43 A LIVE IN NANNY OR AU PAIR PAID TO LOOK AFTER PERSON 2")
    PQ43B4 = (1712, "Q43 A BABY-SITTER WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 2")
    PQ43B5 = (1713, "Q43 A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 2")
    PQ43B6 = (1714, "Q43 A PRIVATE CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 2")
    PQ43B7 = (1715, "Q43 A WORK PLACE CRECHE OR NURSERY PAID TO LOOK AFTER PERSON 2")
    PQ43B8 = (1716, "Q43 A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 2")
    PQ43B9 = (1717, "Q43 A PRIVATE PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 2")
    PQ43B10 = (1718, "Q43 A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 2")
    PQ43B11 = (1719, "Q43 A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 2")
    PQ43B12 = (1720, "Q43 A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 2")
    PQ43B13 = (1721, "Q43 A FAMILY CENTRE PAID TO LOOK AFTER PERSON 2")
    PQ43B14 = (1722, "Q43 A TERM TIME OUT OF SCHOOL CLUB")
    PQ43B15 = (1723, "Q43 A HOLIDAY PLAY SCHEME OR PLAY SCHEME")
    PQ43B16 = (1724, "Q43 MY EX-SPOUSE OR PARTNER PAID TO LOOK AFTER PERSON 2")
    PQ43B17 = (1725, "Q43 THE CHILD'S GRANDPARENT(S) PAID TO LOOK AFTER PERSON 2")
    PQ43B18 = (1726, "Q43 THE CHILD'S OLDER BROTHER OR SISTER PAID TO LOOK AFTER PERSON 2")
    PQ43B19 = (1727, "Q43 ANOTHER RELATIVE PAID TO LOOK AFTER PERSON 2")
    PQ43B20 = (1728, "Q43 FRIENDS OR NEIGHBOURS PAID TO LOOK AFTER PERSON 2")
    PQ43B21 = (1729, "Q43 OTHER (SPECIFY) PAID TO LOOK AFTER PERSON 2")
    PQ43C1 = (1730, "Q43 A CHILDMINDER PAID TO LOOK AFTER PERSON 3")
    PQ43C2 = (1731, "Q43 A DAILY NANNY WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 3")
    PQ43C3 = (1732, "Q43 A LIVE IN NANNY OR AU PAIR PAID TO LOOK AFTER PERSON 3")
    PQ43C4 = (1733, "Q43 A BABY-SITTER WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 3")
    PQ43C5 = (1734, "Q43 A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 3")
    PQ43C6 = (1735, "Q43 A PRIVATE CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 3")
    PQ43C7 = (1736, "Q43 A WORK PLACE CRECHE OR NURSERY PAID TO LOOK AFTER PERSON 3")
    PQ43C8 = (1737, "Q43 A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 3")
    PQ43C9 = (1738, "Q43 A PRIVATE PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 3")
    PQ43C10 = (1739, "Q43 A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 3")
    PQ43C11 = (1740, "Q43 A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 3")
    PQ43C12 = (1741, "Q43 A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 3")
    PQ43C13 = (1742, "Q43 A FAMILY CENTRE PAID TO LOOK AFTER PERSON 3")
    PQ43C14 = (1743, "Q43 A TERM TIME OUT OF SCHOOL CLUB")
    PQ43C15 = (1744, "Q43 A HOLIDAY PLAY SCHEME OR PLAY SCHEME")
    PQ43C16 = (1745, "Q43 MY EX-SPOUSE OR PARTNER PAID TO LOOK AFTER PERSON 3")
    PQ43C17 = (1746, "Q43 THE CHILD'S GRANDPARENT(S) PAID TO LOOK AFTER PERSON 3")
    PQ43C18 = (1747, "Q43 THE CHILD'S OLDER BROTHER OR SISTER PAID TO LOOK AFTER PERSON 3")
    PQ43C19 = (1748, "Q43 ANOTHER RELATIVE PAID TO LOOK AFTER PERSON 3")
    PQ43C20 = (1749, "Q43 FRIENDS OR NEIGHBOURS PAID TO LOOK AFTER PERSON 3")
    PQ43C21 = (1750, "Q43 OTHER (SPECIFY) PAID TO LOOK AFTER PERSON 3")
    PQ43D1 = (1751, "Q43 A CHILDMINDER PAID TO LOOK AFTER PERSON 4")
    PQ43D2 = (1752, "Q43 A DAILY NANNY WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 4")
    PQ43D3 = (1753, "Q43 A LIVE IN NANNY OR AU PAIR PAID TO LOOK AFTER PERSON 4")
    PQ43D4 = (1754, "Q43 A BABY-SITTER WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 4")
    PQ43D5 = (1755, "Q43 A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 4")
    PQ43D6 = (1756, "Q43 A PRIVATE CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 4")
    PQ43D7 = (1757, "Q43 A WORK PLACE CRECHE OR NURSERY PAID TO LOOK AFTER PERSON 4")
    PQ43D8 = (1758, "Q43 A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 4")
    PQ43D9 = (1759, "Q43 A PRIVATE PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 4")
    PQ43D10 = (1760, "Q43 A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 4")
    PQ43D11 = (1761, "Q43 A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 4")
    PQ43D12 = (1762, "Q43 A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 4")
    PQ43D13 = (1763, "Q43 A FAMILY CENTRE PAID TO LOOK AFTER PERSON 4")
    PQ43D14 = (1764, "Q43 A TERM TIME OUT OF SCHOOL CLUB")
    PQ43D15 = (1765, "Q43 A HOLIDAY PLAY SCHEME OR PLAY SCHEME")
    PQ43D16 = (1766, "Q43 MY EX-SPOUSE OR PARTNER PAID TO LOOK AFTER PERSON 4")
    PQ43D17 = (1767, "Q43 THE CHILD'S GRANDPARENT(S) PAID TO LOOK AFTER PERSON 4")
    PQ43D18 = (1768, "Q43 THE CHILD'S OLDER BROTHER OR SISTER PAID TO LOOK AFTER PERSON 4")
    PQ43D19 = (1769, "Q43 ANOTHER RELATIVE PAID TO LOOK AFTER PERSON 4")
    PQ43D20 = (1770, "Q43 FRIENDS OR NEIGHBOURS PAID TO LOOK AFTER PERSON 4")
    PQ43D21 = (1771, "Q43 OTHER (SPECIFY) PAID TO LOOK AFTER PERSON 4")
    PQ43E1 = (1772, "Q43 A CHILDMINDER PAID TO LOOK AFTER PERSON 5")
    PQ43E2 = (1773, "Q43 A DAILY NANNY WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 5")
    PQ43E3 = (1774, "Q43 A LIVE IN NANNY OR AU PAIR PAID TO LOOK AFTER PERSON 5")
    PQ43E4 = (1775, "Q43 A BABY-SITTER WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 5")
    PQ43E5 = (1776, "Q43 A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 5")
    PQ43E6 = (1777, "Q43 A PRIVATE CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 5")
    PQ43E7 = (1778, "Q43 A WORK PLACE CRECHE OR NURSERY PAID TO LOOK AFTER PERSON 5")
    PQ43E8 = (1779, "Q43 A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 5")
    PQ43E9 = (1780, "Q43 A PRIVATE PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 5")
    PQ43E10 = (1781, "Q43 A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 5")
    PQ43E11 = (1782, "Q43 A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 5")
    PQ43E12 = (1783, "Q43 A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 5")
    PQ43E13 = (1784, "Q43 A FAMILY CENTRE PAID TO LOOK AFTER PERSON 5")
    PQ43E14 = (1785, "Q43 A TERM TIME OUT OF SCHOOL CLUB")
    PQ43E15 = (1786, "Q43 A HOLIDAY PLAY SCHEME OR PLAY SCHEME")
    PQ43E16 = (1787, "Q43 MY EX-SPOUSE OR PARTNER PAID TO LOOK AFTER PERSON 5")
    PQ43E17 = (1788, "Q43 THE CHILD'S GRANDPARENT(S) PAID TO LOOK AFTER PERSON 5")
    PQ43E18 = (1789, "Q43 THE CHILD'S OLDER BROTHER OR SISTER PAID TO LOOK AFTER PERSON 5")
    PQ43E19 = (1790, "Q43 ANOTHER RELATIVE PAID TO LOOK AFTER PERSON 5")
    PQ43E20 = (1791, "Q43 FRIENDS OR NEIGHBOURS PAID TO LOOK AFTER PERSON 5")
    PQ43E21 = (1792, "Q43 OTHER (SPECIFY) PAID TO LOOK AFTER PERSON 5")
    PQ43F1 = (1793, "Q43 A CHILDMINDER PAID TO LOOK AFTER PERSON 6")
    PQ43F2 = (1794, "Q43 A DAILY NANNY WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 6")
    PQ43F3 = (1795, "Q43 A LIVE IN NANNY OR AU PAIR PAID TO LOOK AFTER PERSON 6")
    PQ43F4 = (1796, "Q43 A BABY-SITTER WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 6")
    PQ43F5 = (1797, "Q43 A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 6")
    PQ43F6 = (1798, "Q43 A PRIVATE CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 6")
    PQ43F7 = (1799, "Q43 A WORK PLACE CRECHE OR NURSERY PAID TO LOOK AFTER PERSON 6")
    PQ43F8 = (1800, "Q43 A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 6")
    PQ43F9 = (1801, "Q43 A PRIVATE PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 6")
    PQ43F10 = (1802, "Q43 A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 6")
    PQ43F11 = (1803, "Q43 A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 6")
    PQ43F12 = (1804, "Q43 A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 6")
    PQ43F13 = (1805, "Q43 A FAMILY CENTRE PAID TO LOOK AFTER PERSON 6")
    PQ43F14 = (1806, "Q43 A TERM TIME OUT OF SCHOOL CLUB")
    PQ43F15 = (1807, "Q43 A HOLIDAY PLAY SCHEME OR PLAY SCHEME")
    PQ43F16 = (1808, "Q43 MY EX-SPOUSE OR PARTNER PAID TO LOOK AFTER PERSON 6")
    PQ43F17 = (1809, "Q43 THE CHILD'S GRANDPARENT(S) PAID TO LOOK AFTER PERSON 6")
    PQ43F18 = (1810, "Q43 THE CHILD'S OLDER BROTHER OR SISTER PAID TO LOOK AFTER PERSON 6")
    PQ43F19 = (1811, "Q43 ANOTHER RELATIVE PAID TO LOOK AFTER PERSON 6")
    PQ43F20 = (1812, "Q43 FRIENDS OR NEIGHBOURS PAID TO LOOK AFTER PERSON 6")
    PQ43F21 = (1813, "Q43 OTHER (SPECIFY) PAID TO LOOK AFTER PERSON 6")
    PQ43G1 = (1814, "Q43 A CHILDMINDER PAID TO LOOK AFTER PERSON 7")
    PQ43G2 = (1815, "Q43 A DAILY NANNY WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 7")
    PQ43G3 = (1816, "Q43 A LIVE IN NANNY OR AU PAIR PAID TO LOOK AFTER PERSON 7")
    PQ43G4 = (1817, "Q43 A BABY-SITTER WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 7")
    PQ43G5 = (1818, "Q43 A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 7")
    PQ43G6 = (1819, "Q43 A PRIVATE CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 7")
    PQ43G7 = (1820, "Q43 A WORK PLACE CRECHE OR NURSERY PAID TO LOOK AFTER PERSON 7")
    PQ43G8 = (1821, "Q43 A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 7")
    PQ43G9 = (1822, "Q43 A PRIVATE PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 7")
    PQ43G10 = (1823, "Q43 A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 7")
    PQ43G11 = (1824, "Q43 A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 7")
    PQ43G12 = (1825, "Q43 A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 7")
    PQ43G13 = (1826, "Q43 A FAMILY CENTRE PAID TO LOOK AFTER PERSON 7")
    PQ43G14 = (1827, "Q43 A TERM TIME OUT OF SCHOOL CLUB")
    PQ43G15 = (1828, "Q43 A HOLIDAY PLAY SCHEME OR PLAY SCHEME")
    PQ43G16 = (1829, "Q43 MY EX-SPOUSE OR PARTNER PAID TO LOOK AFTER PERSON 7")
    PQ43G17 = (1830, "Q43 THE CHILD'S GRANDPARENT(S) PAID TO LOOK AFTER PERSON 7")
    PQ43G18 = (1831, "Q43 THE CHILD'S OLDER BROTHER OR SISTER PAID TO LOOK AFTER PERSON 7")
    PQ43G19 = (1832, "Q43 ANOTHER RELATIVE PAID TO LOOK AFTER PERSON 7")
    PQ43G20 = (1833, "Q43 FRIENDS OR NEIGHBOURS PAID TO LOOK AFTER PERSON 7")
    PQ43G21 = (1834, "Q43 OTHER (SPECIFY) PAID TO LOOK AFTER PERSON 7")
    PQ43H1 = (1835, "Q43 A CHILDMINDER PAID TO LOOK AFTER PERSON 8")
    PQ43H2 = (1836, "Q43 A DAILY NANNY WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 8")
    PQ43H3 = (1837, "Q43 A LIVE IN NANNY OR AU PAIR PAID TO LOOK AFTER PERSON 8")
    PQ43H4 = (1838, "Q43 A BABY-SITTER WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 8")
    PQ43H5 = (1839, "Q43 A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 8")
    PQ43H6 = (1840, "Q43 A PRIVATE CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 8")
    PQ43H7 = (1841, "Q43 A WORK PLACE CRECHE OR NURSERY PAID TO LOOK AFTER PERSON 8")
    PQ43H8 = (1842, "Q43 A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 8")
    PQ43H9 = (1843, "Q43 A PRIVATE PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 8")
    PQ43H10 = (1844, "Q43 A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 8")
    PQ43H11 = (1845, "Q43 A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 8")
    PQ43H12 = (1846, "Q43 A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 8")
    PQ43H13 = (1847, "Q43 A FAMILY CENTRE PAID TO LOOK AFTER PERSON 8")
    PQ43H14 = (1848, "Q43 A TERM TIME OUT OF SCHOOL CLUB")
    PQ43H15 = (1849, "Q43 A HOLIDAY PLAY SCHEME OR PLAY SCHEME")
    PQ43H16 = (1850, "Q43 MY EX-SPOUSE OR PARTNER PAID TO LOOK AFTER PERSON 8")
    PQ43H17 = (1851, "Q43 THE CHILD'S GRANDPARENT(S) PAID TO LOOK AFTER PERSON 8")
    PQ43H18 = (1852, "Q43 THE CHILD'S OLDER BROTHER OR SISTER PAID TO LOOK AFTER PERSON 8")
    PQ43H19 = (1853, "Q43 ANOTHER RELATIVE PAID TO LOOK AFTER PERSON 8")
    PQ43H20 = (1854, "Q43 FRIENDS OR NEIGHBOURS PAID TO LOOK AFTER PERSON 8")
    PQ43H21 = (1855, "Q43 OTHER (SPECIFY) PAID TO LOOK AFTER PERSON 8")
    PQ43I1 = (1856, "Q43 A CHILDMINDER PAID TO LOOK AFTER PERSON 9")
    PQ43I2 = (1857, "Q43 A DAILY NANNY WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 9")
    PQ43I3 = (1858, "Q43 A LIVE IN NANNY OR AU PAIR PAID TO LOOK AFTER PERSON 9")
    PQ43I4 = (1859, "Q43 A BABY-SITTER WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 9")
    PQ43I5 = (1860, "Q43 A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 9")
    PQ43I6 = (1861, "Q43 A PRIVATE CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 9")
    PQ43I7 = (1862, "Q43 A WORK PLACE CRECHE OR NURSERY PAID TO LOOK AFTER PERSON 9")
    PQ43I8 = (1863, "Q43 A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 9")
    PQ43I9 = (1864, "Q43 A PRIVATE PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 9")
    PQ43I10 = (1865, "Q43 A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 9")
    PQ43I11 = (1866, "Q43 A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 9")
    PQ43I12 = (1867, "Q43 A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 9")
    PQ43I13 = (1868, "Q43 A FAMILY CENTRE PAID TO LOOK AFTER PERSON 9")
    PQ43I14 = (1869, "Q43 A TERM TIME OUT OF SCHOOL CLUB")
    PQ43I15 = (1870, "Q43 A HOLIDAY PLAY SCHEME OR PLAY SCHEME")
    PQ43I16 = (1871, "Q43 MY EX-SPOUSE OR PARTNER PAID TO LOOK AFTER PERSON 9")
    PQ43I17 = (1872, "Q43 THE CHILD'S GRANDPARENT(S) PAID TO LOOK AFTER PERSON 9")
    PQ43I18 = (1873, "Q43 THE CHILD'S OLDER BROTHER OR SISTER PAID TO LOOK AFTER PERSON 9")
    PQ43I19 = (1874, "Q43 ANOTHER RELATIVE PAID TO LOOK AFTER PERSON 9")
    PQ43I20 = (1875, "Q43 FRIENDS OR NEIGHBOURS PAID TO LOOK AFTER PERSON 9")
    PQ43I21 = (1876, "Q43 OTHER (SPECIFY) PAID TO LOOK AFTER PERSON 9")
    PQ43J1 = (1877, "Q43 A CHILDMINDER PAID TO LOOK AFTER PERSON 10")
    PQ43J2 = (1878, "Q43 A DAILY NANNY WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 10")
    PQ43J3 = (1879, "Q43 A LIVE IN NANNY OR AU PAIR PAID TO LOOK AFTER PERSON 10")
    PQ43J4 = (1880, "Q43 A BABY-SITTER WHO CAME TO OUR HOME PAID TO LOOK AFTER PERSON 10")
    PQ43J5 = (1881, "Q43 A LOCAL AUTHORITY CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 10")
    PQ43J6 = (1882, "Q43 A PRIVATE CRECHE OR NURSERY SCHOOL PAID TO LOOK AFTER PERSON 10")
    PQ43J7 = (1883, "Q43 A WORK PLACE CRECHE OR NURSERY PAID TO LOOK AFTER PERSON 10")
    PQ43J8 = (1884, "Q43 A LOCAL AUTHORITY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 10")
    PQ43J9 = (1885, "Q43 A PRIVATE PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 10")
    PQ43J10 = (1886, "Q43 A COMMUNITY OR VOLUNTARY PLAY GROUP OR PRE-SCHOOL PAID TO LOOK AFTER PERSON 10")
    PQ43J11 = (1887, "Q43 A NURSERY CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 10")
    PQ43J12 = (1888, "Q43 A RECEPTION CLASS ATTACHED TO A PRIMARY SCHOOL PAID TO LOOK AFTER PERSON 10")
    PQ43J13 = (1889, "Q43 A FAMILY CENTRE PAID TO LOOK AFTER PERSON 10")
    PQ43J14 = (1890, "Q43 A TERM TIME OUT OF SCHOOL CLUB")
    PQ43J15 = (1891, "Q43 A HOLIDAY PLAY SCHEME OR PLAY SCHEME")
    PQ43J16 = (1892, "Q43 MY EX-SPOUSE OR PARTNER PAID TO LOOK AFTER PERSON 10")
    PQ43J17 = (1893, "Q43 THE CHILD'S GRANDPARENT(S) PAID TO LOOK AFTER PERSON 10")
    PQ43J18 = (1894, "Q43 THE CHILD'S OLDER BROTHER OR SISTER PAID TO LOOK AFTER PERSON 10")
    PQ43J19 = (1895, "Q43 ANOTHER RELATIVE PAID TO LOOK AFTER PERSON 10")
    PQ43J20 = (1896, "Q43 FRIENDS OR NEIGHBOURS PAID TO LOOK AFTER PERSON 10")
    PQ43J21 = (1897, "Q43 OTHER (SPECIFY) PAID TO LOOK AFTER PERSON 10")
    PQ44A = (1898, "PERSON 1   - was last week (ending Sunday) a school holiday for person 1?")
    PQ44B = (1899, "PERSON 2   - was last week (ending Sunday) a school holiday for person 2?")
    PQ44C = (1900, "PERSON 3   - was last week (ending Sunday) a school holiday for person 3?")
    PQ44D = (1901, "PERSON 4   - was last week (ending Sunday) a school holiday for person 4?")
    PQ44E = (1902, "PERSON 5   - was last week (ending Sunday) a school holiday for person 5?")
    PQ44F = (1903, "PERSON 6   - was last week (ending Sunday) a school holiday for person 6?")
    PQ44G = (1904, "PERSON 7   - was last week (ending Sunday) a school holiday for person 7?")
    PQ44H = (1905, "PERSON 8   - was last week (ending Sunday) a school holiday for person 8?")
    PQ44I = (1906, "PERSON 9   - was last week (ending Sunday) a school holiday for person 9?")
    PQ44J = (1907, "PERSON 10 - was last week (ending Sunday) a school holiday for person 10?")
    PQ45 = (1908, "Q45:  Do you look after any sick/ disabled/ elderly LIVING WITH YOU?")
    PQ46 = (1909, "Q46:  Number of sick/ disabled/ elderly LIVING WITH YOU that look after?")
    PQ47 = (1910, "Q47:  Do you look after any sick/ disabled/ elderly NOT LIVING WITH YOU?")
    PQ48 = (1911, "Q48:  Number of sick/ disabled/ elderly NOT LIVING WITH YOU that look after?")
    ATPQ49A1 = (1912, "Q49:  Who is it that you look after or help:  SPOUSE OR PARTNER?")
    ATPQ49A2 = (1913, "Q49:  Who is it that you look after or help:  OWN CHILD, ADOPTED CHILD, OR STEP CHILD?")
    ATPQ49A3 = (1914, "Q49:  Who is it that you look after or help:  FOSTER CHILD?")
    ATPQ49A4 = (1915, "Q49:  Who is it that you look after or help:  BROTHER OR SISTER?")
    ATPQ49A5 = (1916, "Q49:  Who is it that you look after or help:  PARENT?")
    ATPQ49A6 = (1917, "Q49:  Who is it that you look after or help:  PARENT-IN-LAW OR PARTNER'S PARENT?")
    ATPQ49A7 = (1918, "Q49:  Who is it that you look after or help:  OTHER RELATIVE?")
    ATPQ49A8 = (1919, "Q49:  Who is it that you look after or help:  FRIEND OR NEIGHBOUR?")
    ATPQ49A9 = (1920, "Q49:  Who is it that you look after or help:  CLIENT OF VOLUNTARY ORGANISATION?")
    ATPQ49A10 = (1921, "Q49:  Who is it that you look after or help:  OTHER?")
    ATPQ49A11 = (1922, "Q49:  Who is it that you look after or help:  DON'T KNOW?")
    ATPQ49A12 = (1923, "Q49:  Who is it that you look after or help:  REFUSED?")
    ATPQ50A1 = (1924, "Q50:  Age of person or people that you look after:   0 -   4 yrs?")
    ATPQ50A2 = (1925, "Q50:  Age of person or people that you look after:   5 -   9 yrs?")
    ATPQ50A3 = (1926, "Q50:  Age of person or people that you look after:  10 - 14 yrs?")
    ATPQ50A4 = (1927, "Q50:  Age of person or people that you look after:  15 - 19 yrs?")
    ATPQ50A5 = (1928, "Q50:  Age of person or people that you look after:  20 - 29 yrs?")
    ATPQ50A6 = (1929, "Q50:  Age of person or people that you look after:  30 - 39 yrs?")
    ATPQ50A7 = (1930, "Q50:  Age of person or people that you look after:  40 - 49 yrs?")
    ATPQ50A8 = (1931, "Q50:  Age of person or people that you look after:  50 - 59 yrs?")
    ATPQ50A9 = (1932, "Q50:  Age of person or people that you look after:  60 - 69 yrs?")
    ATPQ50A10 = (1933, "Q50:  Age of person or people that you look after:  70 - 79 yrs?")
    ATPQ50A11 = (1934, "Q50:  Age of person or people that you look after:  80 yrs or more?")
    ATPQ50A12 = (1935, "Q50:  Age of person or people that you look after:  DON'T KNOW?")
    ATPQ50A13 = (1936, "Q50:  Age of person or people that you look after:  REFUSED?")
    ATPQ51A1 = (1937, "Q51:  Sex of person or people that you look after:  MALE?")
    ATPQ51A2 = (1938, "Q51:  Sex of person or people that you look after:  FEMALE?")
    ATPQ51A3 = (1939, "Q51:  Sex of person or people that you look after:  DON'T KNOW?")
    ATPQ51A4 = (1940, "Q51:  Sex of person or people that you look after:  REFUSED?")
    PQ52A01 = (1941, "Q52 Adults (16yrs or over) only asked:  Type of help given:  HELP WITH PERSONAL CARE?")
    PQ52A02 = (1942, "Q52 Adults (16yrs or over) only asked:  Type of help given:  PHYSICAL HELP?")
    PQ52A03 = (1943, "Q52 Adults (16yrs or over) only asked:  Type of help given:  HELPING WITH PAPERWORK OR FINANCIAL MATTERS?")
    PQ52A04 = (1944, "Q52 Adults (16yrs or over) only asked:  Type of help given:  OTHER PRACTICAL HELP?")
    PQ52A05 = (1945, "Q52 Adults (16yrs or over) only asked:  Type of help given:  KEEPING HIM/ HER COMPANY?")
    PQ52A06 = (1946, "Q52 Adults (16yrs or over) only asked:  Type of help given:  TAKING HIM/ HER OUT?")
    PQ52A07 = (1947, "Q52 Adults (16yrs or over) only asked:  Type of help given:  GIVING MEDICINES?")
    PQ52A08 = (1948, "Q52 Adults (16yrs or over) only asked:  Type of help given:  KEEPING AN EYE ON HIM/ HER TO SEE IF ALRIGHT?")
    PQ52A09 = (1949, "Q52 Adults (16yrs or over) only asked:  Type of help given:  TAKING OUT (FOR WALKS, A DRIVE, TO SEE FRIENDS OR RELATIVES)?")
    PQ52A10 = (1950, "Q52 Adults (16yrs or over) only asked:  Type of help given:  OTHER?")
    PQ52C01 = (1951, "Q52 Children (under 16yrs) only asked:  Type of help given:  HELP WITH PERSONAL CARE (DRESSING, FEEDING)?")
    PQ52C02 = (1952, "Q52 Children (under 16yrs) only asked:  Type of help given:  HELP AROUND THE HOUSE (TIDYING UP, ETC)?")
    PQ52C03 = (1953, "Q52 Children (under 16yrs) only asked:  Type of help given:  KEEPING HIM/ HER COMPANY?")
    PQ52C04 = (1954, "Q52 Children (under 16yrs) only asked:  Type of help given:  KEEPING AN EYE ON HIM/ HER TO SEE IF ALRIGHT?")
    PQ52C05 = (1955, "Q52 Children (under 16yrs) only asked:  Type of help given:  TAKING OUT (FOR WALKS, TO SEE FRIENDS OR RELATIVES)?")
    PQ52C06 = (1956, "Q52 Children (under 16yrs) only asked:  Type of help given:  OTHER?")
    PQ53 = (1957, "Q53: Total time spent each week on people care for")
    PQ54 = (1958, "Q54 BRITISH NATIONAL?")
    PQ55 = (1959, "Q55 MARITAL STATUS")
    PQ56 = (1960, "[Not living with husband/ wife at Q55]  Are you living with someone as a couple?")
    PQ57 = (1961, "Q57 IS SPOUSE A MEMBER OF THE HOUSEHOLD?")
    PROXY = (1962, "Normal or proxy interview?")
    PROXYTYP = (1963, "Type of interview - adult/child & proxy/normal")
    PROXYWHO = (1964, "Proxy interview is being done with whom?")
    IAGE = (1965, "AGE OF RESPONDENT")
    IAGEGRP = (1966, "Age group")
    ISEX = (1967, "SEX")
    IETHNIC = (1968, "ETHNICITY")
    MANAGE2 = (1969, "Management responsibilities (of economically active & employed)")
    ECONACT = (1970, "Economic activity")
    ECONACT2 = (1971, "Economic activity - 2 (interim variable)")
    ECONACT3 = (1972, "Economic activity - 3")
    EMPINCBD = (1973, "Employee - Net MONTHLY income - Banded (sources: Q10 & Q11a)")
    SEINCBD = (1974, "Self-employed - Net MONTHLY income - Banded (sources: Q13c & Q13d)")
    TOTPINC = (1975, "Total net monthly personal income (for employees & self-employed together)")
    HRS_UNPD = (1976, "Total weekly hours UNPAID work in own/ relatives's business (copy of Q14a)")
    HRS_JOB1 = (1977, "Total weekly hours usually worked in MAIN job (incl paid & unpaid overtime) by people in paid work (employed or self-employed)")
    HRS_JOB2 = (1978, "Total weekly hours usually worked in SECOND job (copy of Q16F)")
    HRS_TOT = (1979, "Total hours usually worked per week: unpaid work for own/rel business + main job + second job combined")
    HRS_GRP = (1980, "Total weekly hours usually worked - paid work (main + 2nd job) or unpaid work - banded")
    SIC = (1981, "Standard Industrial Classification 1992 (4-digit) - for respondent's MAIN JOB")
    SOC = (1982, "Standard Occupational Classification 2000 for respondent's MAIN JOB")
    SIC2 = (1983, "Standard Industrial Classification 1992 (4-digit) - for respondent's SECOND JOB")
    SOC2 = (1984, "Standard Occupational Classification 2000 for respondent's SECOND JOB")
    NSSECB = (1985, "National Statistics Socio-Economic Classification")
    NSSECB_8 = (1986, "NS Socio-Economic Classification - 8 classes")
    NSSECB_5 = (1987, "NS Socio-Economic Classification - 5 classes")
    NSSECB_3 = (1988, "NS Socio-Economic Classification - 3 classes")
    HIQUAL4 = (1989, "Highest qualification gained - HARMONISED DEFINITION")
    AGELEFT = (1990, " Age left full-time education - grouped")
    LIVARR = (1991, "Living arrangements (as reported by respondent at q55 & q56 - NOT based on relationships in hhld grid )")
    PROVCARE = (1992, "Q45 & Q47: Do you look after any sick/ disabled/ elderly person (either living with you or not living with you)?")
    HDAY = (1993, "Day of household interview")
    HMONTH = (1994, "Month of household interview")
    HYEAR = (1995, "Year of household interview")
    GORPAF = (1996, "Government Office Region")
    GORPAF2 = (1997, "Govn Office Region - 8 categories")
    GORPAF3 = (1998, "Govn Office Region - 4 countries")
    POP_DEN = (1999, "Population density (persons per 10 hectares - uses 1991 Census data for postcode sector)")
    POP_DEN2 = (2000, "Population density - banded (persons per 10 hectares)")
    UNEMP = (2001, "Unemployment rate (%) - uses 1991 Census data for postcode sector")
    UNEMP2 = (2002, "Unemployment rate - percentage banded")
    HNUMB = (2003, "Number of people in household (all ages)")
    NUMADULT = (2004, "Number of adults   (16 yrs or more) in hhld")
    NUMCHILD = (2005, "Number of children (15 yrs or less) in hhld")
    CHILD = (2006, "Whether child (15yrs or less) in household or not")
    AGEYNGST = (2007, "Age of youngest person in household")
    NUM0_2 = (2008, "Number aged 0 - 2 yrs in hhld")
    NUM3_4 = (2009, "Number aged 3 - 4 yrs in hhld")
    NUM5_9 = (2010, "Number aged 5 - 9 yrs in hhld")
    NUM10_15 = (2011, "Number aged 10 - 15 yrs in hhld")
    NUM16_17 = (2012, "Number aged 16 - 17yrs")
    HRP_PER = (2013, "Household Reference Person - person number")
    SPOUSE1 = (2014, "For hhlds with one marr/cohab couple - person number of FIRST spouse")
    SPOUSE2 = (2015, "For hhlds with one marr/cohab couple - person number of SECOND spouse")
    TENURE2 = (2016, "Tenure - grouped")
    CARAVAIL = (2017, "Whether household owns/ has continuous use of car, motor bike or other motor vehicle")
    GROSHINC = (2018, "Household Income band (gross ie before deductions) - per year (source: hhld qstn 10b)")
    HHTYPE4 = (2019, "Household type - main variable for hhld type (16 categories)")
    HHTYPE5 = (2020, "Household type - 8 categories")
    WTPQ_GR = (2021, "Weight - for grossing to UK population aged 8yrs or more")
    WTPQ_UG = (2022, "Weight - ungrossed")


class Q1A(OrderedEnum):
    YES = '1'
    NO = '2'
    DON_T_KNOW = '3'
    REFUSED = '4'
    MISSING1 = '-1'


class PC1(OrderedEnum):
    YES = '1'
    NO = '2'
    DON_T_KNOW = '3'
    NO_ANSWER = '4'
    REFUSED = '5'
    MISSING1 = '-1'


Q1B = Q1A


class Q1C(OrderedEnum):
    EMPLOYER_PROVIDING_WEPT = '1'
    PROJECT_PROVIDING_WEPT = '2'
    COLLEGETRAINING_CENTRE = '3'
    AWAY_FROM_EMPLOYERPROJECT = '4'
    AWAY_FROM_COLLEGETRAINING_CENTRE = '5'
    DON_T_KNOW = '6'
    REFUSED = '7'
    MISSING1 = '-1'


class Q2A(OrderedEnum):
    YES = '1'
    NO = '2'
    WAITING_ON_NEW_JOBBUSINESS = '3'
    DON_T_KNOW = '4'
    REFUSED = '5'
    MISSING1 = '-1'


class Q2B(OrderedEnum):
    HOLIDAY = '1'
    SICKNESS = '2'
    STUDYING = '3'
    MATERNITYPATERNITY_LEAVE = '4'
    OTHER_REASON = '5'
    DON_T_KNOW = '6'
    REFUSED = '7'
    MISSING1 = '-1'


Q3A = Q1A


Q3B = Q1A


Q3C = Q1A


class Q3DWK(OrderedEnum):
    YES = '1'
    NO = '2'
    MISSING1 = '-1'


class Q5(OrderedEnum):
    PRIVATE_SECTOR = '1'
    PUBLIC_SECTOR = '2'
    DON_T_KNOW = '3'
    REFUSED = '4'
    MISSING1 = '-1'


class Q7(OrderedEnum):
    EMPLOYEE = '1'
    SELF_EMPLOYED = '2'
    DON_T_KNOW = '3'
    REFUSED = '4'
    MISSING1 = '-1'


class Q8A(OrderedEnum):
    MANAGER = '1'
    FOREMANSUPERVISOR = '2'
    NOT_MANAGERSUPERVISOR = '3'
    DON_T_KNOW = '4'
    REFUSED = '5'
    MISSING1 = '-1'


class Q8B(OrderedEnum):
    N1_2 = '1'
    N3_24 = '2'
    N25_99 = '3'
    N100_499 = '4'
    N500_999 = '5'
    N1000_OR_MORE = '6'
    DK___LESS_THAN_25 = '7'
    DK___25_OR_MORE = '8'
    MISSING1 = '-1'


class Q8C(OrderedEnum):
    FULL_TIME_ = '1'
    OR_PART_TIME = '2'
    DON_T_KNOW = '3'
    REFUSED = '4'
    MISSING1 = '-1'


class Q8D(OrderedEnum):
    MOST_OF_THE_TIME = '1'
    OCCASIONALLY = '2'
    NEVER = '3'
    DON_T_KNOW = '4'
    REFUSED = '5'
    MISSING1 = '-1'


class Q8E(OrderedEnum):
    PROXY_INTERVIEW___NOT_ASKED = '-2'
    THREE_SHIFT_PATTERN = '1'
    CONTINENTAL_SHIFTS = '2'
    TWO_SHIFT_SYSTEM_DOUBLE_DAYS = '3'
    SOME_NIGHT_AND_SOME_DAY_SHIFTS___VARIES = '4'
    SPLIT_SHIFTS = '5'
    MORNING_SHIFTS = '6'
    EVENING_OR_TWILIGHT_SHIFTS = '7'
    NIGHT_SHIFTS = '8'
    WEEKEND_SHIFTS = '9'
    OTHER_TYPES_OF_SHIFTWORK = '10'
    DONT_KNOW = '11'
    REFUSE = '12'
    MISSING1 = '-1'


class ATQ9A1(OrderedEnum):
    NO = '0'
    YES = '1'
    DON_T_KNOW_REFUSE = '3'
    MISSING1 = '-1'


ATQ9A2 = ATQ9A1


ATQ9A3 = ATQ9A1


ATQ9A4 = ATQ9A1


ATQ9A5 = ATQ9A1


ATQ9A6 = ATQ9A1


ATQ9A7 = ATQ9A1


ATQ9A8 = ATQ9A1


class Q10X(OrderedEnum):
    LESS_THAN_217_POUNDS = '0'
    N217_TO_LESS_THAN_433_POUNDS = '1'
    N433_TO_LESS_THAN_867_POUNDS = '2'
    N867_TO_LESS_THAN_1_300_POUNDS = '3'
    N1_300_TO_LESS_THAN_1_733_POUNDS = '4'
    N1_733_TO_LESS_THAN_2_817_POUNDS = '5'
    N2_817_TO_LESS_THAN_3_417_POUNDS = '6'
    N3_417_TO_LESS_THAN_3_833_POUNDS = '7'
    N3_833_TO_LESS_THAN_4_583_POUNDS = '8'
    N4_583_TO_LESS_TAHN_6_667_POUNDS = '9'
    N6_667_POUNDS_OR_MORE = '10'
    DON_T_KNOW = '11'
    REFUSED = '12'
    MISSING1 = '-1'


class Q11(OrderedEnum):
    ONE_WEEK = '1'
    TWO_WEEKS = '2'
    FOUR_WEEKS = '3'
    CALENDAR_MONTH = '4'
    ONE_YEAR12_MONTHS52_WEEKS = '5'
    ONE_OFFLUMP_SUM = '6'
    OTHER = '7'
    HOURS_WRITE_IN = '8'
    DON_T_KNOW = '9'
    REFUSED = '10'
    MISSING1 = '-1'


class Q11A(OrderedEnum):
    LESS_THAN_215_POUNDS = '1'
    N215_TO_LESS_THAN_435_POUNDS = '2'
    N435_TO_LESS_THAN_870_POUNDS = '3'
    N870_TO_LESS_THAN_1_305_POUNDS = '4'
    N1_305_TO_LESS_THAN_1_740_POUNDS = '5'
    N1_740_TO_LESS_THAN_2_820_POUNDS = '6'
    N2_820_TO_LESS_THAN_3_420_POUNDS = '7'
    N3_420_TO_LESS_THAN_3_830_POUNDS = '8'
    N3_830_TO_LESS_THAN_4_580_POUNDS = '9'
    N4_580_TO_LESS_THAN_6_670_POUNDS = '10'
    N6_670_POUNDS_OR_MORE = '11'
    DON_T_KNOW = '12'
    REFUSED = '13'
    MISSING1 = '-1'


class Q13A(OrderedEnum):
    ON_OWNWITH_PARTNER_BUT_NO_EMPLOYEES = '1'
    WITH_EMPLOYEES = '2'
    DON_T_KNOW = '3'
    REFUSED = '4'
    MISSING1 = '-1'


class Q13B(OrderedEnum):
    N1_2 = '1'
    N3_24 = '2'
    N25_99 = '3'
    N100_499 = '4'
    N500_999 = '5'
    N1000_OR_MORE = '6'
    DK___LESS_THAN_25 = '7'
    DK___25_OR_MORE = '8'
    DON_T_KNOW = '9'
    REFUSED = '10'
    MISSING1 = '-1'


Q13D = Q11A


class Q13E(OrderedEnum):
    FULL_TIME = '1'
    OR_PART_TIME = '2'
    DON_T_KNOW = '3'
    REFUSED = '4'
    MISSING1 = '-1'


class Q14B(OrderedEnum):
    YES = '1'
    NO = '2'
    DON_T_KNOW = '3'
    REFUSED = '4'
    MISSING1 = '-9'
    MISSING2 = '-7'
    MISSING3 = '-1'


class Q15(OrderedEnum):
    HOME = '1'
    SAME_GROUNDS_AS_HOME = '2'
    DIFFERENT_PLACES__USING_HISHER_HOME_AS_A_BASE = '3'
    SOMEWHERE_QUITE_SEPARATE_FROM_HOME = '4'
    SOMEDAYS_AT_HOME_OTHERS_QUITE_SEPARATE_FROM_HOME = '5'
    DON_T_KNOW = '6'
    REFUSED = '7'
    MISSING1 = '-1'


Q15B = Q1A


Q16A = Q1A


class Q16B(OrderedEnum):
    N1 = '1'
    N2 = '2'
    N3 = '3'
    N4 = '4'
    N5 = '5'
    N6 = '6'
    N7 = '7'
    N8 = '8'
    DON_T_KNOW = '9'
    REFUSED = '10'
    MISSING1 = '-1'


Q16G = Q8A


class Q16H(OrderedEnum):
    N1_2 = '1'
    N3_24 = '2'
    N25_99 = '3'
    N100_499 = '4'
    N500_999 = '5'
    N1000_OR_MORE = '6'
    DK___LESS_THAN_25 = '7'
    DK___25_OR_MORE = '8'
    DON_T_KNOW = '9'
    REFUSED = '10'
    NO_ANSWER = '11'
    MISSING1 = '-1'


Q17 = Q1A


class Q18A(OrderedEnum):
    PROXY_INTERVIEW___NOT_ASKED = '-2'
    YES = '1'
    NO = '2'
    DON_T_KNOW = '3'
    REFUSED = '4'
    MISSING1 = '-1'


Q18B = Q18A


Q18C = Q18A


Q18D = Q18A


Q18E = Q18A


Q18F = Q18A


Q18G = Q18A


Q18H = Q18A


Q18I = Q18A


Q18J = Q18A


Q18K = Q18A


Q19 = Q18A


class Q20(OrderedEnum):
    WAITING_FOR_RESULTS_OF_A_JOB_INTERVIEW_BEING_ASSESSED = '1'
    STUDENT = '2'
    LOOKING_AFTER_FAMILY_HOME = '3'
    TEMPORARILY_SICK_OR_INJURED = '4'
    LONG_TERM_SICK_OR_DISABLED = '5'
    BELIEVES_NO_JOBS_AVAILABLE = '6'
    NOT_YET_STARTED_LOOKING = '7'
    RETIRED_FROM_PAID_WORK = '8'
    ANY_OTHER_REASON = '9'
    DON_T_KNOW = '10'
    REFUSED = '11'
    MISSING1 = '-1'


class ATQ21A1(OrderedEnum):
    NO = '0'
    YES = '1'
    MISSING1 = '-1'


ATQ21A2 = ATQ21A1


ATQ21A3 = ATQ21A1


ATQ21A4 = ATQ21A1


ATQ21A5 = ATQ21A1


ATQ21A6 = ATQ21A1


ATQ21A7 = ATQ21A1


ATQ21A8 = ATQ21A1


ATQ21A9 = ATQ21A1


ATQ21A10 = ATQ21A1


ATQ21A11 = ATQ21A1


ATQ21B1 = ATQ21A1


ATQ21B2 = ATQ21A1


ATQ21B3 = ATQ21A1


ATQ21B4 = ATQ21A1


ATQ21B5 = ATQ21A1


ATQ21B6 = ATQ21A1


Q21BA01 = Q3DWK


Q21BA02 = Q3DWK


Q21BA03 = Q3DWK


Q21BA04 = Q3DWK


Q21BA05 = Q3DWK


Q21BA06 = Q3DWK


Q21BA07 = Q3DWK


Q21BA08 = Q3DWK


Q21BA09 = Q3DWK


Q21BA10 = Q3DWK


Q21BA11 = Q3DWK


Q21BA12 = Q3DWK


Q21BA13 = Q3DWK


Q21BB01 = Q3DWK


Q21BB02 = Q3DWK


Q21BB03 = Q3DWK


Q21BB04 = Q3DWK


Q21BB05 = Q3DWK


Q21BB06 = Q3DWK


Q21BB07 = Q3DWK


Q21BB08 = Q3DWK


Q21BB09 = Q3DWK


Q21BB10 = Q3DWK


Q21BB11 = Q3DWK


Q21BB12 = Q3DWK


Q21BB13 = Q3DWK


Q21BC01 = Q3DWK


Q21BC02 = Q3DWK


Q21BC03 = Q3DWK


Q21BC04 = Q3DWK


Q21BC05 = Q3DWK


Q21BC06 = Q3DWK


Q21BC07 = Q3DWK


Q21BC08 = Q3DWK


Q21BC09 = Q3DWK


Q21BC10 = Q3DWK


Q21BC11 = Q3DWK


Q21BC12 = Q3DWK


Q21BC13 = Q3DWK


class Q21C(OrderedEnum):
    PROXY_INTERVIEW___NOT_ASKED = '-2'
    TOGETHER_WITH_PENSION = '1'
    SEPARATE_PAYMENT = '2'
    DON_T_KNOW = '3'
    REFUSED = '4'
    MISSING1 = '-1'


ATQ21D1 = ATQ21A1


ATQ21D2 = ATQ21A1


ATQ21D3 = ATQ21A1


ATQ21D4 = ATQ21A1


ATQ21D5 = ATQ21A1


ATQ21D6 = ATQ21A1


ATQ21D7 = ATQ21A1


ATQ21D8 = ATQ21A1


class Q21E(OrderedEnum):
    CONTRIBUTORY_IE_BASED_ON_NATIONAL_INSURANCE = '1'
    INCOME_BASED_IE_BASED_ON_AN_ASSESSMENT_OF_INCOME = '2'
    DON_T_KNOW = '3'
    MISSING1 = '-1'


class Q21F(OrderedEnum):
    MATERNITY_ALLOWANCE = '1'
    STATUTORY_MATERNITY_PAY_FROM_EMPLOYER = '2'
    NEITHER_OF_THESE = '3'
    DON_T_KNOW = '4'
    REFUSE = '5'
    MISSING1 = '-1'


ATQ21H1 = ATQ21A1


ATQ21H2 = ATQ21A1


ATQ21H3 = ATQ21A1


ATQ21H4 = ATQ21A1


ATQ21H5 = ATQ21A1


ATQ21H6 = ATQ21A1


ATQ21H7 = ATQ21A1


ATQ21H8 = ATQ21A1


ATQ21H9 = ATQ21A1


ATQ21H10 = ATQ21A1


ATQ21H11 = ATQ21A1


ATQ21H12 = ATQ21A1


class Q21HA(OrderedEnum):
    WORKING_FAMILIES_TAX_CREDIT = '1'
    DISABLED_PERSON_S_TAX_CREDIT = '2'
    NONE_OF_THESE = '3'
    MISSING1 = '-1'


class Q21HB(OrderedEnum):
    WORKING_FAMILIES_TAX_CREDIT____LUMP_SUM_PAYMENT = '1'
    DISABLED_PERSON_S_TAX_CREDIT___LUMP_SUM_PAYMENT = '2'
    NONE_OF_THESE = '3'
    DON_T_KNOW = '4'
    MISSING1 = '-1'


ATQ21HC1 = ATQ21A1


ATQ21HC2 = ATQ21A1


ATQ21HC3 = ATQ21A1


ATQ21HC4 = ATQ21A1


ATQ21HC5 = ATQ21A1


Q22A = Q1A


ATQ22B1 = ATQ21A1


ATQ22B2 = ATQ21A1


ATQ22B3 = ATQ21A1


ATQ22B4 = ATQ21A1


ATQ22B5 = ATQ21A1


ATQ22B6 = ATQ21A1


ATQ22B7 = ATQ21A1


ATQ22B8 = ATQ21A1


ATQ22B9 = ATQ21A1


ATQ22B10 = ATQ21A1


ATQ22B11 = ATQ21A1


ATQ22B12 = ATQ21A1


ATQ22B13 = ATQ21A1


ATQ22B14 = ATQ21A1


ATQ22B15 = ATQ21A1


ATQ22B16 = ATQ21A1


ATQ22B17 = ATQ21A1


ATQ22B18 = ATQ21A1


ATQ22B19 = ATQ21A1


ATQ22B20 = ATQ21A1


ATQ22B21 = ATQ21A1


ATQ22B22 = ATQ21A1


ATQ22B23 = ATQ21A1


ATQ22B24 = ATQ21A1


ATQ22C1 = ATQ21A1


ATQ22C2 = ATQ21A1


ATQ22C3 = ATQ21A1


ATQ22C4 = ATQ21A1


ATQ22C5 = ATQ21A1


class Q22D(OrderedEnum):
    DOCTORATE = '1'
    MASTERS = '2'
    POSTGRADUATE_CERTIFICATE_IN_EDUCATION = '3'
    OTHER_POSTGRADUATE_DEGREE_OR_PROFESSIONAL_QUALIFICATION = '4'
    DON_T_KNOW = '5'
    MISSING1 = '-1'


class Q22E(OrderedEnum):
    HIGHER_LEVEL = '1'
    NATIONAL_CERTIFICATE_OR_NATIONAL_DIPLOMA_LEVEL = '2'
    FIRST_DIPLOMA_OR_GENERAL_DIPLOMA = '3'
    FIRST_CERTIFICATE_OR_GENERAL_CERTIFICATE = '4'
    DON_T_KNOW = '5'
    MISSING1 = '-1'


class Q22F(OrderedEnum):
    HIGHER_LEVEL = '1'
    FULL_NATIONAL_CERTIFICATE = '2'
    A_FIRST_DIPLOMA_OR_GENERAL_DIPLOMA = '3'
    A_FIRST_CERTIFICATE_OR_GENERAL_CERTIFICATE = '4'
    MODULES_TOWARDS_A_NATIONAL_CERTIFICATE = '5'
    DON_T_KNOW = '6'
    REFUSED = '7'
    MISSING1 = '-1'


ATQ22FI1 = ATQ21A1


ATQ22FI2 = ATQ21A1


ATQ22FI3 = ATQ21A1


ATQ22FI4 = ATQ21A1


ATQ22FI5 = ATQ21A1


class Q22G(OrderedEnum):
    ONE_A_LEVEL_OR_EQUIVALENT = '1'
    MORE_THAN_ONE = '2'
    DON_T_KNOW = '3'
    MISSING1 = '-1'


class Q22H(OrderedEnum):
    ONE_OR_TWO_SCE_HIGHERS = '1'
    THREE_OR_MORE_HIGHERS = '2'
    DON_T_KNOW = '3'
    MISSING1 = '-1'


class Q22I(OrderedEnum):
    LEVEL_1 = '1'
    LEVEL_2 = '2'
    LEVEL_3 = '3'
    LEVEL_4 = '4'
    LEVEL_5 = '5'
    DON_T_KNOW = '6'
    REFUSED = '7'
    MISSING1 = '-1'


class Q22J(OrderedEnum):
    ADVANCED_LEVEL = '1'
    INTERMEDIATE_LEVEL = '2'
    FOUNDATION_LEVEL = '3'
    DON_T_KNOW = '4'
    REFUSED = '5'
    MISSING1 = '-1'


class Q22K(OrderedEnum):
    ONE_AS_LEVEL = '1'
    TWO_OR_THREE_AS_LEVELS = '2'
    FOUR_OR_MORE = '3'
    MISSING1 = '-1'


class Q22L(OrderedEnum):
    A_HIGHER_DIPLOMA = '1'
    AN_ADVANCED_DIPLOMA_OR_ADVANCED_CERTIFICATE = '2'
    A_DIPLOMA = '3'
    OR_SOME_OTHER_RSA_INCLUDING_STAGE_I_II_AND_III = '4'
    DON_T_KNOW = '5'
    REFUSED = '6'
    MISSING1 = '-1'


class Q22M(OrderedEnum):
    ADVANCED_CRAFTPART_3 = '1'
    CRAFTPART_2 = '2'
    FOUNDATIONPART_1 = '3'
    DON_T_KNOW = '4'
    REFUSED = '5'
    MISSING1 = '-1'


class Q22N(OrderedEnum):
    YES = '1'
    NO = '2'
    DON_T_KNOW = '3'
    MISSING1 = '-1'


Q22O = Q22N


class Q22P(OrderedEnum):
    FEWER_THAN_5_PASSES = '1'
    N5_OR_MORE_PASSES = '2'
    DON_T_KNOW = '3'
    MISSING1 = '-1'


ATQ22Q1 = ATQ21A1


ATQ22Q2 = ATQ21A1


ATQ22Q3 = ATQ21A1


class Q22R(OrderedEnum):
    YES_COMPLETED = '1'
    YES_STILL_DOING = '2'
    NO_INCL_APPRENTICESHIPS_BEGUN_BUT_DISCOINTINUED = '3'
    MISSING1 = '-1'


Q23B = Q1A


ATQ23D1 = ATQ21A1


ATQ23D2 = ATQ21A1


ATQ23D3 = ATQ21A1


ATQ23D4 = ATQ21A1


ATQ23D5 = ATQ21A1


ATQ23D6 = ATQ21A1


ATQ23D7 = ATQ21A1


ATQ23D8 = ATQ21A1


ATQ23D9 = ATQ21A1


ATQ23D10 = ATQ21A1


ATQ23D11 = ATQ21A1


ATQ23D12 = ATQ21A1


ATQ23D13 = ATQ21A1


ATQ23D14 = ATQ21A1


ATQ23D15 = ATQ21A1


ATQ23D16 = ATQ21A1


ATQ23D17 = ATQ21A1


ATQ23D18 = ATQ21A1


ATQ23D19 = ATQ21A1


ATQ23D20 = ATQ21A1


ATQ23D21 = ATQ21A1


ATQ23D22 = ATQ21A1


ATQ23D23 = ATQ21A1


ATQ23D24 = ATQ21A1


ATQ23D25 = ATQ21A1


class Q23DI(OrderedEnum):
    HIGHER_DEGREE_INC__PGCE = '1'
    FIRST_DEGREE = '2'
    OTHER = '3'
    DON_T_KNOW = '4'
    REFUSED = '5'
    MISSING1 = '-1'


class Q23DII(OrderedEnum):
    A_DOCTORATE = '1'
    A_MASTERS = '2'
    A_PGCE = '3'
    OTHER = '4'
    DON_T_KNOW = '5'
    REFUSED = '6'
    MISSING1 = '-1'


class Q23E(OrderedEnum):
    AT_HIGHER_LEVEL = '1'
    NATIONAL_CERTIFICATEDIPLOMA = '2'
    FIRSTGENERAL_DIPLOMA = '3'
    FIRSTGENERAL_CERTIFICATE = '4'
    DON_T_KNOW = '5'
    REFUSED = '6'
    MISSING1 = '-1'


class Q23EI(OrderedEnum):
    AT_HIGHER_LEVEL = '1'
    FULL_NATIONAL_CERTIFICATE = '2'
    FIRSTGENERAL_DIPLOMA = '3'
    FIRSTGENERAL_CERTIFICATE = '4'
    MODULES_TOWARDS_NATIONAL_CERTIFICATE = '5'
    DON_T_KNOW = '6'
    REFUSED = '7'
    MISSING1 = '-1'


class Q23F(OrderedEnum):
    ADVANCED_CRAFTPART_3 = '1'
    CRAFTPART_2 = '2'
    FOUNDATIONPART_1 = '3'
    DON_T_KNOW = '4'
    REFUSED = '5'
    MISSING1 = '-1'


class Q23G(OrderedEnum):
    HIGHER_DIPLOMA_LEVEL = '1'
    ADVANCED_DIPLOMACERTIFICATE = '2'
    DIPLOMA_LEVEL = '3'
    SOME_OTHER_RSA_LEVEL = '4'
    DON_T_KNOW = '5'
    REFUSED = '6'
    MISSING1 = '-1'


class Q23H(OrderedEnum):
    LEVEL_1 = '1'
    LEVEL_2 = '2'
    LEVEL_3 = '3'
    LEVEL_4 = '4'
    LEVEL_5 = '5'
    LEVEL_6 = '6'
    UNITS_TOWARDS_NVQ__SVQ = '7'
    OTHER_NVQ = '8'
    DON_T_KNOW = '9'
    REFUSED = '10'
    MISSING1 = '-1'


class Q23I(OrderedEnum):
    ADVANCED_LEVEL = '1'
    INTERMEDIATE_LEVEL = '2'
    FOUNDATION_LEVEL = '3'
    DON_T_KNOW = '4'
    REFUSED = '5'
    MISSING1 = '-1'


class Q23J(OrderedEnum):
    UNIVERSITY__COLLEGE_OF_HIGHER_EDUCATION = '1'
    LOCAL_COLLEG_OF_FURTHER_EDUCATION = '2'
    SIXTH_FORM_COLLEGE_STATE_SYSTEM = '3'
    ADULT_EDUCATIONWEA_INSTITUTION = '4'
    COLLEGE_OR_UNIVERSITY___INDEPENDENT = '5'
    TRAINING_CENTRE_OR_COLLEGE_RUN_BY_EMPLYR = '6'
    TRAINING_CENTRE_PRIVATELY_RUN = '7'
    STATE_SCHOOL = '8'
    INDEPENDENT_SCHOOL = '9'
    OTHER = '10'
    DON_T_KNOW = '11'
    REFUSED = '12'
    MISSING1 = '-1'


ATQ24A1 = ATQ21A1


ATQ24A2 = ATQ21A1


ATQ24A3 = ATQ21A1


ATQ24A4 = ATQ21A1


ATQ24A5 = ATQ21A1


ATQ24A6 = ATQ21A1


ATQ24A7 = ATQ21A1


ATQ24A8 = ATQ21A1


ATQ24A9 = ATQ21A1


class Q24B(OrderedEnum):
    N1 = '1'
    N2 = '2'
    N3 = '3'
    N4 = '4'
    N5 = '5'
    N6 = '6'
    N7 = '7'
    N8 = '8'
    N9 = '9'
    MISSING1 = '-1'


class Q24CA(OrderedEnum):
    COMPUTER_PROGRAMMING = '1'
    KEYBOARD_PACKAGES = '2'
    USE_OF_THE_INTERNET = '3'
    OTHER_COMPUTING = '4'
    OFFICE_SKILLS = '5'
    MANAGEMENT_AND_ADMINISTRATION = '6'
    HEALTH_AND_SAFETY_COURSE = '7'
    FIRST_AID = '8'
    OTHER_OFFICIAL_REGULATIONS = '9'
    SELF_DEVELOPMENT = '10'
    COMMUNICATION_SKILLS = '11'
    BASIC_SKILLS = '12'
    USE_OF_SPECIFIC_EQUIPMENT = '13'
    FINANCE_AND_ACCOUNTANCY = '14'
    TEACHING_EDUCATION = '15'
    COUNSELLING = '16'
    CARE_AND_SOCIAL_SERVICE = '17'
    LEGAL_TRAINING = '18'
    NURSING = '19'
    MEDICAL_PARA_MEDICAL = '20'
    HOTEL_AND_CATERING = '21'
    BUILDING_AND_DECORATING = '22'
    SECURITY_TRADES = '23'
    ENGINEERING = '24'
    RETAIL = '25'
    OTHER_TRAINING = '26'
    ENGLISH_LANGUAGE_WRITING = '27'
    FOREIGN_LANGUAGES = '28'
    MATHS_AND_ARITHMETIC = '29'
    ENGLISH_LITERATURE_ART = '30'
    HISTORY_GEOGRAPHY_HUMANITIES = '31'
    SOCIAL_SCIENCES = '32'
    SCIENCES = '33'
    OTHER_ACADEMIC_SUBJECT = '34'
    DRIVING_LESSONS = '35'
    SPORT_PHYSICAL_ACTIVITY = '36'
    HANDICRAFTS_ARTS = '37'
    MUSIC_DRAMA = '38'
    OTHER_LEISURE_SKILLS = '39'
    OTHER_SUBJECT_LISTED = '40'
    ENGLISH_AS_A_SECOND_LANGUAGE = '41'
    ENGLISH_UNSPECIFIED = '42'
    IRRELEVANT_VAGUE_ANSWER = '43'
    DON_T_KNOW = '44'
    REFUSED = '45'
    MISSING1 = '-1'


Q24CB = Q24CA


Q24CC = Q24CA


Q24CD = Q24CA


Q24CE = Q24CA


Q24CF = Q24CA


Q24CG = Q24CA


Q24CH = Q24CA


Q24CI = Q24CA


class Q24DA(OrderedEnum):
    YES__WHOLE_OR_PART_OF_A_QUALIFICATION = '1'
    NO = '2'
    DON_T_KNOW = '3'
    MISSING1 = '-1'


Q24DB = Q24DA


Q24DC = Q24DA


Q24DD = Q24DA


Q24DE = Q24DA


Q24DF = Q24DA


Q24DG = Q24DA


Q24DH = Q24DA


Q24DI = Q24DA


ATQ24EA1 = ATQ21A1


ATQ24EA2 = ATQ21A1


ATQ24EA3 = ATQ21A1


ATQ24EA4 = ATQ21A1


ATQ24EA5 = ATQ21A1


ATQ24EA6 = ATQ21A1


ATQ24EA7 = ATQ21A1


ATQ24EA8 = ATQ21A1


ATQ24EA9 = ATQ21A1


ATQ24EA10 = ATQ21A1


ATQ24EA11 = ATQ21A1


ATQ24EA12 = ATQ21A1


ATQ24EA13 = ATQ21A1


ATQ24EA14 = ATQ21A1


ATQ24EA15 = ATQ21A1


ATQ24EA16 = ATQ21A1


ATQ24EA17 = ATQ21A1


ATQ24EA18 = ATQ21A1


ATQ24EA19 = ATQ21A1


ATQ24EA20 = ATQ21A1


ATQ24EA21 = ATQ21A1


ATQ24EA22 = ATQ21A1


ATQ24EA23 = ATQ21A1


ATQ24EB1 = ATQ21A1


ATQ24EB2 = ATQ21A1


ATQ24EB3 = ATQ21A1


ATQ24EB4 = ATQ21A1


ATQ24EB5 = ATQ21A1


ATQ24EB6 = ATQ21A1


ATQ24EB7 = ATQ21A1


ATQ24EB8 = ATQ21A1


ATQ24EB9 = ATQ21A1


ATQ24EB10 = ATQ21A1


ATQ24EB11 = ATQ21A1


ATQ24EB12 = ATQ21A1


ATQ24EB13 = ATQ21A1


ATQ24EB14 = ATQ21A1


ATQ24EB15 = ATQ21A1


ATQ24EB16 = ATQ21A1


ATQ24EB17 = ATQ21A1


ATQ24EB18 = ATQ21A1


ATQ24EB19 = ATQ21A1


ATQ24EB20 = ATQ21A1


ATQ24EB21 = ATQ21A1


ATQ24EB22 = ATQ21A1


ATQ24EB23 = ATQ21A1


class Q24EC(OrderedEnum):
    DEGREE = '1'
    DIPLOMA_IN_HIGHER_EDUCATION = '2'
    HNC_HND = '3'
    ONC_OND = '4'
    BTEC__BEC_OR_BEC = '5'
    SCOTVEC__SCOTEC_OR_SCOTBEC = '6'
    TEACHING_QUALIFICATION_EXCL_PGCE = '7'
    NURSING_OR_OTHER_MEDICAL_QUALIFICATION = '8'
    OTHER_HIGHER_EDUCATIONAL_QUALIFICATION = '9'
    A_LEVEL_OR_EQUIVALENT = '10'
    SCE_HIGHERS = '11'
    NVQ_SVQ = '12'
    GNVQ_GSVQ = '13'
    AS_LEVEL = '14'
    CERTIFICATE_OF_6TH_YEAR_STUDIES = '15'
    O_LEVEL_OR_EQUIVALENT = '16'
    SCE_STANDARD_ORDINARY_GRADE = '17'
    GCSE = '18'
    CSE = '19'
    RSA = '20'
    CITY_AND_GUILDS = '21'
    YT_CERTIFICATE = '22'
    ANY_OTHER_QUALIFICATIONS_PROFESS_NAL_VOCAT_NAL_FOREIGN = '23'
    MISSING1 = '-1'


Q24ED = Q24EC


Q24EE = Q24EC


Q24EF = Q24EC


Q24EG = Q24EC


Q24EH = Q24EC


Q24EI = Q24EC


class Q24FA(OrderedEnum):
    UNIVERSITY__POLYTECHNIC__COLLEGE_OF_HIGHER_EDUCATION = '1'
    FURTHER_EDUCATION_FE___TECHNICAL_COLLEGE = '2'
    NATIONAL_EXTENSION_COLLEGE = '3'
    RESIDENTIAL_TRAINING_COLLEGE = '4'
    MUSIC_COLLEGE__CLUB__CENTRE = '5'
    SCHOOL__SIXTH_FORM_COLLEGE = '6'
    BUSINESS_LINK_OR_TEC = '7'
    ADULT_EDUCATION_CENTRE_OR_EVENING_INSTITUTE = '8'
    PRIVATE_TRAINING_CENTRE__DAY_CENTRE = '9'
    LEARNING_RESOURCE_CENTRE = '10'
    OTHER_COLLEGE__TRAINING_CENTRE = '11'
    AT_YOUR_WORK = '12'
    SHELTERED_WORK_PLACEMENT = '13'
    EMPLOYER_S_TRAINING_CENTRE = '14'
    JOBCENTRE__JOBCLUB = '15'
    WORKERS__EDUCATIONAL_ASSOCIATION = '16'
    PRIVATE_TUITION_AT_RESPONDENT_S_HOME__AT_TEACHER_S_HOME = '17'
    COMMUNITY_CENTRE = '18'
    LEISURE_OR_SPORTS_CENTRE = '19'
    COMMUNITY_BUILDING__EG_CHURCH_HALL = '20'
    COMMUNITY_ORGANISATION = '21'
    RELIGIOUS_ORGANISATION = '22'
    WOMEN_S_INSTITUTETOWNSWOMEN_S_GUILD = '23'
    DISABILITY_ORGANISATION = '24'
    VOLUNTARY_GROUP = '25'
    OPEN_UNIVERSITY = '26'
    OTHER = '27'
    DON_T_KNOW = '28'
    NO_ANSWER = '29'
    MISSING1 = '-1'


class Q24FB(OrderedEnum):
    UNIVERSITY__POLYTECHNIC__COLLEGE_OF_HIGHER_EDUCATION = '1'
    FURTHER_EDUCATION_FE___TECHNICAL_COLLEGE = '2'
    NATIONAL_EXTENSION_COLLEGE = '3'
    RESIDENTIAL_TRAINING_COLLEGE = '4'
    MUSIC_COLLEGE__CLUB__CENTRE = '5'
    SCHOOL__SIXTH_FORM_COLLEGE = '6'
    BUSINESS_LINK_OR_TEC = '7'
    ADULT_EDUCATION_CENTRE_OR_EVENING_INSTITUTE = '8'
    PRIVATE_TRAINING_CENTRE__DAY_CENTRE = '9'
    LEARNING_RESOURCE_CENTRE = '10'
    OTHER_COLLEGE__TRAINING_CENTRE = '11'
    AT_YOUR_WORK = '12'
    SHELTERED_WORK_PLACEMENT = '13'
    EMPLOYER_S_TRAINING_CENTRE = '14'
    JOBCENTRE__JOBCLUB = '15'
    WORKERS__EDUCATIONAL_ASSOCIATION = '16'
    PRIVATE_TUITION_AT_RESPONDENT_S_HOME__AT_TEACHER_S_HOME = '17'
    COMMUNITY_CENTRE = '18'
    LEISURE_OR_SPORTS_CENTRE = '19'
    COMMUNITY_BUILDING__EG_CHURCH_HALL = '20'
    COMMUNITY_ORGANISATION = '21'
    RELIGIOUS_ORGANISATION = '22'
    WOMEN_S_INSTITUTETOWNSWOMEN_S_GUILD = '23'
    DISABILITY_ORGANISATION = '24'
    VOLUNTARY_GROUP = '25'
    OPEN_UNIVERSITY = '26'
    OTHER_SPECIFY = '27'
    DON_T_KNOW = '28'
    NO_ANSWER = '29'
    MISSING1 = '-1'


Q24FC = Q24FB


Q24FD = Q24FB


Q24FE = Q24FB


Q24FF = Q24FB


Q24FG = Q24FB


Q24FH = Q24FB


Q24FI = Q24FB


ATQ25A1 = ATQ21A1


ATQ25A2 = ATQ21A1


ATQ25A3 = ATQ21A1


ATQ25A4 = ATQ21A1


ATQ25A5 = ATQ21A1


ATQ25A6 = ATQ21A1


ATQ25A7 = ATQ21A1


class Q25B(OrderedEnum):
    N10_OR_MORE_HOURS = '1'
    FEWER_THAN_10_HOURS = '2'
    DON_T_KNOW = '3'
    MISSING1 = '-1'


class Q25C(OrderedEnum):
    ONE_OR_TWO_SEPARATE_DAYS_ = '1'
    THREE_OR_MORE_DAYS = '2'
    DON_T_KNOW = '3'
    REFUSED = '4'
    MISSING1 = '-1'


class Q25D(OrderedEnum):
    LESS_THAN_A_WEEK = '1'
    ONE_OR_TWO_WEEKS = '2'
    N3_OR_4_WEEKS = '3'
    N1___2_MONTHS = '4'
    N3___5_MONTHS = '5'
    N6___11_MONTHS = '6'
    N1___2_YEARS = '7'
    N3___5_YEARS = '8'
    N6___10_YEARS = '9'
    MORE_THAN_10_YEARS = '10'
    DON_T_KNOW = '11'
    REFUSED = '12'
    MISSING1 = '-1'


Q25E = Q3DWK


Q26A = Q1A


class Q26B1(OrderedEnum):
    PARENT_TEACHER_ASSOCIATION = '1'
    SCHOOL_GOVERNORS = '2'
    ANY_OTHER_SCHOOL_CONCERNED_VOLUNTEERING = '3'
    PRE_SCHOOL_PLAYGROUP = '4'
    OUTSIDE_SCHOOL_GROUP = '5'
    EDUCATION = '6'
    SPORTS_EXERCISE = '7'
    RELIGIOUS = '8'
    POLITICS = '9'
    BLOOD_DONATION = '10'
    LEAGUE_OF_HOSPITAL_FRIENDS_OR_SIMILAR_BODY = '11'
    OTHER_HOSPITAL_BASED_ACTIVITY = '12'
    NURSING_HOME = '13'
    MENTAL_HEALTH_AND_CRISIS_INTERVENTION = '14'
    MEDICAL_RESEARCH = '15'
    ANY_OTHER_HEALTH_RELATED_ACTIVITY = '16'
    ANY_OTHER_SOCIAL_CARE_RELATED_SERVICES = '17'
    ELDERLY = '18'
    SAFETY_FIRST_AID = '19'
    HOUSING = '20'
    ECONOMIC_DEVELOPMENT_TRAINING_OR_EMPLOYMENT = '21'
    ENVIRONMENT = '22'
    INTERNATIONAL_ACTIVITIES = '23'
    NON_STIPENDARY_MAGISTRACY = '24'
    OTHER_JUSTICE_AND_HUMAN_RIGHTS = '25'
    COMMUNITY_OR_NEIGHBOURHOOD_GROUP_NOT_ELSEWHERE_CLASSIFIED = '26'
    WOMENS_INSTITUTE_OR_TOWNSWOMENS_GUILD = '27'
    ROTARY_LIONS_ROUND_TABLE_INNER_WHEEL_ETC__ = '28'
    VOLUNTEER_BUREAU_COUNCIL_FOR_VOLUNTARY_SERVICE_ETC__ = '29'
    CULTURE_OR_ARTS_ORGANISATION = '30'
    PUBLIC_HOUSE = '31'
    LICENSED_SOCIAL_CLUB = '32'
    ANY_OTHER_RECREATION_OR_HOBBY_ACTIVITY = '33'
    ANIMALS = '34'
    GRANT_MAKING_TRUST = '35'
    WORK_EXTRA_TO_JOB = '36'
    GROUP_CONCERNED_WITH_PAID_EMPLOYMENT = '37'
    YOUTH_OR_CHILDRENS_ACTIVITY_USING_SCHOOL_FACILITIES = '38'
    IRRELEVANT_VAGUE_ANSWER = '39'
    OTHER = '40'
    DON_T_KNOW_NONE = '41'
    NOT_ANSWERED = '42'
    MISSING1 = '-1'


Q26B2 = Q26B1


Q26B3 = Q26B1


Q26B4 = Q26B1


Q26B5 = Q26B1


Q26B6 = Q26B1


ATQ26CA1 = ATQ21A1


ATQ26CA2 = ATQ21A1


ATQ26CA3 = ATQ21A1


ATQ26CA4 = ATQ21A1


ATQ26CA5 = ATQ21A1


ATQ26CA6 = ATQ21A1


ATQ26CA7 = ATQ21A1


ATQ26CA8 = ATQ21A1


ATQ26CA9 = ATQ21A1


ATQ26CA10 = ATQ21A1


ATQ26CA11 = ATQ21A1


ATQ26CA12 = ATQ21A1


ATQ26CA13 = ATQ21A1


ATQ26CA14 = ATQ21A1


ATQ26CA15 = ATQ21A1


ATQ26CA16 = ATQ21A1


ATQ26CB1 = ATQ21A1


ATQ26CB2 = ATQ21A1


ATQ26CB3 = ATQ21A1


ATQ26CB4 = ATQ21A1


ATQ26CB5 = ATQ21A1


ATQ26CB6 = ATQ21A1


ATQ26CB7 = ATQ21A1


ATQ26CB8 = ATQ21A1


ATQ26CB9 = ATQ21A1


ATQ26CB10 = ATQ21A1


ATQ26CB11 = ATQ21A1


ATQ26CB12 = ATQ21A1


ATQ26CB13 = ATQ21A1


ATQ26CB14 = ATQ21A1


ATQ26CB15 = ATQ21A1


ATQ26CB16 = ATQ21A1


ATQ26CC1 = ATQ21A1


ATQ26CC2 = ATQ21A1


ATQ26CC3 = ATQ21A1


ATQ26CC4 = ATQ21A1


ATQ26CC5 = ATQ21A1


ATQ26CC6 = ATQ21A1


ATQ26CC7 = ATQ21A1


ATQ26CC8 = ATQ21A1


ATQ26CC9 = ATQ21A1


ATQ26CC10 = ATQ21A1


ATQ26CC11 = ATQ21A1


ATQ26CC12 = ATQ21A1


ATQ26CC13 = ATQ21A1


ATQ26CC14 = ATQ21A1


ATQ26CC15 = ATQ21A1


ATQ26CC16 = ATQ21A1


ATQ26CD1 = ATQ21A1


ATQ26CD2 = ATQ21A1


ATQ26CD3 = ATQ21A1


ATQ26CD4 = ATQ21A1


ATQ26CD5 = ATQ21A1


ATQ26CD6 = ATQ21A1


ATQ26CD7 = ATQ21A1


ATQ26CD8 = ATQ21A1


ATQ26CD9 = ATQ21A1


ATQ26CD10 = ATQ21A1


ATQ26CD11 = ATQ21A1


ATQ26CD12 = ATQ21A1


ATQ26CD13 = ATQ21A1


ATQ26CD14 = ATQ21A1


ATQ26CD15 = ATQ21A1


ATQ26CD16 = ATQ21A1


ATQ26CE1 = ATQ21A1


ATQ26CE2 = ATQ21A1


ATQ26CE3 = ATQ21A1


ATQ26CE4 = ATQ21A1


ATQ26CE5 = ATQ21A1


ATQ26CE6 = ATQ21A1


ATQ26CE7 = ATQ21A1


ATQ26CE8 = ATQ21A1


ATQ26CE9 = ATQ21A1


ATQ26CE10 = ATQ21A1


ATQ26CE11 = ATQ21A1


ATQ26CE12 = ATQ21A1


ATQ26CE13 = ATQ21A1


ATQ26CE14 = ATQ21A1


ATQ26CE15 = ATQ21A1


ATQ26CE16 = ATQ21A1


ATQ26CF1 = ATQ21A1


ATQ26CF2 = ATQ21A1


ATQ26CF3 = ATQ21A1


ATQ26CF4 = ATQ21A1


ATQ26CF5 = ATQ21A1


ATQ26CF6 = ATQ21A1


ATQ26CF7 = ATQ21A1


ATQ26CF8 = ATQ21A1


ATQ26CF9 = ATQ21A1


ATQ26CF10 = ATQ21A1


ATQ26CF11 = ATQ21A1


ATQ26CF12 = ATQ21A1


ATQ26CF13 = ATQ21A1


ATQ26CF14 = ATQ21A1


ATQ26CF15 = ATQ21A1


ATQ26CF16 = ATQ21A1


Q27A = Q18A


class Q27B1(OrderedEnum):
    SPOUSE_PARTNER = '1'
    CHILDREN = '2'
    PARENTS = '3'
    BROTHER_SISTER = '4'
    GRANDPARENTS = '5'
    GRANDCHILDREN = '6'
    OTHER_FAMILY_MEMBER = '7'
    FRIENDS = '8'
    NEIGHBOURS = '9'
    COLLEAGUES = '10'
    UNSPECIFIED_PERSON = '11'
    WINDOW_CLEANERS = '12'
    DOMESTIC_SERVICES = '13'
    GARAGE_SERVICES = '14'
    CHILD_CARE = '15'
    MEDICAL_SERVICES = '16'
    HEALTH_LIFESTYLE_SERVICES = '17'
    OTHER_CARE_SERVICES = '18'
    BUILDING_SERVICES = '19'
    RETAIL_SERVICES = '20'
    FINANCIAL_LEGAL_SERVICES = '21'
    PET_SERVICES = '22'
    IRRELEVANT_OR_VAGUE_ANSWER = '23'
    OTHER = '24'
    DON_T_KNOW_NONE = '25'
    NO_ANSWER = '26'
    MISSING1 = '-1'


Q27B2 = Q27B1


Q27B3 = Q27B1


Q27B4 = Q27B1


Q27B5 = Q27B1


Q27B6 = Q27B1


Q27B7 = Q27B1


Q27B8 = Q27B1


ATQ27CA1 = ATQ21A1


ATQ27CA2 = ATQ21A1


ATQ27CA3 = ATQ21A1


ATQ27CA4 = ATQ21A1


ATQ27CA5 = ATQ21A1


ATQ27CA6 = ATQ21A1


ATQ27CA7 = ATQ21A1


ATQ27CA8 = ATQ21A1


ATQ27CA9 = ATQ21A1


ATQ27CA10 = ATQ21A1


ATQ27CA11 = ATQ21A1


ATQ27CA12 = ATQ21A1


ATQ27CA13 = ATQ21A1


ATQ27CA14 = ATQ21A1


ATQ27CA15 = ATQ21A1


ATQ27CA16 = ATQ21A1


ATQ27CA17 = ATQ21A1


ATQ27CA18 = ATQ21A1


ATQ27CA19 = ATQ21A1


ATQ27CA20 = ATQ21A1


ATQ27CA21 = ATQ21A1


ATQ27CA22 = ATQ21A1


ATQ27CA23 = ATQ21A1


ATQ27CA24 = ATQ21A1


ATQ27CA25 = ATQ21A1


ATQ27CA26 = ATQ21A1


ATQ27CA27 = ATQ21A1


ATQ27CA28 = ATQ21A1


ATQ27CA29 = ATQ21A1


ATQ27CA30 = ATQ21A1


ATQ27CA31 = ATQ21A1


ATQ27CA32 = ATQ21A1


ATQ27CA33 = ATQ21A1


ATQ27CA34 = ATQ21A1


ATQ27CA35 = ATQ21A1


ATQ27CA36 = ATQ21A1


ATQ27CB1 = ATQ21A1


ATQ27CB2 = ATQ21A1


ATQ27CB3 = ATQ21A1


ATQ27CB4 = ATQ21A1


ATQ27CB5 = ATQ21A1


ATQ27CB6 = ATQ21A1


ATQ27CB7 = ATQ21A1


ATQ27CB8 = ATQ21A1


ATQ27CB9 = ATQ21A1


ATQ27CB10 = ATQ21A1


ATQ27CB11 = ATQ21A1


ATQ27CB12 = ATQ21A1


ATQ27CB13 = ATQ21A1


ATQ27CB14 = ATQ21A1


ATQ27CB15 = ATQ21A1


ATQ27CB16 = ATQ21A1


ATQ27CB17 = ATQ21A1


ATQ27CB18 = ATQ21A1


ATQ27CB19 = ATQ21A1


ATQ27CB20 = ATQ21A1


ATQ27CB21 = ATQ21A1


ATQ27CB22 = ATQ21A1


ATQ27CB23 = ATQ21A1


ATQ27CB24 = ATQ21A1


ATQ27CB25 = ATQ21A1


ATQ27CB26 = ATQ21A1


ATQ27CB27 = ATQ21A1


ATQ27CB28 = ATQ21A1


ATQ27CB29 = ATQ21A1


ATQ27CB30 = ATQ21A1


ATQ27CB31 = ATQ21A1


ATQ27CB32 = ATQ21A1


ATQ27CB33 = ATQ21A1


ATQ27CB34 = ATQ21A1


ATQ27CB35 = ATQ21A1


ATQ27CB36 = ATQ21A1


ATQ27CC1 = ATQ21A1


ATQ27CC2 = ATQ21A1


ATQ27CC3 = ATQ21A1


ATQ27CC4 = ATQ21A1


ATQ27CC5 = ATQ21A1


ATQ27CC6 = ATQ21A1


ATQ27CC7 = ATQ21A1


ATQ27CC8 = ATQ21A1


ATQ27CC9 = ATQ21A1


ATQ27CC10 = ATQ21A1


ATQ27CC11 = ATQ21A1


ATQ27CC12 = ATQ21A1


ATQ27CC13 = ATQ21A1


ATQ27CC14 = ATQ21A1


ATQ27CC15 = ATQ21A1


ATQ27CC16 = ATQ21A1


ATQ27CC17 = ATQ21A1


ATQ27CC18 = ATQ21A1


ATQ27CC19 = ATQ21A1


ATQ27CC20 = ATQ21A1


ATQ27CC21 = ATQ21A1


ATQ27CC22 = ATQ21A1


ATQ27CC23 = ATQ21A1


ATQ27CC24 = ATQ21A1


ATQ27CC25 = ATQ21A1


ATQ27CC26 = ATQ21A1


ATQ27CC27 = ATQ21A1


ATQ27CC28 = ATQ21A1


ATQ27CC29 = ATQ21A1


ATQ27CC30 = ATQ21A1


ATQ27CC31 = ATQ21A1


ATQ27CC32 = ATQ21A1


ATQ27CC33 = ATQ21A1


ATQ27CC34 = ATQ21A1


ATQ27CC35 = ATQ21A1


ATQ27CC36 = ATQ21A1


ATQ27CD1 = ATQ21A1


ATQ27CD2 = ATQ21A1


ATQ27CD3 = ATQ21A1


ATQ27CD4 = ATQ21A1


ATQ27CD5 = ATQ21A1


ATQ27CD6 = ATQ21A1


ATQ27CD7 = ATQ21A1


ATQ27CD8 = ATQ21A1


ATQ27CD9 = ATQ21A1


ATQ27CD10 = ATQ21A1


ATQ27CD11 = ATQ21A1


ATQ27CD12 = ATQ21A1


ATQ27CD13 = ATQ21A1


ATQ27CD14 = ATQ21A1


ATQ27CD15 = ATQ21A1


ATQ27CD16 = ATQ21A1


ATQ27CD17 = ATQ21A1


ATQ27CD18 = ATQ21A1


ATQ27CD19 = ATQ21A1


ATQ27CD20 = ATQ21A1


ATQ27CD21 = ATQ21A1


ATQ27CD22 = ATQ21A1


ATQ27CD23 = ATQ21A1


ATQ27CD24 = ATQ21A1


ATQ27CD25 = ATQ21A1


ATQ27CD26 = ATQ21A1


ATQ27CD27 = ATQ21A1


ATQ27CD28 = ATQ21A1


ATQ27CD29 = ATQ21A1


ATQ27CD30 = ATQ21A1


ATQ27CD31 = ATQ21A1


ATQ27CD32 = ATQ21A1


ATQ27CD33 = ATQ21A1


ATQ27CD34 = ATQ21A1


ATQ27CD35 = ATQ21A1


ATQ27CD36 = ATQ21A1


ATQ27CE1 = ATQ21A1


ATQ27CE2 = ATQ21A1


ATQ27CE3 = ATQ21A1


ATQ27CE4 = ATQ21A1


ATQ27CE5 = ATQ21A1


ATQ27CE6 = ATQ21A1


ATQ27CE7 = ATQ21A1


ATQ27CE8 = ATQ21A1


ATQ27CE9 = ATQ21A1


ATQ27CE10 = ATQ21A1


ATQ27CE11 = ATQ21A1


ATQ27CE12 = ATQ21A1


ATQ27CE13 = ATQ21A1


ATQ27CE14 = ATQ21A1


ATQ27CE15 = ATQ21A1


ATQ27CE16 = ATQ21A1


ATQ27CE17 = ATQ21A1


ATQ27CE18 = ATQ21A1


ATQ27CE19 = ATQ21A1


ATQ27CE20 = ATQ21A1


ATQ27CE21 = ATQ21A1


ATQ27CE22 = ATQ21A1


ATQ27CE23 = ATQ21A1


ATQ27CE24 = ATQ21A1


ATQ27CE25 = ATQ21A1


ATQ27CE26 = ATQ21A1


ATQ27CE27 = ATQ21A1


ATQ27CE28 = ATQ21A1


ATQ27CE29 = ATQ21A1


ATQ27CE30 = ATQ21A1


ATQ27CE31 = ATQ21A1


ATQ27CE32 = ATQ21A1


ATQ27CE33 = ATQ21A1


ATQ27CE34 = ATQ21A1


ATQ27CE35 = ATQ21A1


ATQ27CE36 = ATQ21A1


ATQ27CF1 = ATQ21A1


ATQ27CF2 = ATQ21A1


ATQ27CF3 = ATQ21A1


ATQ27CF4 = ATQ21A1


ATQ27CF5 = ATQ21A1


ATQ27CF6 = ATQ21A1


ATQ27CF7 = ATQ21A1


ATQ27CF8 = ATQ21A1


ATQ27CF9 = ATQ21A1


ATQ27CF10 = ATQ21A1


ATQ27CF11 = ATQ21A1


ATQ27CF12 = ATQ21A1


ATQ27CF13 = ATQ21A1


ATQ27CF14 = ATQ21A1


ATQ27CF15 = ATQ21A1


ATQ27CF16 = ATQ21A1


ATQ27CF17 = ATQ21A1


ATQ27CF18 = ATQ21A1


ATQ27CF19 = ATQ21A1


ATQ27CF20 = ATQ21A1


ATQ27CF21 = ATQ21A1


ATQ27CF22 = ATQ21A1


ATQ27CF23 = ATQ21A1


ATQ27CF24 = ATQ21A1


ATQ27CF25 = ATQ21A1


ATQ27CF26 = ATQ21A1


ATQ27CF27 = ATQ21A1


ATQ27CF28 = ATQ21A1


ATQ27CF29 = ATQ21A1


ATQ27CF30 = ATQ21A1


ATQ27CF31 = ATQ21A1


ATQ27CF32 = ATQ21A1


ATQ27CF33 = ATQ21A1


ATQ27CF34 = ATQ21A1


ATQ27CF35 = ATQ21A1


ATQ27CF36 = ATQ21A1


ATQ27CG1 = ATQ21A1


ATQ27CG2 = ATQ21A1


ATQ27CG3 = ATQ21A1


ATQ27CG4 = ATQ21A1


ATQ27CG5 = ATQ21A1


ATQ27CG6 = ATQ21A1


ATQ27CG7 = ATQ21A1


ATQ27CG8 = ATQ21A1


ATQ27CG9 = ATQ21A1


ATQ27CG10 = ATQ21A1


ATQ27CG11 = ATQ21A1


ATQ27CG12 = ATQ21A1


ATQ27CG13 = ATQ21A1


ATQ27CG14 = ATQ21A1


ATQ27CG15 = ATQ21A1


ATQ27CG16 = ATQ21A1


ATQ27CG17 = ATQ21A1


ATQ27CG18 = ATQ21A1


ATQ27CG19 = ATQ21A1


ATQ27CG20 = ATQ21A1


ATQ27CG21 = ATQ21A1


ATQ27CG22 = ATQ21A1


ATQ27CG23 = ATQ21A1


ATQ27CG24 = ATQ21A1


ATQ27CG25 = ATQ21A1


ATQ27CG26 = ATQ21A1


ATQ27CG27 = ATQ21A1


ATQ27CG28 = ATQ21A1


ATQ27CG29 = ATQ21A1


ATQ27CG30 = ATQ21A1


ATQ27CG31 = ATQ21A1


ATQ27CG32 = ATQ21A1


ATQ27CG33 = ATQ21A1


ATQ27CG34 = ATQ21A1


ATQ27CG35 = ATQ21A1


ATQ27CG36 = ATQ21A1


ATQ27CH1 = ATQ21A1


ATQ27CH2 = ATQ21A1


ATQ27CH3 = ATQ21A1


ATQ27CH4 = ATQ21A1


ATQ27CH5 = ATQ21A1


ATQ27CH6 = ATQ21A1


ATQ27CH7 = ATQ21A1


ATQ27CH8 = ATQ21A1


ATQ27CH9 = ATQ21A1


ATQ27CH10 = ATQ21A1


ATQ27CH11 = ATQ21A1


ATQ27CH12 = ATQ21A1


ATQ27CH13 = ATQ21A1


ATQ27CH14 = ATQ21A1


ATQ27CH15 = ATQ21A1


ATQ27CH16 = ATQ21A1


ATQ27CH17 = ATQ21A1


ATQ27CH18 = ATQ21A1


ATQ27CH19 = ATQ21A1


ATQ27CH20 = ATQ21A1


ATQ27CH21 = ATQ21A1


ATQ27CH22 = ATQ21A1


ATQ27CH23 = ATQ21A1


ATQ27CH24 = ATQ21A1


ATQ27CH25 = ATQ21A1


ATQ27CH26 = ATQ21A1


ATQ27CH27 = ATQ21A1


ATQ27CH28 = ATQ21A1


ATQ27CH29 = ATQ21A1


ATQ27CH30 = ATQ21A1


ATQ27CH31 = ATQ21A1


ATQ27CH32 = ATQ21A1


ATQ27CH33 = ATQ21A1


ATQ27CH34 = ATQ21A1


ATQ27CH35 = ATQ21A1


ATQ27CH36 = ATQ21A1


Q27FA = Q1A


Q27FB = Q1A


Q27FC = Q1A


Q27FD = Q1A


Q27FE = Q1A


Q27FF = Q1A


Q27FG = Q1A


Q27FH = Q1A


class Q28A(OrderedEnum):
    PROXY_INTERVIEW___NOT_ASKED = '-2'
    LIKE_A_LOT = '1'
    LIKE_A_LITTLE = '2'
    NEITHER_LIKE_OR_DISLIKE = '3'
    DISLIKE_A_LITTLE = '4'
    DISLIKE_A_LOT = '5'
    DO_NOT_DO_ACTIVITY = '6'
    DON_T_KNOW = '7'
    MISSING1 = '-1'


Q28B = Q28A


Q28C = Q28A


Q28D = Q28A


Q28E = Q28A


Q28F = Q28A


Q28G = Q28A


Q28H = Q28A


Q28I = Q28A


Q28J = Q28A


Q28K = Q28A


Q28L = Q28A


Q28M = Q28A


Q28N = Q28A


Q28O = Q28A


Q28P = Q28A


Q28Q = Q28A


class Q29A(OrderedEnum):
    PROXY_INTERVIEW___NOT_ASKED = '-2'
    YES = '1'
    NO = '2'
    MISSING1 = '-1'


Q29B = Q29A


Q29C = Q29A


Q29D = Q29A


Q29E = Q29A


Q29F = Q29A


Q29G = Q29A


Q29H = Q29A


Q29I = Q29A


Q29J = Q29A


Q29K = Q29A


Q29L = Q29A


Q29M = Q29A


Q29N = Q29A


Q29O = Q29A


Q29P = Q29A


Q29Q = Q29A


Q29R = Q29A


Q29S = Q29A


class Q31A01(OrderedEnum):
    PROXY_INTERVIEW___NOT_ASKED = '-2'
    YES = '1'
    NO = '2'
    MISSING1 = '-1'


Q31A02 = Q31A01


Q31A03 = Q31A01


Q31A04 = Q31A01


Q31A05 = Q31A01


Q31A06 = Q31A01


Q31A07 = Q31A01


Q31A08 = Q31A01


Q31A09 = Q31A01


Q31A10 = Q31A01


Q31A11 = Q31A01


Q31A12 = Q31A01


Q31A13 = Q31A01


Q31A14 = Q31A01


Q31A15 = Q31A01


Q31A16 = Q31A01


Q31A17 = Q31A01


Q31A18 = Q31A01


Q31A19 = Q31A01


Q31A20 = Q31A01


Q31A21 = Q31A01


Q31A22 = Q31A01


Q31A23 = Q31A01


Q31A24 = Q31A01


Q31A25 = Q31A01


Q31A26 = Q31A01


Q31A27 = Q31A01


Q31A28 = Q31A01


Q31A29 = Q31A01


Q31A30 = Q31A01


Q31A31 = Q31A01


Q31A32 = Q31A01


Q31A33 = Q31A01


Q31A34 = Q31A01


Q31A35 = Q31A01


Q31A36 = Q31A01


Q31A37 = Q31A01


Q31A38 = Q31A01


Q31A39 = Q31A01


Q31A40 = Q31A01


Q31A41 = Q31A01


Q31A42 = Q31A01


Q31A43 = Q31A01


Q31A44 = Q31A01


Q31A45 = Q31A01


Q31A46 = Q31A01


Q32A = Q18A


class Q32B(OrderedEnum):
    PURCHASED_BY_RESPONDENT = '1'
    PURCHASED_BY_SOMEONE_ELSE = '2'
    DON_T_KNOW = '3'
    REFUSED = '4'
    MISSING1 = '-1'


class Q32C(OrderedEnum):
    JUST_FOR_SELF = '1'
    JUST_WITH_OTHERS = '2'
    BOTH = '3'
    DON_T_KNOW = '4'
    REFUSED = '5'
    MISSING1 = '-1'


class Q32D(OrderedEnum):
    OTHER_HOUSEHOLD_MEMBERS = '1'
    PEOPLE_OUTSIDE_HOUSEHOLD = '2'
    BOTH_HOUSEHOLD_MEMBERS_AND_OTHERS = '3'
    DON_T_KNOW = '4'
    REFUSED = '5'
    MISSING1 = '-1'


class Q33(OrderedEnum):
    ALL_THE_TIME = '1'
    SOME_OF_THE_TIME = '2'
    RARELY = '3'
    NEVER = '4'
    DON_T_KNOW = '5'
    REFUSED = '6'
    MISSING1 = '-1'


class Q34A(OrderedEnum):
    VERY_GOOD = '1'
    GOOD = '2'
    FAIR = '3'
    BAD = '4'
    OR_VERY_BAD = '5'
    DON_T_KNOW = '6'
    REFUSED = '7'
    MISSING1 = '-1'


Q34B = Q1A


class Q34C(OrderedEnum):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    ELEVEN = '11'
    TWELVE = '12'
    THIRTEEN = '13'
    FOURTEEN = '14'
    DON_T_KNOW = '15'
    REFUSED = '16'
    MISSING1 = '-1'
    MISSING2 = '-7'
    MISSING3 = '-8'


Q35A = Q1A


Q35B = Q1A


Q35C = Q1A


Q35D01 = Q1A


Q35D02 = Q1A


Q35D03 = Q1A


Q35D04 = Q1A


Q35D05 = Q1A


Q35D06 = Q1A


Q35D07 = Q1A


Q35D08 = Q1A


Q35D09 = Q1A


Q35D10 = Q1A


Q35D11 = Q1A


Q35D12 = Q1A


Q35D13 = Q1A


Q35D14 = Q1A


Q35D15 = Q1A


Q35D16 = Q1A


Q35D17 = Q1A


ATQ35DC1 = ATQ21A1


ATQ35DC2 = ATQ21A1


ATQ35DC3 = ATQ21A1


ATQ35DC4 = ATQ21A1


ATQ35DC5 = ATQ21A1


ATQ35DC6 = ATQ21A1


ATQ35DC7 = ATQ21A1


ATQ35DC8 = ATQ21A1


ATQ35DC9 = ATQ21A1


ATQ35DC10 = ATQ21A1


ATQ35DC11 = ATQ21A1


ATQ35DC12 = ATQ21A1


ATQ35DC13 = ATQ21A1


ATQ35DC14 = ATQ21A1


ATQ35DC15 = ATQ21A1


ATQ35DC16 = ATQ21A1


ATQ35DC17 = ATQ21A1


ATQ35DC18 = ATQ21A1


ATQ35DC19 = ATQ21A1


ATQ35DC20 = ATQ21A1


ATQ35DC21 = ATQ21A1


class Q35E(OrderedEnum):
    CONNECTED_WITH_ARMS_OR_HANDS = '1'
    CONNECTED_WITH_LEGS_OR_FEET = '2'
    CONNECTED_WITH_BACK_OR_NECK = '3'
    DIFFICULTY_IN_SEEING = '4'
    DIFFICULTY_IN_HEARING = '5'
    A_SPEECH_IMPEDIMENT = '6'
    SEVERE_DISFIGUREMENT__SKIN_CONDITIONS__ALLERGIES = '7'
    CHEST_OR_BREATHING_PROBLEMS__ASTHMA__BRONCHITIS = '8'
    HEART__BLOOD_PRESSURE_OR_BLOOD_CIRCULATION_PROBLEMS = '9'
    STOMACH__LIVER__KIDNEY_OR_DIGESTIVE_PROBLEMS = '10'
    DIABETES = '11'
    DEPRESSION__BAD_NERVES_OR_ANXIETY = '12'
    EPILEPSY = '13'
    SEVERE_OR_SPECIFIC_LEARNING_DIFFICULTIES = '14'
    MENTAL_ILLNESS_OR_NERVOUS_DISORDERS = '15'
    PROGRESSIVE_ILLNESS = '16'
    OTHER_HEALTH_PROBLEMS_OR_DISABILITIES = '17'
    DON_T_KNOW = '18'
    REFUSED = '19'
    MISSING1 = '-1'


Q35F = Q1A


class Q36A(OrderedEnum):
    PROXY_INTERVIEW___NOT_ASKED = '-2'
    ALWAYS_FEEL_RUSHED = '1'
    ONLY_SOMETIMES_FEEL_RUSHED = '2'
    ALMOST_NEVER_FEEL_RUSHED = '3'
    DON_T_KNOW = '4'
    MISSING1 = '-1'


class Q36B(OrderedEnum):
    SLEEP = '1'
    EATING = '2'
    OTHER_PERSONAL_CARE = '3'
    MAIN_JOB = '4'
    SECOND_JOB = '5'
    ACTIVITIES_RELATED_TO_EMPLOYMENT = '6'
    SCHOOL_OR_UNIVERSITY = '7'
    FREE_TIME_STUDY = '8'
    FOOD_MANAGEMENT = '9'
    HOUSEHOLD_UPKEEP = '10'
    MAKING_AND_CARE_FOR_TEXTILES = '11'
    GARDENING_AND_PET_CARE = '12'
    CONSTRUCTION_AND_REPAIR = '13'
    SHOPPING_AND_SERVICES = '14'
    HOUSEHOLD_MANAGEMENT = '15'
    CHILDCARE_OWN_HHLD_MEMBERS = '16'
    HELP_TO_AN_ADULT_FAMILY_MEMBER = '17'
    ORGANISATIONAL_WORK = '18'
    INFORMAL_HELP_TO_OTHER_HOUSEHOLDS = '19'
    PARTICIPATORY_ACTIVITIES = '20'
    SOCIAL_LIFE = '21'
    ENTERTAINMENT_AND_CULTURE = '22'
    RESTING_TIME_OUT = '23'
    PHYSICAL_EXERCISE = '24'
    PRODUCTIVE_EXERCISE = '25'
    SPORTS_RELATED_ACTIVITIES = '26'
    ARTS = '27'
    HOBBIES = '28'
    GAMES = '29'
    READING = '30'
    TV_VIDEO = '31'
    RADIO_AND_MUSIC = '32'
    TRAVEL = '33'
    OTHER = '34'
    DON_T_KNOW_NONE = '35'
    NO_ANSWER = '36'
    DON_T_KNOW = '37'
    MISSING1 = '-1'


Q38A = Q3DWK


Q38B = Q3DWK


Q38C = Q3DWK


Q38D = Q3DWK


Q38E = Q3DWK


Q38F = Q3DWK


Q38G = Q3DWK


Q38H = Q3DWK


Q38I = Q3DWK


Q38J = Q3DWK


class Q38AA(OrderedEnum):
    NURSERY_CLASS = '1'
    RECEPTION_CLASS = '2'
    YEAR_ONE_OR_ABOVE = '3'
    DON_T_KNOW = '4'
    REFUSED = '5'
    MISSING1 = '-1'


Q38AB = Q38AA


Q38AC = Q38AA


Q38AD = Q38AA


Q38AE = Q38AA


Q38AF = Q38AA


Q38AG = Q38AA


Q38AH = Q38AA


Q38AI = Q38AA


Q38AJ = Q38AA


class Q39A01(OrderedEnum):
    YES___CHILDMINDER = '1'
    NO___CHILDMINDER = '2'
    MISSING1 = '-1'


class Q39A02(OrderedEnum):
    YES___DAILY_NANNY_WHO_CAME_TO_OUR_HOME = '1'
    NO___DAILY_NANNY_WHO_CAME_TO_OUR_HOME = '2'
    MISSING1 = '-1'


class Q39A03(OrderedEnum):
    YES___LIVE_IN_NANNY_OR_AU_PAIR = '1'
    NO___LIVE_IN_NANNY_OR_AU_PAIR = '2'
    MISSING1 = '-1'


class Q39A04(OrderedEnum):
    YES___BABY_SITTER_WHO_CAME_TO_OUR_HOME = '1'
    NO___BABY_SITTER_WHO_CAME_TO_OUR_HOME = '2'
    MISSING1 = '-1'


class Q39A05(OrderedEnum):
    YES___LOCAL_AUTHORITY_CRECHE_OR_NURSERY_SCHOOL = '1'
    NO___LOCAL_AUTHORITY_CRECHE_OR_NURSERY_SCHOOL = '2'
    MISSING1 = '-1'


class Q39A06(OrderedEnum):
    YES___PRIVATE_CRECHE_OR_NURSERY_SCHOOL = '1'
    NO___PRIVATE_CRECHE_OR_NURSERY_SCHOOL = '2'
    MISSING1 = '-1'


class Q39A07(OrderedEnum):
    YES___WORK_PLACE_CRECHE_OR_NURSERY = '1'
    NO___WORK_PLACE_CRECHE_OR_NURSERY = '2'
    MISSING1 = '-1'


class Q39A08(OrderedEnum):
    YES___LOCAL_AUTHORITY_PLAY_GROUP_OR_PRE_SCHOOL = '1'
    NO___LOCAL_AUTHORITY_PLAY_GROUP_OR_PRE_SCHOOL = '2'
    MISSING1 = '-1'


class Q39A09(OrderedEnum):
    YES___PRIVATE_PLAY_GROUP_OR_PRE_SCHOOL = '1'
    NO___PRIVATE_PLAY_GROUP_OR_PRE_SCHOOL = '2'
    MISSING1 = '-1'


class Q39A10(OrderedEnum):
    YES___COMMUNITY_OR_VOLUNTARY_PLAY_GROUP_OR_PRE_SCHOOL = '1'
    NO___COMMUNITY_OR_VOLUNTARY_PLAY_GROUP_OR_PRE_SCHOOL = '2'
    MISSING1 = '-1'


class Q39A11(OrderedEnum):
    YES___NURSERY_CLASS_ATTACHED_TO_A_PRIMARY_SCHOOL = '1'
    NO___NURSERY_CLASS_ATTACHED_TO_A_PRIMARY_SCHOOL = '2'
    MISSING1 = '-1'


class Q39A12(OrderedEnum):
    YES___RECEPTION_CLASS_ATTACHED_TO_A_PRIMARY_SCHOOL = '1'
    NO___RECEPTION_CLASS_ATTACHED_TO_A_PRIMARY_SCHOOL = '2'
    MISSING1 = '-1'


class Q39A13(OrderedEnum):
    YES___FAMILY_CENTRE = '1'
    NO___FAMILY_CENTRE = '2'
    MISSING1 = '-1'


class Q39A14(OrderedEnum):
    YES___TERM_TIME_OUT_OF_SCHOOL_CLUB = '1'
    NO___TERM_TIME_OUT_OF_SCHOOL_CLUB = '2'
    MISSING1 = '-1'


class Q39A15(OrderedEnum):
    YES___HOLIDAY_SCHEME_OR_PLAY_SCHEME = '1'
    NO___HOLIDAY_SCHEME_OR_PLAY_SCHEME = '2'
    MISSING1 = '-1'


class Q39A16(OrderedEnum):
    YES___EX_SPOUSE_OR_PARTNER = '1'
    NO___EX_SPOUSE_OR_PARTNER = '2'
    MISSING1 = '-1'


class Q39A17(OrderedEnum):
    YES___THE_CHILD_S_GRANDPARENT = '1'
    NO___THE_CHILD_S_GRANDPARENT = '2'
    MISSING1 = '-1'


class Q39A18(OrderedEnum):
    YES___THE_CHILD_S_OLDER_BROTHER_OR_SISTER = '1'
    NO___THE_CHILD_S_OLDER_BROTHER_OR_SISTER = '2'
    MISSING1 = '-1'


class Q39A19(OrderedEnum):
    YES___ANOTHER_RELATIVE = '1'
    NO___ANOTHER_RELATIVE = '2'
    MISSING1 = '-1'


class Q39A20(OrderedEnum):
    YES___FRIENDS_OR_NEIGHBOURS = '1'
    NO___FRIENDS_OR_NEIGHBOURS = '2'
    MISSING1 = '-1'


class Q39A21(OrderedEnum):
    YES___OTHER_SPECIFY = '1'
    NO___OTHER_SPECIFY = '2'
    MISSING1 = '-1'


class Q39A22(OrderedEnum):
    YES___NONE = '1'
    NO___NONE = '2'
    MISSING1 = '-1'


Q39B01 = Q39A01


Q39B02 = Q39A02


Q39B03 = Q39A03


Q39B04 = Q39A04


Q39B05 = Q39A05


Q39B06 = Q39A06


Q39B07 = Q39A07


Q39B08 = Q39A08


Q39B09 = Q39A09


Q39B10 = Q39A10


Q39B11 = Q39A11


Q39B12 = Q39A12


Q39B13 = Q39A13


Q39B14 = Q39A14


Q39B15 = Q39A15


Q39B16 = Q39A16


Q39B17 = Q39A17


Q39B18 = Q39A18


Q39B19 = Q39A19


Q39B20 = Q39A20


Q39B21 = Q39A21


Q39B22 = Q39A22


Q39C01 = Q39A01


Q39C02 = Q39A02


Q39C03 = Q39A03


Q39C04 = Q39A04


Q39C05 = Q39A05


Q39C06 = Q39A06


Q39C07 = Q39A07


Q39C08 = Q39A08


Q39C09 = Q39A09


Q39C10 = Q39A10


Q39C11 = Q39A11


Q39C12 = Q39A12


Q39C13 = Q39A13


Q39C14 = Q39A14


Q39C15 = Q39A15


Q39C16 = Q39A16


Q39C17 = Q39A17


Q39C18 = Q39A18


Q39C19 = Q39A19


Q39C20 = Q39A20


Q39C21 = Q39A21


Q39C22 = Q39A22


Q39D01 = Q39A01


Q39D02 = Q39A02


Q39D03 = Q39A03


Q39D04 = Q39A04


Q39D05 = Q39A05


Q39D06 = Q39A06


Q39D07 = Q39A07


Q39D08 = Q39A08


Q39D09 = Q39A09


Q39D10 = Q39A10


Q39D11 = Q39A11


Q39D12 = Q39A12


Q39D13 = Q39A13


Q39D14 = Q39A14


Q39D15 = Q39A15


Q39D16 = Q39A16


Q39D17 = Q39A17


Q39D18 = Q39A18


Q39D19 = Q39A19


Q39D20 = Q39A20


Q39D21 = Q39A21


Q39D22 = Q39A22


Q39E01 = Q39A01


Q39E02 = Q39A02


Q39E03 = Q39A03


Q39E04 = Q39A04


Q39E05 = Q39A05


Q39E06 = Q39A06


Q39E07 = Q39A07


Q39E08 = Q39A08


Q39E09 = Q39A09


Q39E10 = Q39A10


Q39E11 = Q39A11


Q39E12 = Q39A12


Q39E13 = Q39A13


Q39E14 = Q39A14


Q39E15 = Q39A15


Q39E16 = Q39A16


Q39E17 = Q39A17


Q39E18 = Q39A18


Q39E19 = Q39A19


Q39E20 = Q39A20


Q39E21 = Q39A21


Q39E22 = Q39A22


Q39F01 = Q39A01


Q39F02 = Q39A02


Q39F03 = Q39A03


Q39F04 = Q39A04


Q39F05 = Q39A05


Q39F06 = Q39A06


Q39F07 = Q39A07


Q39F08 = Q39A08


Q39F09 = Q39A09


Q39F10 = Q39A10


Q39F11 = Q39A11


Q39F12 = Q39A12


Q39F13 = Q39A13


Q39F14 = Q39A14


Q39F15 = Q39A15


Q39F16 = Q39A16


Q39F17 = Q39A17


Q39F18 = Q39A18


Q39F19 = Q39A19


Q39F20 = Q39A20


Q39F21 = Q39A21


Q39F22 = Q39A22


Q39G01 = Q39A01


Q39G02 = Q39A02


Q39G03 = Q39A03


Q39G04 = Q39A04


Q39G05 = Q39A05


Q39G06 = Q39A06


Q39G07 = Q39A07


Q39G08 = Q39A08


Q39G09 = Q39A09


Q39G10 = Q39A10


Q39G11 = Q39A11


Q39G12 = Q39A12


Q39G13 = Q39A13


Q39G14 = Q39A14


Q39G15 = Q39A15


Q39G16 = Q39A16


Q39G17 = Q39A17


Q39G18 = Q39A18


Q39G19 = Q39A19


Q39G20 = Q39A20


Q39G21 = Q39A21


Q39G22 = Q39A22


Q39H01 = Q39A01


Q39H02 = Q39A02


Q39H03 = Q39A03


Q39H04 = Q39A04


Q39H05 = Q39A05


Q39H06 = Q39A06


Q39H07 = Q39A07


Q39H08 = Q39A08


Q39H09 = Q39A09


Q39H10 = Q39A10


Q39H11 = Q39A11


Q39H12 = Q39A12


Q39H13 = Q39A13


Q39H14 = Q39A14


Q39H15 = Q39A15


Q39H16 = Q39A16


Q39H17 = Q39A17


Q39H18 = Q39A18


Q39H19 = Q39A19


Q39H20 = Q39A20


Q39H21 = Q39A21


Q39H22 = Q39A22


Q39I01 = Q39A01


Q39I02 = Q39A02


Q39I03 = Q39A03


Q39I04 = Q39A04


Q39I05 = Q39A05


Q39I06 = Q39A06


Q39I07 = Q39A07


Q39I08 = Q39A08


Q39I09 = Q39A09


Q39I10 = Q39A10


Q39I11 = Q39A11


Q39I12 = Q39A12


Q39I13 = Q39A13


Q39I14 = Q39A14


Q39I15 = Q39A15


Q39I16 = Q39A16


Q39I17 = Q39A17


Q39I18 = Q39A18


Q39I19 = Q39A19


Q39I20 = Q39A20


Q39I21 = Q39A21


Q39I22 = Q39A22


Q39J01 = Q39A01


Q39J02 = Q39A02


Q39J03 = Q39A03


Q39J04 = Q39A04


Q39J05 = Q39A05


Q39J06 = Q39A06


Q39J07 = Q39A07


Q39J08 = Q39A08


Q39J09 = Q39A09


Q39J10 = Q39A10


Q39J11 = Q39A11


Q39J12 = Q39A12


Q39J13 = Q39A13


Q39J14 = Q39A14


Q39J15 = Q39A15


Q39J16 = Q39A16


Q39J17 = Q39A17


Q39J18 = Q39A18


Q39J19 = Q39A19


Q39J20 = Q39A20


Q39J21 = Q39A21


Q39J22 = Q39A22


PQ43A1 = Q1A


PQ43A2 = Q1A


PQ43A3 = Q1A


PQ43A4 = Q1A


PQ43A5 = Q1A


PQ43A6 = Q1A


PQ43A7 = Q1A


PQ43A8 = Q1A


PQ43A9 = Q1A


PQ43A10 = Q1A


PQ43A11 = Q1A


PQ43A12 = Q1A


PQ43A13 = Q1A


PQ43A14 = Q1A


PQ43A15 = Q1A


PQ43A16 = Q1A


PQ43A17 = Q1A


PQ43A18 = Q1A


PQ43A19 = Q1A


PQ43A20 = Q1A


PQ43A21 = Q1A


PQ43B1 = Q1A


PQ43B2 = Q1A


PQ43B3 = Q1A


PQ43B4 = Q1A


PQ43B5 = Q1A


PQ43B6 = Q1A


PQ43B7 = Q1A


PQ43B8 = Q1A


PQ43B9 = Q1A


PQ43B10 = Q1A


PQ43B11 = Q1A


PQ43B12 = Q1A


PQ43B13 = Q1A


PQ43B14 = Q1A


PQ43B15 = Q1A


PQ43B16 = Q1A


PQ43B17 = Q1A


PQ43B18 = Q1A


PQ43B19 = Q1A


PQ43B20 = Q1A


PQ43B21 = Q1A


PQ43C1 = Q1A


PQ43C2 = Q1A


PQ43C3 = Q1A


PQ43C4 = Q1A


PQ43C5 = Q1A


PQ43C6 = Q1A


PQ43C7 = Q1A


PQ43C8 = Q1A


PQ43C9 = Q1A


PQ43C10 = Q1A


PQ43C11 = Q1A


PQ43C12 = Q1A


PQ43C13 = Q1A


PQ43C14 = Q1A


PQ43C15 = Q1A


PQ43C16 = Q1A


PQ43C17 = Q1A


PQ43C18 = Q1A


PQ43C19 = Q1A


PQ43C20 = Q1A


PQ43C21 = Q1A


PQ43D1 = Q1A


PQ43D2 = Q1A


PQ43D3 = Q1A


PQ43D4 = Q1A


PQ43D5 = Q1A


PQ43D6 = Q1A


PQ43D7 = Q1A


PQ43D8 = Q1A


PQ43D9 = Q1A


PQ43D10 = Q1A


PQ43D11 = Q1A


PQ43D12 = Q1A


PQ43D13 = Q1A


PQ43D14 = Q1A


PQ43D15 = Q1A


PQ43D16 = Q1A


PQ43D17 = Q1A


PQ43D18 = Q1A


PQ43D19 = Q1A


PQ43D20 = Q1A


PQ43D21 = Q1A


PQ43E1 = Q1A


PQ43E2 = Q1A


PQ43E3 = Q1A


PQ43E4 = Q1A


PQ43E5 = Q1A


PQ43E6 = Q1A


PQ43E7 = Q1A


PQ43E8 = Q1A


PQ43E9 = Q1A


PQ43E10 = Q1A


PQ43E11 = Q1A


PQ43E12 = Q1A


PQ43E13 = Q1A


PQ43E14 = Q1A


PQ43E15 = Q1A


PQ43E16 = Q1A


PQ43E17 = Q1A


PQ43E18 = Q1A


PQ43E19 = Q1A


PQ43E20 = Q1A


PQ43E21 = Q1A


PQ43F1 = Q1A


PQ43F2 = Q1A


PQ43F3 = Q1A


PQ43F4 = Q1A


PQ43F5 = Q1A


PQ43F6 = Q1A


PQ43F7 = Q1A


PQ43F8 = Q1A


PQ43F9 = Q1A


PQ43F10 = Q1A


PQ43F11 = Q1A


PQ43F12 = Q1A


PQ43F13 = Q1A


PQ43F14 = Q1A


PQ43F15 = Q1A


PQ43F16 = Q1A


PQ43F17 = Q1A


PQ43F18 = Q1A


PQ43F19 = Q1A


PQ43F20 = Q1A


PQ43F21 = Q1A


PQ43G1 = Q1A


PQ43G2 = Q1A


PQ43G3 = Q1A


PQ43G4 = Q1A


PQ43G5 = Q1A


PQ43G6 = Q1A


PQ43G7 = Q1A


PQ43G8 = Q1A


PQ43G9 = Q1A


PQ43G10 = Q1A


PQ43G11 = Q1A


PQ43G12 = Q1A


PQ43G13 = Q1A


PQ43G14 = Q1A


PQ43G15 = Q1A


PQ43G16 = Q1A


PQ43G17 = Q1A


PQ43G18 = Q1A


PQ43G19 = Q1A


PQ43G20 = Q1A


PQ43G21 = Q1A


PQ43H1 = Q1A


PQ43H2 = Q1A


PQ43H3 = Q1A


PQ43H4 = Q1A


PQ43H5 = Q1A


PQ43H6 = Q1A


PQ43H7 = Q1A


PQ43H8 = Q1A


PQ43H9 = Q1A


PQ43H10 = Q1A


PQ43H11 = Q1A


PQ43H12 = Q1A


PQ43H13 = Q1A


PQ43H14 = Q1A


PQ43H15 = Q1A


PQ43H16 = Q1A


PQ43H17 = Q1A


PQ43H18 = Q1A


PQ43H19 = Q1A


PQ43H20 = Q1A


PQ43H21 = Q1A


PQ43I1 = Q1A


PQ43I2 = Q1A


PQ43I3 = Q1A


PQ43I4 = Q1A


PQ43I5 = Q1A


PQ43I6 = Q1A


PQ43I7 = Q1A


PQ43I8 = Q1A


PQ43I9 = Q1A


PQ43I10 = Q1A


PQ43I11 = Q1A


PQ43I12 = Q1A


PQ43I13 = Q1A


PQ43I14 = Q1A


PQ43I15 = Q1A


PQ43I16 = Q1A


PQ43I17 = Q1A


PQ43I18 = Q1A


PQ43I19 = Q1A


PQ43I20 = Q1A


PQ43I21 = Q1A


PQ43J1 = Q1A


PQ43J2 = Q1A


PQ43J3 = Q1A


PQ43J4 = Q1A


PQ43J5 = Q1A


PQ43J6 = Q1A


PQ43J7 = Q1A


PQ43J8 = Q1A


PQ43J9 = Q1A


PQ43J10 = Q1A


PQ43J11 = Q1A


PQ43J12 = Q1A


PQ43J13 = Q1A


PQ43J14 = Q1A


PQ43J15 = Q1A


PQ43J16 = Q1A


PQ43J17 = Q1A


PQ43J18 = Q1A


PQ43J19 = Q1A


PQ43J20 = Q1A


PQ43J21 = Q1A


PQ44A = Q1A


PQ44B = Q1A


PQ44C = Q1A


PQ44D = Q1A


PQ44E = Q1A


PQ44F = Q1A


PQ44G = Q1A


PQ44H = Q1A


PQ44I = Q1A


PQ44J = Q1A


PQ45 = Q1A


PQ47 = Q1A


ATPQ49A1 = ATQ21A1


ATPQ49A2 = ATQ21A1


ATPQ49A3 = ATQ21A1


ATPQ49A4 = ATQ21A1


ATPQ49A5 = ATQ21A1


ATPQ49A6 = ATQ21A1


ATPQ49A7 = ATQ21A1


ATPQ49A8 = ATQ21A1


ATPQ49A9 = ATQ21A1


ATPQ49A10 = ATQ21A1


ATPQ49A11 = ATQ21A1


ATPQ49A12 = ATQ21A1


ATPQ50A1 = ATQ21A1


ATPQ50A2 = ATQ21A1


ATPQ50A3 = ATQ21A1


ATPQ50A4 = ATQ21A1


ATPQ50A5 = ATQ21A1


ATPQ50A6 = ATQ21A1


ATPQ50A7 = ATQ21A1


ATPQ50A8 = ATQ21A1


ATPQ50A9 = ATQ21A1


ATPQ50A10 = ATQ21A1


ATPQ50A11 = ATQ21A1


ATPQ50A12 = ATQ21A1


ATPQ50A13 = ATQ21A1


ATPQ51A1 = ATQ21A1


ATPQ51A2 = ATQ21A1


ATPQ51A3 = ATQ21A1


ATPQ51A4 = ATQ21A1


PQ52A01 = Q1A


PQ52A02 = Q1A


PQ52A03 = Q1A


PQ52A04 = Q1A


PQ52A05 = Q1A


PQ52A06 = Q1A


PQ52A07 = Q1A


PQ52A08 = Q1A


PQ52A09 = Q1A


PQ52A10 = Q1A


PQ52C01 = Q1A


PQ52C02 = Q1A


PQ52C03 = Q1A


PQ52C04 = Q1A


PQ52C05 = Q1A


PQ52C06 = Q1A


class PQ53(OrderedEnum):
    PROXY_INTERVIEW___NOT_ASKED = '-2'
    __0_____4_HRS_PER_WEEK = '1'
    __5_____9_HRS_PER_WEEK = '2'
    N10___19_HRS_PER_WEEK = '3'
    N20___34_HRS_PER_WEEK = '4'
    N35___49_HRS_PER_WEEK = '5'
    N50___99_HRS_PER_WEEK = '6'
    N100_HRS_OR_MORE_PER_WEEK = '7'
    VARIES_UNDER_20_HRS_PER_WEEK = '8'
    VARIES_OVER___20_HRS_PER_WEEK = '9'
    OTHER = '10'
    DON_T_KNOW = '11'
    REFUSED = '12'
    MISSING1 = '-1'


PQ54 = Q1A


class PQ55(OrderedEnum):
    SINGLE__THAT_IS__NEVER_MARRIED_ = '1'
    MARRIED_AND_LIVING_WITH_YOUR_HUSBANDWIFE_ = '2'
    MARRIED_AND_SEPARATED_FROM_YOUR_HUSBANDWIFE_ = '3'
    DIVORCED_ = '4'
    OR_WIDOWED = '5'
    DON_T_KNOW = '6'
    REFUSED = '7'
    MISSING1 = '-1'


class PQ56(OrderedEnum):
    YES = '1'
    NO = '2'
    SPONTANEOUS_ONLY___SAME_SEX_COUPLE = '3'
    DON_T_KNOW = '4'
    REFUSED = '5'
    MISSING1 = '-1'


PQ57 = Q1A


class PROXY(OrderedEnum):
    NORMAL = '1'
    PROXY = '2'
    MISSING1 = '-1'


class PROXYTYP(OrderedEnum):
    NORMAL_ADULT = '1'
    NORMAL_UNDER_16 = '2'
    PROXY_ADULT = '3'
    PROXY_UNDER_16 = '4'
    MISSING1 = '-1'


class PROXYWHO(OrderedEnum):
    PERSON_1 = '1'
    PERSON_2 = '2'
    PERSON_3 = '3'
    PERSON_4 = '4'
    PERSON_5 = '5'
    PERSON_6 = '6'
    PERSON_7 = '7'
    PERSON_8 = '8'
    PERSON_9 = '9'
    PERSON_10 = '10'
    NOT_ANSWERED = '11'
    MISSING1 = '-1'


class IAGEGRP(OrderedEnum):
    N8__15_YRS = '1'
    N16__24_YRS = '2'
    N25__44_YRS = '3'
    N45__64_YRS = '4'
    N65_YRS_OR_MORE = '5'


class ISEX(OrderedEnum):
    MALE = '1'
    FEMALE = '2'
    DKNA = '3'
    MISSING1 = '-1'


class IETHNIC(OrderedEnum):
    WHITE = '1'
    BLACK___CARRIBBEAN = '2'
    BLACK___AFRICAN = '3'
    BLACK___OTHER = '4'
    INDIAN = '5'
    PAKISTANI = '6'
    BANGLADESHI = '7'
    CHINESE = '8'
    NONE_OF_THESE = '9'
    DON_T_KNOW = '10'
    REFUSED = '11'
    MISSING1 = '-1'


class MANAGE2(OrderedEnum):
    MANAGER___LARGE_ORGANISATION_25_EMP_OR_MORE = '1'
    MANAGER___SMALL_ORGANISATION_24_OR_FEWER_EMP = '2'
    SUPERVISOR = '3'
    SELF_EMPLOYED___NO_EMPLOYEES = '4'
    EMPLOYEES_WITH_NO_MANAGESUPERVISORY_ROLE = '5'
    IN_EMPLOYMENT___INSUFFICIENT_INFO_TO_CODE_RESPONSIBILITIES = '6'
    ECON_ACTIVE___UNEMPLOYED_ILO_DEFINITION = '7'
    ECON_INACTIVE = '8'
    ADULT___ECON_ACTIVEINACTIVE_NOT_CLASSIFIABLE = '9'
    UNDER_16YRS___INELIGIBLE_FOR_EMPLOYMENT_QUESTIONS = '10'


class ECONACT(OrderedEnum):
    ECON_ACTIVE___IN_EMPLOYMENT = '1'
    ECON_ACTIVE___UNEMPLOYED_ILO_DEFINITION = '2'
    ECON_INACTIVE = '3'
    ADULT___NOT_CLASSIFIABLE_BUT_EITHER_UNEMP_OR_INACTIVE = '4'
    ADULT___NOT_CLASSIFIABLE_DK_IF_EMPUNEMPINACTIVE = '5'
    UNDER_16YRS___INELIGIBLE_FOR_EMPLOYMENT_QUESTIONS = '6'


class ECONACT2(OrderedEnum):
    ECON_ACTIVE___EMPLOYEE___FULL_TIME = '1'
    ECON_ACTIVE___EMPLOYEE___PART_TIME = '2'
    ECON_ACTIVE___SELF_EMPLOYED___FULL_TIME = '3'
    ECON_ACTIVE___SELF_EMPLOYED___PART_TIME = '4'
    ECON_ACTIVE___DK_EMPSELFFULLPART = '5'
    ECON_ACTIVE___UNEMPLOYED_ILO_DEFINITION = '6'
    ECON_INACTIVE___RETIRED = '7'
    ECON_INACTIVE___FULL_TIME_STUDENT = '8'
    ECON_INACTIVE___LOOKING_AFTER_FAMILY_HOME = '9'
    ECON_INACTIVE___LONG_TERM_SICK_DISABLED = '10'
    ECON_INACTIVE___OTHER_REASONS_EG_TEMP_SICK__BELIEVES_NO_JOBS = '11'
    ECON_INACTIVE___DK_REASONS = '12'
    ADULT___NOT_CLASSIFIABLE_EITHER_EMP__UNEMP_OR_INACTIVE = '13'
    UNDER_16YRS___INELIGIBLE_FOR_EMPLOYMENT_QUESTIONS = '14'


class ECONACT3(OrderedEnum):
    ECON_ACTIVE___FULL_TIME = '1'
    ECON_ACTIVE___PART_TIME = '2'
    ECON_ACTIVE___UNEMPLOYED_ILO_DEFINITION = '3'
    ECON_INACTIVE___RETIRED = '4'
    ECON_INACTIVE___FULL_TIME_STUDENT = '5'
    ECON_INACTIVE___LOOKING_AFTER_FAMILY_HOME = '6'
    ECON_INACTIVE___LONG_TERM_SICK_DISABLED = '7'
    ECON_INACTIVE___OTHER_REASONS_EG_TEMP_SICK__BELIEVES_NO_JOBS = '8'
    ADULT___NOT_CLASSIFIABLE = '9'
    UNDER_16YRS___INELIGIBLE_FOR_EMPLOYMENT_QUESTIONS = '10'


class EMPINCBD(OrderedEnum):
    INELIGIBLE___NOT_AN_EMPLOYEE = '-2'
    INELIGIBLE___UNDER_16YRS = '-1'
    _____________LESS_THAN_GBP__215 = '1'
    GBP__215_TO_LESS_THAN_GBP__435 = '2'
    GBP__435_TO_LESS_THAN_GBP__870 = '3'
    GBP__870_TO_LESS_THAN_GBP1305 = '4'
    GBP1305_TO_LESS_THAN_GBP1740 = '5'
    GBP1740_TO_LESS_THAN_GBP2820 = '6'
    GBP2820_TO_LESS_THAN_GBP3420 = '7'
    GBP3420_TO_LESS_THAN_GBP3830 = '8'
    GBP3830_TO_LESS_THAN_GBP4580 = '9'
    GBP4580_TO_LESS_THAN_GBP6670 = '10'
    GBP6670_OR_MORE = '11'
    ELIGIBLE___AN_EMPLOYEE___DK_REFUSE_INCOME = '12'


class SEINCBD(OrderedEnum):
    INELIGIBLE___NOT_CURRENTLY_SELF_EMPLOYED = '-2'
    INELIGIBLE___UNDER_16YRS = '-1'
    _____________LESS_THAN_GBP__215 = '1'
    GBP__215_TO_LESS_THAN_GBP__435 = '2'
    GBP__435_TO_LESS_THAN_GBP__870 = '3'
    GBP__870_TO_LESS_THAN_GBP1305 = '4'
    GBP1305_TO_LESS_THAN_GBP1740 = '5'
    GBP1740_TO_LESS_THAN_GBP2820 = '6'
    GBP2820_TO_LESS_THAN_GBP3420 = '7'
    GBP3420_TO_LESS_THAN_GBP3830 = '8'
    GBP3830_TO_LESS_THAN_GBP4580 = '9'
    GBP4580_TO_LESS_THAN_GBP6670 = '10'
    GBP6670_OR_MORE = '11'
    ELIGIBLE_CURRENTLY_SELF_EMP___DK_REFUSE_INCOME = '12'


class TOTPINC(OrderedEnum):
    INELIGIBLE___NOT_CURRENTLY_EMPLOYED_SELF_EMPLOYED = '-2'
    INELIGIBLE___UNDER_16YRS = '-1'
    _____________LESS_THAN_GBP__215 = '1'
    GBP__215_TO_LESS_THAN_GBP__435 = '2'
    GBP__435_TO_LESS_THAN_GBP__870 = '3'
    GBP__870_TO_LESS_THAN_GBP1305 = '4'
    GBP1305_TO_LESS_THAN_GBP1740 = '5'
    GBP1740_TO_LESS_THAN_GBP2820 = '6'
    GBP2820_TO_LESS_THAN_GBP3420 = '7'
    GBP3420_TO_LESS_THAN_GBP3830 = '8'
    GBP3830_TO_LESS_THAN_GBP4580 = '9'
    GBP4580_TO_LESS_THAN_GBP6670 = '10'
    GBP6670_OR_MORE = '11'
    ELIGIBLE_CURRENT_EMPLOYEE_OR_SELF_EMP___DK_REFUSE_INCOME = '12'


class HRS_GRP(OrderedEnum):
    __0_____9_HRS = '1'
    N10___19_HRS = '2'
    N20___29_HRS = '3'
    N30___39_HRS = '4'
    N40___49_HRS = '5'
    N50___59_HRS = '6'
    N60___69_HRS = '7'
    N70_HRS_OR_MORE = '8'
    IN_PAID_WORK_OR_DID_UNPAID_WORK__BUT_DKREFUSE_HOURS_WORKED = '9'
    INELIGIBLE___NOT_IN_PAID_WORK_DO_NO_UNPAID_WORK = '10'


class SIC(OrderedEnum):
    INELIGIBLE___NEVER_WORKED = '-2'
    INELIGIBLE___UNDER_16YRS = '-1'
    N01_11GROWING_CEREALS__OTHER_CROPS = '111'
    N01_12GROWING_VEG_HORTICULTURE_NURSERY = '112'
    N01_13GRWG_FRUIT_NUT_BEVERGE_SPICE_CROP = '113'
    N01_21FARMING_CATTLE_DAIRY = '121'
    N01_22FARMING_SHEEP_GOATS_HORSES_ETC = '122'
    N01_23FARMING_PIGS = '123'
    N01_24FARMING_POULTRY = '124'
    N01_25FARMING_OTHER_ANIMALS = '125'
    N01_30MIXED_FARMING_CROPS_AND_ANIMALS = '130'
    N01_41AGRICULTURAL_SERVICES = '141'
    N01_42ANIMAL_HUSBDRY_SERVICE_NOT_VET = '142'
    N01_50HUNTING_TRAPPING_GAME_ETC = '150'
    N02_01FORESTRY_LOGGING = '201'
    N02_02FORESTRY_LOGGING_SERVICES = '202'
    N05_01FISHING = '501'
    N05_02FISH_HATCHERIES_FARMS = '502'
    N10_101_103MINING_AND_AGGLOMERATION_OF_HARD_COAL = '1010'
    N10_20LIGNITE_MINING_AGGLOMERATION = '1020'
    N10_30PEAT_EXTRACTION_AGGLOMERATION = '1030'
    N11_10CRUDE_OIL_GAS_EXTRACTION = '1110'
    N11_20OIL_GAS_SERVICES_NOT_SURVEYING = '1120'
    N12_00URANIUM_THORIUM_ORE_MINING = '1200'
    N13_10IRON_ORE_MINING = '1310'
    N13_20NON_FERROUS_MINE_NOT_URAN_THOR = '1320'
    N14_11QUARRYING_CONSTRUCTION_STONE = '1411'
    N14_12LIMESTONE_GYPSUM_CHALK_QUARRYING = '1412'
    N14_13SLATE_QUARRYING = '1413'
    N14_21GRAVEL_SAND_PITS = '1421'
    N14_22CLAY_KAOLIN_MINING = '1422'
    N14_30CHEMICAL_FERTILISER_MINING = '1430'
    N14_40SALT_PRODUCTION = '1440'
    N14_50OTHER_MINING_QUARRYING = '1450'
    N15_111_3SLAUGHT_NG_NOT_POULTRY_RABBIT_AND_PROCESS_ANIMLS = '1511'
    N15_12POULTRY_PRODUCTION_PRESERVING = '1512'
    N15_13MEAT_POULTRY_PRODUCTS = '1513'
    N15_20FISH_FISH_PRODUCTS_PRESERVING = '1520'
    N15_31POTATO_PRODUCTS_PRESERVING = '1531'
    N15_32FRUIT_VEGETABLE_JUICE_PROCESSING = '1532'
    N15_33OTHER_FRUIT_VEG_PROCESSING = '1533'
    N15_41CRUDE_OILS_FATS_MANUFACTURE = '1541'
    N15_42REFINED_OILS_FATS_MANUFACTURE = '1542'
    N15_43MARGARINE_EDIBLE_FAT_MANUFACTURE = '1543'
    N15_51DAIRIES_CHEESE_MAKING = '1551'
    N15_52ICE_CREAM_MANUFACTURE = '1552'
    N15_61GRAIN_MILL_PRODUCTS = '1561'
    N15_62STARCHES_STARCH_PRODUCTS = '1562'
    N15_71FARM_ANIMAL_FEED_MANUFACTURE = '1571'
    N15_72PET_FOOD_MANUFACTURE = '1572'
    N15_81BREAD_FRESH_PASTRY_CAKES_MANUFACT_ = '1581'
    N15_82BISCUITS_RUSKS_PRESERVED_PASTRIES = '1582'
    N15_83SUGAR_MANUFACTURE = '1583'
    N15_84CHOCOLATE_COCOA_SUGAR_CONFECT_Y = '1584'
    N15_85MACARONI_NOODLES_COUSCOUS_ETC = '1585'
    N15_86TEA_COFFEE_MANUFACTURE = '1586'
    N15_87CONDIMENT_SEASONING_MANUFACTURE = '1587'
    N15_88HOMOGENISED_DIETETIC_FOOD_PRODUCTS = '1588'
    N15_89OTHER_FOOD_PRODUCTS_MANUFACTURE = '1589'
    N15_91DISTILLED_ALCOHOLIC_DRINKS = '1591'
    N15_92ETHYL_ALCOHOL_FROM_FERMENTATION = '1592'
    N15_93WINE_PRODUCTION = '1593'
    N15_94CIDER_OTHER_FRUIT_WINE_PRODUCTION = '1594'
    N15_95NON_DISTILLED_FERMENTED_DRINKS = '1595'
    N15_96BEER_PRODUCTION = '1596'
    N15_97MALT_PRODUCTION = '1597'
    N15_98MINERAL_WATER_SOFT_DRINK_PRODCTN_ = '1598'
    N16_00TOBACCO_PRODUCTS = '1600'
    N17_11COTTON_FIBRE_PREPARATION = '1711'
    N17_12WOOL_FIBRE_PREPARATION = '1712'
    N17_13WORSTED_FIBRE_PREPARATION = '1713'
    N17_14FLAX_FIBRE_PREPARATION = '1714'
    N17_15SILK_SYNTHETIC_PREPARATION = '1715'
    N17_16SEWING_THREAD_MANUFACTURE = '1716'
    N17_17OTHER_TEXTILE_PREPARATION = '1717'
    N17_21COTTON_WEAVING = '1721'
    N17_22WOOLLEN_WEAVING = '1722'
    N17_23WORSTED_WEAVING = '1723'
    N17_24SILK_WEAVING = '1724'
    N17_25OTHER_TEXTILE_WEAVING = '1725'
    N17_30TEXTILE_FINISHING = '1730'
    N17_401_403SOFT_FURNISHING_AND_HHLD_TEXTILE_MANUFACTURE = '1740'
    N17_511_3CARPETS_AND_RUG_MANUFACTURE = '1751'
    N17_52CORDAGE_ROPE_TWINE_MANUFACTURE = '1752'
    N17_53NON_WOVEN_ARTICLES_NOT_CLOTHING = '1753'
    N17_541_543LACE__NARROW_FABRICS_AND_OTHER_TEXTILE_MANUF_ = '1754'
    N17_60KNITTED_CROCHETED_FABRIC_MANUF_ = '1760'
    N17_71KNITTED_CROCHETED_HOSIERY_MANUF_ = '1771'
    N17_72KNITTED_CROCHETED_CLOTHING = '1772'
    N18_10LEATHER_CLOTHING_MANUFACTURE = '1810'
    N18_21WORKWEAR_MANUFACTURE = '1821'
    N18_221_222_OTHER_MENSWOMEN_S_OUTERWEAR_MANUF_ = '1822'
    N18_231_232_MENSWOMEN_S_UNDERWEAR_MANUFACTURE = '1823'
    N18_241_242_HAT_ACCESSORIES_MANUFACTURE = '1824'
    N18_30FUR_PROCESSING = '1830'
    N19_10LEATHER_TANNING_DRESSING = '1910'
    N19_20LUGGAGE_HANDBAGS_SADDLERY_MANUF_ = '1920'
    N19_30FOOTWEAR_MANUFACTURE = '1930'
    N20_10WOOD_SAWMILL_PLANING_IMPREGNATION = '2010'
    N20_20WOOD_VENEER_PLYWOOD_ETC_PRODUCTION = '2020'
    N20_30BUILDERS_CARPENTRY_JOINERY = '2030'
    N20_40WOODED_CONTAINERS_MANUFACTURE = '2040'
    N20_51OTHER_WOOD_PRODUCTS_MANUFACTURE = '2051'
    N20_52CORK_STRAW_ETC_MANUFACTURE = '2052'
    N21_11PULP_MANUFACTURE = '2111'
    N21_12PAPER_CARD_MANUFACTURE = '2112'
    N21_211_212PAPER_BOARD_SACKS_BAGS_BOXES_ETC_MANUF_ = '2121'
    N21_22SANITARY_TOILET_REQUIS__PRODUCTION = '2122'
    N21_23PAPER_STATIONARY_MANUFACTURE = '2123'
    N21_24WALLPAPER_MANUFACTURE = '2124'
    N21_25OTHER_PAPER_ARTICLES_MANUFACTURE = '2125'
    N22_11BOOK_PUBLISHING = '2211'
    N22_12NEWSPAPER_PUBLISHING = '2212'
    N22_13JOURNAL_PERIODICAL_PUBLISHING = '2213'
    N22_14SOUND_RECORDING_PUBLISHING = '2214'
    N22_15OTHER_PUBLISHING = '2215'
    N22_21NEWSPAPER_PRINTING = '2221'
    N22_22OTHER_PRINTING = '2222'
    N22_23BOOKBINDING_FINISHING = '2223'
    N22_24COMPOSITION_PLATE_MAKING = '2224'
    N22_25OTHER_PRINTING_ACTIVITIES = '2225'
    N22_31REPRODUCTION_OF_SOUND_RECORDING = '2231'
    N22_32REPRODUCTION_OF_VIDEO_RECORDING = '2232'
    N22_33REPRODUCTION_OF_COMPUTER_MEDIA = '2233'
    N23_10COKE_OVEN_PRODUCTS_MANUFACTURE = '2310'
    N23_201_202_MANUF_OF_REFINED_PETROLEUM_PRODUCTS = '2320'
    N23_30NUCLEAR_FUEL_PROCESSING = '2330'
    N24_11INDUSTRIAL_GAS_MANUFACTURE = '2411'
    N24_12DYE_PIGMENT_MANUFACTURE = '2412'
    N24_13INORGANIC_CHEMICAL_MANUFACTURE = '2413'
    N24_14ORGANIC_CHEMICAL_MANUFACTURE = '2414'
    N24_15FERTILIZER_ETC_MANUFACTURE = '2415'
    N24_16PRIMARY_PLASTICS_MANUFACTURE = '2416'
    N24_17PRIMARY_SYNTHETIC_RUBBER = '2417'
    N24_20PESTICIDES_ETC_MANUFACTURE = '2420'
    N24_301_303PAINT_VARNSH_PRINTING_INK__MASTIC_MAN = '2430'
    N24_41BASIC_PHARMACEUTICAL_MANUFACTURE = '2441'
    N24_42PHARMACEUTICAL_PREPARATIONS_MAN_ = '2442'
    N24_511_512SOAP_DETERGENT_CLEANING_POLISHING_AGENT_MAN = '2451'
    N24_52PERFUMES_ETC_MANUFACTURE = '2452'
    N24_61EXPLOSIVES_MANUFACTURE = '2461'
    N24_62GLUES_ETC_MANUFACTURE = '2462'
    N24_63ESSENTIAL_OILS_MANUFACTURE = '2463'
    N24_64PHOTOGRAPHIC_CHEMICALS_MAN_ = '2464'
    N24_65RECORDING_MEDIA_MANUFACTURE = '2465'
    N24_66OTHER_CHEMICAL_PRODUCTS_MAN_ = '2466'
    N24_70MAN_MADE_FIBRES_MANUFACTURE = '2470'
    N25_11RUBBER_TYRES_ETC_MANUFACTURE = '2511'
    N25_12RUBBER_TYRES_RETREADING_ETC = '2512'
    N25_13OTHER_RUBBER_PRODUCTS_MANUFACTURE = '2513'
    N25_21PLASTIC_SHEETS_TUBES_ETC_MAN_ = '2521'
    N25_22PLASTIC_PACKING_MANUFACTURE = '2522'
    N25_231_232PLASTIC_FLOORING_AND_OTHER_PLASTIC_BLDNG_WARES_MAN = '2523'
    N25_24MANUF_OF_OTHER_PLASTIC_PRODUCTS = '2524'
    N26_11FLAT_GLASS_MANUFACTURE = '2611'
    N26_12FLAT_GLASS_SHAPING_PROCESSING = '2612'
    N26_13HOLLOW_GLASS_MANUFACTURE = '2613'
    N26_14GLASS_FIBRE_MANUFACTURE = '2614'
    N26_15OTHER_GLASS_PROC_MANUFACTURE = '2615'
    N26_21CERAMIC_HHLD_ORNAMENTAL_MAN_ = '2621'
    N26_22CERAMIC_SANITARY_FIXTURES_MAN_ = '2622'
    N26_23CERAMIC_INSULATORS_ETC_MAN_ = '2623'
    N26_24OTHER_TECHNICAL_CERAMIC_MAN_ = '2624'
    N26_25OTHER_CERAMIC_MANUFACTURE = '2625'
    N26_26REFRACTORY_CERAMIC_MANUFACTURE = '2626'
    N26_30CERAMIC_TILE_FLAGS_MANUFACTURE = '2630'
    N26_40BRICKS_TILES_ETC_MANUFACTURE = '2640'
    N26_51CEMENT_MANUFACTURE = '2651'
    N26_52LIME_MANUFACTURE = '2652'
    N26_53PLASTER_MANUFACTURE = '2653'
    N26_61CONCRETE_PRODSCONSTRUCTIONMAN_ = '2661'
    N26_62PLASTER_PRODUCTSCONSTRUCTIONMAN_ = '2662'
    N26_63READY_MIXED_CONCRETE_MANUFACTURE = '2663'
    N26_64MORTARS_MANUFACTURE = '2664'
    N26_65FIBRE_CEMENT_MANUFACTURE = '2665'
    N26_66OTHER_CONCRETE_PLASTER_ETC_MAN_ = '2666'
    N26_70STONE_CUTTING_SHAPING = '2670'
    N26_81ABRASIVE_PRODUCTS_MANUFACTURE = '2681'
    N26_821_822ASBESTOS_AND_OTH_NON_METAL_MINERAL_PROD_MAN_ = '2682'
    N27_10BASIC_IRON_STEEL_FERRO_ALLOYS_MAN_ = '2710'
    N27_21CAST_IRON_TUBES_MANUFACTURE = '2721'
    N27_22STEEL_TUBES_MANUFACTURE = '2722'
    N27_31COLD_DRAWING = '2731'
    N27_32COLD_ROLLINGNARROW_STRIP = '2732'
    N27_33COLD_FORMING_FOLDING = '2733'
    N27_34WIRE_DRAWING = '2734'
    N27_35OTHER_1ST_PROC_IRON_STEEL = '2735'
    N27_41PRECIOUS_METALS_PRODUCTION = '2741'
    N27_42ALUMINIUM_PRODUCTION = '2742'
    N27_43LEAD_ZINC_TIN_PRODUCTION = '2743'
    N27_44COPPER_PRODUCTION = '2744'
    N27_45OTHER_NON_METAL_PRODUCTION = '2745'
    N27_51IRON_CASTING = '2751'
    N27_52STEEL_CASTING = '2752'
    N27_53LIGHT_METALS_CASTING = '2753'
    N27_54OTHER_NON_FERROUS_CASTING = '2754'
    N28_11METAL_STRUCTURES_ETC_MANUFACTURE = '2811'
    N28_12BUILDERS_METAL_WORK = '2812'
    N28_21METAL_CONTAINERS_MANUFACTURE = '2821'
    N28_22RADIATORS_BOILERS_MANUFACTURE = '2822'
    N28_30STEAM_GENERATORS_MANUFACTURE = '2830'
    N28_40FORGING_PRESSING_ETC = '2840'
    N28_51TREATMENT_COATING_OF_METALS = '2851'
    N28_52GENERAL_MECH_ENGINEERING = '2852'
    N28_61CUTLERY_MANUFACTURE = '2861'
    N28_62TOOLS_MANUFACTURE = '2862'
    N28_63LOCKS_HINGES_ETC_MANUFACTURE = '2863'
    N28_71STEEL_DRUMS_ETC_MANUFACTURE = '2871'
    N28_72LIGHT_METAL_PACKAGING_MANUFACTURE = '2872'
    N28_73WIRE_PRODUCTS_MANUFACTURE = '2873'
    N28_74FASTENERS_CHAINS_ETC_MANUFACTURE = '2874'
    N28_75OTHER_METAL_PRODUCTS_MANUFACTURE = '2875'
    N29_11ENGINES_TURBINES_NOT_AIRCRAFT = '2911'
    N29_121_122_PUMPS_AND_COMPRESSOR_MANUFACTURE = '2912'
    N29_13TAPS_VALVES_MANUFACTURE = '2913'
    N29_14BEARINGS_GEARS_ETC_MANUFACTURE = '2914'
    N29_21FURNACE_MANUFACTURE = '2921'
    N29_22LIFTING_HANDLING_EQT_MANUFACTURE = '2922'
    N29_23COOL__VENTILAT_EQTNOT_DOMESTIC = '2923'
    N29_24OTHER_GEN_PURPOSE_MACH_MANUFACTURE = '2924'
    N29_31AGRICULTURAL_TRACTORS_MANUFACTURE = '2931'
    N29_32OTHER_AGRIC__FORESTRY_MACH__MAN_ = '2932'
    N29_40MACHINE_TOOL_MANUFACTURE = '2940'
    N29_51METALLURGY_MACH_MANUFACTURE = '2951'
    N29_521_523_MINING_ROADWK__EARTHMOVING_EQT_MAN_ = '2952'
    N29_53FOOD_TOBACCO_PROC_MACH = '2953'
    N29_54TEXTILE_ETC__LEATHER_MACH_MAN_ = '2954'
    N29_55PAPER_ETC_PROD_MACH_MANUFACTURE = '2955'
    N29_56OTHER_SPECIAL_PURPOSE_MACH_MAN_ = '2956'
    N29_60WEAPONS_AMMUNITION_MANUFACTURE = '2960'
    N29_71ELEC_DOMESTIC_APPLIANCES_MAN_ = '2971'
    N29_72NON_ELEC_DOMESTIC_APPLIANCES_MAN_ = '2972'
    N30_01OFFICE_MACH_MANUFACTURE = '3001'
    N30_02COMPUTERS__IT_EQT_MANUFACTURE = '3002'
    N31_10ELEC_MOTORS_GENTORS_TRANS_MAN_ = '3110'
    N31_20ELEC_DISTRIBUTION__CONTROL_MAN_ = '3120'
    N31_30INSULATED_CABLE_MANUFACTURE = '3130'
    N31_40ELECTRIC_BATTERY_MANUFACTURE = '3140'
    N31_50LIGHTING_EQT_MANUFACTURE = '3150'
    N31_61OTHER_ELEC_EQT_ENGINESVEH_MAN_ = '3161'
    N31_62OTHER_ELEC_EQT_MANUFACTURE = '3162'
    N32_10ELECTRONIC_COMPONENTS_ETC_MAN_ = '3210'
    N32_201_202_TELEPHONE__RADIO_ELECTRONIC_GOODS_MAN_ = '3220'
    N32_30TV_RADIO_HIFI_ETC_EQT_MANUFACTURE = '3230'
    N33_10MEDICAL_EQT_APPLIANCES_MANUFACTURE = '3310'
    N33_20TESTING_NAVIGATING_ETC_EQT_MAN_ = '3320'
    N33_30INDUSTRIAL_PROC_CONTROL_EQT_MAN_ = '3330'
    N33_401_403SPECTACLES__OPTICAL__PHOTOGRAPHIC_EQT_MAN_ = '3340'
    N33_50WATCHES_CLOCK_MANUFACTURE = '3350'
    N34_10MOTOR_VEH_MANUFACTURE = '3410'
    N34_201_203MOTOR_VEH_BODYWORK_TRAILERS_CARAVAN_MANU = '3420'
    N34_30MOTOR_VEH_PARTS_ETC_MANUFACTURE = '3430'
    N35_11SHIP_BUILDING_REPAIRING = '3511'
    N35_12BOAT_BUILDING_REPAIRING = '3512'
    N35_20RAIL_TRAM_ROLLING_STK_ETC_MAN_ = '3520'
    N35_30AIRCRAFT_SPACECRAFT_MANUFACTURE = '3530'
    N35_41MOTORCYCLE_MANUFACTURE = '3541'
    N35_42BICYCLE_MANUFACTURE = '3542'
    N35_43INVALID_CARRIAGE_MANUFACTURE = '3543'
    N35_50OTHER_TRANSPORT_EQT_MANUFACTURE = '3550'
    N36_11CHAIRS_ETC_MANUFACTURE = '3611'
    N36_12OTHER_OFFICE_SHOP_FURNITURE_MAN_ = '3612'
    N36_13OTHER_KITCHEN_FURNITURE_MAN_ = '3613'
    N36_14OTHER_FURNITURE_MANUFACTURE = '3614'
    N36_15MATTRESSES_MANUFACTURE = '3615'
    N36_21COINS_MEDAL_MANUFACTURE = '3621'
    N36_22JEWELLERY_ETC_MANUFACTURE = '3622'
    N36_30MUSICAL_INSTRUMENTS_MANUFACTURE = '3630'
    N36_40SPORTS_GOODS_MANUFACTURE = '3640'
    N36_501_502MANUF__OF_GANES_AND_TOYS = '3650'
    N36_61IMITATION_JEWELLERY_MANUFACTURE = '3661'
    N36_62BROOMS_BRUSHES_ETC_MANUFACTURE = '3662'
    N36_631_632STATIONERS_GOODS_AND_OTHER_MANUF = '3663'
    N37_10METAL_SCRAP_RECYCLING = '3710'
    N37_20NON_METAL_SCRAP_RECYCLING = '3720'
    N40_10ELEC_GENERATION_SUPPLY = '4010'
    N40_20GAS_PRODUCTION_SUPPLY = '4020'
    N40_30STEAM_HOT_WATER_SUPPLY = '4030'
    N41_00WATER_SUPPLY_ETC = '4100'
    N45_11DEMOLISH_BUILDINGS_EARTH_MOVING = '4511'
    N45_12TEST_DRILLING_AND_BORING = '4512'
    N45_21CONSTRUCT_BUILDINGS_AND_GENERAL_CIVIL_ENGINEERING = '4521'
    N45_22ERECTION_OF_ROOF_COVERING_AND_FRAMES = '4522'
    N45_23CONSTRUCTION_OF_ROADS__AIRFIELDS_AND_SPORTS_FACILITIES = '4523'
    N45_24CONSTRUCTION_OF_WATER_PROJECTS = '4524'
    N45_25OTHER_CONSTRUCTION_USING_SPECIAL_TRADES = '4525'
    N45_31INSTALLATION_OF_ELECTRICAL_WIRING_AND_FITTINGS = '4531'
    N45_32INSULATION_WORK_ACTIVITIES = '4532'
    N45_33PLUMBING = '4533'
    N45_34OTHER_BUILDING_INSTALLATION = '4534'
    N45_41PLASTERING = '4541'
    N45_42JOINERY_INSTALLATION = '4542'
    N45_43FLOOR_AND_WALL_COVERING = '4543'
    N45_44PAINTING_AND_GLAZING = '4544'
    N45_45OTHER_BUILDING_COMPLETION = '4545'
    N45_55RENT_CONSTRUCTION_DEMOL__EQUIP__WITH_OPERATOR = '4555'
    N50_10SALE_OF_MOTOR_VEHICLES = '5010'
    N50_20MOTOR_VEH_REPAIR = '5020'
    N50_30SALES_OF_MOTOR_VEH_PARTS_AND_ACCESSORIESR = '5030'
    N50_40MOTORCYCLE_SALE_REPAIR_ETC = '5040'
    N50_50RETAIL_SALE_OF_AUTOMOTIVE_FUEL = '5050'
    N50_11AGENTS_IN_WSALE_AGRIC_RAW_MATERIALS = '5111'
    N50_12AGENTS_IN_WSALE_FUEL__ORE__METAL__CHEMICALS = '5112'
    N50_13AGENTS_IN_WSALE_TIMBER_AND_BUILDING_MATERIALS = '5113'
    N50_14AGENTS_IN_WSALE_MCHNRY__INDSTRL_EQPT__SHIPS__AIRCRAFT = '5114'
    N50_15AGENTS_IN_WSALE_FURNITURE__HHLD_GOODS__HARDWARE = '5115'
    N50_16AGENTS_IN_WSALE_TEXTILES__CLOTHING__FOOTWEAR = '5116'
    N50_17AGENTS_IN_WSALE_FOOD__BEVERAGES_AND_TOBACCO = '5117'
    N50_18AGENTS_IN_WSALE_PRODUCTS_NOT_ELSEWHERE_CLASSIFIED = '5118'
    N50_19AGENTS_IN_WSALE_VARIETY_OF_GOODS = '5119'
    N50_21WHOLESALE_GRAIN__SEEDS_AND_ANIMAL_FEEDS = '5121'
    N50_22WHOLESALE_FLOWERS_AND_PLANTS = '5122'
    N50_23WHOLESALE_LIVE_ANIMALS = '5123'
    N50_24WHOLESALE_HIDES__SKINS_AND_LEATHER = '5124'
    N50_25WHOLESALE_UNMANUFACTURED_TOBACCO = '5125'
    N50_31WHOLESALE_FRUIT_AND_VEG = '5131'
    N50_32WHOLESALE_MEAT_AND_MEAT_PRODUCTS = '5132'
    N50_33WHOLESALE_DAIRY_PRODUCE__EGGS__EDIBLE_OILS = '5133'
    N50_34WHOLESALE_ALCOHOLIC_AND_OTHER_BEVERAGES = '5134'
    N50_35WHOLESALE_TOBACCO_PRODUCTS = '5135'
    N50_36WHOLESALE_SUGAR__CHOCOLATE_AND_SUGAR_CNFCTNRY = '5136'
    N50_37WHOLESALE_COFFEE__TEA__COCOA__SPICES = '5137'
    N50_38WHOLESALE_OTHER_FOOD_INCL_FISH = '5138'
    N50_39WHOLESALE_NON_SPECIALISED_OF_FOOD__DRINK__TOBACCO = '5139'
    N50_41WHOLESALE_TEXTILES = '5141'
    N50_42WHOLESALE_CLOTHING_AND_FOOTWEAR = '5142'
    N50_43WHOLESALE_ELCTRCL_HHLD_APPLIANCES__RADIO__TV = '5143'
    N50_44WHOLESALE_CHINA__GLASSWARE__WALLPAPER_CLEANING_MTRLS = '5144'
    N50_45WHOLESALE_PERFUME_AND_COSMETICS = '5145'
    N50_46WHOLESALE_PHARMACEUTICAL_GOODS = '5146'
    N50_47WHOLESALE_FURNITURE_AND_HHLD_GOOD_N_E_C = '5147'
    N50_51WHOLESALE_PETROLEUM_AND_FUELS = '5151'
    N50_52WHOLESALE_METAL_AND_METAL_ORES = '5152'
    N50_53WHOLESALE_WOOD_AND_CONSTRUCTION_MTRLS = '5153'
    N50_54WHOLESALE_HARDWARE__PLUMBING_AND_HEATING_EQUIP = '5154'
    N50_55WHOLESALE_CHEMICAL_PRODUCTS = '5155'
    N50_56WHOLESALE_OTHER_INTERMEDIATE_PRODUCTS = '5156'
    N50_57WHOLESALE_WASTE_AND_SCRAP = '5157'
    N50_61WHOLESALE_MACHINE_TOOLS = '5161'
    N50_62WHOLESALE_CONSTRUCTION_MACHINERY = '5162'
    N50_63WHOLESALE_MCHNRY_FOR_TEXTILE_INDTRY__SEWING_MACHINES = '5163'
    N50_64WHOLESALE_OFFICE_MCHNRY_AND_EQUIP = '5164'
    N50_65WHOLESALE_OTHER_MCHNRY_FOR_INDUSTRY_AND_TRADE = '5165'
    N50_66WHOLESALE_AGRIC_MCHNRY_INCL_TRACTORS = '5166'
    N50_70WHOLESALE_OTHER = '5170'
    N52_11RETAIL_IN_NON_SPCLISED_SHOP_MAINLY_FOODDRNKTOBACCO = '5211'
    N52_12OTHER_RETAIL_IN_NON_SPCLISED_SHOPS = '5212'
    N52_21RETAIL_FRUIT_AND_VEG = '5221'
    N52_22RETAIL_MEAT_AND_MEAT_PRODUCTS = '5222'
    N52_23RETAIL_FISH = '5223'
    N52_24RETAIL_BREAD__CAKES = '5224'
    N52_25RETAIL_ALCOHOL_AND_OTHER_BEVERAGES = '5225'
    N52_26RETAIL_TOBACCO_PRODUCTS = '5226'
    N52_27OTHER_RETAIL_OF_FOOD_DRINKTOBACCO_IN_SPCLSED_SHOPS = '5227'
    N52_31DISPENSING_CHEMISTS = '5231'
    N52_32RETAIL_OF_MEDICAL_AND_ORTHOPAEDIC_GOODS = '5232'
    N52_33RETAIL_COSMETIC_ARTICLES = '5233'
    N52_41RETAIL_OF_TEXTILES = '5241'
    N52_42RETAIL_OF_CLOTHING = '5242'
    N52_43RETAIL_OF_FOOTWEAR_AND_LEATHER_GOODS = '5243'
    N52_44RETAIL_FURNITURE__LIGHTING_EQT_AND_HHLD_ARTICLES_NEC = '5244'
    N52_45RETAIL_ELCTRCL_HHLD_APPLIANCES__RADIO__TV = '5245'
    N52_46RETAIL_HARDWARE__PAINTS_AND_GLASS = '5246'
    N52_47RETAIL_BOOKS__NEWSPAPERS_AND_STATIONERY = '5247'
    N52_48RETAIL_FLOOR_COVERNGS__OFFICE_EQT__CMPTRS__OTHER_NEC = '5248'
    N52_50RETAIL_OF_SECOND_HAND_GOODS_IN_STORES = '5250'
    N52_61RETAIL_VIA_MAIL_ORDER = '5261'
    N52_62RETAIL_VIA_STALLS_AND_MARKETS = '5262'
    N52_63OTHER_NON_STORE_RETAIL = '5263'
    N52_71REPAIR_LEATHER_ARTICLES = '5271'
    N52_72REPAIR_ELEC_HHLD_GOODS = '5272'
    N52_73REPAIR_WATCHES_CLOCKS_ETC = '5273'
    N52_74OTHER_REPAIR = '5274'
    N55_11HOTELS_MOTELS_WITH_RESTAURANT = '5511'
    N55_12HOTELS_MOTELS_WITHOUT_RESTAURANT = '5512'
    N55_21YOUTH_HOSTEL_MOUNTAIN_REFUGE = '5521'
    N55_22CAMPING_CARAVAN_SITES = '5522'
    N55_23OTHER_PROVISION_OF_LODGINGS = '5523'
    N55301_3RESTAURANTS__CAFES_AND_TAKE_AWAY_FOOD_SHOPS = '5530'
    N55_401_2PUBLIC_HOUSES__BARS_AND_LICENCED_CLUBS_WITH_ENTNMNT = '5540'
    N55_51CANTEENS = '5551'
    N55_52CATERING = '5552'
    N60_10TRANSPORT_VIA_RAILWAY = '6010'
    N60_21OTHER_SCHEDULED_LAND_TRANSPORT = '6021'
    N60_22TAXI = '6022'
    N60_23OTHER_PASSENGER_LAND_TRANSPORT = '6023'
    N60_24FREIGHT_TRANSPORT_BY_ROAD = '6024'
    N60_30TRANSPORT_VIA_PIPELINES = '6030'
    N61_10SEA_COASTAL_WATER_TRANSPORT = '6110'
    N61_20INLAND_WATER_TRANSPORT = '6120'
    N62_10SCHEDULED_AIR_TRANSPORT = '6210'
    N62_20NON_SCHEDULED_AIR_TRANSPORT = '6220'
    N62_30SPACE_TRANSPORT = '6230'
    N63_11CARGO_HANDLING = '6311'
    N63_12STORAGE_WAREHOUSING = '6312'
    N63_21OTHER_LAND_TRANSPORT_ACTIVITIES = '6321'
    N63_22OTHER_WATER_TRANSPORT_ACTIVITIES = '6322'
    N63_23OTHER_AIR_TRANSPORT_ACTIVITIES = '6323'
    N63_301_4TRAVEL_AGENTS__ORGANISERS__GUIDES__TOURIST_ASSTNCE = '6330'
    N63_40OTHER_TRANSPORT_AGENCIES = '6340'
    N64_11NATIONAL_POST_ACTIVITIES = '6411'
    _64_12COURIER_ACTIV__NOT_NATNL__POST = '6412'
    N64_20TELECOMMUNICATIONS = '6420'
    N65_11CENTRAL_BANKING = '6511'
    N65_121_2BANKS_AND_BUILDING_SOCIETIES = '6512'
    N65_21FINANCIAL_LEASING = '6521'
    N65_22OTHER_CREDIT_GRANTING = '6522'
    N65_231_6UNIT_TRUST__INVSTMNT_TRUSTS__HLDING_CO_ETC = '6523'
    N66_01LIFE_INSURANCE = '6601'
    N66_02PENSION_FUNDING = '6602'
    N66_03NON_LIFE_INSURANCE = '6603'
    N67_11FINANCIAL_MARKET_ADMINISTRATION = '6711'
    N67_12SECURITIES_FUND_MANAGEMENT = '6712'
    N67_13OTHER_FINANCIAL_INTERMED__ACTIV_ = '6713'
    N67_20OTHER_INSURANCE_ACTIVITIES = '6720'
    N70_11DEVELOPMENT_SALE_OF_REAL_ESTATE = '7011'
    N70_12BUYING_SELLING_REAL_ESTATE_SELF = '7012'
    N70_20LETTING_OWN_PROPERTY = '7020'
    N70_31REAL_ESTATE_AGENCY = '7031'
    N70_32MANAGEMENT_OF_REAL_ESTATE = '7032'
    N71_10CAR_RENTAL = '7110'
    N71_21OTHER_LAND_TRANSPORT_RENTAL = '7121'
    N71_22WATER_TRANSPORT_EQT_RENTAL = '7122'
    N71_23AIR_TRANSPORT_EQT_RENTAL = '7123'
    N71_31AGRICULTURAL_MACH_EQT_RENTAL = '7131'
    N71_32CONSTRUCTION_MACH_EQT_RENTAL = '7132'
    N71_33OFFICE_MACH_EQT_RENTAL = '7133'
    N71_34OTHER_MACH_EQT_RENTAL = '7134'
    N71_40PERSON_HHLD_EQT_RENTAL = '7140'
    N72_10COMPUTER_HARDWARE_CONSULTANCY = '7210'
    N72_20COMPUTER_SOFTWARE_CONSULTANCY = '7220'
    N72_30DATA_PROCESSING = '7230'
    N72_40DATA_BASE_ACTIVITIES = '7240'
    N72_50REPAIR_OF_OFFICE_COMPUTER_EQT = '7250'
    N72_60OTHER_COMPUTER_ACTIVITIES = '7260'
    N73_10RESEARCH_NATURAL_SCIENCES_ENGIN_ = '7310'
    N73_20RES__SOCIAL_SCIENCES_HUMANITIES = '7320'
    N74_11LEGAL_ACTIVITIES = '7411'
    N74_12ACCOUNTNG_AUDITNG_TAX_CONSULTANCY = '7412'
    N74_13MARKET_OPINION_RESEARCH = '7413'
    N74_14BUSINESS_MANAGEMENT_CONSULTANCY = '7414'
    N74_15MANAGEMNT_ACTIVITIES_HOLDING_COMPS = '7415'
    N74_20ARCHIT__ENGINEERING_ETC_CONSULTNCY = '7420'
    N74_30TECHNICAL_TESTING_ANALYSIS = '7430'
    N74_40ADVERTISING = '7440'
    N74_50LABOUR_PERSONNEL_RECRUITMENT = '7450'
    N74_60INVESTIGATION_SECURITY_SERVICES = '7460'
    N74_70INDUSTRIAL_CLEANING = '7470'
    N74_81PHOTOGRAPHIC_ACTIVITIES = '7481'
    N74_82PACKAGING_ACTIVITIES = '7482'
    N74_83SECRETARIAL_TRANSLATION = '7483'
    N74_84OTHER_BUSINESS_ACTIVITIES = '7484'
    N75_11GENERAL_PUBLIC_SERVICE_ACTIVITIES = '7511'
    N75_12REGULN_GOVT_AGENCY_NOT_SOC_SEC = '7512'
    N75_13DEVELOPMENT_OF_GOVT_AGENCIES = '7513'
    N75_14SUPPORT_OF_GOVT_AS_A_WHOLE = '7514'
    N75_21FOREIGN_AFFAIRS = '7521'
    N75_22DEFENCE = '7522'
    N75_23JUSTICE_AND_JUDICIAL_ACTIVITIES = '7523'
    N75_24PUBLIC_SECURITY_LAW_AND_ORDER_ETC = '7524'
    N75_25FIRE_SERVICE = '7525'
    N75_30COMPULSORY_SOCIAL_SECURITY_ACTIV_ = '7530'
    N80_10PRIMARY_EDUCATION = '8010'
    N80_21GENERAL_SECONDARY_EDUCATION = '8021'
    N80_22TECH_VOCATIONAL_2ND_ARY_EDUCATION = '8022'
    N80_301_3HIGHER_EDUCN_SUB_DEGREE_FIRST_DGREE_PGRAD_DGREE = '8030'
    N80_41DRIVING_SCHOOL_ACTIVITIES = '8041'
    N80_42ADULT_OTHER_EDUCATION = '8042'
    N85_11HOSPITAL_ACTIVITIES = '8511'
    N85_12MEDICAL_PRACTICE_ACTIVITIES = '8512'
    N85_13DENTAL_PRACTICE_ACTIVITIES = '8513'
    N85_14OTHER_HUMAN_HEALTH_ACTIVITIES = '8514'
    N85_20VETERINARY_ACTIVITIES = '8520'
    N85_31SOCIAL_WORK_WITH_ACCOM = '8531'
    N85_32SOCIAL_WORK_WITHOUT_ACCOM = '8532'
    N90_00SEWAGE_REFUSE_DISPOSAL_ETC = '9000'
    N91_11BUSINESS_EMPLOYERS_ORGANISATIONS = '9111'
    N91_12PROFESSIONAL_ORGANISATIONS = '9112'
    N91_20TRADE_UNIONS = '9120'
    N91_31RELIGIOUS_ORGANISATIONS = '9131'
    N91_32POLITICAL_ORGANISATIONS = '9132'
    N91_33OTHER_MEMBERSHIP_ORGANISATIONS = '9133'
    N92_11MOTION_PICTURE_VIDEO_PRODUCTION = '9211'
    N92_12MOTION_PICTURE_VIDEO_DISTRIBUTION = '9212'
    N92_13MOTION_PICTURE_PROJECTION = '9213'
    N92_20RADIO_TV_ACTIVITIES = '9220'
    N92_31ARTISTIC_LITERARY_CREATION_ETC = '9231'
    N92_32ARTS_FACILITIES = '9232'
    N92_33FAIR_AMUSEMENT_PARK_ACTIVITIES = '9233'
    N92_34OTHER_ENTERTAINMENT_ACTIVITIES = '9234'
    N92_40NEWS_AGENCY_ACTIVITIES = '9240'
    N92_51LIBRARY_ARCHIVE_ACTIVITIES = '9251'
    N92_52MUSEUM_ACTIVITIES = '9252'
    N92_53BOTANICAL_ZOOLOGICAL_GARDENS_ETC = '9253'
    N92_61OPERATION_OF_SPORTS_ARENAS_STADIA = '9261'
    N92_62OTHER_SPORTING_ACTIVITIES = '9262'
    N92_71GAMBLING_BETTING_ACTIVITIES = '9271'
    N92_72OTHER_RECREATIONAL_ACTIVITIES = '9272'
    N93_01WASHING_DRY_CLEANING_TEXTILES_FURS = '9301'
    N93_02HAIRDRESSING_OTH_BEAUTY_TREATMENT = '9302'
    N93_03FUNERAL_ETC = '9303'
    N93_04PHYSICAL_WELL_BEING_ACTIVITIES = '9304'
    N93_05OTHER_SERVICE_ACTIVITIES = '9305'
    N95_00PRIV__HHLDS_WITH_EMPLYED_PERSONS = '9500'
    N99_00EXTRA_TERRITORIAL_ORGANISATIONS = '9900'
    IN_WORK_OR_EVER_WORKED___DK_REFUSE_INDUSTRY = '9999'


class SOC(OrderedEnum):
    INELIGIBLE___NEVER_WORKED = '-2'
    INELIGIBLE___UNDER_16YRS = '-1'
    SENIOR_OFFICIALS_IN_NATIONAL_GOVERNMENT = '1111'
    DIRECTORS_AND_CHIEF_EXECUTIVES_OF_MAJOR_ORGANISATIONS = '1112'
    SENIOR_OFFICIALS_IN_LOCAL_GOVERNMENT = '1113'
    SENIOR_OFFICIALS_OF_SPECIAL_INTEREST_ORGANISATIONS = '1114'
    PRODUCTION__WORKS_AND_MAINTENANCE_MANAGERS = '1121'
    MANAGERS_IN_CONSTRUCTION = '1122'
    MANAGERS_IN_MINING_AND_ENERGY = '1123'
    FINANCIAL_MANAGERS_AND_CHARTERED_SECRETARIES = '1131'
    MARKETING_AND_SALES_MANAGERS = '1132'
    PURCHASING_MANAGERS = '1133'
    ADVERTISING_AND_PUBLIC_RELATIONS_MANAGERS = '1134'
    PERSONNEL__TRAINING_AND_INDUSTRIAL_RELATIONS_MANAGERS = '1135'
    INFORMATION_AND_COMMUNICATION_TECHNOLOGY_MANAGERS = '1136'
    RESEARCH_AND_DEVELOPMENT_MANAGERS = '1137'
    QUALITY_ASSURANCE_MANAGERS = '1141'
    CUSTOMER_CARE_MANAGERS = '1142'
    FINANCIAL_INSTITUTION_MANAGERS = '1151'
    OFFICE_MANAGERS = '1152'
    TRANSPORT_AND_DISTRIBUTION_MANAGERS = '1161'
    STORAGE_AND_WAREHOUSE_MANAGERS = '1162'
    RETAIL_AND_WHOLESALE_MANAGERS = '1163'
    OFFICERS_IN_ARMED_FORCES = '1171'
    POLICE_OFFICERS_INSPECTORS_AND_ABOVE = '1172'
    SENIOR_OFFICERS_IN_FIRE__AMBULANCE__PRISON_ETC_SERVICES = '1173'
    SECURITY_MANAGERS = '1174'
    HOSPITAL_AND_HEALTH_SERVICE_MANAGERS = '1181'
    PHARMACY_MANAGERS = '1182'
    HEALTHCARE_PRACTICE_MANAGERS = '1183'
    SOCIAL_SERVICES_MANAGERS = '1184'
    RESIDENTIAL_AND_DAY_CARE_MANAGERS = '1185'
    FARM_MANAGERS = '1211'
    NATURAL_ENVIRONMENT_AND_CONSERVATION_MANAGERS = '1212'
    MANAGERS_IN_ANIMAL_HUSBANDRY__FORESTRY_AND_FISHING_N_E_C = '1219'
    HOTEL_AND_ACCOMMODATION_MANAGERS = '1221'
    CONFERENCE_AND_EXHIBITION_MANAGERS = '1222'
    RESTAURANT_AND_CATERING_MANAGERS = '1223'
    PUBLICANS_AND_MANAGERS_OF_LICENSED_PREMISES = '1224'
    LEISURE_AND_SPORTS_MANAGERS = '1225'
    TRAVEL_AGENCY_MANAGERS = '1226'
    PROPERTY__HOUSING_AND_LAND_MANAGERS = '1231'
    GARAGE_MANAGERS_AND_PROPRIETORS = '1232'
    HAIRDRESSING_AND_BEAUTY_SALON_MANAGERS_AND_PROPRIETORS = '1233'
    SHOPKEEPERS_AND_WHOLESALERETAIL_DEALERS = '1234'
    RECYCLING_AND_REFUSE_DISPOSAL_MANAGERS = '1235'
    MANAGERS_AND_PROPRIETORS_IN_OTHER_SERVICES_N_E_C = '1239'
    CHEMISTS = '2111'
    BIOLOGICAL_SCIENTISTS_AND_BIOCHEMISTS = '2112'
    PHYSICISTS__GEOLOGISTS_AND_METEOROLOGISTS = '2113'
    CIVIL_ENGINEERS = '2121'
    MECHANICAL_ENGINEERS = '2122'
    ELECTRICAL_ENGINEERS = '2123'
    ELECTRONICS_ENGINEERS = '2124'
    CHEMICAL_ENGINEERS = '2125'
    DESIGN_AND_DEVELOPMENT_ENGINEERS = '2126'
    PRODUCTION_AND_PROCESS_ENGINEERS = '2127'
    PLANNING_AND_QUALITY_CONTROL_ENGINEERS = '2128'
    ENGINEERING_PROFESSIONALS_N_E_C = '2129'
    IT_STRATEGY_AND_PLANNING_PROFESSIONALS = '2131'
    SOFTWARE_PROFESSIONALS = '2132'
    MEDICAL_PRACTITIONERS = '2211'
    PSYCHOLOGISTS = '2212'
    PHARMACISTSPHARMACOLOGISTS = '2213'
    OPHTHALMIC_OPTICIANS = '2214'
    DENTAL_PRACTITIONERS = '2215'
    VETERINARIANS = '2216'
    HIGHER_EDUCATION_TEACHING_PROFESSIONALS = '2311'
    FURTHER_EDUCATION_TEACHING_PROFESSIONALS = '2312'
    EDUCATION_OFFICERS__SCHOOL_INSPECTORS = '2313'
    SECONDARY_EDUCATION_TEACHING_PROFESSIONALS = '2314'
    PRIMARY_AND_NURSERY_EDUCATION_TEACHING_PROFESSIONALS = '2315'
    SPECIAL_NEEDS_EDUCATION_TEACHING_PROFESSIONALS = '2316'
    REGISTRARS_AND_SENIOR_ADMINISTRATORS_OF_EDUCATIONAL_PLACES = '2317'
    TEACHING_PROFESSIONALS_N_E_C = '2319'
    SCIENTIFIC_RESEARCHERS = '2321'
    SOCIAL_SCIENCE_RESEARCHERS = '2322'
    RESEARCHERS_N_E_C = '2329'
    SOLICITORS_AND_LAWYERS__JUDGES_AND_CORONERS = '2411'
    LEGAL_PROFESSIONALS_N_E_C = '2419'
    CHARTERED_AND_CERTIFIED_ACCOUNTANTS = '2421'
    MANAGEMENT_ACCOUNTANTS = '2422'
    MANAGEMENT_CONSULTANTS__ECONOMISTS_AND_STATISTICIANS = '2423'
    ARCHITECTS = '2431'
    TOWN_PLANNERS = '2432'
    QUANTITY_SURVEYORS = '2433'
    CHARTERED_SURVEYORS_NOT_QUANTITY_SURVEYORS = '2434'
    PUBLIC_SERVICE_ADMINISTRATIVE_PROFESSIONALS = '2441'
    SOCIAL_WORKERS = '2442'
    PROBATION_OFFICERS = '2443'
    CLERGY = '2444'
    LIBRARIANS = '2451'
    ARCHIVISTS_AND_CURATORS = '2452'
    LABORATORY_TECHNICIANS = '3111'
    ELECTRICALELECTRONICS_TECHNICIANS = '3112'
    ENGINEERING_TECHNICIANS = '3113'
    BUILDING_AND_CIVIL_ENGINEERING_TECHNICIANS = '3114'
    QUALITY_ASSURANCE_TECHNICIANS = '3115'
    SCIENCE_AND_ENGINEERING_TECHNICIANS_N_E_C = '3119'
    ARCHITECTURAL_TECHNOLOGISTS_AND_TOWN_PLANNING_TECHNICIANS = '3121'
    DRAUGHTSPERSONS = '3122'
    BUILDING_INSPECTORS = '3123'
    IT_OPERATIONS_TECHNICIANS = '3131'
    IT_USER_SUPPORT_TECHNICIANS = '3132'
    NURSES = '3211'
    MIDWIVES = '3212'
    PARAMEDICS = '3213'
    MEDICAL_RADIOGRAPHERS = '3214'
    CHIROPODISTS = '3215'
    DISPENSING_OPTICIANS = '3216'
    PHARMACEUTICAL_DISPENSERS = '3217'
    MEDICAL_AND_DENTAL_TECHNICIANS = '3218'
    PHYSIOTHERAPISTS = '3221'
    OCCUPATIONAL_THERAPISTS = '3222'
    SPEECH_AND_LANGUAGE_THERAPISTS = '3223'
    THERAPISTS_N_E_C = '3229'
    YOUTH_AND_COMMUNITY_WORKERS = '3231'
    HOUSING_AND_WELFARE_OFFICERS = '3232'
    NCOS_AND_OTHER_RANKS = '3311'
    POLICE_OFFICERS_SERGEANT_AND_BELOW = '3312'
    FIRE_SERVICE_OFFICERS_LEADING_FIRE_OFFICER_AND_BELOW = '3313'
    PRISON_SERVICE_OFFICERS_BELOW_PRINCIPAL_OFFICER = '3314'
    PROTECTIVE_SERVICE_ASSOCIATE_PROFESSIONALS_N_E_C = '3319'
    ARTISTS = '3411'
    AUTHORS__WRITERS = '3412'
    ACTORS__ENTERTAINERS = '3413'
    DANCERS_AND_CHOREOGRAPHERS = '3414'
    MUSICIANS = '3415'
    ARTS_OFFICERS__PRODUCERS_AND_DIRECTORS = '3416'
    GRAPHIC_DESIGNERS = '3421'
    PRODUCT__CLOTHING_AND_RELATED_DESIGNERS = '3422'
    JOURNALISTS__NEWSPAPER_AND_PERIODICAL_EDITORS = '3431'
    BROADCASTING_ASSOCIATE_PROFESSIONALS = '3432'
    PUBLIC_RELATIONS_OFFICERS = '3433'
    PHOTOGRAPHERS_AND_AUDIO_VISUAL_EQUIPMENT_OPERATORS = '3434'
    SPORTS_PLAYERS = '3441'
    SPORTS_COACHES__INSTRUCTORS_AND_OFFICIALS = '3442'
    FITNESS_INSTRUCTORS = '3443'
    SPORTS_AND_FITNESS_OCCUPATIONS_N_E_C = '3449'
    AIR_TRAFFIC_CONTROLLERS = '3511'
    AIRCRAFT_PILOTS_AND_FLIGHT_ENGINEERS = '3512'
    SHIP_AND_HOVERCRAFT_OFFICERS = '3513'
    TRAIN_DRIVERS = '3514'
    LEGAL_ASSOCIATE_PROFESSIONALS = '3520'
    ESTIMATORS__VALUERS_AND_ASSESSORS = '3531'
    BROKERS = '3532'
    INSURANCE_UNDERWRITERS = '3533'
    FINANCE_AND_INVESTMENT_ANALYSTSADVISERS = '3534'
    TAXATION_EXPERTS = '3535'
    IMPORTERS__EXPORTERS = '3536'
    FINANCIAL_AND_ACCOUNTING_TECHNICIANS = '3537'
    BUSINESS_AND_RELATED_ASSOCIATE_PROFESSIONALS_N_E_C = '3539'
    BUYERS_AND_PURCHASING_OFFICERS = '3541'
    SALES_REPRESENTATIVES = '3542'
    MARKETING_ASSOCIATE_PROFESSIONALS = '3543'
    ESTATE_AGENTS__AUCTIONEERS = '3544'
    CONSERVATION_AND_ENVIRONMENTAL_PROTECTION_OFFICERS = '3551'
    COUNTRYSIDE_AND_PARK_RANGERS = '3552'
    PUBLIC_SERVICE_ASSOCIATE_PROFESSIONALS = '3561'
    PERSONNEL_AND_INDUSTRIAL_RELATIONS_OFFICERS = '3562'
    VOCATIONAL_AND_INDUSTRIAL_TRAINERS_AND_INSTRUCTORS = '3563'
    CAREERS_ADVISERS_AND_VOCATIONAL_GUIDANCE_SPECIALISTS = '3564'
    INSPECTORS_OF_FACTORIES__UTILITIES_AND_TRADING_STANDARDS = '3565'
    STATUTORY_EXAMINERS = '3566'
    OCCUPATIONAL_HYGIENISTS_AND_SAFETY_OFFICERS_HEALTH_AND_SAFETY = '3567'
    ENVIRONMENTAL_HEALTH_OFFICERS = '3568'
    CIVIL_SERVICE_EXECUTIVE_OFFICERS = '4111'
    CIVIL_SERVICE_ADMINISTRATIVE_OFFICERS_AND_ASSISTANTS = '4112'
    LOCAL_GOVERNMENT_CLERICAL_OFFICERS_AND_ASSISTANTS = '4113'
    OFFICERS_OF_NON_GOVERNMENTAL_ORGANISATIONS = '4114'
    CREDIT_CONTROLLERS = '4121'
    ACCOUNTS__WAGES_AND_OTHER_FINANCIAL_CLERKS__BOOKKEEPERS = '4122'
    COUNTER_CLERKS = '4123'
    FILING_AND_OTHER_RECORDS_ASSISTANTSCLERKS = '4131'
    PENSIONS_AND_INSURANCE_CLERKS = '4132'
    STOCK_CONTROL_CLERKS = '4133'
    TRANSPORT_AND_DISTRIBUTION_CLERKS = '4134'
    LIBRARY_ASSISTANTSCLERKS = '4135'
    DATABASE_ASSISTANTSCLERKS = '4136'
    MARKET_RESEARCH_INTERVIEWERS = '4137'
    TELEPHONISTS = '4141'
    COMMUNICATION_OPERATORS = '4142'
    GENERAL_OFFICE_ASSISTANTSCLERKS = '4150'
    MEDICAL_SECRETARIES = '4211'
    LEGAL_SECRETARIES = '4212'
    SCHOOL_SECRETARIES = '4213'
    COMPANY_SECRETARIES = '4214'
    PERSONAL_ASSISTANTS_AND_OTHER_SECRETARIES = '4215'
    RECEPTIONISTS = '4216'
    TYPISTS = '4217'
    FARMERS = '5111'
    HORTICULTURAL_TRADES = '5112'
    GARDENERS_AND_GROUNDSMENGROUNDSWOMEN = '5113'
    AGRICULTURAL_AND_FISHING_TRADES_N_E_C = '5119'
    SMITHS_AND_FORGE_WORKERS = '5211'
    MOULDERS__CORE_MAKERS__DIE_CASTERS = '5212'
    SHEET_METAL_WORKERS = '5213'
    METAL_PLATE_WORKERS__SHIPWRIGHTS__RIVETERS = '5214'
    WELDING_TRADES = '5215'
    PIPE_FITTERS = '5216'
    METAL_MACHINING_SETTERS_AND_SETTER_OPERATORS = '5221'
    TOOL_MAKERS__TOOL_FITTERS_AND_MARKERS_OUT = '5222'
    METAL_WORKING_PRODUCTION_AND_MAINTENANCE_FITTERS = '5223'
    PRECISION_INSTRUMENT_MAKERS_AND_REPAIRERS = '5224'
    MOTOR_MECHANICS__AUTO_ENGINEERS = '5231'
    VEHICLE_BODY_BUILDERS_AND_REPAIRERS = '5232'
    AUTO_ELECTRICIANS = '5233'
    VEHICLE_SPRAY_PAINTERS = '5234'
    ELECTRICIANS__ELECTRICAL_FITTERS = '5241'
    TELECOMMUNICATIONS_ENGINEERS = '5242'
    LINES_REPAIRERS_AND_CABLE_JOINTERS = '5243'
    TV__VIDEO_AND_AUDIO_ENGINEERS = '5244'
    COMPUTER_ENGINEERS__INSTALLATION_AND_MAINTENANCE = '5245'
    ELECTRICALELECTRONICS_ENGINEERS_N_E_C = '5249'
    STEEL_ERECTORS = '5311'
    BRICKLAYERS__MASONS = '5312'
    ROOFERS__ROOF_TILERS_AND_SLATERS = '5313'
    PLUMBERS__HEATING_AND_VENTILATING_ENGINEERS = '5314'
    CARPENTERS_AND_JOINERS = '5315'
    GLAZIERS__WINDOW_FABRICATORS_AND_FITTERS = '5316'
    CONSTRUCTION_TRADES_N_E_C = '5319'
    PLASTERERS = '5321'
    FLOORERS_AND_WALL_TILERS = '5322'
    PAINTERS_AND_DECORATORS = '5323'
    WEAVERS_AND_KNITTERS = '5411'
    UPHOLSTERERS = '5412'
    LEATHER_AND_RELATED_TRADES = '5413'
    TAILORS_AND_DRESSMAKERS = '5414'
    TEXTILES__GARMENTS_AND_RELATED_TRADES_N_E_C = '5419'
    ORIGINATORS__COMPOSITORS_AND_PRINT_PREPARERS = '5421'
    PRINTERS = '5422'
    BOOKBINDERS_AND_PRINT_FINISHERS = '5423'
    SCREEN_PRINTERS = '5424'
    BUTCHERS__MEAT_CUTTERS = '5431'
    BAKERS__FLOUR_CONFECTIONERS = '5432'
    FISHMONGERS__POULTRY_DRESSERS = '5433'
    CHEFS__COOKS = '5434'
    GLASS_AND_CERAMICS_MAKERS__DECORATORS_AND_FINISHERS = '5491'
    FURNITURE_MAKERS__OTHER_CRAFT_WOODWORKERS = '5492'
    PATTERN_MAKERS_MOULDS = '5493'
    MUSICAL_INSTRUMENT_MAKERS_AND_TUNERS = '5494'
    GOLDSMITHS__SILVERSMITHS__PRECIOUS_STONE_WORKERS = '5495'
    FLORAL_ARRANGERS__FLORISTS = '5496'
    HAND_CRAFT_OCCUPATIONS_N_E_C = '5499'
    NURSING_AUXILIARIES_AND_ASSISTANTS = '6111'
    AMBULANCE_STAFF_EXCLUDING_PARAMEDICS = '6112'
    DENTAL_NURSES = '6113'
    HOUSEPARENTS_AND_RESIDENTIAL_WARDENS = '6114'
    CARE_ASSISTANTS_AND_HOME_CARERS = '6115'
    NURSERY_NURSES = '6121'
    CHILDMINDERS_AND_RELATED_OCCUPATIONS = '6122'
    PLAYGROUP_LEADERSASSISTANTS = '6123'
    EDUCATIONAL_ASSISTANTS = '6124'
    VETERINARY_NURSES_AND_ASSISTANTS = '6131'
    ANIMAL_CARE_OCCUPATIONS_N_E_C = '6139'
    SPORTS_AND_LEISURE_ASSISTANTS = '6211'
    TRAVEL_AGENTS = '6212'
    TRAVEL_AND_TOUR_GUIDES = '6213'
    AIR_TRAVEL_ASSISTANTS = '6214'
    RAIL_TRAVEL_ASSISTANTS = '6215'
    LEISURE_AND_TRAVEL_SERVICE_OCCUPATIONS_N_E_C = '6219'
    HAIRDRESSERS__BARBERS = '6221'
    BEAUTICIANS_AND_RELATED_OCCUPATIONS = '6222'
    HOUSEKEEPERS_AND_RELATED_OCCUPATIONS = '6231'
    CARETAKERS = '6232'
    UNDERTAKERS_AND_MORTUARY_ASSISTANTS = '6291'
    PEST_CONTROL_OFFICERS = '6292'
    SALES_AND_RETAIL_ASSISTANTS = '7111'
    RETAIL_CASHIERS_AND_CHECK_OUT_OPERATORS = '7112'
    TELEPHONE_SALESPERSONS = '7113'
    COLLECTOR_SALESPERSONS_AND_CREDIT_AGENTS = '7121'
    DEBT__RENT_AND_OTHER_CASH_COLLECTORS = '7122'
    ROUNDSMENWOMEN_AND_VAN_SALESPERSONS = '7123'
    MARKET_AND_STREET_TRADERS_AND_ASSISTANTS = '7124'
    MERCHANDISERS_AND_WINDOW_DRESSERS = '7125'
    SALES_RELATED_OCCUPATIONS_N_E_C = '7129'
    CALL_CENTRE_AGENTSOPERATORS = '7211'
    CUSTOMER_CARE_OCCUPATIONS = '7212'
    FOOD__DRINK_AND_TOBACCO_PROCESS_OPERATIVES = '8111'
    GLASS_AND_CERAMICS_PROCESS_OPERATIVES = '8112'
    TEXTILE_PROCESS_OPERATIVES = '8113'
    CHEMICAL_AND_RELATED_PROCESS_OPERATIVES = '8114'
    RUBBER_PROCESS_OPERATIVES = '8115'
    PLASTICS_PROCESS_OPERATIVES = '8116'
    METAL_MAKING_AND_TREATING_PROCESS_OPERATIVES = '8117'
    ELECTROPLATERS = '8118'
    PROCESS_OPERATIVES_N_E_C = '8119'
    PAPER_AND_WOOD_MACHINE_OPERATIVES = '8121'
    COAL_MINE_OPERATIVES = '8122'
    QUARRY_WORKERS_AND_RELATED_OPERATIVES = '8123'
    ENERGY_PLANT_OPERATIVES = '8124'
    METAL_WORKING_MACHINE_OPERATIVES = '8125'
    WATER_AND_SEWERAGE_PLANT_OPERATIVES = '8126'
    PLANT_AND_MACHINE_OPERATIVES_N_E_C = '8129'
    ASSEMBLERS_ELECTRICAL_PRODUCTS = '8131'
    ASSEMBLERS_VEHICLES_AND_METAL_GOODS = '8132'
    ROUTINE_INSPECTORS_AND_TESTERS = '8133'
    WEIGHERS__GRADERS__SORTERS = '8134'
    TYRE__EXHAUST_AND_WINDSCREEN_FITTERS = '8135'
    CLOTHING_CUTTERS = '8136'
    SEWING_MACHINISTS = '8137'
    ROUTINE_LABORATORY_TESTERS = '8138'
    ASSEMBLERS_AND_ROUTINE_OPERATIVES_N_E_C = '8139'
    SCAFFOLDERS__STAGERS__RIGGERS = '8141'
    ROAD_CONSTRUCTION_OPERATIVES = '8142'
    RAIL_CONSTRUCTION_AND_MAINTENANCE_OPERATIVES = '8143'
    CONSTRUCTION_OPERATIVES_N_E_C = '8149'
    HEAVY_GOODS_VEHICLE_DRIVERS = '8211'
    VAN_DRIVERS = '8212'
    BUS_AND_COACH_DRIVERS = '8213'
    TAXI__CAB_DRIVERS_AND_CHAUFFEURS = '8214'
    DRIVING_INSTRUCTORS = '8215'
    RAIL_TRANSPORT_OPERATIVES = '8216'
    SEAFARERS_MERCHANT_NAVY_BARGE_AND_BOAT_OPERATIVES = '8217'
    AIR_TRANSPORT_OPERATIVES = '8218'
    TRANSPORT_OPERATIVES_N_E_C = '8219'
    CRANE_DRIVERS = '8221'
    FORK_LIFT_TRUCK_DRIVERS = '8222'
    AGRICULTURAL_MACHINERY_DRIVERS = '8223'
    MOBILE_MACHINE_DRIVERS_AND_OPERATIVES_N_E_C = '8229'
    FARM_WORKERS = '9111'
    FORESTRY_WORKERS = '9112'
    FISHING_AND_AGRICULTURE_RELATED_OCCUPATIONS_N_E_C = '9119'
    LABOURERS_IN_BUILDING_AND_WOODWORKING_TRADES = '9121'
    LABOURERS_IN_OTHER_CONSTRUCTION_TRADES_N_E_C = '9129'
    LABOURERS_IN_FOUNDRIES = '9131'
    INDUSTRIAL_CLEANING_PROCESS_OCCUPATIONS = '9132'
    PRINTING_MACHINE_MINDERS_AND_ASSISTANTS = '9133'
    PACKERS__BOTTLERS__CANNERS__FILLERS = '9134'
    LABOURERS_IN_PROCESS_AND_PLANT_OPERATIONS_N_E_C = '9139'
    STEVEDORES__DOCKERS_AND_SLINGERS = '9141'
    OTHER_GOODS_HANDLING_AND_STORAGE_OCCUPATIONS_N_E_C = '9149'
    POSTAL_WORKERS__MAIL_SORTERS__MESSENGERS__COURIERS = '9211'
    ELEMENTARY_OFFICE_OCCUPATIONS_N_E_C = '9219'
    HOSPITAL_PORTERS = '9221'
    HOTEL_PORTERS = '9222'
    KITCHEN_AND_CATERING_ASSISTANTS = '9223'
    WAITERS__WAITRESSES = '9224'
    BAR_STAFF = '9225'
    LEISURE_AND_THEME_PARK_ATTENDANTS = '9226'
    ELEMENTARY_PERSONAL_SERVICES_OCCUPATIONS_N_E_C = '9229'
    WINDOW_CLEANERS = '9231'
    ROAD_SWEEPERS = '9232'
    CLEANERS__DOMESTICS = '9233'
    LAUNDERERS__DRY_CLEANERS__PRESSERS = '9234'
    REFUSE_AND_SALVAGE_OCCUPATIONS = '9235'
    ELEMENTARY_CLEANING_OCCUPATIONS_N_E_C = '9239'
    SECURITY_GUARDS_AND_RELATED_OCCUPATIONS = '9241'
    TRAFFIC_WARDENS = '9242'
    SCHOOL_CROSSING_PATROL_ATTENDANTS = '9243'
    SCHOOL_MID_DAY_ASSISTANTS = '9244'
    CAR_PARK_ATTENDANTS = '9245'
    ELEMENTARY_SECURITY_OCCUPATIONS_N_E_C = '9249'
    SHELF_FILLERS = '9251'
    ELEMENTARY_SALES_OCCUPATIONS_N_E_C = '9259'
    IN_WORK_OR_EVER_WORKED___DK_REFUSE_OCCUPATION = '9999'


class SIC2(OrderedEnum):
    INELIGIBLE___NO_SECOND_JOB = '-2'
    INELIGIBLE___UNDER_16YRS = '-1'
    N01_11GROWING_CEREALS__OTHER_CROPS = '111'
    N01_12GROWING_VEG_HORTICULTURE_NURSERY = '112'
    N01_13GRWG_FRUIT_NUT_BEVERGE_SPICE_CROP = '113'
    N01_21FARMING_CATTLE_DAIRY = '121'
    N01_22FARMING_SHEEP_GOATS_HORSES_ETC = '122'
    N01_23FARMING_PIGS = '123'
    N01_24FARMING_POULTRY = '124'
    N01_25FARMING_OTHER_ANIMALS = '125'
    N01_30MIXED_FARMING_CROPS_AND_ANIMALS = '130'
    N01_41AGRICULTURAL_SERVICES = '141'
    N01_42ANIMAL_HUSBDRY_SERVICE_NOT_VET = '142'
    N01_50HUNTING_TRAPPING_GAME_ETC = '150'
    N02_01FORESTRY_LOGGING = '201'
    N02_02FORESTRY_LOGGING_SERVICES = '202'
    N05_01FISHING = '501'
    N05_02FISH_HATCHERIES_FARMS = '502'
    N10_101_103MINING_AND_AGGLOMERATION_OF_HARD_COAL = '1010'
    N10_20LIGNITE_MINING_AGGLOMERATION = '1020'
    N10_30PEAT_EXTRACTION_AGGLOMERATION = '1030'
    N11_10CRUDE_OIL_GAS_EXTRACTION = '1110'
    N11_20OIL_GAS_SERVICES_NOT_SURVEYING = '1120'
    N12_00URANIUM_THORIUM_ORE_MINING = '1200'
    N13_10IRON_ORE_MINING = '1310'
    N13_20NON_FERROUS_MINE_NOT_URAN_THOR = '1320'
    N14_11QUARRYING_CONSTRUCTION_STONE = '1411'
    N14_12LIMESTONE_GYPSUM_CHALK_QUARRYING = '1412'
    N14_13SLATE_QUARRYING = '1413'
    N14_21GRAVEL_SAND_PITS = '1421'
    N14_22CLAY_KAOLIN_MINING = '1422'
    N14_30CHEMICAL_FERTILISER_MINING = '1430'
    N14_40SALT_PRODUCTION = '1440'
    N14_50OTHER_MINING_QUARRYING = '1450'
    N15_111_3SLAUGHT_NG_NOT_POULTRY_RABBIT_AND_PROCESS_ANIMLS = '1511'
    N15_12POULTRY_PRODUCTION_PRESERVING = '1512'
    N15_13MEAT_POULTRY_PRODUCTS = '1513'
    N15_20FISH_FISH_PRODUCTS_PRESERVING = '1520'
    N15_31POTATO_PRODUCTS_PRESERVING = '1531'
    N15_32FRUIT_VEGETABLE_JUICE_PROCESSING = '1532'
    N15_33OTHER_FRUIT_VEG_PROCESSING = '1533'
    N15_41CRUDE_OILS_FATS_MANUFACTURE = '1541'
    N15_42REFINED_OILS_FATS_MANUFACTURE = '1542'
    N15_43MARGARINE_EDIBLE_FAT_MANUFACTURE = '1543'
    N15_51DAIRIES_CHEESE_MAKING = '1551'
    N15_52ICE_CREAM_MANUFACTURE = '1552'
    N15_61GRAIN_MILL_PRODUCTS = '1561'
    N15_62STARCHES_STARCH_PRODUCTS = '1562'
    N15_71FARM_ANIMAL_FEED_MANUFACTURE = '1571'
    N15_72PET_FOOD_MANUFACTURE = '1572'
    N15_81BREAD_FRESH_PASTRY_CAKES_MANUFACT_ = '1581'
    N15_82BISCUITS_RUSKS_PRESERVED_PASTRIES = '1582'
    N15_83SUGAR_MANUFACTURE = '1583'
    N15_84CHOCOLATE_COCOA_SUGAR_CONFECT_Y = '1584'
    N15_85MACARONI_NOODLES_COUSCOUS_ETC = '1585'
    N15_86TEA_COFFEE_MANUFACTURE = '1586'
    N15_87CONDIMENT_SEASONING_MANUFACTURE = '1587'
    N15_88HOMOGENISED_DIETETIC_FOOD_PRODUCTS = '1588'
    N15_89OTHER_FOOD_PRODUCTS_MANUFACTURE = '1589'
    N15_91DISTILLED_ALCOHOLIC_DRINKS = '1591'
    N15_92ETHYL_ALCOHOL_FROM_FERMENTATION = '1592'
    N15_93WINE_PRODUCTION = '1593'
    N15_94CIDER_OTHER_FRUIT_WINE_PRODUCTION = '1594'
    N15_95NON_DISTILLED_FERMENTED_DRINKS = '1595'
    N15_96BEER_PRODUCTION = '1596'
    N15_97MALT_PRODUCTION = '1597'
    N15_98MINERAL_WATER_SOFT_DRINK_PRODCTN_ = '1598'
    N16_00TOBACCO_PRODUCTS = '1600'
    N17_11COTTON_FIBRE_PREPARATION = '1711'
    N17_12WOOL_FIBRE_PREPARATION = '1712'
    N17_13WORSTED_FIBRE_PREPARATION = '1713'
    N17_14FLAX_FIBRE_PREPARATION = '1714'
    N17_15SILK_SYNTHETIC_PREPARATION = '1715'
    N17_16SEWING_THREAD_MANUFACTURE = '1716'
    N17_17OTHER_TEXTILE_PREPARATION = '1717'
    N17_21COTTON_WEAVING = '1721'
    N17_22WOOLLEN_WEAVING = '1722'
    N17_23WORSTED_WEAVING = '1723'
    N17_24SILK_WEAVING = '1724'
    N17_25OTHER_TEXTILE_WEAVING = '1725'
    N17_30TEXTILE_FINISHING = '1730'
    N17_401_403SOFT_FURNISHING_AND_HHLD_TEXTILE_MANUFACTURE = '1740'
    N17_511_3CARPETS_AND_RUG_MANUFACTURE = '1751'
    N17_52CORDAGE_ROPE_TWINE_MANUFACTURE = '1752'
    N17_53NON_WOVEN_ARTICLES_NOT_CLOTHING = '1753'
    N17_541_543LACE__NARROW_FABRICS_AND_OTHER_TEXTILE_MANUF_ = '1754'
    N17_60KNITTED_CROCHETED_FABRIC_MANUF_ = '1760'
    N17_71KNITTED_CROCHETED_HOSIERY_MANUF_ = '1771'
    N17_72KNITTED_CROCHETED_CLOTHING = '1772'
    N18_10LEATHER_CLOTHING_MANUFACTURE = '1810'
    N18_21WORKWEAR_MANUFACTURE = '1821'
    N18_221_222_OTHER_MENSWOMEN_S_OUTERWEAR_MANUF_ = '1822'
    N18_231_232_MENSWOMEN_S_UNDERWEAR_MANUFACTURE = '1823'
    N18_241_242_HAT_ACCESSORIES_MANUFACTURE = '1824'
    N18_30FUR_PROCESSING = '1830'
    N19_10LEATHER_TANNING_DRESSING = '1910'
    N19_20LUGGAGE_HANDBAGS_SADDLERY_MANUF_ = '1920'
    N19_30FOOTWEAR_MANUFACTURE = '1930'
    N20_10WOOD_SAWMILL_PLANING_IMPREGNATION = '2010'
    N20_20WOOD_VENEER_PLYWOOD_ETC_PRODUCTION = '2020'
    N20_30BUILDERS_CARPENTRY_JOINERY = '2030'
    N20_40WOODED_CONTAINERS_MANUFACTURE = '2040'
    N20_51OTHER_WOOD_PRODUCTS_MANUFACTURE = '2051'
    N20_52CORK_STRAW_ETC_MANUFACTURE = '2052'
    N21_11PULP_MANUFACTURE = '2111'
    N21_12PAPER_CARD_MANUFACTURE = '2112'
    N21_211_212PAPER_BOARD_SACKS_BAGS_BOXES_ETC_MANUF_ = '2121'
    N21_22SANITARY_TOILET_REQUIS__PRODUCTION = '2122'
    N21_23PAPER_STATIONARY_MANUFACTURE = '2123'
    N21_24WALLPAPER_MANUFACTURE = '2124'
    N21_25OTHER_PAPER_ARTICLES_MANUFACTURE = '2125'
    N22_11BOOK_PUBLISHING = '2211'
    N22_12NEWSPAPER_PUBLISHING = '2212'
    N22_13JOURNAL_PERIODICAL_PUBLISHING = '2213'
    N22_14SOUND_RECORDING_PUBLISHING = '2214'
    N22_15OTHER_PUBLISHING = '2215'
    N22_21NEWSPAPER_PRINTING = '2221'
    N22_22OTHER_PRINTING = '2222'
    N22_23BOOKBINDING_FINISHING = '2223'
    N22_24COMPOSITION_PLATE_MAKING = '2224'
    N22_25OTHER_PRINTING_ACTIVITIES = '2225'
    N22_31REPRODUCTION_OF_SOUND_RECORDING = '2231'
    N22_32REPRODUCTION_OF_VIDEO_RECORDING = '2232'
    N22_33REPRODUCTION_OF_COMPUTER_MEDIA = '2233'
    N23_10COKE_OVEN_PRODUCTS_MANUFACTURE = '2310'
    N23_201_202_MANUF_OF_REFINED_PETROLEUM_PRODUCTS = '2320'
    N23_30NUCLEAR_FUEL_PROCESSING = '2330'
    N24_11INDUSTRIAL_GAS_MANUFACTURE = '2411'
    N24_12DYE_PIGMENT_MANUFACTURE = '2412'
    N24_13INORGANIC_CHEMICAL_MANUFACTURE = '2413'
    N24_14ORGANIC_CHEMICAL_MANUFACTURE = '2414'
    N24_15FERTILIZER_ETC_MANUFACTURE = '2415'
    N24_16PRIMARY_PLASTICS_MANUFACTURE = '2416'
    N24_17PRIMARY_SYNTHETIC_RUBBER = '2417'
    N24_20PESTICIDES_ETC_MANUFACTURE = '2420'
    N24_301_303PAINT_VARNSH_PRINTING_INK__MASTIC_MAN = '2430'
    N24_41BASIC_PHARMACEUTICAL_MANUFACTURE = '2441'
    N24_42PHARMACEUTICAL_PREPARATIONS_MAN_ = '2442'
    N24_511_512SOAP_DETERGENT_CLEANING_POLISHING_AGENT_MAN = '2451'
    N24_52PERFUMES_ETC_MANUFACTURE = '2452'
    N24_61EXPLOSIVES_MANUFACTURE = '2461'
    N24_62GLUES_ETC_MANUFACTURE = '2462'
    N24_63ESSENTIAL_OILS_MANUFACTURE = '2463'
    N24_64PHOTOGRAPHIC_CHEMICALS_MAN_ = '2464'
    N24_65RECORDING_MEDIA_MANUFACTURE = '2465'
    N24_66OTHER_CHEMICAL_PRODUCTS_MAN_ = '2466'
    N24_70MAN_MADE_FIBRES_MANUFACTURE = '2470'
    N25_11RUBBER_TYRES_ETC_MANUFACTURE = '2511'
    N25_12RUBBER_TYRES_RETREADING_ETC = '2512'
    N25_13OTHER_RUBBER_PRODUCTS_MANUFACTURE = '2513'
    N25_21PLASTIC_SHEETS_TUBES_ETC_MAN_ = '2521'
    N25_22PLASTIC_PACKING_MANUFACTURE = '2522'
    N25_231_232PLASTIC_FLOORING_AND_OTHER_PLASTIC_BLDNG_WARES_MAN = '2523'
    N25_24MANUF_OF_OTHER_PLASTIC_PRODUCTS = '2524'
    N26_11FLAT_GLASS_MANUFACTURE = '2611'
    N26_12FLAT_GLASS_SHAPING_PROCESSING = '2612'
    N26_13HOLLOW_GLASS_MANUFACTURE = '2613'
    N26_14GLASS_FIBRE_MANUFACTURE = '2614'
    N26_15OTHER_GLASS_PROC_MANUFACTURE = '2615'
    N26_21CERAMIC_HHLD_ORNAMENTAL_MAN_ = '2621'
    N26_22CERAMIC_SANITARY_FIXTURES_MAN_ = '2622'
    N26_23CERAMIC_INSULATORS_ETC_MAN_ = '2623'
    N26_24OTHER_TECHNICAL_CERAMIC_MAN_ = '2624'
    N26_25OTHER_CERAMIC_MANUFACTURE = '2625'
    N26_26REFRACTORY_CERAMIC_MANUFACTURE = '2626'
    N26_30CERAMIC_TILE_FLAGS_MANUFACTURE = '2630'
    N26_40BRICKS_TILES_ETC_MANUFACTURE = '2640'
    N26_51CEMENT_MANUFACTURE = '2651'
    N26_52LIME_MANUFACTURE = '2652'
    N26_53PLASTER_MANUFACTURE = '2653'
    N26_61CONCRETE_PRODSCONSTRUCTIONMAN_ = '2661'
    N26_62PLASTER_PRODUCTSCONSTRUCTIONMAN_ = '2662'
    N26_63READY_MIXED_CONCRETE_MANUFACTURE = '2663'
    N26_64MORTARS_MANUFACTURE = '2664'
    N26_65FIBRE_CEMENT_MANUFACTURE = '2665'
    N26_66OTHER_CONCRETE_PLASTER_ETC_MAN_ = '2666'
    N26_70STONE_CUTTING_SHAPING = '2670'
    N26_81ABRASIVE_PRODUCTS_MANUFACTURE = '2681'
    N26_821_822ASBESTOS_AND_OTH_NON_METAL_MINERAL_PROD_MAN_ = '2682'
    N27_10BASIC_IRON_STEEL_FERRO_ALLOYS_MAN_ = '2710'
    N27_21CAST_IRON_TUBES_MANUFACTURE = '2721'
    N27_22STEEL_TUBES_MANUFACTURE = '2722'
    N27_31COLD_DRAWING = '2731'
    N27_32COLD_ROLLINGNARROW_STRIP = '2732'
    N27_33COLD_FORMING_FOLDING = '2733'
    N27_34WIRE_DRAWING = '2734'
    N27_35OTHER_1ST_PROC_IRON_STEEL = '2735'
    N27_41PRECIOUS_METALS_PRODUCTION = '2741'
    N27_42ALUMINIUM_PRODUCTION = '2742'
    N27_43LEAD_ZINC_TIN_PRODUCTION = '2743'
    N27_44COPPER_PRODUCTION = '2744'
    N27_45OTHER_NON_METAL_PRODUCTION = '2745'
    N27_51IRON_CASTING = '2751'
    N27_52STEEL_CASTING = '2752'
    N27_53LIGHT_METALS_CASTING = '2753'
    N27_54OTHER_NON_FERROUS_CASTING = '2754'
    N28_11METAL_STRUCTURES_ETC_MANUFACTURE = '2811'
    N28_12BUILDERS_METAL_WORK = '2812'
    N28_21METAL_CONTAINERS_MANUFACTURE = '2821'
    N28_22RADIATORS_BOILERS_MANUFACTURE = '2822'
    N28_30STEAM_GENERATORS_MANUFACTURE = '2830'
    N28_40FORGING_PRESSING_ETC = '2840'
    N28_51TREATMENT_COATING_OF_METALS = '2851'
    N28_52GENERAL_MECH_ENGINEERING = '2852'
    N28_61CUTLERY_MANUFACTURE = '2861'
    N28_62TOOLS_MANUFACTURE = '2862'
    N28_63LOCKS_HINGES_ETC_MANUFACTURE = '2863'
    N28_71STEEL_DRUMS_ETC_MANUFACTURE = '2871'
    N28_72LIGHT_METAL_PACKAGING_MANUFACTURE = '2872'
    N28_73WIRE_PRODUCTS_MANUFACTURE = '2873'
    N28_74FASTENERS_CHAINS_ETC_MANUFACTURE = '2874'
    N28_75OTHER_METAL_PRODUCTS_MANUFACTURE = '2875'
    N29_11ENGINES_TURBINES_NOT_AIRCRAFT = '2911'
    N29_121_122_PUMPS_AND_COMPRESSOR_MANUFACTURE = '2912'
    N29_13TAPS_VALVES_MANUFACTURE = '2913'
    N29_14BEARINGS_GEARS_ETC_MANUFACTURE = '2914'
    N29_21FURNACE_MANUFACTURE = '2921'
    N29_22LIFTING_HANDLING_EQT_MANUFACTURE = '2922'
    N29_23COOL__VENTILAT_EQTNOT_DOMESTIC = '2923'
    N29_24OTHER_GEN_PURPOSE_MACH_MANUFACTURE = '2924'
    N29_31AGRICULTURAL_TRACTORS_MANUFACTURE = '2931'
    N29_32OTHER_AGRIC__FORESTRY_MACH__MAN_ = '2932'
    N29_40MACHINE_TOOL_MANUFACTURE = '2940'
    N29_51METALLURGY_MACH_MANUFACTURE = '2951'
    N29_521_523_MINING_ROADWK__EARTHMOVING_EQT_MAN_ = '2952'
    N29_53FOOD_TOBACCO_PROC_MACH = '2953'
    N29_54TEXTILE_ETC__LEATHER_MACH_MAN_ = '2954'
    N29_55PAPER_ETC_PROD_MACH_MANUFACTURE = '2955'
    N29_56OTHER_SPECIAL_PURPOSE_MACH_MAN_ = '2956'
    N29_60WEAPONS_AMMUNITION_MANUFACTURE = '2960'
    N29_71ELEC_DOMESTIC_APPLIANCES_MAN_ = '2971'
    N29_72NON_ELEC_DOMESTIC_APPLIANCES_MAN_ = '2972'
    N30_01OFFICE_MACH_MANUFACTURE = '3001'
    N30_02COMPUTERS__IT_EQT_MANUFACTURE = '3002'
    N31_10ELEC_MOTORS_GENTORS_TRANS_MAN_ = '3110'
    N31_20ELEC_DISTRIBUTION__CONTROL_MAN_ = '3120'
    N31_30INSULATED_CABLE_MANUFACTURE = '3130'
    N31_40ELECTRIC_BATTERY_MANUFACTURE = '3140'
    N31_50LIGHTING_EQT_MANUFACTURE = '3150'
    N31_61OTHER_ELEC_EQT_ENGINESVEH_MAN_ = '3161'
    N31_62OTHER_ELEC_EQT_MANUFACTURE = '3162'
    N32_10ELECTRONIC_COMPONENTS_ETC_MAN_ = '3210'
    N32_201_202_TELEPHONE__RADIO_ELECTRONIC_GOODS_MAN_ = '3220'
    N32_30TV_RADIO_HIFI_ETC_EQT_MANUFACTURE = '3230'
    N33_10MEDICAL_EQT_APPLIANCES_MANUFACTURE = '3310'
    N33_20TESTING_NAVIGATING_ETC_EQT_MAN_ = '3320'
    N33_30INDUSTRIAL_PROC_CONTROL_EQT_MAN_ = '3330'
    N33_401_403SPECTACLES__OPTICAL__PHOTOGRAPHIC_EQT_MAN_ = '3340'
    N33_50WATCHES_CLOCK_MANUFACTURE = '3350'
    N34_10MOTOR_VEH_MANUFACTURE = '3410'
    N34_201_203MOTOR_VEH_BODYWORK_TRAILERS_CARAVAN_MANU = '3420'
    N34_30MOTOR_VEH_PARTS_ETC_MANUFACTURE = '3430'
    N35_11SHIP_BUILDING_REPAIRING = '3511'
    N35_12BOAT_BUILDING_REPAIRING = '3512'
    N35_20RAIL_TRAM_ROLLING_STK_ETC_MAN_ = '3520'
    N35_30AIRCRAFT_SPACECRAFT_MANUFACTURE = '3530'
    N35_41MOTORCYCLE_MANUFACTURE = '3541'
    N35_42BICYCLE_MANUFACTURE = '3542'
    N35_43INVALID_CARRIAGE_MANUFACTURE = '3543'
    N35_50OTHER_TRANSPORT_EQT_MANUFACTURE = '3550'
    N36_11CHAIRS_ETC_MANUFACTURE = '3611'
    N36_12OTHER_OFFICE_SHOP_FURNITURE_MAN_ = '3612'
    N36_13OTHER_KITCHEN_FURNITURE_MAN_ = '3613'
    N36_14OTHER_FURNITURE_MANUFACTURE = '3614'
    N36_15MATTRESSES_MANUFACTURE = '3615'
    N36_21COINS_MEDAL_MANUFACTURE = '3621'
    N36_22JEWELLERY_ETC_MANUFACTURE = '3622'
    N36_30MUSICAL_INSTRUMENTS_MANUFACTURE = '3630'
    N36_40SPORTS_GOODS_MANUFACTURE = '3640'
    N36_501_502MANUF__OF_GANES_AND_TOYS = '3650'
    N36_61IMITATION_JEWELLERY_MANUFACTURE = '3661'
    N36_62BROOMS_BRUSHES_ETC_MANUFACTURE = '3662'
    N36_631_632STATIONERS_GOODS_AND_OTHER_MANUF = '3663'
    N37_10METAL_SCRAP_RECYCLING = '3710'
    N37_20NON_METAL_SCRAP_RECYCLING = '3720'
    N40_10ELEC_GENERATION_SUPPLY = '4010'
    N40_20GAS_PRODUCTION_SUPPLY = '4020'
    N40_30STEAM_HOT_WATER_SUPPLY = '4030'
    N41_00WATER_SUPPLY_ETC = '4100'
    N45_11DEMOLISH_BUILDINGS_EARTH_MOVING = '4511'
    N45_12TEST_DRILLING_AND_BORING = '4512'
    N45_21CONSTRUCT_BUILDINGS_AND_GENERAL_CIVIL_ENGINEERING = '4521'
    N45_22ERECTION_OF_ROOF_COVERING_AND_FRAMES = '4522'
    N45_23CONSTRUCTION_OF_ROADS__AIRFIELDS_AND_SPORTS_FACILITIES = '4523'
    N45_24CONSTRUCTION_OF_WATER_PROJECTS = '4524'
    N45_25OTHER_CONSTRUCTION_USING_SPECIAL_TRADES = '4525'
    N45_31INSTALLATION_OF_ELECTRICAL_WIRING_AND_FITTINGS = '4531'
    N45_32INSULATION_WORK_ACTIVITIES = '4532'
    N45_33PLUMBING = '4533'
    N45_34OTHER_BUILDING_INSTALLATION = '4534'
    N45_41PLASTERING = '4541'
    N45_42JOINERY_INSTALLATION = '4542'
    N45_43FLOOR_AND_WALL_COVERING = '4543'
    N45_44PAINTING_AND_GLAZING = '4544'
    N45_45OTHER_BUILDING_COMPLETION = '4545'
    N45_55RENT_CONSTRUCTION_DEMOL__EQUIP__WITH_OPERATOR = '4555'
    N50_10SALE_OF_MOTOR_VEHICLES = '5010'
    N50_20MOTOR_VEH_REPAIR = '5020'
    N50_30SALES_OF_MOTOR_VEH_PARTS_AND_ACCESSORIESR = '5030'
    N50_40MOTORCYCLE_SALE_REPAIR_ETC = '5040'
    N50_50RETAIL_SALE_OF_AUTOMOTIVE_FUEL = '5050'
    N50_11AGENTS_IN_WSALE_AGRIC_RAW_MATERIALS = '5111'
    N50_12AGENTS_IN_WSALE_FUEL__ORE__METAL__CHEMICALS = '5112'
    N50_13AGENTS_IN_WSALE_TIMBER_AND_BUILDING_MATERIALS = '5113'
    N50_14AGENTS_IN_WSALE_MCHNRY__INDSTRL_EQPT__SHIPS__AIRCRAFT = '5114'
    N50_15AGENTS_IN_WSALE_FURNITURE__HHLD_GOODS__HARDWARE = '5115'
    N50_16AGENTS_IN_WSALE_TEXTILES__CLOTHING__FOOTWEAR = '5116'
    N50_17AGENTS_IN_WSALE_FOOD__BEVERAGES_AND_TOBACCO = '5117'
    N50_18AGENTS_IN_WSALE_PRODUCTS_NOT_ELSEWHERE_CLASSIFIED = '5118'
    N50_19AGENTS_IN_WSALE_VARIETY_OF_GOODS = '5119'
    N50_21WHOLESALE_GRAIN__SEEDS_AND_ANIMAL_FEEDS = '5121'
    N50_22WHOLESALE_FLOWERS_AND_PLANTS = '5122'
    N50_23WHOLESALE_LIVE_ANIMALS = '5123'
    N50_24WHOLESALE_HIDES__SKINS_AND_LEATHER = '5124'
    N50_25WHOLESALE_UNMANUFACTURED_TOBACCO = '5125'
    N50_31WHOLESALE_FRUIT_AND_VEG = '5131'
    N50_32WHOLESALE_MEAT_AND_MEAT_PRODUCTS = '5132'
    N50_33WHOLESALE_DAIRY_PRODUCE__EGGS__EDIBLE_OILS = '5133'
    N50_34WHOLESALE_ALCOHOLIC_AND_OTHER_BEVERAGES = '5134'
    N50_35WHOLESALE_TOBACCO_PRODUCTS = '5135'
    N50_36WHOLESALE_SUGAR__CHOCOLATE_AND_SUGAR_CNFCTNRY = '5136'
    N50_37WHOLESALE_COFFEE__TEA__COCOA__SPICES = '5137'
    N50_38WHOLESALE_OTHER_FOOD_INCL_FISH = '5138'
    N50_39WHOLESALE_NON_SPECIALISED_OF_FOOD__DRINK__TOBACCO = '5139'
    N50_41WHOLESALE_TEXTILES = '5141'
    N50_42WHOLESALE_CLOTHING_AND_FOOTWEAR = '5142'
    N50_43WHOLESALE_ELCTRCL_HHLD_APPLIANCES__RADIO__TV = '5143'
    N50_44WHOLESALE_CHINA__GLASSWARE__WALLPAPER_CLEANING_MTRLS = '5144'
    N50_45WHOLESALE_PERFUME_AND_COSMETICS = '5145'
    N50_46WHOLESALE_PHARMACEUTICAL_GOODS = '5146'
    N50_47WHOLESALE_FURNITURE_AND_HHLD_GOOD_N_E_C = '5147'
    N50_51WHOLESALE_PETROLEUM_AND_FUELS = '5151'
    N50_52WHOLESALE_METAL_AND_METAL_ORES = '5152'
    N50_53WHOLESALE_WOOD_AND_CONSTRUCTION_MTRLS = '5153'
    N50_54WHOLESALE_HARDWARE__PLUMBING_AND_HEATING_EQUIP = '5154'
    N50_55WHOLESALE_CHEMICAL_PRODUCTS = '5155'
    N50_56WHOLESALE_OTHER_INTERMEDIATE_PRODUCTS = '5156'
    N50_57WHOLESALE_WASTE_AND_SCRAP = '5157'
    N50_61WHOLESALE_MACHINE_TOOLS = '5161'
    N50_62WHOLESALE_CONSTRUCTION_MACHINERY = '5162'
    N50_63WHOLESALE_MCHNRY_FOR_TEXTILE_INDTRY__SEWING_MACHINES = '5163'
    N50_64WHOLESALE_OFFICE_MCHNRY_AND_EQUIP = '5164'
    N50_65WHOLESALE_OTHER_MCHNRY_FOR_INDUSTRY_AND_TRADE = '5165'
    N50_66WHOLESALE_AGRIC_MCHNRY_INCL_TRACTORS = '5166'
    N50_70WHOLESALE_OTHER = '5170'
    N52_11RETAIL_IN_NON_SPCLISED_SHOP_MAINLY_FOODDRNKTOBACCO = '5211'
    N52_12OTHER_RETAIL_IN_NON_SPCLISED_SHOPS = '5212'
    N52_21RETAIL_FRUIT_AND_VEG = '5221'
    N52_22RETAIL_MEAT_AND_MEAT_PRODUCTS = '5222'
    N52_23RETAIL_FISH = '5223'
    N52_24RETAIL_BREAD__CAKES = '5224'
    N52_25RETAIL_ALCOHOL_AND_OTHER_BEVERAGES = '5225'
    N52_26RETAIL_TOBACCO_PRODUCTS = '5226'
    N52_27OTHER_RETAIL_OF_FOOD_DRINKTOBACCO_IN_SPCLSED_SHOPS = '5227'
    N52_31DISPENSING_CHEMISTS = '5231'
    N52_32RETAIL_OF_MEDICAL_AND_ORTHOPAEDIC_GOODS = '5232'
    N52_33RETAIL_COSMETIC_ARTICLES = '5233'
    N52_41RETAIL_OF_TEXTILES = '5241'
    N52_42RETAIL_OF_CLOTHING = '5242'
    N52_43RETAIL_OF_FOOTWEAR_AND_LEATHER_GOODS = '5243'
    N52_44RETAIL_FURNITURE__LIGHTING_EQT_AND_HHLD_ARTICLES_NEC = '5244'
    N52_45RETAIL_ELCTRCL_HHLD_APPLIANCES__RADIO__TV = '5245'
    N52_46RETAIL_HARDWARE__PAINTS_AND_GLASS = '5246'
    N52_47RETAIL_BOOKS__NEWSPAPERS_AND_STATIONERY = '5247'
    N52_48RETAIL_FLOOR_COVERNGS__OFFICE_EQT__CMPTRS__OTHER_NEC = '5248'
    N52_50RETAIL_OF_SECOND_HAND_GOODS_IN_STORES = '5250'
    N52_61RETAIL_VIA_MAIL_ORDER = '5261'
    N52_62RETAIL_VIA_STALLS_AND_MARKETS = '5262'
    N52_63OTHER_NON_STORE_RETAIL = '5263'
    N52_71REPAIR_LEATHER_ARTICLES = '5271'
    N52_72REPAIR_ELEC_HHLD_GOODS = '5272'
    N52_73REPAIR_WATCHES_CLOCKS_ETC = '5273'
    N52_74OTHER_REPAIR = '5274'
    N55_11HOTELS_MOTELS_WITH_RESTAURANT = '5511'
    N55_12HOTELS_MOTELS_WITHOUT_RESTAURANT = '5512'
    N55_21YOUTH_HOSTEL_MOUNTAIN_REFUGE = '5521'
    N55_22CAMPING_CARAVAN_SITES = '5522'
    N55_23OTHER_PROVISION_OF_LODGINGS = '5523'
    N55301_3RESTAURANTS__CAFES_AND_TAKE_AWAY_FOOD_SHOPS = '5530'
    N55_401_2PUBLIC_HOUSES__BARS_AND_LICENCED_CLUBS_WITH_ENTNMNT = '5540'
    N55_51CANTEENS = '5551'
    N55_52CATERING = '5552'
    N60_10TRANSPORT_VIA_RAILWAY = '6010'
    N60_21OTHER_SCHEDULED_LAND_TRANSPORT = '6021'
    N60_22TAXI = '6022'
    N60_23OTHER_PASSENGER_LAND_TRANSPORT = '6023'
    N60_24FREIGHT_TRANSPORT_BY_ROAD = '6024'
    N60_30TRANSPORT_VIA_PIPELINES = '6030'
    N61_10SEA_COASTAL_WATER_TRANSPORT = '6110'
    N61_20INLAND_WATER_TRANSPORT = '6120'
    N62_10SCHEDULED_AIR_TRANSPORT = '6210'
    N62_20NON_SCHEDULED_AIR_TRANSPORT = '6220'
    N62_30SPACE_TRANSPORT = '6230'
    N63_11CARGO_HANDLING = '6311'
    N63_12STORAGE_WAREHOUSING = '6312'
    N63_21OTHER_LAND_TRANSPORT_ACTIVITIES = '6321'
    N63_22OTHER_WATER_TRANSPORT_ACTIVITIES = '6322'
    N63_23OTHER_AIR_TRANSPORT_ACTIVITIES = '6323'
    N63_301_4TRAVEL_AGENTS__ORGANISERS__GUIDES__TOURIST_ASSTNCE = '6330'
    N63_40OTHER_TRANSPORT_AGENCIES = '6340'
    N64_11NATIONAL_POST_ACTIVITIES = '6411'
    _64_12COURIER_ACTIV__NOT_NATNL__POST = '6412'
    N64_20TELECOMMUNICATIONS = '6420'
    N65_11CENTRAL_BANKING = '6511'
    N65_121_2BANKS_AND_BUILDING_SOCIETIES = '6512'
    N65_21FINANCIAL_LEASING = '6521'
    N65_22OTHER_CREDIT_GRANTING = '6522'
    N65_231_6UNIT_TRUST__INVSTMNT_TRUSTS__HLDING_CO_ETC = '6523'
    N66_01LIFE_INSURANCE = '6601'
    N66_02PENSION_FUNDING = '6602'
    N66_03NON_LIFE_INSURANCE = '6603'
    N67_11FINANCIAL_MARKET_ADMINISTRATION = '6711'
    N67_12SECURITIES_FUND_MANAGEMENT = '6712'
    N67_13OTHER_FINANCIAL_INTERMED__ACTIV_ = '6713'
    N67_20OTHER_INSURANCE_ACTIVITIES = '6720'
    N70_11DEVELOPMENT_SALE_OF_REAL_ESTATE = '7011'
    N70_12BUYING_SELLING_REAL_ESTATE_SELF = '7012'
    N70_20LETTING_OWN_PROPERTY = '7020'
    N70_31REAL_ESTATE_AGENCY = '7031'
    N70_32MANAGEMENT_OF_REAL_ESTATE = '7032'
    N71_10CAR_RENTAL = '7110'
    N71_21OTHER_LAND_TRANSPORT_RENTAL = '7121'
    N71_22WATER_TRANSPORT_EQT_RENTAL = '7122'
    N71_23AIR_TRANSPORT_EQT_RENTAL = '7123'
    N71_31AGRICULTURAL_MACH_EQT_RENTAL = '7131'
    N71_32CONSTRUCTION_MACH_EQT_RENTAL = '7132'
    N71_33OFFICE_MACH_EQT_RENTAL = '7133'
    N71_34OTHER_MACH_EQT_RENTAL = '7134'
    N71_40PERSON_HHLD_EQT_RENTAL = '7140'
    N72_10COMPUTER_HARDWARE_CONSULTANCY = '7210'
    N72_20COMPUTER_SOFTWARE_CONSULTANCY = '7220'
    N72_30DATA_PROCESSING = '7230'
    N72_40DATA_BASE_ACTIVITIES = '7240'
    N72_50REPAIR_OF_OFFICE_COMPUTER_EQT = '7250'
    N72_60OTHER_COMPUTER_ACTIVITIES = '7260'
    N73_10RESEARCH_NATURAL_SCIENCES_ENGIN_ = '7310'
    N73_20RES__SOCIAL_SCIENCES_HUMANITIES = '7320'
    N74_11LEGAL_ACTIVITIES = '7411'
    N74_12ACCOUNTNG_AUDITNG_TAX_CONSULTANCY = '7412'
    N74_13MARKET_OPINION_RESEARCH = '7413'
    N74_14BUSINESS_MANAGEMENT_CONSULTANCY = '7414'
    N74_15MANAGEMNT_ACTIVITIES_HOLDING_COMPS = '7415'
    N74_20ARCHIT__ENGINEERING_ETC_CONSULTNCY = '7420'
    N74_30TECHNICAL_TESTING_ANALYSIS = '7430'
    N74_40ADVERTISING = '7440'
    N74_50LABOUR_PERSONNEL_RECRUITMENT = '7450'
    N74_60INVESTIGATION_SECURITY_SERVICES = '7460'
    N74_70INDUSTRIAL_CLEANING = '7470'
    N74_81PHOTOGRAPHIC_ACTIVITIES = '7481'
    N74_82PACKAGING_ACTIVITIES = '7482'
    N74_83SECRETARIAL_TRANSLATION = '7483'
    N74_84OTHER_BUSINESS_ACTIVITIES = '7484'
    N75_11GENERAL_PUBLIC_SERVICE_ACTIVITIES = '7511'
    N75_12REGULN_GOVT_AGENCY_NOT_SOC_SEC = '7512'
    N75_13DEVELOPMENT_OF_GOVT_AGENCIES = '7513'
    N75_14SUPPORT_OF_GOVT_AS_A_WHOLE = '7514'
    N75_21FOREIGN_AFFAIRS = '7521'
    N75_22DEFENCE = '7522'
    N75_23JUSTICE_AND_JUDICIAL_ACTIVITIES = '7523'
    N75_24PUBLIC_SECURITY_LAW_AND_ORDER_ETC = '7524'
    N75_25FIRE_SERVICE = '7525'
    N75_30COMPULSORY_SOCIAL_SECURITY_ACTIV_ = '7530'
    N80_10PRIMARY_EDUCATION = '8010'
    N80_21GENERAL_SECONDARY_EDUCATION = '8021'
    N80_22TECH_VOCATIONAL_2ND_ARY_EDUCATION = '8022'
    N80_301_3HIGHER_EDUCN_SUB_DEGREE_FIRST_DGREE_PGRAD_DGREE = '8030'
    N80_41DRIVING_SCHOOL_ACTIVITIES = '8041'
    N80_42ADULT_OTHER_EDUCATION = '8042'
    N85_11HOSPITAL_ACTIVITIES = '8511'
    N85_12MEDICAL_PRACTICE_ACTIVITIES = '8512'
    N85_13DENTAL_PRACTICE_ACTIVITIES = '8513'
    N85_14OTHER_HUMAN_HEALTH_ACTIVITIES = '8514'
    N85_20VETERINARY_ACTIVITIES = '8520'
    N85_31SOCIAL_WORK_WITH_ACCOM = '8531'
    N85_32SOCIAL_WORK_WITHOUT_ACCOM = '8532'
    N90_00SEWAGE_REFUSE_DISPOSAL_ETC = '9000'
    N91_11BUSINESS_EMPLOYERS_ORGANISATIONS = '9111'
    N91_12PROFESSIONAL_ORGANISATIONS = '9112'
    N91_20TRADE_UNIONS = '9120'
    N91_31RELIGIOUS_ORGANISATIONS = '9131'
    N91_32POLITICAL_ORGANISATIONS = '9132'
    N91_33OTHER_MEMBERSHIP_ORGANISATIONS = '9133'
    N92_11MOTION_PICTURE_VIDEO_PRODUCTION = '9211'
    N92_12MOTION_PICTURE_VIDEO_DISTRIBUTION = '9212'
    N92_13MOTION_PICTURE_PROJECTION = '9213'
    N92_20RADIO_TV_ACTIVITIES = '9220'
    N92_31ARTISTIC_LITERARY_CREATION_ETC = '9231'
    N92_32ARTS_FACILITIES = '9232'
    N92_33FAIR_AMUSEMENT_PARK_ACTIVITIES = '9233'
    N92_34OTHER_ENTERTAINMENT_ACTIVITIES = '9234'
    N92_40NEWS_AGENCY_ACTIVITIES = '9240'
    N92_51LIBRARY_ARCHIVE_ACTIVITIES = '9251'
    N92_52MUSEUM_ACTIVITIES = '9252'
    N92_53BOTANICAL_ZOOLOGICAL_GARDENS_ETC = '9253'
    N92_61OPERATION_OF_SPORTS_ARENAS_STADIA = '9261'
    N92_62OTHER_SPORTING_ACTIVITIES = '9262'
    N92_71GAMBLING_BETTING_ACTIVITIES = '9271'
    N92_72OTHER_RECREATIONAL_ACTIVITIES = '9272'
    N93_01WASHING_DRY_CLEANING_TEXTILES_FURS = '9301'
    N93_02HAIRDRESSING_OTH_BEAUTY_TREATMENT = '9302'
    N93_03FUNERAL_ETC = '9303'
    N93_04PHYSICAL_WELL_BEING_ACTIVITIES = '9304'
    N93_05OTHER_SERVICE_ACTIVITIES = '9305'
    N95_00PRIV__HHLDS_WITH_EMPLYED_PERSONS = '9500'
    N99_00EXTRA_TERRITORIAL_ORGANISATIONS = '9900'
    HAVE_SECOND_JOB___DK_REFUSE__INDUSTRY = '9999'


class SOC2(OrderedEnum):
    INELIGIBLE___NO_SECOND_JOB = '-2'
    INELIGIBLE___UNDER_16YRS = '-1'
    SENIOR_OFFICIALS_IN_NATIONAL_GOVERNMENT = '1111'
    DIRECTORS_AND_CHIEF_EXECUTIVES_OF_MAJOR_ORGANISATIONS = '1112'
    SENIOR_OFFICIALS_IN_LOCAL_GOVERNMENT = '1113'
    SENIOR_OFFICIALS_OF_SPECIAL_INTEREST_ORGANISATIONS = '1114'
    PRODUCTION__WORKS_AND_MAINTENANCE_MANAGERS = '1121'
    MANAGERS_IN_CONSTRUCTION = '1122'
    MANAGERS_IN_MINING_AND_ENERGY = '1123'
    FINANCIAL_MANAGERS_AND_CHARTERED_SECRETARIES = '1131'
    MARKETING_AND_SALES_MANAGERS = '1132'
    PURCHASING_MANAGERS = '1133'
    ADVERTISING_AND_PUBLIC_RELATIONS_MANAGERS = '1134'
    PERSONNEL__TRAINING_AND_INDUSTRIAL_RELATIONS_MANAGERS = '1135'
    INFORMATION_AND_COMMUNICATION_TECHNOLOGY_MANAGERS = '1136'
    RESEARCH_AND_DEVELOPMENT_MANAGERS = '1137'
    QUALITY_ASSURANCE_MANAGERS = '1141'
    CUSTOMER_CARE_MANAGERS = '1142'
    FINANCIAL_INSTITUTION_MANAGERS = '1151'
    OFFICE_MANAGERS = '1152'
    TRANSPORT_AND_DISTRIBUTION_MANAGERS = '1161'
    STORAGE_AND_WAREHOUSE_MANAGERS = '1162'
    RETAIL_AND_WHOLESALE_MANAGERS = '1163'
    OFFICERS_IN_ARMED_FORCES = '1171'
    POLICE_OFFICERS_INSPECTORS_AND_ABOVE = '1172'
    SENIOR_OFFICERS_IN_FIRE__AMBULANCE__PRISON_ETC_SERVICES = '1173'
    SECURITY_MANAGERS = '1174'
    HOSPITAL_AND_HEALTH_SERVICE_MANAGERS = '1181'
    PHARMACY_MANAGERS = '1182'
    HEALTHCARE_PRACTICE_MANAGERS = '1183'
    SOCIAL_SERVICES_MANAGERS = '1184'
    RESIDENTIAL_AND_DAY_CARE_MANAGERS = '1185'
    FARM_MANAGERS = '1211'
    NATURAL_ENVIRONMENT_AND_CONSERVATION_MANAGERS = '1212'
    MANAGERS_IN_ANIMAL_HUSBANDRY__FORESTRY_AND_FISHING_N_E_C = '1219'
    HOTEL_AND_ACCOMMODATION_MANAGERS = '1221'
    CONFERENCE_AND_EXHIBITION_MANAGERS = '1222'
    RESTAURANT_AND_CATERING_MANAGERS = '1223'
    PUBLICANS_AND_MANAGERS_OF_LICENSED_PREMISES = '1224'
    LEISURE_AND_SPORTS_MANAGERS = '1225'
    TRAVEL_AGENCY_MANAGERS = '1226'
    PROPERTY__HOUSING_AND_LAND_MANAGERS = '1231'
    GARAGE_MANAGERS_AND_PROPRIETORS = '1232'
    HAIRDRESSING_AND_BEAUTY_SALON_MANAGERS_AND_PROPRIETORS = '1233'
    SHOPKEEPERS_AND_WHOLESALERETAIL_DEALERS = '1234'
    RECYCLING_AND_REFUSE_DISPOSAL_MANAGERS = '1235'
    MANAGERS_AND_PROPRIETORS_IN_OTHER_SERVICES_N_E_C = '1239'
    CHEMISTS = '2111'
    BIOLOGICAL_SCIENTISTS_AND_BIOCHEMISTS = '2112'
    PHYSICISTS__GEOLOGISTS_AND_METEOROLOGISTS = '2113'
    CIVIL_ENGINEERS = '2121'
    MECHANICAL_ENGINEERS = '2122'
    ELECTRICAL_ENGINEERS = '2123'
    ELECTRONICS_ENGINEERS = '2124'
    CHEMICAL_ENGINEERS = '2125'
    DESIGN_AND_DEVELOPMENT_ENGINEERS = '2126'
    PRODUCTION_AND_PROCESS_ENGINEERS = '2127'
    PLANNING_AND_QUALITY_CONTROL_ENGINEERS = '2128'
    ENGINEERING_PROFESSIONALS_N_E_C = '2129'
    IT_STRATEGY_AND_PLANNING_PROFESSIONALS = '2131'
    SOFTWARE_PROFESSIONALS = '2132'
    MEDICAL_PRACTITIONERS = '2211'
    PSYCHOLOGISTS = '2212'
    PHARMACISTSPHARMACOLOGISTS = '2213'
    OPHTHALMIC_OPTICIANS = '2214'
    DENTAL_PRACTITIONERS = '2215'
    VETERINARIANS = '2216'
    HIGHER_EDUCATION_TEACHING_PROFESSIONALS = '2311'
    FURTHER_EDUCATION_TEACHING_PROFESSIONALS = '2312'
    EDUCATION_OFFICERS__SCHOOL_INSPECTORS = '2313'
    SECONDARY_EDUCATION_TEACHING_PROFESSIONALS = '2314'
    PRIMARY_AND_NURSERY_EDUCATION_TEACHING_PROFESSIONALS = '2315'
    SPECIAL_NEEDS_EDUCATION_TEACHING_PROFESSIONALS = '2316'
    REGISTRARS_AND_SENIOR_ADMINISTRATORS_OF_EDUCATIONAL_PLACES = '2317'
    TEACHING_PROFESSIONALS_N_E_C = '2319'
    SCIENTIFIC_RESEARCHERS = '2321'
    SOCIAL_SCIENCE_RESEARCHERS = '2322'
    RESEARCHERS_N_E_C = '2329'
    SOLICITORS_AND_LAWYERS__JUDGES_AND_CORONERS = '2411'
    LEGAL_PROFESSIONALS_N_E_C = '2419'
    CHARTERED_AND_CERTIFIED_ACCOUNTANTS = '2421'
    MANAGEMENT_ACCOUNTANTS = '2422'
    MANAGEMENT_CONSULTANTS__ECONOMISTS_AND_STATISTICIANS = '2423'
    ARCHITECTS = '2431'
    TOWN_PLANNERS = '2432'
    QUANTITY_SURVEYORS = '2433'
    CHARTERED_SURVEYORS_NOT_QUANTITY_SURVEYORS = '2434'
    PUBLIC_SERVICE_ADMINISTRATIVE_PROFESSIONALS = '2441'
    SOCIAL_WORKERS = '2442'
    PROBATION_OFFICERS = '2443'
    CLERGY = '2444'
    LIBRARIANS = '2451'
    ARCHIVISTS_AND_CURATORS = '2452'
    LABORATORY_TECHNICIANS = '3111'
    ELECTRICALELECTRONICS_TECHNICIANS = '3112'
    ENGINEERING_TECHNICIANS = '3113'
    BUILDING_AND_CIVIL_ENGINEERING_TECHNICIANS = '3114'
    QUALITY_ASSURANCE_TECHNICIANS = '3115'
    SCIENCE_AND_ENGINEERING_TECHNICIANS_N_E_C = '3119'
    ARCHITECTURAL_TECHNOLOGISTS_AND_TOWN_PLANNING_TECHNICIANS = '3121'
    DRAUGHTSPERSONS = '3122'
    BUILDING_INSPECTORS = '3123'
    IT_OPERATIONS_TECHNICIANS = '3131'
    IT_USER_SUPPORT_TECHNICIANS = '3132'
    NURSES = '3211'
    MIDWIVES = '3212'
    PARAMEDICS = '3213'
    MEDICAL_RADIOGRAPHERS = '3214'
    CHIROPODISTS = '3215'
    DISPENSING_OPTICIANS = '3216'
    PHARMACEUTICAL_DISPENSERS = '3217'
    MEDICAL_AND_DENTAL_TECHNICIANS = '3218'
    PHYSIOTHERAPISTS = '3221'
    OCCUPATIONAL_THERAPISTS = '3222'
    SPEECH_AND_LANGUAGE_THERAPISTS = '3223'
    THERAPISTS_N_E_C = '3229'
    YOUTH_AND_COMMUNITY_WORKERS = '3231'
    HOUSING_AND_WELFARE_OFFICERS = '3232'
    NCOS_AND_OTHER_RANKS = '3311'
    POLICE_OFFICERS_SERGEANT_AND_BELOW = '3312'
    FIRE_SERVICE_OFFICERS_LEADING_FIRE_OFFICER_AND_BELOW = '3313'
    PRISON_SERVICE_OFFICERS_BELOW_PRINCIPAL_OFFICER = '3314'
    PROTECTIVE_SERVICE_ASSOCIATE_PROFESSIONALS_N_E_C = '3319'
    ARTISTS = '3411'
    AUTHORS__WRITERS = '3412'
    ACTORS__ENTERTAINERS = '3413'
    DANCERS_AND_CHOREOGRAPHERS = '3414'
    MUSICIANS = '3415'
    ARTS_OFFICERS__PRODUCERS_AND_DIRECTORS = '3416'
    GRAPHIC_DESIGNERS = '3421'
    PRODUCT__CLOTHING_AND_RELATED_DESIGNERS = '3422'
    JOURNALISTS__NEWSPAPER_AND_PERIODICAL_EDITORS = '3431'
    BROADCASTING_ASSOCIATE_PROFESSIONALS = '3432'
    PUBLIC_RELATIONS_OFFICERS = '3433'
    PHOTOGRAPHERS_AND_AUDIO_VISUAL_EQUIPMENT_OPERATORS = '3434'
    SPORTS_PLAYERS = '3441'
    SPORTS_COACHES__INSTRUCTORS_AND_OFFICIALS = '3442'
    FITNESS_INSTRUCTORS = '3443'
    SPORTS_AND_FITNESS_OCCUPATIONS_N_E_C = '3449'
    AIR_TRAFFIC_CONTROLLERS = '3511'
    AIRCRAFT_PILOTS_AND_FLIGHT_ENGINEERS = '3512'
    SHIP_AND_HOVERCRAFT_OFFICERS = '3513'
    TRAIN_DRIVERS = '3514'
    LEGAL_ASSOCIATE_PROFESSIONALS = '3520'
    ESTIMATORS__VALUERS_AND_ASSESSORS = '3531'
    BROKERS = '3532'
    INSURANCE_UNDERWRITERS = '3533'
    FINANCE_AND_INVESTMENT_ANALYSTSADVISERS = '3534'
    TAXATION_EXPERTS = '3535'
    IMPORTERS__EXPORTERS = '3536'
    FINANCIAL_AND_ACCOUNTING_TECHNICIANS = '3537'
    BUSINESS_AND_RELATED_ASSOCIATE_PROFESSIONALS_N_E_C = '3539'
    BUYERS_AND_PURCHASING_OFFICERS = '3541'
    SALES_REPRESENTATIVES = '3542'
    MARKETING_ASSOCIATE_PROFESSIONALS = '3543'
    ESTATE_AGENTS__AUCTIONEERS = '3544'
    CONSERVATION_AND_ENVIRONMENTAL_PROTECTION_OFFICERS = '3551'
    COUNTRYSIDE_AND_PARK_RANGERS = '3552'
    PUBLIC_SERVICE_ASSOCIATE_PROFESSIONALS = '3561'
    PERSONNEL_AND_INDUSTRIAL_RELATIONS_OFFICERS = '3562'
    VOCATIONAL_AND_INDUSTRIAL_TRAINERS_AND_INSTRUCTORS = '3563'
    CAREERS_ADVISERS_AND_VOCATIONAL_GUIDANCE_SPECIALISTS = '3564'
    INSPECTORS_OF_FACTORIES__UTILITIES_AND_TRADING_STANDARDS = '3565'
    STATUTORY_EXAMINERS = '3566'
    OCCUPATIONAL_HYGIENISTS_AND_SAFETY_OFFICERS_HEALTH_AND_SAFETY = '3567'
    ENVIRONMENTAL_HEALTH_OFFICERS = '3568'
    CIVIL_SERVICE_EXECUTIVE_OFFICERS = '4111'
    CIVIL_SERVICE_ADMINISTRATIVE_OFFICERS_AND_ASSISTANTS = '4112'
    LOCAL_GOVERNMENT_CLERICAL_OFFICERS_AND_ASSISTANTS = '4113'
    OFFICERS_OF_NON_GOVERNMENTAL_ORGANISATIONS = '4114'
    CREDIT_CONTROLLERS = '4121'
    ACCOUNTS__WAGES_AND_OTHER_FINANCIAL_CLERKS__BOOKKEEPERS = '4122'
    COUNTER_CLERKS = '4123'
    FILING_AND_OTHER_RECORDS_ASSISTANTSCLERKS = '4131'
    PENSIONS_AND_INSURANCE_CLERKS = '4132'
    STOCK_CONTROL_CLERKS = '4133'
    TRANSPORT_AND_DISTRIBUTION_CLERKS = '4134'
    LIBRARY_ASSISTANTSCLERKS = '4135'
    DATABASE_ASSISTANTSCLERKS = '4136'
    MARKET_RESEARCH_INTERVIEWERS = '4137'
    TELEPHONISTS = '4141'
    COMMUNICATION_OPERATORS = '4142'
    GENERAL_OFFICE_ASSISTANTSCLERKS = '4150'
    MEDICAL_SECRETARIES = '4211'
    LEGAL_SECRETARIES = '4212'
    SCHOOL_SECRETARIES = '4213'
    COMPANY_SECRETARIES = '4214'
    PERSONAL_ASSISTANTS_AND_OTHER_SECRETARIES = '4215'
    RECEPTIONISTS = '4216'
    TYPISTS = '4217'
    FARMERS = '5111'
    HORTICULTURAL_TRADES = '5112'
    GARDENERS_AND_GROUNDSMENGROUNDSWOMEN = '5113'
    AGRICULTURAL_AND_FISHING_TRADES_N_E_C = '5119'
    SMITHS_AND_FORGE_WORKERS = '5211'
    MOULDERS__CORE_MAKERS__DIE_CASTERS = '5212'
    SHEET_METAL_WORKERS = '5213'
    METAL_PLATE_WORKERS__SHIPWRIGHTS__RIVETERS = '5214'
    WELDING_TRADES = '5215'
    PIPE_FITTERS = '5216'
    METAL_MACHINING_SETTERS_AND_SETTER_OPERATORS = '5221'
    TOOL_MAKERS__TOOL_FITTERS_AND_MARKERS_OUT = '5222'
    METAL_WORKING_PRODUCTION_AND_MAINTENANCE_FITTERS = '5223'
    PRECISION_INSTRUMENT_MAKERS_AND_REPAIRERS = '5224'
    MOTOR_MECHANICS__AUTO_ENGINEERS = '5231'
    VEHICLE_BODY_BUILDERS_AND_REPAIRERS = '5232'
    AUTO_ELECTRICIANS = '5233'
    VEHICLE_SPRAY_PAINTERS = '5234'
    ELECTRICIANS__ELECTRICAL_FITTERS = '5241'
    TELECOMMUNICATIONS_ENGINEERS = '5242'
    LINES_REPAIRERS_AND_CABLE_JOINTERS = '5243'
    TV__VIDEO_AND_AUDIO_ENGINEERS = '5244'
    COMPUTER_ENGINEERS__INSTALLATION_AND_MAINTENANCE = '5245'
    ELECTRICALELECTRONICS_ENGINEERS_N_E_C = '5249'
    STEEL_ERECTORS = '5311'
    BRICKLAYERS__MASONS = '5312'
    ROOFERS__ROOF_TILERS_AND_SLATERS = '5313'
    PLUMBERS__HEATING_AND_VENTILATING_ENGINEERS = '5314'
    CARPENTERS_AND_JOINERS = '5315'
    GLAZIERS__WINDOW_FABRICATORS_AND_FITTERS = '5316'
    CONSTRUCTION_TRADES_N_E_C = '5319'
    PLASTERERS = '5321'
    FLOORERS_AND_WALL_TILERS = '5322'
    PAINTERS_AND_DECORATORS = '5323'
    WEAVERS_AND_KNITTERS = '5411'
    UPHOLSTERERS = '5412'
    LEATHER_AND_RELATED_TRADES = '5413'
    TAILORS_AND_DRESSMAKERS = '5414'
    TEXTILES__GARMENTS_AND_RELATED_TRADES_N_E_C = '5419'
    ORIGINATORS__COMPOSITORS_AND_PRINT_PREPARERS = '5421'
    PRINTERS = '5422'
    BOOKBINDERS_AND_PRINT_FINISHERS = '5423'
    SCREEN_PRINTERS = '5424'
    BUTCHERS__MEAT_CUTTERS = '5431'
    BAKERS__FLOUR_CONFECTIONERS = '5432'
    FISHMONGERS__POULTRY_DRESSERS = '5433'
    CHEFS__COOKS = '5434'
    GLASS_AND_CERAMICS_MAKERS__DECORATORS_AND_FINISHERS = '5491'
    FURNITURE_MAKERS__OTHER_CRAFT_WOODWORKERS = '5492'
    PATTERN_MAKERS_MOULDS = '5493'
    MUSICAL_INSTRUMENT_MAKERS_AND_TUNERS = '5494'
    GOLDSMITHS__SILVERSMITHS__PRECIOUS_STONE_WORKERS = '5495'
    FLORAL_ARRANGERS__FLORISTS = '5496'
    HAND_CRAFT_OCCUPATIONS_N_E_C = '5499'
    NURSING_AUXILIARIES_AND_ASSISTANTS = '6111'
    AMBULANCE_STAFF_EXCLUDING_PARAMEDICS = '6112'
    DENTAL_NURSES = '6113'
    HOUSEPARENTS_AND_RESIDENTIAL_WARDENS = '6114'
    CARE_ASSISTANTS_AND_HOME_CARERS = '6115'
    NURSERY_NURSES = '6121'
    CHILDMINDERS_AND_RELATED_OCCUPATIONS = '6122'
    PLAYGROUP_LEADERSASSISTANTS = '6123'
    EDUCATIONAL_ASSISTANTS = '6124'
    VETERINARY_NURSES_AND_ASSISTANTS = '6131'
    ANIMAL_CARE_OCCUPATIONS_N_E_C = '6139'
    SPORTS_AND_LEISURE_ASSISTANTS = '6211'
    TRAVEL_AGENTS = '6212'
    TRAVEL_AND_TOUR_GUIDES = '6213'
    AIR_TRAVEL_ASSISTANTS = '6214'
    RAIL_TRAVEL_ASSISTANTS = '6215'
    LEISURE_AND_TRAVEL_SERVICE_OCCUPATIONS_N_E_C = '6219'
    HAIRDRESSERS__BARBERS = '6221'
    BEAUTICIANS_AND_RELATED_OCCUPATIONS = '6222'
    HOUSEKEEPERS_AND_RELATED_OCCUPATIONS = '6231'
    CARETAKERS = '6232'
    UNDERTAKERS_AND_MORTUARY_ASSISTANTS = '6291'
    PEST_CONTROL_OFFICERS = '6292'
    SALES_AND_RETAIL_ASSISTANTS = '7111'
    RETAIL_CASHIERS_AND_CHECK_OUT_OPERATORS = '7112'
    TELEPHONE_SALESPERSONS = '7113'
    COLLECTOR_SALESPERSONS_AND_CREDIT_AGENTS = '7121'
    DEBT__RENT_AND_OTHER_CASH_COLLECTORS = '7122'
    ROUNDSMENWOMEN_AND_VAN_SALESPERSONS = '7123'
    MARKET_AND_STREET_TRADERS_AND_ASSISTANTS = '7124'
    MERCHANDISERS_AND_WINDOW_DRESSERS = '7125'
    SALES_RELATED_OCCUPATIONS_N_E_C = '7129'
    CALL_CENTRE_AGENTSOPERATORS = '7211'
    CUSTOMER_CARE_OCCUPATIONS = '7212'
    FOOD__DRINK_AND_TOBACCO_PROCESS_OPERATIVES = '8111'
    GLASS_AND_CERAMICS_PROCESS_OPERATIVES = '8112'
    TEXTILE_PROCESS_OPERATIVES = '8113'
    CHEMICAL_AND_RELATED_PROCESS_OPERATIVES = '8114'
    RUBBER_PROCESS_OPERATIVES = '8115'
    PLASTICS_PROCESS_OPERATIVES = '8116'
    METAL_MAKING_AND_TREATING_PROCESS_OPERATIVES = '8117'
    ELECTROPLATERS = '8118'
    PROCESS_OPERATIVES_N_E_C = '8119'
    PAPER_AND_WOOD_MACHINE_OPERATIVES = '8121'
    COAL_MINE_OPERATIVES = '8122'
    QUARRY_WORKERS_AND_RELATED_OPERATIVES = '8123'
    ENERGY_PLANT_OPERATIVES = '8124'
    METAL_WORKING_MACHINE_OPERATIVES = '8125'
    WATER_AND_SEWERAGE_PLANT_OPERATIVES = '8126'
    PLANT_AND_MACHINE_OPERATIVES_N_E_C = '8129'
    ASSEMBLERS_ELECTRICAL_PRODUCTS = '8131'
    ASSEMBLERS_VEHICLES_AND_METAL_GOODS = '8132'
    ROUTINE_INSPECTORS_AND_TESTERS = '8133'
    WEIGHERS__GRADERS__SORTERS = '8134'
    TYRE__EXHAUST_AND_WINDSCREEN_FITTERS = '8135'
    CLOTHING_CUTTERS = '8136'
    SEWING_MACHINISTS = '8137'
    ROUTINE_LABORATORY_TESTERS = '8138'
    ASSEMBLERS_AND_ROUTINE_OPERATIVES_N_E_C = '8139'
    SCAFFOLDERS__STAGERS__RIGGERS = '8141'
    ROAD_CONSTRUCTION_OPERATIVES = '8142'
    RAIL_CONSTRUCTION_AND_MAINTENANCE_OPERATIVES = '8143'
    CONSTRUCTION_OPERATIVES_N_E_C = '8149'
    HEAVY_GOODS_VEHICLE_DRIVERS = '8211'
    VAN_DRIVERS = '8212'
    BUS_AND_COACH_DRIVERS = '8213'
    TAXI__CAB_DRIVERS_AND_CHAUFFEURS = '8214'
    DRIVING_INSTRUCTORS = '8215'
    RAIL_TRANSPORT_OPERATIVES = '8216'
    SEAFARERS_MERCHANT_NAVY_BARGE_AND_BOAT_OPERATIVES = '8217'
    AIR_TRANSPORT_OPERATIVES = '8218'
    TRANSPORT_OPERATIVES_N_E_C = '8219'
    CRANE_DRIVERS = '8221'
    FORK_LIFT_TRUCK_DRIVERS = '8222'
    AGRICULTURAL_MACHINERY_DRIVERS = '8223'
    MOBILE_MACHINE_DRIVERS_AND_OPERATIVES_N_E_C = '8229'
    FARM_WORKERS = '9111'
    FORESTRY_WORKERS = '9112'
    FISHING_AND_AGRICULTURE_RELATED_OCCUPATIONS_N_E_C = '9119'
    LABOURERS_IN_BUILDING_AND_WOODWORKING_TRADES = '9121'
    LABOURERS_IN_OTHER_CONSTRUCTION_TRADES_N_E_C = '9129'
    LABOURERS_IN_FOUNDRIES = '9131'
    INDUSTRIAL_CLEANING_PROCESS_OCCUPATIONS = '9132'
    PRINTING_MACHINE_MINDERS_AND_ASSISTANTS = '9133'
    PACKERS__BOTTLERS__CANNERS__FILLERS = '9134'
    LABOURERS_IN_PROCESS_AND_PLANT_OPERATIONS_N_E_C = '9139'
    STEVEDORES__DOCKERS_AND_SLINGERS = '9141'
    OTHER_GOODS_HANDLING_AND_STORAGE_OCCUPATIONS_N_E_C = '9149'
    POSTAL_WORKERS__MAIL_SORTERS__MESSENGERS__COURIERS = '9211'
    ELEMENTARY_OFFICE_OCCUPATIONS_N_E_C = '9219'
    HOSPITAL_PORTERS = '9221'
    HOTEL_PORTERS = '9222'
    KITCHEN_AND_CATERING_ASSISTANTS = '9223'
    WAITERS__WAITRESSES = '9224'
    BAR_STAFF = '9225'
    LEISURE_AND_THEME_PARK_ATTENDANTS = '9226'
    ELEMENTARY_PERSONAL_SERVICES_OCCUPATIONS_N_E_C = '9229'
    WINDOW_CLEANERS = '9231'
    ROAD_SWEEPERS = '9232'
    CLEANERS__DOMESTICS = '9233'
    LAUNDERERS__DRY_CLEANERS__PRESSERS = '9234'
    REFUSE_AND_SALVAGE_OCCUPATIONS = '9235'
    ELEMENTARY_CLEANING_OCCUPATIONS_N_E_C = '9239'
    SECURITY_GUARDS_AND_RELATED_OCCUPATIONS = '9241'
    TRAFFIC_WARDENS = '9242'
    SCHOOL_CROSSING_PATROL_ATTENDANTS = '9243'
    SCHOOL_MID_DAY_ASSISTANTS = '9244'
    CAR_PARK_ATTENDANTS = '9245'
    ELEMENTARY_SECURITY_OCCUPATIONS_N_E_C = '9249'
    SHELF_FILLERS = '9251'
    ELEMENTARY_SALES_OCCUPATIONS_N_E_C = '9259'
    HAVE_SECOND_JOB___DK_REFUSE_OCCUPATION = '9999'


class NSSECB(OrderedEnum):
    INELIGIBLE___CHILDREN_UNDER_16_YRS = '-1'
    EMPLOYERS_IN_LARGE_ORGANISATIONS = '1'
    HIGHER_MANAGERIAL = '2'
    HIGHER_PROFESSIONAL____TRADITIONAL__EMPLOYEES = '3.1'
    HIGHER_PROFESSIONAL____NEW__EMPLOYEES = '3.2'
    HIGHER_PROFESSIONAL____TRADITIONAL__SELF_EMPLOYED = '3.3'
    LOWER_PROFESSIONAL____NEW__SELF_EMPLOYED = '3.4'
    LOWER_PROFESSIONAL____TRADITIONAL__EMPLOYEES = '4.1'
    LOWER_PROFESSIONAL____NEW__EMPLOYEES = '4.2'
    LOWER_PROFESSIONAL____TRADITIONAL__SELF_EMPLOYED = '4.3'
    LOWER_PROFESSIONAL____NEW__SELF_EMPLOYED2 = '4.4'
    LOWER_MANAGERIAL = '5'
    HIGHER_SUPERVISORY = '6'
    INTERMEDIATE_CLERICAL_AND_ADMINISTRATIVE = '7.1'
    INTERMEDIATE_SALES_AND_SERVICE = '7.2'
    INTERMEDIATE_TECHNICAL_AND_AUXILLARY = '7.3'
    INTERMEDIATE_ENGINEERING = '7.4'
    EMPLOYERS_IN_SMALL_ORGANISATIONS_NON_PROFESSIONAL = '8.1'
    EMPLOYERS_IN_SMALL_ORGANISATIONS_AGRICULTURE = '8.2'
    OWN_ACCOUNT_WORKERS_NON_PROFESSIONAL = '9.1'
    OWN_ACCOUNT_WORKERS_AGRICULTURE = '9.2'
    LOWER_SUPERVISORY = '10'
    LOWER_TECHNICAL_CRAFT = '11.1'
    LOWER_TECHNICAL_PROCESS_OPERATIVE = '11.2'
    SEMI_ROUTINE_SALES = '12.1'
    SEMI_ROUTINE_SERVICE = '12.2'
    SEMI_ROUTINE_TECHNICAL = '12.3'
    SEMI_ROUTINE_OPERATIVE = '12.4'
    SEMI_ROUTINE_AGRICULTURAL = '12.5'
    SEMI_ROUTINE_CLERICAL = '12.6'
    SEMI_ROUTINE_CHILDCARE = '12.7'
    ROUTINE_SALES_AND_SERVICE = '13.1'
    ROUTINE_PRODUCTION = '13.2'
    ROUTINE_TECHNICAL = '13.3'
    ROUTINE_OPERATIVE = '13.4'
    ROUTINE_AGRICULTURAL = '13.5'
    NEVER_WORKED = '14.1'
    LONG_TERM_UNEMPLOYED_CODE_NOT_USED___PREVIOUS_JOB_CODED = '14.2'
    FULL_TIME_STUDENTS = '15'
    OCCUPATION_NOT_STATED_OR_INADEQUATELY_DESCRIBED = '16'
    NOT_CLASSIFIABLE_FOR_OTHER_REASONS = '17'


class NSSECB_8(OrderedEnum):
    INELIGIBLE___CHILDREN_UNDER_16_YRS = '-1'
    LARGE_EMPLOYERS_AND_HIGHER_MANAGERIAL_OCCS = '1.1'
    HIGHER_PROF_OCCS = '1.2'
    LOWER_MANAG_AND_PROF_OCCS = '2'
    INTERMEDIATE_OCCS = '3'
    SMALL_EMPLOYERS_AND_OWN_ACCNT_WORKERS = '4'
    LOWER_SUPERVISORY_AND_TECHNICAL_OCCS = '5'
    SEMI_ROUTINE_OCCS = '6'
    ROUTINE_OCCS = '7'
    NEVER_WORKED = '8'
    NOT_CLASSIFIABLE_EG_STUDENTS__MISSING_OCCS = '9'


class NSSECB_5(OrderedEnum):
    INELIGIBLE___CHILDREN_UNDER_16_YRS = '-1'
    MANAGERIAL_AND_PROFESSIONAL_OCCS = '1'
    INTERMEDIATE_OCCS = '2'
    SMALL_EMPLOYERS_AND_OWN_ACCOUNT_WORKERS = '3'
    LOWER_SUPERVISORY_AND_TECHNICAL_OCCS = '4'
    SEMI_ROUTINE_AND_ROUTINE_OCCS = '5'
    NEVER_WORKED = '6'
    NOT_CLASSIFIABLE_EG_STUDENTS__MISSING_OCCS = '7'


class NSSECB_3(OrderedEnum):
    INELIGIBLE___CHILDREN_UNDER_16_YRS = '-1'
    MANAGERIAL_AND_PROFESSIONAL_OCCS = '1'
    INTERMEDIATE_OCCS = '2'
    ROUTINE_AND_MANUAL_OCCS = '3'
    NEVER_WORKED = '4'
    NOT_CLASSIFIABLE_EG_STUDENTS__MISSING_OCCS = '5'


class HIQUAL4(OrderedEnum):
    DEGREE_LEVEL_QUALIFICATION_OR_ABOVE = '1'
    HIGHER_EDN_BELOW_DEGREE_LEVEL_EG_HNC__NURSING_QUAL = '2'
    A_LEVELS__VOCATIONAL_LEVEL_3_AND_EQUIVLNT_EG_AS_LEVEL__NVQ_3 = '3'
    O_LEVELS__GCSE_GRADE_A_C__VOCATIONAL_LEVEL_2_AND_EQUIVLNT = '4'
    GCSE_BELOW_GRADE_C__CSE__VOCATIONAL_LEVEL_1_AND_EQUIVLNT = '5'
    QUALIFICATION_BELOW_GCSEO_LEVEL_EG_TRADE_APPRENTICESHIPS = '6'
    OTHER_QUALIFICATION_INCL_PROFESSIONAL__VOCATIONAL__FOREIGN = '7'
    QUALIFICATIONS___BUT_DK_WHICH = '8'
    QUALIFICATIONS___GCSE___BUT_DK_GRADE = '9'
    QUALIFICATIONS___CITY_AND_GUILDS___DK_LEVEL = '10'
    QUALIFICATIONS___OTHER___BUT_DK_GRADELEVEL = '11'
    NO_QUALIFICATIONS = '12'
    ELIGIBLE___NO_ANSWER = '13'
    UNDER_16YRS___INELIGIBLE_FOR_QUALIFICATIONS_QUESTIONS = '14'


class AGELEFT(OrderedEnum):
    UP_TO_14_YRS = '1'
    N15___18_YRS = '2'
    N19___25_YRS = '3'
    N26_YRS_AND_OVER = '4'
    STILL_IN_EDUCATION = '5'
    NEVER_IN_FULL_TIME_EDUCATION = '6'
    N16YRS_OR_OVER____ANSWER_MISSING = '7'
    UNDER_16YRS___INELIGIBLE_FOR_QUESTION = '8'


class LIVARR(OrderedEnum):
    MARRIED__AND_LIVING_WITH_SPOUSE = '1'
    COHABITING = '2'
    SINGLE_NEVER_MARRIED = '3'
    SEPARATED_BUT_STILL_MARRIED = '4'
    DIVORCED = '5'
    WIDOWED = '6'
    NO_ANSWER_DK = '7'
    UNDER_16YRS___INELIGIBLE = '8'
    MISSING1 = '-1'


class PROVCARE(OrderedEnum):
    YES = '1'
    NO = '2'
    DKREFUSE = '3'


class HMONTH(OrderedEnum):
    JANUARY = '1'
    FEBRUARY = '2'
    MARCH = '3'
    APRIL = '4'
    MAY = '5'
    JUNE = '6'
    JULY = '7'
    AUGUST = '8'
    SEPTEMBER = '9'
    OCTOBER = '10'
    NOVEMBER = '11'
    DECEMBER = '12'
    MISSING1 = '99'


class GORPAF(OrderedEnum):
    NORTH_EAST = '1'
    NORTH_WEST_INCL_MERSEYSIDE = '2'
    YORKSHIRE_AND_HUMBERSIDE = '3'
    EAST_MIDLANDS = '4'
    WEST_MIDLANDS = '5'
    EASTERN = '6'
    LONDON = '7'
    SOUTH_EAST_EXCL_LONDON = '8'
    SOUTH_WEST = '9'
    WALES = '10'
    SCOTLAND = '11'
    NORTHERN_IRELAND = '12'


class GORPAF2(OrderedEnum):
    NORTH = '1'
    MIDLANDS = '2'
    EASTERN = '3'
    LONDON_AND_SOUTH_EAST = '4'
    SOUTH_WEST = '5'
    WALES = '6'
    SCOTLAND = '7'
    NORTHERN_IRELAND = '8'


class GORPAF3(OrderedEnum):
    ENGLAND = '1'
    WALES = '2'
    SCOTLAND = '3'
    NORTHERN_IRELAND = '4'


class POP_DEN2(OrderedEnum):
    MISSING = '-9'
    ____0______249 = '1'
    _250______999 = '2'
    N1000___1999 = '3'
    N2000___2999 = '4'
    N3000___3999 = '5'
    N4000___4999 = '6'
    N5000_OR_MORE_MAX_WAS_JUST_OVER_10_000 = '7'


class UNEMP2(OrderedEnum):
    MISSING = '-9'
    ____0______2_49_PERCENT = '1'
    _2_50_____4_99_PERCENT = '2'
    _5_00_____7_49_PERCENT = '3'
    _7_50_____9_99_PERCENT = '4'
    N10_00___14_99_PERCENT = '5'
    N15_00_PERCENT_OR_MORE_MAX_WAS_ABOUT_24_PERCENT_ = '6'


class CHILD(OrderedEnum):
    YES = '1'
    NO = '2'


class AGEYNGST(OrderedEnum):
    __0_____2_YRS = '1'
    __3_____4_YRS = '2'
    __5_____9_YRS = '3'
    N10___15_YRS = '4'
    N16___17_YRS = '5'
    N18_YRS_OR_MORE = '6'


class TENURE2(OrderedEnum):
    OWNS___OUTRIGHT = '1'
    OWNS___BUYING_WITH_MORTGAGE = '2'
    RENTS = '3'
    DK_REFUSE = '4'


CARAVAIL = CHILD


class GROSHINC(OrderedEnum):
    LESS_THAN_2_610_POUNDS = '1'
    __2_610_____5_210_POUNDS = '2'
    __5_210___10_430_POUNDS = '3'
    N10_430___15_640_POUNDS = '4'
    N15_640___20_860_POUNDS = '5'
    N20_860___33_800_POUNDS = '6'
    N33_800___41_000_POUNDS = '7'
    N41_000___46_000_POUNDS = '8'
    N46_000___55_000_POUNDS = '9'
    N55_000___80_000_POUNDS = '10'
    N80_000_POUNDS_OR_MORE = '11'
    DON_T_KNOW = '12'
    REFUSE = '13'


class HHTYPE4(OrderedEnum):
    SINGLE_PERSON_HOUSEHOLD = '1'
    HHLDS_WITH_2_OR_MORE_UNRELATED_PEOPLE_ONLY = '2'
    MARRIED_COUPLE___NO_CHILDREN_COUPLE_ONLY = '3'
    MARRIED_COUPLE___WITH_CHILDREN_SMALLEREQUAL_15 = '4'
    MARRIED_COUPLE___WITH_CHILDREN_GREATEREQUAL_16 = '5'
    COHAB_COUPLE___NO_CHILDREN_COUPLE_ONLY = '6'
    COHAB_COUPLE___WITH_CHILDREN_SMALLEREQUAL_15 = '7'
    COHAB_COUPLE___WITH_CHILDREN_GREATEREQUAL_16 = '8'
    SINGLE_PARENT____WITH_CHILDREN_SMALLEREQUAL_15 = '9'
    SINGLE_PARENT___WITH_CHILDREN_GREATEREQUAL_16 = '10'
    TWO_OR_MORE_COUPLES_MARRIED_OR_COHAB_WITHWITHOUT_CHILDRN = '11'
    SAME_SEX_COUPLES___SPONTANEOUSLY_DESCRIBED = '12'
    UNCLASSIFIED___MARRIED_COUPLES_IN_COMPLEX_HHLDS = '13'
    UNCLASSIFIED___COHABITING_COUPLES_IN_COMPLEX_HHLDS = '14'
    UNCLASSIFIED___SINGLE_PARENTS_IN_COMPLEX_HHLDS = '15'
    UNCLASSIFIED___OTHER_HHLDS_WITHOUT_COUPLES_EG_BROTHERS_DK = '16'


class HHTYPE5(OrderedEnum):
    SINGLE_PERSON_HOUSEHOLD = '1'
    MARRIEDCOHAB_COUPLE___WITH_CHILDREN_SMALLEREQUAL_15 = '2'
    MARRIEDCOHAB_COUPLE____NO_CHILDREN_SMALLEREQUAL_15 = '3'
    SINGLE_PARENT____WITH_CHILDREN_SMALLEREQUAL_15 = '4'
    SINGLE_PARENT_____NO_CHILDREN_SMALLEREQUAL_15 = '5'
    UNCLASSIFIED___MARRIEDCOHAB_COUPLES_IN_COMPLEX_HHLDS = '6'
    UNCLASSIFIED___SINGLE_PARENTS_IN_COMPLEX_HHLDS = '7'
    OTHER_HHLDS_EG_BROTHERSSISTERS_UNRELATED_ETC = '8'
