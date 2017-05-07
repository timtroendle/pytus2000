"""This is a auto-generated data dictionary file of the UK Time Use Study 2000."""
from enum import Enum

from pytus2000.datadicts import OrderedEnum, VariableEnum


class Variable(VariableEnum):
    SN1 = (1, " Point Number")
    SN2 = (2, " Household Number")
    SN3 = (3, " Person Number")
    WSDAY1 = (4, "Day 1 of worksheet is ....(day of week)")
    WJOB01S1 = (5, " Day 1/ First job line starts at")
    WJOB02S1 = (6, " Day 1/ Second job line starts at")
    WJOB03S1 = (7, " Day 1/ Third job line starts at")
    WJOB04S1 = (8, " Day 1/ Fourth job line starts at")
    WJOB05S1 = (9, " Day 1/ Fifth job line starts at")
    WJOB06S1 = (10, " Day 1/ Sixth job line starts at")
    WJOB07S1 = (11, " Day 1/ Seventh job line starts at")
    WJOB08S1 = (12, " Day 1/ Eighth job line starts at")
    WJOB09S1 = (13, " Day 1/ Ninth job line starts at")
    WJOB10S1 = (14, " Day 1/ Tenth job line starts at")
    WJOB11S1 = (15, " Day 1/ Eleventh job line starts at")
    WJOB12S1 = (16, " Day 1/ Twelfth job line starts at")
    WJOB13S1 = (17, " Day 1/ Thirteenth job line starts at")
    WJOB14S1 = (18, " Day 1/ Fourteenth job line starts at")
    WJOB15S1 = (19, " Day 1/ Fifteenth job line starts at")
    WJOB16S1 = (20, " Day 1/ Sixteenth job line starts at")
    WJOB01E1 = (21, " Day 1/ First job line ends at")
    WJOB02E1 = (22, " Day 1/ Second job line ends at")
    WJOB03E1 = (23, " Day 1/ Third job line ends at")
    WJOB04E1 = (24, " Day 1/ Fourth job line ends at")
    WJOB05E1 = (25, " Day 1/ Fifth job line ends at")
    WJOB06E1 = (26, " Day 1/ Sixth job line ends at")
    WJOB07E1 = (27, " Day 1/ Seventh job line ends at")
    WJOB08E1 = (28, " Day 1/ Eighth job line ends at")
    WJOB09E1 = (29, " Day 1/ Ninth job line ends at")
    WJOB10E1 = (30, " Day 1/ Tenth job line ends at")
    WJOB11E1 = (31, " Day 1/ Eleventh job line ends at")
    WJOB12E1 = (32, " Day 1/ Twelfth job line ends at")
    WJOB13E1 = (33, " Day 1/ Thirteenth job line ends at")
    WJOB14E1 = (34, " Day 1/ Fourteenth job line ends at")
    WJOB15E1 = (35, " Day 1/ Fifteenth job line ends at")
    WJOB16E1 = (36, " Day 1/ Sixteenth job line ends at")
    WJOB01S2 = (37, " Day 2/ First job line starts at")
    WJOB02S2 = (38, " Day 2/ Second job line starts at")
    WJOB03S2 = (39, " Day 2/ Third job line starts at")
    WJOB04S2 = (40, " Day 2/ Fourth job line starts at")
    WJOB05S2 = (41, " Day 2/ Fifth job line starts at")
    WJOB06S2 = (42, " Day 2/ Sixth job line starts at")
    WJOB07S2 = (43, " Day 2/ Seventh job line starts at")
    WJOB08S2 = (44, " Day 2/ Eighth job line starts at")
    WJOB09S2 = (45, " Day 2/ Ninth job line starts at")
    WJOB10S2 = (46, " Day 2/ Tenth job line starts at")
    WJOB11S2 = (47, " Day 2/ Eleventh job line starts at")
    WJOB12S2 = (48, " Day 2/ Twelfth job line starts at")
    WJOB13S2 = (49, " Day 2/ Thirteenth job line starts at")
    WJOB14S2 = (50, " Day 2/ Fourteenth job line starts at")
    WJOB15S2 = (51, " Day 2/ Fifteenth job line starts at")
    WJOB16S2 = (52, " Day 2/ Sixteenth job line starts at")
    WJOB01E2 = (53, " Day 2/ First job line ends at")
    WJOB02E2 = (54, " Day 2/ Second job line ends at")
    WJOB03E2 = (55, " Day 2/ Third job line ends at")
    WJOB04E2 = (56, " Day 2/ Fourth job line ends at")
    WJOB05E2 = (57, " Day 2/ Fifth job line ends at")
    WJOB06E2 = (58, " Day 2/ Sixth job line ends at")
    WJOB07E2 = (59, " Day 2/ Seventh job line ends at")
    WJOB08E2 = (60, " Day 2/ Eighth job line ends at")
    WJOB09E2 = (61, " Day 2/ Ninth job line ends at")
    WJOB10E2 = (62, " Day 2/ Tenth job line ends at")
    WJOB11E2 = (63, " Day 2/ Eleventh job line ends at")
    WJOB12E2 = (64, " Day 2/ Twelfth job line ends at")
    WJOB13E2 = (65, " Day 2/ Thirteenth job line ends at")
    WJOB14E2 = (66, " Day 2/ Fourteenth job line ends at")
    WJOB15E2 = (67, " Day 2/ Fifteenth job line ends at")
    WJOB16E2 = (68, " Day 2/ Sixteenth job line ends at")
    WJOB01S3 = (69, " Day 3/ First job line starts at")
    WJOB02S3 = (70, " Day 3/ Second job line starts at")
    WJOB03S3 = (71, " Day 3/ Third job line starts at")
    WJOB04S3 = (72, " Day 3/ Fourth job line starts at")
    WJOB05S3 = (73, " Day 3/ Fifth job line starts at")
    WJOB06S3 = (74, " Day 3/ Sixth job line starts at")
    WJOB07S3 = (75, " Day 3/ Seventh job line starts at")
    WJOB08S3 = (76, " Day 3/ Eighth job line starts at")
    WJOB09S3 = (77, " Day 3/ Ninth job line starts at")
    WJOB10S3 = (78, " Day 3/ Tenth job line starts at")
    WJOB11S3 = (79, " Day 3/ Eleventh job line starts at")
    WJOB12S3 = (80, " Day 3/ Twelfth job line starts at")
    WJOB13S3 = (81, " Day 3/ Thirteenth job line starts at")
    WJOB14S3 = (82, " Day 3/ Fourteenth job line starts at")
    WJOB15S3 = (83, " Day 3/ Fifteenth job line starts at")
    WJOB16S3 = (84, " Day 3/ Sixteenth job line starts at")
    WJOB01E3 = (85, " Day 3/ First job line ends at")
    WJOB02E3 = (86, " Day 3/ Second job line ends at")
    WJOB03E3 = (87, " Day 3/ Third job line ends at")
    WJOB04E3 = (88, " Day 3/ Fourth job line ends at")
    WJOB05E3 = (89, " Day 3/ Fifth job line ends at")
    WJOB06E3 = (90, " Day 3/ Sixth job line ends at")
    WJOB07E3 = (91, " Day 3/ Seventh job line ends at")
    WJOB08E3 = (92, " Day 3/ Eighth job line ends at")
    WJOB09E3 = (93, " Day 3/ Ninth job line ends at")
    WJOB10E3 = (94, " Day 3/ Tenth job line ends at")
    WJOB11E3 = (95, " Day 3/ Eleventh job line ends at")
    WJOB12E3 = (96, " Day 3/ Twelfth job line ends at")
    WJOB13E3 = (97, " Day 3/ Thirteenth job line ends at")
    WJOB14E3 = (98, " Day 3/ Fourteenth job line ends at")
    WJOB15E3 = (99, " Day 3/ Fifteenth job line ends at")
    WJOB16E3 = (100, " Day 3/ Sixteenth job line ends at")
    WJOB01S4 = (101, " Day 4/ First job line starts at")
    WJOB02S4 = (102, " Day 4/ Second job line starts at")
    WJOB03S4 = (103, " Day 4/ Third job line starts at")
    WJOB04S4 = (104, " Day 4/ Fourth job line starts at")
    WJOB05S4 = (105, " Day 4/ Fifth job line starts at")
    WJOB06S4 = (106, " Day 4/ Sixth job line starts at")
    WJOB07S4 = (107, " Day 4/ Seventh job line starts at")
    WJOB08S4 = (108, " Day 4/ Eighth job line starts at")
    WJOB09S4 = (109, " Day 4/ Ninth job line starts at")
    WJOB10S4 = (110, " Day 4/ Tenth job line starts at")
    WJOB11S4 = (111, " Day 4/ Eleventh job line starts at")
    WJOB12S4 = (112, " Day 4/ Twelfth job line starts at")
    WJOB13S4 = (113, " Day 4/ Thirteenth job line starts at")
    WJOB14S4 = (114, " Day 4/ Fourteenth job line starts at")
    WJOB15S4 = (115, " Day 4/ Fifteenth job line starts at")
    WJOB16S4 = (116, " Day 4/ Sixteenth job line starts at")
    WJOB01E4 = (117, " Day 4/ First job line ends at")
    WJOB02E4 = (118, " Day 4/ Second job line ends at")
    WJOB03E4 = (119, " Day 4/ Third job line ends at")
    WJOB04E4 = (120, " Day 4/ Fourth job line ends at")
    WJOB05E4 = (121, " Day 4/ Fifth job line ends at")
    WJOB06E4 = (122, " Day 4/ Sixth job line ends at")
    WJOB07E4 = (123, " Day 4/ Seventh job line ends at")
    WJOB08E4 = (124, " Day 4/ Eighth job line ends at")
    WJOB09E4 = (125, " Day 4/ Ninth job line ends at")
    WJOB10E4 = (126, " Day 4/ Tenth job line ends at")
    WJOB11E4 = (127, " Day 4/ Eleventh job line ends at")
    WJOB12E4 = (128, " Day 4/ Twelfth job line ends at")
    WJOB13E4 = (129, " Day 4/ Thirteenth job line ends at")
    WJOB14E4 = (130, " Day 4/ Fourteenth job line ends at")
    WJOB15E4 = (131, " Day 4/ Fifteenth job line ends at")
    WJOB16E4 = (132, " Day 4/ Sixteenth job line ends at")
    WJOB01S5 = (133, " Day 5/ First job line starts at")
    WJOB02S5 = (134, " Day 5/ Second job line starts at")
    WJOB03S5 = (135, " Day 5/ Third job line starts at")
    WJOB04S5 = (136, " Day 5/ Fourth job line starts at")
    WJOB05S5 = (137, " Day 5/ Fifth job line starts at")
    WJOB06S5 = (138, " Day 5/ Sixth job line starts at")
    WJOB07S5 = (139, " Day 5/ Seventh job line starts at")
    WJOB08S5 = (140, " Day 5/ Eighth job line starts at")
    WJOB09S5 = (141, " Day 5/ Ninth job line starts at")
    WJOB10S5 = (142, " Day 5/ Tenth job line starts at")
    WJOB11S5 = (143, " Day 5/ Eleventh job line starts at")
    WJOB12S5 = (144, " Day 5/ Twelfth job line starts at")
    WJOB13S5 = (145, " Day 5/ Thirteenth job line starts at")
    WJOB14S5 = (146, " Day 5/ Fourteenth job line starts at")
    WJOB15S5 = (147, " Day 5/ Fifteenth job line starts at")
    WJOB16S5 = (148, " Day 5/ Sixteenth job line starts at")
    WJOB01E5 = (149, " Day 5/ First job line ends at")
    WJOB02E5 = (150, " Day 5/ Second job line ends at")
    WJOB03E5 = (151, " Day 5/ Third job line ends at")
    WJOB04E5 = (152, " Day 5/ Fourth job line ends at")
    WJOB05E5 = (153, " Day 5/ Fifth job line ends at")
    WJOB06E5 = (154, " Day 5/ Sixth job line ends at")
    WJOB07E5 = (155, " Day 5/ Seventh job line ends at")
    WJOB08E5 = (156, " Day 5/ Eighth job line ends at")
    WJOB09E5 = (157, " Day 5/ Ninth job line ends at")
    WJOB10E5 = (158, " Day 5/ Tenth job line ends at")
    WJOB11E5 = (159, " Day 5/ Eleventh job line ends at")
    WJOB12E5 = (160, " Day 5/ Twelfth job line ends at")
    WJOB13E5 = (161, " Day 5/ Thirteenth job line ends at")
    WJOB14E5 = (162, " Day 5/ Fourteenth job line ends at")
    WJOB15E5 = (163, " Day 5/ Fifteenth job line ends at")
    WJOB16E5 = (164, " Day 5/ Sixteenth job line ends at")
    WJOB01S6 = (165, " Day 6/ First job line starts at")
    WJOB02S6 = (166, " Day 6/ Second job line starts at")
    WJOB03S6 = (167, " Day 6/ Third job line starts at")
    WJOB04S6 = (168, " Day 6/ Fourth job line starts at")
    WJOB05S6 = (169, " Day 6/ Fifth job line starts at")
    WJOB06S6 = (170, " Day 6/ Sixth job line starts at")
    WJOB07S6 = (171, " Day 6/ Seventh job line starts at")
    WJOB08S6 = (172, " Day 6/ Eighth job line starts at")
    WJOB09S6 = (173, " Day 6/ Ninth job line starts at")
    WJOB10S6 = (174, " Day 6/ Tenth job line starts at")
    WJOB11S6 = (175, " Day 6/ Eleventh job line starts at")
    WJOB12S6 = (176, " Day 6/ Twelfth job line starts at")
    WJOB13S6 = (177, " Day 6/ Thirteenth job line starts at")
    WJOB14S6 = (178, " Day 6/ Fourteenth job line starts at")
    WJOB15S6 = (179, " Day 6/ Fifteenth job line starts at")
    WJOB16S6 = (180, " Day 6/ Sixteenth job line starts at")
    WJOB01E6 = (181, " Day 6/ First job line ends at")
    WJOB02E6 = (182, " Day 6/ Second job line ends at")
    WJOB03E6 = (183, " Day 6/ Third job line ends at")
    WJOB04E6 = (184, " Day 6/ Fourth job line ends at")
    WJOB05E6 = (185, " Day 6/ Fifth job line ends at")
    WJOB06E6 = (186, " Day 6/ Sixth job line ends at")
    WJOB07E6 = (187, " Day 6/ Seventh job line ends at")
    WJOB08E6 = (188, " Day 6/ Eighth job line ends at")
    WJOB09E6 = (189, " Day 6/ Ninth job line ends at")
    WJOB10E6 = (190, " Day 6/ Tenth job line ends at")
    WJOB11E6 = (191, " Day 6/ Eleventh job line ends at")
    WJOB12E6 = (192, " Day 6/ Twelfth job line ends at")
    WJOB13E6 = (193, " Day 6/ Thirteenth job line ends at")
    WJOB14E6 = (194, " Day 6/ Fourteenth job line ends at")
    WJOB15E6 = (195, " Day 6/ Fifteenth job line ends at")
    WJOB16E6 = (196, " Day 6/ Sixteenth job line ends at")
    WJOB01S7 = (197, " Day 7/ First job line starts at")
    WJOB02S7 = (198, " Day 7/ Second job line starts at")
    WJOB03S7 = (199, " Day 7/ Third job line starts at")
    WJOB04S7 = (200, " Day 7/ Fourth job line starts at")
    WJOB05S7 = (201, " Day 7/ Fifth job line starts at")
    WJOB06S7 = (202, " Day 7/ Sixth job line starts at")
    WJOB07S7 = (203, " Day 7/ Seventh job line starts at")
    WJOB08S7 = (204, " Day 7/ Eighth job line starts at")
    WJOB09S7 = (205, " Day 7/ Ninth job line starts at")
    WJOB10S7 = (206, " Day 7/ Tenth job line starts at")
    WJOB11S7 = (207, " Day 7/ Eleventh job line starts at")
    WJOB12S7 = (208, " Day 7/ Twelfth job line starts at")
    WJOB13S7 = (209, " Day 7/ Thirteenth job line starts at")
    WJOB14S7 = (210, " Day 7/ Fourteenth job line starts at")
    WJOB15S7 = (211, " Day 7/ Fifteenth job line starts at")
    WJOB16S7 = (212, " Day 7/ Sixteenth job line starts at")
    WJOB01E7 = (213, " Day 7/ First job line ends at")
    WJOB02E7 = (214, " Day 7/ Second job line ends at")
    WJOB03E7 = (215, " Day 7/ Third job line ends at")
    WJOB04E7 = (216, " Day 7/ Fourth job line ends at")
    WJOB05E7 = (217, " Day 7/ Fifth job line ends at")
    WJOB06E7 = (218, " Day 7/ Sixth job line ends at")
    WJOB07E7 = (219, " Day 7/ Seventh job line ends at")
    WJOB08E7 = (220, " Day 7/ Eighth job line ends at")
    WJOB09E7 = (221, " Day 7/ Ninth job line ends at")
    WJOB10E7 = (222, " Day 7/ Tenth job line ends at")
    WJOB11E7 = (223, " Day 7/ Eleventh job line ends at")
    WJOB12E7 = (224, " Day 7/ Twelfth job line ends at")
    WJOB13E7 = (225, " Day 7/ Thirteenth job line ends at")
    WJOB14E7 = (226, " Day 7/ Fourteenth job line ends at")
    WJOB15E7 = (227, " Day 7/ Fifteenth job line ends at")
    WJOB16E7 = (228, " Day 7/ Sixteenth job line ends at")
    WOTH01S1 = (229, " Day 1/ First other paid work line starts at")
    WOTH02S1 = (230, " Day 1/ Second other paid work line starts at")
    WOTH03S1 = (231, " Day 1/ Third other paid work line starts at")
    WOTH04S1 = (232, " Day 1/ Fourth other paid work line starts at")
    WOTH05S1 = (233, " Day 1/ Fifth other paid work line starts at")
    WOTH06S1 = (234, " Day 1/ Sixth other paid work line starts at")
    WOTH07S1 = (235, " Day 1/ Seventh other paid work line starts at")
    WOTH08S1 = (236, " Day 1/ Eighth other paid work line starts at")
    WOTH09S1 = (237, " Day 1/ Ninth other paid work line starts at")
    WOTH10S1 = (238, " Day 1/ Tenth other paid work line starts at")
    WOTH11S1 = (239, " Day 1/ Eleventh other paid work line starts at")
    WOTH12S1 = (240, " Day 1/ Twelfth other paid work line starts at")
    WOTH13S1 = (241, " Day 1/ Thirteenth other paid work line starts at")
    WOTH14S1 = (242, " Day 1/ Fourteenth other paid work line starts at")
    WOTH15S1 = (243, " Day 1/ Fifteenth other paid work line starts at")
    WOTH16S1 = (244, " Day 1/ Sixteenth other paid work line starts at")
    WOTH01E1 = (245, " Day 1/ First other paid work line ends at")
    WOTH02E1 = (246, " Day 1/ Second other paid work line ends at")
    WOTH03E1 = (247, " Day 1/ Third other paid work line ends at")
    WOTH04E1 = (248, " Day 1/ Fourth other paid work line ends at")
    WOTH05E1 = (249, " Day 1/ Fifth other paid work line ends at")
    WOTH06E1 = (250, " Day 1/ Sixth other paid work line ends at")
    WOTH07E1 = (251, " Day 1/ Seventh other paid work line ends at")
    WOTH08E1 = (252, " Day 1/ Eighth other paid work line ends at")
    WOTH09E1 = (253, " Day 1/ Ninth other paid work line ends at")
    WOTH10E1 = (254, " Day 1/ Tenth other paid work line ends at")
    WOTH11E1 = (255, " Day 1/ Eleventh other paid work line ends at")
    WOTH12E1 = (256, " Day 1/ Twelfth other paid work line ends at")
    WOTH13E1 = (257, " Day 1/ Thirteenth other paid work line ends at")
    WOTH14E1 = (258, " Day 1/ Fourteenth other paid work line ends at")
    WOTH15E1 = (259, " Day 1/ Fifteenth other paid work line ends at")
    WOTH16E1 = (260, " Day 1/ Sixteenth other paid work line ends at")
    WOTH01S2 = (261, " Day 2/ First other paid work line starts at")
    WOTH02S2 = (262, " Day 2/ Second other paid work line starts at")
    WOTH03S2 = (263, " Day 2/ Third other paid work line starts at")
    WOTH04S2 = (264, " Day 2/ Fourth other paid work line starts at")
    WOTH05S2 = (265, " Day 2/ Fifth other paid work line starts at")
    WOTH06S2 = (266, " Day 2/ Sixth other paid work line starts at")
    WOTH07S2 = (267, " Day 2/ Seventh other paid work line starts at")
    WOTH08S2 = (268, " Day 2/ Eighth other paid work line starts at")
    WOTH09S2 = (269, " Day 2/ Ninth other paid work line starts at")
    WOTH10S2 = (270, " Day 2/ Tenth other paid work line starts at")
    WOTH11S2 = (271, " Day 2/ Eleventh other paid work line starts at")
    WOTH12S2 = (272, " Day 2/ Twelfth other paid work line starts at")
    WOTH13S2 = (273, " Day 2/ Thirteenth other paid work line starts at")
    WOTH14S2 = (274, " Day 2/ Fourteenth other paid work line starts at")
    WOTH15S2 = (275, " Day 2/ Fifteenth other paid work line starts at")
    WOTH16S2 = (276, " Day 2/ Sixteenth other paid work line starts at")
    WOTH01E2 = (277, " Day 2/ First other paid work line ends at")
    WOTH02E2 = (278, " Day 2/ Second other paid work line ends at")
    WOTH03E2 = (279, " Day 2/ Third other paid work line ends at")
    WOTH04E2 = (280, " Day 2/ Fourth other paid work line ends at")
    WOTH05E2 = (281, " Day 2/ Fifth other paid work line ends at")
    WOTH06E2 = (282, " Day 2/ Sixth other paid work line ends at")
    WOTH07E2 = (283, " Day 2/ Seventh other paid work line ends at")
    WOTH08E2 = (284, " Day 2/ Eighth other paid work line ends at")
    WOTH09E2 = (285, " Day 2/ Ninth other paid work line ends at")
    WOTH10E2 = (286, " Day 2/ Tenth other paid work line ends at")
    WOTH11E2 = (287, " Day 2/ Eleventh other paid work line ends at")
    WOTH12E2 = (288, " Day 2/ Twelfth other paid work line ends at")
    WOTH13E2 = (289, " Day 2/ Thirteenth other paid work line ends at")
    WOTH14E2 = (290, " Day 2/ Fourteenth other paid work line ends at")
    WOTH15E2 = (291, " Day 2/ Fifteenth other paid work line ends at")
    WOTH16E2 = (292, " Day 2/ Sixteenth other paid work line ends at")
    WOTH01S3 = (293, " Day 3/ First other paid work line starts at")
    WOTH02S3 = (294, " Day 3/ Second other paid work line starts at")
    WOTH03S3 = (295, " Day 3/ Third other paid work line starts at")
    WOTH04S3 = (296, " Day 3/ Fourth other paid work line starts at")
    WOTH05S3 = (297, " Day 3/ Fifth other paid work line starts at")
    WOTH06S3 = (298, " Day 3/ Sixth other paid work line starts at")
    WOTH07S3 = (299, " Day 3/ Seventh other paid work line starts at")
    WOTH08S3 = (300, " Day 3/ Eighth other paid work line starts at")
    WOTH09S3 = (301, " Day 3/ Ninth other paid work line starts at")
    WOTH10S3 = (302, " Day 3/ Tenth other paid work line starts at")
    WOTH11S3 = (303, " Day 3/ Eleventh other paid work line starts at")
    WOTH12S3 = (304, " Day 3/ Twelfth other paid work line starts at")
    WOTH13S3 = (305, " Day 3/ Thirteenth other paid work line starts at")
    WOTH14S3 = (306, " Day 3/ Fourteenth other paid work line starts at")
    WOTH15S3 = (307, " Day 3/ Fifteenth other paid work line starts at")
    WOTH16S3 = (308, " Day 3/ Sixteenth other paid work line starts at")
    WOTH01E3 = (309, " Day 3/ First other paid work line ends at")
    WOTH02E3 = (310, " Day 3/ Second other paid work line ends at")
    WOTH03E3 = (311, " Day 3/ Third other paid work line ends at")
    WOTH04E3 = (312, " Day 3/ Fourth other paid work line ends at")
    WOTH05E3 = (313, " Day 3/ Fifth other paid work line ends at")
    WOTH06E3 = (314, " Day 3/ Sixth other paid work line ends at")
    WOTH07E3 = (315, " Day 3/ Seventh other paid work line ends at")
    WOTH08E3 = (316, " Day 3/ Eighth other paid work line ends at")
    WOTH09E3 = (317, " Day 3/ Ninth other paid work line ends at")
    WOTH10E3 = (318, " Day 3/ Tenth other paid work line ends at")
    WOTH11E3 = (319, " Day 3/ Eleventh other paid work line ends at")
    WOTH12E3 = (320, " Day 3/ Twelfth other paid work line ends at")
    WOTH13E3 = (321, " Day 3/ Thirteenth other paid work line ends at")
    WOTH14E3 = (322, " Day 3/ Fourteenth other paid work line ends at")
    WOTH15E3 = (323, " Day 3/ Fifteenth other paid work line ends at")
    WOTH16E3 = (324, " Day 3/ Sixteenth other paid work line ends at")
    WOTH01S4 = (325, " Day 4/ First other paid work line starts at")
    WOTH02S4 = (326, " Day 4/ Second other paid work line starts at")
    WOTH03S4 = (327, " Day 4/ Third other paid work line starts at")
    WOTH04S4 = (328, " Day 4/ Fourth other paid work line starts at")
    WOTH05S4 = (329, " Day 4/ Fifth other paid work line starts at")
    WOTH06S4 = (330, " Day 4/ Sixth other paid work line starts at")
    WOTH07S4 = (331, " Day 4/ Seventh other paid work line starts at")
    WOTH08S4 = (332, " Day 4/ Eighth other paid work line starts at")
    WOTH09S4 = (333, " Day 4/ Ninth other paid work line starts at")
    WOTH10S4 = (334, " Day 4/ Tenth other paid work line starts at")
    WOTH11S4 = (335, " Day 4/ Eleventh other paid work line starts at")
    WOTH12S4 = (336, " Day 4/ Twelfth other paid work line starts at")
    WOTH13S4 = (337, " Day 4/ Thirteenth other paid work line starts at")
    WOTH14S4 = (338, " Day 4/ Fourteenth other paid work line starts at")
    WOTH15S4 = (339, " Day 4/ Fifteenth other paid work line starts at")
    WOTH16S4 = (340, " Day 4/ Sixteenth other paid work line starts at")
    WOTH01E4 = (341, " Day 4/ First other paid work line ends at")
    WOTH02E4 = (342, " Day 4/ Second other paid work line ends at")
    WOTH03E4 = (343, " Day 4/ Third other paid work line ends at")
    WOTH04E4 = (344, " Day 4/ Fourth other paid work line ends at")
    WOTH05E4 = (345, " Day 4/ Fifth other paid work line ends at")
    WOTH06E4 = (346, " Day 4/ Sixth other paid work line ends at")
    WOTH07E4 = (347, " Day 4/ Seventh other paid work line ends at")
    WOTH08E4 = (348, " Day 4/ Eighth other paid work line ends at")
    WOTH09E4 = (349, " Day 4/ Ninth other paid work line ends at")
    WOTH10E4 = (350, " Day 4/ Tenth other paid work line ends at")
    WOTH11E4 = (351, " Day 4/ Eleventh other paid work line ends at")
    WOTH12E4 = (352, " Day 4/ Twelfth other paid work line ends at")
    WOTH13E4 = (353, " Day 4/ Thirteenth other paid work line ends at")
    WOTH14E4 = (354, " Day 4/ Fourteenth other paid work line ends at")
    WOTH15E4 = (355, " Day 4/ Fifteenth other paid work line ends at")
    WOTH16E4 = (356, " Day 4/ Sixteenth other paid work line ends at")
    WOTH01S5 = (357, " Day 5/ First other paid work line starts at")
    WOTH02S5 = (358, " Day 5/ Second other paid work line starts at")
    WOTH03S5 = (359, " Day 5/ Third other paid work line starts at")
    WOTH04S5 = (360, " Day 5/ Fourth other paid work line starts at")
    WOTH05S5 = (361, " Day 5/ Fifth other paid work line starts at")
    WOTH06S5 = (362, " Day 5/ Sixth other paid work line starts at")
    WOTH07S5 = (363, " Day 5/ Seventh other paid work line starts at")
    WOTH08S5 = (364, " Day 5/ Eighth other paid work line starts at")
    WOTH09S5 = (365, " Day 5/ Ninth other paid work line starts at")
    WOTH10S5 = (366, " Day 5/ Tenth other paid work line starts at")
    WOTH11S5 = (367, " Day 5/ Eleventh other paid work line starts at")
    WOTH12S5 = (368, " Day 5/ Twelfth other paid work line starts at")
    WOTH13S5 = (369, " Day 5/ Thirteenth other paid work line starts at")
    WOTH14S5 = (370, " Day 5/ Fourteenth other paid work line starts at")
    WOTH15S5 = (371, " Day 5/ Fifteenth other paid work line starts at")
    WOTH16S5 = (372, " Day 5/ Sixteenth other paid work line starts at")
    WOTH01E5 = (373, " Day 5/ First other paid work line ends at")
    WOTH02E5 = (374, " Day 5/ Second other paid work line ends at")
    WOTH03E5 = (375, " Day 5/ Third other paid work line ends at")
    WOTH04E5 = (376, " Day 5/ Fourth other paid work line ends at")
    WOTH05E5 = (377, " Day 5/ Fifth other paid work line ends at")
    WOTH06E5 = (378, " Day 5/ Sixth other paid work line ends at")
    WOTH07E5 = (379, " Day 5/ Seventh other paid work line ends at")
    WOTH08E5 = (380, " Day 5/ Eighth other paid work line ends at")
    WOTH09E5 = (381, " Day 5/ Ninth other paid work line ends at")
    WOTH10E5 = (382, " Day 5/ Tenth other paid work line ends at")
    WOTH11E5 = (383, " Day 5/ Eleventh other paid work line ends at")
    WOTH12E5 = (384, " Day 5/ Twelfth other paid work line ends at")
    WOTH13E5 = (385, " Day 5/ Thirteenth other paid work line ends at")
    WOTH14E5 = (386, " Day 5/ Fourteenth other paid work line ends at")
    WOTH15E5 = (387, " Day 5/ Fifteenth other paid work line ends at")
    WOTH16E5 = (388, " Day 5/ Sixteenth other paid work line ends at")
    WOTH01S6 = (389, " Day 6/ First other paid work line starts at")
    WOTH02S6 = (390, " Day 6/ Second other paid work line starts at")
    WOTH03S6 = (391, " Day 6/ Third other paid work line starts at")
    WOTH04S6 = (392, " Day 6/ Fourth other paid work line starts at")
    WOTH05S6 = (393, " Day 6/ Fifth other paid work line starts at")
    WOTH06S6 = (394, " Day 6/ Sixth other paid work line starts at")
    WOTH07S6 = (395, " Day 6/ Seventh other paid work line starts at")
    WOTH08S6 = (396, " Day 6/ Eighth other paid work line starts at")
    WOTH09S6 = (397, " Day 6/ Ninth other paid work line starts at")
    WOTH10S6 = (398, " Day 6/ Tenth other paid work line starts at")
    WOTH11S6 = (399, " Day 6/ Eleventh other paid work line starts at")
    WOTH12S6 = (400, " Day 6/ Twelfth other paid work line starts at")
    WOTH13S6 = (401, " Day 6/ Thirteenth other paid work line starts at")
    WOTH14S6 = (402, " Day 6/ Fourteenth other paid work line starts at")
    WOTH15S6 = (403, " Day 6/ Fifteenth other paid work line starts at")
    WOTH16S6 = (404, " Day 6/ Sixteenth other paid work line starts at")
    WOTH01E6 = (405, " Day 6/ First other paid work line ends at")
    WOTH02E6 = (406, " Day 6/ Second other paid work line ends at")
    WOTH03E6 = (407, " Day 6/ Third other paid work line ends at")
    WOTH04E6 = (408, " Day 6/ Fourth other paid work line ends at")
    WOTH05E6 = (409, " Day 6/ Fifth other paid work line ends at")
    WOTH06E6 = (410, " Day 6/ Sixth other paid work line ends at")
    WOTH07E6 = (411, " Day 6/ Seventh other paid work line ends at")
    WOTH08E6 = (412, " Day 6/ Eighth other paid work line ends at")
    WOTH09E6 = (413, " Day 6/ Ninth other paid work line ends at")
    WOTH10E6 = (414, " Day 6/ Tenth other paid work line ends at")
    WOTH11E6 = (415, " Day 6/ Eleventh other paid work line ends at")
    WOTH12E6 = (416, " Day 6/ Twelfth other paid work line ends at")
    WOTH13E6 = (417, " Day 6/ Thirteenth other paid work line ends at")
    WOTH14E6 = (418, " Day 6/ Fourteenth other paid work line ends at")
    WOTH15E6 = (419, " Day 6/ Fifteenth other paid work line ends at")
    WOTH16E6 = (420, " Day 6/ Sixteenth other paid work line ends at")
    WOTH01S7 = (421, " Day 7/ First other paid work line starts at")
    WOTH02S7 = (422, " Day 7/ Second other paid work line starts at")
    WOTH03S7 = (423, " Day 7/ Third other paid work line starts at")
    WOTH04S7 = (424, " Day 7/ Fourth other paid work line starts at")
    WOTH05S7 = (425, " Day 7/ Fifth other paid work line starts at")
    WOTH06S7 = (426, " Day 7/ Sixth other paid work line starts at")
    WOTH07S7 = (427, " Day 7/ Seventh other paid work line starts at")
    WOTH08S7 = (428, " Day 7/ Eighth other paid work line starts at")
    WOTH09S7 = (429, " Day 7/ Ninth other paid work line starts at")
    WOTH10S7 = (430, " Day 7/ Tenth other paid work line starts at")
    WOTH11S7 = (431, " Day 7/ Eleventh other paid work line starts at")
    WOTH12S7 = (432, " Day 7/ Twelfth other paid work line starts at")
    WOTH13S7 = (433, " Day 7/ Thirteenth other paid work line starts at")
    WOTH14S7 = (434, " Day 7/ Fourteenth other paid work line starts at")
    WOTH15S7 = (435, " Day 7/ Fifteenth other paid work line starts at")
    WOTH16S7 = (436, " Day 7/ Sixteenth other paid work line starts at")
    WOTH01E7 = (437, " Day 7/ First other paid work line ends at")
    WOTH02E7 = (438, " Day 7/ Second other paid work line ends at")
    WOTH03E7 = (439, " Day 7/ Third other paid work line ends at")
    WOTH04E7 = (440, " Day 7/ Fourth other paid work line ends at")
    WOTH05E7 = (441, " Day 7/ Fifth other paid work line ends at")
    WOTH06E7 = (442, " Day 7/ Sixth other paid work line ends at")
    WOTH07E7 = (443, " Day 7/ Seventh other paid work line ends at")
    WOTH08E7 = (444, " Day 7/ Eighth other paid work line ends at")
    WOTH09E7 = (445, " Day 7/ Ninth other paid work line ends at")
    WOTH10E7 = (446, " Day 7/ Tenth other paid work line ends at")
    WOTH11E7 = (447, " Day 7/ Eleventh other paid work line ends at")
    WOTH12E7 = (448, " Day 7/ Twelfth other paid work line ends at")
    WOTH13E7 = (449, " Day 7/ Thirteenth other paid work line ends at")
    WOTH14E7 = (450, " Day 7/ Fourteenth other paid work line ends at")
    WOTH15E7 = (451, " Day 7/ Fifteenth other paid work line ends at")
    WOTH16E7 = (452, " Day 7/ Sixteenth other paid work line ends at")
    WTRV01S1 = (453, " Day 1/ First travelling at work line starts at")
    WTRV02S1 = (454, " Day 1/ Second travelling at work line starts at")
    WTRV03S1 = (455, " Day 1/ Third travelling at work line starts at")
    WTRV04S1 = (456, " Day 1/ Fourth travelling at work line starts at")
    WTRV05S1 = (457, " Day 1/ Fifth travelling at work line starts at")
    WTRV06S1 = (458, " Day 1/ Sixth travelling at work line starts at")
    WTRV07S1 = (459, " Day 1/ Seventh travelling at work line starts at")
    WTRV08S1 = (460, " Day 1/ Eighth travelling at work line starts at")
    WTRV09S1 = (461, " Day 1/ Ninth travelling at work line starts at")
    WTRV10S1 = (462, " Day 1/ Tenth travelling at work line starts at")
    WTRV11S1 = (463, " Day 1/ Eleventh travelling at work line starts at")
    WTRV12S1 = (464, " Day 1/ Twelfth travelling at work line starts at")
    WTRV13S1 = (465, " Day 1/ Thirteenth travelling at work line starts at")
    WTRV14S1 = (466, " Day 1/ Fourteenth travelling at work line starts at")
    WTRV15S1 = (467, " Day 1/ Fifteenth travelling at work line starts at")
    WTRV16S1 = (468, " Day 1/ Sixteenth travelling at work line starts at")
    WTRV01E1 = (469, " Day 1/ First travelling at work line ends at")
    WTRV02E1 = (470, " Day 1/ Second travelling at work line ends at")
    WTRV03E1 = (471, " Day 1/ Third travelling at work line ends at")
    WTRV04E1 = (472, " Day 1/ Fourth travelling at work line ends at")
    WTRV05E1 = (473, " Day 1/ Fifth travelling at work line ends at")
    WTRV06E1 = (474, " Day 1/ Sixth travelling at work line ends at")
    WTRV07E1 = (475, " Day 1/ Seventh travelling at work line ends at")
    WTRV08E1 = (476, " Day 1/ Eighth travelling at work line ends at")
    WTRV09E1 = (477, " Day 1/ Ninth travelling at work line ends at")
    WTRV10E1 = (478, " Day 1/ Tenth travelling at work line ends at")
    WTRV11E1 = (479, " Day 1/ Eleventh travelling at work line ends at")
    WTRV12E1 = (480, " Day 1/ Twelfth travelling at work line ends at")
    WTRV13E1 = (481, " Day 1/ Thirteenth travelling at work line ends at")
    WTRV14E1 = (482, " Day 1/ Fourteenth travelling at work line ends at")
    WTRV15E1 = (483, " Day 1/ Fifteenth travelling at work line ends at")
    WTRV16E1 = (484, " Day 1/ Sixteenth travelling at work line ends at")
    WTRV01S2 = (485, " Day 2/ First travelling at work line starts at")
    WTRV02S2 = (486, " Day 2/ Second travelling at work line starts at")
    WTRV03S2 = (487, " Day 2/ Third travelling at work line starts at")
    WTRV04S2 = (488, " Day 2/ Fourth travelling at work line starts at")
    WTRV05S2 = (489, " Day 2/ Fifth travelling at work line starts at")
    WTRV06S2 = (490, " Day 2/ Sixth travelling at work line starts at")
    WTRV07S2 = (491, " Day 2/ Seventh travelling at work line starts at")
    WTRV08S2 = (492, " Day 2/ Eighth travelling at work line starts at")
    WTRV09S2 = (493, " Day 2/ Ninth travelling at work line starts at")
    WTRV10S2 = (494, " Day 2/ Tenth travelling at work line starts at")
    WTRV11S2 = (495, " Day 2/ Eleventh travelling at work line starts at")
    WTRV12S2 = (496, " Day 2/ Twelfth travelling at work line starts at")
    WTRV13S2 = (497, " Day 2/ Thirteenth travelling at work line starts at")
    WTRV14S2 = (498, " Day 2/ Fourteenth travelling at work line starts at")
    WTRV15S2 = (499, " Day 2/ Fifteenth travelling at work line starts at")
    WTRV16S2 = (500, " Day 2/ Sixteenth travelling at work line starts at")
    WTRV01E2 = (501, " Day 2/ First travelling at work line ends at")
    WTRV02E2 = (502, " Day 2/ Second travelling at work line ends at")
    WTRV03E2 = (503, " Day 2/ Third travelling at work line ends at")
    WTRV04E2 = (504, " Day 2/ Fourth travelling at work line ends at")
    WTRV05E2 = (505, " Day 2/ Fifth travelling at work line ends at")
    WTRV06E2 = (506, " Day 2/ Sixth travelling at work line ends at")
    WTRV07E2 = (507, " Day 2/ Seventh travelling at work line ends at")
    WTRV08E2 = (508, " Day 2/ Eighth travelling at work line ends at")
    WTRV09E2 = (509, " Day 2/ Ninth travelling at work line ends at")
    WTRV10E2 = (510, " Day 2/ Tenth travelling at work line ends at")
    WTRV11E2 = (511, " Day 2/ Eleventh travelling at work line ends at")
    WTRV12E2 = (512, " Day 2/ Twelfth travelling at work line ends at")
    WTRV13E2 = (513, " Day 2/ Thirteenth travelling at work line ends at")
    WTRV14E2 = (514, " Day 2/ Fourteenth travelling at work line ends at")
    WTRV15E2 = (515, " Day 2/ Fifteenth travelling at work line ends at")
    WTRV16E2 = (516, " Day 2/ Sixteenth travelling at work line ends at")
    WTRV01S3 = (517, " Day 3/ First travelling at work line starts at")
    WTRV02S3 = (518, " Day 3/ Second travelling at work line starts at")
    WTRV03S3 = (519, " Day 3/ Third travelling at work line starts at")
    WTRV04S3 = (520, " Day 3/ Fourth travelling at work line starts at")
    WTRV05S3 = (521, " Day 3/ Fifth travelling at work line starts at")
    WTRV06S3 = (522, " Day 3/ Sixth travelling at work line starts at")
    WTRV07S3 = (523, " Day 3/ Seventh travelling at work line starts at")
    WTRV08S3 = (524, " Day 3/ Eighth travelling at work line starts at")
    WTRV09S3 = (525, " Day 3/ Ninth travelling at work line starts at")
    WTRV10S3 = (526, " Day 3/ Tenth travelling at work line starts at")
    WTRV11S3 = (527, " Day 3/ Eleventh travelling at work line starts at")
    WTRV12S3 = (528, " Day 3/ Twelfth travelling at work line starts at")
    WTRV13S3 = (529, " Day 3/ Thirteenth travelling at work line starts at")
    WTRV14S3 = (530, " Day 3/ Fourteenth travelling at work line starts at")
    WTRV15S3 = (531, " Day 3/ Fifteenth travelling at work line starts at")
    WTRV16S3 = (532, " Day 3/ Sixteenth travelling at work line starts at")
    WTRV01E3 = (533, " Day 3/ First travelling at work line ends at")
    WTRV02E3 = (534, " Day 3/ Second travelling at work line ends at")
    WTRV03E3 = (535, " Day 3/ Third travelling at work line ends at")
    WTRV04E3 = (536, " Day 3/ Fourth travelling at work line ends at")
    WTRV05E3 = (537, " Day 3/ Fifth travelling at work line ends at")
    WTRV06E3 = (538, " Day 3/ Sixth travelling at work line ends at")
    WTRV07E3 = (539, " Day 3/ Seventh travelling at work line ends at")
    WTRV08E3 = (540, " Day 3/ Eighth travelling at work line ends at")
    WTRV09E3 = (541, " Day 3/ Ninth travelling at work line ends at")
    WTRV10E3 = (542, " Day 3/ Tenth travelling at work line ends at")
    WTRV11E3 = (543, " Day 3/ Eleventh travelling at work line ends at")
    WTRV12E3 = (544, " Day 3/ Twelfth travelling at work line ends at")
    WTRV13E3 = (545, " Day 3/ Thirteenth travelling at work line ends at")
    WTRV14E3 = (546, " Day 3/ Fourteenth travelling at work line ends at")
    WTRV15E3 = (547, " Day 3/ Fifteenth travelling at work line ends at")
    WTRV16E3 = (548, " Day 3/ Sixteenth travelling at work line ends at")
    WTRV01S4 = (549, " Day 4/ First travelling at work line starts at")
    WTRV02S4 = (550, " Day 4/ Second travelling at work line starts at")
    WTRV03S4 = (551, " Day 4/ Third travelling at work line starts at")
    WTRV04S4 = (552, " Day 4/ Fourth travelling at work line starts at")
    WTRV05S4 = (553, " Day 4/ Fifth travelling at work line starts at")
    WTRV06S4 = (554, " Day 4/ Sixth travelling at work line starts at")
    WTRV07S4 = (555, " Day 4/ Seventh travelling at work line starts at")
    WTRV08S4 = (556, " Day 4/ Eighth travelling at work line starts at")
    WTRV09S4 = (557, " Day 4/ Ninth travelling at work line starts at")
    WTRV10S4 = (558, " Day 4/ Tenth travelling at work line starts at")
    WTRV11S4 = (559, " Day 4/ Eleventh travelling at work line starts at")
    WTRV12S4 = (560, " Day 4/ Twelfth travelling at work line starts at")
    WTRV13S4 = (561, " Day 4/ Thirteenth travelling at work line starts at")
    WTRV14S4 = (562, " Day 4/ Fourteenth travelling at work line starts at")
    WTRV15S4 = (563, " Day 4/ Fifteenth travelling at work line starts at")
    WTRV16S4 = (564, " Day 4/ Sixteenth travelling at work line starts at")
    WTRV01E4 = (565, " Day 4/ First travelling at work line ends at")
    WTRV02E4 = (566, " Day 4/ Second travelling at work line ends at")
    WTRV03E4 = (567, " Day 4/ Third travelling at work line ends at")
    WTRV04E4 = (568, " Day 4/ Fourth travelling at work line ends at")
    WTRV05E4 = (569, " Day 4/ Fifth travelling at work line ends at")
    WTRV06E4 = (570, " Day 4/ Sixth travelling at work line ends at")
    WTRV07E4 = (571, " Day 4/ Seventh travelling at work line ends at")
    WTRV08E4 = (572, " Day 4/ Eighth travelling at work line ends at")
    WTRV09E4 = (573, " Day 4/ Ninth travelling at work line ends at")
    WTRV10E4 = (574, " Day 4/ Tenth travelling at work line ends at")
    WTRV11E4 = (575, " Day 4/ Eleventh travelling at work line ends at")
    WTRV12E4 = (576, " Day 4/ Twelfth travelling at work line ends at")
    WTRV13E4 = (577, " Day 4/ Thirteenth travelling at work line ends at")
    WTRV14E4 = (578, " Day 4/ Fourteenth travelling at work line ends at")
    WTRV15E4 = (579, " Day 4/ Fifteenth travelling at work line ends at")
    WTRV16E4 = (580, " Day 4/ Sixteenth travelling at work line ends at")
    WTRV01S5 = (581, " Day 5/ First travelling at work line starts at")
    WTRV02S5 = (582, " Day 5/ Second travelling at work line starts at")
    WTRV03S5 = (583, " Day 5/ Third travelling at work line starts at")
    WTRV04S5 = (584, " Day 5/ Fourth travelling at work line starts at")
    WTRV05S5 = (585, " Day 5/ Fifth travelling at work line starts at")
    WTRV06S5 = (586, " Day 5/ Sixth travelling at work line starts at")
    WTRV07S5 = (587, " Day 5/ Seventh travelling at work line starts at")
    WTRV08S5 = (588, " Day 5/ Eighth travelling at work line starts at")
    WTRV09S5 = (589, " Day 5/ Ninth travelling at work line starts at")
    WTRV10S5 = (590, " Day 5/ Tenth travelling at work line starts at")
    WTRV11S5 = (591, " Day 5/ Eleventh travelling at work line starts at")
    WTRV12S5 = (592, " Day 5/ Twelfth travelling at work line starts at")
    WTRV13S5 = (593, " Day 5/ Thirteenth travelling at work line starts at")
    WTRV14S5 = (594, " Day 5/ Fourteenth travelling at work line starts at")
    WTRV15S5 = (595, " Day 5/ Fifteenth travelling at work line starts at")
    WTRV16S5 = (596, " Day 5/ Sixteenth travelling at work line starts at")
    WTRV01E5 = (597, " Day 5/ First travelling at work line ends at")
    WTRV02E5 = (598, " Day 5/ Second travelling at work line ends at")
    WTRV03E5 = (599, " Day 5/ Third travelling at work line ends at")
    WTRV04E5 = (600, " Day 5/ Fourth travelling at work line ends at")
    WTRV05E5 = (601, " Day 5/ Fifth travelling at work line ends at")
    WTRV06E5 = (602, " Day 5/ Sixth travelling at work line ends at")
    WTRV07E5 = (603, " Day 5/ Seventh travelling at work line ends at")
    WTRV08E5 = (604, " Day 5/ Eighth travelling at work line ends at")
    WTRV09E5 = (605, " Day 5/ Ninth travelling at work line ends at")
    WTRV10E5 = (606, " Day 5/ Tenth travelling at work line ends at")
    WTRV11E5 = (607, " Day 5/ Eleventh travelling at work line ends at")
    WTRV12E5 = (608, " Day 5/ Twelfth travelling at work line ends at")
    WTRV13E5 = (609, " Day 5/ Thirteenth travelling at work line ends at")
    WTRV14E5 = (610, " Day 5/ Fourteenth travelling at work line ends at")
    WTRV15E5 = (611, " Day 5/ Fifteenth travelling at work line ends at")
    WTRV16E5 = (612, " Day 5/ Sixteenth travelling at work line ends at")
    WTRV01S6 = (613, " Day 6/ First travelling at work line starts at")
    WTRV02S6 = (614, " Day 6/ Second travelling at work line starts at")
    WTRV03S6 = (615, " Day 6/ Third travelling at work line starts at")
    WTRV04S6 = (616, " Day 6/ Fourth travelling at work line starts at")
    WTRV05S6 = (617, " Day 6/ Fifth travelling at work line starts at")
    WTRV06S6 = (618, " Day 6/ Sixth travelling at work line starts at")
    WTRV07S6 = (619, " Day 6/ Seventh travelling at work line starts at")
    WTRV08S6 = (620, " Day 6/ Eighth travelling at work line starts at")
    WTRV09S6 = (621, " Day 6/ Ninth travelling at work line starts at")
    WTRV10S6 = (622, " Day 6/ Tenth travelling at work line starts at")
    WTRV11S6 = (623, " Day 6/ Eleventh travelling at work line starts at")
    WTRV12S6 = (624, " Day 6/ Twelfth travelling at work line starts at")
    WTRV13S6 = (625, " Day 6/ Thirteenth travelling at work line starts at")
    WTRV14S6 = (626, " Day 6/ Fourteenth travelling at work line starts at")
    WTRV15S6 = (627, " Day 6/ Fifteenth travelling at work line starts at")
    WTRV16S6 = (628, " Day 6/ Sixteenth travelling at work line starts at")
    WTRV01E6 = (629, " Day 6/ First travelling at work line ends at")
    WTRV02E6 = (630, " Day 6/ Second travelling at work line ends at")
    WTRV03E6 = (631, " Day 6/ Third travelling at work line ends at")
    WTRV04E6 = (632, " Day 6/ Fourth travelling at work line ends at")
    WTRV05E6 = (633, " Day 6/ Fifth travelling at work line ends at")
    WTRV06E6 = (634, " Day 6/ Sixth travelling at work line ends at")
    WTRV07E6 = (635, " Day 6/ Seventh travelling at work line ends at")
    WTRV08E6 = (636, " Day 6/ Eighth travelling at work line ends at")
    WTRV09E6 = (637, " Day 6/ Ninth travelling at work line ends at")
    WTRV10E6 = (638, " Day 6/ Tenth travelling at work line ends at")
    WTRV11E6 = (639, " Day 6/ Eleventh travelling at work line ends at")
    WTRV12E6 = (640, " Day 6/ Twelfth travelling at work line ends at")
    WTRV13E6 = (641, " Day 6/ Thirteenth travelling at work line ends at")
    WTRV14E6 = (642, " Day 6/ Fourteenth travelling at work line ends at")
    WTRV15E6 = (643, " Day 6/ Fifteenth travelling at work line ends at")
    WTRV16E6 = (644, " Day 6/ Sixteenth travelling at work line ends at")
    WTRV01S7 = (645, " Day 7/ First travelling at work line starts at")
    WTRV02S7 = (646, " Day 7/ Second travelling at work line starts at")
    WTRV03S7 = (647, " Day 7/ Third travelling at work line starts at")
    WTRV04S7 = (648, " Day 7/ Fourth travelling at work line starts at")
    WTRV05S7 = (649, " Day 7/ Fifth travelling at work line starts at")
    WTRV06S7 = (650, " Day 7/ Sixth travelling at work line starts at")
    WTRV07S7 = (651, " Day 7/ Seventh travelling at work line starts at")
    WTRV08S7 = (652, " Day 7/ Eighth travelling at work line starts at")
    WTRV09S7 = (653, " Day 7/ Ninth travelling at work line starts at")
    WTRV10S7 = (654, " Day 7/ Tenth travelling at work line starts at")
    WTRV11S7 = (655, " Day 7/ Eleventh travelling at work line starts at")
    WTRV12S7 = (656, " Day 7/ Twelfth travelling at work line starts at")
    WTRV13S7 = (657, " Day 7/ Thirteenth travelling at work line starts at")
    WTRV14S7 = (658, " Day 7/ Fourteenth travelling at work line starts at")
    WTRV15S7 = (659, " Day 7/ Fifteenth travelling at work line starts at")
    WTRV16S7 = (660, " Day 7/ Sixteenth travelling at work line starts at")
    WTRV01E7 = (661, " Day 7/ First travelling at work line ends at")
    WTRV02E7 = (662, " Day 7/ Second travelling at work line ends at")
    WTRV03E7 = (663, " Day 7/ Third travelling at work line ends at")
    WTRV04E7 = (664, " Day 7/ Fourth travelling at work line ends at")
    WTRV05E7 = (665, " Day 7/ Fifth travelling at work line ends at")
    WTRV06E7 = (666, " Day 7/ Sixth travelling at work line ends at")
    WTRV07E7 = (667, " Day 7/ Seventh travelling at work line ends at")
    WTRV08E7 = (668, " Day 7/ Eighth travelling at work line ends at")
    WTRV09E7 = (669, " Day 7/ Ninth travelling at work line ends at")
    WTRV10E7 = (670, " Day 7/ Tenth travelling at work line ends at")
    WTRV11E7 = (671, " Day 7/ Eleventh travelling at work line ends at")
    WTRV12E7 = (672, " Day 7/ Twelfth travelling at work line ends at")
    WTRV13E7 = (673, " Day 7/ Thirteenth travelling at work line ends at")
    WTRV14E7 = (674, " Day 7/ Fourteenth travelling at work line ends at")
    WTRV15E7 = (675, " Day 7/ Fifteenth travelling at work line ends at")
    WTRV16E7 = (676, " Day 7/ Sixteenth travelling at work line ends at")
    WTRV1 = (677, " Day 1/ Main Mode of Travel")
    WTRV2 = (678, " Day 2/ Main Mode of Travel")
    WTRV3 = (679, " Day 3/ Main Mode of Travel")
    WTRV4 = (680, " Day 4/ Main Mode of Travel")
    WTRV5 = (681, " Day 5/ Main Mode of Travel")
    WTRV6 = (682, " Day 6/ Main Mode of Travel")
    WTRV7 = (683, " Day 7/ Main Mode of Travel")
    W_IND = (684, "Worksheet indicator field - no work or education in 7 days, worksheet BLANK")
    TOTJOB1 = (685, "Total time in MAIN job/ full-time education - Day 1 of worksheet (mins)")
    TOTJOB2 = (686, "Total time in MAIN job/ full-time education - Day 2 of worksheet (mins)")
    TOTJOB3 = (687, "Total time in MAIN job/ full-time education - Day 3 of worksheet (mins)")
    TOTJOB4 = (688, "Total time in MAIN job/ full-time education - Day 4 of worksheet (mins)")
    TOTJOB5 = (689, "Total time in MAIN job/ full-time education - Day 5 of worksheet (mins)")
    TOTJOB6 = (690, "Total time in MAIN job/ full-time education - Day 6 of worksheet (mins)")
    TOTJOB7 = (691, "Total time in MAIN job/ full-time education - Day 7 of worksheet (mins)")
    TOTJOBWK = (692, "Total time in MAIN job/ full-time education - whole week of worksheet (mins)")
    WD1_IND = (693, "Indicator field - ANY time spent on MAIN job/ education on day 1 ?")
    WD2_IND = (694, "Indicator field - ANY time spent on MAIN job/ education on day 2 ?")
    WD3_IND = (695, "Indicator field - ANY time spent on MAIN job/ education on day 3 ?")
    WD4_IND = (696, "Indicator field - ANY time spent on MAIN job/ education on day 4 ?")
    WD5_IND = (697, "Indicator field - ANY time spent on MAIN job/ education on day 5 ?")
    WD6_IND = (698, "Indicator field - ANY time spent on MAIN job/ education on day 6 ?")
    WD7_IND = (699, "Indicator field - ANY time spent on MAIN job/ education on day 7 ?")
    TOTOTH1 = (700, "Total time in OTHER PAID WORK - Day 1 of worksheet (mins)")
    TOTOTH2 = (701, "Total time in OTHER PAID WORK - Day 2 of worksheet (mins)")
    TOTOTH3 = (702, "Total time in OTHER PAID WORK - Day 3 of worksheet (mins)")
    TOTOTH4 = (703, "Total time in OTHER PAID WORK - Day 4 of worksheet (mins)")
    TOTOTH5 = (704, "Total time in OTHER PAID WORK - Day 5 of worksheet (mins)")
    TOTOTH6 = (705, "Total time in OTHER PAID WORK - Day 6 of worksheet (mins)")
    TOTOTH7 = (706, "Total time in OTHER PAID WORK - Day 7 of worksheet (mins)")
    TOTOTHWK = (707, "Total time in OTHER PAID WORK - whole week of worksheet (mins)")
    TOTALLWK = (708, "Total time in ALL JOBS/ EDUCATION: MAIN + OTHER PAID WORK (mins)")
    TOTTRV1 = (709, "Travel while AT work - total time for day 1 of worksheet (mins)")
    TOTTRV2 = (710, "Travel while AT work - total time for day 2 of worksheet (mins)")
    TOTTRV3 = (711, "Travel while AT work - total time for day 3 of worksheet (mins)")
    TOTTRV4 = (712, "Travel while AT work - total time for day 4 of worksheet (mins)")
    TOTTRV5 = (713, "Travel while AT work - total time for day 5 of worksheet (mins)")
    TOTTRV6 = (714, "Travel while AT work - total time for day 6 of worksheet (mins)")
    TOTTRV7 = (715, "Travel while AT work - total time for day 7 of worksheet (mins)")
    TOTTRVWK = (716, "Travel while AT work - total time for whole week of worksheet (mins)")
    HAGE = (717, "Age (as given in hhld qnre)")
    HSEX = (718, "Sex (as given in hhld qnre)")
    HAGEGRP = (719, "Age group")
    HDAY = (720, "Day of household interview")
    HMONTH = (721, "Month of household interview")
    HYEAR = (722, "Year of household interview")
    GORPAF = (723, "Government Office Region")
    GORPAF2 = (724, "Govn Office Region - 8 categories")
    GORPAF3 = (725, "Govn Office Region - 4 countries")
    POP_DEN = (726, "Population density (persons per 10 hectares - uses 1991 Census data for postcode sector)")
    POP_DEN2 = (727, "Population density - banded (persons per 10 hectares)")
    UNEMP = (728, "Unemployment rate (%) - uses 1991 Census data for postcode sector")
    UNEMP2 = (729, "Unemployment rate - percentage banded")
    HNUMB = (730, "Number of people in household (all ages)")
    NUMADULT = (731, "Number of adults   (16 yrs or more) in hhld")
    NUMCHILD = (732, "Number of children (15 yrs or less) in hhld")
    CHILD = (733, "Whether child (15yrs or less) in household or not")
    AGEYNGST = (734, "Age of youngest person in household")
    NUM0_2 = (735, "Number aged 0 - 2 yrs in hhld")
    NUM3_4 = (736, "Number aged 3 - 4 yrs in hhld")
    NUM5_9 = (737, "Number aged 5 - 9 yrs in hhld")
    NUM10_15 = (738, "Number aged 10 - 15 yrs in hhld")
    NUM16_17 = (739, "Number aged 16 - 17yrs")
    HRP_PER = (740, "Household Reference Person - person number")
    SPOUSE1 = (741, "For hhlds with one marr/cohab couple - person number of FIRST spouse")
    SPOUSE2 = (742, "For hhlds with one marr/cohab couple - person number of SECOND spouse")
    TENURE2 = (743, "Tenure - grouped")
    CARAVAIL = (744, "Whether household owns/ has continuous use of car, motor bike or other motor vehicle")
    GROSHINC = (745, "Household Income band (gross ie before deductions) - per year (source: hhld qstn 10b)")
    HHTYPE4 = (746, "Household type - main variable for hhld type (16 categories)")
    HHTYPE5 = (747, "Household type - 8 categories")
    MANAGE2 = (748, "Management responsibilities (of economically active & employed)")
    ECONACT = (749, "Economic activity")
    ECONACT3 = (750, "Economic activity - 3")
    EMPINCBD = (751, "Employee - Net MONTHLY income - Banded (sources: Q10 & Q11a)")
    SEINCBD = (752, "Self-employed - Net MONTHLY income - Banded (sources: Q13c & Q13d)")
    TOTPINC = (753, "Total net monthly personal income (for employees & self-employed together)")
    HRS_UNPD = (754, "Total weekly hours UNPAID work in own/ relatives's business (copy of Q14a)")
    HRS_JOB1 = (755, "Total weekly hours usually worked in MAIN job (incl paid & unpaid overtime) by people in paid work (employed or self-employed)")
    HRS_JOB2 = (756, "Total weekly hours usually worked in SECOND job (copy of Q16F)")
    HRS_TOT = (757, "Total hours usually worked per week: unpaid work for own/rel business + main job + second job combined")
    HRS_GRP = (758, "Total weekly hours usually worked - paid work (main + 2nd job) or unpaid work - banded")
    SIC = (759, "Standard Industrial Classification 1992 (4-digit) - for respondent's MAIN JOB")
    SOC = (760, "Standard Occupational Classification 2000 for respondent's MAIN JOB")
    SIC2 = (761, "Standard Industrial Classification 1992 (4-digit) - for respondent's SECOND JOB")
    SOC2 = (762, "Standard Occupational Classification 2000 for respondent's SECOND JOB")
    NSSECB = (763, "National Statistics Socio-Economic Classification")
    NSSECB_8 = (764, "NS Socio-Economic Classification - 8 classes")
    NSSECB_5 = (765, "NS Socio-Economic Classification - 5 classes")
    NSSECB_3 = (766, "NS Socio-Economic Classification - 3 classes")
    HIQUAL4 = (767, "Highest qualification gained - HARMONISED DEFINITION")
    AGELEFT = (768, " Age left full-time education - grouped")
    LIVARR = (769, "Living arrangements (as reported by respondent at q55 & q56 - NOT based on relationships in hhld grid )")
    PROVCARE = (770, "Q45 & Q47: Do you look after any sick/ disabled/ elderly person (either living with you or not living with you)?")
    WTWRK_GR = (771, "Worksheet weight - for grossing to UK population aged 8yrs or more")
    WTWRK_UG = (772, "Worksheet weight - ungrossed")


class WSDAY1(OrderedEnum):
    MONDAY = '1'
    TUESDAY = '2'
    WEDNESDAY = '3'
    THURSDAY = '4'
    FRIDAY = '5'
    SATURDAY = '6'
    SUNDAY = '7'


class WJOB01S1(OrderedEnum):
    _401_415 = '1'
    _416_430 = '2'
    _431_445 = '3'
    _446_500 = '4'
    _501_515 = '5'
    _516_530 = '6'
    _531_545 = '7'
    _546_600 = '8'
    _601_615 = '9'
    _616_630 = '10'
    _631_645 = '11'
    _646_700 = '12'
    _701_715 = '13'
    _716_730 = '14'
    _731_745 = '15'
    _746_800 = '16'
    _801_815 = '17'
    _816_830 = '18'
    _831_845 = '19'
    _846_900 = '20'
    _901_915 = '21'
    _916_930 = '22'
    _931_945 = '23'
    _946_1000 = '24'
    _1001_1015 = '25'
    _1016_1030 = '26'
    _1031_1045 = '27'
    _1046_1100 = '28'
    _1101_1115 = '29'
    _1116_1130 = '30'
    _1131_1145 = '31'
    _1146_1200 = '32'
    _1201_1215 = '33'
    _1216_1230 = '34'
    _1231_1245 = '35'
    _1246_1300 = '36'
    _1301_1315 = '37'
    _1316_1330 = '38'
    _1331_1345 = '39'
    _1346_1400 = '40'
    _1401_1415 = '41'
    _1416_1430 = '42'
    _1431_1445 = '43'
    _1446_1500 = '44'
    _1501_1515 = '45'
    _1516_1530 = '46'
    _1531_1545 = '47'
    _1546_1600 = '48'
    _1601_1615 = '49'
    _1616_1630 = '50'
    _1631_1645 = '51'
    _1646_1700 = '52'
    _1701_1715 = '53'
    _1716_1730 = '54'
    _1731_1745 = '55'
    _1746_1800 = '56'
    _1801_1815 = '57'
    _1816_1830 = '58'
    _1831_1845 = '59'
    _1846_1900 = '60'
    _1901_1915 = '61'
    _1916_1930 = '62'
    _1931_1945 = '63'
    _1946_2000 = '64'
    _2001_2015 = '65'
    _2016_2030 = '66'
    _2031_2045 = '67'
    _2046_2100 = '68'
    _2101_2115 = '69'
    _2116_2130 = '70'
    _2131_2145 = '71'
    _2146_2200 = '72'
    _2201_2215 = '73'
    _2216_2230 = '74'
    _2231_2245 = '75'
    _2246_2300 = '76'
    _2301_2315 = '77'
    _2316_2330 = '78'
    _2331_2345 = '79'
    _2346_000 = '80'
    _001_015 = '81'
    _016_030 = '82'
    _031_045 = '83'
    _046_100 = '84'
    _101_115 = '85'
    _116_130 = '86'
    _131_145 = '87'
    _146_200 = '88'
    _201_215 = '89'
    _216_230 = '90'
    _231_245 = '91'
    _246_300 = '92'
    _301_315 = '93'
    _316_330 = '94'
    _331_345 = '95'
    _346_400 = '96'


WJOB02S1 = WJOB01S1


WJOB03S1 = WJOB01S1


WJOB04S1 = WJOB01S1


WJOB05S1 = WJOB01S1


WJOB06S1 = WJOB01S1


WJOB07S1 = WJOB01S1


WJOB08S1 = WJOB01S1


WJOB09S1 = WJOB01S1


WJOB10S1 = WJOB01S1


WJOB11S1 = WJOB01S1


WJOB12S1 = WJOB01S1


WJOB13S1 = WJOB01S1


WJOB14S1 = WJOB01S1


WJOB15S1 = WJOB01S1


WJOB16S1 = WJOB01S1


WJOB01E1 = WJOB01S1


WJOB02E1 = WJOB01S1


WJOB03E1 = WJOB01S1


WJOB04E1 = WJOB01S1


WJOB05E1 = WJOB01S1


WJOB06E1 = WJOB01S1


WJOB07E1 = WJOB01S1


WJOB08E1 = WJOB01S1


WJOB09E1 = WJOB01S1


WJOB10E1 = WJOB01S1


WJOB11E1 = WJOB01S1


WJOB12E1 = WJOB01S1


WJOB13E1 = WJOB01S1


WJOB14E1 = WJOB01S1


WJOB15E1 = WJOB01S1


WJOB16E1 = WJOB01S1


WJOB01S2 = WJOB01S1


WJOB02S2 = WJOB01S1


WJOB03S2 = WJOB01S1


WJOB04S2 = WJOB01S1


WJOB05S2 = WJOB01S1


WJOB06S2 = WJOB01S1


WJOB07S2 = WJOB01S1


WJOB08S2 = WJOB01S1


WJOB09S2 = WJOB01S1


WJOB10S2 = WJOB01S1


WJOB11S2 = WJOB01S1


WJOB12S2 = WJOB01S1


WJOB13S2 = WJOB01S1


WJOB14S2 = WJOB01S1


WJOB15S2 = WJOB01S1


WJOB16S2 = WJOB01S1


WJOB01E2 = WJOB01S1


WJOB02E2 = WJOB01S1


WJOB03E2 = WJOB01S1


WJOB04E2 = WJOB01S1


WJOB05E2 = WJOB01S1


WJOB06E2 = WJOB01S1


WJOB07E2 = WJOB01S1


WJOB08E2 = WJOB01S1


WJOB09E2 = WJOB01S1


WJOB10E2 = WJOB01S1


WJOB11E2 = WJOB01S1


WJOB12E2 = WJOB01S1


WJOB13E2 = WJOB01S1


WJOB14E2 = WJOB01S1


WJOB15E2 = WJOB01S1


WJOB16E2 = WJOB01S1


WJOB01S3 = WJOB01S1


WJOB02S3 = WJOB01S1


WJOB03S3 = WJOB01S1


WJOB04S3 = WJOB01S1


WJOB05S3 = WJOB01S1


WJOB06S3 = WJOB01S1


WJOB07S3 = WJOB01S1


WJOB08S3 = WJOB01S1


WJOB09S3 = WJOB01S1


WJOB10S3 = WJOB01S1


WJOB11S3 = WJOB01S1


WJOB12S3 = WJOB01S1


WJOB13S3 = WJOB01S1


WJOB14S3 = WJOB01S1


WJOB15S3 = WJOB01S1


WJOB16S3 = WJOB01S1


WJOB01E3 = WJOB01S1


WJOB02E3 = WJOB01S1


WJOB03E3 = WJOB01S1


WJOB04E3 = WJOB01S1


WJOB05E3 = WJOB01S1


WJOB06E3 = WJOB01S1


WJOB07E3 = WJOB01S1


WJOB08E3 = WJOB01S1


WJOB09E3 = WJOB01S1


WJOB10E3 = WJOB01S1


WJOB11E3 = WJOB01S1


WJOB12E3 = WJOB01S1


WJOB13E3 = WJOB01S1


WJOB14E3 = WJOB01S1


WJOB15E3 = WJOB01S1


WJOB16E3 = WJOB01S1


WJOB01S4 = WJOB01S1


WJOB02S4 = WJOB01S1


WJOB03S4 = WJOB01S1


WJOB04S4 = WJOB01S1


WJOB05S4 = WJOB01S1


WJOB06S4 = WJOB01S1


WJOB07S4 = WJOB01S1


WJOB08S4 = WJOB01S1


WJOB09S4 = WJOB01S1


WJOB10S4 = WJOB01S1


WJOB11S4 = WJOB01S1


WJOB12S4 = WJOB01S1


WJOB13S4 = WJOB01S1


WJOB14S4 = WJOB01S1


WJOB15S4 = WJOB01S1


WJOB16S4 = WJOB01S1


WJOB01E4 = WJOB01S1


WJOB02E4 = WJOB01S1


WJOB03E4 = WJOB01S1


WJOB04E4 = WJOB01S1


WJOB05E4 = WJOB01S1


WJOB06E4 = WJOB01S1


WJOB07E4 = WJOB01S1


WJOB08E4 = WJOB01S1


WJOB09E4 = WJOB01S1


WJOB10E4 = WJOB01S1


WJOB11E4 = WJOB01S1


WJOB12E4 = WJOB01S1


WJOB13E4 = WJOB01S1


WJOB14E4 = WJOB01S1


WJOB15E4 = WJOB01S1


WJOB16E4 = WJOB01S1


WJOB01S5 = WJOB01S1


WJOB02S5 = WJOB01S1


WJOB03S5 = WJOB01S1


WJOB04S5 = WJOB01S1


WJOB05S5 = WJOB01S1


WJOB06S5 = WJOB01S1


WJOB07S5 = WJOB01S1


WJOB08S5 = WJOB01S1


WJOB09S5 = WJOB01S1


WJOB10S5 = WJOB01S1


WJOB11S5 = WJOB01S1


WJOB12S5 = WJOB01S1


WJOB13S5 = WJOB01S1


WJOB14S5 = WJOB01S1


WJOB15S5 = WJOB01S1


WJOB16S5 = WJOB01S1


WJOB01E5 = WJOB01S1


WJOB02E5 = WJOB01S1


WJOB03E5 = WJOB01S1


WJOB04E5 = WJOB01S1


WJOB05E5 = WJOB01S1


WJOB06E5 = WJOB01S1


WJOB07E5 = WJOB01S1


WJOB08E5 = WJOB01S1


WJOB09E5 = WJOB01S1


WJOB10E5 = WJOB01S1


WJOB11E5 = WJOB01S1


WJOB12E5 = WJOB01S1


WJOB13E5 = WJOB01S1


WJOB14E5 = WJOB01S1


WJOB15E5 = WJOB01S1


WJOB16E5 = WJOB01S1


WJOB01S6 = WJOB01S1


WJOB02S6 = WJOB01S1


WJOB03S6 = WJOB01S1


WJOB04S6 = WJOB01S1


WJOB05S6 = WJOB01S1


WJOB06S6 = WJOB01S1


WJOB07S6 = WJOB01S1


WJOB08S6 = WJOB01S1


WJOB09S6 = WJOB01S1


WJOB10S6 = WJOB01S1


WJOB11S6 = WJOB01S1


WJOB12S6 = WJOB01S1


WJOB13S6 = WJOB01S1


WJOB14S6 = WJOB01S1


WJOB15S6 = WJOB01S1


WJOB16S6 = WJOB01S1


WJOB01E6 = WJOB01S1


WJOB02E6 = WJOB01S1


WJOB03E6 = WJOB01S1


WJOB04E6 = WJOB01S1


WJOB05E6 = WJOB01S1


WJOB06E6 = WJOB01S1


WJOB07E6 = WJOB01S1


WJOB08E6 = WJOB01S1


WJOB09E6 = WJOB01S1


WJOB10E6 = WJOB01S1


WJOB11E6 = WJOB01S1


WJOB12E6 = WJOB01S1


WJOB13E6 = WJOB01S1


WJOB14E6 = WJOB01S1


WJOB15E6 = WJOB01S1


WJOB16E6 = WJOB01S1


WJOB01S7 = WJOB01S1


WJOB02S7 = WJOB01S1


WJOB03S7 = WJOB01S1


WJOB04S7 = WJOB01S1


WJOB05S7 = WJOB01S1


WJOB06S7 = WJOB01S1


WJOB07S7 = WJOB01S1


WJOB08S7 = WJOB01S1


WJOB09S7 = WJOB01S1


WJOB10S7 = WJOB01S1


WJOB11S7 = WJOB01S1


WJOB12S7 = WJOB01S1


WJOB13S7 = WJOB01S1


WJOB14S7 = WJOB01S1


WJOB15S7 = WJOB01S1


WJOB16S7 = WJOB01S1


WJOB01E7 = WJOB01S1


WJOB02E7 = WJOB01S1


WJOB03E7 = WJOB01S1


WJOB04E7 = WJOB01S1


WJOB05E7 = WJOB01S1


WJOB06E7 = WJOB01S1


WJOB07E7 = WJOB01S1


WJOB08E7 = WJOB01S1


WJOB09E7 = WJOB01S1


WJOB10E7 = WJOB01S1


WJOB11E7 = WJOB01S1


WJOB12E7 = WJOB01S1


WJOB13E7 = WJOB01S1


WJOB14E7 = WJOB01S1


WJOB15E7 = WJOB01S1


WJOB16E7 = WJOB01S1


WOTH01S1 = WJOB01S1


WOTH02S1 = WJOB01S1


WOTH03S1 = WJOB01S1


WOTH04S1 = WJOB01S1


WOTH05S1 = WJOB01S1


WOTH06S1 = WJOB01S1


WOTH07S1 = WJOB01S1


WOTH08S1 = WJOB01S1


WOTH09S1 = WJOB01S1


WOTH10S1 = WJOB01S1


WOTH11S1 = WJOB01S1


WOTH12S1 = WJOB01S1


WOTH13S1 = WJOB01S1


WOTH14S1 = WJOB01S1


WOTH15S1 = WJOB01S1


WOTH16S1 = WJOB01S1


WOTH01E1 = WJOB01S1


WOTH02E1 = WJOB01S1


WOTH03E1 = WJOB01S1


WOTH04E1 = WJOB01S1


WOTH05E1 = WJOB01S1


WOTH06E1 = WJOB01S1


WOTH07E1 = WJOB01S1


WOTH08E1 = WJOB01S1


WOTH09E1 = WJOB01S1


WOTH10E1 = WJOB01S1


WOTH11E1 = WJOB01S1


WOTH12E1 = WJOB01S1


WOTH13E1 = WJOB01S1


WOTH14E1 = WJOB01S1


WOTH15E1 = WJOB01S1


WOTH16E1 = WJOB01S1


WOTH01S2 = WJOB01S1


WOTH02S2 = WJOB01S1


WOTH03S2 = WJOB01S1


WOTH04S2 = WJOB01S1


WOTH05S2 = WJOB01S1


WOTH06S2 = WJOB01S1


WOTH07S2 = WJOB01S1


WOTH08S2 = WJOB01S1


WOTH09S2 = WJOB01S1


WOTH10S2 = WJOB01S1


WOTH11S2 = WJOB01S1


WOTH12S2 = WJOB01S1


WOTH13S2 = WJOB01S1


WOTH14S2 = WJOB01S1


WOTH15S2 = WJOB01S1


WOTH16S2 = WJOB01S1


WOTH01E2 = WJOB01S1


WOTH02E2 = WJOB01S1


WOTH03E2 = WJOB01S1


WOTH04E2 = WJOB01S1


WOTH05E2 = WJOB01S1


WOTH06E2 = WJOB01S1


WOTH07E2 = WJOB01S1


WOTH08E2 = WJOB01S1


WOTH09E2 = WJOB01S1


WOTH10E2 = WJOB01S1


WOTH11E2 = WJOB01S1


WOTH12E2 = WJOB01S1


WOTH13E2 = WJOB01S1


WOTH14E2 = WJOB01S1


WOTH15E2 = WJOB01S1


WOTH16E2 = WJOB01S1


WOTH01S3 = WJOB01S1


WOTH02S3 = WJOB01S1


WOTH03S3 = WJOB01S1


WOTH04S3 = WJOB01S1


WOTH05S3 = WJOB01S1


WOTH06S3 = WJOB01S1


WOTH07S3 = WJOB01S1


WOTH08S3 = WJOB01S1


WOTH09S3 = WJOB01S1


WOTH10S3 = WJOB01S1


WOTH11S3 = WJOB01S1


WOTH12S3 = WJOB01S1


WOTH13S3 = WJOB01S1


WOTH14S3 = WJOB01S1


WOTH15S3 = WJOB01S1


WOTH16S3 = WJOB01S1


WOTH01E3 = WJOB01S1


WOTH02E3 = WJOB01S1


WOTH03E3 = WJOB01S1


WOTH04E3 = WJOB01S1


WOTH05E3 = WJOB01S1


WOTH06E3 = WJOB01S1


WOTH07E3 = WJOB01S1


WOTH08E3 = WJOB01S1


WOTH09E3 = WJOB01S1


WOTH10E3 = WJOB01S1


WOTH11E3 = WJOB01S1


WOTH12E3 = WJOB01S1


WOTH13E3 = WJOB01S1


WOTH14E3 = WJOB01S1


WOTH15E3 = WJOB01S1


WOTH16E3 = WJOB01S1


WOTH01S4 = WJOB01S1


WOTH02S4 = WJOB01S1


WOTH03S4 = WJOB01S1


WOTH04S4 = WJOB01S1


WOTH05S4 = WJOB01S1


WOTH06S4 = WJOB01S1


WOTH07S4 = WJOB01S1


WOTH08S4 = WJOB01S1


WOTH09S4 = WJOB01S1


WOTH10S4 = WJOB01S1


WOTH11S4 = WJOB01S1


WOTH12S4 = WJOB01S1


WOTH13S4 = WJOB01S1


WOTH14S4 = WJOB01S1


WOTH15S4 = WJOB01S1


WOTH16S4 = WJOB01S1


WOTH01E4 = WJOB01S1


WOTH02E4 = WJOB01S1


WOTH03E4 = WJOB01S1


WOTH04E4 = WJOB01S1


WOTH05E4 = WJOB01S1


WOTH06E4 = WJOB01S1


WOTH07E4 = WJOB01S1


WOTH08E4 = WJOB01S1


WOTH09E4 = WJOB01S1


WOTH10E4 = WJOB01S1


WOTH11E4 = WJOB01S1


WOTH12E4 = WJOB01S1


WOTH13E4 = WJOB01S1


WOTH14E4 = WJOB01S1


WOTH15E4 = WJOB01S1


WOTH16E4 = WJOB01S1


WOTH01S5 = WJOB01S1


WOTH02S5 = WJOB01S1


WOTH03S5 = WJOB01S1


WOTH04S5 = WJOB01S1


WOTH05S5 = WJOB01S1


WOTH06S5 = WJOB01S1


WOTH07S5 = WJOB01S1


WOTH08S5 = WJOB01S1


WOTH09S5 = WJOB01S1


WOTH10S5 = WJOB01S1


WOTH11S5 = WJOB01S1


WOTH12S5 = WJOB01S1


WOTH13S5 = WJOB01S1


WOTH14S5 = WJOB01S1


WOTH15S5 = WJOB01S1


WOTH16S5 = WJOB01S1


WOTH01E5 = WJOB01S1


WOTH02E5 = WJOB01S1


WOTH03E5 = WJOB01S1


WOTH04E5 = WJOB01S1


WOTH05E5 = WJOB01S1


WOTH06E5 = WJOB01S1


WOTH07E5 = WJOB01S1


WOTH08E5 = WJOB01S1


WOTH09E5 = WJOB01S1


WOTH10E5 = WJOB01S1


WOTH11E5 = WJOB01S1


WOTH12E5 = WJOB01S1


WOTH13E5 = WJOB01S1


WOTH14E5 = WJOB01S1


WOTH15E5 = WJOB01S1


WOTH16E5 = WJOB01S1


WOTH01S6 = WJOB01S1


WOTH02S6 = WJOB01S1


WOTH03S6 = WJOB01S1


WOTH04S6 = WJOB01S1


WOTH05S6 = WJOB01S1


WOTH06S6 = WJOB01S1


WOTH07S6 = WJOB01S1


WOTH08S6 = WJOB01S1


WOTH09S6 = WJOB01S1


WOTH10S6 = WJOB01S1


WOTH11S6 = WJOB01S1


WOTH12S6 = WJOB01S1


WOTH13S6 = WJOB01S1


WOTH14S6 = WJOB01S1


WOTH15S6 = WJOB01S1


WOTH16S6 = WJOB01S1


WOTH01E6 = WJOB01S1


WOTH02E6 = WJOB01S1


WOTH03E6 = WJOB01S1


WOTH04E6 = WJOB01S1


WOTH05E6 = WJOB01S1


WOTH06E6 = WJOB01S1


WOTH07E6 = WJOB01S1


WOTH08E6 = WJOB01S1


WOTH09E6 = WJOB01S1


WOTH10E6 = WJOB01S1


WOTH11E6 = WJOB01S1


WOTH12E6 = WJOB01S1


WOTH13E6 = WJOB01S1


WOTH14E6 = WJOB01S1


WOTH15E6 = WJOB01S1


WOTH16E6 = WJOB01S1


WOTH01S7 = WJOB01S1


WOTH02S7 = WJOB01S1


WOTH03S7 = WJOB01S1


WOTH04S7 = WJOB01S1


WOTH05S7 = WJOB01S1


WOTH06S7 = WJOB01S1


WOTH07S7 = WJOB01S1


WOTH08S7 = WJOB01S1


WOTH09S7 = WJOB01S1


WOTH10S7 = WJOB01S1


WOTH11S7 = WJOB01S1


WOTH12S7 = WJOB01S1


WOTH13S7 = WJOB01S1


WOTH14S7 = WJOB01S1


WOTH15S7 = WJOB01S1


WOTH16S7 = WJOB01S1


WOTH01E7 = WJOB01S1


WOTH02E7 = WJOB01S1


WOTH03E7 = WJOB01S1


WOTH04E7 = WJOB01S1


WOTH05E7 = WJOB01S1


WOTH06E7 = WJOB01S1


WOTH07E7 = WJOB01S1


WOTH08E7 = WJOB01S1


WOTH09E7 = WJOB01S1


WOTH10E7 = WJOB01S1


WOTH11E7 = WJOB01S1


WOTH12E7 = WJOB01S1


WOTH13E7 = WJOB01S1


WOTH14E7 = WJOB01S1


WOTH15E7 = WJOB01S1


WOTH16E7 = WJOB01S1


WTRV01S1 = WJOB01S1


WTRV02S1 = WJOB01S1


WTRV03S1 = WJOB01S1


WTRV04S1 = WJOB01S1


WTRV05S1 = WJOB01S1


WTRV06S1 = WJOB01S1


WTRV07S1 = WJOB01S1


WTRV08S1 = WJOB01S1


WTRV09S1 = WJOB01S1


WTRV10S1 = WJOB01S1


WTRV11S1 = WJOB01S1


WTRV12S1 = WJOB01S1


WTRV13S1 = WJOB01S1


WTRV14S1 = WJOB01S1


WTRV15S1 = WJOB01S1


WTRV16S1 = WJOB01S1


WTRV01E1 = WJOB01S1


WTRV02E1 = WJOB01S1


WTRV03E1 = WJOB01S1


WTRV04E1 = WJOB01S1


WTRV05E1 = WJOB01S1


WTRV06E1 = WJOB01S1


WTRV07E1 = WJOB01S1


WTRV08E1 = WJOB01S1


WTRV09E1 = WJOB01S1


WTRV10E1 = WJOB01S1


WTRV11E1 = WJOB01S1


WTRV12E1 = WJOB01S1


WTRV13E1 = WJOB01S1


WTRV14E1 = WJOB01S1


WTRV15E1 = WJOB01S1


WTRV16E1 = WJOB01S1


WTRV01S2 = WJOB01S1


WTRV02S2 = WJOB01S1


WTRV03S2 = WJOB01S1


WTRV04S2 = WJOB01S1


WTRV05S2 = WJOB01S1


WTRV06S2 = WJOB01S1


WTRV07S2 = WJOB01S1


WTRV08S2 = WJOB01S1


WTRV09S2 = WJOB01S1


WTRV10S2 = WJOB01S1


WTRV11S2 = WJOB01S1


WTRV12S2 = WJOB01S1


WTRV13S2 = WJOB01S1


WTRV14S2 = WJOB01S1


WTRV15S2 = WJOB01S1


WTRV16S2 = WJOB01S1


WTRV01E2 = WJOB01S1


WTRV02E2 = WJOB01S1


WTRV03E2 = WJOB01S1


WTRV04E2 = WJOB01S1


WTRV05E2 = WJOB01S1


WTRV06E2 = WJOB01S1


WTRV07E2 = WJOB01S1


WTRV08E2 = WJOB01S1


WTRV09E2 = WJOB01S1


WTRV10E2 = WJOB01S1


WTRV11E2 = WJOB01S1


WTRV12E2 = WJOB01S1


WTRV13E2 = WJOB01S1


WTRV14E2 = WJOB01S1


WTRV15E2 = WJOB01S1


WTRV16E2 = WJOB01S1


WTRV01S3 = WJOB01S1


WTRV02S3 = WJOB01S1


WTRV03S3 = WJOB01S1


WTRV04S3 = WJOB01S1


WTRV05S3 = WJOB01S1


WTRV06S3 = WJOB01S1


WTRV07S3 = WJOB01S1


WTRV08S3 = WJOB01S1


WTRV09S3 = WJOB01S1


WTRV10S3 = WJOB01S1


WTRV11S3 = WJOB01S1


WTRV12S3 = WJOB01S1


WTRV13S3 = WJOB01S1


WTRV14S3 = WJOB01S1


WTRV15S3 = WJOB01S1


WTRV16S3 = WJOB01S1


WTRV01E3 = WJOB01S1


WTRV02E3 = WJOB01S1


WTRV03E3 = WJOB01S1


WTRV04E3 = WJOB01S1


WTRV05E3 = WJOB01S1


WTRV06E3 = WJOB01S1


WTRV07E3 = WJOB01S1


WTRV08E3 = WJOB01S1


WTRV09E3 = WJOB01S1


WTRV10E3 = WJOB01S1


WTRV11E3 = WJOB01S1


WTRV12E3 = WJOB01S1


WTRV13E3 = WJOB01S1


WTRV14E3 = WJOB01S1


WTRV15E3 = WJOB01S1


WTRV16E3 = WJOB01S1


WTRV01S4 = WJOB01S1


WTRV02S4 = WJOB01S1


WTRV03S4 = WJOB01S1


WTRV04S4 = WJOB01S1


WTRV05S4 = WJOB01S1


WTRV06S4 = WJOB01S1


WTRV07S4 = WJOB01S1


WTRV08S4 = WJOB01S1


WTRV09S4 = WJOB01S1


WTRV10S4 = WJOB01S1


WTRV11S4 = WJOB01S1


WTRV12S4 = WJOB01S1


WTRV13S4 = WJOB01S1


WTRV14S4 = WJOB01S1


WTRV15S4 = WJOB01S1


WTRV16S4 = WJOB01S1


WTRV01E4 = WJOB01S1


WTRV02E4 = WJOB01S1


WTRV03E4 = WJOB01S1


WTRV04E4 = WJOB01S1


WTRV05E4 = WJOB01S1


WTRV06E4 = WJOB01S1


WTRV07E4 = WJOB01S1


WTRV08E4 = WJOB01S1


WTRV09E4 = WJOB01S1


WTRV10E4 = WJOB01S1


WTRV11E4 = WJOB01S1


WTRV12E4 = WJOB01S1


WTRV13E4 = WJOB01S1


WTRV14E4 = WJOB01S1


WTRV15E4 = WJOB01S1


WTRV16E4 = WJOB01S1


WTRV01S5 = WJOB01S1


WTRV02S5 = WJOB01S1


WTRV03S5 = WJOB01S1


WTRV04S5 = WJOB01S1


WTRV05S5 = WJOB01S1


WTRV06S5 = WJOB01S1


WTRV07S5 = WJOB01S1


WTRV08S5 = WJOB01S1


WTRV09S5 = WJOB01S1


WTRV10S5 = WJOB01S1


WTRV11S5 = WJOB01S1


WTRV12S5 = WJOB01S1


WTRV13S5 = WJOB01S1


WTRV14S5 = WJOB01S1


WTRV15S5 = WJOB01S1


WTRV16S5 = WJOB01S1


WTRV01E5 = WJOB01S1


WTRV02E5 = WJOB01S1


WTRV03E5 = WJOB01S1


WTRV04E5 = WJOB01S1


WTRV05E5 = WJOB01S1


WTRV06E5 = WJOB01S1


WTRV07E5 = WJOB01S1


WTRV08E5 = WJOB01S1


WTRV09E5 = WJOB01S1


WTRV10E5 = WJOB01S1


WTRV11E5 = WJOB01S1


WTRV12E5 = WJOB01S1


WTRV13E5 = WJOB01S1


WTRV14E5 = WJOB01S1


WTRV15E5 = WJOB01S1


WTRV16E5 = WJOB01S1


WTRV01S6 = WJOB01S1


WTRV02S6 = WJOB01S1


WTRV03S6 = WJOB01S1


WTRV04S6 = WJOB01S1


WTRV05S6 = WJOB01S1


WTRV06S6 = WJOB01S1


WTRV07S6 = WJOB01S1


WTRV08S6 = WJOB01S1


WTRV09S6 = WJOB01S1


WTRV10S6 = WJOB01S1


WTRV11S6 = WJOB01S1


WTRV12S6 = WJOB01S1


WTRV13S6 = WJOB01S1


WTRV14S6 = WJOB01S1


WTRV15S6 = WJOB01S1


WTRV16S6 = WJOB01S1


WTRV01E6 = WJOB01S1


WTRV02E6 = WJOB01S1


WTRV03E6 = WJOB01S1


WTRV04E6 = WJOB01S1


WTRV05E6 = WJOB01S1


WTRV06E6 = WJOB01S1


WTRV07E6 = WJOB01S1


WTRV08E6 = WJOB01S1


WTRV09E6 = WJOB01S1


WTRV10E6 = WJOB01S1


WTRV11E6 = WJOB01S1


WTRV12E6 = WJOB01S1


WTRV13E6 = WJOB01S1


WTRV14E6 = WJOB01S1


WTRV15E6 = WJOB01S1


WTRV16E6 = WJOB01S1


WTRV01S7 = WJOB01S1


WTRV02S7 = WJOB01S1


WTRV03S7 = WJOB01S1


WTRV04S7 = WJOB01S1


WTRV05S7 = WJOB01S1


WTRV06S7 = WJOB01S1


WTRV07S7 = WJOB01S1


WTRV08S7 = WJOB01S1


WTRV09S7 = WJOB01S1


WTRV10S7 = WJOB01S1


WTRV11S7 = WJOB01S1


WTRV12S7 = WJOB01S1


WTRV13S7 = WJOB01S1


WTRV14S7 = WJOB01S1


WTRV15S7 = WJOB01S1


WTRV16S7 = WJOB01S1


WTRV01E7 = WJOB01S1


WTRV02E7 = WJOB01S1


WTRV03E7 = WJOB01S1


WTRV04E7 = WJOB01S1


WTRV05E7 = WJOB01S1


WTRV06E7 = WJOB01S1


WTRV07E7 = WJOB01S1


WTRV08E7 = WJOB01S1


WTRV09E7 = WJOB01S1


WTRV10E7 = WJOB01S1


WTRV11E7 = WJOB01S1


WTRV12E7 = WJOB01S1


WTRV13E7 = WJOB01S1


WTRV14E7 = WJOB01S1


WTRV15E7 = WJOB01S1


WTRV16E7 = WJOB01S1


class WTRV1(OrderedEnum):
    VAN = '1'
    CAR = '2'
    BUS = '3'
    BICYCLE = '4'
    FOOT = '5'
    PLANE = '6'
    TRAIN = '7'
    MINIBUS_COACH = '8'
    LORRY = '9'
    UNDERGROUND = '10'
    MOTORBIKE = '11'
    TRACTOR = '12'
    OTHER = '13'
    MISSING = '14'
    NOT_APPLY___DID_NOT_TRAVEL_WHILE_AT_WORK = '15'


WTRV2 = WTRV1


WTRV3 = WTRV1


WTRV4 = WTRV1


WTRV5 = WTRV1


WTRV6 = WTRV1


WTRV7 = WTRV1


class W_IND(OrderedEnum):
    WORKSHEET_BLANK = '0'
    SOME_TIME_RECORDED_ON_WORKSHEET = '1'


class WD1_IND(OrderedEnum):
    NO_TIME = '0'
    YES___SOME_TIME = '1'


WD2_IND = WD1_IND


WD3_IND = WD1_IND


WD4_IND = WD1_IND


WD5_IND = WD1_IND


WD6_IND = WD1_IND


WD7_IND = WD1_IND


class HSEX(OrderedEnum):
    MALE = '1'
    FEMALE = '2'
    MISSING1 = '-1'


class HAGEGRP(OrderedEnum):
    N8__15_YRS = '1'
    N16__24_YRS = '2'
    N25__44_YRS = '3'
    N45__64_YRS = '4'
    N65_YRS_OR_MORE = '5'


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
