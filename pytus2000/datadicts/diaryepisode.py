"""This is a auto-generated data dictionary file of the UK Time Use Study 2000."""
from enum import Enum

from pytus2000.datadicts import OrderedEnum, VariableEnum


class Variable(VariableEnum):
    SN1 = (1, "Point Number")
    SN2 = (2, "Household Number")
    SN3 = (3, "Person number")
    SN4 = (4, "Diary number")
    DTYPE = (5, "Diary Type")
    DDAY = (6, "Diary - Day of month")
    DMONTH = (7, "Diary - Month")
    DYEAR = (8, "Diary - Year")
    DDAYOFWK = (9, "Diary - day of week")
    EVACT1 = (10, "main activity -episode 1")
    EVACT2 = (11, "main activity -episode 2")
    EVACT3 = (12, "main activity -episode 3")
    EVACT4 = (13, "main activity -episode 4")
    EVACT5 = (14, "main activity -episode 5")
    EVACT6 = (15, "main activity -episode 6")
    EVACT7 = (16, "main activity -episode 7")
    EVACT8 = (17, "main activity -episode 8")
    EVACT9 = (18, "main activity -episode 9")
    EVACT10 = (19, "main activity -episode 10")
    EVACT11 = (20, "main activity -episode 11")
    EVACT12 = (21, "main activity -episode 12")
    EVACT13 = (22, "main activity -episode 13")
    EVACT14 = (23, "main activity -episode 14")
    EVACT15 = (24, "main activity -episode 15")
    EVACT16 = (25, "main activity -episode 16")
    EVACT17 = (26, "main activity -episode 17")
    EVACT18 = (27, "main activity -episode 18")
    EVACT19 = (28, "main activity -episode 19")
    EVACT20 = (29, "main activity -episode 20")
    EVACT21 = (30, "main activity -episode 21")
    EVACT22 = (31, "main activity -episode 22")
    EVACT23 = (32, "main activity -episode 23")
    EVACT24 = (33, "main activity -episode 24")
    EVACT25 = (34, "main activity -episode 25")
    EVACT26 = (35, "main activity -episode 26")
    EVACT27 = (36, "main activity -episode 27")
    EVACT28 = (37, "main activity -episode 28")
    EVACT29 = (38, "main activity -episode 29")
    EVACT30 = (39, "main activity -episode 30")
    EVACT31 = (40, "main activity -episode 31")
    EVACT32 = (41, "main activity -episode 32")
    EVACT33 = (42, "main activity -episode 33")
    EVACT34 = (43, "main activity -episode 34")
    EVACT35 = (44, "main activity -episode 35")
    EVACT36 = (45, "main activity -episode 36")
    EVACT37 = (46, "main activity -episode 37")
    EVACT38 = (47, "main activity -episode 38")
    EVACT39 = (48, "main activity -episode 39")
    EVACT40 = (49, "main activity -episode 40")
    EVACT41 = (50, "main activity -episode 41")
    EVACT42 = (51, "main activity -episode 42")
    EVACT43 = (52, "main activity -episode 43")
    EVACT44 = (53, "main activity -episode 44")
    EVACT45 = (54, "main activity -episode 45")
    EVACT46 = (55, "main activity -episode 46")
    EVACT47 = (56, "main activity -episode 47")
    EVACT48 = (57, "main activity -episode 48")
    EVACT49 = (58, "main activity -episode 49")
    EVACT50 = (59, "main activity -episode 50")
    EVACT51 = (60, "main activity -episode 51")
    EVACT52 = (61, "main activity -episode 52")
    EVACT53 = (62, "main activity -episode 53")
    EVACT54 = (63, "main activity -episode 54")
    EVACT55 = (64, "main activity -episode 55")
    EVACT56 = (65, "main activity -episode 56")
    EVACT57 = (66, "main activity -episode 57")
    EVACT58 = (67, "main activity -episode 58")
    EVACT59 = (68, "main activity -episode 59")
    EVACT60 = (69, "main activity -episode 60")
    EVACT61 = (70, "main activity -episode 61")
    EVACT62 = (71, "main activity -episode 62")
    EVACT63 = (72, "main activity -episode 63")
    EVACT64 = (73, "main activity -episode 64")
    EVACT65 = (74, "main activity -episode 65")
    EVACT66 = (75, "main activity -episode 66")
    EVACT67 = (76, "main activity -episode 67")
    EVACT68 = (77, "main activity -episode 68")
    EVACT69 = (78, "main activity -episode 69")
    EVACT70 = (79, "main activity -episode 70")
    EVACT71 = (80, "main activity -episode 71")
    EVACT72 = (81, "main activity -episode 72")
    EVACT73 = (82, "main activity -episode 73")
    EVACT74 = (83, "main activity -episode 74")
    EVACT75 = (84, "main activity -episode 75")
    EVACT76 = (85, "main activity -episode 76")
    EVACT77 = (86, "main activity -episode 77")
    EVACT78 = (87, "main activity -episode 78")
    EVACT79 = (88, "main activity -episode 79")
    EVACT80 = (89, "main activity -episode 80")
    EVACT81 = (90, "main activity -episode 81")
    EVACT82 = (91, "main activity -episode 82")
    EVACT83 = (92, "main activity -episode 83")
    EVACT84 = (93, "main activity -episode 84")
    EVACT85 = (94, "main activity -episode 85")
    EVACT86 = (95, "main activity -episode 86")
    EVACT87 = (96, "main activity -episode 87")
    EVACT88 = (97, "main activity -episode 88")
    EVACT89 = (98, "main activity -episode 89")
    EVACT90 = (99, "main activity -episode 90")
    EVACT91 = (100, "main activity -episode 91")
    EVACT92 = (101, "main activity -episode 92")
    EVACT93 = (102, "main activity -episode 93")
    EVACT94 = (103, "main activity -episode 94")
    EVACT95 = (104, "main activity -episode 95")
    EVACT96 = (105, "main activity -episode 96")
    EVACT97 = (106, "main activity -episode 97")
    EVACT98 = (107, "main activity -episode 98")
    EVACT99 = (108, "main activity -episode 99")
    ESACT1 = (109, "secondary activity -episode 1")
    ESACT2 = (110, "secondary activity -episode 2")
    ESACT3 = (111, "secondary activity -episode 3")
    ESACT4 = (112, "secondary activity -episode 4")
    ESACT5 = (113, "secondary activity -episode 5")
    ESACT6 = (114, "secondary activity -episode 6")
    ESACT7 = (115, "secondary activity -episode 7")
    ESACT8 = (116, "secondary activity -episode 8")
    ESACT9 = (117, "secondary activity -episode 9")
    ESACT10 = (118, "secondary activity -episode 10")
    ESACT11 = (119, "secondary activity -episode 11")
    ESACT12 = (120, "secondary activity -episode 12")
    ESACT13 = (121, "secondary activity -episode 13")
    ESACT14 = (122, "secondary activity -episode 14")
    ESACT15 = (123, "secondary activity -episode 15")
    ESACT16 = (124, "secondary activity -episode 16")
    ESACT17 = (125, "secondary activity -episode 17")
    ESACT18 = (126, "secondary activity -episode 18")
    ESACT19 = (127, "secondary activity -episode 19")
    ESACT20 = (128, "secondary activity -episode 20")
    ESACT21 = (129, "secondary activity -episode 21")
    ESACT22 = (130, "secondary activity -episode 22")
    ESACT23 = (131, "secondary activity -episode 23")
    ESACT24 = (132, "secondary activity -episode 24")
    ESACT25 = (133, "secondary activity -episode 25")
    ESACT26 = (134, "secondary activity -episode 26")
    ESACT27 = (135, "secondary activity -episode 27")
    ESACT28 = (136, "secondary activity -episode 28")
    ESACT29 = (137, "secondary activity -episode 29")
    ESACT30 = (138, "secondary activity -episode 30")
    ESACT31 = (139, "secondary activity -episode 31")
    ESACT32 = (140, "secondary activity -episode 32")
    ESACT33 = (141, "secondary activity -episode 33")
    ESACT34 = (142, "secondary activity -episode 34")
    ESACT35 = (143, "secondary activity -episode 35")
    ESACT36 = (144, "secondary activity -episode 36")
    ESACT37 = (145, "secondary activity -episode 37")
    ESACT38 = (146, "secondary activity -episode 38")
    ESACT39 = (147, "secondary activity -episode 39")
    ESACT40 = (148, "secondary activity -episode 40")
    ESACT41 = (149, "secondary activity -episode 41")
    ESACT42 = (150, "secondary activity -episode 42")
    ESACT43 = (151, "secondary activity -episode 43")
    ESACT44 = (152, "secondary activity -episode 44")
    ESACT45 = (153, "secondary activity -episode 45")
    ESACT46 = (154, "secondary activity -episode 46")
    ESACT47 = (155, "secondary activity -episode 47")
    ESACT48 = (156, "secondary activity -episode 48")
    ESACT49 = (157, "secondary activity -episode 49")
    ESACT50 = (158, "secondary activity -episode 50")
    ESACT51 = (159, "secondary activity -episode 51")
    ESACT52 = (160, "secondary activity -episode 52")
    ESACT53 = (161, "secondary activity -episode 53")
    ESACT54 = (162, "secondary activity -episode 54")
    ESACT55 = (163, "secondary activity -episode 55")
    ESACT56 = (164, "secondary activity -episode 56")
    ESACT57 = (165, "secondary activity -episode 57")
    ESACT58 = (166, "secondary activity -episode 58")
    ESACT59 = (167, "secondary activity -episode 59")
    ESACT60 = (168, "secondary activity -episode 60")
    ESACT61 = (169, "secondary activity -episode 61")
    ESACT62 = (170, "secondary activity -episode 62")
    ESACT63 = (171, "secondary activity -episode 63")
    ESACT64 = (172, "secondary activity -episode 64")
    ESACT65 = (173, "secondary activity -episode 65")
    ESACT66 = (174, "secondary activity -episode 66")
    ESACT67 = (175, "secondary activity -episode 67")
    ESACT68 = (176, "secondary activity -episode 68")
    ESACT69 = (177, "secondary activity -episode 69")
    ESACT70 = (178, "secondary activity -episode 70")
    ESACT71 = (179, "secondary activity -episode 71")
    ESACT72 = (180, "secondary activity -episode 72")
    ESACT73 = (181, "secondary activity -episode 73")
    ESACT74 = (182, "secondary activity -episode 74")
    ESACT75 = (183, "secondary activity -episode 75")
    ESACT76 = (184, "secondary activity -episode 76")
    ESACT77 = (185, "secondary activity -episode 77")
    ESACT78 = (186, "secondary activity -episode 78")
    ESACT79 = (187, "secondary activity -episode 79")
    ESACT80 = (188, "secondary activity -episode 80")
    ESACT81 = (189, "secondary activity -episode 81")
    ESACT82 = (190, "secondary activity -episode 82")
    ESACT83 = (191, "secondary activity -episode 83")
    ESACT84 = (192, "secondary activity -episode 84")
    ESACT85 = (193, "secondary activity -episode 85")
    ESACT86 = (194, "secondary activity -episode 86")
    ESACT87 = (195, "secondary activity -episode 87")
    ESACT88 = (196, "secondary activity -episode 88")
    ESACT89 = (197, "secondary activity -episode 89")
    ESACT90 = (198, "secondary activity -episode 90")
    ESACT91 = (199, "secondary activity -episode 91")
    ESACT92 = (200, "secondary activity -episode 92")
    ESACT93 = (201, "secondary activity -episode 93")
    ESACT94 = (202, "secondary activity -episode 94")
    ESACT95 = (203, "secondary activity -episode 95")
    ESACT96 = (204, "secondary activity -episode 96")
    ESACT97 = (205, "secondary activity -episode 97")
    ESACT98 = (206, "secondary activity -episode 98")
    ESACT99 = (207, "secondary activity -episode 99")
    EWHER1 = (208, "location -episode 1")
    EWHER2 = (209, "location -episode 2")
    EWHER3 = (210, "location -episode 3")
    EWHER4 = (211, "location -episode 4")
    EWHER5 = (212, "location -episode 5")
    EWHER6 = (213, "location -episode 6")
    EWHER7 = (214, "location -episode 7")
    EWHER8 = (215, "location -episode 8")
    EWHER9 = (216, "location -episode 9")
    EWHER10 = (217, "location -episode 10")
    EWHER11 = (218, "location -episode 11")
    EWHER12 = (219, "location -episode 12")
    EWHER13 = (220, "location -episode 13")
    EWHER14 = (221, "location -episode 14")
    EWHER15 = (222, "location -episode 15")
    EWHER16 = (223, "location -episode 16")
    EWHER17 = (224, "location -episode 17")
    EWHER18 = (225, "location -episode 18")
    EWHER19 = (226, "location -episode 19")
    EWHER20 = (227, "location -episode 20")
    EWHER21 = (228, "location -episode 21")
    EWHER22 = (229, "location -episode 22")
    EWHER23 = (230, "location -episode 23")
    EWHER24 = (231, "location -episode 24")
    EWHER25 = (232, "location -episode 25")
    EWHER26 = (233, "location -episode 26")
    EWHER27 = (234, "location -episode 27")
    EWHER28 = (235, "location -episode 28")
    EWHER29 = (236, "location -episode 29")
    EWHER30 = (237, "location -episode 30")
    EWHER31 = (238, "location -episode 31")
    EWHER32 = (239, "location -episode 32")
    EWHER33 = (240, "location -episode 33")
    EWHER34 = (241, "location -episode 34")
    EWHER35 = (242, "location -episode 35")
    EWHER36 = (243, "location -episode 36")
    EWHER37 = (244, "location -episode 37")
    EWHER38 = (245, "location -episode 38")
    EWHER39 = (246, "location -episode 39")
    EWHER40 = (247, "location -episode 40")
    EWHER41 = (248, "location -episode 41")
    EWHER42 = (249, "location -episode 42")
    EWHER43 = (250, "location -episode 43")
    EWHER44 = (251, "location -episode 44")
    EWHER45 = (252, "location -episode 45")
    EWHER46 = (253, "location -episode 46")
    EWHER47 = (254, "location -episode 47")
    EWHER48 = (255, "location -episode 48")
    EWHER49 = (256, "location -episode 49")
    EWHER50 = (257, "location -episode 50")
    EWHER51 = (258, "location -episode 51")
    EWHER52 = (259, "location -episode 52")
    EWHER53 = (260, "location -episode 53")
    EWHER54 = (261, "location -episode 54")
    EWHER55 = (262, "location -episode 55")
    EWHER56 = (263, "location -episode 56")
    EWHER57 = (264, "location -episode 57")
    EWHER58 = (265, "location -episode 58")
    EWHER59 = (266, "location -episode 59")
    EWHER60 = (267, "location -episode 60")
    EWHER61 = (268, "location -episode 61")
    EWHER62 = (269, "location -episode 62")
    EWHER63 = (270, "location -episode 63")
    EWHER64 = (271, "location -episode 64")
    EWHER65 = (272, "location -episode 65")
    EWHER66 = (273, "location -episode 66")
    EWHER67 = (274, "location -episode 67")
    EWHER68 = (275, "location -episode 68")
    EWHER69 = (276, "location -episode 69")
    EWHER70 = (277, "location -episode 70")
    EWHER71 = (278, "location -episode 71")
    EWHER72 = (279, "location -episode 72")
    EWHER73 = (280, "location -episode 73")
    EWHER74 = (281, "location -episode 74")
    EWHER75 = (282, "location -episode 75")
    EWHER76 = (283, "location -episode 76")
    EWHER77 = (284, "location -episode 77")
    EWHER78 = (285, "location -episode 78")
    EWHER79 = (286, "location -episode 79")
    EWHER80 = (287, "location -episode 80")
    EWHER81 = (288, "location -episode 81")
    EWHER82 = (289, "location -episode 82")
    EWHER83 = (290, "location -episode 83")
    EWHER84 = (291, "location -episode 84")
    EWHER85 = (292, "location -episode 85")
    EWHER86 = (293, "location -episode 86")
    EWHER87 = (294, "location -episode 87")
    EWHER88 = (295, "location -episode 88")
    EWHER89 = (296, "location -episode 89")
    EWHER90 = (297, "location -episode 90")
    EWHER91 = (298, "location -episode 91")
    EWHER92 = (299, "location -episode 92")
    EWHER93 = (300, "location -episode 93")
    EWHER94 = (301, "location -episode 94")
    EWHER95 = (302, "location -episode 95")
    EWHER96 = (303, "location -episode 96")
    EWHER97 = (304, "location -episode 97")
    EWHER98 = (305, "location -episode 98")
    EWHER99 = (306, "location -episode 99")
    EWIT01 = (307, "alone -episode 1")
    EWIT02 = (308, "alone -episode 2")
    EWIT03 = (309, "alone -episode 3")
    EWIT04 = (310, "alone -episode 4")
    EWIT05 = (311, "alone -episode 5")
    EWIT06 = (312, "alone -episode 6")
    EWIT07 = (313, "alone -episode 7")
    EWIT08 = (314, "alone -episode 8")
    EWIT09 = (315, "alone -episode 9")
    EWIT010 = (316, "alone -episode 10")
    EWIT011 = (317, "alone -episode 11")
    EWIT012 = (318, "alone -episode 12")
    EWIT013 = (319, "alone -episode 13")
    EWIT014 = (320, "alone -episode 14")
    EWIT015 = (321, "alone -episode 15")
    EWIT016 = (322, "alone -episode 16")
    EWIT017 = (323, "alone -episode 17")
    EWIT018 = (324, "alone -episode 18")
    EWIT019 = (325, "alone -episode 19")
    EWIT020 = (326, "alone -episode 20")
    EWIT021 = (327, "alone -episode 21")
    EWIT022 = (328, "alone -episode 22")
    EWIT023 = (329, "alone -episode 23")
    EWIT024 = (330, "alone -episode 24")
    EWIT025 = (331, "alone -episode 25")
    EWIT026 = (332, "alone -episode 26")
    EWIT027 = (333, "alone -episode 27")
    EWIT028 = (334, "alone -episode 28")
    EWIT029 = (335, "alone -episode 29")
    EWIT030 = (336, "alone -episode 30")
    EWIT031 = (337, "alone -episode 31")
    EWIT032 = (338, "alone -episode 32")
    EWIT033 = (339, "alone -episode 33")
    EWIT034 = (340, "alone -episode 34")
    EWIT035 = (341, "alone -episode 35")
    EWIT036 = (342, "alone -episode 36")
    EWIT037 = (343, "alone -episode 37")
    EWIT038 = (344, "alone -episode 38")
    EWIT039 = (345, "alone -episode 39")
    EWIT040 = (346, "alone -episode 40")
    EWIT041 = (347, "alone -episode 41")
    EWIT042 = (348, "alone -episode 42")
    EWIT043 = (349, "alone -episode 43")
    EWIT044 = (350, "alone -episode 44")
    EWIT045 = (351, "alone -episode 45")
    EWIT046 = (352, "alone -episode 46")
    EWIT047 = (353, "alone -episode 47")
    EWIT048 = (354, "alone -episode 48")
    EWIT049 = (355, "alone -episode 49")
    EWIT050 = (356, "alone -episode 50")
    EWIT051 = (357, "alone -episode 51")
    EWIT052 = (358, "alone -episode 52")
    EWIT053 = (359, "alone -episode 53")
    EWIT054 = (360, "alone -episode 54")
    EWIT055 = (361, "alone -episode 55")
    EWIT056 = (362, "alone -episode 56")
    EWIT057 = (363, "alone -episode 57")
    EWIT058 = (364, "alone -episode 58")
    EWIT059 = (365, "alone -episode 59")
    EWIT060 = (366, "alone -episode 60")
    EWIT061 = (367, "alone -episode 61")
    EWIT062 = (368, "alone -episode 62")
    EWIT063 = (369, "alone -episode 63")
    EWIT064 = (370, "alone -episode 64")
    EWIT065 = (371, "alone -episode 65")
    EWIT066 = (372, "alone -episode 66")
    EWIT067 = (373, "alone -episode 67")
    EWIT068 = (374, "alone -episode 68")
    EWIT069 = (375, "alone -episode 69")
    EWIT070 = (376, "alone -episode 70")
    EWIT071 = (377, "alone -episode 71")
    EWIT072 = (378, "alone -episode 72")
    EWIT073 = (379, "alone -episode 73")
    EWIT074 = (380, "alone -episode 74")
    EWIT075 = (381, "alone -episode 75")
    EWIT076 = (382, "alone -episode 76")
    EWIT077 = (383, "alone -episode 77")
    EWIT078 = (384, "alone -episode 78")
    EWIT079 = (385, "alone -episode 79")
    EWIT080 = (386, "alone -episode 80")
    EWIT081 = (387, "alone -episode 81")
    EWIT082 = (388, "alone -episode 82")
    EWIT083 = (389, "alone -episode 83")
    EWIT084 = (390, "alone -episode 84")
    EWIT085 = (391, "alone -episode 85")
    EWIT086 = (392, "alone -episode 86")
    EWIT087 = (393, "alone -episode 87")
    EWIT088 = (394, "alone -episode 88")
    EWIT089 = (395, "alone -episode 89")
    EWIT090 = (396, "alone -episode 90")
    EWIT091 = (397, "alone -episode 91")
    EWIT092 = (398, "alone -episode 92")
    EWIT093 = (399, "alone -episode 93")
    EWIT094 = (400, "alone -episode 94")
    EWIT095 = (401, "alone -episode 95")
    EWIT096 = (402, "alone -episode 96")
    EWIT097 = (403, "alone -episode 97")
    EWIT098 = (404, "alone -episode 98")
    EWIT099 = (405, "alone -episode 99")
    EWIT11 = (406, "with kids 0-9 -episode 1")
    EWIT12 = (407, "with kids 0-9 -episode 2")
    EWIT13 = (408, "with kids 0-9 -episode 3")
    EWIT14 = (409, "with kids 0-9 -episode 4")
    EWIT15 = (410, "with kids 0-9 -episode 5")
    EWIT16 = (411, "with kids 0-9 -episode 6")
    EWIT17 = (412, "with kids 0-9 -episode 7")
    EWIT18 = (413, "with kids 0-9 -episode 8")
    EWIT19 = (414, "with kids 0-9 -episode 9")
    EWIT110 = (415, "with kids 0-9 -episode 10")
    EWIT111 = (416, "with kids 0-9 -episode 11")
    EWIT112 = (417, "with kids 0-9 -episode 12")
    EWIT113 = (418, "with kids 0-9 -episode 13")
    EWIT114 = (419, "with kids 0-9 -episode 14")
    EWIT115 = (420, "with kids 0-9 -episode 15")
    EWIT116 = (421, "with kids 0-9 -episode 16")
    EWIT117 = (422, "with kids 0-9 -episode 17")
    EWIT118 = (423, "with kids 0-9 -episode 18")
    EWIT119 = (424, "with kids 0-9 -episode 19")
    EWIT120 = (425, "with kids 0-9 -episode 20")
    EWIT121 = (426, "with kids 0-9 -episode 21")
    EWIT122 = (427, "with kids 0-9 -episode 22")
    EWIT123 = (428, "with kids 0-9 -episode 23")
    EWIT124 = (429, "with kids 0-9 -episode 24")
    EWIT125 = (430, "with kids 0-9 -episode 25")
    EWIT126 = (431, "with kids 0-9 -episode 26")
    EWIT127 = (432, "with kids 0-9 -episode 27")
    EWIT128 = (433, "with kids 0-9 -episode 28")
    EWIT129 = (434, "with kids 0-9 -episode 29")
    EWIT130 = (435, "with kids 0-9 -episode 30")
    EWIT131 = (436, "with kids 0-9 -episode 31")
    EWIT132 = (437, "with kids 0-9 -episode 32")
    EWIT133 = (438, "with kids 0-9 -episode 33")
    EWIT134 = (439, "with kids 0-9 -episode 34")
    EWIT135 = (440, "with kids 0-9 -episode 35")
    EWIT136 = (441, "with kids 0-9 -episode 36")
    EWIT137 = (442, "with kids 0-9 -episode 37")
    EWIT138 = (443, "with kids 0-9 -episode 38")
    EWIT139 = (444, "with kids 0-9 -episode 39")
    EWIT140 = (445, "with kids 0-9 -episode 40")
    EWIT141 = (446, "with kids 0-9 -episode 41")
    EWIT142 = (447, "with kids 0-9 -episode 42")
    EWIT143 = (448, "with kids 0-9 -episode 43")
    EWIT144 = (449, "with kids 0-9 -episode 44")
    EWIT145 = (450, "with kids 0-9 -episode 45")
    EWIT146 = (451, "with kids 0-9 -episode 46")
    EWIT147 = (452, "with kids 0-9 -episode 47")
    EWIT148 = (453, "with kids 0-9 -episode 48")
    EWIT149 = (454, "with kids 0-9 -episode 49")
    EWIT150 = (455, "with kids 0-9 -episode 50")
    EWIT151 = (456, "with kids 0-9 -episode 51")
    EWIT152 = (457, "with kids 0-9 -episode 52")
    EWIT153 = (458, "with kids 0-9 -episode 53")
    EWIT154 = (459, "with kids 0-9 -episode 54")
    EWIT155 = (460, "with kids 0-9 -episode 55")
    EWIT156 = (461, "with kids 0-9 -episode 56")
    EWIT157 = (462, "with kids 0-9 -episode 57")
    EWIT158 = (463, "with kids 0-9 -episode 58")
    EWIT159 = (464, "with kids 0-9 -episode 59")
    EWIT160 = (465, "with kids 0-9 -episode 60")
    EWIT161 = (466, "with kids 0-9 -episode 61")
    EWIT162 = (467, "with kids 0-9 -episode 62")
    EWIT163 = (468, "with kids 0-9 -episode 63")
    EWIT164 = (469, "with kids 0-9 -episode 64")
    EWIT165 = (470, "with kids 0-9 -episode 65")
    EWIT166 = (471, "with kids 0-9 -episode 66")
    EWIT167 = (472, "with kids 0-9 -episode 67")
    EWIT168 = (473, "with kids 0-9 -episode 68")
    EWIT169 = (474, "with kids 0-9 -episode 69")
    EWIT170 = (475, "with kids 0-9 -episode 70")
    EWIT171 = (476, "with kids 0-9 -episode 71")
    EWIT172 = (477, "with kids 0-9 -episode 72")
    EWIT173 = (478, "with kids 0-9 -episode 73")
    EWIT174 = (479, "with kids 0-9 -episode 74")
    EWIT175 = (480, "with kids 0-9 -episode 75")
    EWIT176 = (481, "with kids 0-9 -episode 76")
    EWIT177 = (482, "with kids 0-9 -episode 77")
    EWIT178 = (483, "with kids 0-9 -episode 78")
    EWIT179 = (484, "with kids 0-9 -episode 79")
    EWIT180 = (485, "with kids 0-9 -episode 80")
    EWIT181 = (486, "with kids 0-9 -episode 81")
    EWIT182 = (487, "with kids 0-9 -episode 82")
    EWIT183 = (488, "with kids 0-9 -episode 83")
    EWIT184 = (489, "with kids 0-9 -episode 84")
    EWIT185 = (490, "with kids 0-9 -episode 85")
    EWIT186 = (491, "with kids 0-9 -episode 86")
    EWIT187 = (492, "with kids 0-9 -episode 87")
    EWIT188 = (493, "with kids 0-9 -episode 88")
    EWIT189 = (494, "with kids 0-9 -episode 89")
    EWIT190 = (495, "with kids 0-9 -episode 90")
    EWIT191 = (496, "with kids 0-9 -episode 91")
    EWIT192 = (497, "with kids 0-9 -episode 92")
    EWIT193 = (498, "with kids 0-9 -episode 93")
    EWIT194 = (499, "with kids 0-9 -episode 94")
    EWIT195 = (500, "with kids 0-9 -episode 95")
    EWIT196 = (501, "with kids 0-9 -episode 96")
    EWIT197 = (502, "with kids 0-9 -episode 97")
    EWIT198 = (503, "with kids 0-9 -episode 98")
    EWIT199 = (504, "with kids 0-9 -episode 99")
    EWIT21 = (505, "with kids 10-13 -episode 1")
    EWIT22 = (506, "with kids 10-13 -episode 2")
    EWIT23 = (507, "with kids 10-13 -episode 3")
    EWIT24 = (508, "with kids 10-13 -episode 4")
    EWIT25 = (509, "with kids 10-13 -episode 5")
    EWIT26 = (510, "with kids 10-13 -episode 6")
    EWIT27 = (511, "with kids 10-13 -episode 7")
    EWIT28 = (512, "with kids 10-13 -episode 8")
    EWIT29 = (513, "with kids 10-13 -episode 9")
    EWIT210 = (514, "with kids 10-13 -episode 10")
    EWIT211 = (515, "with kids 10-13 -episode 11")
    EWIT212 = (516, "with kids 10-13 -episode 12")
    EWIT213 = (517, "with kids 10-13 -episode 13")
    EWIT214 = (518, "with kids 10-13 -episode 14")
    EWIT215 = (519, "with kids 10-13 -episode 15")
    EWIT216 = (520, "with kids 10-13 -episode 16")
    EWIT217 = (521, "with kids 10-13 -episode 17")
    EWIT218 = (522, "with kids 10-13 -episode 18")
    EWIT219 = (523, "with kids 10-13 -episode 19")
    EWIT220 = (524, "with kids 10-13 -episode 20")
    EWIT221 = (525, "with kids 10-13 -episode 21")
    EWIT222 = (526, "with kids 10-13 -episode 22")
    EWIT223 = (527, "with kids 10-13 -episode 23")
    EWIT224 = (528, "with kids 10-13 -episode 24")
    EWIT225 = (529, "with kids 10-13 -episode 25")
    EWIT226 = (530, "with kids 10-13 -episode 26")
    EWIT227 = (531, "with kids 10-13 -episode 27")
    EWIT228 = (532, "with kids 10-13 -episode 28")
    EWIT229 = (533, "with kids 10-13 -episode 29")
    EWIT230 = (534, "with kids 10-13 -episode 30")
    EWIT231 = (535, "with kids 10-13 -episode 31")
    EWIT232 = (536, "with kids 10-13 -episode 32")
    EWIT233 = (537, "with kids 10-13 -episode 33")
    EWIT234 = (538, "with kids 10-13 -episode 34")
    EWIT235 = (539, "with kids 10-13 -episode 35")
    EWIT236 = (540, "with kids 10-13 -episode 36")
    EWIT237 = (541, "with kids 10-13 -episode 37")
    EWIT238 = (542, "with kids 10-13 -episode 38")
    EWIT239 = (543, "with kids 10-13 -episode 39")
    EWIT240 = (544, "with kids 10-13 -episode 40")
    EWIT241 = (545, "with kids 10-13 -episode 41")
    EWIT242 = (546, "with kids 10-13 -episode 42")
    EWIT243 = (547, "with kids 10-13 -episode 43")
    EWIT244 = (548, "with kids 10-13 -episode 44")
    EWIT245 = (549, "with kids 10-13 -episode 45")
    EWIT246 = (550, "with kids 10-13 -episode 46")
    EWIT247 = (551, "with kids 10-13 -episode 47")
    EWIT248 = (552, "with kids 10-13 -episode 48")
    EWIT249 = (553, "with kids 10-13 -episode 49")
    EWIT250 = (554, "with kids 10-13 -episode 50")
    EWIT251 = (555, "with kids 10-13 -episode 51")
    EWIT252 = (556, "with kids 10-13 -episode 52")
    EWIT253 = (557, "with kids 10-13 -episode 53")
    EWIT254 = (558, "with kids 10-13 -episode 54")
    EWIT255 = (559, "with kids 10-13 -episode 55")
    EWIT256 = (560, "with kids 10-13 -episode 56")
    EWIT257 = (561, "with kids 10-13 -episode 57")
    EWIT258 = (562, "with kids 10-13 -episode 58")
    EWIT259 = (563, "with kids 10-13 -episode 59")
    EWIT260 = (564, "with kids 10-13 -episode 60")
    EWIT261 = (565, "with kids 10-13 -episode 61")
    EWIT262 = (566, "with kids 10-13 -episode 62")
    EWIT263 = (567, "with kids 10-13 -episode 63")
    EWIT264 = (568, "with kids 10-13 -episode 64")
    EWIT265 = (569, "with kids 10-13 -episode 65")
    EWIT266 = (570, "with kids 10-13 -episode 66")
    EWIT267 = (571, "with kids 10-13 -episode 67")
    EWIT268 = (572, "with kids 10-13 -episode 68")
    EWIT269 = (573, "with kids 10-13 -episode 69")
    EWIT270 = (574, "with kids 10-13 -episode 70")
    EWIT271 = (575, "with kids 10-13 -episode 71")
    EWIT272 = (576, "with kids 10-13 -episode 72")
    EWIT273 = (577, "with kids 10-13 -episode 73")
    EWIT274 = (578, "with kids 10-13 -episode 74")
    EWIT275 = (579, "with kids 10-13 -episode 75")
    EWIT276 = (580, "with kids 10-13 -episode 76")
    EWIT277 = (581, "with kids 10-13 -episode 77")
    EWIT278 = (582, "with kids 10-13 -episode 78")
    EWIT279 = (583, "with kids 10-13 -episode 79")
    EWIT280 = (584, "with kids 10-13 -episode 80")
    EWIT281 = (585, "with kids 10-13 -episode 81")
    EWIT282 = (586, "with kids 10-13 -episode 82")
    EWIT283 = (587, "with kids 10-13 -episode 83")
    EWIT284 = (588, "with kids 10-13 -episode 84")
    EWIT285 = (589, "with kids 10-13 -episode 85")
    EWIT286 = (590, "with kids 10-13 -episode 86")
    EWIT287 = (591, "with kids 10-13 -episode 87")
    EWIT288 = (592, "with kids 10-13 -episode 88")
    EWIT289 = (593, "with kids 10-13 -episode 89")
    EWIT290 = (594, "with kids 10-13 -episode 90")
    EWIT291 = (595, "with kids 10-13 -episode 91")
    EWIT292 = (596, "with kids 10-13 -episode 92")
    EWIT293 = (597, "with kids 10-13 -episode 93")
    EWIT294 = (598, "with kids 10-13 -episode 94")
    EWIT295 = (599, "with kids 10-13 -episode 95")
    EWIT296 = (600, "with kids 10-13 -episode 96")
    EWIT297 = (601, "with kids 10-13 -episode 97")
    EWIT298 = (602, "with kids 10-13 -episode 98")
    EWIT299 = (603, "with kids 10-13 -episode 99")
    EWIT31 = (604, "with other household members -episode 1")
    EWIT32 = (605, "with other household members -episode 2")
    EWIT33 = (606, "with other household members -episode 3")
    EWIT34 = (607, "with other household members -episode 4")
    EWIT35 = (608, "with other household members -episode 5")
    EWIT36 = (609, "with other household members -episode 6")
    EWIT37 = (610, "with other household members -episode 7")
    EWIT38 = (611, "with other household members -episode 8")
    EWIT39 = (612, "with other household members -episode 9")
    EWIT310 = (613, "with other household members -episode 10")
    EWIT311 = (614, "with other household members -episode 11")
    EWIT312 = (615, "with other household members -episode 12")
    EWIT313 = (616, "with other household members -episode 13")
    EWIT314 = (617, "with other household members -episode 14")
    EWIT315 = (618, "with other household members -episode 15")
    EWIT316 = (619, "with other household members -episode 16")
    EWIT317 = (620, "with other household members -episode 17")
    EWIT318 = (621, "with other household members -episode 18")
    EWIT319 = (622, "with other household members -episode 19")
    EWIT320 = (623, "with other household members -episode 20")
    EWIT321 = (624, "with other household members -episode 21")
    EWIT322 = (625, "with other household members -episode 22")
    EWIT323 = (626, "with other household members -episode 23")
    EWIT324 = (627, "with other household members -episode 24")
    EWIT325 = (628, "with other household members -episode 25")
    EWIT326 = (629, "with other household members -episode 26")
    EWIT327 = (630, "with other household members -episode 27")
    EWIT328 = (631, "with other household members -episode 28")
    EWIT329 = (632, "with other household members -episode 29")
    EWIT330 = (633, "with other household members -episode 30")
    EWIT331 = (634, "with other household members -episode 31")
    EWIT332 = (635, "with other household members -episode 32")
    EWIT333 = (636, "with other household members -episode 33")
    EWIT334 = (637, "with other household members -episode 34")
    EWIT335 = (638, "with other household members -episode 35")
    EWIT336 = (639, "with other household members -episode 36")
    EWIT337 = (640, "with other household members -episode 37")
    EWIT338 = (641, "with other household members -episode 38")
    EWIT339 = (642, "with other household members -episode 39")
    EWIT340 = (643, "with other household members -episode 40")
    EWIT341 = (644, "with other household members -episode 41")
    EWIT342 = (645, "with other household members -episode 42")
    EWIT343 = (646, "with other household members -episode 43")
    EWIT344 = (647, "with other household members -episode 44")
    EWIT345 = (648, "with other household members -episode 45")
    EWIT346 = (649, "with other household members -episode 46")
    EWIT347 = (650, "with other household members -episode 47")
    EWIT348 = (651, "with other household members -episode 48")
    EWIT349 = (652, "with other household members -episode 49")
    EWIT350 = (653, "with other household members -episode 50")
    EWIT351 = (654, "with other household members -episode 51")
    EWIT352 = (655, "with other household members -episode 52")
    EWIT353 = (656, "with other household members -episode 53")
    EWIT354 = (657, "with other household members -episode 54")
    EWIT355 = (658, "with other household members -episode 55")
    EWIT356 = (659, "with other household members -episode 56")
    EWIT357 = (660, "with other household members -episode 57")
    EWIT358 = (661, "with other household members -episode 58")
    EWIT359 = (662, "with other household members -episode 59")
    EWIT360 = (663, "with other household members -episode 60")
    EWIT361 = (664, "with other household members -episode 61")
    EWIT362 = (665, "with other household members -episode 62")
    EWIT363 = (666, "with other household members -episode 63")
    EWIT364 = (667, "with other household members -episode 64")
    EWIT365 = (668, "with other household members -episode 65")
    EWIT366 = (669, "with other household members -episode 66")
    EWIT367 = (670, "with other household members -episode 67")
    EWIT368 = (671, "with other household members -episode 68")
    EWIT369 = (672, "with other household members -episode 69")
    EWIT370 = (673, "with other household members -episode 70")
    EWIT371 = (674, "with other household members -episode 71")
    EWIT372 = (675, "with other household members -episode 72")
    EWIT373 = (676, "with other household members -episode 73")
    EWIT374 = (677, "with other household members -episode 74")
    EWIT375 = (678, "with other household members -episode 75")
    EWIT376 = (679, "with other household members -episode 76")
    EWIT377 = (680, "with other household members -episode 77")
    EWIT378 = (681, "with other household members -episode 78")
    EWIT379 = (682, "with other household members -episode 79")
    EWIT380 = (683, "with other household members -episode 80")
    EWIT381 = (684, "with other household members -episode 81")
    EWIT382 = (685, "with other household members -episode 82")
    EWIT383 = (686, "with other household members -episode 83")
    EWIT384 = (687, "with other household members -episode 84")
    EWIT385 = (688, "with other household members -episode 85")
    EWIT386 = (689, "with other household members -episode 86")
    EWIT387 = (690, "with other household members -episode 87")
    EWIT388 = (691, "with other household members -episode 88")
    EWIT389 = (692, "with other household members -episode 89")
    EWIT390 = (693, "with other household members -episode 90")
    EWIT391 = (694, "with other household members -episode 91")
    EWIT392 = (695, "with other household members -episode 92")
    EWIT393 = (696, "with other household members -episode 93")
    EWIT394 = (697, "with other household members -episode 94")
    EWIT395 = (698, "with other household members -episode 95")
    EWIT396 = (699, "with other household members -episode 96")
    EWIT397 = (700, "with other household members -episode 97")
    EWIT398 = (701, "with other household members -episode 98")
    EWIT399 = (702, "with other household members -episode 99")
    EWIT41 = (703, "with other persons known -episode 1")
    EWIT42 = (704, "with other persons known -episode 2")
    EWIT43 = (705, "with other persons known -episode 3")
    EWIT44 = (706, "with other persons known -episode 4")
    EWIT45 = (707, "with other persons known -episode 5")
    EWIT46 = (708, "with other persons known -episode 6")
    EWIT47 = (709, "with other persons known -episode 7")
    EWIT48 = (710, "with other persons known -episode 8")
    EWIT49 = (711, "with other persons known -episode 9")
    EWIT410 = (712, "with other persons known -episode 10")
    EWIT411 = (713, "with other persons known -episode 11")
    EWIT412 = (714, "with other persons known -episode 12")
    EWIT413 = (715, "with other persons known -episode 13")
    EWIT414 = (716, "with other persons known -episode 14")
    EWIT415 = (717, "with other persons known -episode 15")
    EWIT416 = (718, "with other persons known -episode 16")
    EWIT417 = (719, "with other persons known -episode 17")
    EWIT418 = (720, "with other persons known -episode 18")
    EWIT419 = (721, "with other persons known -episode 19")
    EWIT420 = (722, "with other persons known -episode 20")
    EWIT421 = (723, "with other persons known -episode 21")
    EWIT422 = (724, "with other persons known -episode 22")
    EWIT423 = (725, "with other persons known -episode 23")
    EWIT424 = (726, "with other persons known -episode 24")
    EWIT425 = (727, "with other persons known -episode 25")
    EWIT426 = (728, "with other persons known -episode 26")
    EWIT427 = (729, "with other persons known -episode 27")
    EWIT428 = (730, "with other persons known -episode 28")
    EWIT429 = (731, "with other persons known -episode 29")
    EWIT430 = (732, "with other persons known -episode 30")
    EWIT431 = (733, "with other persons known -episode 31")
    EWIT432 = (734, "with other persons known -episode 32")
    EWIT433 = (735, "with other persons known -episode 33")
    EWIT434 = (736, "with other persons known -episode 34")
    EWIT435 = (737, "with other persons known -episode 35")
    EWIT436 = (738, "with other persons known -episode 36")
    EWIT437 = (739, "with other persons known -episode 37")
    EWIT438 = (740, "with other persons known -episode 38")
    EWIT439 = (741, "with other persons known -episode 39")
    EWIT440 = (742, "with other persons known -episode 40")
    EWIT441 = (743, "with other persons known -episode 41")
    EWIT442 = (744, "with other persons known -episode 42")
    EWIT443 = (745, "with other persons known -episode 43")
    EWIT444 = (746, "with other persons known -episode 44")
    EWIT445 = (747, "with other persons known -episode 45")
    EWIT446 = (748, "with other persons known -episode 46")
    EWIT447 = (749, "with other persons known -episode 47")
    EWIT448 = (750, "with other persons known -episode 48")
    EWIT449 = (751, "with other persons known -episode 49")
    EWIT450 = (752, "with other persons known -episode 50")
    EWIT451 = (753, "with other persons known -episode 51")
    EWIT452 = (754, "with other persons known -episode 52")
    EWIT453 = (755, "with other persons known -episode 53")
    EWIT454 = (756, "with other persons known -episode 54")
    EWIT455 = (757, "with other persons known -episode 55")
    EWIT456 = (758, "with other persons known -episode 56")
    EWIT457 = (759, "with other persons known -episode 57")
    EWIT458 = (760, "with other persons known -episode 58")
    EWIT459 = (761, "with other persons known -episode 59")
    EWIT460 = (762, "with other persons known -episode 60")
    EWIT461 = (763, "with other persons known -episode 61")
    EWIT462 = (764, "with other persons known -episode 62")
    EWIT463 = (765, "with other persons known -episode 63")
    EWIT464 = (766, "with other persons known -episode 64")
    EWIT465 = (767, "with other persons known -episode 65")
    EWIT466 = (768, "with other persons known -episode 66")
    EWIT467 = (769, "with other persons known -episode 67")
    EWIT468 = (770, "with other persons known -episode 68")
    EWIT469 = (771, "with other persons known -episode 69")
    EWIT470 = (772, "with other persons known -episode 70")
    EWIT471 = (773, "with other persons known -episode 71")
    EWIT472 = (774, "with other persons known -episode 72")
    EWIT473 = (775, "with other persons known -episode 73")
    EWIT474 = (776, "with other persons known -episode 74")
    EWIT475 = (777, "with other persons known -episode 75")
    EWIT476 = (778, "with other persons known -episode 76")
    EWIT477 = (779, "with other persons known -episode 77")
    EWIT478 = (780, "with other persons known -episode 78")
    EWIT479 = (781, "with other persons known -episode 79")
    EWIT480 = (782, "with other persons known -episode 80")
    EWIT481 = (783, "with other persons known -episode 81")
    EWIT482 = (784, "with other persons known -episode 82")
    EWIT483 = (785, "with other persons known -episode 83")
    EWIT484 = (786, "with other persons known -episode 84")
    EWIT485 = (787, "with other persons known -episode 85")
    EWIT486 = (788, "with other persons known -episode 86")
    EWIT487 = (789, "with other persons known -episode 87")
    EWIT488 = (790, "with other persons known -episode 88")
    EWIT489 = (791, "with other persons known -episode 89")
    EWIT490 = (792, "with other persons known -episode 90")
    EWIT491 = (793, "with other persons known -episode 91")
    EWIT492 = (794, "with other persons known -episode 92")
    EWIT493 = (795, "with other persons known -episode 93")
    EWIT494 = (796, "with other persons known -episode 94")
    EWIT495 = (797, "with other persons known -episode 95")
    EWIT496 = (798, "with other persons known -episode 96")
    EWIT497 = (799, "with other persons known -episode 97")
    EWIT498 = (800, "with other persons known -episode 98")
    EWIT499 = (801, "with other persons known -episode 99")
    EWIT51 = (802, "at work/study/asleep -episode 1")
    EWIT52 = (803, "at work/study/asleep -episode 2")
    EWIT53 = (804, "at work/study/asleep -episode 3")
    EWIT54 = (805, "at work/study/asleep -episode 4")
    EWIT55 = (806, "at work/study/asleep -episode 5")
    EWIT56 = (807, "at work/study/asleep -episode 6")
    EWIT57 = (808, "at work/study/asleep -episode 7")
    EWIT58 = (809, "at work/study/asleep -episode 8")
    EWIT59 = (810, "at work/study/asleep -episode 9")
    EWIT510 = (811, "at work/study/asleep -episode 10")
    EWIT511 = (812, "at work/study/asleep -episode 11")
    EWIT512 = (813, "at work/study/asleep -episode 12")
    EWIT513 = (814, "at work/study/asleep -episode 13")
    EWIT514 = (815, "at work/study/asleep -episode 14")
    EWIT515 = (816, "at work/study/asleep -episode 15")
    EWIT516 = (817, "at work/study/asleep -episode 16")
    EWIT517 = (818, "at work/study/asleep -episode 17")
    EWIT518 = (819, "at work/study/asleep -episode 18")
    EWIT519 = (820, "at work/study/asleep -episode 19")
    EWIT520 = (821, "at work/study/asleep -episode 20")
    EWIT521 = (822, "at work/study/asleep -episode 21")
    EWIT522 = (823, "at work/study/asleep -episode 22")
    EWIT523 = (824, "at work/study/asleep -episode 23")
    EWIT524 = (825, "at work/study/asleep -episode 24")
    EWIT525 = (826, "at work/study/asleep -episode 25")
    EWIT526 = (827, "at work/study/asleep -episode 26")
    EWIT527 = (828, "at work/study/asleep -episode 27")
    EWIT528 = (829, "at work/study/asleep -episode 28")
    EWIT529 = (830, "at work/study/asleep -episode 29")
    EWIT530 = (831, "at work/study/asleep -episode 30")
    EWIT531 = (832, "at work/study/asleep -episode 31")
    EWIT532 = (833, "at work/study/asleep -episode 32")
    EWIT533 = (834, "at work/study/asleep -episode 33")
    EWIT534 = (835, "at work/study/asleep -episode 34")
    EWIT535 = (836, "at work/study/asleep -episode 35")
    EWIT536 = (837, "at work/study/asleep -episode 36")
    EWIT537 = (838, "at work/study/asleep -episode 37")
    EWIT538 = (839, "at work/study/asleep -episode 38")
    EWIT539 = (840, "at work/study/asleep -episode 39")
    EWIT540 = (841, "at work/study/asleep -episode 40")
    EWIT541 = (842, "at work/study/asleep -episode 41")
    EWIT542 = (843, "at work/study/asleep -episode 42")
    EWIT543 = (844, "at work/study/asleep -episode 43")
    EWIT544 = (845, "at work/study/asleep -episode 44")
    EWIT545 = (846, "at work/study/asleep -episode 45")
    EWIT546 = (847, "at work/study/asleep -episode 46")
    EWIT547 = (848, "at work/study/asleep -episode 47")
    EWIT548 = (849, "at work/study/asleep -episode 48")
    EWIT549 = (850, "at work/study/asleep -episode 49")
    EWIT550 = (851, "at work/study/asleep -episode 50")
    EWIT551 = (852, "at work/study/asleep -episode 51")
    EWIT552 = (853, "at work/study/asleep -episode 52")
    EWIT553 = (854, "at work/study/asleep -episode 53")
    EWIT554 = (855, "at work/study/asleep -episode 54")
    EWIT555 = (856, "at work/study/asleep -episode 55")
    EWIT556 = (857, "at work/study/asleep -episode 56")
    EWIT557 = (858, "at work/study/asleep -episode 57")
    EWIT558 = (859, "at work/study/asleep -episode 58")
    EWIT559 = (860, "at work/study/asleep -episode 59")
    EWIT560 = (861, "at work/study/asleep -episode 60")
    EWIT561 = (862, "at work/study/asleep -episode 61")
    EWIT562 = (863, "at work/study/asleep -episode 62")
    EWIT563 = (864, "at work/study/asleep -episode 63")
    EWIT564 = (865, "at work/study/asleep -episode 64")
    EWIT565 = (866, "at work/study/asleep -episode 65")
    EWIT566 = (867, "at work/study/asleep -episode 66")
    EWIT567 = (868, "at work/study/asleep -episode 67")
    EWIT568 = (869, "at work/study/asleep -episode 68")
    EWIT569 = (870, "at work/study/asleep -episode 69")
    EWIT570 = (871, "at work/study/asleep -episode 70")
    EWIT571 = (872, "at work/study/asleep -episode 71")
    EWIT572 = (873, "at work/study/asleep -episode 72")
    EWIT573 = (874, "at work/study/asleep -episode 73")
    EWIT574 = (875, "at work/study/asleep -episode 74")
    EWIT575 = (876, "at work/study/asleep -episode 75")
    EWIT576 = (877, "at work/study/asleep -episode 76")
    EWIT577 = (878, "at work/study/asleep -episode 77")
    EWIT578 = (879, "at work/study/asleep -episode 78")
    EWIT579 = (880, "at work/study/asleep -episode 79")
    EWIT580 = (881, "at work/study/asleep -episode 80")
    EWIT581 = (882, "at work/study/asleep -episode 81")
    EWIT582 = (883, "at work/study/asleep -episode 82")
    EWIT583 = (884, "at work/study/asleep -episode 83")
    EWIT584 = (885, "at work/study/asleep -episode 84")
    EWIT585 = (886, "at work/study/asleep -episode 85")
    EWIT586 = (887, "at work/study/asleep -episode 86")
    EWIT587 = (888, "at work/study/asleep -episode 87")
    EWIT588 = (889, "at work/study/asleep -episode 88")
    EWIT589 = (890, "at work/study/asleep -episode 89")
    EWIT590 = (891, "at work/study/asleep -episode 90")
    EWIT591 = (892, "at work/study/asleep -episode 91")
    EWIT592 = (893, "at work/study/asleep -episode 92")
    EWIT593 = (894, "at work/study/asleep -episode 93")
    EWIT594 = (895, "at work/study/asleep -episode 94")
    EWIT595 = (896, "at work/study/asleep -episode 95")
    EWIT596 = (897, "at work/study/asleep -episode 96")
    EWIT597 = (898, "at work/study/asleep -episode 97")
    EWIT598 = (899, "at work/study/asleep -episode 98")
    EWIT599 = (900, "at work/study/asleep -episode 99")
    EWIT61 = (901, "no answer for who with -episode 1")
    EWIT62 = (902, "no answer for who with -episode 2")
    EWIT63 = (903, "no answer for who with -episode 3")
    EWIT64 = (904, "no answer for who with -episode 4")
    EWIT65 = (905, "no answer for who with -episode 5")
    EWIT66 = (906, "no answer for who with -episode 6")
    EWIT67 = (907, "no answer for who with -episode 7")
    EWIT68 = (908, "no answer for who with -episode 8")
    EWIT69 = (909, "no answer for who with -episode 9")
    EWIT610 = (910, "no answer for who with -episode 10")
    EWIT611 = (911, "no answer for who with -episode 11")
    EWIT612 = (912, "no answer for who with -episode 12")
    EWIT613 = (913, "no answer for who with -episode 13")
    EWIT614 = (914, "no answer for who with -episode 14")
    EWIT615 = (915, "no answer for who with -episode 15")
    EWIT616 = (916, "no answer for who with -episode 16")
    EWIT617 = (917, "no answer for who with -episode 17")
    EWIT618 = (918, "no answer for who with -episode 18")
    EWIT619 = (919, "no answer for who with -episode 19")
    EWIT620 = (920, "no answer for who with -episode 20")
    EWIT621 = (921, "no answer for who with -episode 21")
    EWIT622 = (922, "no answer for who with -episode 22")
    EWIT623 = (923, "no answer for who with -episode 23")
    EWIT624 = (924, "no answer for who with -episode 24")
    EWIT625 = (925, "no answer for who with -episode 25")
    EWIT626 = (926, "no answer for who with -episode 26")
    EWIT627 = (927, "no answer for who with -episode 27")
    EWIT628 = (928, "no answer for who with -episode 28")
    EWIT629 = (929, "no answer for who with -episode 29")
    EWIT630 = (930, "no answer for who with -episode 30")
    EWIT631 = (931, "no answer for who with -episode 31")
    EWIT632 = (932, "no answer for who with -episode 32")
    EWIT633 = (933, "no answer for who with -episode 33")
    EWIT634 = (934, "no answer for who with -episode 34")
    EWIT635 = (935, "no answer for who with -episode 35")
    EWIT636 = (936, "no answer for who with -episode 36")
    EWIT637 = (937, "no answer for who with -episode 37")
    EWIT638 = (938, "no answer for who with -episode 38")
    EWIT639 = (939, "no answer for who with -episode 39")
    EWIT640 = (940, "no answer for who with -episode 40")
    EWIT641 = (941, "no answer for who with -episode 41")
    EWIT642 = (942, "no answer for who with -episode 42")
    EWIT643 = (943, "no answer for who with -episode 43")
    EWIT644 = (944, "no answer for who with -episode 44")
    EWIT645 = (945, "no answer for who with -episode 45")
    EWIT646 = (946, "no answer for who with -episode 46")
    EWIT647 = (947, "no answer for who with -episode 47")
    EWIT648 = (948, "no answer for who with -episode 48")
    EWIT649 = (949, "no answer for who with -episode 49")
    EWIT650 = (950, "no answer for who with -episode 50")
    EWIT651 = (951, "no answer for who with -episode 51")
    EWIT652 = (952, "no answer for who with -episode 52")
    EWIT653 = (953, "no answer for who with -episode 53")
    EWIT654 = (954, "no answer for who with -episode 54")
    EWIT655 = (955, "no answer for who with -episode 55")
    EWIT656 = (956, "no answer for who with -episode 56")
    EWIT657 = (957, "no answer for who with -episode 57")
    EWIT658 = (958, "no answer for who with -episode 58")
    EWIT659 = (959, "no answer for who with -episode 59")
    EWIT660 = (960, "no answer for who with -episode 60")
    EWIT661 = (961, "no answer for who with -episode 61")
    EWIT662 = (962, "no answer for who with -episode 62")
    EWIT663 = (963, "no answer for who with -episode 63")
    EWIT664 = (964, "no answer for who with -episode 64")
    EWIT665 = (965, "no answer for who with -episode 65")
    EWIT666 = (966, "no answer for who with -episode 66")
    EWIT667 = (967, "no answer for who with -episode 67")
    EWIT668 = (968, "no answer for who with -episode 68")
    EWIT669 = (969, "no answer for who with -episode 69")
    EWIT670 = (970, "no answer for who with -episode 70")
    EWIT671 = (971, "no answer for who with -episode 71")
    EWIT672 = (972, "no answer for who with -episode 72")
    EWIT673 = (973, "no answer for who with -episode 73")
    EWIT674 = (974, "no answer for who with -episode 74")
    EWIT675 = (975, "no answer for who with -episode 75")
    EWIT676 = (976, "no answer for who with -episode 76")
    EWIT677 = (977, "no answer for who with -episode 77")
    EWIT678 = (978, "no answer for who with -episode 78")
    EWIT679 = (979, "no answer for who with -episode 79")
    EWIT680 = (980, "no answer for who with -episode 80")
    EWIT681 = (981, "no answer for who with -episode 81")
    EWIT682 = (982, "no answer for who with -episode 82")
    EWIT683 = (983, "no answer for who with -episode 83")
    EWIT684 = (984, "no answer for who with -episode 84")
    EWIT685 = (985, "no answer for who with -episode 85")
    EWIT686 = (986, "no answer for who with -episode 86")
    EWIT687 = (987, "no answer for who with -episode 87")
    EWIT688 = (988, "no answer for who with -episode 88")
    EWIT689 = (989, "no answer for who with -episode 89")
    EWIT690 = (990, "no answer for who with -episode 90")
    EWIT691 = (991, "no answer for who with -episode 91")
    EWIT692 = (992, "no answer for who with -episode 92")
    EWIT693 = (993, "no answer for who with -episode 93")
    EWIT694 = (994, "no answer for who with -episode 94")
    EWIT695 = (995, "no answer for who with -episode 95")
    EWIT696 = (996, "no answer for who with -episode 96")
    EWIT697 = (997, "no answer for who with -episode 97")
    EWIT698 = (998, "no answer for who with -episode 98")
    EWIT699 = (999, "no answer for who with -episode 99")
    EVST1 = (1000, "start time of episode 1")
    EVST2 = (1001, "start time of episode 2")
    EVST3 = (1002, "start time of episode 3")
    EVST4 = (1003, "start time of episode 4")
    EVST5 = (1004, "start time of episode 5")
    EVST6 = (1005, "start time of episode 6")
    EVST7 = (1006, "start time of episode 7")
    EVST8 = (1007, "start time of episode 8")
    EVST9 = (1008, "start time of episode 9")
    EVST10 = (1009, "start time of episode 10")
    EVST11 = (1010, "start time of episode 11")
    EVST12 = (1011, "start time of episode 12")
    EVST13 = (1012, "start time of episode 13")
    EVST14 = (1013, "start time of episode 14")
    EVST15 = (1014, "start time of episode 15")
    EVST16 = (1015, "start time of episode 16")
    EVST17 = (1016, "start time of episode 17")
    EVST18 = (1017, "start time of episode 18")
    EVST19 = (1018, "start time of episode 19")
    EVST20 = (1019, "start time of episode 20")
    EVST21 = (1020, "start time of episode 21")
    EVST22 = (1021, "start time of episode 22")
    EVST23 = (1022, "start time of episode 23")
    EVST24 = (1023, "start time of episode 24")
    EVST25 = (1024, "start time of episode 25")
    EVST26 = (1025, "start time of episode 26")
    EVST27 = (1026, "start time of episode 27")
    EVST28 = (1027, "start time of episode 28")
    EVST29 = (1028, "start time of episode 29")
    EVST30 = (1029, "start time of episode 30")
    EVST31 = (1030, "start time of episode 31")
    EVST32 = (1031, "start time of episode 32")
    EVST33 = (1032, "start time of episode 33")
    EVST34 = (1033, "start time of episode 34")
    EVST35 = (1034, "start time of episode 35")
    EVST36 = (1035, "start time of episode 36")
    EVST37 = (1036, "start time of episode 37")
    EVST38 = (1037, "start time of episode 38")
    EVST39 = (1038, "start time of episode 39")
    EVST40 = (1039, "start time of episode 40")
    EVST41 = (1040, "start time of episode 41")
    EVST42 = (1041, "start time of episode 42")
    EVST43 = (1042, "start time of episode 43")
    EVST44 = (1043, "start time of episode 44")
    EVST45 = (1044, "start time of episode 45")
    EVST46 = (1045, "start time of episode 46")
    EVST47 = (1046, "start time of episode 47")
    EVST48 = (1047, "start time of episode 48")
    EVST49 = (1048, "start time of episode 49")
    EVST50 = (1049, "start time of episode 50")
    EVST51 = (1050, "start time of episode 51")
    EVST52 = (1051, "start time of episode 52")
    EVST53 = (1052, "start time of episode 53")
    EVST54 = (1053, "start time of episode 54")
    EVST55 = (1054, "start time of episode 55")
    EVST56 = (1055, "start time of episode 56")
    EVST57 = (1056, "start time of episode 57")
    EVST58 = (1057, "start time of episode 58")
    EVST59 = (1058, "start time of episode 59")
    EVST60 = (1059, "start time of episode 60")
    EVST61 = (1060, "start time of episode 61")
    EVST62 = (1061, "start time of episode 62")
    EVST63 = (1062, "start time of episode 63")
    EVST64 = (1063, "start time of episode 64")
    EVST65 = (1064, "start time of episode 65")
    EVST66 = (1065, "start time of episode 66")
    EVST67 = (1066, "start time of episode 67")
    EVST68 = (1067, "start time of episode 68")
    EVST69 = (1068, "start time of episode 69")
    EVST70 = (1069, "start time of episode 70")
    EVST71 = (1070, "start time of episode 71")
    EVST72 = (1071, "start time of episode 72")
    EVST73 = (1072, "start time of episode 73")
    EVST74 = (1073, "start time of episode 74")
    EVST75 = (1074, "start time of episode 75")
    EVST76 = (1075, "start time of episode 76")
    EVST77 = (1076, "start time of episode 77")
    EVST78 = (1077, "start time of episode 78")
    EVST79 = (1078, "start time of episode 79")
    EVST80 = (1079, "start time of episode 80")
    EVST81 = (1080, "start time of episode 81")
    EVST82 = (1081, "start time of episode 82")
    EVST83 = (1082, "start time of episode 83")
    EVST84 = (1083, "start time of episode 84")
    EVST85 = (1084, "start time of episode 85")
    EVST86 = (1085, "start time of episode 86")
    EVST87 = (1086, "start time of episode 87")
    EVST88 = (1087, "start time of episode 88")
    EVST89 = (1088, "start time of episode 89")
    EVST90 = (1089, "start time of episode 90")
    EVST91 = (1090, "start time of episode 91")
    EVST92 = (1091, "start time of episode 92")
    EVST93 = (1092, "start time of episode 93")
    EVST94 = (1093, "start time of episode 94")
    EVST95 = (1094, "start time of episode 95")
    EVST96 = (1095, "start time of episode 96")
    EVST97 = (1096, "start time of episode 97")
    EVST98 = (1097, "start time of episode 98")
    EVST99 = (1098, "start time of episode 99")
    EVND1 = (1099, "end time of episode 1")
    EVND2 = (1100, "end time of episode 2")
    EVND3 = (1101, "end time of episode 3")
    EVND4 = (1102, "end time of episode 4")
    EVND5 = (1103, "end time of episode 5")
    EVND6 = (1104, "end time of episode 6")
    EVND7 = (1105, "end time of episode 7")
    EVND8 = (1106, "end time of episode 8")
    EVND9 = (1107, "end time of episode 9")
    EVND10 = (1108, "end time of episode 10")
    EVND11 = (1109, "end time of episode 11")
    EVND12 = (1110, "end time of episode 12")
    EVND13 = (1111, "end time of episode 13")
    EVND14 = (1112, "end time of episode 14")
    EVND15 = (1113, "end time of episode 15")
    EVND16 = (1114, "end time of episode 16")
    EVND17 = (1115, "end time of episode 17")
    EVND18 = (1116, "end time of episode 18")
    EVND19 = (1117, "end time of episode 19")
    EVND20 = (1118, "end time of episode 20")
    EVND21 = (1119, "end time of episode 21")
    EVND22 = (1120, "end time of episode 22")
    EVND23 = (1121, "end time of episode 23")
    EVND24 = (1122, "end time of episode 24")
    EVND25 = (1123, "end time of episode 25")
    EVND26 = (1124, "end time of episode 26")
    EVND27 = (1125, "end time of episode 27")
    EVND28 = (1126, "end time of episode 28")
    EVND29 = (1127, "end time of episode 29")
    EVND30 = (1128, "end time of episode 30")
    EVND31 = (1129, "end time of episode 31")
    EVND32 = (1130, "end time of episode 32")
    EVND33 = (1131, "end time of episode 33")
    EVND34 = (1132, "end time of episode 34")
    EVND35 = (1133, "end time of episode 35")
    EVND36 = (1134, "end time of episode 36")
    EVND37 = (1135, "end time of episode 37")
    EVND38 = (1136, "end time of episode 38")
    EVND39 = (1137, "end time of episode 39")
    EVND40 = (1138, "end time of episode 40")
    EVND41 = (1139, "end time of episode 41")
    EVND42 = (1140, "end time of episode 42")
    EVND43 = (1141, "end time of episode 43")
    EVND44 = (1142, "end time of episode 44")
    EVND45 = (1143, "end time of episode 45")
    EVND46 = (1144, "end time of episode 46")
    EVND47 = (1145, "end time of episode 47")
    EVND48 = (1146, "end time of episode 48")
    EVND49 = (1147, "end time of episode 49")
    EVND50 = (1148, "end time of episode 50")
    EVND51 = (1149, "end time of episode 51")
    EVND52 = (1150, "end time of episode 52")
    EVND53 = (1151, "end time of episode 53")
    EVND54 = (1152, "end time of episode 54")
    EVND55 = (1153, "end time of episode 55")
    EVND56 = (1154, "end time of episode 56")
    EVND57 = (1155, "end time of episode 57")
    EVND58 = (1156, "end time of episode 58")
    EVND59 = (1157, "end time of episode 59")
    EVND60 = (1158, "end time of episode 60")
    EVND61 = (1159, "end time of episode 61")
    EVND62 = (1160, "end time of episode 62")
    EVND63 = (1161, "end time of episode 63")
    EVND64 = (1162, "end time of episode 64")
    EVND65 = (1163, "end time of episode 65")
    EVND66 = (1164, "end time of episode 66")
    EVND67 = (1165, "end time of episode 67")
    EVND68 = (1166, "end time of episode 68")
    EVND69 = (1167, "end time of episode 69")
    EVND70 = (1168, "end time of episode 70")
    EVND71 = (1169, "end time of episode 71")
    EVND72 = (1170, "end time of episode 72")
    EVND73 = (1171, "end time of episode 73")
    EVND74 = (1172, "end time of episode 74")
    EVND75 = (1173, "end time of episode 75")
    EVND76 = (1174, "end time of episode 76")
    EVND77 = (1175, "end time of episode 77")
    EVND78 = (1176, "end time of episode 78")
    EVND79 = (1177, "end time of episode 79")
    EVND80 = (1178, "end time of episode 80")
    EVND81 = (1179, "end time of episode 81")
    EVND82 = (1180, "end time of episode 82")
    EVND83 = (1181, "end time of episode 83")
    EVND84 = (1182, "end time of episode 84")
    EVND85 = (1183, "end time of episode 85")
    EVND86 = (1184, "end time of episode 86")
    EVND87 = (1185, "end time of episode 87")
    EVND88 = (1186, "end time of episode 88")
    EVND89 = (1187, "end time of episode 89")
    EVND90 = (1188, "end time of episode 90")
    EVND91 = (1189, "end time of episode 91")
    EVND92 = (1190, "end time of episode 92")
    EVND93 = (1191, "end time of episode 93")
    EVND94 = (1192, "end time of episode 94")
    EVND95 = (1193, "end time of episode 95")
    EVND96 = (1194, "end time of episode 96")
    EVND97 = (1195, "end time of episode 97")
    EVND98 = (1196, "end time of episode 98")
    EVND99 = (1197, "end time of episode 99")
    EKID01 = (1198, "alone -episode 1")
    EKID02 = (1199, "alone -episode 2")
    EKID03 = (1200, "alone -episode 3")
    EKID04 = (1201, "alone -episode 4")
    EKID05 = (1202, "alone -episode 5")
    EKID06 = (1203, "alone -episode 6")
    EKID07 = (1204, "alone -episode 7")
    EKID08 = (1205, "alone -episode 8")
    EKID09 = (1206, "alone -episode 9")
    EKID010 = (1207, "alone -episode 10")
    EKID011 = (1208, "alone -episode 11")
    EKID012 = (1209, "alone -episode 12")
    EKID013 = (1210, "alone -episode 13")
    EKID014 = (1211, "alone -episode 14")
    EKID015 = (1212, "alone -episode 15")
    EKID016 = (1213, "alone -episode 16")
    EKID017 = (1214, "alone -episode 17")
    EKID018 = (1215, "alone -episode 18")
    EKID019 = (1216, "alone -episode 19")
    EKID020 = (1217, "alone -episode 20")
    EKID021 = (1218, "alone -episode 21")
    EKID022 = (1219, "alone -episode 22")
    EKID023 = (1220, "alone -episode 23")
    EKID024 = (1221, "alone -episode 24")
    EKID025 = (1222, "alone -episode 25")
    EKID026 = (1223, "alone -episode 26")
    EKID027 = (1224, "alone -episode 27")
    EKID028 = (1225, "alone -episode 28")
    EKID029 = (1226, "alone -episode 29")
    EKID030 = (1227, "alone -episode 30")
    EKID031 = (1228, "alone -episode 31")
    EKID032 = (1229, "alone -episode 32")
    EKID033 = (1230, "alone -episode 33")
    EKID034 = (1231, "alone -episode 34")
    EKID035 = (1232, "alone -episode 35")
    EKID036 = (1233, "alone -episode 36")
    EKID037 = (1234, "alone -episode 37")
    EKID038 = (1235, "alone -episode 38")
    EKID039 = (1236, "alone -episode 39")
    EKID040 = (1237, "alone -episode 40")
    EKID041 = (1238, "alone -episode 41")
    EKID042 = (1239, "alone -episode 42")
    EKID043 = (1240, "alone -episode 43")
    EKID044 = (1241, "alone -episode 44")
    EKID045 = (1242, "alone -episode 45")
    EKID046 = (1243, "alone -episode 46")
    EKID047 = (1244, "alone -episode 47")
    EKID048 = (1245, "alone -episode 48")
    EKID049 = (1246, "alone -episode 49")
    EKID050 = (1247, "alone -episode 50")
    EKID051 = (1248, "alone -episode 51")
    EKID052 = (1249, "alone -episode 52")
    EKID053 = (1250, "alone -episode 53")
    EKID054 = (1251, "alone -episode 54")
    EKID055 = (1252, "alone -episode 55")
    EKID056 = (1253, "alone -episode 56")
    EKID057 = (1254, "alone -episode 57")
    EKID058 = (1255, "alone -episode 58")
    EKID059 = (1256, "alone -episode 59")
    EKID060 = (1257, "alone -episode 60")
    EKID061 = (1258, "alone -episode 61")
    EKID062 = (1259, "alone -episode 62")
    EKID063 = (1260, "alone -episode 63")
    EKID064 = (1261, "alone -episode 64")
    EKID065 = (1262, "alone -episode 65")
    EKID066 = (1263, "alone -episode 66")
    EKID067 = (1264, "alone -episode 67")
    EKID068 = (1265, "alone -episode 68")
    EKID069 = (1266, "alone -episode 69")
    EKID070 = (1267, "alone -episode 70")
    EKID071 = (1268, "alone -episode 71")
    EKID072 = (1269, "alone -episode 72")
    EKID073 = (1270, "alone -episode 73")
    EKID074 = (1271, "alone -episode 74")
    EKID075 = (1272, "alone -episode 75")
    EKID076 = (1273, "alone -episode 76")
    EKID077 = (1274, "alone -episode 77")
    EKID078 = (1275, "alone -episode 78")
    EKID079 = (1276, "alone -episode 79")
    EKID080 = (1277, "alone -episode 80")
    EKID081 = (1278, "alone -episode 81")
    EKID082 = (1279, "alone -episode 82")
    EKID083 = (1280, "alone -episode 83")
    EKID084 = (1281, "alone -episode 84")
    EKID085 = (1282, "alone -episode 85")
    EKID086 = (1283, "alone -episode 86")
    EKID087 = (1284, "alone -episode 87")
    EKID088 = (1285, "alone -episode 88")
    EKID089 = (1286, "alone -episode 89")
    EKID090 = (1287, "alone -episode 90")
    EKID091 = (1288, "alone -episode 91")
    EKID092 = (1289, "alone -episode 92")
    EKID093 = (1290, "alone -episode 93")
    EKID094 = (1291, "alone -episode 94")
    EKID095 = (1292, "alone -episode 95")
    EKID096 = (1293, "alone -episode 96")
    EKID097 = (1294, "alone -episode 97")
    EKID098 = (1295, "alone -episode 98")
    EKID099 = (1296, "alone -episode 99")
    EKID11 = (1297, "with parents -episode 1")
    EKID12 = (1298, "with parents -episode 2")
    EKID13 = (1299, "with parents -episode 3")
    EKID14 = (1300, "with parents -episode 4")
    EKID15 = (1301, "with parents -episode 5")
    EKID16 = (1302, "with parents -episode 6")
    EKID17 = (1303, "with parents -episode 7")
    EKID18 = (1304, "with parents -episode 8")
    EKID19 = (1305, "with parents -episode 9")
    EKID110 = (1306, "with parents -episode 10")
    EKID111 = (1307, "with parents -episode 11")
    EKID112 = (1308, "with parents -episode 12")
    EKID113 = (1309, "with parents -episode 13")
    EKID114 = (1310, "with parents -episode 14")
    EKID115 = (1311, "with parents -episode 15")
    EKID116 = (1312, "with parents -episode 16")
    EKID117 = (1313, "with parents -episode 17")
    EKID118 = (1314, "with parents -episode 18")
    EKID119 = (1315, "with parents -episode 19")
    EKID120 = (1316, "with parents -episode 20")
    EKID121 = (1317, "with parents -episode 21")
    EKID122 = (1318, "with parents -episode 22")
    EKID123 = (1319, "with parents -episode 23")
    EKID124 = (1320, "with parents -episode 24")
    EKID125 = (1321, "with parents -episode 25")
    EKID126 = (1322, "with parents -episode 26")
    EKID127 = (1323, "with parents -episode 27")
    EKID128 = (1324, "with parents -episode 28")
    EKID129 = (1325, "with parents -episode 29")
    EKID130 = (1326, "with parents -episode 30")
    EKID131 = (1327, "with parents -episode 31")
    EKID132 = (1328, "with parents -episode 32")
    EKID133 = (1329, "with parents -episode 33")
    EKID134 = (1330, "with parents -episode 34")
    EKID135 = (1331, "with parents -episode 35")
    EKID136 = (1332, "with parents -episode 36")
    EKID137 = (1333, "with parents -episode 37")
    EKID138 = (1334, "with parents -episode 38")
    EKID139 = (1335, "with parents -episode 39")
    EKID140 = (1336, "with parents -episode 40")
    EKID141 = (1337, "with parents -episode 41")
    EKID142 = (1338, "with parents -episode 42")
    EKID143 = (1339, "with parents -episode 43")
    EKID144 = (1340, "with parents -episode 44")
    EKID145 = (1341, "with parents -episode 45")
    EKID146 = (1342, "with parents -episode 46")
    EKID147 = (1343, "with parents -episode 47")
    EKID148 = (1344, "with parents -episode 48")
    EKID149 = (1345, "with parents -episode 49")
    EKID150 = (1346, "with parents -episode 50")
    EKID151 = (1347, "with parents -episode 51")
    EKID152 = (1348, "with parents -episode 52")
    EKID153 = (1349, "with parents -episode 53")
    EKID154 = (1350, "with parents -episode 54")
    EKID155 = (1351, "with parents -episode 55")
    EKID156 = (1352, "with parents -episode 56")
    EKID157 = (1353, "with parents -episode 57")
    EKID158 = (1354, "with parents -episode 58")
    EKID159 = (1355, "with parents -episode 59")
    EKID160 = (1356, "with parents -episode 60")
    EKID161 = (1357, "with parents -episode 61")
    EKID162 = (1358, "with parents -episode 62")
    EKID163 = (1359, "with parents -episode 63")
    EKID164 = (1360, "with parents -episode 64")
    EKID165 = (1361, "with parents -episode 65")
    EKID166 = (1362, "with parents -episode 66")
    EKID167 = (1363, "with parents -episode 67")
    EKID168 = (1364, "with parents -episode 68")
    EKID169 = (1365, "with parents -episode 69")
    EKID170 = (1366, "with parents -episode 70")
    EKID171 = (1367, "with parents -episode 71")
    EKID172 = (1368, "with parents -episode 72")
    EKID173 = (1369, "with parents -episode 73")
    EKID174 = (1370, "with parents -episode 74")
    EKID175 = (1371, "with parents -episode 75")
    EKID176 = (1372, "with parents -episode 76")
    EKID177 = (1373, "with parents -episode 77")
    EKID178 = (1374, "with parents -episode 78")
    EKID179 = (1375, "with parents -episode 79")
    EKID180 = (1376, "with parents -episode 80")
    EKID181 = (1377, "with parents -episode 81")
    EKID182 = (1378, "with parents -episode 82")
    EKID183 = (1379, "with parents -episode 83")
    EKID184 = (1380, "with parents -episode 84")
    EKID185 = (1381, "with parents -episode 85")
    EKID186 = (1382, "with parents -episode 86")
    EKID187 = (1383, "with parents -episode 87")
    EKID188 = (1384, "with parents -episode 88")
    EKID189 = (1385, "with parents -episode 89")
    EKID190 = (1386, "with parents -episode 90")
    EKID191 = (1387, "with parents -episode 91")
    EKID192 = (1388, "with parents -episode 92")
    EKID193 = (1389, "with parents -episode 93")
    EKID194 = (1390, "with parents -episode 94")
    EKID195 = (1391, "with parents -episode 95")
    EKID196 = (1392, "with parents -episode 96")
    EKID197 = (1393, "with parents -episode 97")
    EKID198 = (1394, "with parents -episode 98")
    EKID199 = (1395, "with parents -episode 99")
    EKID21 = (1396, "with other household members -episode 1")
    EKID22 = (1397, "with other household members -episode 2")
    EKID23 = (1398, "with other household members -episode 3")
    EKID24 = (1399, "with other household members -episode 4")
    EKID25 = (1400, "with other household members -episode 5")
    EKID26 = (1401, "with other household members -episode 6")
    EKID27 = (1402, "with other household members -episode 7")
    EKID28 = (1403, "with other household members -episode 8")
    EKID29 = (1404, "with other household members -episode 9")
    EKID210 = (1405, "with other household members -episode 10")
    EKID211 = (1406, "with other household members -episode 11")
    EKID212 = (1407, "with other household members -episode 12")
    EKID213 = (1408, "with other household members -episode 13")
    EKID214 = (1409, "with other household members -episode 14")
    EKID215 = (1410, "with other household members -episode 15")
    EKID216 = (1411, "with other household members -episode 16")
    EKID217 = (1412, "with other household members -episode 17")
    EKID218 = (1413, "with other household members -episode 18")
    EKID219 = (1414, "with other household members -episode 19")
    EKID220 = (1415, "with other household members -episode 20")
    EKID221 = (1416, "with other household members -episode 21")
    EKID222 = (1417, "with other household members -episode 22")
    EKID223 = (1418, "with other household members -episode 23")
    EKID224 = (1419, "with other household members -episode 24")
    EKID225 = (1420, "with other household members -episode 25")
    EKID226 = (1421, "with other household members -episode 26")
    EKID227 = (1422, "with other household members -episode 27")
    EKID228 = (1423, "with other household members -episode 28")
    EKID229 = (1424, "with other household members -episode 29")
    EKID230 = (1425, "with other household members -episode 30")
    EKID231 = (1426, "with other household members -episode 31")
    EKID232 = (1427, "with other household members -episode 32")
    EKID233 = (1428, "with other household members -episode 33")
    EKID234 = (1429, "with other household members -episode 34")
    EKID235 = (1430, "with other household members -episode 35")
    EKID236 = (1431, "with other household members -episode 36")
    EKID237 = (1432, "with other household members -episode 37")
    EKID238 = (1433, "with other household members -episode 38")
    EKID239 = (1434, "with other household members -episode 39")
    EKID240 = (1435, "with other household members -episode 40")
    EKID241 = (1436, "with other household members -episode 41")
    EKID242 = (1437, "with other household members -episode 42")
    EKID243 = (1438, "with other household members -episode 43")
    EKID244 = (1439, "with other household members -episode 44")
    EKID245 = (1440, "with other household members -episode 45")
    EKID246 = (1441, "with other household members -episode 46")
    EKID247 = (1442, "with other household members -episode 47")
    EKID248 = (1443, "with other household members -episode 48")
    EKID249 = (1444, "with other household members -episode 49")
    EKID250 = (1445, "with other household members -episode 50")
    EKID251 = (1446, "with other household members -episode 51")
    EKID252 = (1447, "with other household members -episode 52")
    EKID253 = (1448, "with other household members -episode 53")
    EKID254 = (1449, "with other household members -episode 54")
    EKID255 = (1450, "with other household members -episode 55")
    EKID256 = (1451, "with other household members -episode 56")
    EKID257 = (1452, "with other household members -episode 57")
    EKID258 = (1453, "with other household members -episode 58")
    EKID259 = (1454, "with other household members -episode 59")
    EKID260 = (1455, "with other household members -episode 60")
    EKID261 = (1456, "with other household members -episode 61")
    EKID262 = (1457, "with other household members -episode 62")
    EKID263 = (1458, "with other household members -episode 63")
    EKID264 = (1459, "with other household members -episode 64")
    EKID265 = (1460, "with other household members -episode 65")
    EKID266 = (1461, "with other household members -episode 66")
    EKID267 = (1462, "with other household members -episode 67")
    EKID268 = (1463, "with other household members -episode 68")
    EKID269 = (1464, "with other household members -episode 69")
    EKID270 = (1465, "with other household members -episode 70")
    EKID271 = (1466, "with other household members -episode 71")
    EKID272 = (1467, "with other household members -episode 72")
    EKID273 = (1468, "with other household members -episode 73")
    EKID274 = (1469, "with other household members -episode 74")
    EKID275 = (1470, "with other household members -episode 75")
    EKID276 = (1471, "with other household members -episode 76")
    EKID277 = (1472, "with other household members -episode 77")
    EKID278 = (1473, "with other household members -episode 78")
    EKID279 = (1474, "with other household members -episode 79")
    EKID280 = (1475, "with other household members -episode 80")
    EKID281 = (1476, "with other household members -episode 81")
    EKID282 = (1477, "with other household members -episode 82")
    EKID283 = (1478, "with other household members -episode 83")
    EKID284 = (1479, "with other household members -episode 84")
    EKID285 = (1480, "with other household members -episode 85")
    EKID286 = (1481, "with other household members -episode 86")
    EKID287 = (1482, "with other household members -episode 87")
    EKID288 = (1483, "with other household members -episode 88")
    EKID289 = (1484, "with other household members -episode 89")
    EKID290 = (1485, "with other household members -episode 90")
    EKID291 = (1486, "with other household members -episode 91")
    EKID292 = (1487, "with other household members -episode 92")
    EKID293 = (1488, "with other household members -episode 93")
    EKID294 = (1489, "with other household members -episode 94")
    EKID295 = (1490, "with other household members -episode 95")
    EKID296 = (1491, "with other household members -episode 96")
    EKID297 = (1492, "with other household members -episode 97")
    EKID298 = (1493, "with other household members -episode 98")
    EKID299 = (1494, "with other household members -episode 99")
    EKID31 = (1495, "with other people they know -episode 1")
    EKID32 = (1496, "with other people they know -episode 2")
    EKID33 = (1497, "with other people they know -episode 3")
    EKID34 = (1498, "with other people they know -episode 4")
    EKID35 = (1499, "with other people they know -episode 5")
    EKID36 = (1500, "with other people they know -episode 6")
    EKID37 = (1501, "with other people they know -episode 7")
    EKID38 = (1502, "with other people they know -episode 8")
    EKID39 = (1503, "with other people they know -episode 9")
    EKID310 = (1504, "with other people they know -episode 10")
    EKID311 = (1505, "with other people they know -episode 11")
    EKID312 = (1506, "with other people they know -episode 12")
    EKID313 = (1507, "with other people they know -episode 13")
    EKID314 = (1508, "with other people they know -episode 14")
    EKID315 = (1509, "with other people they know -episode 15")
    EKID316 = (1510, "with other people they know -episode 16")
    EKID317 = (1511, "with other people they know -episode 17")
    EKID318 = (1512, "with other people they know -episode 18")
    EKID319 = (1513, "with other people they know -episode 19")
    EKID320 = (1514, "with other people they know -episode 20")
    EKID321 = (1515, "with other people they know -episode 21")
    EKID322 = (1516, "with other people they know -episode 22")
    EKID323 = (1517, "with other people they know -episode 23")
    EKID324 = (1518, "with other people they know -episode 24")
    EKID325 = (1519, "with other people they know -episode 25")
    EKID326 = (1520, "with other people they know -episode 26")
    EKID327 = (1521, "with other people they know -episode 27")
    EKID328 = (1522, "with other people they know -episode 28")
    EKID329 = (1523, "with other people they know -episode 29")
    EKID330 = (1524, "with other people they know -episode 30")
    EKID331 = (1525, "with other people they know -episode 31")
    EKID332 = (1526, "with other people they know -episode 32")
    EKID333 = (1527, "with other people they know -episode 33")
    EKID334 = (1528, "with other people they know -episode 34")
    EKID335 = (1529, "with other people they know -episode 35")
    EKID336 = (1530, "with other people they know -episode 36")
    EKID337 = (1531, "with other people they know -episode 37")
    EKID338 = (1532, "with other people they know -episode 38")
    EKID339 = (1533, "with other people they know -episode 39")
    EKID340 = (1534, "with other people they know -episode 40")
    EKID341 = (1535, "with other people they know -episode 41")
    EKID342 = (1536, "with other people they know -episode 42")
    EKID343 = (1537, "with other people they know -episode 43")
    EKID344 = (1538, "with other people they know -episode 44")
    EKID345 = (1539, "with other people they know -episode 45")
    EKID346 = (1540, "with other people they know -episode 46")
    EKID347 = (1541, "with other people they know -episode 47")
    EKID348 = (1542, "with other people they know -episode 48")
    EKID349 = (1543, "with other people they know -episode 49")
    EKID350 = (1544, "with other people they know -episode 50")
    EKID351 = (1545, "with other people they know -episode 51")
    EKID352 = (1546, "with other people they know -episode 52")
    EKID353 = (1547, "with other people they know -episode 53")
    EKID354 = (1548, "with other people they know -episode 54")
    EKID355 = (1549, "with other people they know -episode 55")
    EKID356 = (1550, "with other people they know -episode 56")
    EKID357 = (1551, "with other people they know -episode 57")
    EKID358 = (1552, "with other people they know -episode 58")
    EKID359 = (1553, "with other people they know -episode 59")
    EKID360 = (1554, "with other people they know -episode 60")
    EKID361 = (1555, "with other people they know -episode 61")
    EKID362 = (1556, "with other people they know -episode 62")
    EKID363 = (1557, "with other people they know -episode 63")
    EKID364 = (1558, "with other people they know -episode 64")
    EKID365 = (1559, "with other people they know -episode 65")
    EKID366 = (1560, "with other people they know -episode 66")
    EKID367 = (1561, "with other people they know -episode 67")
    EKID368 = (1562, "with other people they know -episode 68")
    EKID369 = (1563, "with other people they know -episode 69")
    EKID370 = (1564, "with other people they know -episode 70")
    EKID371 = (1565, "with other people they know -episode 71")
    EKID372 = (1566, "with other people they know -episode 72")
    EKID373 = (1567, "with other people they know -episode 73")
    EKID374 = (1568, "with other people they know -episode 74")
    EKID375 = (1569, "with other people they know -episode 75")
    EKID376 = (1570, "with other people they know -episode 76")
    EKID377 = (1571, "with other people they know -episode 77")
    EKID378 = (1572, "with other people they know -episode 78")
    EKID379 = (1573, "with other people they know -episode 79")
    EKID380 = (1574, "with other people they know -episode 80")
    EKID381 = (1575, "with other people they know -episode 81")
    EKID382 = (1576, "with other people they know -episode 82")
    EKID383 = (1577, "with other people they know -episode 83")
    EKID384 = (1578, "with other people they know -episode 84")
    EKID385 = (1579, "with other people they know -episode 85")
    EKID386 = (1580, "with other people they know -episode 86")
    EKID387 = (1581, "with other people they know -episode 87")
    EKID388 = (1582, "with other people they know -episode 88")
    EKID389 = (1583, "with other people they know -episode 89")
    EKID390 = (1584, "with other people they know -episode 90")
    EKID391 = (1585, "with other people they know -episode 91")
    EKID392 = (1586, "with other people they know -episode 92")
    EKID393 = (1587, "with other people they know -episode 93")
    EKID394 = (1588, "with other people they know -episode 94")
    EKID395 = (1589, "with other people they know -episode 95")
    EKID396 = (1590, "with other people they know -episode 96")
    EKID397 = (1591, "with other people they know -episode 97")
    EKID398 = (1592, "with other people they know -episode 98")
    EKID399 = (1593, "with other people they know -episode 99")
    EKID41 = (1594, "at work/study/asleep -episode 1")
    EKID42 = (1595, "at work/study/asleep -episode 2")
    EKID43 = (1596, "at work/study/asleep -episode 3")
    EKID44 = (1597, "at work/study/asleep -episode 4")
    EKID45 = (1598, "at work/study/asleep -episode 5")
    EKID46 = (1599, "at work/study/asleep -episode 6")
    EKID47 = (1600, "at work/study/asleep -episode 7")
    EKID48 = (1601, "at work/study/asleep -episode 8")
    EKID49 = (1602, "at work/study/asleep -episode 9")
    EKID410 = (1603, "at work/study/asleep -episode 10")
    EKID411 = (1604, "at work/study/asleep -episode 11")
    EKID412 = (1605, "at work/study/asleep -episode 12")
    EKID413 = (1606, "at work/study/asleep -episode 13")
    EKID414 = (1607, "at work/study/asleep -episode 14")
    EKID415 = (1608, "at work/study/asleep -episode 15")
    EKID416 = (1609, "at work/study/asleep -episode 16")
    EKID417 = (1610, "at work/study/asleep -episode 17")
    EKID418 = (1611, "at work/study/asleep -episode 18")
    EKID419 = (1612, "at work/study/asleep -episode 19")
    EKID420 = (1613, "at work/study/asleep -episode 20")
    EKID421 = (1614, "at work/study/asleep -episode 21")
    EKID422 = (1615, "at work/study/asleep -episode 22")
    EKID423 = (1616, "at work/study/asleep -episode 23")
    EKID424 = (1617, "at work/study/asleep -episode 24")
    EKID425 = (1618, "at work/study/asleep -episode 25")
    EKID426 = (1619, "at work/study/asleep -episode 26")
    EKID427 = (1620, "at work/study/asleep -episode 27")
    EKID428 = (1621, "at work/study/asleep -episode 28")
    EKID429 = (1622, "at work/study/asleep -episode 29")
    EKID430 = (1623, "at work/study/asleep -episode 30")
    EKID431 = (1624, "at work/study/asleep -episode 31")
    EKID432 = (1625, "at work/study/asleep -episode 32")
    EKID433 = (1626, "at work/study/asleep -episode 33")
    EKID434 = (1627, "at work/study/asleep -episode 34")
    EKID435 = (1628, "at work/study/asleep -episode 35")
    EKID436 = (1629, "at work/study/asleep -episode 36")
    EKID437 = (1630, "at work/study/asleep -episode 37")
    EKID438 = (1631, "at work/study/asleep -episode 38")
    EKID439 = (1632, "at work/study/asleep -episode 39")
    EKID440 = (1633, "at work/study/asleep -episode 40")
    EKID441 = (1634, "at work/study/asleep -episode 41")
    EKID442 = (1635, "at work/study/asleep -episode 42")
    EKID443 = (1636, "at work/study/asleep -episode 43")
    EKID444 = (1637, "at work/study/asleep -episode 44")
    EKID445 = (1638, "at work/study/asleep -episode 45")
    EKID446 = (1639, "at work/study/asleep -episode 46")
    EKID447 = (1640, "at work/study/asleep -episode 47")
    EKID448 = (1641, "at work/study/asleep -episode 48")
    EKID449 = (1642, "at work/study/asleep -episode 49")
    EKID450 = (1643, "at work/study/asleep -episode 50")
    EKID451 = (1644, "at work/study/asleep -episode 51")
    EKID452 = (1645, "at work/study/asleep -episode 52")
    EKID453 = (1646, "at work/study/asleep -episode 53")
    EKID454 = (1647, "at work/study/asleep -episode 54")
    EKID455 = (1648, "at work/study/asleep -episode 55")
    EKID456 = (1649, "at work/study/asleep -episode 56")
    EKID457 = (1650, "at work/study/asleep -episode 57")
    EKID458 = (1651, "at work/study/asleep -episode 58")
    EKID459 = (1652, "at work/study/asleep -episode 59")
    EKID460 = (1653, "at work/study/asleep -episode 60")
    EKID461 = (1654, "at work/study/asleep -episode 61")
    EKID462 = (1655, "at work/study/asleep -episode 62")
    EKID463 = (1656, "at work/study/asleep -episode 63")
    EKID464 = (1657, "at work/study/asleep -episode 64")
    EKID465 = (1658, "at work/study/asleep -episode 65")
    EKID466 = (1659, "at work/study/asleep -episode 66")
    EKID467 = (1660, "at work/study/asleep -episode 67")
    EKID468 = (1661, "at work/study/asleep -episode 68")
    EKID469 = (1662, "at work/study/asleep -episode 69")
    EKID470 = (1663, "at work/study/asleep -episode 70")
    EKID471 = (1664, "at work/study/asleep -episode 71")
    EKID472 = (1665, "at work/study/asleep -episode 72")
    EKID473 = (1666, "at work/study/asleep -episode 73")
    EKID474 = (1667, "at work/study/asleep -episode 74")
    EKID475 = (1668, "at work/study/asleep -episode 75")
    EKID476 = (1669, "at work/study/asleep -episode 76")
    EKID477 = (1670, "at work/study/asleep -episode 77")
    EKID478 = (1671, "at work/study/asleep -episode 78")
    EKID479 = (1672, "at work/study/asleep -episode 79")
    EKID480 = (1673, "at work/study/asleep -episode 80")
    EKID481 = (1674, "at work/study/asleep -episode 81")
    EKID482 = (1675, "at work/study/asleep -episode 82")
    EKID483 = (1676, "at work/study/asleep -episode 83")
    EKID484 = (1677, "at work/study/asleep -episode 84")
    EKID485 = (1678, "at work/study/asleep -episode 85")
    EKID486 = (1679, "at work/study/asleep -episode 86")
    EKID487 = (1680, "at work/study/asleep -episode 87")
    EKID488 = (1681, "at work/study/asleep -episode 88")
    EKID489 = (1682, "at work/study/asleep -episode 89")
    EKID490 = (1683, "at work/study/asleep -episode 90")
    EKID491 = (1684, "at work/study/asleep -episode 91")
    EKID492 = (1685, "at work/study/asleep -episode 92")
    EKID493 = (1686, "at work/study/asleep -episode 93")
    EKID494 = (1687, "at work/study/asleep -episode 94")
    EKID495 = (1688, "at work/study/asleep -episode 95")
    EKID496 = (1689, "at work/study/asleep -episode 96")
    EKID497 = (1690, "at work/study/asleep -episode 97")
    EKID498 = (1691, "at work/study/asleep -episode 98")
    EKID499 = (1692, "at work/study/asleep -episode 99")
    EKID51 = (1693, "no answer -episode 1")
    EKID52 = (1694, "no answer -episode 2")
    EKID53 = (1695, "no answer -episode 3")
    EKID54 = (1696, "no answer -episode 4")
    EKID55 = (1697, "no answer -episode 5")
    EKID56 = (1698, "no answer -episode 6")
    EKID57 = (1699, "no answer -episode 7")
    EKID58 = (1700, "no answer -episode 8")
    EKID59 = (1701, "no answer -episode 9")
    EKID510 = (1702, "no answer -episode 10")
    EKID511 = (1703, "no answer -episode 11")
    EKID512 = (1704, "no answer -episode 12")
    EKID513 = (1705, "no answer -episode 13")
    EKID514 = (1706, "no answer -episode 14")
    EKID515 = (1707, "no answer -episode 15")
    EKID516 = (1708, "no answer -episode 16")
    EKID517 = (1709, "no answer -episode 17")
    EKID518 = (1710, "no answer -episode 18")
    EKID519 = (1711, "no answer -episode 19")
    EKID520 = (1712, "no answer -episode 20")
    EKID521 = (1713, "no answer -episode 21")
    EKID522 = (1714, "no answer -episode 22")
    EKID523 = (1715, "no answer -episode 23")
    EKID524 = (1716, "no answer -episode 24")
    EKID525 = (1717, "no answer -episode 25")
    EKID526 = (1718, "no answer -episode 26")
    EKID527 = (1719, "no answer -episode 27")
    EKID528 = (1720, "no answer -episode 28")
    EKID529 = (1721, "no answer -episode 29")
    EKID530 = (1722, "no answer -episode 30")
    EKID531 = (1723, "no answer -episode 31")
    EKID532 = (1724, "no answer -episode 32")
    EKID533 = (1725, "no answer -episode 33")
    EKID534 = (1726, "no answer -episode 34")
    EKID535 = (1727, "no answer -episode 35")
    EKID536 = (1728, "no answer -episode 36")
    EKID537 = (1729, "no answer -episode 37")
    EKID538 = (1730, "no answer -episode 38")
    EKID539 = (1731, "no answer -episode 39")
    EKID540 = (1732, "no answer -episode 40")
    EKID541 = (1733, "no answer -episode 41")
    EKID542 = (1734, "no answer -episode 42")
    EKID543 = (1735, "no answer -episode 43")
    EKID544 = (1736, "no answer -episode 44")
    EKID545 = (1737, "no answer -episode 45")
    EKID546 = (1738, "no answer -episode 46")
    EKID547 = (1739, "no answer -episode 47")
    EKID548 = (1740, "no answer -episode 48")
    EKID549 = (1741, "no answer -episode 49")
    EKID550 = (1742, "no answer -episode 50")
    EKID551 = (1743, "no answer -episode 51")
    EKID552 = (1744, "no answer -episode 52")
    EKID553 = (1745, "no answer -episode 53")
    EKID554 = (1746, "no answer -episode 54")
    EKID555 = (1747, "no answer -episode 55")
    EKID556 = (1748, "no answer -episode 56")
    EKID557 = (1749, "no answer -episode 57")
    EKID558 = (1750, "no answer -episode 58")
    EKID559 = (1751, "no answer -episode 59")
    EKID560 = (1752, "no answer -episode 60")
    EKID561 = (1753, "no answer -episode 61")
    EKID562 = (1754, "no answer -episode 62")
    EKID563 = (1755, "no answer -episode 63")
    EKID564 = (1756, "no answer -episode 64")
    EKID565 = (1757, "no answer -episode 65")
    EKID566 = (1758, "no answer -episode 66")
    EKID567 = (1759, "no answer -episode 67")
    EKID568 = (1760, "no answer -episode 68")
    EKID569 = (1761, "no answer -episode 69")
    EKID570 = (1762, "no answer -episode 70")
    EKID571 = (1763, "no answer -episode 71")
    EKID572 = (1764, "no answer -episode 72")
    EKID573 = (1765, "no answer -episode 73")
    EKID574 = (1766, "no answer -episode 74")
    EKID575 = (1767, "no answer -episode 75")
    EKID576 = (1768, "no answer -episode 76")
    EKID577 = (1769, "no answer -episode 77")
    EKID578 = (1770, "no answer -episode 78")
    EKID579 = (1771, "no answer -episode 79")
    EKID580 = (1772, "no answer -episode 80")
    EKID581 = (1773, "no answer -episode 81")
    EKID582 = (1774, "no answer -episode 82")
    EKID583 = (1775, "no answer -episode 83")
    EKID584 = (1776, "no answer -episode 84")
    EKID585 = (1777, "no answer -episode 85")
    EKID586 = (1778, "no answer -episode 86")
    EKID587 = (1779, "no answer -episode 87")
    EKID588 = (1780, "no answer -episode 88")
    EKID589 = (1781, "no answer -episode 89")
    EKID590 = (1782, "no answer -episode 90")
    EKID591 = (1783, "no answer -episode 91")
    EKID592 = (1784, "no answer -episode 92")
    EKID593 = (1785, "no answer -episode 93")
    EKID594 = (1786, "no answer -episode 94")
    EKID595 = (1787, "no answer -episode 95")
    EKID596 = (1788, "no answer -episode 96")
    EKID597 = (1789, "no answer -episode 97")
    EKID598 = (1790, "no answer -episode 98")
    EKID599 = (1791, "no answer -episode 99")
    DAGE = (1792, "Diary Age")
    DAGEGRP = (1793, "Age group")
    DSEX = (1794, "Diary-sex")
    DETHNIC = (1795, "Diary-ethnicity")
    DDAYW = (1796, "Diary day - Weekday, Saturday or Sunday")
    DDAYW2 = (1797, "Diary day - weekday or weekend")
    HDAY = (1798, "Day of household interview")
    HMONTH = (1799, "Month of household interview")
    HYEAR = (1800, "Year of household interview")
    GORPAF = (1801, "Government Office Region")
    GORPAF2 = (1802, "Govn Office Region - 8 categories")
    GORPAF3 = (1803, "Govn Office Region - 4 countries")
    POP_DEN = (1804, "Population density (persons per 10 hectares - uses 1991 Census data for postcode sector)")
    POP_DEN2 = (1805, "Population density - banded (persons per 10 hectares)")
    UNEMP = (1806, "Unemployment rate (%) - uses 1991 Census data for postcode sector")
    UNEMP2 = (1807, "Unemployment rate - percentage banded")
    HNUMB = (1808, "Number of people in household (all ages)")
    NUMADULT = (1809, "Number of adults   (16 yrs or more) in hhld")
    NUMCHILD = (1810, "Number of children (15 yrs or less) in hhld")
    CHILD = (1811, "Whether child (15yrs or less) in household or not")
    AGEYNGST = (1812, "Age of youngest person in household")
    NUM0_2 = (1813, "Number aged 0 - 2 yrs in hhld")
    NUM3_4 = (1814, "Number aged 3 - 4 yrs in hhld")
    NUM5_9 = (1815, "Number aged 5 - 9 yrs in hhld")
    NUM10_15 = (1816, "Number aged 10 - 15 yrs in hhld")
    NUM16_17 = (1817, "Number aged 16 - 17yrs")
    HRP_PER = (1818, "Household Reference Person - person number")
    SPOUSE1 = (1819, "For hhlds with one marr/cohab couple - person number of FIRST spouse")
    SPOUSE2 = (1820, "For hhlds with one marr/cohab couple - person number of SECOND spouse")
    TENURE2 = (1821, "Tenure - grouped")
    CARAVAIL = (1822, "Whether household owns/ has continuous use of car, motor bike or other motor vehicle")
    GROSHINC = (1823, "Household Income band (gross ie before deductions) - per year (source: hhld qstn 10b)")
    HHTYPE4 = (1824, "Household type - main variable for hhld type (16 categories)")
    HHTYPE5 = (1825, "Household type - 8 categories")
    MANAGE2 = (1826, "Management responsibilities (of economically active & employed)")
    ECONACT = (1827, "Economic activity")
    ECONACT3 = (1828, "Economic activity - 3")
    EMPINCBD = (1829, "Employee - Net MONTHLY income - Banded (sources: Q10 & Q11a)")
    SEINCBD = (1830, "Self-employed - Net MONTHLY income - Banded (sources: Q13c & Q13d)")
    TOTPINC = (1831, "Total net monthly personal income (for employees & self-employed together)")
    HRS_UNPD = (1832, "Total weekly hours UNPAID work in own/ relatives's business (copy of Q14a)")
    HRS_JOB1 = (1833, "Total weekly hours usually worked in MAIN job (incl paid & unpaid overtime) by people in paid work (employed or self-employed)")
    HRS_JOB2 = (1834, "Total weekly hours usually worked in SECOND job (copy of Q16F)")
    HRS_TOT = (1835, "Total hours usually worked per week: unpaid work for own/rel business + main job + second job combined")
    HRS_GRP = (1836, "Total weekly hours usually worked - paid work (main + 2nd job) or unpaid work - banded")
    SIC = (1837, "Standard Industrial Classification 1992 (4-digit) - for respondent's MAIN JOB")
    SOC = (1838, "Standard Occupational Classification 2000 for respondent's MAIN JOB")
    SIC2 = (1839, "Standard Industrial Classification 1992 (4-digit) - for respondent's SECOND JOB")
    SOC2 = (1840, "Standard Occupational Classification 2000 for respondent's SECOND JOB")
    NSSECB = (1841, "National Statistics Socio-Economic Classification")
    NSSECB_8 = (1842, "NS Socio-Economic Classification - 8 classes")
    NSSECB_5 = (1843, "NS Socio-Economic Classification - 5 classes")
    NSSECB_3 = (1844, "NS Socio-Economic Classification - 3 classes")
    HIQUAL4 = (1845, "Highest qualification gained - HARMONISED DEFINITION")
    AGELEFT = (1846, " Age left full-time education - grouped")
    LIVARR = (1847, "Living arrangements (as reported by respondent at q55 & q56 - NOT based on relationships in hhld grid )")
    PROVCARE = (1848, "Q45 & Q47: Do you look after any sick/ disabled/ elderly person (either living with you or not living with you)?")
    MGROUP = (1849, "(H) GB MOSAIC Group (area classification) - household level")
    MTYPE = (1850, "(H) GB MOSAIC Type - household level")
    MGRPPC = (1851, "(PC) GB MOSAIC Group - post code level")
    MTYPEPC = (1852, "(PC) GB MOSAIC Type - post code level")
    ISBA = (1853, "ISBA - Code")
    CINEMA = (1854, "distance to nearest cinema")
    THEATRE = (1855, "distance to nearest theatre")
    SPORT = (1856, "distance to nearest sports centre")
    SHOPPING = (1857, "distance to nearest shopping centre")
    GROCERY = (1858, "distance to nearest grocery shop")
    SCHOOL = (1859, "distance to nearest school")
    TOT_EPIS = (1860, "Total number of episodes (excluding 'not spec' activities 996 & 997)")
    MISSTIME = (1861, "Missing main activity (codes 996 & 997) - minutes per day")
    DRY_IND = (1862, "Suitability of diaries for analysis - indicator field")
    WTDRY_GR = (1863, "Diary weight - for grossing to UK population aged 8yrs or more")
    WTDRY_UG = (1864, "Diary weight - ungrossed")


class DTYPE(OrderedEnum):
    CHILD_DIARY = '0'
    ADULT_DIARY = '1'
    ADULTS_WHO_COMPLETED_A_CHILD_DIARY = '2'


class DMONTH(OrderedEnum):
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
    MONTH_MISSING = '99'


class DDAYOFWK(OrderedEnum):
    MONDAY = '1'
    TUESDAY = '2'
    WEDNESDAY = '3'
    THURSDAY = '4'
    FRIDAY = '5'
    SATURDAY = '6'
    SUNDAY = '7'


class EVACT1(OrderedEnum):
    UNSPECIFIED_PERSONAL_CARE = '0'
    UNSPECIFIED_SLEEP = '10'
    SLEEP = '110'
    SICK_IN_BED = '120'
    EATING = '210'
    UNSPECIFIED_OTHER_PERSONAL_CARE = '300'
    WASH_AND_DRESS = '310'
    OTHER_SPECIFIED_PERSONAL_CARE = '390'
    UNSPECIFIED_EMPLOYMENT = '1000'
    WORKING_TIME_IN_MAIN_JOB = '1110'
    COFFEE_AND_OTHER_BREAKS_IN_MAIN_JOB = '1120'
    WORKING_TIME_IN_SECOND_JOB = '1210'
    COFFEE_AND_OTHER_BREAKS_IN_SECOND_JOB = '1220'
    UNSPECIFIED_ACTIVITIES_RELATED_TO_EMPLOYMENT = '1300'
    LUNCH_BREAK = '1310'
    OTHER_SPECIFIED_ACTIVITIES_RELATED_TO_EMPLOYMENT = '1390'
    ACTIVITIES_RELATED_TO_JOB_SEEKING = '1391'
    OTHER_SPECIFIED_ACTIVITIES_RELATED_TO_EMPLOYMENT2 = '1399'
    UNSPECIFIED_STUDY = '2000'
    UNSPECIFIED_ACTIVITIES_RELATED_TO_SCHOOL_OR_UNIVERSITY = '2100'
    CLASSES_AND_LECTURES = '2110'
    HOMEWORK = '2120'
    OTHER_SPECIFIED_ACTIVITIES_RELATED_TO_SCHOOL_OR_UNIVERSITY = '2190'
    FREE_TIME_STUDY = '2210'
    UNSPECIFIED_HOUSEHOLD_AND_FAMILY_CARE = '3000'
    UNSPECIFIED_FOOD_MANAGEMENT = '3100'
    FOOD_PREPARATION = '3110'
    BAKING = '3120'
    DISH_WASHING = '3130'
    PRESERVING = '3140'
    OTHER_SPECIFIED_FOOD_MANAGEMENT = '3190'
    UNSPECIFIED_HOUSEHOLD_UPKEEP = '3200'
    CLEANING_DWELLING = '3210'
    CLEANING_YARD = '3220'
    HEATING_AND_WATER = '3230'
    VARIOUS_ARRANGEMENTS = '3240'
    DISPOSAL_OF_WASTE = '3250'
    OTHER_SPECIFIED_HOUSEHOLD_UPKEEP = '3290'
    UNSPECIFIED_MAKING_AND_CARE_FOR_TEXTILES = '3300'
    LAUNDRY = '3310'
    IRONING = '3320'
    HANDICRAFT_AND_PRODUCING_TEXTILES = '3330'
    OTHER_SPECIFIED_MAKING_AND_CARE_FOR_TEXTILES = '3390'
    UNSPECIFIED_GARDENING_AND_PET_CARE = '3400'
    GARDENING = '3410'
    TENDING_DOMESTIC_ANIMALS = '3420'
    CARING_FOR_PETS = '3430'
    WALKING_THE_DOG = '3440'
    OTHER_SPECIFIED_GARDENING_AND_PET_CARE = '3490'
    UNSPECIFIED_CONSTRUCTION_AND_REPAIRS = '3500'
    HOUSE_CONSTRUCTION_AND_RENOVATION = '3510'
    REPAIRS_OF_DWELLING = '3520'
    UNSPECIFIED_MAKING__REPAIRING_AND_MAINTAINING_EQUIPMENT = '3530'
    WOODCRAFT__METAL_CRAFT__SCULPTURE_AND_POTTERY = '3531'
    OTHER_SPECIFIED_MAKING__REPAIRING_AND_MAINTAINING_EQUIPMENT = '3539'
    VEHICLE_MAINTENANCE = '3540'
    OTHER_SPECIFIED_CONSTRUCTION_AND_REPAIRS = '3590'
    UNSPECIFIED_SHOPPING_AND_SERVICES = '3600'
    UNSPECIFIED_SHOPPING = '3610'
    SHOPPING_MAINLY_FOR_FOOD = '3611'
    SHOPPING_MAINLY_FOR_CLOTHING = '3612'
    SHOPPING_MAINLY_RELATED_TO_ACCOMMODATION = '3613'
    SHOPPING_OR_BROWSING_AT_CAR_BOOT_SALES_OR_ANTIQUE_FAIRS = '3614'
    WINDOW_SHOPPING_OR_OTHER_SHOPPING_AS_LEISURE = '3615'
    OTHER_SPECIFIED_SHOPPING = '3619'
    COMMERCIAL_AND_ADMINISTRATIVE_SERVICES = '3620'
    PERSONAL_SERVICES = '3630'
    OTHER_SPECIFIED_SHOPPING_AND_SERVICES = '3690'
    HOUSEHOLD_MANAGEMENT_NOT_USING_THE_INTERNET = '3710'
    UNSPECIFIED_HOUSEHOLD_MANAGEMENT_USING_THE_INTERNET = '3720'
    SHPING_FORANDORDRING_UNSPEC_GDSANDSRVS_VIA_INTERNET = '3721'
    SHPING_FORANDORDRING_FOOD_VIA_THE_INTERNET = '3722'
    SHPING_FORANDORDRING_CLOTHING_VIA_THE_INTERNET = '3723'
    SHPING_FORANDORDRING_GDSANDSRV_RELATED_TO_ACC_VIA_INTERNET = '3724'
    SHPING_FORANDORDRING_MASS_MEDIA_VIA_THE_INTERNET = '3725'
    SHPING_FORANDORDRING_ENTERTAINMENT_VIA_THE_INTERNET = '3726'
    BANKING_AND_BILL_PAYING_VIA_THE_INTERNET = '3727'
    OTHER_SPECIFIED_HOUSEHOLD_MANAGEMENT_USING_THE_INTERNET = '3729'
    UNSPECIFIED_CHILDCARE = '3800'
    UNSPECIFIED_PHYSICAL_CARE_AND_SUPERVISION_OF_A_CHILD = '3810'
    FEEDING_THE_CHILD = '3811'
    OTHER_SPECIFIED_PHYSICAL_CARE_AND_SUPERVISION_OF_A_CHILD = '3819'
    TEACHING_THE_CHILD = '3820'
    READING__PLAYING_AND_TALKING_WITH_CHILD = '3830'
    ACCOMPANYING_CHILD = '3840'
    OTHER_SPECIFIED_CHILDCARE = '3890'
    UNSPECIFIED_HELP_TO_AN_ADULT_HOUSEHOLD_MEMBER = '3910'
    PHYSICAL_CARE_AND_SUPERVISION_OF_AN_ADULT_HOUSEHOLD_MEMBER = '3911'
    ACCOMPANYING_AN_ADULT_HOUSEHOLD_MEMBER = '3914'
    OTHER_SPECIFIED_HELP_TO_AN_ADULT_HOUSEHOLD_MEMBER = '3919'
    UNSPECIFIED_VOLUNTEER_WORK_AND_MEETINGS = '4000'
    UNSPECIFIED_ORGANISATIONAL_WORK = '4100'
    WORK_FOR_AN_ORGANISATION = '4110'
    VOLUNTEER_WORK_THROUGH_AN_ORGANISATION = '4120'
    OTHER_SPECIFIED_ORGANISATIONAL_WORK = '4190'
    UNSPECIFIED_INFORMAL_HELP = '4200'
    FOOD_MANAGEMENT_AS_HELP = '4210'
    HOUSEHOLD_UPKEEP_AS_HELP = '4220'
    GARDENING_AND_PET_CARE_AS_HELP = '4230'
    CONSTRUCTION_AND_REPAIRS_AS_HELP = '4240'
    SHOPPING_AND_SERVICES_AS_HELP = '4250'
    HELP_IN_EMPLOYMENT_AND_FARMING = '4260'
    UNSPECIFIED_CHILDCARE_AS_HELP = '4270'
    PHYSICAL_CARE_AND_SUPERVISION_OF_A_CHILD_AS_HELP = '4271'
    TEACHING_THE_CHILD_AS_HELP = '4272'
    READING__PLAYING_AND_TALKING_TO_THE_CHILD_AS_HELP = '4273'
    ACCOMPANYING_THE_CHILD_AS_HELP = '4274'
    OTHER_SPECIFIED_CHILDCARE_AS_HELP = '4279'
    UNSPECIFIED_HELP_TO_AN_ADULT_MEMBER_OF_ANOTHER_HOUSEHOLD = '4280'
    PHYSICAL_CARE_AND_SUPERVISION_OF_AN_ADULT_AS_HELP = '4281'
    ACCOMPANYING_AN_ADULT_AS_HELP = '4284'
    OTHER_SPECIFIED_HELP_TO_AN_ADULT_MEMBER_OF_ANOTHER_HOUSEHOLD = '4289'
    OTHER_SPECIFIED_INFORMAL_HELP = '4290'
    UNSPECIFIED_PARTICIPATORY_ACTIVITIES = '4300'
    MEETINGS = '4310'
    RELIGIOUS_ACTIVITIES = '4320'
    OTHER_SPECIFIED_PARTICIPATORY_ACTIVITIES = '4390'
    UNSPECIFIED_SOCIAL_LIFE_AND_ENTERTAINMENT = '5000'
    UNSPECIFIED_SOCIAL_LIFE = '5100'
    SOCIALISING_WITH_HOUSEHOLD_MEMBERS = '5110'
    VISITING_AND_RECEIVING_VISITORS = '5120'
    FEASTS = '5130'
    TELEPHONE_CONVERSATION = '5140'
    OTHER_SPECIFIED_SOCIAL_LIFE = '5190'
    UNSPECIFIED_ENTERTAINMENT_AND_CULTURE = '5200'
    CINEMA = '5210'
    UNSPECIFIED_THEATRE_OR_CONCERTS = '5220'
    PLAYS__MUSICALS_OR_PANTOMIMES = '5221'
    OPERA__OPERETTA_OR_LIGHT_OPERA = '5222'
    CONCERTS_OR_OTHER_PERFORMANCES_OF_CLASSICAL_MUSIC = '5223'
    LIVE_MUSIC_OTHER_THAN_CLASSICAL_CONCERTS__OPERA_AND_MUSICALS = '5224'
    DANCE_PERFORMANCES = '5225'
    OTHER_SPECIFIED_THEATRE_OR_CONCERTS = '5229'
    ART_EXHIBITIONS_AND_MUSEUMS = '5230'
    UNSPECIFIED_LIBRARY = '5240'
    BRWING_BKS_RCDS_AUDIO_VIDEO_CDS_VDS_FROM_LIBRARY = '5241'
    REFERENCE_TO_BKS_AND_OTHER_LIBRARY_MATERIALS_WITHIN_LIBRARY = '5242'
    USING_INTERNET_IN_THE_LIBRARY = '5243'
    USING_COMPUTERS_IN_THE_LIBRARY_OTHER_THAN_INTERNET_USE = '5244'
    READING_NEWSPAPERS_IN_A_LIBRARY = '5245'
    LISTENING_TO_MUSIC_IN_A_LIBRARY = '5246'
    OTHER_SPECIFIED_LIBRARY_ACTIVITIES = '5249'
    SPORTS_EVENTS = '5250'
    OTHER_SPECIFIED_ENTERTAINMENT_AND_CULTURE = '5290'
    VISITING_A_HISTORICAL_SITE = '5291'
    VISITING_A_WILDLIFE_SITE = '5292'
    VISITING_A_BOTANICAL_SITE = '5293'
    VISITING_A_LEISURE_PARK = '5294'
    VISITING_AN_URBAN_PARK__PLAYGROUND_OR_DESIGNATED_PLAY_AREA = '5295'
    OTHER_SPECIFIED_ENTERTAINMENT_OR_CULTURE = '5299'
    RESTING_TIME_OUT = '5310'
    UNSPECIFIED_SPORTS_AND_OUTDOOR_ACTIVITIES = '6000'
    UNSPECIFIED_PHYSICAL_EXERCISE = '6100'
    WALKING_AND_HIKING = '6110'
    TAKING_A_WALK_OR_HIKE_THAT_LASTS_AT_LEAST_2_MILES_OR_1_HOUR = '6111'
    OTHER_WALK_OR_HIKE = '6119'
    JOGGING_AND_RUNNING = '6120'
    BIKING__SKIING_AND_SKATING = '6130'
    BIKING = '6131'
    SKIING_OR_SKATING = '6132'
    UNSPECIFIED_BALL_GAMES = '6140'
    INDOOR_PAIRS_OR_DOUBLES_GAMES = '6141'
    INDOOR_TEAM_GAMES = '6142'
    OUTDOOR_PAIRS_OR_DOUBLES_GAMES = '6143'
    OUTDOOR_TEAM_GAMES = '6144'
    OTHER_SPECIFIED_BALL_GAMES = '6149'
    GYMNASTICS = '6150'
    FITNESS = '6160'
    UNSPECIFIED_WATER_SPORTS = '6170'
    SWIMMING = '6171'
    OTHER_SPECIFIED_WATER_SPORTS = '6179'
    OTHER_SPECIFIED_PHYSICAL_EXERCISE = '6190'
    UNSPECIFIED_PRODUCTIVE_EXERCISE = '6200'
    HUNTING_AND_FISHING = '6210'
    PICKING_BERRIES__MUSHROOM_AND_HERBS = '6220'
    OTHER_SPECIFIED_PRODUCTIVE_EXERCISE = '6290'
    UNSPECIFIED_SPORTS_RELATED_ACTIVITIES = '6310'
    ACTIVITIES_RELATED_TO_SPORTS = '6311'
    ACTIVITIES_RELATED_TO_PRODUCTIVE_EXERCISE = '6312'
    UNSPECIFIED_HOBBIES_AND_GAMES = '7000'
    UNSPECIFIED_ARTS = '7100'
    UNSPECIFIED_VISUAL_ARTS = '7110'
    PAINTING__DRAWING_OR_OTHER_GRAPHIC_ARTS = '7111'
    MAKING_VIDEOS__TAKING_PHOTOS_OR_RELATED_ACTIVITIES = '7112'
    OTHER_SPECIFIED_VISUAL_ARTS = '7119'
    UNSPECIFIED_PERFORMING_ARTS = '7120'
    SINGING_OR_OTHER_MUSICAL_ACTIVITIES = '7121'
    OTHER_SPECIFIED_PERFORMING_ARTS = '7129'
    LITERARY_ARTS = '7130'
    OTHER_SPECIFIED_ARTS = '7190'
    UNSPECIFIED_HOBBIES = '7200'
    COLLECTING = '7210'
    COMPUTING_PROGRAMMING = '7220'
    UNSPECIFIED_INFORMATION_BY_COMPUTING = '7230'
    INFORMATION_SEARCHING_ON_THE_INTERNET = '7231'
    OTHER_SPECIFIED_INFORMATION_BY_COMPUTING = '7239'
    UNSPECIFIED_COMMUNICATION_BY_COMPUTER = '7240'
    COMMUNICATION_ON_THE_INTERNET = '7241'
    OTHER_SPECIFIED_COMMUNICATION_BY_COMPUTING = '7249'
    UNSPECIFIED_OTHER_COMPUTING = '7250'
    UNSPECIFIED_INTERNET_USE = '7251'
    OTHER_SPECIFIED_COMPUTING = '7259'
    CORRESPONDENCE = '7260'
    OTHER_SPECIFIED_HOBBIES = '7290'
    UNSPECIFIED_GAMES = '7300'
    SOLO_GAMES_AND_PLAY = '7310'
    UNSPECIFIED_GAMES_AND_PLAY_WITH_OTHERS = '7320'
    BILLIARDS__POOL__SNOOKER_OR_PETANQUE = '7321'
    CHESS_AND_BRIDGE = '7322'
    OTHER_SPECIFIED_PARLOUR_GAMES_AND_PLAY = '7329'
    COMPUTER_GAMES = '7330'
    GAMBLING = '7340'
    OTHER_SPECIFIED_GAMES = '7390'
    UNSPECIFIED_MASS_MEDIA = '8000'
    UNSPECIFIED_READING = '8100'
    READING_PERIODICALS = '8110'
    READING_BOOKS = '8120'
    OTHER_SPECIFIED_READING = '8190'
    UNSPECIFIED_TV_WATCHING = '8210'
    WATCHING_A_FILM_ON_TV = '8211'
    WATCHING_SPORT_ON_TV = '8212'
    OTHER_SPECIFIED_TV_WATCHING = '8219'
    UNSPECIFIED_VIDEO_WATCHING = '8220'
    WATCHING_A_FILM_ON_VIDEO = '8221'
    WATCHING_SPORT_ON_VIDEO = '8222'
    OTHER_SPECIFIED_VIDEO_WATCHING = '8229'
    UNSPECIFIED_LISTENING_TO_RADIO_AND_MUSIC = '8300'
    UNSPECIFIED_RADIO_LISTENING = '8310'
    LISTENING_TO_MUSIC_ON_THE_RADIO = '8311'
    LISTENING_TO_SPORT_ON_THE_RADIO = '8312'
    OTHER_SPECIFIED_RADIO_LISTENING = '8319'
    LISTENING_TO_RECORDINGS = '8320'
    TRAVEL_RELATED_TO_UNSPECIFIED_TIME_USE = '9000'
    TRAVEL_RELATED_TO_PERSONAL_BUSINESS = '9010'
    TRAVEL_IN_THE_COURSE_OF_WORK = '9110'
    TRAVEL_TO_WORK_FROM_HOME_AND_BACK_ONLY = '9130'
    TRAVEL_TO_WORK_FROM_A_PLACE_OTHER_THAN_HOME = '9140'
    TRAVEL_RELATED_TO_EDUCATION = '9210'
    TRAVEL_ESCORTING_TO_FROM_EDUCATION = '9230'
    TRAVEL_RELATED_TO_HOUSEHOLD_CARE = '9310'
    TRAVEL_RELATED_TO_SHOPPING = '9360'
    TRAVEL_RELATED_TO_SERVICES = '9370'
    TRAVEL_ESCORTING_A_CHILD_OTHER_THAN_EDUCATION = '9380'
    TRAVEL_ESCORTING_AN_ADULT_OTHER_THAN_EDUCATION = '9390'
    TRAVEL_RELATED_TO_ORGANISATIONAL_WORK = '9410'
    TRAVEL_RELATED_TO_INFORMAL_HELP_TO_OTHER_HOUSEHOLDS = '9420'
    TRAVEL_RELATED_TO_RELIGIOUS_ACTIVITIES = '9430'
    TRAVEL_RLT_TO_PARTICIPATORY_ACTV_EXCEPT_REL_ACTV = '9440'
    TRAVEL_TO_VISIT_FRIENDS_RELATIVES_IN_THEIR_HOMES = '9500'
    TRAVEL_RELATED_TO_OTHER_SOCIAL_ACTIVITIES = '9510'
    TRAVEL_RELATED_TO_ENTERTAINMENT_AND_CULTURE = '9520'
    TRAVEL_RELATED_TO_PHYSICAL_EXERCISE = '9610'
    TRAVEL_RELATED_TO_HUNTING_AND_FISHING = '9620'
    TRAVEL_RELATED_TO_PRODUCTIVE_EXCS_EXPT_HUNTING_AND_FISHING = '9630'
    TRAVEL_RELATED_TO_GAMBLING = '9710'
    TRAVEL_RELATED_TO_HOBBIES_OTHER_THAN_GAMBLING = '9720'
    TRAVEL_TO_HOLIDAY_BASE = '9810'
    TRAVEL_FOR_DAY_TRIP_JUST_WALK = '9820'
    OTHER_SPECIFIED_TRAVEL = '9890'
    PUNCTUATING_ACTIVITY = '9940'
    FILLING_IN_THE_TIME_USE_DIARY = '9950'
    NO_MAIN_ACTIVITY__NO_IDEA_WHAT_IT_MIGHT_BE = '9960'
    NO_MAIN_ACTIVITY__SOME_IDEA_WHAT_IT_MIGHT_BE = '9970'
    ILLEGIBLE_ACTIVITY = '9980'
    UNSPECIFIED_TIME_USE = '9990'
    MISSING1 = '-1'


EVACT2 = EVACT1


EVACT3 = EVACT1


EVACT4 = EVACT1


EVACT5 = EVACT1


EVACT6 = EVACT1


EVACT7 = EVACT1


EVACT8 = EVACT1


EVACT9 = EVACT1


EVACT10 = EVACT1


EVACT11 = EVACT1


EVACT12 = EVACT1


EVACT13 = EVACT1


EVACT14 = EVACT1


EVACT15 = EVACT1


EVACT16 = EVACT1


EVACT17 = EVACT1


EVACT18 = EVACT1


EVACT19 = EVACT1


EVACT20 = EVACT1


EVACT21 = EVACT1


EVACT22 = EVACT1


EVACT23 = EVACT1


EVACT24 = EVACT1


EVACT25 = EVACT1


EVACT26 = EVACT1


EVACT27 = EVACT1


EVACT28 = EVACT1


EVACT29 = EVACT1


EVACT30 = EVACT1


EVACT31 = EVACT1


EVACT32 = EVACT1


EVACT33 = EVACT1


EVACT34 = EVACT1


EVACT35 = EVACT1


EVACT36 = EVACT1


EVACT37 = EVACT1


EVACT38 = EVACT1


EVACT39 = EVACT1


EVACT40 = EVACT1


EVACT41 = EVACT1


EVACT42 = EVACT1


EVACT43 = EVACT1


EVACT44 = EVACT1


EVACT45 = EVACT1


EVACT46 = EVACT1


EVACT47 = EVACT1


EVACT48 = EVACT1


EVACT49 = EVACT1


EVACT50 = EVACT1


EVACT51 = EVACT1


EVACT52 = EVACT1


EVACT53 = EVACT1


EVACT54 = EVACT1


EVACT55 = EVACT1


EVACT56 = EVACT1


EVACT57 = EVACT1


EVACT58 = EVACT1


EVACT59 = EVACT1


EVACT60 = EVACT1


EVACT61 = EVACT1


EVACT62 = EVACT1


EVACT63 = EVACT1


EVACT64 = EVACT1


EVACT65 = EVACT1


EVACT66 = EVACT1


EVACT67 = EVACT1


EVACT68 = EVACT1


EVACT69 = EVACT1


EVACT70 = EVACT1


EVACT71 = EVACT1


EVACT72 = EVACT1


EVACT73 = EVACT1


EVACT74 = EVACT1


EVACT75 = EVACT1


EVACT76 = EVACT1


EVACT77 = EVACT1


EVACT78 = EVACT1


EVACT79 = EVACT1


EVACT80 = EVACT1


EVACT81 = EVACT1


EVACT82 = EVACT1


EVACT83 = EVACT1


EVACT84 = EVACT1


EVACT85 = EVACT1


EVACT86 = EVACT1


EVACT87 = EVACT1


EVACT88 = EVACT1


EVACT89 = EVACT1


EVACT90 = EVACT1


EVACT91 = EVACT1


EVACT92 = EVACT1


EVACT93 = EVACT1


EVACT94 = EVACT1


EVACT95 = EVACT1


EVACT96 = EVACT1


EVACT97 = EVACT1


EVACT98 = EVACT1


EVACT99 = EVACT1


class ESACT1(OrderedEnum):
    UNSPECIFIED_PERSONAL_CARE = '0'
    UNSPECIFIED_SLEEP = '10'
    SLEEP = '110'
    SICK_IN_BED = '120'
    EATING = '210'
    UNSPECIFIED_OTHER_PERSONAL_CARE = '300'
    WASH_AND_DRESS = '310'
    OTHER_SPECIFIED_PERSONAL_CARE = '390'
    UNSPECIFIED_EMPLOYMENT = '1000'
    WORKING_TIME_IN_MAIN_JOB = '1110'
    COFFEE_AND_OTHER_BREAKS_IN_MAIN_JOB = '1120'
    WORKING_TIME_IN_SECOND_JOB = '1210'
    COFFEE_AND_OTHER_BREAKS_IN_SECOND_JOB = '1220'
    UNSPECIFIED_ACTIVITIES_RELATED_TO_EMPLOYMENT = '1300'
    LUNCH_BREAK = '1310'
    OTHER_SPECIFIED_ACTIVITIES_RELATED_TO_EMPLOYMENT = '1390'
    ACTIVITIES_RELATED_TO_JOB_SEEKING = '1391'
    OTHER_SPECIFIED_ACTIVITIES_RELATED_TO_EMPLOYMENT2 = '1399'
    UNSPECIFIED_STUDY = '2000'
    UNSPECIFIED_ACTIVITIES_RELATED_TO_SCHOOL_OR_UNIVERSITY = '2100'
    CLASSES_AND_LECTURES = '2110'
    HOMEWORK = '2120'
    OTHER_SPECIFIED_ACTIVITIES_RELATED_TO_SCHOOL_OR_UNIVERSITY = '2190'
    FREE_TIME_STUDY = '2210'
    UNSPECIFIED_HOUSEHOLD_AND_FAMILY_CARE = '3000'
    UNSPECIFIED_FOOD_MANAGEMENT = '3100'
    FOOD_PREPARATION = '3110'
    BAKING = '3120'
    DISH_WASHING = '3130'
    PRESERVING = '3140'
    OTHER_SPECIFIED_FOOD_MANAGEMENT = '3190'
    UNSPECIFIED_HOUSEHOLD_UPKEEP = '3200'
    CLEANING_DWELLING = '3210'
    CLEANING_YARD = '3220'
    HEATING_AND_WATER = '3230'
    VARIOUS_ARRANGEMENTS = '3240'
    DISPOSAL_OF_WASTE = '3250'
    OTHER_SPECIFIED_HOUSEHOLD_UPKEEP = '3290'
    UNSPECIFIED_MAKING_AND_CARE_FOR_TEXTILES = '3300'
    LAUNDRY = '3310'
    IRONING = '3320'
    HANDICRAFT_AND_PRODUCING_TEXTILES = '3330'
    OTHER_SPECIFIED_MAKING_AND_CARE_FOR_TEXTILES = '3390'
    UNSPECIFIED_GARDENING_AND_PET_CARE = '3400'
    GARDENING = '3410'
    TENDING_DOMESTIC_ANIMALS = '3420'
    CARING_FOR_PETS = '3430'
    WALKING_THE_DOG = '3440'
    OTHER_SPECIFIED_GARDENING_AND_PET_CARE = '3490'
    UNSPECIFIED_CONSTRUCTION_AND_REPAIRS = '3500'
    HOUSE_CONSTRUCTION_AND_RENOVATION = '3510'
    REPAIRS_OF_DWELLING = '3520'
    UNSPECIFIED_MAKING__REPAIRING_AND_MAINTAINING_EQUIPMENT = '3530'
    WOODCRAFT__METAL_CRAFT__SCULPTURE_AND_POTTERY = '3531'
    OTHER_SPECIFIED_MAKING__REPAIRING_AND_MAINTAINING_EQUIPMENT = '3539'
    VEHICLE_MAINTENANCE = '3540'
    OTHER_SPECIFIED_CONSTRUCTION_AND_REPAIRS = '3590'
    UNSPECIFIED_SHOPPING_AND_SERVICES = '3600'
    UNSPECIFIED_SHOPPING = '3610'
    SHOPPING_MAINLY_FOR_FOOD = '3611'
    SHOPPING_MAINLY_FOR_CLOTHING = '3612'
    SHOPPING_MAINLY_RELATED_TO_ACCOMMODATION = '3613'
    SHOPPING_OR_BROWSING_AT_CAR_BOOT_SALES_OR_ANTIQUE_FAIRS = '3614'
    WINDOW_SHOPPING_OR_OTHER_SHOPPING_AS_LEISURE = '3615'
    OTHER_SPECIFIED_SHOPPING = '3619'
    COMMERCIAL_AND_ADMINISTRATIVE_SERVICES = '3620'
    PERSONAL_SERVICES = '3630'
    OTHER_SPECIFIED_SHOPPING_AND_SERVICES = '3690'
    HOUSEHOLD_MANAGEMENT_NOT_USING_THE_INTERNET = '3710'
    UNSPECIFIED_HOUSEHOLD_MANAGEMENT_USING_THE_INTERNET = '3720'
    SHPING_FORANDORDRING_UNSPEC_GDSANDSRVS_VIA_INTERNET = '3721'
    SHPING_FORANDORDRING_FOOD_VIA_THE_INTERNET = '3722'
    SHPING_FORANDORDRING_CLOTHING_VIA_THE_INTERNET = '3723'
    SHPING_FORANDORDRING_GDSANDSRV_RELATED_TO_ACC_VIA_INTERNET = '3724'
    SHPING_FORANDORDRING_MASS_MEDIA_VIA_THE_INTERNET = '3725'
    SHPING_FORANDORDRING_ENTERTAINMENT_VIA_THE_INTERNET = '3726'
    BANKING_AND_BILL_PAYING_VIA_THE_INTERNET = '3727'
    OTHER_SPECIFIED_HOUSEHOLD_MANAGEMENT_USING_THE_INTERNET = '3729'
    UNSPECIFIED_CHILDCARE = '3800'
    UNSPECIFIED_PHYSICAL_CARE_AND_SUPERVISION_OF_A_CHILD = '3810'
    FEEDING_THE_CHILD = '3811'
    OTHER_SPECIFIED_PHYSICAL_CARE_AND_SUPERVISION_OF_A_CHILD = '3819'
    TEACHING_THE_CHILD = '3820'
    READING__PLAYING_AND_TALKING_WITH_CHILD = '3830'
    ACCOMPANYING_CHILD = '3840'
    OTHER_SPECIFIED_CHILDCARE = '3890'
    UNSPECIFIED_HELP_TO_AN_ADULT_HOUSEHOLD_MEMBER = '3910'
    PHYSICAL_CARE_AND_SUPERVISION_OF_AN_ADULT_HOUSEHOLD_MEMBER = '3911'
    ACCOMPANYING_AN_ADULT_HOUSEHOLD_MEMBER = '3914'
    OTHER_SPECIFIED_HELP_TO_AN_ADULT_HOUSEHOLD_MEMBER = '3919'
    UNSPECIFIED_VOLUNTEER_WORK_AND_MEETINGS = '4000'
    UNSPECIFIED_ORGANISATIONAL_WORK = '4100'
    WORK_FOR_AN_ORGANISATION = '4110'
    VOLUNTEER_WORK_THROUGH_AN_ORGANISATION = '4120'
    OTHER_SPECIFIED_ORGANISATIONAL_WORK = '4190'
    UNSPECIFIED_INFORMAL_HELP = '4200'
    FOOD_MANAGEMENT_AS_HELP = '4210'
    HOUSEHOLD_UPKEEP_AS_HELP = '4220'
    GARDENING_AND_PET_CARE_AS_HELP = '4230'
    CONSTRUCTION_AND_REPAIRS_AS_HELP = '4240'
    SHOPPING_AND_SERVICES_AS_HELP = '4250'
    HELP_IN_EMPLOYMENT_AND_FARMING = '4260'
    UNSPECIFIED_CHILDCARE_AS_HELP = '4270'
    PHYSICAL_CARE_AND_SUPERVISION_OF_A_CHILD_AS_HELP = '4271'
    TEACHING_THE_CHILD_AS_HELP = '4272'
    READING__PLAYING_AND_TALKING_TO_THE_CHILD_AS_HELP = '4273'
    ACCOMPANYING_THE_CHILD_AS_HELP = '4274'
    OTHER_SPECIFIED_CHILDCARE_AS_HELP = '4279'
    UNSPECIFIED_HELP_TO_AN_ADULT_MEMBER_OF_ANOTHER_HOUSEHOLD = '4280'
    PHYSICAL_CARE_AND_SUPERVISION_OF_AN_ADULT_AS_HELP = '4281'
    ACCOMPANYING_AN_ADULT_AS_HELP = '4284'
    OTHER_SPECIFIED_HELP_TO_AN_ADULT_MEMBER_OF_ANOTHER_HOUSEHOLD = '4289'
    OTHER_SPECIFIED_INFORMAL_HELP = '4290'
    UNSPECIFIED_PARTICIPATORY_ACTIVITIES = '4300'
    MEETINGS = '4310'
    RELIGIOUS_ACTIVITIES = '4320'
    OTHER_SPECIFIED_PARTICIPATORY_ACTIVITIES = '4390'
    UNSPECIFIED_SOCIAL_LIFE_AND_ENTERTAINMENT = '5000'
    UNSPECIFIED_SOCIAL_LIFE = '5100'
    SOCIALISING_WITH_HOUSEHOLD_MEMBERS = '5110'
    VISITING_AND_RECEIVING_VISITORS = '5120'
    FEASTS = '5130'
    TELEPHONE_CONVERSATION = '5140'
    OTHER_SPECIFIED_SOCIAL_LIFE = '5190'
    UNSPECIFIED_ENTERTAINMENT_AND_CULTURE = '5200'
    CINEMA = '5210'
    UNSPECIFIED_THEATRE_OR_CONCERTS = '5220'
    PLAYS__MUSICALS_OR_PANTOMIMES = '5221'
    OPERA__OPERETTA_OR_LIGHT_OPERA = '5222'
    CONCERTS_OR_OTHER_PERFORMANCES_OF_CLASSICAL_MUSIC = '5223'
    LIVE_MUSIC_OTHER_THAN_CLASSICAL_CONCERTS__OPERA_AND_MUSICALS = '5224'
    DANCE_PERFORMANCES = '5225'
    OTHER_SPECIFIED_THEATRE_OR_CONCERTS = '5229'
    ART_EXHIBITIONS_AND_MUSEUMS = '5230'
    UNSPECIFIED_LIBRARY = '5240'
    BRWING_BKS_RCDS_AUDIO_VIDEO_CDS_VDS_FROM_LIBRARY = '5241'
    REFERENCE_TO_BKS_AND_OTHER_LIBRARY_MATERIALS_WITHIN_LIBRARY = '5242'
    USING_INTERNET_IN_THE_LIBRARY = '5243'
    USING_COMPUTERS_IN_THE_LIBRARY_OTHER_THAN_INTERNET_USE = '5244'
    READING_NEWSPAPERS_IN_A_LIBRARY = '5245'
    LISTENING_TO_MUSIC_IN_A_LIBRARY = '5246'
    OTHER_SPECIFIED_LIBRARY_ACTIVITIES = '5249'
    SPORTS_EVENTS = '5250'
    OTHER_SPECIFIED_ENTERTAINMENT_AND_CULTURE = '5290'
    VISITING_A_HISTORICAL_SITE = '5291'
    VISITING_A_WILDLIFE_SITE = '5292'
    VISITING_A_BOTANICAL_SITE = '5293'
    VISITING_A_LEISURE_PARK = '5294'
    VISITING_AN_URBAN_PARK__PLAYGROUND_OR_DESIGNATED_PLAY_AREA = '5295'
    OTHER_SPECIFIED_ENTERTAINMENT_OR_CULTURE = '5299'
    RESTING_TIME_OUT = '5310'
    UNSPECIFIED_SPORTS_AND_OUTDOOR_ACTIVITIES = '6000'
    UNSPECIFIED_PHYSICAL_EXERCISE = '6100'
    WALKING_AND_HIKING = '6110'
    TAKING_A_WALK_OR_HIKE_THAT_LASTS_AT_LEAST_2_MILES_OR_1_HOUR = '6111'
    OTHER_WALK_OR_HIKE = '6119'
    JOGGING_AND_RUNNING = '6120'
    BIKING__SKIING_AND_SKATING = '6130'
    BIKING = '6131'
    SKIING_OR_SKATING = '6132'
    UNSPECIFIED_BALL_GAMES = '6140'
    INDOOR_PAIRS_OR_DOUBLES_GAMES = '6141'
    INDOOR_TEAM_GAMES = '6142'
    OUTDOOR_PAIRS_OR_DOUBLES_GAMES = '6143'
    OUTDOOR_TEAM_GAMES = '6144'
    OTHER_SPECIFIED_BALL_GAMES = '6149'
    GYMNASTICS = '6150'
    FITNESS = '6160'
    UNSPECIFIED_WATER_SPORTS = '6170'
    SWIMMING = '6171'
    OTHER_SPECIFIED_WATER_SPORTS = '6179'
    OTHER_SPECIFIED_PHYSICAL_EXERCISE = '6190'
    UNSPECIFIED_PRODUCTIVE_EXERCISE = '6200'
    HUNTING_AND_FISHING = '6210'
    PICKING_BERRIES__MUSHROOM_AND_HERBS = '6220'
    OTHER_SPECIFIED_PRODUCTIVE_EXERCISE = '6290'
    UNSPECIFIED_SPORTS_RELATED_ACTIVITIES = '6310'
    ACTIVITIES_RELATED_TO_SPORTS = '6311'
    ACTIVITIES_RELATED_TO_PRODUCTIVE_EXERCISE = '6312'
    UNSPECIFIED_HOBBIES_AND_GAMES = '7000'
    UNSPECIFIED_ARTS = '7100'
    UNSPECIFIED_VISUAL_ARTS = '7110'
    PAINTING__DRAWING_OR_OTHER_GRAPHIC_ARTS = '7111'
    MAKING_VIDEOS__TAKING_PHOTOS_OR_RELATED_ACTIVITIES = '7112'
    OTHER_SPECIFIED_VISUAL_ARTS = '7119'
    UNSPECIFIED_PERFORMING_ARTS = '7120'
    SINGING_OR_OTHER_MUSICAL_ACTIVITIES = '7121'
    OTHER_SPECIFIED_PERFORMING_ARTS = '7129'
    LITERARY_ARTS = '7130'
    OTHER_SPECIFIED_ARTS = '7190'
    UNSPECIFIED_HOBBIES = '7200'
    COLLECTING = '7210'
    COMPUTING_PROGRAMMING = '7220'
    UNSPECIFIED_INFORMATION_BY_COMPUTING = '7230'
    INFORMATION_SEARCHING_ON_THE_INTERNET = '7231'
    OTHER_SPECIFIED_INFORMATION_BY_COMPUTING = '7239'
    UNSPECIFIED_COMMUNICATION_BY_COMPUTER = '7240'
    COMMUNICATION_ON_THE_INTERNET = '7241'
    OTHER_SPECIFIED_COMMUNICATION_BY_COMPUTING = '7249'
    UNSPECIFIED_OTHER_COMPUTING = '7250'
    UNSPECIFIED_INTERNET_USE = '7251'
    OTHER_SPECIFIED_COMPUTING = '7259'
    CORRESPONDENCE = '7260'
    OTHER_SPECIFIED_HOBBIES = '7290'
    UNSPECIFIED_GAMES = '7300'
    SOLO_GAMES_AND_PLAY = '7310'
    UNSPECIFIED_GAMES_AND_PLAY_WITH_OTHERS = '7320'
    BILLIARDS__POOL__SNOOKER_OR_PETANQUE = '7321'
    CHESS_AND_BRIDGE = '7322'
    OTHER_SPECIFIED_PARLOUR_GAMES_AND_PLAY = '7329'
    COMPUTER_GAMES = '7330'
    GAMBLING = '7340'
    OTHER_SPECIFIED_GAMES = '7390'
    UNSPECIFIED_MASS_MEDIA = '8000'
    UNSPECIFIED_READING = '8100'
    READING_PERIODICALS = '8110'
    READING_BOOKS = '8120'
    OTHER_SPECIFIED_READING = '8190'
    UNSPECIFIED_TV_WATCHING = '8210'
    WATCHING_A_FILM_ON_TV = '8211'
    WATCHING_SPORT_ON_TV = '8212'
    OTHER_SPECIFIED_TV_WATCHING = '8219'
    UNSPECIFIED_VIDEO_WATCHING = '8220'
    WATCHING_A_FILM_ON_VIDEO = '8221'
    WATCHING_SPORT_ON_VIDEO = '8222'
    OTHER_SPECIFIED_VIDEO_WATCHING = '8229'
    UNSPECIFIED_LISTENING_TO_RADIO_AND_MUSIC = '8300'
    UNSPECIFIED_RADIO_LISTENING = '8310'
    LISTENING_TO_MUSIC_ON_THE_RADIO = '8311'
    LISTENING_TO_SPORT_ON_THE_RADIO = '8312'
    OTHER_SPECIFIED_RADIO_LISTENING = '8319'
    LISTENING_TO_RECORDINGS = '8320'
    TRAVEL_RELATED_TO_UNSPECIFIED_TIME_USE = '9000'
    TRAVEL_RELATED_TO_PERSONAL_BUSINESS = '9010'
    TRAVEL_IN_THE_COURSE_OF_WORK = '9110'
    TRAVEL_TO_WORK_FROM_HOME_AND_BACK_ONLY = '9130'
    TRAVEL_TO_WORK_FROM_A_PLACE_OTHER_THAN_HOME = '9140'
    TRAVEL_RELATED_TO_EDUCATION = '9210'
    TRAVEL_ESCORTING_TO_FROM_EDUCATION = '9230'
    TRAVEL_RELATED_TO_HOUSEHOLD_CARE = '9310'
    TRAVEL_RELATED_TO_SHOPPING = '9360'
    TRAVEL_RELATED_TO_SERVICES = '9370'
    TRAVEL_ESCORTING_A_CHILD_OTHER_THAN_EDUCATION = '9380'
    TRAVEL_ESCORTING_AN_ADULT_OTHER_THAN_EDUCATION = '9390'
    TRAVEL_RELATED_TO_ORGANISATIONAL_WORK = '9410'
    TRAVEL_RELATED_TO_INFORMAL_HELP_TO_OTHER_HOUSEHOLDS = '9420'
    TRAVEL_RELATED_TO_RELIGIOUS_ACTIVITIES = '9430'
    TRAVEL_RLT_TO_PARTICIPATORY_ACTV_EXCEPT_REL_ACTV = '9440'
    TRAVEL_TO_VISIT_FRIENDS_RELATIVES_IN_THEIR_HOMES = '9500'
    TRAVEL_RELATED_TO_OTHER_SOCIAL_ACTIVITIES = '9510'
    TRAVEL_RELATED_TO_ENTERTAINMENT_AND_CULTURE = '9520'
    TRAVEL_RELATED_TO_PHYSICAL_EXERCISE = '9610'
    TRAVEL_RELATED_TO_HUNTING_AND_FISHING = '9620'
    TRAVEL_RELATED_TO_PRODUCTIVE_EXCS_EXPT_HUNTING_AND_FISHING = '9630'
    TRAVEL_RELATED_TO_GAMBLING = '9710'
    TRAVEL_RELATED_TO_HOBBIES_OTHER_THAN_GAMBLING = '9720'
    TRAVEL_TO_HOLIDAY_BASE = '9810'
    TRAVEL_FOR_DAY_TRIP_JUST_WALK = '9820'
    OTHER_SPECIFIED_TRAVEL = '9890'
    PUNCTUATING_ACTIVITY = '9940'
    FILLING_IN_THE_TIME_USE_DIARY = '9950'
    NO_MAIN_ACTIVITY__NO_IDEA_WHAT_IT_MIGHT_BE = '9960'
    NO_MAIN_ACTIVITY__SOME_IDEA_WHAT_IT_MIGHT_BE = '9970'
    ILLEGIBLE_ACTIVITY = '9980'
    UNSPECIFIED_TIME_USE = '9990'
    MISSING1 = '-1'
    MISSING2 = '-2'
    MISSING3 = '-9'


ESACT2 = ESACT1


ESACT3 = ESACT1


ESACT4 = ESACT1


ESACT5 = ESACT1


ESACT6 = ESACT1


ESACT7 = ESACT1


ESACT8 = ESACT1


ESACT9 = ESACT1


ESACT10 = ESACT1


ESACT11 = ESACT1


ESACT12 = ESACT1


ESACT13 = ESACT1


ESACT14 = ESACT1


ESACT15 = ESACT1


ESACT16 = ESACT1


ESACT17 = ESACT1


ESACT18 = ESACT1


ESACT19 = ESACT1


ESACT20 = ESACT1


ESACT21 = ESACT1


ESACT22 = ESACT1


ESACT23 = ESACT1


ESACT24 = ESACT1


ESACT25 = ESACT1


ESACT26 = ESACT1


ESACT27 = ESACT1


ESACT28 = ESACT1


ESACT29 = ESACT1


ESACT30 = ESACT1


ESACT31 = ESACT1


ESACT32 = ESACT1


ESACT33 = ESACT1


ESACT34 = ESACT1


ESACT35 = ESACT1


ESACT36 = ESACT1


ESACT37 = ESACT1


ESACT38 = ESACT1


ESACT39 = ESACT1


ESACT40 = ESACT1


ESACT41 = ESACT1


ESACT42 = ESACT1


ESACT43 = ESACT1


ESACT44 = ESACT1


ESACT45 = ESACT1


ESACT46 = ESACT1


ESACT47 = ESACT1


ESACT48 = ESACT1


ESACT49 = ESACT1


ESACT50 = ESACT1


ESACT51 = ESACT1


ESACT52 = ESACT1


ESACT53 = ESACT1


ESACT54 = ESACT1


ESACT55 = ESACT1


ESACT56 = ESACT1


ESACT57 = ESACT1


ESACT58 = ESACT1


ESACT59 = ESACT1


ESACT60 = ESACT1


ESACT61 = ESACT1


ESACT62 = ESACT1


ESACT63 = ESACT1


ESACT64 = ESACT1


ESACT65 = ESACT1


ESACT66 = ESACT1


ESACT67 = ESACT1


ESACT68 = ESACT1


ESACT69 = ESACT1


ESACT70 = ESACT1


ESACT71 = ESACT1


ESACT72 = ESACT1


ESACT73 = ESACT1


ESACT74 = ESACT1


ESACT75 = ESACT1


ESACT76 = ESACT1


ESACT77 = ESACT1


ESACT78 = ESACT1


ESACT79 = ESACT1


ESACT80 = ESACT1


ESACT81 = ESACT1


ESACT82 = ESACT1


ESACT83 = ESACT1


ESACT84 = ESACT1


ESACT85 = ESACT1


ESACT86 = ESACT1


ESACT87 = ESACT1


ESACT88 = ESACT1


ESACT89 = ESACT1


ESACT90 = ESACT1


ESACT91 = ESACT1


ESACT92 = ESACT1


ESACT93 = ESACT1


ESACT94 = ESACT1


ESACT95 = ESACT1


ESACT96 = ESACT1


ESACT97 = ESACT1


ESACT98 = ESACT1


ESACT99 = ESACT1


class EWHER1(OrderedEnum):
    _MISSING = '-1'
    _UNSPECIFIED_LOCATION = '0'
    _UNSPECIFIED_LOCATION_NOT_TRAVELLING = '1'
    _HOME = '2'
    _SECOND_HOME_OR_WEEKEND_HOUSE = '3'
    _WORKING_PLACE_OR_SCHOOL = '4'
    _OTHER_PEOPLE_S_HOME = '5'
    _RESTAURANT__CAFÉ_OR_PUB = '6'
    _SPORTS_FACILITY = '7'
    __ARTS_OR_CULTURAL_CENTRE = '8'
    _THE_COUNTRY_COUNTRYSIDE__SEASIDE__BEACH_OR_COAST = '9'
    _OTHER_SPECIFIED_LOCATION_NOT_TRAVELLING = '10'
    _UNSPECIFIED_PRIVATE_TRANSPORT_MODE = '11'
    _TRAVELLING_ON_FOOT = '12'
    _TRAVELLING_BY_BICYCLE = '13'
    _TRAVELLING_BY_MOPED__MOTORCYCLE_OR_MOTORBOAT = '14'
    _TRAVELLING_BY_PASSENGER_CAR_AS_THE_DRIVER = '15'
    _TRAVELLING_BY_PASSENGER_CAR_AS_A_PASSENGER = '16'
    _TRAVELLING_BY_PASSENGER_CAR_DRIVER_STATUS_UNSPECIFIED = '17'
    _TRAVELLING_BY_LORRY__OR_TRACTOR = '18'
    _TRAVELLING_BY_VAN = '19'
    _OTHER_SPECIFIED_PRIVATE_TRAVELLING_MODE = '20'
    _UNSPECIFIED_PUBLIC_TRANSPORT_MODE = '21'
    _TRAVELLING_BY_TAXI = '22'
    _TRAVELLING_BY_BUS = '23'
    _TRAVELLING_BY_TRAM_OR_UNDERGROUND = '24'
    _TRAVELLING_BY_TRAIN = '25'
    _TRAVELLING_BY_AEROPLANE = '26'
    _TRAVELLING_BY_BOAT_OR_SHIP = '27'
    __TRAVELLING_BY_COACH = '28'
    _WAITING_FOR_PUBLIC_TRANSPORT = '29'
    _OTHER_SPECIFIED_PUBLIC_TRANSPORT_MODE = '30'
    _UNSPECIFIED_TRANSPORT_MODE = '31'
    _ILLEGIBLE_LOCATION_OR_TRANSPORT_MODE = '32'
    MISSING2 = '-2'
    MISSING3 = '-9'


EWHER2 = EWHER1


EWHER3 = EWHER1


EWHER4 = EWHER1


EWHER5 = EWHER1


EWHER6 = EWHER1


EWHER7 = EWHER1


EWHER8 = EWHER1


EWHER9 = EWHER1


EWHER10 = EWHER1


EWHER11 = EWHER1


EWHER12 = EWHER1


EWHER13 = EWHER1


EWHER14 = EWHER1


EWHER15 = EWHER1


EWHER16 = EWHER1


EWHER17 = EWHER1


EWHER18 = EWHER1


EWHER19 = EWHER1


EWHER20 = EWHER1


EWHER21 = EWHER1


EWHER22 = EWHER1


EWHER23 = EWHER1


EWHER24 = EWHER1


EWHER25 = EWHER1


EWHER26 = EWHER1


EWHER27 = EWHER1


EWHER28 = EWHER1


EWHER29 = EWHER1


EWHER30 = EWHER1


EWHER31 = EWHER1


EWHER32 = EWHER1


EWHER33 = EWHER1


EWHER34 = EWHER1


EWHER35 = EWHER1


EWHER36 = EWHER1


EWHER37 = EWHER1


EWHER38 = EWHER1


EWHER39 = EWHER1


EWHER40 = EWHER1


EWHER41 = EWHER1


EWHER42 = EWHER1


EWHER43 = EWHER1


EWHER44 = EWHER1


EWHER45 = EWHER1


EWHER46 = EWHER1


EWHER47 = EWHER1


EWHER48 = EWHER1


EWHER49 = EWHER1


EWHER50 = EWHER1


EWHER51 = EWHER1


EWHER52 = EWHER1


EWHER53 = EWHER1


EWHER54 = EWHER1


EWHER55 = EWHER1


EWHER56 = EWHER1


EWHER57 = EWHER1


EWHER58 = EWHER1


EWHER59 = EWHER1


EWHER60 = EWHER1


EWHER61 = EWHER1


EWHER62 = EWHER1


EWHER63 = EWHER1


EWHER64 = EWHER1


EWHER65 = EWHER1


EWHER66 = EWHER1


EWHER67 = EWHER1


EWHER68 = EWHER1


EWHER69 = EWHER1


EWHER70 = EWHER1


EWHER71 = EWHER1


EWHER72 = EWHER1


EWHER73 = EWHER1


EWHER74 = EWHER1


EWHER75 = EWHER1


EWHER76 = EWHER1


EWHER77 = EWHER1


EWHER78 = EWHER1


EWHER79 = EWHER1


EWHER80 = EWHER1


EWHER81 = EWHER1


EWHER82 = EWHER1


EWHER83 = EWHER1


EWHER84 = EWHER1


EWHER85 = EWHER1


EWHER86 = EWHER1


EWHER87 = EWHER1


EWHER88 = EWHER1


EWHER89 = EWHER1


EWHER90 = EWHER1


EWHER91 = EWHER1


EWHER92 = EWHER1


EWHER93 = EWHER1


EWHER94 = EWHER1


EWHER95 = EWHER1


EWHER96 = EWHER1


EWHER97 = EWHER1


EWHER98 = EWHER1


EWHER99 = EWHER1


class EWIT01(OrderedEnum):
    NOT_ALONE = '0'
    ALONE = '1'
    MISSING1 = '-1'


EWIT02 = EWIT01


EWIT03 = EWIT01


EWIT04 = EWIT01


EWIT05 = EWIT01


EWIT06 = EWIT01


EWIT07 = EWIT01


EWIT08 = EWIT01


EWIT09 = EWIT01


EWIT010 = EWIT01


EWIT011 = EWIT01


EWIT012 = EWIT01


EWIT013 = EWIT01


EWIT014 = EWIT01


EWIT015 = EWIT01


EWIT016 = EWIT01


EWIT017 = EWIT01


EWIT018 = EWIT01


EWIT019 = EWIT01


EWIT020 = EWIT01


EWIT021 = EWIT01


EWIT022 = EWIT01


EWIT023 = EWIT01


EWIT024 = EWIT01


EWIT025 = EWIT01


EWIT026 = EWIT01


EWIT027 = EWIT01


EWIT028 = EWIT01


EWIT029 = EWIT01


EWIT030 = EWIT01


EWIT031 = EWIT01


EWIT032 = EWIT01


EWIT033 = EWIT01


EWIT034 = EWIT01


EWIT035 = EWIT01


EWIT036 = EWIT01


EWIT037 = EWIT01


EWIT038 = EWIT01


EWIT039 = EWIT01


EWIT040 = EWIT01


EWIT041 = EWIT01


EWIT042 = EWIT01


EWIT043 = EWIT01


EWIT044 = EWIT01


EWIT045 = EWIT01


EWIT046 = EWIT01


EWIT047 = EWIT01


EWIT048 = EWIT01


EWIT049 = EWIT01


EWIT050 = EWIT01


EWIT051 = EWIT01


EWIT052 = EWIT01


EWIT053 = EWIT01


EWIT054 = EWIT01


EWIT055 = EWIT01


EWIT056 = EWIT01


EWIT057 = EWIT01


EWIT058 = EWIT01


EWIT059 = EWIT01


EWIT060 = EWIT01


EWIT061 = EWIT01


EWIT062 = EWIT01


EWIT063 = EWIT01


EWIT064 = EWIT01


EWIT065 = EWIT01


EWIT066 = EWIT01


EWIT067 = EWIT01


EWIT068 = EWIT01


EWIT069 = EWIT01


EWIT070 = EWIT01


EWIT071 = EWIT01


EWIT072 = EWIT01


EWIT073 = EWIT01


EWIT074 = EWIT01


EWIT075 = EWIT01


EWIT076 = EWIT01


EWIT077 = EWIT01


EWIT078 = EWIT01


EWIT079 = EWIT01


EWIT080 = EWIT01


EWIT081 = EWIT01


EWIT082 = EWIT01


EWIT083 = EWIT01


EWIT084 = EWIT01


EWIT085 = EWIT01


EWIT086 = EWIT01


EWIT087 = EWIT01


EWIT088 = EWIT01


EWIT089 = EWIT01


EWIT090 = EWIT01


EWIT091 = EWIT01


EWIT092 = EWIT01


EWIT093 = EWIT01


EWIT094 = EWIT01


EWIT095 = EWIT01


EWIT096 = EWIT01


EWIT097 = EWIT01


EWIT098 = EWIT01


EWIT099 = EWIT01


class EWIT11(OrderedEnum):
    NOT_WITH_KIDS_0_9 = '0'
    WITH_KIDS_0_9 = '1'
    MISSING1 = '-1'


EWIT12 = EWIT11


EWIT13 = EWIT11


EWIT14 = EWIT11


EWIT15 = EWIT11


EWIT16 = EWIT11


EWIT17 = EWIT11


EWIT18 = EWIT11


EWIT19 = EWIT11


EWIT110 = EWIT11


EWIT111 = EWIT11


EWIT112 = EWIT11


EWIT113 = EWIT11


EWIT114 = EWIT11


EWIT115 = EWIT11


EWIT116 = EWIT11


EWIT117 = EWIT11


EWIT118 = EWIT11


EWIT119 = EWIT11


EWIT120 = EWIT11


EWIT121 = EWIT11


EWIT122 = EWIT11


EWIT123 = EWIT11


EWIT124 = EWIT11


EWIT125 = EWIT11


EWIT126 = EWIT11


EWIT127 = EWIT11


EWIT128 = EWIT11


EWIT129 = EWIT11


EWIT130 = EWIT11


EWIT131 = EWIT11


EWIT132 = EWIT11


EWIT133 = EWIT11


EWIT134 = EWIT11


EWIT135 = EWIT11


EWIT136 = EWIT11


EWIT137 = EWIT11


EWIT138 = EWIT11


EWIT139 = EWIT11


EWIT140 = EWIT11


EWIT141 = EWIT11


EWIT142 = EWIT11


EWIT143 = EWIT11


EWIT144 = EWIT11


EWIT145 = EWIT11


EWIT146 = EWIT11


EWIT147 = EWIT11


EWIT148 = EWIT11


EWIT149 = EWIT11


EWIT150 = EWIT11


EWIT151 = EWIT11


EWIT152 = EWIT11


EWIT153 = EWIT11


EWIT154 = EWIT11


EWIT155 = EWIT11


EWIT156 = EWIT11


EWIT157 = EWIT11


EWIT158 = EWIT11


EWIT159 = EWIT11


EWIT160 = EWIT11


EWIT161 = EWIT11


EWIT162 = EWIT11


EWIT163 = EWIT11


EWIT164 = EWIT11


EWIT165 = EWIT11


EWIT166 = EWIT11


EWIT167 = EWIT11


EWIT168 = EWIT11


EWIT169 = EWIT11


EWIT170 = EWIT11


EWIT171 = EWIT11


EWIT172 = EWIT11


EWIT173 = EWIT11


EWIT174 = EWIT11


EWIT175 = EWIT11


EWIT176 = EWIT11


EWIT177 = EWIT11


EWIT178 = EWIT11


EWIT179 = EWIT11


EWIT180 = EWIT11


EWIT181 = EWIT11


EWIT182 = EWIT11


EWIT183 = EWIT11


EWIT184 = EWIT11


EWIT185 = EWIT11


EWIT186 = EWIT11


EWIT187 = EWIT11


EWIT188 = EWIT11


EWIT189 = EWIT11


EWIT190 = EWIT11


EWIT191 = EWIT11


EWIT192 = EWIT11


EWIT193 = EWIT11


EWIT194 = EWIT11


EWIT195 = EWIT11


EWIT196 = EWIT11


EWIT197 = EWIT11


EWIT198 = EWIT11


EWIT199 = EWIT11


class EWIT21(OrderedEnum):
    NOT_WITH_KIDS_10_13 = '0'
    WITH_KIDS_10_13 = '1'
    MISSING1 = '-1'


EWIT22 = EWIT21


EWIT23 = EWIT21


EWIT24 = EWIT21


EWIT25 = EWIT21


EWIT26 = EWIT21


EWIT27 = EWIT21


EWIT28 = EWIT21


EWIT29 = EWIT21


EWIT210 = EWIT21


EWIT211 = EWIT21


EWIT212 = EWIT21


EWIT213 = EWIT21


EWIT214 = EWIT21


EWIT215 = EWIT21


EWIT216 = EWIT21


EWIT217 = EWIT21


EWIT218 = EWIT21


EWIT219 = EWIT21


EWIT220 = EWIT21


EWIT221 = EWIT21


EWIT222 = EWIT21


EWIT223 = EWIT21


EWIT224 = EWIT21


EWIT225 = EWIT21


EWIT226 = EWIT21


EWIT227 = EWIT21


EWIT228 = EWIT21


EWIT229 = EWIT21


EWIT230 = EWIT21


EWIT231 = EWIT21


EWIT232 = EWIT21


EWIT233 = EWIT21


EWIT234 = EWIT21


EWIT235 = EWIT21


EWIT236 = EWIT21


EWIT237 = EWIT21


EWIT238 = EWIT21


EWIT239 = EWIT21


EWIT240 = EWIT21


EWIT241 = EWIT21


EWIT242 = EWIT21


EWIT243 = EWIT21


EWIT244 = EWIT21


EWIT245 = EWIT21


EWIT246 = EWIT21


EWIT247 = EWIT21


EWIT248 = EWIT21


EWIT249 = EWIT21


EWIT250 = EWIT21


EWIT251 = EWIT21


EWIT252 = EWIT21


EWIT253 = EWIT21


EWIT254 = EWIT21


EWIT255 = EWIT21


EWIT256 = EWIT21


EWIT257 = EWIT21


EWIT258 = EWIT21


EWIT259 = EWIT21


EWIT260 = EWIT21


EWIT261 = EWIT21


EWIT262 = EWIT21


EWIT263 = EWIT21


EWIT264 = EWIT21


EWIT265 = EWIT21


EWIT266 = EWIT21


EWIT267 = EWIT21


EWIT268 = EWIT21


EWIT269 = EWIT21


EWIT270 = EWIT21


EWIT271 = EWIT21


EWIT272 = EWIT21


EWIT273 = EWIT21


EWIT274 = EWIT21


EWIT275 = EWIT21


EWIT276 = EWIT21


EWIT277 = EWIT21


EWIT278 = EWIT21


EWIT279 = EWIT21


EWIT280 = EWIT21


EWIT281 = EWIT21


EWIT282 = EWIT21


EWIT283 = EWIT21


EWIT284 = EWIT21


EWIT285 = EWIT21


EWIT286 = EWIT21


EWIT287 = EWIT21


EWIT288 = EWIT21


EWIT289 = EWIT21


EWIT290 = EWIT21


EWIT291 = EWIT21


EWIT292 = EWIT21


EWIT293 = EWIT21


EWIT294 = EWIT21


EWIT295 = EWIT21


EWIT296 = EWIT21


EWIT297 = EWIT21


EWIT298 = EWIT21


EWIT299 = EWIT21


class EWIT31(OrderedEnum):
    NOT_WITH_OTHER_HOUSEHOLD_MEMBERS = '0'
    WITH_OTHER_HOUSEHOLD_MEMBERS = '1'
    MISSING1 = '-1'


EWIT32 = EWIT31


EWIT33 = EWIT31


EWIT34 = EWIT31


EWIT35 = EWIT31


EWIT36 = EWIT31


EWIT37 = EWIT31


EWIT38 = EWIT31


EWIT39 = EWIT31


EWIT310 = EWIT31


EWIT311 = EWIT31


EWIT312 = EWIT31


EWIT313 = EWIT31


EWIT314 = EWIT31


EWIT315 = EWIT31


EWIT316 = EWIT31


EWIT317 = EWIT31


EWIT318 = EWIT31


EWIT319 = EWIT31


EWIT320 = EWIT31


EWIT321 = EWIT31


EWIT322 = EWIT31


EWIT323 = EWIT31


EWIT324 = EWIT31


EWIT325 = EWIT31


EWIT326 = EWIT31


EWIT327 = EWIT31


EWIT328 = EWIT31


EWIT329 = EWIT31


EWIT330 = EWIT31


EWIT331 = EWIT31


EWIT332 = EWIT31


EWIT333 = EWIT31


EWIT334 = EWIT31


EWIT335 = EWIT31


EWIT336 = EWIT31


EWIT337 = EWIT31


EWIT338 = EWIT31


EWIT339 = EWIT31


EWIT340 = EWIT31


EWIT341 = EWIT31


EWIT342 = EWIT31


EWIT343 = EWIT31


EWIT344 = EWIT31


EWIT345 = EWIT31


EWIT346 = EWIT31


EWIT347 = EWIT31


EWIT348 = EWIT31


EWIT349 = EWIT31


EWIT350 = EWIT31


EWIT351 = EWIT31


EWIT352 = EWIT31


EWIT353 = EWIT31


EWIT354 = EWIT31


EWIT355 = EWIT31


EWIT356 = EWIT31


EWIT357 = EWIT31


EWIT358 = EWIT31


EWIT359 = EWIT31


EWIT360 = EWIT31


EWIT361 = EWIT31


EWIT362 = EWIT31


EWIT363 = EWIT31


EWIT364 = EWIT31


EWIT365 = EWIT31


EWIT366 = EWIT31


EWIT367 = EWIT31


EWIT368 = EWIT31


EWIT369 = EWIT31


EWIT370 = EWIT31


EWIT371 = EWIT31


EWIT372 = EWIT31


EWIT373 = EWIT31


EWIT374 = EWIT31


EWIT375 = EWIT31


EWIT376 = EWIT31


EWIT377 = EWIT31


EWIT378 = EWIT31


EWIT379 = EWIT31


EWIT380 = EWIT31


EWIT381 = EWIT31


EWIT382 = EWIT31


EWIT383 = EWIT31


EWIT384 = EWIT31


EWIT385 = EWIT31


EWIT386 = EWIT31


EWIT387 = EWIT31


EWIT388 = EWIT31


EWIT389 = EWIT31


EWIT390 = EWIT31


EWIT391 = EWIT31


EWIT392 = EWIT31


EWIT393 = EWIT31


EWIT394 = EWIT31


EWIT395 = EWIT31


EWIT396 = EWIT31


EWIT397 = EWIT31


EWIT398 = EWIT31


EWIT399 = EWIT31


class EWIT41(OrderedEnum):
    NOT_WITH_OTHER_PERSONS_THEY_KNOW = '0'
    WITH_OTHER_PERSONS_THEY_KNOW = '1'
    MISSING1 = '-1'


EWIT42 = EWIT41


EWIT43 = EWIT41


EWIT44 = EWIT41


EWIT45 = EWIT41


EWIT46 = EWIT41


EWIT47 = EWIT41


EWIT48 = EWIT41


EWIT49 = EWIT41


EWIT410 = EWIT41


EWIT411 = EWIT41


EWIT412 = EWIT41


EWIT413 = EWIT41


EWIT414 = EWIT41


EWIT415 = EWIT41


EWIT416 = EWIT41


EWIT417 = EWIT41


EWIT418 = EWIT41


EWIT419 = EWIT41


EWIT420 = EWIT41


EWIT421 = EWIT41


EWIT422 = EWIT41


EWIT423 = EWIT41


EWIT424 = EWIT41


EWIT425 = EWIT41


EWIT426 = EWIT41


EWIT427 = EWIT41


EWIT428 = EWIT41


EWIT429 = EWIT41


EWIT430 = EWIT41


EWIT431 = EWIT41


EWIT432 = EWIT41


EWIT433 = EWIT41


EWIT434 = EWIT41


EWIT435 = EWIT41


EWIT436 = EWIT41


EWIT437 = EWIT41


EWIT438 = EWIT41


EWIT439 = EWIT41


EWIT440 = EWIT41


EWIT441 = EWIT41


EWIT442 = EWIT41


EWIT443 = EWIT41


EWIT444 = EWIT41


EWIT445 = EWIT41


EWIT446 = EWIT41


EWIT447 = EWIT41


EWIT448 = EWIT41


EWIT449 = EWIT41


EWIT450 = EWIT41


EWIT451 = EWIT41


EWIT452 = EWIT41


EWIT453 = EWIT41


EWIT454 = EWIT41


EWIT455 = EWIT41


EWIT456 = EWIT41


EWIT457 = EWIT41


EWIT458 = EWIT41


EWIT459 = EWIT41


EWIT460 = EWIT41


EWIT461 = EWIT41


EWIT462 = EWIT41


EWIT463 = EWIT41


EWIT464 = EWIT41


EWIT465 = EWIT41


EWIT466 = EWIT41


EWIT467 = EWIT41


EWIT468 = EWIT41


EWIT469 = EWIT41


EWIT470 = EWIT41


EWIT471 = EWIT41


EWIT472 = EWIT41


EWIT473 = EWIT41


EWIT474 = EWIT41


EWIT475 = EWIT41


EWIT476 = EWIT41


EWIT477 = EWIT41


EWIT478 = EWIT41


EWIT479 = EWIT41


EWIT480 = EWIT41


EWIT481 = EWIT41


EWIT482 = EWIT41


EWIT483 = EWIT41


EWIT484 = EWIT41


EWIT485 = EWIT41


EWIT486 = EWIT41


EWIT487 = EWIT41


EWIT488 = EWIT41


EWIT489 = EWIT41


EWIT490 = EWIT41


EWIT491 = EWIT41


EWIT492 = EWIT41


EWIT493 = EWIT41


EWIT494 = EWIT41


EWIT495 = EWIT41


EWIT496 = EWIT41


EWIT497 = EWIT41


EWIT498 = EWIT41


EWIT499 = EWIT41


class EWIT51(OrderedEnum):
    NOT_AT_WORK__STUDY__ASLEEP = '0'
    AT_WORK__STUDY__ASLEEP = '1'
    MISSING1 = '-1'


EWIT52 = EWIT51


EWIT53 = EWIT51


EWIT54 = EWIT51


EWIT55 = EWIT51


EWIT56 = EWIT51


EWIT57 = EWIT51


EWIT58 = EWIT51


EWIT59 = EWIT51


EWIT510 = EWIT51


EWIT511 = EWIT51


EWIT512 = EWIT51


EWIT513 = EWIT51


EWIT514 = EWIT51


EWIT515 = EWIT51


EWIT516 = EWIT51


EWIT517 = EWIT51


EWIT518 = EWIT51


EWIT519 = EWIT51


EWIT520 = EWIT51


EWIT521 = EWIT51


EWIT522 = EWIT51


EWIT523 = EWIT51


EWIT524 = EWIT51


EWIT525 = EWIT51


EWIT526 = EWIT51


EWIT527 = EWIT51


EWIT528 = EWIT51


EWIT529 = EWIT51


EWIT530 = EWIT51


EWIT531 = EWIT51


EWIT532 = EWIT51


EWIT533 = EWIT51


EWIT534 = EWIT51


EWIT535 = EWIT51


EWIT536 = EWIT51


EWIT537 = EWIT51


EWIT538 = EWIT51


EWIT539 = EWIT51


EWIT540 = EWIT51


EWIT541 = EWIT51


EWIT542 = EWIT51


EWIT543 = EWIT51


EWIT544 = EWIT51


EWIT545 = EWIT51


EWIT546 = EWIT51


EWIT547 = EWIT51


EWIT548 = EWIT51


EWIT549 = EWIT51


EWIT550 = EWIT51


EWIT551 = EWIT51


EWIT552 = EWIT51


EWIT553 = EWIT51


EWIT554 = EWIT51


EWIT555 = EWIT51


EWIT556 = EWIT51


EWIT557 = EWIT51


EWIT558 = EWIT51


EWIT559 = EWIT51


EWIT560 = EWIT51


EWIT561 = EWIT51


EWIT562 = EWIT51


EWIT563 = EWIT51


EWIT564 = EWIT51


EWIT565 = EWIT51


EWIT566 = EWIT51


EWIT567 = EWIT51


EWIT568 = EWIT51


EWIT569 = EWIT51


EWIT570 = EWIT51


EWIT571 = EWIT51


EWIT572 = EWIT51


EWIT573 = EWIT51


EWIT574 = EWIT51


EWIT575 = EWIT51


EWIT576 = EWIT51


EWIT577 = EWIT51


EWIT578 = EWIT51


EWIT579 = EWIT51


EWIT580 = EWIT51


EWIT581 = EWIT51


EWIT582 = EWIT51


EWIT583 = EWIT51


EWIT584 = EWIT51


EWIT585 = EWIT51


EWIT586 = EWIT51


EWIT587 = EWIT51


EWIT588 = EWIT51


EWIT589 = EWIT51


EWIT590 = EWIT51


EWIT591 = EWIT51


EWIT592 = EWIT51


EWIT593 = EWIT51


EWIT594 = EWIT51


EWIT595 = EWIT51


EWIT596 = EWIT51


EWIT597 = EWIT51


EWIT598 = EWIT51


EWIT599 = EWIT51


class EWIT61(OrderedEnum):
    NOT_NO_ANSWER = '0'
    NO_ANSWER = '1'
    MISSING1 = '-1'


EWIT62 = EWIT61


EWIT63 = EWIT61


EWIT64 = EWIT61


EWIT65 = EWIT61


EWIT66 = EWIT61


EWIT67 = EWIT61


EWIT68 = EWIT61


EWIT69 = EWIT61


EWIT610 = EWIT61


EWIT611 = EWIT61


EWIT612 = EWIT61


EWIT613 = EWIT61


EWIT614 = EWIT61


EWIT615 = EWIT61


EWIT616 = EWIT61


EWIT617 = EWIT61


EWIT618 = EWIT61


EWIT619 = EWIT61


EWIT620 = EWIT61


EWIT621 = EWIT61


EWIT622 = EWIT61


EWIT623 = EWIT61


EWIT624 = EWIT61


EWIT625 = EWIT61


EWIT626 = EWIT61


EWIT627 = EWIT61


EWIT628 = EWIT61


EWIT629 = EWIT61


EWIT630 = EWIT61


EWIT631 = EWIT61


EWIT632 = EWIT61


EWIT633 = EWIT61


EWIT634 = EWIT61


EWIT635 = EWIT61


EWIT636 = EWIT61


EWIT637 = EWIT61


EWIT638 = EWIT61


EWIT639 = EWIT61


EWIT640 = EWIT61


EWIT641 = EWIT61


EWIT642 = EWIT61


EWIT643 = EWIT61


EWIT644 = EWIT61


EWIT645 = EWIT61


EWIT646 = EWIT61


EWIT647 = EWIT61


EWIT648 = EWIT61


EWIT649 = EWIT61


EWIT650 = EWIT61


EWIT651 = EWIT61


EWIT652 = EWIT61


EWIT653 = EWIT61


EWIT654 = EWIT61


EWIT655 = EWIT61


EWIT656 = EWIT61


EWIT657 = EWIT61


EWIT658 = EWIT61


EWIT659 = EWIT61


EWIT660 = EWIT61


EWIT661 = EWIT61


EWIT662 = EWIT61


EWIT663 = EWIT61


EWIT664 = EWIT61


EWIT665 = EWIT61


EWIT666 = EWIT61


EWIT667 = EWIT61


EWIT668 = EWIT61


EWIT669 = EWIT61


EWIT670 = EWIT61


EWIT671 = EWIT61


EWIT672 = EWIT61


EWIT673 = EWIT61


EWIT674 = EWIT61


EWIT675 = EWIT61


EWIT676 = EWIT61


EWIT677 = EWIT61


EWIT678 = EWIT61


EWIT679 = EWIT61


EWIT680 = EWIT61


EWIT681 = EWIT61


EWIT682 = EWIT61


EWIT683 = EWIT61


EWIT684 = EWIT61


EWIT685 = EWIT61


EWIT686 = EWIT61


EWIT687 = EWIT61


EWIT688 = EWIT61


EWIT689 = EWIT61


EWIT690 = EWIT61


EWIT691 = EWIT61


EWIT692 = EWIT61


EWIT693 = EWIT61


EWIT694 = EWIT61


EWIT695 = EWIT61


EWIT696 = EWIT61


EWIT697 = EWIT61


EWIT698 = EWIT61


EWIT699 = EWIT61


class EVST1(OrderedEnum):
    N4_00 = '1'
    N4_10 = '2'
    N4_20 = '3'
    N4_30 = '4'
    N4_40 = '5'
    N4_50 = '6'
    N5_00 = '7'
    N5_10 = '8'
    N5_20 = '9'
    N5_30 = '10'
    N5_40 = '11'
    N5_50 = '12'
    N6_00 = '13'
    N6_10 = '14'
    N6_20 = '15'
    N6_30 = '16'
    N6_40 = '17'
    N6_50 = '18'
    N7_00 = '19'
    N7_10 = '20'
    N7_20 = '21'
    N7_30 = '22'
    N7_40 = '23'
    N7_50 = '24'
    N8_00 = '25'
    N8_10 = '26'
    N8_20 = '27'
    N8_30 = '28'
    N8_40 = '29'
    N8_50 = '30'
    N9_00 = '31'
    N9_10 = '32'
    N9_20 = '33'
    N9_30 = '34'
    N9_40 = '35'
    N9_50 = '36'
    N10_00 = '37'
    N10_10 = '38'
    N10_20 = '39'
    N10_30 = '40'
    N10_40 = '41'
    N10_50 = '42'
    N11_00 = '43'
    N11_10 = '44'
    N11_20 = '45'
    N11_30 = '46'
    N11_40 = '47'
    N11_50 = '48'
    N12_00 = '49'
    N12_10 = '50'
    N12_20 = '51'
    N12_30 = '52'
    N12_40 = '53'
    N12_50 = '54'
    N13_00 = '55'
    N13_10 = '56'
    N13_20 = '57'
    N13_30 = '58'
    N13_40 = '59'
    N13_50 = '60'
    N14_00 = '61'
    N14_10 = '62'
    N14_20 = '63'
    N14_30 = '64'
    N14_40 = '65'
    N14_50 = '66'
    N15_00 = '67'
    N15_10 = '68'
    N15_20 = '69'
    N15_30 = '70'
    N15_40 = '71'
    N15_50 = '72'
    N16_00 = '73'
    N16_10 = '74'
    N16_20 = '75'
    N16_30 = '76'
    N16_40 = '77'
    N16_50 = '78'
    N17_00 = '79'
    N17_10 = '80'
    N17_20 = '81'
    N17_30 = '82'
    N17_40 = '83'
    N17_50 = '84'
    N18_00 = '85'
    N18_10 = '86'
    N18_20 = '87'
    N18_30 = '88'
    N18_40 = '89'
    N18_50 = '90'
    N19_00 = '91'
    N19_10 = '92'
    N19_20 = '93'
    N19_30 = '94'
    N19_40 = '95'
    N19_50 = '96'
    N20_00 = '97'
    N20_10 = '98'
    N20_20 = '99'
    N20_30 = '100'
    N20_40 = '101'
    N20_50 = '102'
    N21_00 = '103'
    N21_10 = '104'
    N21_20 = '105'
    N21_30 = '106'
    N21_40 = '107'
    N21_50 = '108'
    N22_00 = '109'
    N22_10 = '110'
    N22_20 = '111'
    N22_30 = '112'
    N22_40 = '113'
    N22_50 = '114'
    N23_00 = '115'
    N23_10 = '116'
    N23_20 = '117'
    N23_30 = '118'
    N23_40 = '119'
    N23_50 = '120'
    N00_00 = '121'
    N00_10 = '122'
    N00_20 = '123'
    N00_30 = '124'
    N00_40 = '125'
    N00_50 = '126'
    N01_00 = '127'
    N01_10 = '128'
    N01_20 = '129'
    N01_30 = '130'
    N01_40 = '131'
    N01_50 = '132'
    N02_00 = '133'
    N02_10 = '134'
    N02_20 = '135'
    N02_30 = '136'
    N02_40 = '137'
    N02_50 = '138'
    N03_00 = '139'
    N03_10 = '140'
    N03_20 = '141'
    N03_30 = '142'
    N03_40 = '143'
    N03_50 = '144'


EVST2 = EVST1


EVST3 = EVST1


EVST4 = EVST1


EVST5 = EVST1


EVST6 = EVST1


EVST7 = EVST1


EVST8 = EVST1


EVST9 = EVST1


EVST10 = EVST1


EVST11 = EVST1


EVST12 = EVST1


EVST13 = EVST1


EVST14 = EVST1


EVST15 = EVST1


EVST16 = EVST1


EVST17 = EVST1


EVST18 = EVST1


EVST19 = EVST1


EVST20 = EVST1


EVST21 = EVST1


EVST22 = EVST1


EVST23 = EVST1


EVST24 = EVST1


EVST25 = EVST1


EVST26 = EVST1


EVST27 = EVST1


EVST28 = EVST1


EVST29 = EVST1


EVST30 = EVST1


EVST31 = EVST1


EVST32 = EVST1


EVST33 = EVST1


EVST34 = EVST1


EVST35 = EVST1


EVST36 = EVST1


EVST37 = EVST1


EVST38 = EVST1


EVST39 = EVST1


EVST40 = EVST1


EVST41 = EVST1


EVST42 = EVST1


EVST43 = EVST1


EVST44 = EVST1


EVST45 = EVST1


EVST46 = EVST1


EVST47 = EVST1


EVST48 = EVST1


EVST49 = EVST1


EVST50 = EVST1


EVST51 = EVST1


EVST52 = EVST1


EVST53 = EVST1


EVST54 = EVST1


EVST55 = EVST1


EVST56 = EVST1


EVST57 = EVST1


EVST58 = EVST1


EVST59 = EVST1


EVST60 = EVST1


EVST61 = EVST1


EVST62 = EVST1


EVST63 = EVST1


EVST64 = EVST1


EVST65 = EVST1


EVST66 = EVST1


EVST67 = EVST1


EVST68 = EVST1


EVST69 = EVST1


EVST70 = EVST1


EVST71 = EVST1


EVST72 = EVST1


EVST73 = EVST1


EVST74 = EVST1


EVST75 = EVST1


EVST76 = EVST1


EVST77 = EVST1


EVST78 = EVST1


EVST79 = EVST1


EVST80 = EVST1


EVST81 = EVST1


EVST82 = EVST1


EVST83 = EVST1


EVST84 = EVST1


EVST85 = EVST1


EVST86 = EVST1


EVST87 = EVST1


EVST88 = EVST1


EVST89 = EVST1


EVST90 = EVST1


EVST91 = EVST1


EVST92 = EVST1


EVST93 = EVST1


EVST94 = EVST1


EVST95 = EVST1


EVST96 = EVST1


EVST97 = EVST1


EVST98 = EVST1


EVST99 = EVST1


EVND1 = EVST1


EVND2 = EVST1


EVND3 = EVST1


EVND4 = EVST1


EVND5 = EVST1


EVND6 = EVST1


EVND7 = EVST1


EVND8 = EVST1


EVND9 = EVST1


EVND10 = EVST1


EVND11 = EVST1


EVND12 = EVST1


EVND13 = EVST1


EVND14 = EVST1


EVND15 = EVST1


EVND16 = EVST1


EVND17 = EVST1


EVND18 = EVST1


EVND19 = EVST1


EVND20 = EVST1


EVND21 = EVST1


EVND22 = EVST1


EVND23 = EVST1


EVND24 = EVST1


EVND25 = EVST1


EVND26 = EVST1


EVND27 = EVST1


EVND28 = EVST1


EVND29 = EVST1


EVND30 = EVST1


EVND31 = EVST1


EVND32 = EVST1


EVND33 = EVST1


EVND34 = EVST1


EVND35 = EVST1


EVND36 = EVST1


EVND37 = EVST1


EVND38 = EVST1


EVND39 = EVST1


EVND40 = EVST1


EVND41 = EVST1


EVND42 = EVST1


EVND43 = EVST1


EVND44 = EVST1


EVND45 = EVST1


EVND46 = EVST1


EVND47 = EVST1


EVND48 = EVST1


EVND49 = EVST1


EVND50 = EVST1


EVND51 = EVST1


EVND52 = EVST1


EVND53 = EVST1


EVND54 = EVST1


EVND55 = EVST1


EVND56 = EVST1


EVND57 = EVST1


EVND58 = EVST1


EVND59 = EVST1


EVND60 = EVST1


EVND61 = EVST1


EVND62 = EVST1


EVND63 = EVST1


EVND64 = EVST1


EVND65 = EVST1


EVND66 = EVST1


EVND67 = EVST1


EVND68 = EVST1


EVND69 = EVST1


EVND70 = EVST1


EVND71 = EVST1


EVND72 = EVST1


EVND73 = EVST1


EVND74 = EVST1


EVND75 = EVST1


EVND76 = EVST1


EVND77 = EVST1


EVND78 = EVST1


EVND79 = EVST1


EVND80 = EVST1


EVND81 = EVST1


EVND82 = EVST1


EVND83 = EVST1


EVND84 = EVST1


EVND85 = EVST1


EVND86 = EVST1


EVND87 = EVST1


EVND88 = EVST1


EVND89 = EVST1


EVND90 = EVST1


EVND91 = EVST1


EVND92 = EVST1


EVND93 = EVST1


EVND94 = EVST1


EVND95 = EVST1


EVND96 = EVST1


EVND97 = EVST1


EVND98 = EVST1


EVND99 = EVST1


EKID01 = EWIT01


EKID02 = EWIT01


EKID03 = EWIT01


EKID04 = EWIT01


EKID05 = EWIT01


EKID06 = EWIT01


EKID07 = EWIT01


EKID08 = EWIT01


EKID09 = EWIT01


EKID010 = EWIT01


EKID011 = EWIT01


EKID012 = EWIT01


EKID013 = EWIT01


EKID014 = EWIT01


EKID015 = EWIT01


EKID016 = EWIT01


EKID017 = EWIT01


EKID018 = EWIT01


EKID019 = EWIT01


EKID020 = EWIT01


EKID021 = EWIT01


EKID022 = EWIT01


EKID023 = EWIT01


EKID024 = EWIT01


EKID025 = EWIT01


EKID026 = EWIT01


EKID027 = EWIT01


EKID028 = EWIT01


EKID029 = EWIT01


EKID030 = EWIT01


EKID031 = EWIT01


EKID032 = EWIT01


EKID033 = EWIT01


EKID034 = EWIT01


EKID035 = EWIT01


EKID036 = EWIT01


EKID037 = EWIT01


EKID038 = EWIT01


EKID039 = EWIT01


EKID040 = EWIT01


EKID041 = EWIT01


EKID042 = EWIT01


EKID043 = EWIT01


EKID044 = EWIT01


EKID045 = EWIT01


EKID046 = EWIT01


EKID047 = EWIT01


EKID048 = EWIT01


EKID049 = EWIT01


EKID050 = EWIT01


EKID051 = EWIT01


EKID052 = EWIT01


EKID053 = EWIT01


EKID054 = EWIT01


EKID055 = EWIT01


EKID056 = EWIT01


EKID057 = EWIT01


EKID058 = EWIT01


EKID059 = EWIT01


EKID060 = EWIT01


EKID061 = EWIT01


EKID062 = EWIT01


EKID063 = EWIT01


EKID064 = EWIT01


EKID065 = EWIT01


EKID066 = EWIT01


EKID067 = EWIT01


EKID068 = EWIT01


EKID069 = EWIT01


EKID070 = EWIT01


EKID071 = EWIT01


EKID072 = EWIT01


EKID073 = EWIT01


EKID074 = EWIT01


EKID075 = EWIT01


EKID076 = EWIT01


EKID077 = EWIT01


EKID078 = EWIT01


EKID079 = EWIT01


EKID080 = EWIT01


EKID081 = EWIT01


EKID082 = EWIT01


EKID083 = EWIT01


EKID084 = EWIT01


EKID085 = EWIT01


EKID086 = EWIT01


EKID087 = EWIT01


EKID088 = EWIT01


EKID089 = EWIT01


EKID090 = EWIT01


EKID091 = EWIT01


EKID092 = EWIT01


EKID093 = EWIT01


EKID094 = EWIT01


EKID095 = EWIT01


EKID096 = EWIT01


EKID097 = EWIT01


EKID098 = EWIT01


EKID099 = EWIT01


class EKID11(OrderedEnum):
    NOT_WITH_PARENTS = '0'
    WITH_PARENTS = '1'
    MISSING1 = '-1'


EKID12 = EKID11


EKID13 = EKID11


EKID14 = EKID11


EKID15 = EKID11


EKID16 = EKID11


EKID17 = EKID11


EKID18 = EKID11


EKID19 = EKID11


EKID110 = EKID11


EKID111 = EKID11


EKID112 = EKID11


EKID113 = EKID11


EKID114 = EKID11


EKID115 = EKID11


EKID116 = EKID11


EKID117 = EKID11


EKID118 = EKID11


EKID119 = EKID11


EKID120 = EKID11


EKID121 = EKID11


EKID122 = EKID11


EKID123 = EKID11


EKID124 = EKID11


EKID125 = EKID11


EKID126 = EKID11


EKID127 = EKID11


EKID128 = EKID11


EKID129 = EKID11


EKID130 = EKID11


EKID131 = EKID11


EKID132 = EKID11


EKID133 = EKID11


EKID134 = EKID11


EKID135 = EKID11


EKID136 = EKID11


EKID137 = EKID11


EKID138 = EKID11


EKID139 = EKID11


EKID140 = EKID11


EKID141 = EKID11


EKID142 = EKID11


EKID143 = EKID11


EKID144 = EKID11


EKID145 = EKID11


EKID146 = EKID11


EKID147 = EKID11


EKID148 = EKID11


EKID149 = EKID11


EKID150 = EKID11


EKID151 = EKID11


EKID152 = EKID11


EKID153 = EKID11


EKID154 = EKID11


EKID155 = EKID11


EKID156 = EKID11


EKID157 = EKID11


EKID158 = EKID11


EKID159 = EKID11


EKID160 = EKID11


EKID161 = EKID11


EKID162 = EKID11


EKID163 = EKID11


EKID164 = EKID11


EKID165 = EKID11


EKID166 = EKID11


EKID167 = EKID11


EKID168 = EKID11


EKID169 = EKID11


EKID170 = EKID11


EKID171 = EKID11


EKID172 = EKID11


EKID173 = EKID11


EKID174 = EKID11


EKID175 = EKID11


EKID176 = EKID11


EKID177 = EKID11


EKID178 = EKID11


EKID179 = EKID11


EKID180 = EKID11


EKID181 = EKID11


EKID182 = EKID11


EKID183 = EKID11


EKID184 = EKID11


EKID185 = EKID11


EKID186 = EKID11


EKID187 = EKID11


EKID188 = EKID11


EKID189 = EKID11


EKID190 = EKID11


EKID191 = EKID11


EKID192 = EKID11


EKID193 = EKID11


EKID194 = EKID11


EKID195 = EKID11


EKID196 = EKID11


EKID197 = EKID11


EKID198 = EKID11


EKID199 = EKID11


EKID21 = EWIT31


EKID22 = EWIT31


EKID23 = EWIT31


EKID24 = EWIT31


EKID25 = EWIT31


EKID26 = EWIT31


EKID27 = EWIT31


EKID28 = EWIT31


EKID29 = EWIT31


EKID210 = EWIT31


EKID211 = EWIT31


EKID212 = EWIT31


EKID213 = EWIT31


EKID214 = EWIT31


EKID215 = EWIT31


EKID216 = EWIT31


EKID217 = EWIT31


EKID218 = EWIT31


EKID219 = EWIT31


EKID220 = EWIT31


EKID221 = EWIT31


EKID222 = EWIT31


EKID223 = EWIT31


EKID224 = EWIT31


EKID225 = EWIT31


EKID226 = EWIT31


EKID227 = EWIT31


EKID228 = EWIT31


EKID229 = EWIT31


EKID230 = EWIT31


EKID231 = EWIT31


EKID232 = EWIT31


EKID233 = EWIT31


EKID234 = EWIT31


EKID235 = EWIT31


EKID236 = EWIT31


EKID237 = EWIT31


EKID238 = EWIT31


EKID239 = EWIT31


EKID240 = EWIT31


EKID241 = EWIT31


EKID242 = EWIT31


EKID243 = EWIT31


EKID244 = EWIT31


EKID245 = EWIT31


EKID246 = EWIT31


EKID247 = EWIT31


EKID248 = EWIT31


EKID249 = EWIT31


EKID250 = EWIT31


EKID251 = EWIT31


EKID252 = EWIT31


EKID253 = EWIT31


EKID254 = EWIT31


EKID255 = EWIT31


EKID256 = EWIT31


EKID257 = EWIT31


EKID258 = EWIT31


EKID259 = EWIT31


EKID260 = EWIT31


EKID261 = EWIT31


EKID262 = EWIT31


EKID263 = EWIT31


EKID264 = EWIT31


EKID265 = EWIT31


EKID266 = EWIT31


EKID267 = EWIT31


EKID268 = EWIT31


EKID269 = EWIT31


EKID270 = EWIT31


EKID271 = EWIT31


EKID272 = EWIT31


EKID273 = EWIT31


EKID274 = EWIT31


EKID275 = EWIT31


EKID276 = EWIT31


EKID277 = EWIT31


EKID278 = EWIT31


EKID279 = EWIT31


EKID280 = EWIT31


EKID281 = EWIT31


EKID282 = EWIT31


EKID283 = EWIT31


EKID284 = EWIT31


EKID285 = EWIT31


EKID286 = EWIT31


EKID287 = EWIT31


EKID288 = EWIT31


EKID289 = EWIT31


EKID290 = EWIT31


EKID291 = EWIT31


EKID292 = EWIT31


EKID293 = EWIT31


EKID294 = EWIT31


EKID295 = EWIT31


EKID296 = EWIT31


EKID297 = EWIT31


EKID298 = EWIT31


EKID299 = EWIT31


class EKID31(OrderedEnum):
    NOT_WITH_OTHER_PEOPLE_THEY_KNOW = '0'
    WITH_OTHER_PEOPLE_THEY_KNOW = '1'
    MISSING1 = '-1'


EKID32 = EKID31


EKID33 = EKID31


EKID34 = EKID31


EKID35 = EKID31


EKID36 = EKID31


EKID37 = EKID31


EKID38 = EKID31


EKID39 = EKID31


EKID310 = EKID31


EKID311 = EKID31


EKID312 = EKID31


EKID313 = EKID31


EKID314 = EKID31


EKID315 = EKID31


EKID316 = EKID31


EKID317 = EKID31


EKID318 = EKID31


EKID319 = EKID31


EKID320 = EKID31


EKID321 = EKID31


EKID322 = EKID31


EKID323 = EKID31


EKID324 = EKID31


EKID325 = EKID31


EKID326 = EKID31


EKID327 = EKID31


EKID328 = EKID31


EKID329 = EKID31


EKID330 = EKID31


EKID331 = EKID31


EKID332 = EKID31


EKID333 = EKID31


EKID334 = EKID31


EKID335 = EKID31


EKID336 = EKID31


EKID337 = EKID31


EKID338 = EKID31


EKID339 = EKID31


EKID340 = EKID31


EKID341 = EKID31


EKID342 = EKID31


EKID343 = EKID31


EKID344 = EKID31


EKID345 = EKID31


EKID346 = EKID31


EKID347 = EKID31


EKID348 = EKID31


EKID349 = EKID31


EKID350 = EKID31


EKID351 = EKID31


EKID352 = EKID31


EKID353 = EKID31


EKID354 = EKID31


EKID355 = EKID31


EKID356 = EKID31


EKID357 = EKID31


EKID358 = EKID31


EKID359 = EKID31


EKID360 = EKID31


EKID361 = EKID31


EKID362 = EKID31


EKID363 = EKID31


EKID364 = EKID31


EKID365 = EKID31


EKID366 = EKID31


EKID367 = EKID31


EKID368 = EKID31


EKID369 = EKID31


EKID370 = EKID31


EKID371 = EKID31


EKID372 = EKID31


EKID373 = EKID31


EKID374 = EKID31


EKID375 = EKID31


EKID376 = EKID31


EKID377 = EKID31


EKID378 = EKID31


EKID379 = EKID31


EKID380 = EKID31


EKID381 = EKID31


EKID382 = EKID31


EKID383 = EKID31


EKID384 = EKID31


EKID385 = EKID31


EKID386 = EKID31


EKID387 = EKID31


EKID388 = EKID31


EKID389 = EKID31


EKID390 = EKID31


EKID391 = EKID31


EKID392 = EKID31


EKID393 = EKID31


EKID394 = EKID31


EKID395 = EKID31


EKID396 = EKID31


EKID397 = EKID31


EKID398 = EKID31


EKID399 = EKID31


EKID41 = EWIT51


EKID42 = EWIT51


EKID43 = EWIT51


EKID44 = EWIT51


EKID45 = EWIT51


EKID46 = EWIT51


EKID47 = EWIT51


EKID48 = EWIT51


EKID49 = EWIT51


EKID410 = EWIT51


EKID411 = EWIT51


EKID412 = EWIT51


EKID413 = EWIT51


EKID414 = EWIT51


EKID415 = EWIT51


EKID416 = EWIT51


EKID417 = EWIT51


EKID418 = EWIT51


EKID419 = EWIT51


EKID420 = EWIT51


EKID421 = EWIT51


EKID422 = EWIT51


EKID423 = EWIT51


EKID424 = EWIT51


EKID425 = EWIT51


EKID426 = EWIT51


EKID427 = EWIT51


EKID428 = EWIT51


EKID429 = EWIT51


EKID430 = EWIT51


EKID431 = EWIT51


EKID432 = EWIT51


EKID433 = EWIT51


EKID434 = EWIT51


EKID435 = EWIT51


EKID436 = EWIT51


EKID437 = EWIT51


EKID438 = EWIT51


EKID439 = EWIT51


EKID440 = EWIT51


EKID441 = EWIT51


EKID442 = EWIT51


EKID443 = EWIT51


EKID444 = EWIT51


EKID445 = EWIT51


EKID446 = EWIT51


EKID447 = EWIT51


EKID448 = EWIT51


EKID449 = EWIT51


EKID450 = EWIT51


EKID451 = EWIT51


EKID452 = EWIT51


EKID453 = EWIT51


EKID454 = EWIT51


EKID455 = EWIT51


EKID456 = EWIT51


EKID457 = EWIT51


EKID458 = EWIT51


EKID459 = EWIT51


EKID460 = EWIT51


EKID461 = EWIT51


EKID462 = EWIT51


EKID463 = EWIT51


EKID464 = EWIT51


EKID465 = EWIT51


EKID466 = EWIT51


EKID467 = EWIT51


EKID468 = EWIT51


EKID469 = EWIT51


EKID470 = EWIT51


EKID471 = EWIT51


EKID472 = EWIT51


EKID473 = EWIT51


EKID474 = EWIT51


EKID475 = EWIT51


EKID476 = EWIT51


EKID477 = EWIT51


EKID478 = EWIT51


EKID479 = EWIT51


EKID480 = EWIT51


EKID481 = EWIT51


EKID482 = EWIT51


EKID483 = EWIT51


EKID484 = EWIT51


EKID485 = EWIT51


EKID486 = EWIT51


EKID487 = EWIT51


EKID488 = EWIT51


EKID489 = EWIT51


EKID490 = EWIT51


EKID491 = EWIT51


EKID492 = EWIT51


EKID493 = EWIT51


EKID494 = EWIT51


EKID495 = EWIT51


EKID496 = EWIT51


EKID497 = EWIT51


EKID498 = EWIT51


EKID499 = EWIT51


EKID51 = EWIT61


EKID52 = EWIT61


EKID53 = EWIT61


EKID54 = EWIT61


EKID55 = EWIT61


EKID56 = EWIT61


EKID57 = EWIT61


EKID58 = EWIT61


EKID59 = EWIT61


EKID510 = EWIT61


EKID511 = EWIT61


EKID512 = EWIT61


EKID513 = EWIT61


EKID514 = EWIT61


EKID515 = EWIT61


EKID516 = EWIT61


EKID517 = EWIT61


EKID518 = EWIT61


EKID519 = EWIT61


EKID520 = EWIT61


EKID521 = EWIT61


EKID522 = EWIT61


EKID523 = EWIT61


EKID524 = EWIT61


EKID525 = EWIT61


EKID526 = EWIT61


EKID527 = EWIT61


EKID528 = EWIT61


EKID529 = EWIT61


EKID530 = EWIT61


EKID531 = EWIT61


EKID532 = EWIT61


EKID533 = EWIT61


EKID534 = EWIT61


EKID535 = EWIT61


EKID536 = EWIT61


EKID537 = EWIT61


EKID538 = EWIT61


EKID539 = EWIT61


EKID540 = EWIT61


EKID541 = EWIT61


EKID542 = EWIT61


EKID543 = EWIT61


EKID544 = EWIT61


EKID545 = EWIT61


EKID546 = EWIT61


EKID547 = EWIT61


EKID548 = EWIT61


EKID549 = EWIT61


EKID550 = EWIT61


EKID551 = EWIT61


EKID552 = EWIT61


EKID553 = EWIT61


EKID554 = EWIT61


EKID555 = EWIT61


EKID556 = EWIT61


EKID557 = EWIT61


EKID558 = EWIT61


EKID559 = EWIT61


EKID560 = EWIT61


EKID561 = EWIT61


EKID562 = EWIT61


EKID563 = EWIT61


EKID564 = EWIT61


EKID565 = EWIT61


EKID566 = EWIT61


EKID567 = EWIT61


EKID568 = EWIT61


EKID569 = EWIT61


EKID570 = EWIT61


EKID571 = EWIT61


EKID572 = EWIT61


EKID573 = EWIT61


EKID574 = EWIT61


EKID575 = EWIT61


EKID576 = EWIT61


EKID577 = EWIT61


EKID578 = EWIT61


EKID579 = EWIT61


EKID580 = EWIT61


EKID581 = EWIT61


EKID582 = EWIT61


EKID583 = EWIT61


EKID584 = EWIT61


EKID585 = EWIT61


EKID586 = EWIT61


EKID587 = EWIT61


EKID588 = EWIT61


EKID589 = EWIT61


EKID590 = EWIT61


EKID591 = EWIT61


EKID592 = EWIT61


EKID593 = EWIT61


EKID594 = EWIT61


EKID595 = EWIT61


EKID596 = EWIT61


EKID597 = EWIT61


EKID598 = EWIT61


EKID599 = EWIT61


class DAGEGRP(OrderedEnum):
    N8__15_YRS = '1'
    N16__24_YRS = '2'
    N25__44_YRS = '3'
    N45__64_YRS = '4'
    N65_YRS_OR_MORE = '5'


class DSEX(OrderedEnum):
    MALE = '1'
    FEMALE = '2'


class DETHNIC(OrderedEnum):
    WHITE = '0'
    BLACK___CARRIBBEAN = '1'
    BLACK___AFRICAN = '2'
    BLACK___OTHER = '3'
    INDIAN = '4'
    PAKISTANI = '5'
    BANGLADESHI = '6'
    CHINESE = '7'
    NONE_OF_THESE = '8'
    DON_T_KNOW = '9'
    REFUSED = '10'
    NO_ANSWER = '11'


class DDAYW(OrderedEnum):
    WEEKDAY = '1'
    SATURDAY = '2'
    SUNDAY = '3'


class DDAYW2(OrderedEnum):
    WEEKDAY_MON___FRI = '1'
    WEEKEND_DAY = '2'


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
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


class ECONACT(OrderedEnum):
    ECON_ACTIVE___IN_EMPLOYMENT = '1'
    ECON_ACTIVE___UNEMPLOYED_ILO_DEFINITION = '2'
    ECON_INACTIVE = '3'
    ADULT___NOT_CLASSIFIABLE_BUT_EITHER_UNEMP_OR_INACTIVE = '4'
    ADULT___NOT_CLASSIFIABLE_DK_IF_EMPUNEMPINACTIVE = '5'
    UNDER_16YRS___INELIGIBLE_FOR_EMPLOYMENT_QUESTIONS = '6'
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


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
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


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
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


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
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


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
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


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
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


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
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


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
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


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
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


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
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


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
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


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
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


class NSSECB_5(OrderedEnum):
    INELIGIBLE___CHILDREN_UNDER_16_YRS = '-1'
    MANAGERIAL_AND_PROFESSIONAL_OCCS = '1'
    INTERMEDIATE_OCCS = '2'
    SMALL_EMPLOYERS_AND_OWN_ACCOUNT_WORKERS = '3'
    LOWER_SUPERVISORY_AND_TECHNICAL_OCCS = '4'
    SEMI_ROUTINE_AND_ROUTINE_OCCS = '5'
    NEVER_WORKED = '6'
    NOT_CLASSIFIABLE_EG_STUDENTS__MISSING_OCCS = '7'
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


class NSSECB_3(OrderedEnum):
    INELIGIBLE___CHILDREN_UNDER_16_YRS = '-1'
    MANAGERIAL_AND_PROFESSIONAL_OCCS = '1'
    INTERMEDIATE_OCCS = '2'
    ROUTINE_AND_MANUAL_OCCS = '3'
    NEVER_WORKED = '4'
    NOT_CLASSIFIABLE_EG_STUDENTS__MISSING_OCCS = '5'
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


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
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


class AGELEFT(OrderedEnum):
    UP_TO_14_YRS = '1'
    N15___18_YRS = '2'
    N19___25_YRS = '3'
    N26_YRS_AND_OVER = '4'
    STILL_IN_EDUCATION = '5'
    NEVER_IN_FULL_TIME_EDUCATION = '6'
    N16YRS_OR_OVER____ANSWER_MISSING = '7'
    UNDER_16YRS___INELIGIBLE_FOR_QUESTION = '8'
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


class LIVARR(OrderedEnum):
    MARRIED__AND_LIVING_WITH_SPOUSE = '1'
    COHABITING = '2'
    SINGLE_NEVER_MARRIED = '3'
    SEPARATED_BUT_STILL_MARRIED = '4'
    DIVORCED = '5'
    WIDOWED = '6'
    NO_ANSWER_DK = '7'
    UNDER_16YRS___INELIGIBLE = '8'
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


class PROVCARE(OrderedEnum):
    YES = '1'
    NO = '2'
    DKREFUSE = '3'
    NO_INFORMATION___NO_PERSON_QNRE = '999999'


class MGROUP(OrderedEnum):
    SYSTEM_MISSING = '-1'
    HIGH_INCOME_FAMILIES = '1'
    SUBURBAN_SEMIS = '2'
    BLUE_COLLAR_OWNERS = '3'
    LOW_RISE_COUNCIL = '4'
    COUNCIL_FLATS = '5'
    VICTORIAN_LOW_STATUS = '6'
    TOWN_HOUSES_AND_FLATS = '7'
    STYLISH_SINGLES = '8'
    INDEPENDENT_ELDERS = '9'
    MORTGAGED_FAMILIES = '10'
    COUNTRY_DWELLERS = '11'
    INSTITUTIONAL_AREAS = '12'
    OUTSIDE_GB = '99'


class MTYPE(OrderedEnum):
    SYSTEM_MISSING = '-1'
    CLEVER_CAPITALISTS = '1'
    RISING_MATERIALISTS = '2'
    CORPORATE_CAREERISTS = '3'
    AGEING_PROFESSIONALS = '4'
    SMALL_TIEM_BUSINESS = '5'
    GREEN_BELT_EXPANSION = '6'
    SUBURBAN_MOCK_TUDOR = '7'
    PEBBLE_DASH_SUBTOPIA = '8'
    AFFLUENT_BLUE_COLLAR = '9'
    N30S_INDUSRIAL_SPEC = '10'
    LO_RISE_RIGHT_TO_BUY = '11'
    SMOKESTACK_SHIFTWORK = '12'
    COALFIELD_LEGACY = '13'
    BETTER_OFF_COUNCIL = '14'
    LOW_RISE_PENSIONERS = '15'
    LOW_RISE_SUBSISTENCE = '16'
    PERIPHERAL_POVERTY = '17'
    FAMILIES_IN_THE_SKY = '18'
    VICTIMS_OF_CLEARANCE = '19'
    SMALL_TOWN_INDUSTRY = '20'
    MID_RISE_OVERSPILL = '21'
    FLATS_FOR_THE_AGED = '22'
    INNER_CITY_TOWERS = '23'
    BOHEMIAN_MELTING_POT = '24'
    SMARTENED_TENEMENTS = '25'
    ROOTLESS_RENTERS = '26'
    ASIAN_HEARTLANDS = '27'
    DEPOPULATED_TERRACES = '28'
    REJUVENATED_TERRACES = '29'
    BIJOU_HOMEMAKERS = '30'
    MARKET_TOWN_MIXTURE = '31'
    TOWN_CENTRE_SINGLES = '32'
    BEDSITSAND_SHOPFLATS = '33'
    STUDIO_SINGLES = '34'
    COLLEGE_ANDCOMMUNAK = '35'
    CHATTERING_CLASSES = '36'
    SOLO_PENSIONERS = '37'
    HIGH_SPENDING_GREYS = '38'
    AGED_OWNER_OCCUPIERS = '39'
    ELDERLY_IN_OWN_FLATS = '40'
    BRNAD_NEW_AREAS = '41'
    PRE_NUPTIAL_OWNERS = '42'
    NESTMAKING_FAMILIES = '43'
    MATURING_MORTGAGES = '44'
    GENTRIFIED_VILLAGES = '45'
    RURAL_RETIREMENT_MIX = '46'
    LOWLAND_AGRIBUSINESS = '47'
    RURAL_DISADVANTAGE = '48'
    TIEDTENANT_FARMERS = '49'
    UPLAND_AND_SMALL_FARMS = '50'
    MILITARY_BASES = '51'
    NON_PRIVATE_HOUSING = '52'
    OUTSIDE_GB = '99'


MGRPPC = MGROUP


MTYPEPC = MTYPE


class ISBA(OrderedEnum):
    NORTHERN_SCOTLAND = '1'
    CENTRAL_SCOTLAND = '2'
    BORDER = '3'
    NORTH_EAST = '4'
    LANCASHIRE = '5'
    YORKSHIRE = '6'
    WALES_AND_WEST = '7'
    MIDLANDS = '8'
    EAST_OF_ENGLAND = '9'
    SOUTH_WEST = '10'
    SOUTHERN = '11'
    LONDON = '12'
    MISSING1 = '-1'


class CINEMA(OrderedEnum):
    N0_TO_10KM = '1'
    N10_TO_20KM = '2'
    N20_TO_30KM = '3'
    N30_TO_40KM = '4'
    N40_TO_50KM = '5'
    N50KM_PLUS = '6'


class THEATRE(OrderedEnum):
    N0_TO_20KM = '1'
    N20_TO_40KM = '2'
    N40_TO_60KM = '3'
    N60_TO_80KM = '4'
    N80_TO_100KM = '5'
    N100KM_PLUS = '6'


class SPORT(OrderedEnum):
    N0_TO_5KM = '1'
    N5_TO_10KM = '2'
    N10_TO_15KM = '3'
    N15KM_PLUS = '4'


class SHOPPING(OrderedEnum):
    N0_TO_10KM = '1'
    N10_TO_20KM = '2'
    N20_TO_30KM = '3'
    N30KM_PLUS = '4'


GROCERY = SPORT


SCHOOL = SHOPPING


class DRY_IND(OrderedEnum):
    INCLUDE___MISSING_TIME_996PLUS997_IS_SMALLEREQUAL_90_MINUTES = '1'
    EXCLUDE___MISSING_TIME_996PLUS997_IS_GREATER__90_MINUTES = '2'
    EXCLUDE___4_EPISODES_OR_FEWER = '3'
