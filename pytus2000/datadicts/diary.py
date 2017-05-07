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
    ACT1_001 = (10, " Main Activity  between  4:00 and  4:10")
    ACT2_001 = (11, " Secondary Activity between  4:00 and  4:10")
    WHER_001 = (12, " Location  between  4:00 and  4:10")
    WIT0_001 = (13, " Alone or with people that you don't know between  4:00 and  4:10")
    WIT1_001 = (14, " With children up to 9 living in your household between  4:00 and  4:10")
    WIT2_001 = (15, " With children aged 10 to 14 living in your household between  4:00 and  4:10")
    WIT3_001 = (16, " With other household members  between  4:00 and  4:10")
    WIT4_001 = (17, " With other persons that you know  between  4:00 and  4:10")
    WIT5_001 = (18, " Main Activity:Asleep/ Employment/ Study between  4:00 and  4:10")
    WIT6_001 = (19, " No Answer  between  4:00 and  4:10")
    ACT1_002 = (20, " Main Activity  between  4:10 and  4:20")
    ACT2_002 = (21, " Secondary Activity between  4:10 and  4:20")
    WHER_002 = (22, " Location  between  4:10 and  4:20")
    WIT0_002 = (23, " Alone or with people that you don't know between  4:10 and  4:20")
    WIT1_002 = (24, " With children up to 9 living in your household between  4:10 and  4:20")
    WIT2_002 = (25, " With children aged 10 to 14 living in your household between  4:10 and  4:20")
    WIT3_002 = (26, " With other household members  between  4:10 and  4:20")
    WIT4_002 = (27, " With other persons that you know  between  4:10 and  4:20")
    WIT5_002 = (28, " Main Activity:Asleep/ Employment/ Study between  4:10 and  4:20")
    WIT6_002 = (29, " No Answer  between  4:10 and  4:20")
    ACT1_003 = (30, " Main Activity  between  4:20 and  4:30")
    ACT2_003 = (31, " Secondary Activity between  4:20 and  4:30")
    WHER_003 = (32, " Location  between  4:20 and  4:30")
    WIT0_003 = (33, " Alone or with people that you don't know between  4:20 and  4:30")
    WIT1_003 = (34, " With children up to 9 living in your household between  4:20 and  4:30")
    WIT2_003 = (35, " With children aged 10 to 14 living in your household between  4:20 and  4:30")
    WIT3_003 = (36, " With other household members  between  4:20 and  4:30")
    WIT4_003 = (37, " With other persons that you know  between  4:20 and  4:30")
    WIT5_003 = (38, " Main Activity:Asleep/ Employment/ Study between  4:20 and  4:30")
    WIT6_003 = (39, " No Answer  between  4:20 and  4:30")
    ACT1_004 = (40, " Main Activity  between  4:30 and  4:40")
    ACT2_004 = (41, " Secondary Activity between  4:30 and  4:40")
    WHER_004 = (42, " Location  between  4:30 and  4:40")
    WIT0_004 = (43, " Alone or with people that you don't know between  4:30 and  4:40")
    WIT1_004 = (44, " With children up to 9 living in your household between  4:30 and  4:40")
    WIT2_004 = (45, " With children aged 10 to 14 living in your household between  4:30 and  4:40")
    WIT3_004 = (46, " With other household members  between  4:30 and  4:40")
    WIT4_004 = (47, " With other persons that you know  between  4:30 and  4:40")
    WIT5_004 = (48, " Main Activity:Asleep/ Employment/ Study between  4:30 and  4:40")
    WIT6_004 = (49, " No Answer  between  4:30 and  4:40")
    ACT1_005 = (50, " Main Activity  between  4:40 and  4:50")
    ACT2_005 = (51, " Secondary Activity between  4:40 and  4:50")
    WHER_005 = (52, " Location  between  4:40 and  4:50")
    WIT0_005 = (53, " Alone or with people that you don't know between  4:40 and  4:50")
    WIT1_005 = (54, " With children up to 9 living in your household between  4:40 and  4:50")
    WIT2_005 = (55, " With children aged 10 to 14 living in your household between  4:40 and  4:50")
    WIT3_005 = (56, " With other household members  between  4:40 and  4:50")
    WIT4_005 = (57, " With other persons that you know  between  4:40 and  4:50")
    WIT5_005 = (58, " Main Activity:Asleep/ Employment/ Study between  4:40 and  4:50")
    WIT6_005 = (59, " No Answer  between  4:40 and  4:50")
    ACT1_006 = (60, " Main Activity  between  4:50 and  5:00")
    ACT2_006 = (61, " Secondary Activity between  4:50 and  5:00")
    WHER_006 = (62, " Location  between  4:50 and  5:00")
    WIT0_006 = (63, " Alone or with people that you don't know between  4:50 and  5:00")
    WIT1_006 = (64, " With children up to 9 living in your household between  4:50 and  5:00")
    WIT2_006 = (65, " With children aged 10 to 14 living in your household between  4:50 and  5:00")
    WIT3_006 = (66, " With other household members  between  4:50 and  5:00")
    WIT4_006 = (67, " With other persons that you know  between  4:50 and  5:00")
    WIT5_006 = (68, " Main Activity:Asleep/ Employment/ Study between  4:50 and  5:00")
    WIT6_006 = (69, " No Answer  between  4:50 and  5:00")
    ACT1_007 = (70, " Main Activity  between  5:00 and  5:10")
    ACT2_007 = (71, " Secondary Activity between  5:00 and  5:10")
    WHER_007 = (72, " Location  between  5:00 and  5:10")
    WIT0_007 = (73, " Alone or with people that you don't know between  5:00 and  5:10")
    WIT1_007 = (74, " With children up to 9 living in your household between  5:00 and  5:10")
    WIT2_007 = (75, " With children aged 10 to 14 living in your household between  5:00 and  5:10")
    WIT3_007 = (76, " With other household members  between  5:00 and  5:10")
    WIT4_007 = (77, " With other persons that you know  between  5:00 and  5:10")
    WIT5_007 = (78, " Main Activity:Asleep/ Employment/ Study between  5:00 and  5:10")
    WIT6_007 = (79, " No Answer  between  5:00 and  5:10")
    ACT1_008 = (80, " Main Activity  between  5:10 and  5:20")
    ACT2_008 = (81, " Secondary Activity between  5:10 and  5:20")
    WHER_008 = (82, " Location  between  5:10 and  5:20")
    WIT0_008 = (83, " Alone or with people that you don't know between  5:10 and  5:20")
    WIT1_008 = (84, " With children up to 9 living in your household between  5:10 and  5:20")
    WIT2_008 = (85, " With children aged 10 to 14 living in your household between  5:10 and  5:20")
    WIT3_008 = (86, " With other household members  between  5:10 and  5:20")
    WIT4_008 = (87, " With other persons that you know  between  5:10 and  5:20")
    WIT5_008 = (88, " Main Activity:Asleep/ Employment/ Study between  5:10 and  5:20")
    WIT6_008 = (89, " No Answer  between  5:10 and  5:20")
    ACT1_009 = (90, " Main Activity  between  5:20 and  5:30")
    ACT2_009 = (91, " Secondary Activity between  5:20 and  5:30")
    WHER_009 = (92, " Location  between  5:20 and  5:30")
    WIT0_009 = (93, " Alone or with people that you don't know between  5:20 and  5:30")
    WIT1_009 = (94, " With children up to 9 living in your household between  5:20 and  5:30")
    WIT2_009 = (95, " With children aged 10 to 14 living in your household between  5:20 and  5:30")
    WIT3_009 = (96, " With other household members  between  5:20 and  5:30")
    WIT4_009 = (97, " With other persons that you know  between  5:20 and  5:30")
    WIT5_009 = (98, " Main Activity:Asleep/ Employment/ Study between  5:20 and  5:30")
    WIT6_009 = (99, " No Answer  between  5:20 and  5:30")
    ACT1_010 = (100, " Main Activity  between  5:30 and  5:40")
    ACT2_010 = (101, " Secondary Activity between  5:30 and  5:40")
    WHER_010 = (102, " Location  between  5:30 and  5:40")
    WIT0_010 = (103, " Alone or with people that you don't know between  5:30 and  5:40")
    WIT1_010 = (104, " With children up to 9 living in your household between  5:30 and  5:40")
    WIT2_010 = (105, " With children aged 10 to 14 living in your household between  5:30 and  5:40")
    WIT3_010 = (106, " With other household members  between  5:30 and  5:40")
    WIT4_010 = (107, " With other persons that you know  between  5:30 and  5:40")
    WIT5_010 = (108, " Main Activity:Asleep/ Employment/ Study between  5:30 and  5:40")
    WIT6_010 = (109, " No Answer  between  5:30 and  5:40")
    ACT1_011 = (110, " Main Activity  between  5:40 and  5:50")
    ACT2_011 = (111, " Secondary Activity between  5:40 and  5:50")
    WHER_011 = (112, " Location  between  5:40 and  5:50")
    WIT0_011 = (113, " Alone or with people that you don't know between  5:40 and  5:50")
    WIT1_011 = (114, " With children up to 9 living in your household between  5:40 and  5:50")
    WIT2_011 = (115, " With children aged 10 to 14 living in your household between  5:40 and  5:50")
    WIT3_011 = (116, " With other household members  between  5:40 and  5:50")
    WIT4_011 = (117, " With other persons that you know  between  5:40 and  5:50")
    WIT5_011 = (118, " Main Activity:Asleep/ Employment/ Study between  5:40 and  5:50")
    WIT6_011 = (119, " No Answer  between  5:40 and  5:50")
    ACT1_012 = (120, " Main Activity  between  5:50 and  6:00")
    ACT2_012 = (121, " Secondary Activity between  5:50 and  6:00")
    WHER_012 = (122, " Location  between  5:50 and  6:00")
    WIT0_012 = (123, " Alone or with people that you don't know between  5:50 and  6:00")
    WIT1_012 = (124, " With children up to 9 living in your household between  5:50 and  6:00")
    WIT2_012 = (125, " With children aged 10 to 14 living in your household between  5:50 and  6:00")
    WIT3_012 = (126, " With other household members  between  5:50 and  6:00")
    WIT4_012 = (127, " With other persons that you know  between  5:50 and  6:00")
    WIT5_012 = (128, " Main Activity:Asleep/ Employment/ Study between  5:50 and  6:00")
    WIT6_012 = (129, " No Answer  between  5:50 and  6:00")
    ACT1_013 = (130, " Main Activity  between  6:00 and  6:10")
    ACT2_013 = (131, " Secondary Activity between  6:00 and  6:10")
    WHER_013 = (132, " Location  between  6:00 and  6:10")
    WIT0_013 = (133, " Alone or with people that you don't know between  6:00 and  6:10")
    WIT1_013 = (134, " With children up to 9 living in your household between  6:00 and  6:10")
    WIT2_013 = (135, " With children aged 10 to 14 living in your household between  6:00 and  6:10")
    WIT3_013 = (136, " With other household members  between  6:00 and  6:10")
    WIT4_013 = (137, " With other persons that you know  between  6:00 and  6:10")
    WIT5_013 = (138, " Main Activity:Asleep/ Employment/ Study between  6:00 and  6:10")
    WIT6_013 = (139, " No Answer  between  6:00 and  6:10")
    ACT1_014 = (140, " Main Activity  between  6:10 and  6:20")
    ACT2_014 = (141, " Secondary Activity between  6:10 and  6:20")
    WHER_014 = (142, " Location  between  6:10 and  6:20")
    WIT0_014 = (143, " Alone or with people that you don't know between  6:10 and  6:20")
    WIT1_014 = (144, " With children up to 9 living in your household between  6:10 and  6:20")
    WIT2_014 = (145, " With children aged 10 to 14 living in your household between  6:10 and  6:20")
    WIT3_014 = (146, " With other household members  between  6:10 and  6:20")
    WIT4_014 = (147, " With other persons that you know  between  6:10 and  6:20")
    WIT5_014 = (148, " Main Activity:Asleep/ Employment/ Study between  6:10 and  6:20")
    WIT6_014 = (149, " No Answer  between  6:10 and  6:20")
    ACT1_015 = (150, " Main Activity  between  6:20 and  6:30")
    ACT2_015 = (151, " Secondary Activity between  6:20 and  6:30")
    WHER_015 = (152, " Location  between  6:20 and  6:30")
    WIT0_015 = (153, " Alone or with people that you don't know between  6:20 and  6:30")
    WIT1_015 = (154, " With children up to 9 living in your household between  6:20 and  6:30")
    WIT2_015 = (155, " With children aged 10 to 14 living in your household between  6:20 and  6:30")
    WIT3_015 = (156, " With other household members  between  6:20 and  6:30")
    WIT4_015 = (157, " With other persons that you know  between  6:20 and  6:30")
    WIT5_015 = (158, " Main Activity:Asleep/ Employment/ Study between  6:20 and  6:30")
    WIT6_015 = (159, " No Answer  between  6:20 and  6:30")
    ACT1_016 = (160, " Main Activity  between  6:30 and  6:40")
    ACT2_016 = (161, " Secondary Activity between  6:30 and  6:40")
    WHER_016 = (162, " Location  between  6:30 and  6:40")
    WIT0_016 = (163, " Alone or with people that you don't know between  6:30 and  6:40")
    WIT1_016 = (164, " With children up to 9 living in your household between  6:30 and  6:40")
    WIT2_016 = (165, " With children aged 10 to 14 living in your household between  6:30 and  6:40")
    WIT3_016 = (166, " With other household members  between  6:30 and  6:40")
    WIT4_016 = (167, " With other persons that you know  between  6:30 and  6:40")
    WIT5_016 = (168, " Main Activity:Asleep/ Employment/ Study between  6:30 and  6:40")
    WIT6_016 = (169, " No Answer  between  6:30 and  6:40")
    ACT1_017 = (170, " Main Activity  between  6:40 and  6:50")
    ACT2_017 = (171, " Secondary Activity between  6:40 and  6:50")
    WHER_017 = (172, " Location  between  6:40 and  6:50")
    WIT0_017 = (173, " Alone or with people that you don't know between  6:40 and  6:50")
    WIT1_017 = (174, " With children up to 9 living in your household between  6:40 and  6:50")
    WIT2_017 = (175, " With children aged 10 to 14 living in your household between  6:40 and  6:50")
    WIT3_017 = (176, " With other household members  between  6:40 and  6:50")
    WIT4_017 = (177, " With other persons that you know  between  6:40 and  6:50")
    WIT5_017 = (178, " Main Activity:Asleep/ Employment/ Study between  6:40 and  6:50")
    WIT6_017 = (179, " No Answer  between  6:40 and  6:50")
    ACT1_018 = (180, " Main Activity  between  6:50 and  7:00")
    ACT2_018 = (181, " Secondary Activity between  6:50 and  7:00")
    WHER_018 = (182, " Location  between  6:50 and  7:00")
    WIT0_018 = (183, " Alone or with people that you don't know between  6:50 and  7:00")
    WIT1_018 = (184, " With children up to 9 living in your household between  6:50 and  7:00")
    WIT2_018 = (185, " With children aged 10 to 14 living in your household between  6:50 and  7:00")
    WIT3_018 = (186, " With other household members  between  6:50 and  7:00")
    WIT4_018 = (187, " With other persons that you know  between  6:50 and  7:00")
    WIT5_018 = (188, " Main Activity:Asleep/ Employment/ Study between  6:50 and  7:00")
    WIT6_018 = (189, " No Answer  between  6:50 and  7:00")
    ACT1_019 = (190, " Main Activity  between  7:00 and  7:10")
    ACT2_019 = (191, " Secondary Activity between  7:00 and  7:10")
    WHER_019 = (192, " Location  between  7:00 and  7:10")
    WIT0_019 = (193, " Alone or with people that you don't know between  7:00 and  7:10")
    WIT1_019 = (194, " With children up to 9 living in your household between  7:00 and  7:10")
    WIT2_019 = (195, " With children aged 10 to 14 living in your household between  7:00 and  7:10")
    WIT3_019 = (196, " With other household members  between  7:00 and  7:10")
    WIT4_019 = (197, " With other persons that you know  between  7:00 and  7:10")
    WIT5_019 = (198, " Main Activity:Asleep/ Employment/ Study between  7:00 and  7:10")
    WIT6_019 = (199, " No Answer  between  7:00 and  7:10")
    ACT1_020 = (200, " Main Activity  between  7:10 and  7:20")
    ACT2_020 = (201, " Secondary Activity between  7:10 and  7:20")
    WHER_020 = (202, " Location  between  7:10 and  7:20")
    WIT0_020 = (203, " Alone or with people that you don't know between  7:10 and  7:20")
    WIT1_020 = (204, " With children up to 9 living in your household between  7:10 and  7:20")
    WIT2_020 = (205, " With children aged 10 to 14 living in your household between  7:10 and  7:20")
    WIT3_020 = (206, " With other household members  between  7:10 and  7:20")
    WIT4_020 = (207, " With other persons that you know  between  7:10 and  7:20")
    WIT5_020 = (208, " Main Activity:Asleep/ Employment/ Study between  7:10 and  7:20")
    WIT6_020 = (209, " No Answer  between  7:10 and  7:20")
    ACT1_021 = (210, " Main Activity  between  7:20 and  7:30")
    ACT2_021 = (211, " Secondary Activity between  7:20 and  7:30")
    WHER_021 = (212, " Location  between  7:20 and  7:30")
    WIT0_021 = (213, " Alone or with people that you don't know between  7:20 and  7:30")
    WIT1_021 = (214, " With children up to 9 living in your household between  7:20 and  7:30")
    WIT2_021 = (215, " With children aged 10 to 14 living in your household between  7:20 and  7:30")
    WIT3_021 = (216, " With other household members  between  7:20 and  7:30")
    WIT4_021 = (217, " With other persons that you know  between  7:20 and  7:30")
    WIT5_021 = (218, " Main Activity:Asleep/ Employment/ Study between  7:20 and  7:30")
    WIT6_021 = (219, " No Answer  between  7:20 and  7:30")
    ACT1_022 = (220, " Main Activity  between  7:30 and  7:40")
    ACT2_022 = (221, " Secondary Activity between  7:30 and  7:40")
    WHER_022 = (222, " Location  between  7:30 and  7:40")
    WIT0_022 = (223, " Alone or with people that you don't know between  7:30 and  7:40")
    WIT1_022 = (224, " With children up to 9 living in your household between  7:30 and  7:40")
    WIT2_022 = (225, " With children aged 10 to 14 living in your household between  7:30 and  7:40")
    WIT3_022 = (226, " With other household members  between  7:30 and  7:40")
    WIT4_022 = (227, " With other persons that you know  between  7:30 and  7:40")
    WIT5_022 = (228, " Main Activity:Asleep/ Employment/ Study between  7:30 and  7:40")
    WIT6_022 = (229, " No Answer  between  7:30 and  7:40")
    ACT1_023 = (230, " Main Activity  between  7:40 and  7:50")
    ACT2_023 = (231, " Secondary Activity between  7:40 and  7:50")
    WHER_023 = (232, " Location  between  7:40 and  7:50")
    WIT0_023 = (233, " Alone or with people that you don't know between  7:40 and  7:50")
    WIT1_023 = (234, " With children up to 9 living in your household between  7:40 and  7:50")
    WIT2_023 = (235, " With children aged 10 to 14 living in your household between  7:40 and  7:50")
    WIT3_023 = (236, " With other household members  between  7:40 and  7:50")
    WIT4_023 = (237, " With other persons that you know  between  7:40 and  7:50")
    WIT5_023 = (238, " Main Activity:Asleep/ Employment/ Study between  7:40 and  7:50")
    WIT6_023 = (239, " No Answer  between  7:40 and  7:50")
    ACT1_024 = (240, " Main Activity  between  7:50 and  8:00")
    ACT2_024 = (241, " Secondary Activity between  7:50 and  8:00")
    WHER_024 = (242, " Location  between  7:50 and  8:00")
    WIT0_024 = (243, " Alone or with people that you don't know between  7:50 and  8:00")
    WIT1_024 = (244, " With children up to 9 living in your household between  7:50 and  8:00")
    WIT2_024 = (245, " With children aged 10 to 14 living in your household between  7:50 and  8:00")
    WIT3_024 = (246, " With other household members  between  7:50 and  8:00")
    WIT4_024 = (247, " With other persons that you know  between  7:50 and  8:00")
    WIT5_024 = (248, " Main Activity:Asleep/ Employment/ Study between  7:50 and  8:00")
    WIT6_024 = (249, " No Answer  between  7:50 and  8:00")
    ACT1_025 = (250, " Main Activity  between  8:00 and  8:10")
    ACT2_025 = (251, " Secondary Activity between  8:00 and  8:10")
    WHER_025 = (252, " Location  between  8:00 and  8:10")
    WIT0_025 = (253, " Alone or with people that you don't know between  8:00 and  8:10")
    WIT1_025 = (254, " With children up to 9 living in your household between  8:00 and  8:10")
    WIT2_025 = (255, " With children aged 10 to 14 living in your household between  8:00 and  8:10")
    WIT3_025 = (256, " With other household members  between  8:00 and  8:10")
    WIT4_025 = (257, " With other persons that you know  between  8:00 and  8:10")
    WIT5_025 = (258, " Main Activity:Asleep/ Employment/ Study between  8:00 and  8:10")
    WIT6_025 = (259, " No Answer  between  8:00 and  8:10")
    ACT1_026 = (260, " Main Activity  between  8:10 and  8:20")
    ACT2_026 = (261, " Secondary Activity between  8:10 and  8:20")
    WHER_026 = (262, " Location  between  8:10 and  8:20")
    WIT0_026 = (263, " Alone or with people that you don't know between  8:10 and  8:20")
    WIT1_026 = (264, " With children up to 9 living in your household between  8:10 and  8:20")
    WIT2_026 = (265, " With children aged 10 to 14 living in your household between  8:10 and  8:20")
    WIT3_026 = (266, " With other household members  between  8:10 and  8:20")
    WIT4_026 = (267, " With other persons that you know  between  8:10 and  8:20")
    WIT5_026 = (268, " Main Activity:Asleep/ Employment/ Study between  8:10 and  8:20")
    WIT6_026 = (269, " No Answer  between  8:10 and  8:20")
    ACT1_027 = (270, " Main Activity  between  8:20 and  8:30")
    ACT2_027 = (271, " Secondary Activity between  8:20 and  8:30")
    WHER_027 = (272, " Location  between  8:20 and  8:30")
    WIT0_027 = (273, " Alone or with people that you don't know between  8:20 and  8:30")
    WIT1_027 = (274, " With children up to 9 living in your household between  8:20 and  8:30")
    WIT2_027 = (275, " With children aged 10 to 14 living in your household between  8:20 and  8:30")
    WIT3_027 = (276, " With other household members  between  8:20 and  8:30")
    WIT4_027 = (277, " With other persons that you know  between  8:20 and  8:30")
    WIT5_027 = (278, " Main Activity:Asleep/ Employment/ Study between  8:20 and  8:30")
    WIT6_027 = (279, " No Answer  between  8:20 and  8:30")
    ACT1_028 = (280, " Main Activity  between  8:30 and  8:40")
    ACT2_028 = (281, " Secondary Activity between  8:30 and  8:40")
    WHER_028 = (282, " Location  between  8:30 and  8:40")
    WIT0_028 = (283, " Alone or with people that you don't know between  8:30 and  8:40")
    WIT1_028 = (284, " With children up to 9 living in your household between  8:30 and  8:40")
    WIT2_028 = (285, " With children aged 10 to 14 living in your household between  8:30 and  8:40")
    WIT3_028 = (286, " With other household members  between  8:30 and  8:40")
    WIT4_028 = (287, " With other persons that you know  between  8:30 and  8:40")
    WIT5_028 = (288, " Main Activity:Asleep/ Employment/ Study between  8:30 and  8:40")
    WIT6_028 = (289, " No Answer  between  8:30 and  8:40")
    ACT1_029 = (290, " Main Activity  between  8:40 and  8:50")
    ACT2_029 = (291, " Secondary Activity between  8:40 and  8:50")
    WHER_029 = (292, " Location  between  8:40 and  8:50")
    WIT0_029 = (293, " Alone or with people that you don't know between  8:40 and  8:50")
    WIT1_029 = (294, " With children up to 9 living in your household between  8:40 and  8:50")
    WIT2_029 = (295, " With children aged 10 to 14 living in your household between  8:40 and  8:50")
    WIT3_029 = (296, " With other household members  between  8:40 and  8:50")
    WIT4_029 = (297, " With other persons that you know  between  8:40 and  8:50")
    WIT5_029 = (298, " Main Activity:Asleep/ Employment/ Study between  8:40 and  8:50")
    WIT6_029 = (299, " No Answer  between  8:40 and  8:50")
    ACT1_030 = (300, " Main Activity  between  8:50 and  9:00")
    ACT2_030 = (301, " Secondary Activity between  8:50 and  9:00")
    WHER_030 = (302, " Location  between  8:50 and  9:00")
    WIT0_030 = (303, " Alone or with people that you don't know between  8:50 and  9:00")
    WIT1_030 = (304, " With children up to 9 living in your household between  8:50 and  9:00")
    WIT2_030 = (305, " With children aged 10 to 14 living in your household between  8:50 and  9:00")
    WIT3_030 = (306, " With other household members  between  8:50 and  9:00")
    WIT4_030 = (307, " With other persons that you know  between  8:50 and  9:00")
    WIT5_030 = (308, " Main Activity:Asleep/ Employment/ Study between  8:50 and  9:00")
    WIT6_030 = (309, " No Answer  between  8:50 and  9:00")
    ACT1_031 = (310, " Main Activity  between  9:00 and  9:10")
    ACT2_031 = (311, " Secondary Activity between  9:00 and  9:10")
    WHER_031 = (312, " Location  between  9:00 and  9:10")
    WIT0_031 = (313, " Alone or with people that you don't know between  9:00 and  9:10")
    WIT1_031 = (314, " With children up to 9 living in your household between  9:00 and  9:10")
    WIT2_031 = (315, " With children aged 10 to 14 living in your household between  9:00 and  9:10")
    WIT3_031 = (316, " With other household members  between  9:00 and  9:10")
    WIT4_031 = (317, " With other persons that you know  between  9:00 and  9:10")
    WIT5_031 = (318, " Main Activity:Asleep/ Employment/ Study between  9:00 and  9:10")
    WIT6_031 = (319, " No Answer  between  9:00 and  9:10")
    ACT1_032 = (320, " Main Activity  between  9:10 and  9:20")
    ACT2_032 = (321, " Secondary Activity between  9:10 and  9:20")
    WHER_032 = (322, " Location  between  9:10 and  9:20")
    WIT0_032 = (323, " Alone or with people that you don't know between  9:10 and  9:20")
    WIT1_032 = (324, " With children up to 9 living in your household between  9:10 and  9:20")
    WIT2_032 = (325, " With children aged 10 to 14 living in your household between  9:10 and  9:20")
    WIT3_032 = (326, " With other household members  between  9:10 and  9:20")
    WIT4_032 = (327, " With other persons that you know  between  9:10 and  9:20")
    WIT5_032 = (328, " Main Activity:Asleep/ Employment/ Study between  9:10 and  9:20")
    WIT6_032 = (329, " No Answer  between  9:10 and  9:20")
    ACT1_033 = (330, " Main Activity  between  9:20 and  9:30")
    ACT2_033 = (331, " Secondary Activity between  9:20 and  9:30")
    WHER_033 = (332, " Location  between  9:20 and  9:30")
    WIT0_033 = (333, " Alone or with people that you don't know between  9:20 and  9:30")
    WIT1_033 = (334, " With children up to 9 living in your household between  9:20 and  9:30")
    WIT2_033 = (335, " With children aged 10 to 14 living in your household between  9:20 and  9:30")
    WIT3_033 = (336, " With other household members  between  9:20 and  9:30")
    WIT4_033 = (337, " With other persons that you know  between  9:20 and  9:30")
    WIT5_033 = (338, " Main Activity:Asleep/ Employment/ Study between  9:20 and  9:30")
    WIT6_033 = (339, " No Answer  between  9:20 and  9:30")
    ACT1_034 = (340, " Main Activity  between  9:30 and  9:40")
    ACT2_034 = (341, " Secondary Activity between  9:30 and  9:40")
    WHER_034 = (342, " Location  between  9:30 and  9:40")
    WIT0_034 = (343, " Alone or with people that you don't know between  9:30 and  9:40")
    WIT1_034 = (344, " With children up to 9 living in your household between  9:30 and  9:40")
    WIT2_034 = (345, " With children aged 10 to 14 living in your household between  9:30 and  9:40")
    WIT3_034 = (346, " With other household members  between  9:30 and  9:40")
    WIT4_034 = (347, " With other persons that you know  between  9:30 and  9:40")
    WIT5_034 = (348, " Main Activity:Asleep/ Employment/ Study between  9:30 and  9:40")
    WIT6_034 = (349, " No Answer  between  9:30 and  9:40")
    ACT1_035 = (350, " Main Activity  between  9:40 and  9:50")
    ACT2_035 = (351, " Secondary Activity between  9:40 and  9:50")
    WHER_035 = (352, " Location  between  9:40 and  9:50")
    WIT0_035 = (353, " Alone or with people that you don't know between  9:40 and  9:50")
    WIT1_035 = (354, " With children up to 9 living in your household between  9:40 and  9:50")
    WIT2_035 = (355, " With children aged 10 to 14 living in your household between  9:40 and  9:50")
    WIT3_035 = (356, " With other household members  between  9:40 and  9:50")
    WIT4_035 = (357, " With other persons that you know  between  9:40 and  9:50")
    WIT5_035 = (358, " Main Activity:Asleep/ Employment/ Study between  9:40 and  9:50")
    WIT6_035 = (359, " No Answer  between  9:40 and  9:50")
    ACT1_036 = (360, " Main Activity  between  9:50 and  10:00")
    ACT2_036 = (361, " Secondary Activity between  9:50 and  10:00")
    WHER_036 = (362, " Location  between  9:50 and  10:00")
    WIT0_036 = (363, " Alone or with people that you don't know between  9:50 and  10:00")
    WIT1_036 = (364, " With children up to 9 living in your household between  9:50 and  10:00")
    WIT2_036 = (365, " With children aged 10 to 14 living in your household between  9:50 and  10:00")
    WIT3_036 = (366, " With other household members  between  9:50 and  10:00")
    WIT4_036 = (367, " With other persons that you know  between  9:50 and  10:00")
    WIT5_036 = (368, " Main Activity:Asleep/ Employment/ Study between  9:50 and  10:00")
    WIT6_036 = (369, " No Answer  between  9:50 and  10:00")
    ACT1_037 = (370, " Main Activity  between  10:00 and  10:10")
    ACT2_037 = (371, " Secondary Activity between  10:00 and  10:10")
    WHER_037 = (372, " Location  between  10:00 and  10:10")
    WIT0_037 = (373, " Alone or with people that you don't know between  10:00 and  10:10")
    WIT1_037 = (374, " With children up to 9 living in your household between  10:00 and  10:10")
    WIT2_037 = (375, " With children aged 10 to 14 living in your household between  10:00 and  10:10")
    WIT3_037 = (376, " With other household members  between  10:00 and  10:10")
    WIT4_037 = (377, " With other persons that you know  between  10:00 and  10:10")
    WIT5_037 = (378, " Main Activity:Asleep/ Employment/ Study between  10:00 and  10:10")
    WIT6_037 = (379, " No Answer  between  10:00 and  10:10")
    ACT1_038 = (380, " Main Activity  between  10:10 and  10:20")
    ACT2_038 = (381, " Secondary Activity between  10:10 and  10:20")
    WHER_038 = (382, " Location  between  10:10 and  10:20")
    WIT0_038 = (383, " Alone or with people that you don't know between  10:10 and  10:20")
    WIT1_038 = (384, " With children up to 9 living in your household between  10:10 and  10:20")
    WIT2_038 = (385, " With children aged 10 to 14 living in your household between  10:10 and  10:20")
    WIT3_038 = (386, " With other household members  between  10:10 and  10:20")
    WIT4_038 = (387, " With other persons that you know  between  10:10 and  10:20")
    WIT5_038 = (388, " Main Activity:Asleep/ Employment/ Study between  10:10 and  10:20")
    WIT6_038 = (389, " No Answer  between  10:10 and  10:20")
    ACT1_039 = (390, " Main Activity  between  10:20 and  10:30")
    ACT2_039 = (391, " Secondary Activity between  10:20 and  10:30")
    WHER_039 = (392, " Location  between  10:20 and  10:30")
    WIT0_039 = (393, " Alone or with people that you don't know between  10:20 and  10:30")
    WIT1_039 = (394, " With children up to 9 living in your household between  10:20 and  10:30")
    WIT2_039 = (395, " With children aged 10 to 14 living in your household between  10:20 and  10:30")
    WIT3_039 = (396, " With other household members  between  10:20 and  10:30")
    WIT4_039 = (397, " With other persons that you know  between  10:20 and  10:30")
    WIT5_039 = (398, " Main Activity:Asleep/ Employment/ Study between  10:20 and  10:30")
    WIT6_039 = (399, " No Answer  between  10:20 and  10:30")
    ACT1_040 = (400, " Main Activity  between  10:30 and  10:40")
    ACT2_040 = (401, " Secondary Activity between  10:30 and  10:40")
    WHER_040 = (402, " Location  between  10:30 and  10:40")
    WIT0_040 = (403, " Alone or with people that you don't know between  10:30 and  10:40")
    WIT1_040 = (404, " With children up to 9 living in your household between  10:30 and  10:40")
    WIT2_040 = (405, " With children aged 10 to 14 living in your household between  10:30 and  10:40")
    WIT3_040 = (406, " With other household members  between  10:30 and  10:40")
    WIT4_040 = (407, " With other persons that you know  between  10:30 and  10:40")
    WIT5_040 = (408, " Main Activity:Asleep/ Employment/ Study between  10:30 and  10:40")
    WIT6_040 = (409, " No Answer  between  10:30 and  10:40")
    ACT1_041 = (410, " Main Activity  between  10:40 and  10:50")
    ACT2_041 = (411, " Secondary Activity between  10:40 and  10:50")
    WHER_041 = (412, " Location  between  10:40 and  10:50")
    WIT0_041 = (413, " Alone or with people that you don't know between  10:40 and  10:50")
    WIT1_041 = (414, " With children up to 9 living in your household between  10:40 and  10:50")
    WIT2_041 = (415, " With children aged 10 to 14 living in your household between  10:40 and  10:50")
    WIT3_041 = (416, " With other household members  between  10:40 and  10:50")
    WIT4_041 = (417, " With other persons that you know  between  10:40 and  10:50")
    WIT5_041 = (418, " Main Activity:Asleep/ Employment/ Study between  10:40 and  10:50")
    WIT6_041 = (419, " No Answer  between  10:40 and  10:50")
    ACT1_042 = (420, " Main Activity  between  10:50 and  11:00")
    ACT2_042 = (421, " Secondary Activity between  10:50 and  11:00")
    WHER_042 = (422, " Location  between  10:50 and  11:00")
    WIT0_042 = (423, " Alone or with people that you don't know between  10:50 and  11:00")
    WIT1_042 = (424, " With children up to 9 living in your household between  10:50 and  11:00")
    WIT2_042 = (425, " With children aged 10 to 14 living in your household between  10:50 and  11:00")
    WIT3_042 = (426, " With other household members  between  10:50 and  11:00")
    WIT4_042 = (427, " With other persons that you know  between  10:50 and  11:00")
    WIT5_042 = (428, " Main Activity:Asleep/ Employment/ Study between  10:50 and  11:00")
    WIT6_042 = (429, " No Answer  between  10:50 and  11:00")
    ACT1_043 = (430, " Main Activity  between  11:00 and  11:10")
    ACT2_043 = (431, " Secondary Activity between  11:00 and  11:10")
    WHER_043 = (432, " Location  between  11:00 and  11:10")
    WIT0_043 = (433, " Alone or with people that you don't know between  11:00 and  11:10")
    WIT1_043 = (434, " With children up to 9 living in your household between  11:00 and  11:10")
    WIT2_043 = (435, " With children aged 10 to 14 living in your household between  11:00 and  11:10")
    WIT3_043 = (436, " With other household members  between  11:00 and  11:10")
    WIT4_043 = (437, " With other persons that you know  between  11:00 and  11:10")
    WIT5_043 = (438, " Main Activity:Asleep/ Employment/ Study between  11:00 and  11:10")
    WIT6_043 = (439, " No Answer  between  11:00 and  11:10")
    ACT1_044 = (440, " Main Activity  between  11:10 and  11:20")
    ACT2_044 = (441, " Secondary Activity between  11:10 and  11:20")
    WHER_044 = (442, " Location  between  11:10 and  11:20")
    WIT0_044 = (443, " Alone or with people that you don't know between  11:10 and  11:20")
    WIT1_044 = (444, " With children up to 9 living in your household between  11:10 and  11:20")
    WIT2_044 = (445, " With children aged 10 to 14 living in your household between  11:10 and  11:20")
    WIT3_044 = (446, " With other household members  between  11:10 and  11:20")
    WIT4_044 = (447, " With other persons that you know  between  11:10 and  11:20")
    WIT5_044 = (448, " Main Activity:Asleep/ Employment/ Study between  11:10 and  11:20")
    WIT6_044 = (449, " No Answer  between  11:10 and  11:20")
    ACT1_045 = (450, " Main Activity  between  11:20 and  11:30")
    ACT2_045 = (451, " Secondary Activity between  11:20 and  11:30")
    WHER_045 = (452, " Location  between  11:20 and  11:30")
    WIT0_045 = (453, " Alone or with people that you don't know between  11:20 and  11:30")
    WIT1_045 = (454, " With children up to 9 living in your household between  11:20 and  11:30")
    WIT2_045 = (455, " With children aged 10 to 14 living in your household between  11:20 and  11:30")
    WIT3_045 = (456, " With other household members  between  11:20 and  11:30")
    WIT4_045 = (457, " With other persons that you know  between  11:20 and  11:30")
    WIT5_045 = (458, " Main Activity:Asleep/ Employment/ Study between  11:20 and  11:30")
    WIT6_045 = (459, " No Answer  between  11:20 and  11:30")
    ACT1_046 = (460, " Main Activity  between  11:30 and  11:40")
    ACT2_046 = (461, " Secondary Activity between  11:30 and  11:40")
    WHER_046 = (462, " Location  between  11:30 and  11:40")
    WIT0_046 = (463, " Alone or with people that you don't know between  11:30 and  11:40")
    WIT1_046 = (464, " With children up to 9 living in your household between  11:30 and  11:40")
    WIT2_046 = (465, " With children aged 10 to 14 living in your household between  11:30 and  11:40")
    WIT3_046 = (466, " With other household members  between  11:30 and  11:40")
    WIT4_046 = (467, " With other persons that you know  between  11:30 and  11:40")
    WIT5_046 = (468, " Main Activity:Asleep/ Employment/ Study between  11:30 and  11:40")
    WIT6_046 = (469, " No Answer  between  11:30 and  11:40")
    ACT1_047 = (470, " Main Activity  between  11:40 and  11:50")
    ACT2_047 = (471, " Secondary Activity between  11:40 and  11:50")
    WHER_047 = (472, " Location  between  11:40 and  11:50")
    WIT0_047 = (473, " Alone or with people that you don't know between  11:40 and  11:50")
    WIT1_047 = (474, " With children up to 9 living in your household between  11:40 and  11:50")
    WIT2_047 = (475, " With children aged 10 to 14 living in your household between  11:40 and  11:50")
    WIT3_047 = (476, " With other household members  between  11:40 and  11:50")
    WIT4_047 = (477, " With other persons that you know  between  11:40 and  11:50")
    WIT5_047 = (478, " Main Activity:Asleep/ Employment/ Study between  11:40 and  11:50")
    WIT6_047 = (479, " No Answer  between  11:40 and  11:50")
    ACT1_048 = (480, " Main Activity  between  11:50 and  12:00")
    ACT2_048 = (481, " Secondary Activity between  11:50 and  12:00")
    WHER_048 = (482, " Location  between  11:50 and  12:00")
    WIT0_048 = (483, " Alone or with people that you don't know between  11:50 and  12:00")
    WIT1_048 = (484, " With children up to 9 living in your household between  11:50 and  12:00")
    WIT2_048 = (485, " With children aged 10 to 14 living in your household between  11:50 and  12:00")
    WIT3_048 = (486, " With other household members  between  11:50 and  12:00")
    WIT4_048 = (487, " With other persons that you know  between  11:50 and  12:00")
    WIT5_048 = (488, " Main Activity:Asleep/ Employment/ Study between  11:50 and  12:00")
    WIT6_048 = (489, " No Answer  between  11:50 and  12:00")
    ACT1_049 = (490, " Main Activity  between  12:00 and  12:10")
    ACT2_049 = (491, " Secondary Activity between  12:00 and  12:10")
    WHER_049 = (492, " Location  between  12:00 and  12:10")
    WIT0_049 = (493, " Alone or with people that you don't know between  12:00 and  12:10")
    WIT1_049 = (494, " With children up to 9 living in your household between  12:00 and  12:10")
    WIT2_049 = (495, " With children aged 10 to 14 living in your household between  12:00 and  12:10")
    WIT3_049 = (496, " With other household members  between  12:00 and  12:10")
    WIT4_049 = (497, " With other persons that you know  between  12:00 and  12:10")
    WIT5_049 = (498, " Main Activity:Asleep/ Employment/ Study between  12:00 and  12:10")
    WIT6_049 = (499, " No Answer  between  12:00 and  12:10")
    ACT1_050 = (500, " Main Activity  between  12:10 and  12:20")
    ACT2_050 = (501, " Secondary Activity between  12:10 and  12:20")
    WHER_050 = (502, " Location  between  12:10 and  12:20")
    WIT0_050 = (503, " Alone or with people that you don't know between  12:10 and  12:20")
    WIT1_050 = (504, " With children up to 9 living in your household between  12:10 and  12:20")
    WIT2_050 = (505, " With children aged 10 to 14 living in your household between  12:10 and  12:20")
    WIT3_050 = (506, " With other household members  between  12:10 and  12:20")
    WIT4_050 = (507, " With other persons that you know  between  12:10 and  12:20")
    WIT5_050 = (508, " Main Activity:Asleep/ Employment/ Study between  12:10 and  12:20")
    WIT6_050 = (509, " No Answer  between  12:10 and  12:20")
    ACT1_051 = (510, " Main Activity  between  12:20 and  12:30")
    ACT2_051 = (511, " Secondary Activity between  12:20 and  12:30")
    WHER_051 = (512, " Location  between  12:20 and  12:30")
    WIT0_051 = (513, " Alone or with people that you don't know between  12:20 and  12:30")
    WIT1_051 = (514, " With children up to 9 living in your household between  12:20 and  12:30")
    WIT2_051 = (515, " With children aged 10 to 14 living in your household between  12:20 and  12:30")
    WIT3_051 = (516, " With other household members  between  12:20 and  12:30")
    WIT4_051 = (517, " With other persons that you know  between  12:20 and  12:30")
    WIT5_051 = (518, " Main Activity:Asleep/ Employment/ Study between  12:20 and  12:30")
    WIT6_051 = (519, " No Answer  between  12:20 and  12:30")
    ACT1_052 = (520, " Main Activity  between  12:30 and  12:40")
    ACT2_052 = (521, " Secondary Activity between  12:30 and  12:40")
    WHER_052 = (522, " Location  between  12:30 and  12:40")
    WIT0_052 = (523, " Alone or with people that you don't know between  12:30 and  12:40")
    WIT1_052 = (524, " With children up to 9 living in your household between  12:30 and  12:40")
    WIT2_052 = (525, " With children aged 10 to 14 living in your household between  12:30 and  12:40")
    WIT3_052 = (526, " With other household members  between  12:30 and  12:40")
    WIT4_052 = (527, " With other persons that you know  between  12:30 and  12:40")
    WIT5_052 = (528, " Main Activity:Asleep/ Employment/ Study between  12:30 and  12:40")
    WIT6_052 = (529, " No Answer  between  12:30 and  12:40")
    ACT1_053 = (530, " Main Activity  between  12:40 and  12:50")
    ACT2_053 = (531, " Secondary Activity between  12:40 and  12:50")
    WHER_053 = (532, " Location  between  12:40 and  12:50")
    WIT0_053 = (533, " Alone or with people that you don't know between  12:40 and  12:50")
    WIT1_053 = (534, " With children up to 9 living in your household between  12:40 and  12:50")
    WIT2_053 = (535, " With children aged 10 to 14 living in your household between  12:40 and  12:50")
    WIT3_053 = (536, " With other household members  between  12:40 and  12:50")
    WIT4_053 = (537, " With other persons that you know  between  12:40 and  12:50")
    WIT5_053 = (538, " Main Activity:Asleep/ Employment/ Study between  12:40 and  12:50")
    WIT6_053 = (539, " No Answer  between  12:40 and  12:50")
    ACT1_054 = (540, " Main Activity  between  12:50 and  13:00")
    ACT2_054 = (541, " Secondary Activity between  12:50 and  13:00")
    WHER_054 = (542, " Location  between  12:50 and  13:00")
    WIT0_054 = (543, " Alone or with people that you don't know between  12:50 and  13:00")
    WIT1_054 = (544, " With children up to 9 living in your household between  12:50 and  13:00")
    WIT2_054 = (545, " With children aged 10 to 14 living in your household between  12:50 and  13:00")
    WIT3_054 = (546, " With other household members  between  12:50 and  13:00")
    WIT4_054 = (547, " With other persons that you know  between  12:50 and  13:00")
    WIT5_054 = (548, " Main Activity:Asleep/ Employment/ Study between  12:50 and  13:00")
    WIT6_054 = (549, " No Answer  between  12:50 and  13:00")
    ACT1_055 = (550, " Main Activity  between  13:00 and  13:10")
    ACT2_055 = (551, " Secondary Activity between  13:00 and  13:10")
    WHER_055 = (552, " Location  between  13:00 and  13:10")
    WIT0_055 = (553, " Alone or with people that you don't know between  13:00 and  13:10")
    WIT1_055 = (554, " With children up to 9 living in your household between  13:00 and  13:10")
    WIT2_055 = (555, " With children aged 10 to 14 living in your household between  13:00 and  13:10")
    WIT3_055 = (556, " With other household members  between  13:00 and  13:10")
    WIT4_055 = (557, " With other persons that you know  between  13:00 and  13:10")
    WIT5_055 = (558, " Main Activity:Asleep/ Employment/ Study between  13:00 and  13:10")
    WIT6_055 = (559, " No Answer  between  13:00 and  13:10")
    ACT1_056 = (560, " Main Activity  between  13:10 and  13:20")
    ACT2_056 = (561, " Secondary Activity between  13:10 and  13:20")
    WHER_056 = (562, " Location  between  13:10 and  13:20")
    WIT0_056 = (563, " Alone or with people that you don't know between  13:10 and  13:20")
    WIT1_056 = (564, " With children up to 9 living in your household between  13:10 and  13:20")
    WIT2_056 = (565, " With children aged 10 to 14 living in your household between  13:10 and  13:20")
    WIT3_056 = (566, " With other household members  between  13:10 and  13:20")
    WIT4_056 = (567, " With other persons that you know  between  13:10 and  13:20")
    WIT5_056 = (568, " Main Activity:Asleep/ Employment/ Study between  13:10 and  13:20")
    WIT6_056 = (569, " No Answer  between  13:10 and  13:20")
    ACT1_057 = (570, " Main Activity  between  13:20 and  13:30")
    ACT2_057 = (571, " Secondary Activity between  13:20 and  13:30")
    WHER_057 = (572, " Location  between  13:20 and  13:30")
    WIT0_057 = (573, " Alone or with people that you don't know between  13:20 and  13:30")
    WIT1_057 = (574, " With children up to 9 living in your household between  13:20 and  13:30")
    WIT2_057 = (575, " With children aged 10 to 14 living in your household between  13:20 and  13:30")
    WIT3_057 = (576, " With other household members  between  13:20 and  13:30")
    WIT4_057 = (577, " With other persons that you know  between  13:20 and  13:30")
    WIT5_057 = (578, " Main Activity:Asleep/ Employment/ Study between  13:20 and  13:30")
    WIT6_057 = (579, " No Answer  between  13:20 and  13:30")
    ACT1_058 = (580, " Main Activity  between  13:30 and  13:40")
    ACT2_058 = (581, " Secondary Activity between  13:30 and  13:40")
    WHER_058 = (582, " Location  between  13:30 and  13:40")
    WIT0_058 = (583, " Alone or with people that you don't know between  13:30 and  13:40")
    WIT1_058 = (584, " With children up to 9 living in your household between  13:30 and  13:40")
    WIT2_058 = (585, " With children aged 10 to 14 living in your household between  13:30 and  13:40")
    WIT3_058 = (586, " With other household members  between  13:30 and  13:40")
    WIT4_058 = (587, " With other persons that you know  between  13:30 and  13:40")
    WIT5_058 = (588, " Main Activity:Asleep/ Employment/ Study between  13:30 and  13:40")
    WIT6_058 = (589, " No Answer  between  13:30 and  13:40")
    ACT1_059 = (590, " Main Activity  between  13:40 and  13:50")
    ACT2_059 = (591, " Secondary Activity between  13:40 and  13:50")
    WHER_059 = (592, " Location  between  13:40 and  13:50")
    WIT0_059 = (593, " Alone or with people that you don't know between  13:40 and  13:50")
    WIT1_059 = (594, " With children up to 9 living in your household between  13:40 and  13:50")
    WIT2_059 = (595, " With children aged 10 to 14 living in your household between  13:40 and  13:50")
    WIT3_059 = (596, " With other household members  between  13:40 and  13:50")
    WIT4_059 = (597, " With other persons that you know  between  13:40 and  13:50")
    WIT5_059 = (598, " Main Activity:Asleep/ Employment/ Study between  13:40 and  13:50")
    WIT6_059 = (599, " No Answer  between  13:40 and  13:50")
    ACT1_060 = (600, " Main Activity  between  13:50 and  14:00")
    ACT2_060 = (601, " Secondary Activity between  13:50 and  14:00")
    WHER_060 = (602, " Location  between  13:50 and  14:00")
    WIT0_060 = (603, " Alone or with people that you don't know between  13:50 and  14:00")
    WIT1_060 = (604, " With children up to 9 living in your household between  13:50 and  14:00")
    WIT2_060 = (605, " With children aged 10 to 14 living in your household between  13:50 and  14:00")
    WIT3_060 = (606, " With other household members  between  13:50 and  14:00")
    WIT4_060 = (607, " With other persons that you know  between  13:50 and  14:00")
    WIT5_060 = (608, " Main Activity:Asleep/ Employment/ Study between  13:50 and  14:00")
    WIT6_060 = (609, " No Answer  between  13:50 and  14:00")
    ACT1_061 = (610, " Main Activity  between  14:00 and  14:10")
    ACT2_061 = (611, " Secondary Activity between  14:00 and  14:10")
    WHER_061 = (612, " Location  between  14:00 and  14:10")
    WIT0_061 = (613, " Alone or with people that you don't know between  14:00 and  14:10")
    WIT1_061 = (614, " With children up to 9 living in your household between  14:00 and  14:10")
    WIT2_061 = (615, " With children aged 10 to 14 living in your household between  14:00 and  14:10")
    WIT3_061 = (616, " With other household members  between  14:00 and  14:10")
    WIT4_061 = (617, " With other persons that you know  between  14:00 and  14:10")
    WIT5_061 = (618, " Main Activity:Asleep/ Employment/ Study between  14:00 and  14:10")
    WIT6_061 = (619, " No Answer  between  14:00 and  14:10")
    ACT1_062 = (620, " Main Activity  between  14:10 and  14:20")
    ACT2_062 = (621, " Secondary Activity between  14:10 and  14:20")
    WHER_062 = (622, " Location  between  14:10 and  14:20")
    WIT0_062 = (623, " Alone or with people that you don't know between  14:10 and  14:20")
    WIT1_062 = (624, " With children up to 9 living in your household between  14:10 and  14:20")
    WIT2_062 = (625, " With children aged 10 to 14 living in your household between  14:10 and  14:20")
    WIT3_062 = (626, " With other household members  between  14:10 and  14:20")
    WIT4_062 = (627, " With other persons that you know  between  14:10 and  14:20")
    WIT5_062 = (628, " Main Activity:Asleep/ Employment/ Study between  14:10 and  14:20")
    WIT6_062 = (629, " No Answer  between  14:10 and  14:20")
    ACT1_063 = (630, " Main Activity  between  14:20 and  14:30")
    ACT2_063 = (631, " Secondary Activity between  14:20 and  14:30")
    WHER_063 = (632, " Location  between  14:20 and  14:30")
    WIT0_063 = (633, " Alone or with people that you don't know between  14:20 and  14:30")
    WIT1_063 = (634, " With children up to 9 living in your household between  14:20 and  14:30")
    WIT2_063 = (635, " With children aged 10 to 14 living in your household between  14:20 and  14:30")
    WIT3_063 = (636, " With other household members  between  14:20 and  14:30")
    WIT4_063 = (637, " With other persons that you know  between  14:20 and  14:30")
    WIT5_063 = (638, " Main Activity:Asleep/ Employment/ Study between  14:20 and  14:30")
    WIT6_063 = (639, " No Answer  between  14:20 and  14:30")
    ACT1_064 = (640, " Main Activity  between  14:30 and  14:40")
    ACT2_064 = (641, " Secondary Activity between  14:30 and  14:40")
    WHER_064 = (642, " Location  between  14:30 and  14:40")
    WIT0_064 = (643, " Alone or with people that you don't know between  14:30 and  14:40")
    WIT1_064 = (644, " With children up to 9 living in your household between  14:30 and  14:40")
    WIT2_064 = (645, " With children aged 10 to 14 living in your household between  14:30 and  14:40")
    WIT3_064 = (646, " With other household members  between  14:30 and  14:40")
    WIT4_064 = (647, " With other persons that you know  between  14:30 and  14:40")
    WIT5_064 = (648, " Main Activity:Asleep/ Employment/ Study between  14:30 and  14:40")
    WIT6_064 = (649, " No Answer  between  14:30 and  14:40")
    ACT1_065 = (650, " Main Activity  between  14:40 and  14:50")
    ACT2_065 = (651, " Secondary Activity between  14:40 and  14:50")
    WHER_065 = (652, " Location  between  14:40 and  14:50")
    WIT0_065 = (653, " Alone or with people that you don't know between  14:40 and  14:50")
    WIT1_065 = (654, " With children up to 9 living in your household between  14:40 and  14:50")
    WIT2_065 = (655, " With children aged 10 to 14 living in your household between  14:40 and  14:50")
    WIT3_065 = (656, " With other household members  between  14:40 and  14:50")
    WIT4_065 = (657, " With other persons that you know  between  14:40 and  14:50")
    WIT5_065 = (658, " Main Activity:Asleep/ Employment/ Study between  14:40 and  14:50")
    WIT6_065 = (659, " No Answer  between  14:40 and  14:50")
    ACT1_066 = (660, " Main Activity  between  14:50 and  15:00")
    ACT2_066 = (661, " Secondary Activity between  14:50 and  15:00")
    WHER_066 = (662, " Location  between  14:50 and  15:00")
    WIT0_066 = (663, " Alone or with people that you don't know between  14:50 and  15:00")
    WIT1_066 = (664, " With children up to 9 living in your household between  14:50 and  15:00")
    WIT2_066 = (665, " With children aged 10 to 14 living in your household between  14:50 and  15:00")
    WIT3_066 = (666, " With other household members  between  14:50 and  15:00")
    WIT4_066 = (667, " With other persons that you know  between  14:50 and  15:00")
    WIT5_066 = (668, " Main Activity:Asleep/ Employment/ Study between  14:50 and  15:00")
    WIT6_066 = (669, " No Answer  between  14:50 and  15:00")
    ACT1_067 = (670, " Main Activity  between  15:00 and  15:10")
    ACT2_067 = (671, " Secondary Activity between  15:00 and  15:10")
    WHER_067 = (672, " Location  between  15:00 and  15:10")
    WIT0_067 = (673, " Alone or with people that you don't know between  15:00 and  15:10")
    WIT1_067 = (674, " With children up to 9 living in your household between  15:00 and  15:10")
    WIT2_067 = (675, " With children aged 10 to 14 living in your household between  15:00 and  15:10")
    WIT3_067 = (676, " With other household members  between  15:00 and  15:10")
    WIT4_067 = (677, " With other persons that you know  between  15:00 and  15:10")
    WIT5_067 = (678, " Main Activity:Asleep/ Employment/ Study between  15:00 and  15:10")
    WIT6_067 = (679, " No Answer  between  15:00 and  15:10")
    ACT1_068 = (680, " Main Activity  between  15:10 and  15:20")
    ACT2_068 = (681, " Secondary Activity between  15:10 and  15:20")
    WHER_068 = (682, " Location  between  15:10 and  15:20")
    WIT0_068 = (683, " Alone or with people that you don't know between  15:10 and  15:20")
    WIT1_068 = (684, " With children up to 9 living in your household between  15:10 and  15:20")
    WIT2_068 = (685, " With children aged 10 to 14 living in your household between  15:10 and  15:20")
    WIT3_068 = (686, " With other household members  between  15:10 and  15:20")
    WIT4_068 = (687, " With other persons that you know  between  15:10 and  15:20")
    WIT5_068 = (688, " Main Activity:Asleep/ Employment/ Study between  15:10 and  15:20")
    WIT6_068 = (689, " No Answer  between  15:10 and  15:20")
    ACT1_069 = (690, " Main Activity  between  15:20 and  15:30")
    ACT2_069 = (691, " Secondary Activity between  15:20 and  15:30")
    WHER_069 = (692, " Location  between  15:20 and  15:30")
    WIT0_069 = (693, " Alone or with people that you don't know between  15:20 and  15:30")
    WIT1_069 = (694, " With children up to 9 living in your household between  15:20 and  15:30")
    WIT2_069 = (695, " With children aged 10 to 14 living in your household between  15:20 and  15:30")
    WIT3_069 = (696, " With other household members  between  15:20 and  15:30")
    WIT4_069 = (697, " With other persons that you know  between  15:20 and  15:30")
    WIT5_069 = (698, " Main Activity:Asleep/ Employment/ Study between  15:20 and  15:30")
    WIT6_069 = (699, " No Answer  between  15:20 and  15:30")
    ACT1_070 = (700, " Main Activity  between  15:30 and  15:40")
    ACT2_070 = (701, " Secondary Activity between  15:30 and  15:40")
    WHER_070 = (702, " Location  between  15:30 and  15:40")
    WIT0_070 = (703, " Alone or with people that you don't know between  15:30 and  15:40")
    WIT1_070 = (704, " With children up to 9 living in your household between  15:30 and  15:40")
    WIT2_070 = (705, " With children aged 10 to 14 living in your household between  15:30 and  15:40")
    WIT3_070 = (706, " With other household members  between  15:30 and  15:40")
    WIT4_070 = (707, " With other persons that you know  between  15:30 and  15:40")
    WIT5_070 = (708, " Main Activity:Asleep/ Employment/ Study between  15:30 and  15:40")
    WIT6_070 = (709, " No Answer  between  15:30 and  15:40")
    ACT1_071 = (710, " Main Activity  between  15:40 and  15:50")
    ACT2_071 = (711, " Secondary Activity between  15:40 and  15:50")
    WHER_071 = (712, " Location  between  15:40 and  15:50")
    WIT0_071 = (713, " Alone or with people that you don't know between  15:40 and  15:50")
    WIT1_071 = (714, " With children up to 9 living in your household between  15:40 and  15:50")
    WIT2_071 = (715, " With children aged 10 to 14 living in your household between  15:40 and  15:50")
    WIT3_071 = (716, " With other household members  between  15:40 and  15:50")
    WIT4_071 = (717, " With other persons that you know  between  15:40 and  15:50")
    WIT5_071 = (718, " Main Activity:Asleep/ Employment/ Study between  15:40 and  15:50")
    WIT6_071 = (719, " No Answer  between  15:40 and  15:50")
    ACT1_072 = (720, " Main Activity  between  15:50 and  16:00")
    ACT2_072 = (721, " Secondary Activity between  15:50 and  16:00")
    WHER_072 = (722, " Location  between  15:50 and  16:00")
    WIT0_072 = (723, " Alone or with people that you don't know between  15:50 and  16:00")
    WIT1_072 = (724, " With children up to 9 living in your household between  15:50 and  16:00")
    WIT2_072 = (725, " With children aged 10 to 14 living in your household between  15:50 and  16:00")
    WIT3_072 = (726, " With other household members  between  15:50 and  16:00")
    WIT4_072 = (727, " With other persons that you know  between  15:50 and  16:00")
    WIT5_072 = (728, " Main Activity:Asleep/ Employment/ Study between  15:50 and  16:00")
    WIT6_072 = (729, " No Answer  between  15:50 and  16:00")
    ACT1_073 = (730, " Main Activity  between  16:00 and  16:10")
    ACT2_073 = (731, " Secondary Activity between  16:00 and  16:10")
    WHER_073 = (732, " Location  between  16:00 and  16:10")
    WIT0_073 = (733, " Alone or with people that you don't know between  16:00 and  16:10")
    WIT1_073 = (734, " With children up to 9 living in your household between  16:00 and  16:10")
    WIT2_073 = (735, " With children aged 10 to 14 living in your household between  16:00 and  16:10")
    WIT3_073 = (736, " With other household members  between  16:00 and  16:10")
    WIT4_073 = (737, " With other persons that you know  between  16:00 and  16:10")
    WIT5_073 = (738, " Main Activity:Asleep/ Employment/ Study between  16:00 and  16:10")
    WIT6_073 = (739, " No Answer  between  16:00 and  16:10")
    ACT1_074 = (740, " Main Activity  between  16:10 and  16:20")
    ACT2_074 = (741, " Secondary Activity between  16:10 and  16:20")
    WHER_074 = (742, " Location  between  16:10 and  16:20")
    WIT0_074 = (743, " Alone or with people that you don't know between  16:10 and  16:20")
    WIT1_074 = (744, " With children up to 9 living in your household between  16:10 and  16:20")
    WIT2_074 = (745, " With children aged 10 to 14 living in your household between  16:10 and  16:20")
    WIT3_074 = (746, " With other household members  between  16:10 and  16:20")
    WIT4_074 = (747, " With other persons that you know  between  16:10 and  16:20")
    WIT5_074 = (748, " Main Activity:Asleep/ Employment/ Study between  16:10 and  16:20")
    WIT6_074 = (749, " No Answer  between  16:10 and  16:20")
    ACT1_075 = (750, " Main Activity  between  16:20 and  16:30")
    ACT2_075 = (751, " Secondary Activity between  16:20 and  16:30")
    WHER_075 = (752, " Location  between  16:20 and  16:30")
    WIT0_075 = (753, " Alone or with people that you don't know between  16:20 and  16:30")
    WIT1_075 = (754, " With children up to 9 living in your household between  16:20 and  16:30")
    WIT2_075 = (755, " With children aged 10 to 14 living in your household between  16:20 and  16:30")
    WIT3_075 = (756, " With other household members  between  16:20 and  16:30")
    WIT4_075 = (757, " With other persons that you know  between  16:20 and  16:30")
    WIT5_075 = (758, " Main Activity:Asleep/ Employment/ Study between  16:20 and  16:30")
    WIT6_075 = (759, " No Answer  between  16:20 and  16:30")
    ACT1_076 = (760, " Main Activity  between  16:30 and  16:40")
    ACT2_076 = (761, " Secondary Activity between  16:30 and  16:40")
    WHER_076 = (762, " Location  between  16:30 and  16:40")
    WIT0_076 = (763, " Alone or with people that you don't know between  16:30 and  16:40")
    WIT1_076 = (764, " With children up to 9 living in your household between  16:30 and  16:40")
    WIT2_076 = (765, " With children aged 10 to 14 living in your household between  16:30 and  16:40")
    WIT3_076 = (766, " With other household members  between  16:30 and  16:40")
    WIT4_076 = (767, " With other persons that you know  between  16:30 and  16:40")
    WIT5_076 = (768, " Main Activity:Asleep/ Employment/ Study between  16:30 and  16:40")
    WIT6_076 = (769, " No Answer  between  16:30 and  16:40")
    ACT1_077 = (770, " Main Activity  between  16:40 and  16:50")
    ACT2_077 = (771, " Secondary Activity between  16:40 and  16:50")
    WHER_077 = (772, " Location  between  16:40 and  16:50")
    WIT0_077 = (773, " Alone or with people that you don't know between  16:40 and  16:50")
    WIT1_077 = (774, " With children up to 9 living in your household between  16:40 and  16:50")
    WIT2_077 = (775, " With children aged 10 to 14 living in your household between  16:40 and  16:50")
    WIT3_077 = (776, " With other household members  between  16:40 and  16:50")
    WIT4_077 = (777, " With other persons that you know  between  16:40 and  16:50")
    WIT5_077 = (778, " Main Activity:Asleep/ Employment/ Study between  16:40 and  16:50")
    WIT6_077 = (779, " No Answer  between  16:40 and  16:50")
    ACT1_078 = (780, " Main Activity  between  16:50 and  17:00")
    ACT2_078 = (781, " Secondary Activity between  16:50 and  17:00")
    WHER_078 = (782, " Location  between  16:50 and  17:00")
    WIT0_078 = (783, " Alone or with people that you don't know between  16:50 and  17:00")
    WIT1_078 = (784, " With children up to 9 living in your household between  16:50 and  17:00")
    WIT2_078 = (785, " With children aged 10 to 14 living in your household between  16:50 and  17:00")
    WIT3_078 = (786, " With other household members  between  16:50 and  17:00")
    WIT4_078 = (787, " With other persons that you know  between  16:50 and  17:00")
    WIT5_078 = (788, " Main Activity:Asleep/ Employment/ Study between  16:50 and  17:00")
    WIT6_078 = (789, " No Answer  between  16:50 and  17:00")
    ACT1_079 = (790, " Main Activity  between  17:00 and  17:10")
    ACT2_079 = (791, " Secondary Activity between  17:00 and  17:10")
    WHER_079 = (792, " Location  between  17:00 and  17:10")
    WIT0_079 = (793, " Alone or with people that you don't know between  17:00 and  17:10")
    WIT1_079 = (794, " With children up to 9 living in your household between  17:00 and  17:10")
    WIT2_079 = (795, " With children aged 10 to 14 living in your household between  17:00 and  17:10")
    WIT3_079 = (796, " With other household members  between  17:00 and  17:10")
    WIT4_079 = (797, " With other persons that you know  between  17:00 and  17:10")
    WIT5_079 = (798, " Main Activity:Asleep/ Employment/ Study between  17:00 and  17:10")
    WIT6_079 = (799, " No Answer  between  17:00 and  17:10")
    ACT1_080 = (800, " Main Activity  between  17:10 and  17:20")
    ACT2_080 = (801, " Secondary Activity between  17:10 and  17:20")
    WHER_080 = (802, " Location  between  17:10 and  17:20")
    WIT0_080 = (803, " Alone or with people that you don't know between  17:10 and  17:20")
    WIT1_080 = (804, " With children up to 9 living in your household between  17:10 and  17:20")
    WIT2_080 = (805, " With children aged 10 to 14 living in your household between  17:10 and  17:20")
    WIT3_080 = (806, " With other household members  between  17:10 and  17:20")
    WIT4_080 = (807, " With other persons that you know  between  17:10 and  17:20")
    WIT5_080 = (808, " Main Activity:Asleep/ Employment/ Study between  17:10 and  17:20")
    WIT6_080 = (809, " No Answer  between  17:10 and  17:20")
    ACT1_081 = (810, " Main Activity  between  17:20 and  17:30")
    ACT2_081 = (811, " Secondary Activity between  17:20 and  17:30")
    WHER_081 = (812, " Location  between  17:20 and  17:30")
    WIT0_081 = (813, " Alone or with people that you don't know between  17:20 and  17:30")
    WIT1_081 = (814, " With children up to 9 living in your household between  17:20 and  17:30")
    WIT2_081 = (815, " With children aged 10 to 14 living in your household between  17:20 and  17:30")
    WIT3_081 = (816, " With other household members  between  17:20 and  17:30")
    WIT4_081 = (817, " With other persons that you know  between  17:20 and  17:30")
    WIT5_081 = (818, " Main Activity:Asleep/ Employment/ Study between  17:20 and  17:30")
    WIT6_081 = (819, " No Answer  between  17:20 and  17:30")
    ACT1_082 = (820, " Main Activity  between  17:30 and  17:40")
    ACT2_082 = (821, " Secondary Activity between  17:30 and  17:40")
    WHER_082 = (822, " Location  between  17:30 and  17:40")
    WIT0_082 = (823, " Alone or with people that you don't know between  17:30 and  17:40")
    WIT1_082 = (824, " With children up to 9 living in your household between  17:30 and  17:40")
    WIT2_082 = (825, " With children aged 10 to 14 living in your household between  17:30 and  17:40")
    WIT3_082 = (826, " With other household members  between  17:30 and  17:40")
    WIT4_082 = (827, " With other persons that you know  between  17:30 and  17:40")
    WIT5_082 = (828, " Main Activity:Asleep/ Employment/ Study between  17:30 and  17:40")
    WIT6_082 = (829, " No Answer  between  17:30 and  17:40")
    ACT1_083 = (830, " Main Activity  between  17:40 and  17:50")
    ACT2_083 = (831, " Secondary Activity between  17:40 and  17:50")
    WHER_083 = (832, " Location  between  17:40 and  17:50")
    WIT0_083 = (833, " Alone or with people that you don't know between  17:40 and  17:50")
    WIT1_083 = (834, " With children up to 9 living in your household between  17:40 and  17:50")
    WIT2_083 = (835, " With children aged 10 to 14 living in your household between  17:40 and  17:50")
    WIT3_083 = (836, " With other household members  between  17:40 and  17:50")
    WIT4_083 = (837, " With other persons that you know  between  17:40 and  17:50")
    WIT5_083 = (838, " Main Activity:Asleep/ Employment/ Study between  17:40 and  17:50")
    WIT6_083 = (839, " No Answer  between  17:40 and  17:50")
    ACT1_084 = (840, " Main Activity  between  17:50 and  18:00")
    ACT2_084 = (841, " Secondary Activity between  17:50 and  18:00")
    WHER_084 = (842, " Location  between  17:50 and  18:00")
    WIT0_084 = (843, " Alone or with people that you don't know between  17:50 and  18:00")
    WIT1_084 = (844, " With children up to 9 living in your household between  17:50 and  18:00")
    WIT2_084 = (845, " With children aged 10 to 14 living in your household between  17:50 and  18:00")
    WIT3_084 = (846, " With other household members  between  17:50 and  18:00")
    WIT4_084 = (847, " With other persons that you know  between  17:50 and  18:00")
    WIT5_084 = (848, " Main Activity:Asleep/ Employment/ Study between  17:50 and  18:00")
    WIT6_084 = (849, " No Answer  between  17:50 and  18:00")
    ACT1_085 = (850, " Main Activity  between  18:00 and  18:10")
    ACT2_085 = (851, " Secondary Activity between  18:00 and  18:10")
    WHER_085 = (852, " Location  between  18:00 and  18:10")
    WIT0_085 = (853, " Alone or with people that you don't know between  18:00 and  18:10")
    WIT1_085 = (854, " With children up to 9 living in your household between  18:00 and  18:10")
    WIT2_085 = (855, " With children aged 10 to 14 living in your household between  18:00 and  18:10")
    WIT3_085 = (856, " With other household members  between  18:00 and  18:10")
    WIT4_085 = (857, " With other persons that you know  between  18:00 and  18:10")
    WIT5_085 = (858, " Main Activity:Asleep/ Employment/ Study between  18:00 and  18:10")
    WIT6_085 = (859, " No Answer  between  18:00 and  18:10")
    ACT1_086 = (860, " Main Activity  between  18:10 and  18:20")
    ACT2_086 = (861, " Secondary Activity between  18:10 and  18:20")
    WHER_086 = (862, " Location  between  18:10 and  18:20")
    WIT0_086 = (863, " Alone or with people that you don't know between  18:10 and  18:20")
    WIT1_086 = (864, " With children up to 9 living in your household between  18:10 and  18:20")
    WIT2_086 = (865, " With children aged 10 to 14 living in your household between  18:10 and  18:20")
    WIT3_086 = (866, " With other household members  between  18:10 and  18:20")
    WIT4_086 = (867, " With other persons that you know  between  18:10 and  18:20")
    WIT5_086 = (868, " Main Activity:Asleep/ Employment/ Study between  18:10 and  18:20")
    WIT6_086 = (869, " No Answer  between  18:10 and  18:20")
    ACT1_087 = (870, " Main Activity  between  18:20 and  18:30")
    ACT2_087 = (871, " Secondary Activity between  18:20 and  18:30")
    WHER_087 = (872, " Location  between  18:20 and  18:30")
    WIT0_087 = (873, " Alone or with people that you don't know between  18:20 and  18:30")
    WIT1_087 = (874, " With children up to 9 living in your household between  18:20 and  18:30")
    WIT2_087 = (875, " With children aged 10 to 14 living in your household between  18:20 and  18:30")
    WIT3_087 = (876, " With other household members  between  18:20 and  18:30")
    WIT4_087 = (877, " With other persons that you know  between  18:20 and  18:30")
    WIT5_087 = (878, " Main Activity:Asleep/ Employment/ Study between  18:20 and  18:30")
    WIT6_087 = (879, " No Answer  between  18:20 and  18:30")
    ACT1_088 = (880, " Main Activity  between  18:30 and  18:40")
    ACT2_088 = (881, " Secondary Activity between  18:30 and  18:40")
    WHER_088 = (882, " Location  between  18:30 and  18:40")
    WIT0_088 = (883, " Alone or with people that you don't know between  18:30 and  18:40")
    WIT1_088 = (884, " With children up to 9 living in your household between  18:30 and  18:40")
    WIT2_088 = (885, " With children aged 10 to 14 living in your household between  18:30 and  18:40")
    WIT3_088 = (886, " With other household members  between  18:30 and  18:40")
    WIT4_088 = (887, " With other persons that you know  between  18:30 and  18:40")
    WIT5_088 = (888, " Main Activity:Asleep/ Employment/ Study between  18:30 and  18:40")
    WIT6_088 = (889, " No Answer  between  18:30 and  18:40")
    ACT1_089 = (890, " Main Activity  between  18:40 and  18:50")
    ACT2_089 = (891, " Secondary Activity between  18:40 and  18:50")
    WHER_089 = (892, " Location  between  18:40 and  18:50")
    WIT0_089 = (893, " Alone or with people that you don't know between  18:40 and  18:50")
    WIT1_089 = (894, " With children up to 9 living in your household between  18:40 and  18:50")
    WIT2_089 = (895, " With children aged 10 to 14 living in your household between  18:40 and  18:50")
    WIT3_089 = (896, " With other household members  between  18:40 and  18:50")
    WIT4_089 = (897, " With other persons that you know  between  18:40 and  18:50")
    WIT5_089 = (898, " Main Activity:Asleep/ Employment/ Study between  18:40 and  18:50")
    WIT6_089 = (899, " No Answer  between  18:40 and  18:50")
    ACT1_090 = (900, " Main Activity  between  18:50 and  19:00")
    ACT2_090 = (901, " Secondary Activity between  18:50 and  19:00")
    WHER_090 = (902, " Location  between  18:50 and  19:00")
    WIT0_090 = (903, " Alone or with people that you don't know between  18:50 and  19:00")
    WIT1_090 = (904, " With children up to 9 living in your household between  18:50 and  19:00")
    WIT2_090 = (905, " With children aged 10 to 14 living in your household between  18:50 and  19:00")
    WIT3_090 = (906, " With other household members  between  18:50 and  19:00")
    WIT4_090 = (907, " With other persons that you know  between  18:50 and  19:00")
    WIT5_090 = (908, " Main Activity:Asleep/ Employment/ Study between  18:50 and  19:00")
    WIT6_090 = (909, " No Answer  between  18:50 and  19:00")
    ACT1_091 = (910, " Main Activity  between  19:00 and  19:10")
    ACT2_091 = (911, " Secondary Activity between  19:00 and  19:10")
    WHER_091 = (912, " Location  between  19:00 and  19:10")
    WIT0_091 = (913, " Alone or with people that you don't know between  19:00 and  19:10")
    WIT1_091 = (914, " With children up to 9 living in your household between  19:00 and  19:10")
    WIT2_091 = (915, " With children aged 10 to 14 living in your household between  19:00 and  19:10")
    WIT3_091 = (916, " With other household members  between  19:00 and  19:10")
    WIT4_091 = (917, " With other persons that you know  between  19:00 and  19:10")
    WIT5_091 = (918, " Main Activity:Asleep/ Employment/ Study between  19:00 and  19:10")
    WIT6_091 = (919, " No Answer  between  19:00 and  19:10")
    ACT1_092 = (920, " Main Activity  between  19:10 and  19:20")
    ACT2_092 = (921, " Secondary Activity between  19:10 and  19:20")
    WHER_092 = (922, " Location  between  19:10 and  19:20")
    WIT0_092 = (923, " Alone or with people that you don't know between  19:10 and  19:20")
    WIT1_092 = (924, " With children up to 9 living in your household between  19:10 and  19:20")
    WIT2_092 = (925, " With children aged 10 to 14 living in your household between  19:10 and  19:20")
    WIT3_092 = (926, " With other household members  between  19:10 and  19:20")
    WIT4_092 = (927, " With other persons that you know  between  19:10 and  19:20")
    WIT5_092 = (928, " Main Activity:Asleep/ Employment/ Study between  19:10 and  19:20")
    WIT6_092 = (929, " No Answer  between  19:10 and  19:20")
    ACT1_093 = (930, " Main Activity  between  19:20 and  19:30")
    ACT2_093 = (931, " Secondary Activity between  19:20 and  19:30")
    WHER_093 = (932, " Location  between  19:20 and  19:30")
    WIT0_093 = (933, " Alone or with people that you don't know between  19:20 and  19:30")
    WIT1_093 = (934, " With children up to 9 living in your household between  19:20 and  19:30")
    WIT2_093 = (935, " With children aged 10 to 14 living in your household between  19:20 and  19:30")
    WIT3_093 = (936, " With other household members  between  19:20 and  19:30")
    WIT4_093 = (937, " With other persons that you know  between  19:20 and  19:30")
    WIT5_093 = (938, " Main Activity:Asleep/ Employment/ Study between  19:20 and  19:30")
    WIT6_093 = (939, " No Answer  between  19:20 and  19:30")
    ACT1_094 = (940, " Main Activity  between  19:30 and  19:40")
    ACT2_094 = (941, " Secondary Activity between  19:30 and  19:40")
    WHER_094 = (942, " Location  between  19:30 and  19:40")
    WIT0_094 = (943, " Alone or with people that you don't know between  19:30 and  19:40")
    WIT1_094 = (944, " With children up to 9 living in your household between  19:30 and  19:40")
    WIT2_094 = (945, " With children aged 10 to 14 living in your household between  19:30 and  19:40")
    WIT3_094 = (946, " With other household members  between  19:30 and  19:40")
    WIT4_094 = (947, " With other persons that you know  between  19:30 and  19:40")
    WIT5_094 = (948, " Main Activity:Asleep/ Employment/ Study between  19:30 and  19:40")
    WIT6_094 = (949, " No Answer  between  19:30 and  19:40")
    ACT1_095 = (950, " Main Activity  between  19:40 and  19:50")
    ACT2_095 = (951, " Secondary Activity between  19:40 and  19:50")
    WHER_095 = (952, " Location  between  19:40 and  19:50")
    WIT0_095 = (953, " Alone or with people that you don't know between  19:40 and  19:50")
    WIT1_095 = (954, " With children up to 9 living in your household between  19:40 and  19:50")
    WIT2_095 = (955, " With children aged 10 to 14 living in your household between  19:40 and  19:50")
    WIT3_095 = (956, " With other household members  between  19:40 and  19:50")
    WIT4_095 = (957, " With other persons that you know  between  19:40 and  19:50")
    WIT5_095 = (958, " Main Activity:Asleep/ Employment/ Study between  19:40 and  19:50")
    WIT6_095 = (959, " No Answer  between  19:40 and  19:50")
    ACT1_096 = (960, " Main Activity  between  19:50 and  20:00")
    ACT2_096 = (961, " Secondary Activity between  19:50 and  20:00")
    WHER_096 = (962, " Location  between  19:50 and  20:00")
    WIT0_096 = (963, " Alone or with people that you don't know between  19:50 and  20:00")
    WIT1_096 = (964, " With children up to 9 living in your household between  19:50 and  20:00")
    WIT2_096 = (965, " With children aged 10 to 14 living in your household between  19:50 and  20:00")
    WIT3_096 = (966, " With other household members  between  19:50 and  20:00")
    WIT4_096 = (967, " With other persons that you know  between  19:50 and  20:00")
    WIT5_096 = (968, " Main Activity:Asleep/ Employment/ Study between  19:50 and  20:00")
    WIT6_096 = (969, " No Answer  between  19:50 and  20:00")
    ACT1_097 = (970, " Main Activity  between  20:00 and  20:10")
    ACT2_097 = (971, " Secondary Activity between  20:00 and  20:10")
    WHER_097 = (972, " Location  between  20:00 and  20:10")
    WIT0_097 = (973, " Alone or with people that you don't know between  20:00 and  20:10")
    WIT1_097 = (974, " With children up to 9 living in your household between  20:00 and  20:10")
    WIT2_097 = (975, " With children aged 10 to 14 living in your household between  20:00 and  20:10")
    WIT3_097 = (976, " With other household members  between  20:00 and  20:10")
    WIT4_097 = (977, " With other persons that you know  between  20:00 and  20:10")
    WIT5_097 = (978, " Main Activity:Asleep/ Employment/ Study between  20:00 and  20:10")
    WIT6_097 = (979, " No Answer  between  20:00 and  20:10")
    ACT1_098 = (980, " Main Activity  between  20:10 and  20:20")
    ACT2_098 = (981, " Secondary Activity between  20:10 and  20:20")
    WHER_098 = (982, " Location  between  20:10 and  20:20")
    WIT0_098 = (983, " Alone or with people that you don't know between  20:10 and  20:20")
    WIT1_098 = (984, " With children up to 9 living in your household between  20:10 and  20:20")
    WIT2_098 = (985, " With children aged 10 to 14 living in your household between  20:10 and  20:20")
    WIT3_098 = (986, " With other household members  between  20:10 and  20:20")
    WIT4_098 = (987, " With other persons that you know  between  20:10 and  20:20")
    WIT5_098 = (988, " Main Activity:Asleep/ Employment/ Study between  20:10 and  20:20")
    WIT6_098 = (989, " No Answer  between  20:10 and  20:20")
    ACT1_099 = (990, " Main Activity  between  20:20 and  20:30")
    ACT2_099 = (991, " Secondary Activity between  20:20 and  20:30")
    WHER_099 = (992, " Location  between  20:20 and  20:30")
    WIT0_099 = (993, " Alone or with people that you don't know between  20:20 and  20:30")
    WIT1_099 = (994, " With children up to 9 living in your household between  20:20 and  20:30")
    WIT2_099 = (995, " With children aged 10 to 14 living in your household between  20:20 and  20:30")
    WIT3_099 = (996, " With other household members  between  20:20 and  20:30")
    WIT4_099 = (997, " With other persons that you know  between  20:20 and  20:30")
    WIT5_099 = (998, " Main Activity:Asleep/ Employment/ Study between  20:20 and  20:30")
    WIT6_099 = (999, " No Answer  between  20:20 and  20:30")
    ACT1_100 = (1000, " Main Activity  between  20:30 and  20:40")
    ACT2_100 = (1001, " Secondary Activity between  20:30 and  20:40")
    WHER_100 = (1002, " Location  between  20:30 and  20:40")
    WIT0_100 = (1003, " Alone or with people that you don't know between  20:30 and  20:40")
    WIT1_100 = (1004, " With children up to 9 living in your household between  20:30 and  20:40")
    WIT2_100 = (1005, " With children aged 10 to 14 living in your household between  20:30 and  20:40")
    WIT3_100 = (1006, " With other household members  between  20:30 and  20:40")
    WIT4_100 = (1007, " With other persons that you know  between  20:30 and  20:40")
    WIT5_100 = (1008, " Main Activity:Asleep/ Employment/ Study between  20:30 and  20:40")
    WIT6_100 = (1009, " No Answer  between  20:30 and  20:40")
    ACT1_101 = (1010, " Main Activity  between  20:40 and  20:50")
    ACT2_101 = (1011, " Secondary Activity between  20:40 and  20:50")
    WHER_101 = (1012, " Location  between  20:40 and  20:50")
    WIT0_101 = (1013, " Alone or with people that you don't know between  20:40 and  20:50")
    WIT1_101 = (1014, " With children up to 9 living in your household between  20:40 and  20:50")
    WIT2_101 = (1015, " With children aged 10 to 14 living in your household between  20:40 and  20:50")
    WIT3_101 = (1016, " With other household members  between  20:40 and  20:50")
    WIT4_101 = (1017, " With other persons that you know  between  20:40 and  20:50")
    WIT5_101 = (1018, " Main Activity:Asleep/ Employment/ Study between  20:40 and  20:50")
    WIT6_101 = (1019, " No Answer  between  20:40 and  20:50")
    ACT1_102 = (1020, " Main Activity  between  20:50 and  21:00")
    ACT2_102 = (1021, " Secondary Activity between  20:50 and  21:00")
    WHER_102 = (1022, " Location  between  20:50 and  21:00")
    WIT0_102 = (1023, " Alone or with people that you don't know between  20:50 and  21:00")
    WIT1_102 = (1024, " With children up to 9 living in your household between  20:50 and  21:00")
    WIT2_102 = (1025, " With children aged 10 to 14 living in your household between  20:50 and  21:00")
    WIT3_102 = (1026, " With other household members  between  20:50 and  21:00")
    WIT4_102 = (1027, " With other persons that you know  between  20:50 and  21:00")
    WIT5_102 = (1028, " Main Activity:Asleep/ Employment/ Study between  20:50 and  21:00")
    WIT6_102 = (1029, " No Answer  between  20:50 and  21:00")
    ACT1_103 = (1030, " Main Activity  between  21:00 and  21:10")
    ACT2_103 = (1031, " Secondary Activity between  21:00 and  21:10")
    WHER_103 = (1032, " Location  between  21:00 and  21:10")
    WIT0_103 = (1033, " Alone or with people that you don't know between  21:00 and  21:10")
    WIT1_103 = (1034, " With children up to 9 living in your household between  21:00 and  21:10")
    WIT2_103 = (1035, " With children aged 10 to 14 living in your household between  21:00 and  21:10")
    WIT3_103 = (1036, " With other household members  between  21:00 and  21:10")
    WIT4_103 = (1037, " With other persons that you know  between  21:00 and  21:10")
    WIT5_103 = (1038, " Main Activity:Asleep/ Employment/ Study between  21:00 and  21:10")
    WIT6_103 = (1039, " No Answer  between  21:00 and  21:10")
    ACT1_104 = (1040, " Main Activity  between  21:10 and  21:20")
    ACT2_104 = (1041, " Secondary Activity between  21:10 and  21:20")
    WHER_104 = (1042, " Location  between  21:10 and  21:20")
    WIT0_104 = (1043, " Alone or with people that you don't know between  21:10 and  21:20")
    WIT1_104 = (1044, " With children up to 9 living in your household between  21:10 and  21:20")
    WIT2_104 = (1045, " With children aged 10 to 14 living in your household between  21:10 and  21:20")
    WIT3_104 = (1046, " With other household members  between  21:10 and  21:20")
    WIT4_104 = (1047, " With other persons that you know  between  21:10 and  21:20")
    WIT5_104 = (1048, " Main Activity:Asleep/ Employment/ Study between  21:10 and  21:20")
    WIT6_104 = (1049, " No Answer  between  21:10 and  21:20")
    ACT1_105 = (1050, " Main Activity  between  21:20 and  21:30")
    ACT2_105 = (1051, " Secondary Activity between  21:20 and  21:30")
    WHER_105 = (1052, " Location  between  21:20 and  21:30")
    WIT0_105 = (1053, " Alone or with people that you don't know between  21:20 and  21:30")
    WIT1_105 = (1054, " With children up to 9 living in your household between  21:20 and  21:30")
    WIT2_105 = (1055, " With children aged 10 to 14 living in your household between  21:20 and  21:30")
    WIT3_105 = (1056, " With other household members  between  21:20 and  21:30")
    WIT4_105 = (1057, " With other persons that you know  between  21:20 and  21:30")
    WIT5_105 = (1058, " Main Activity:Asleep/ Employment/ Study between  21:20 and  21:30")
    WIT6_105 = (1059, " No Answer  between  21:20 and  21:30")
    ACT1_106 = (1060, " Main Activity  between  21:30 and  21:40")
    ACT2_106 = (1061, " Secondary Activity between  21:30 and  21:40")
    WHER_106 = (1062, " Location  between  21:30 and  21:40")
    WIT0_106 = (1063, " Alone or with people that you don't know between  21:30 and  21:40")
    WIT1_106 = (1064, " With children up to 9 living in your household between  21:30 and  21:40")
    WIT2_106 = (1065, " With children aged 10 to 14 living in your household between  21:30 and  21:40")
    WIT3_106 = (1066, " With other household members  between  21:30 and  21:40")
    WIT4_106 = (1067, " With other persons that you know  between  21:30 and  21:40")
    WIT5_106 = (1068, " Main Activity:Asleep/ Employment/ Study between  21:30 and  21:40")
    WIT6_106 = (1069, " No Answer  between  21:30 and  21:40")
    ACT1_107 = (1070, " Main Activity  between  21:40 and  21:50")
    ACT2_107 = (1071, " Secondary Activity between  21:40 and  21:50")
    WHER_107 = (1072, " Location  between  21:40 and  21:50")
    WIT0_107 = (1073, " Alone or with people that you don't know between  21:40 and  21:50")
    WIT1_107 = (1074, " With children up to 9 living in your household between  21:40 and  21:50")
    WIT2_107 = (1075, " With children aged 10 to 14 living in your household between  21:40 and  21:50")
    WIT3_107 = (1076, " With other household members  between  21:40 and  21:50")
    WIT4_107 = (1077, " With other persons that you know  between  21:40 and  21:50")
    WIT5_107 = (1078, " Main Activity:Asleep/ Employment/ Study between  21:40 and  21:50")
    WIT6_107 = (1079, " No Answer  between  21:40 and  21:50")
    ACT1_108 = (1080, " Main Activity  between  21:50 and  22:00")
    ACT2_108 = (1081, " Secondary Activity between  21:50 and  22:00")
    WHER_108 = (1082, " Location  between  21:50 and  22:00")
    WIT0_108 = (1083, " Alone or with people that you don't know between  21:50 and  22:00")
    WIT1_108 = (1084, " With children up to 9 living in your household between  21:50 and  22:00")
    WIT2_108 = (1085, " With children aged 10 to 14 living in your household between  21:50 and  22:00")
    WIT3_108 = (1086, " With other household members  between  21:50 and  22:00")
    WIT4_108 = (1087, " With other persons that you know  between  21:50 and  22:00")
    WIT5_108 = (1088, " Main Activity:Asleep/ Employment/ Study between  21:50 and  22:00")
    WIT6_108 = (1089, " No Answer  between  21:50 and  22:00")
    ACT1_109 = (1090, " Main Activity  between  22:00 and  22:10")
    ACT2_109 = (1091, " Secondary Activity between  22:00 and  22:10")
    WHER_109 = (1092, " Location  between  22:00 and  22:10")
    WIT0_109 = (1093, " Alone or with people that you don't know between  22:00 and  22:10")
    WIT1_109 = (1094, " With children up to 9 living in your household between  22:00 and  22:10")
    WIT2_109 = (1095, " With children aged 10 to 14 living in your household between  22:00 and  22:10")
    WIT3_109 = (1096, " With other household members  between  22:00 and  22:10")
    WIT4_109 = (1097, " With other persons that you know  between  22:00 and  22:10")
    WIT5_109 = (1098, " Main Activity:Asleep/ Employment/ Study between  22:00 and  22:10")
    WIT6_109 = (1099, " No Answer  between  22:00 and  22:10")
    ACT1_110 = (1100, " Main Activity  between  22:10 and  22:20")
    ACT2_110 = (1101, " Secondary Activity between  22:10 and  22:20")
    WHER_110 = (1102, " Location  between  22:10 and  22:20")
    WIT0_110 = (1103, " Alone or with people that you don't know between  22:10 and  22:20")
    WIT1_110 = (1104, " With children up to 9 living in your household between  22:10 and  22:20")
    WIT2_110 = (1105, " With children aged 10 to 14 living in your household between  22:10 and  22:20")
    WIT3_110 = (1106, " With other household members  between  22:10 and  22:20")
    WIT4_110 = (1107, " With other persons that you know  between  22:10 and  22:20")
    WIT5_110 = (1108, " Main Activity:Asleep/ Employment/ Study between  22:10 and  22:20")
    WIT6_110 = (1109, " No Answer  between  22:10 and  22:20")
    ACT1_111 = (1110, " Main Activity  between  22:20 and  22:30")
    ACT2_111 = (1111, " Secondary Activity between  22:20 and  22:30")
    WHER_111 = (1112, " Location  between  22:20 and  22:30")
    WIT0_111 = (1113, " Alone or with people that you don't know between  22:20 and  22:30")
    WIT1_111 = (1114, " With children up to 9 living in your household between  22:20 and  22:30")
    WIT2_111 = (1115, " With children aged 10 to 14 living in your household between  22:20 and  22:30")
    WIT3_111 = (1116, " With other household members  between  22:20 and  22:30")
    WIT4_111 = (1117, " With other persons that you know  between  22:20 and  22:30")
    WIT5_111 = (1118, " Main Activity:Asleep/ Employment/ Study between  22:20 and  22:30")
    WIT6_111 = (1119, " No Answer  between  22:20 and  22:30")
    ACT1_112 = (1120, " Main Activity  between  22:30 and  22:40")
    ACT2_112 = (1121, " Secondary Activity between  22:30 and  22:40")
    WHER_112 = (1122, " Location  between  22:30 and  22:40")
    WIT0_112 = (1123, " Alone or with people that you don't know between  22:30 and  22:40")
    WIT1_112 = (1124, " With children up to 9 living in your household between  22:30 and  22:40")
    WIT2_112 = (1125, " With children aged 10 to 14 living in your household between  22:30 and  22:40")
    WIT3_112 = (1126, " With other household members  between  22:30 and  22:40")
    WIT4_112 = (1127, " With other persons that you know  between  22:30 and  22:40")
    WIT5_112 = (1128, " Main Activity:Asleep/ Employment/ Study between  22:30 and  22:40")
    WIT6_112 = (1129, " No Answer  between  22:30 and  22:40")
    ACT1_113 = (1130, " Main Activity  between  22:40 and  22:50")
    ACT2_113 = (1131, " Secondary Activity between  22:40 and  22:50")
    WHER_113 = (1132, " Location  between  22:40 and  22:50")
    WIT0_113 = (1133, " Alone or with people that you don't know between  22:40 and  22:50")
    WIT1_113 = (1134, " With children up to 9 living in your household between  22:40 and  22:50")
    WIT2_113 = (1135, " With children aged 10 to 14 living in your household between  22:40 and  22:50")
    WIT3_113 = (1136, " With other household members  between  22:40 and  22:50")
    WIT4_113 = (1137, " With other persons that you know  between  22:40 and  22:50")
    WIT5_113 = (1138, " Main Activity:Asleep/ Employment/ Study between  22:40 and  22:50")
    WIT6_113 = (1139, " No Answer  between  22:40 and  22:50")
    ACT1_114 = (1140, " Main Activity  between  22:50 and  23:00")
    ACT2_114 = (1141, " Secondary Activity between  22:50 and  23:00")
    WHER_114 = (1142, " Location  between  22:50 and  23:00")
    WIT0_114 = (1143, " Alone or with people that you don't know between  22:50 and  23:00")
    WIT1_114 = (1144, " With children up to 9 living in your household between  22:50 and  23:00")
    WIT2_114 = (1145, " With children aged 10 to 14 living in your household between  22:50 and  23:00")
    WIT3_114 = (1146, " With other household members  between  22:50 and  23:00")
    WIT4_114 = (1147, " With other persons that you know  between  22:50 and  23:00")
    WIT5_114 = (1148, " Main Activity:Asleep/ Employment/ Study between  22:50 and  23:00")
    WIT6_114 = (1149, " No Answer  between  22:50 and  23:00")
    ACT1_115 = (1150, " Main Activity  between  23:00 and  23:10")
    ACT2_115 = (1151, " Secondary Activity between  23:00 and  23:10")
    WHER_115 = (1152, " Location  between  23:00 and  23:10")
    WIT0_115 = (1153, " Alone or with people that you don't know between  23:00 and  23:10")
    WIT1_115 = (1154, " With children up to 9 living in your household between  23:00 and  23:10")
    WIT2_115 = (1155, " With children aged 10 to 14 living in your household between  23:00 and  23:10")
    WIT3_115 = (1156, " With other household members  between  23:00 and  23:10")
    WIT4_115 = (1157, " With other persons that you know  between  23:00 and  23:10")
    WIT5_115 = (1158, " Main Activity:Asleep/ Employment/ Study between  23:00 and  23:10")
    WIT6_115 = (1159, " No Answer  between  23:00 and  23:10")
    ACT1_116 = (1160, " Main Activity  between  23:10 and  23:20")
    ACT2_116 = (1161, " Secondary Activity between  23:10 and  23:20")
    WHER_116 = (1162, " Location  between  23:10 and  23:20")
    WIT0_116 = (1163, " Alone or with people that you don't know between  23:10 and  23:20")
    WIT1_116 = (1164, " With children up to 9 living in your household between  23:10 and  23:20")
    WIT2_116 = (1165, " With children aged 10 to 14 living in your household between  23:10 and  23:20")
    WIT3_116 = (1166, " With other household members  between  23:10 and  23:20")
    WIT4_116 = (1167, " With other persons that you know  between  23:10 and  23:20")
    WIT5_116 = (1168, " Main Activity:Asleep/ Employment/ Study between  23:10 and  23:20")
    WIT6_116 = (1169, " No Answer  between  23:10 and  23:20")
    ACT1_117 = (1170, " Main Activity  between  23:20 and  23:30")
    ACT2_117 = (1171, " Secondary Activity between  23:20 and  23:30")
    WHER_117 = (1172, " Location  between  23:20 and  23:30")
    WIT0_117 = (1173, " Alone or with people that you don't know between  23:20 and  23:30")
    WIT1_117 = (1174, " With children up to 9 living in your household between  23:20 and  23:30")
    WIT2_117 = (1175, " With children aged 10 to 14 living in your household between  23:20 and  23:30")
    WIT3_117 = (1176, " With other household members  between  23:20 and  23:30")
    WIT4_117 = (1177, " With other persons that you know  between  23:20 and  23:30")
    WIT5_117 = (1178, " Main Activity:Asleep/ Employment/ Study between  23:20 and  23:30")
    WIT6_117 = (1179, " No Answer  between  23:20 and  23:30")
    ACT1_118 = (1180, " Main Activity  between  23:30 and  23:40")
    ACT2_118 = (1181, " Secondary Activity between  23:30 and  23:40")
    WHER_118 = (1182, " Location  between  23:30 and  23:40")
    WIT0_118 = (1183, " Alone or with people that you don't know between  23:30 and  23:40")
    WIT1_118 = (1184, " With children up to 9 living in your household between  23:30 and  23:40")
    WIT2_118 = (1185, " With children aged 10 to 14 living in your household between  23:30 and  23:40")
    WIT3_118 = (1186, " With other household members  between  23:30 and  23:40")
    WIT4_118 = (1187, " With other persons that you know  between  23:30 and  23:40")
    WIT5_118 = (1188, " Main Activity:Asleep/ Employment/ Study between  23:30 and  23:40")
    WIT6_118 = (1189, " No Answer  between  23:30 and  23:40")
    ACT1_119 = (1190, " Main Activity  between  23:40 and  23:50")
    ACT2_119 = (1191, " Secondary Activity between  23:40 and  23:50")
    WHER_119 = (1192, " Location  between  23:40 and  23:50")
    WIT0_119 = (1193, " Alone or with people that you don't know between  23:40 and  23:50")
    WIT1_119 = (1194, " With children up to 9 living in your household between  23:40 and  23:50")
    WIT2_119 = (1195, " With children aged 10 to 14 living in your household between  23:40 and  23:50")
    WIT3_119 = (1196, " With other household members  between  23:40 and  23:50")
    WIT4_119 = (1197, " With other persons that you know  between  23:40 and  23:50")
    WIT5_119 = (1198, " Main Activity:Asleep/ Employment/ Study between  23:40 and  23:50")
    WIT6_119 = (1199, " No Answer  between  23:40 and  23:50")
    ACT1_120 = (1200, " Main Activity  between  23:50 and  0:00")
    ACT2_120 = (1201, " Secondary Activity between  23:50 and  0:00")
    WHER_120 = (1202, " Location  between  23:50 and  0:00")
    WIT0_120 = (1203, " Alone or with people that you don't know between  23:50 and  0:00")
    WIT1_120 = (1204, " With children up to 9 living in your household between  23:50 and  0:00")
    WIT2_120 = (1205, " With children aged 10 to 14 living in your household between  23:50 and  0:00")
    WIT3_120 = (1206, " With other household members  between  23:50 and  0:00")
    WIT4_120 = (1207, " With other persons that you know  between  23:50 and  0:00")
    WIT5_120 = (1208, " Main Activity:Asleep/ Employment/ Study between  23:50 and  0:00")
    WIT6_120 = (1209, " No Answer  between  23:50 and  0:00")
    ACT1_121 = (1210, " Main Activity  between  0:00 and  0:10")
    ACT2_121 = (1211, " Secondary Activity between  0:00 and  0:10")
    WHER_121 = (1212, " Location  between  0:00 and  0:10")
    WIT0_121 = (1213, " Alone or with people that you don't know between  0:00 and  0:10")
    WIT1_121 = (1214, " With children up to 9 living in your household between  0:00 and  0:10")
    WIT2_121 = (1215, " With children aged 10 to 14 living in your household between  0:00 and  0:10")
    WIT3_121 = (1216, " With other household members  between  0:00 and  0:10")
    WIT4_121 = (1217, " With other persons that you know  between  0:00 and  0:10")
    WIT5_121 = (1218, " Main Activity:Asleep/ Employment/ Study between  0:00 and  0:10")
    WIT6_121 = (1219, " No Answer  between  0:00 and  0:10")
    ACT1_122 = (1220, " Main Activity  between  0:10 and  0:20")
    ACT2_122 = (1221, " Secondary Activity between  0:10 and  0:20")
    WHER_122 = (1222, " Location  between  0:10 and  0:20")
    WIT0_122 = (1223, " Alone or with people that you don't know between  0:10 and  0:20")
    WIT1_122 = (1224, " With children up to 9 living in your household between  0:10 and  0:20")
    WIT2_122 = (1225, " With children aged 10 to 14 living in your household between  0:10 and  0:20")
    WIT3_122 = (1226, " With other household members  between  0:10 and  0:20")
    WIT4_122 = (1227, " With other persons that you know  between  0:10 and  0:20")
    WIT5_122 = (1228, " Main Activity:Asleep/ Employment/ Study between  0:10 and  0:20")
    WIT6_122 = (1229, " No Answer  between  0:10 and  0:20")
    ACT1_123 = (1230, " Main Activity  between  0:20 and  0:30")
    ACT2_123 = (1231, " Secondary Activity between  0:20 and  0:30")
    WHER_123 = (1232, " Location  between  0:20 and  0:30")
    WIT0_123 = (1233, " Alone or with people that you don't know between  0:20 and  0:30")
    WIT1_123 = (1234, " With children up to 9 living in your household between  0:20 and  0:30")
    WIT2_123 = (1235, " With children aged 10 to 14 living in your household between  0:20 and  0:30")
    WIT3_123 = (1236, " With other household members  between  0:20 and  0:30")
    WIT4_123 = (1237, " With other persons that you know  between  0:20 and  0:30")
    WIT5_123 = (1238, " Main Activity:Asleep/ Employment/ Study between  0:20 and  0:30")
    WIT6_123 = (1239, " No Answer  between  0:20 and  0:30")
    ACT1_124 = (1240, " Main Activity  between  0:30 and  0:40")
    ACT2_124 = (1241, "Secondary Activity between  0:30 and  0:40")
    WHER_124 = (1242, " Location  between  0:30 and  0:40")
    WIT0_124 = (1243, " Alone or with people that you don't know between  0:30 and  0:40")
    WIT1_124 = (1244, "With children up to 9 living in your household between  0:30 and  0:40 '")
    WIT2_124 = (1245, " With children aged 10 to 14 living in your household between  0:30 and  0:40")
    WIT3_124 = (1246, " With other household members  between  0:30 and  0:40")
    WIT4_124 = (1247, " With other persons that you know  between  0:30 and  0:40")
    WIT5_124 = (1248, " Main Activity:Asleep/ Employment/ Study between  0:30 and  0:40")
    WIT6_124 = (1249, " No Answer  between  0:30 and  0:40")
    ACT1_125 = (1250, " Main Activity  between  0:40 and  0:50")
    ACT2_125 = (1251, "Act2 at time slot125")
    WHER_125 = (1252, " Location  between  0:40 and  0:50")
    WIT0_125 = (1253, " Alone or with people that you don't know between  0:40 and  0:50")
    WIT1_125 = (1254, "With children up to 9 living in your household between  0:40 and  0:50 '")
    WIT2_125 = (1255, " With children aged 10 to 14 living in your household between  0:40 and  0:50")
    WIT3_125 = (1256, " With other household members  between  0:40 and  0:50")
    WIT4_125 = (1257, " With other persons that you know  between  0:40 and  0:50")
    WIT5_125 = (1258, " Main Activity:Asleep/ Employment/ Study between  0:40 and  0:50")
    WIT6_125 = (1259, " No Answer  between  0:40 and  0:50")
    ACT1_126 = (1260, " Main Activity  between  0:50 and  1:00")
    ACT2_126 = (1261, "Act2 at time slot126")
    WHER_126 = (1262, " Location  between  0:50 and  1:00")
    WIT0_126 = (1263, " Alone or with people that you don't know between  0:50 and  1:00")
    WIT1_126 = (1264, " With children up to 9 living in your household between  0:50 and  1:00")
    WIT2_126 = (1265, " With children aged 10 to 14 living in your household between  0:50 and  1:00")
    WIT3_126 = (1266, " With other household members  between  0:50 and  1:00")
    WIT4_126 = (1267, " With other persons that you know  between  0:50 and  1:00")
    WIT5_126 = (1268, " Main Activity:Asleep/ Employment/ Study between  0:50 and  1:00")
    WIT6_126 = (1269, " No Answer  between  0:50 and  1:00")
    ACT1_127 = (1270, " Main Activity  between  1:00 and  1:10")
    ACT2_127 = (1271, " Secondary Activity between  1:00 and  1:10")
    WHER_127 = (1272, " Location  between  1:00 and  1:10")
    WIT0_127 = (1273, " Alone or with people that you don't know between  1:00 and  1:10")
    WIT1_127 = (1274, " With children up to 9 living in your household between  1:00 and  1:10")
    WIT2_127 = (1275, " With children aged 10 to 14 living in your household between  1:00 and  1:10")
    WIT3_127 = (1276, " With other household members  between  1:00 and  1:10")
    WIT4_127 = (1277, " With other persons that you know  between  1:00 and  1:10")
    WIT5_127 = (1278, " Main Activity:Asleep/ Employment/ Study between  1:00 and  1:10")
    WIT6_127 = (1279, " No Answer  between  1:00 and  1:10")
    ACT1_128 = (1280, " Main Activity  between  1:10 and  1:20")
    ACT2_128 = (1281, " Secondary Activity between  1:10 and  1:20")
    WHER_128 = (1282, " Location  between  1:10 and  1:20")
    WIT0_128 = (1283, " Alone or with people that you don't know between  1:10 and  1:20")
    WIT1_128 = (1284, " With children up to 9 living in your household between  1:10 and  1:20")
    WIT2_128 = (1285, " With children aged 10 to 14 living in your household between  1:10 and  1:20")
    WIT3_128 = (1286, " With other household members  between  1:10 and  1:20")
    WIT4_128 = (1287, " With other persons that you know  between  1:10 and  1:20")
    WIT5_128 = (1288, " Main Activity:Asleep/ Employment/ Study between  1:10 and  1:20")
    WIT6_128 = (1289, " No Answer  between  1:10 and  1:20")
    ACT1_129 = (1290, " Main Activity  between  1:20 and  1:30")
    ACT2_129 = (1291, " Secondary Activity between  1:20 and  1:30")
    WHER_129 = (1292, " Location  between  1:20 and  1:30")
    WIT0_129 = (1293, " Alone or with people that you don't know between  1:20 and  1:30")
    WIT1_129 = (1294, " With children up to 9 living in your household between  1:20 and  1:30")
    WIT2_129 = (1295, " With children aged 10 to 14 living in your household between  1:20 and  1:30")
    WIT3_129 = (1296, " With other household members  between  1:20 and  1:30")
    WIT4_129 = (1297, " With other persons that you know  between  1:20 and  1:30")
    WIT5_129 = (1298, " Main Activity:Asleep/ Employment/ Study between  1:20 and  1:30")
    WIT6_129 = (1299, " No Answer  between  1:20 and  1:30")
    ACT1_130 = (1300, " Main Activity  between  1:30 and  1:40")
    ACT2_130 = (1301, " Secondary Activity between  1:30 and  1:40")
    WHER_130 = (1302, " Location  between  1:30 and  1:40")
    WIT0_130 = (1303, " Alone or with people that you don't know between  1:30 and  1:40")
    WIT1_130 = (1304, " With children up to 9 living in your household between  1:30 and  1:40")
    WIT2_130 = (1305, " With children aged 10 to 14 living in your household between  1:30 and  1:40")
    WIT3_130 = (1306, " With other household members  between  1:30 and  1:40")
    WIT4_130 = (1307, " With other persons that you know  between  1:30 and  1:40")
    WIT5_130 = (1308, " Main Activity:Asleep/ Employment/ Study between  1:30 and  1:40")
    WIT6_130 = (1309, " No Answer  between  1:30 and  1:40")
    ACT1_131 = (1310, " Main Activity  between  1:40 and  1:50")
    ACT2_131 = (1311, " Secondary Activity between  1:40 and  1:50")
    WHER_131 = (1312, " Location  between  1:40 and  1:50")
    WIT0_131 = (1313, " Alone or with people that you don't know between  1:40 and  1:50")
    WIT1_131 = (1314, " With children up to 9 living in your household between  1:40 and  1:50")
    WIT2_131 = (1315, " With children aged 10 to 14 living in your household between  1:40 and  1:50")
    WIT3_131 = (1316, " With other household members  between  1:40 and  1:50")
    WIT4_131 = (1317, " With other persons that you know  between  1:40 and  1:50")
    WIT5_131 = (1318, " Main Activity:Asleep/ Employment/ Study between  1:40 and  1:50")
    WIT6_131 = (1319, " No Answer  between  1:40 and  1:50")
    ACT1_132 = (1320, " Main Activity  between  1:50 and  2:00")
    ACT2_132 = (1321, " Secondary Activity between  1:50 and  2:00")
    WHER_132 = (1322, " Location  between  1:50 and  2:00")
    WIT0_132 = (1323, " Alone or with people that you don't know between  1:50 and  2:00")
    WIT1_132 = (1324, " With children up to 9 living in your household between  1:50 and  2:00")
    WIT2_132 = (1325, " With children aged 10 to 14 living in your household between  1:50 and  2:00")
    WIT3_132 = (1326, " With other household members  between  1:50 and  2:00")
    WIT4_132 = (1327, " With other persons that you know  between  1:50 and  2:00")
    WIT5_132 = (1328, " Main Activity:Asleep/ Employment/ Study between  1:50 and  2:00")
    WIT6_132 = (1329, " No Answer  between  1:50 and  2:00")
    ACT1_133 = (1330, " Main Activity  between  2:00 and  2:10")
    ACT2_133 = (1331, " Secondary Activity between  2:00 and  2:10")
    WHER_133 = (1332, " Location  between  2:00 and  2:10")
    WIT0_133 = (1333, " Alone or with people that you don't know between  2:00 and  2:10")
    WIT1_133 = (1334, " With children up to 9 living in your household between  2:00 and  2:10")
    WIT2_133 = (1335, " With children aged 10 to 14 living in your household between  2:00 and  2:10")
    WIT3_133 = (1336, " With other household members  between  2:00 and  2:10")
    WIT4_133 = (1337, " With other persons that you know  between  2:00 and  2:10")
    WIT5_133 = (1338, " Main Activity:Asleep/ Employment/ Study between  2:00 and  2:10")
    WIT6_133 = (1339, " No Answer  between  2:00 and  2:10")
    ACT1_134 = (1340, " Main Activity  between  2:10 and  2:20")
    ACT2_134 = (1341, " Secondary Activity between  2:10 and  2:20")
    WHER_134 = (1342, " Location  between  2:10 and  2:20")
    WIT0_134 = (1343, " Alone or with people that you don't know between  2:10 and  2:20")
    WIT1_134 = (1344, " With children up to 9 living in your household between  2:10 and  2:20")
    WIT2_134 = (1345, " With children aged 10 to 14 living in your household between  2:10 and  2:20")
    WIT3_134 = (1346, " With other household members  between  2:10 and  2:20")
    WIT4_134 = (1347, " With other persons that you know  between  2:10 and  2:20")
    WIT5_134 = (1348, " Main Activity:Asleep/ Employment/ Study between  2:10 and  2:20")
    WIT6_134 = (1349, " No Answer  between  2:10 and  2:20")
    ACT1_135 = (1350, " Main Activity  between  2:20 and  2:30")
    ACT2_135 = (1351, " Secondary Activity between  2:20 and  2:30")
    WHER_135 = (1352, " Location  between  2:20 and  2:30")
    WIT0_135 = (1353, " Alone or with people that you don't know between  2:20 and  2:30")
    WIT1_135 = (1354, " With children up to 9 living in your household between  2:20 and  2:30")
    WIT2_135 = (1355, " With children aged 10 to 14 living in your household between  2:20 and  2:30")
    WIT3_135 = (1356, " With other household members  between  2:20 and  2:30")
    WIT4_135 = (1357, " With other persons that you know  between  2:20 and  2:30")
    WIT5_135 = (1358, " Main Activity:Asleep/ Employment/ Study between  2:20 and  2:30")
    WIT6_135 = (1359, " No Answer  between  2:20 and  2:30")
    ACT1_136 = (1360, " Main Activity  between  2:30 and  2:40")
    ACT2_136 = (1361, " Secondary Activity between  2:30 and  2:40")
    WHER_136 = (1362, " Location  between  2:30 and  2:40")
    WIT0_136 = (1363, " Alone or with people that you don't know between  2:30 and  2:40")
    WIT1_136 = (1364, " With children up to 9 living in your household between  2:30 and  2:40")
    WIT2_136 = (1365, " With children aged 10 to 14 living in your household between  2:30 and  2:40")
    WIT3_136 = (1366, " With other household members  between  2:30 and  2:40")
    WIT4_136 = (1367, " With other persons that you know  between  2:30 and  2:40")
    WIT5_136 = (1368, " Main Activity:Asleep/ Employment/ Study between  2:30 and  2:40")
    WIT6_136 = (1369, " No Answer  between  2:30 and  2:40")
    ACT1_137 = (1370, " Main Activity  between  2:40 and  2:50")
    ACT2_137 = (1371, " Secondary Activity between  2:40 and  2:50")
    WHER_137 = (1372, " Location  between  2:40 and  2:50")
    WIT0_137 = (1373, " Alone or with people that you don't know between  2:40 and  2:50")
    WIT1_137 = (1374, " With children up to 9 living in your household between  2:40 and  2:50")
    WIT2_137 = (1375, " With children aged 10 to 14 living in your household between  2:40 and  2:50")
    WIT3_137 = (1376, " With other household members  between  2:40 and  2:50")
    WIT4_137 = (1377, " With other persons that you know  between  2:40 and  2:50")
    WIT5_137 = (1378, " Main Activity:Asleep/ Employment/ Study between  2:40 and  2:50")
    WIT6_137 = (1379, " No Answer  between  2:40 and  2:50")
    ACT1_138 = (1380, " Main Activity  between  2:50 and  3:00")
    ACT2_138 = (1381, " Secondary Activity between  2:50 and  3:00")
    WHER_138 = (1382, " Location  between  2:50 and  3:00")
    WIT0_138 = (1383, " Alone or with people that you don't know between  2:50 and  3:00")
    WIT1_138 = (1384, " With children up to 9 living in your household between  2:50 and  3:00")
    WIT2_138 = (1385, " With children aged 10 to 14 living in your household between  2:50 and  3:00")
    WIT3_138 = (1386, " With other household members  between  2:50 and  3:00")
    WIT4_138 = (1387, " With other persons that you know  between  2:50 and  3:00")
    WIT5_138 = (1388, " Main Activity:Asleep/ Employment/ Study between  2:50 and  3:00")
    WIT6_138 = (1389, " No Answer  between  2:50 and  3:00")
    ACT1_139 = (1390, " Main Activity  between  3:00 and  3:10")
    ACT2_139 = (1391, " Secondary Activity between  3:00 and  3:10")
    WHER_139 = (1392, " Location  between  3:00 and  3:10")
    WIT0_139 = (1393, " Alone or with people that you don't know between  3:00 and  3:10")
    WIT1_139 = (1394, " With children up to 9 living in your household between  3:00 and  3:10")
    WIT2_139 = (1395, " With children aged 10 to 14 living in your household between  3:00 and  3:10")
    WIT3_139 = (1396, " With other household members  between  3:00 and  3:10")
    WIT4_139 = (1397, " With other persons that you know  between  3:00 and  3:10")
    WIT5_139 = (1398, " Main Activity:Asleep/ Employment/ Study between  3:00 and  3:10")
    WIT6_139 = (1399, " No Answer  between  3:00 and  3:10")
    ACT1_140 = (1400, " Main Activity  between  3:10 and  3:20")
    ACT2_140 = (1401, " Secondary Activity between  3:10 and  3:20")
    WHER_140 = (1402, " Location  between  3:10 and  3:20")
    WIT0_140 = (1403, " Alone or with people that you don't know between  3:10 and  3:20")
    WIT1_140 = (1404, " With children up to 9 living in your household between  3:10 and  3:20")
    WIT2_140 = (1405, " With children aged 10 to 14 living in your household between  3:10 and  3:20")
    WIT3_140 = (1406, " With other household members  between  3:10 and  3:20")
    WIT4_140 = (1407, " With other persons that you know  between  3:10 and  3:20")
    WIT5_140 = (1408, " Main Activity:Asleep/ Employment/ Study between  3:10 and  3:20")
    WIT6_140 = (1409, " No Answer  between  3:10 and  3:20")
    ACT1_141 = (1410, " Main Activity  between  3:20 and  3:30")
    ACT2_141 = (1411, " Secondary Activity between  3:20 and  3:30")
    WHER_141 = (1412, " Location  between  3:20 and  3:30")
    WIT0_141 = (1413, " Alone or with people that you don't know between  3:20 and  3:30")
    WIT1_141 = (1414, " With children up to 9 living in your household between  3:20 and  3:30")
    WIT2_141 = (1415, " With children aged 10 to 14 living in your household between  3:20 and  3:30")
    WIT3_141 = (1416, " With other household members  between  3:20 and  3:30")
    WIT4_141 = (1417, " With other persons that you know  between  3:20 and  3:30")
    WIT5_141 = (1418, " Main Activity:Asleep/ Employment/ Study between  3:20 and  3:30")
    WIT6_141 = (1419, " No Answer  between  3:20 and  3:30")
    ACT1_142 = (1420, " Main Activity  between  3:30 and  3:40")
    ACT2_142 = (1421, " Secondary Activity between  3:30 and  3:40")
    WHER_142 = (1422, " Location  between  3:30 and  3:40")
    WIT0_142 = (1423, " Alone or with people that you don't know between  3:30 and  3:40")
    WIT1_142 = (1424, " With children up to 9 living in your household between  3:30 and  3:40")
    WIT2_142 = (1425, " With children aged 10 to 14 living in your household between  3:30 and  3:40")
    WIT3_142 = (1426, " With other household members  between  3:30 and  3:40")
    WIT4_142 = (1427, " With other persons that you know  between  3:30 and  3:40")
    WIT5_142 = (1428, " Main Activity:Asleep/ Employment/ Study between  3:30 and  3:40")
    WIT6_142 = (1429, " No Answer  between  3:30 and  3:40")
    ACT1_143 = (1430, " Main Activity  between  3:40 and  3:50")
    ACT2_143 = (1431, " Secondary Activity between  3:40 and  3:50")
    WHER_143 = (1432, " Location  between  3:40 and  3:50")
    WIT0_143 = (1433, " Alone or with people that you don't know between  3:40 and  3:50")
    WIT1_143 = (1434, " With children up to 9 living in your household between  3:40 and  3:50")
    WIT2_143 = (1435, " With children aged 10 to 14 living in your household between  3:40 and  3:50")
    WIT3_143 = (1436, " With other household members  between  3:40 and  3:50")
    WIT4_143 = (1437, " With other persons that you know  between  3:40 and  3:50")
    WIT5_143 = (1438, " Main Activity:Asleep/ Employment/ Study between  3:40 and  3:50")
    WIT6_143 = (1439, " No Answer  between  3:40 and  3:50")
    ACT1_144 = (1440, " Main Activity  between  3:50 and  4:00")
    ACT2_144 = (1441, " Secondary Activity between  3:50 and  4:00")
    WHER_144 = (1442, " Location  between  3:50 and  4:00")
    WIT0_144 = (1443, " Alone or with people that you don't know between  3:50 and  4:00")
    WIT1_144 = (1444, " With children up to 9 living in your household between  3:50 and  4:00")
    WIT2_144 = (1445, " With children aged 10 to 14 living in your household between  3:50 and  4:00")
    WIT3_144 = (1446, " With other household members  between  3:50 and  4:00")
    WIT4_144 = (1447, " With other persons that you know  between  3:50 and  4:00")
    WIT5_144 = (1448, " Main Activity:Asleep/ Employment/ Study between  3:50 and  4:00")
    WIT6_144 = (1449, " No Answer  between  3:50 and  4:00")
    KID01 = (1450, " Alone or with people that you don't know between  4:00 and  4:10")
    KID02 = (1451, " Alone or with people that you don't know between  4:10 and  4:20")
    KID03 = (1452, " Alone or with people that you don't know between  4:20 and  4:30")
    KID04 = (1453, " Alone or with people that you don't know between  4:30 and  4:40")
    KID05 = (1454, " Alone or with people that you don't know between  4:40 and  4:50")
    KID06 = (1455, " Alone or with people that you don't know between  4:50 and  5:00")
    KID07 = (1456, " Alone or with people that you don't know between  5:00 and  5:10")
    KID08 = (1457, " Alone or with people that you don't know between  5:10 and  5:20")
    KID09 = (1458, " Alone or with people that you don't know between  5:20 and  5:30")
    KID010 = (1459, " Alone or with people that you don't know between  5:30 and  5:40")
    KID011 = (1460, " Alone or with people that you don't know between  5:40 and  5:50")
    KID012 = (1461, " Alone or with people that you don't know between  5:50 and  6:00")
    KID013 = (1462, " Alone or with people that you don't know between  6:00 and  6:10")
    KID014 = (1463, " Alone or with people that you don't know between  6:10 and  6:20")
    KID015 = (1464, " Alone or with people that you don't know between  6:20 and  6:30")
    KID016 = (1465, " Alone or with people that you don't know between  6:30 and  6:40")
    KID017 = (1466, " Alone or with people that you don't know between  6:40 and  6:50")
    KID018 = (1467, " Alone or with people that you don't know between  6:50 and  7:00")
    KID019 = (1468, " Alone or with people that you don't know between  7:00 and  7:10")
    KID020 = (1469, " Alone or with people that you don't know between  7:10 and  7:20")
    KID021 = (1470, " Alone or with people that you don't know between  7:20 and  7:30")
    KID022 = (1471, " Alone or with people that you don't know between  7:30 and  7:40")
    KID023 = (1472, " Alone or with people that you don't know between  7:40 and  7:50")
    KID024 = (1473, " Alone or with people that you don't know between  7:50 and  8:00")
    KID025 = (1474, " Alone or with people that you don't know between  8:00 and  8:10")
    KID026 = (1475, " Alone or with people that you don't know between  8:10 and  8:20")
    KID027 = (1476, " Alone or with people that you don't know between  8:20 and  8:30")
    KID028 = (1477, " Alone or with people that you don't know between  8:30 and  8:40")
    KID029 = (1478, " Alone or with people that you don't know between  8:40 and  8:50")
    KID030 = (1479, " Alone or with people that you don't know between  8:50 and  9:00")
    KID031 = (1480, " Alone or with people that you don't know between  9:00 and  9:10")
    KID032 = (1481, " Alone or with people that you don't know between  9:10 and  9:20")
    KID033 = (1482, " Alone or with people that you don't know between  9:20 and  9:30")
    KID034 = (1483, " Alone or with people that you don't know between  9:30 and  9:40")
    KID035 = (1484, " Alone or with people that you don't know between  9:40 and  9:50")
    KID036 = (1485, " Alone or with people that you don't know between  9:50 and  10:00")
    KID037 = (1486, " Alone or with people that you don't know between  10:00 and  10:10")
    KID038 = (1487, " Alone or with people that you don't know between  10:10 and  10:20")
    KID039 = (1488, " Alone or with people that you don't know between  10:20 and  10:30")
    KID040 = (1489, " Alone or with people that you don't know between  10:30 and  10:40")
    KID041 = (1490, " Alone or with people that you don't know between  10:40 and  10:50")
    KID042 = (1491, " Alone or with people that you don't know between  10:50 and  11:00")
    KID043 = (1492, " Alone or with people that you don't know between  11:00 and  11:10")
    KID044 = (1493, " Alone or with people that you don't know between  11:10 and  11:20")
    KID045 = (1494, " Alone or with people that you don't know between  11:20 and  11:30")
    KID046 = (1495, " Alone or with people that you don't know between  11:30 and  11:40")
    KID047 = (1496, " Alone or with people that you don't know between  11:40 and  11:50")
    KID048 = (1497, " Alone or with people that you don't know between  11:50 and  12:00")
    KID049 = (1498, " Alone or with people that you don't know between  12:00 and  12:10")
    KID050 = (1499, " Alone or with people that you don't know between  12:10 and  12:20")
    KID051 = (1500, " Alone or with people that you don't know between  12:20 and  12:30")
    KID052 = (1501, " Alone or with people that you don't know between  12:30 and  12:40")
    KID053 = (1502, " Alone or with people that you don't know between  12:40 and  12:50")
    KID054 = (1503, " Alone or with people that you don't know between  12:50 and  13:00")
    KID055 = (1504, " Alone or with people that you don't know between  13:00 and  13:10")
    KID056 = (1505, " Alone or with people that you don't know between  13:10 and  13:20")
    KID057 = (1506, " Alone or with people that you don't know between  13:20 and  13:30")
    KID058 = (1507, " Alone or with people that you don't know between  13:30 and  13:40")
    KID059 = (1508, " Alone or with people that you don't know between  13:40 and  13:50")
    KID060 = (1509, " Alone or with people that you don't know between  13:50 and  14:00")
    KID061 = (1510, " Alone or with people that you don't know between  14:00 and  14:10")
    KID062 = (1511, " Alone or with people that you don't know between  14:10 and  14:20")
    KID063 = (1512, " Alone or with people that you don't know between  14:20 and  14:30")
    KID064 = (1513, " Alone or with people that you don't know between  14:30 and  14:40")
    KID065 = (1514, " Alone or with people that you don't know between  14:40 and  14:50")
    KID066 = (1515, " Alone or with people that you don't know between  14:50 and  15:00")
    KID067 = (1516, " Alone or with people that you don't know between  15:00 and  15:10")
    KID068 = (1517, " Alone or with people that you don't know between  15:10 and  15:20")
    KID069 = (1518, " Alone or with people that you don't know between  15:20 and  15:30")
    KID070 = (1519, " Alone or with people that you don't know between  15:30 and  15:40")
    KID071 = (1520, " Alone or with people that you don't know between  15:40 and  15:50")
    KID072 = (1521, " Alone or with people that you don't know between  15:50 and  16:00")
    KID073 = (1522, " Alone or with people that you don't know between  16:00 and  16:10")
    KID074 = (1523, " Alone or with people that you don't know between  16:10 and  16:20")
    KID075 = (1524, " Alone or with people that you don't know between  16:20 and  16:30")
    KID076 = (1525, " Alone or with people that you don't know between  16:30 and  16:40")
    KID077 = (1526, " Alone or with people that you don't know between  16:40 and  16:50")
    KID078 = (1527, " Alone or with people that you don't know between  16:50 and  17:00")
    KID079 = (1528, " Alone or with people that you don't know between  17:00 and  17:10")
    KID080 = (1529, " Alone or with people that you don't know between  17:10 and  17:20")
    KID081 = (1530, " Alone or with people that you don't know between  17:20 and  17:30")
    KID082 = (1531, " Alone or with people that you don't know between  17:30 and  17:40")
    KID083 = (1532, " Alone or with people that you don't know between  17:40 and  17:50")
    KID084 = (1533, " Alone or with people that you don't know between  17:50 and  18:00")
    KID085 = (1534, " Alone or with people that you don't know between  18:00 and  18:10")
    KID086 = (1535, " Alone or with people that you don't know between  18:10 and  18:20")
    KID087 = (1536, " Alone or with people that you don't know between  18:20 and  18:30")
    KID088 = (1537, " Alone or with people that you don't know between  18:30 and  18:40")
    KID089 = (1538, " Alone or with people that you don't know between  18:40 and  18:50")
    KID090 = (1539, " Alone or with people that you don't know between  18:50 and  19:00")
    KID091 = (1540, " Alone or with people that you don't know between  19:00 and  19:10")
    KID092 = (1541, " Alone or with people that you don't know between  19:10 and  19:20")
    KID093 = (1542, " Alone or with people that you don't know between  19:20 and  19:30")
    KID094 = (1543, " Alone or with people that you don't know between  19:30 and  19:40")
    KID095 = (1544, " Alone or with people that you don't know between  19:40 and  19:50")
    KID096 = (1545, " Alone or with people that you don't know between  19:50 and  20:00")
    KID097 = (1546, " Alone or with people that you don't know between  20:00 and  20:10")
    KID098 = (1547, " Alone or with people that you don't know between  20:10 and  20:20")
    KID099 = (1548, " Alone or with people that you don't know between  20:20 and  20:30")
    KID0100 = (1549, " Alone or with people that you don't know between  20:30 and  20:40")
    KID0101 = (1550, " Alone or with people that you don't know between  20:40 and  20:50")
    KID0102 = (1551, " Alone or with people that you don't know between  20:50 and  21:00")
    KID0103 = (1552, " Alone or with people that you don't know between  21:00 and  21:10")
    KID0104 = (1553, " Alone or with people that you don't know between  21:10 and  21:20")
    KID0105 = (1554, " Alone or with people that you don't know between  21:20 and  21:30")
    KID0106 = (1555, " Alone or with people that you don't know between  21:30 and  21:40")
    KID0107 = (1556, " Alone or with people that you don't know between  21:40 and  21:50")
    KID0108 = (1557, " Alone or with people that you don't know between  21:50 and  22:00")
    KID0109 = (1558, " Alone or with people that you don't know between  22:00 and  22:10")
    KID0110 = (1559, " Alone or with people that you don't know between  22:10 and  22:20")
    KID0111 = (1560, " Alone or with people that you don't know between  22:20 and  22:30")
    KID0112 = (1561, " Alone or with people that you don't know between  22:30 and  22:40")
    KID0113 = (1562, " Alone or with people that you don't know between  22:40 and  22:50")
    KID0114 = (1563, " Alone or with people that you don't know between  22:50 and  23:00")
    KID0115 = (1564, " Alone or with people that you don't know between  23:00 and  23:10")
    KID0116 = (1565, " Alone or with people that you don't know between  23:10 and  23:20")
    KID0117 = (1566, " Alone or with people that you don't know between  23:20 and  23:30")
    KID0118 = (1567, " Alone or with people that you don't know between  23:30 and  23:40")
    KID0119 = (1568, " Alone or with people that you don't know between  23:40 and  23:50")
    KID0120 = (1569, " Alone or with people that you don't know between  23:50 and  0:00")
    KID0121 = (1570, " Alone or with people that you don't know between  0:00 and  0:10")
    KID0122 = (1571, " Alone or with people that you don't know between  0:10 and  0:20")
    KID0123 = (1572, " Alone or with people that you don't know between  0:20 and  0:30")
    KID0124 = (1573, " Alone or with people that you don't know between  0:30 and  0:40")
    KID0125 = (1574, " Alone or with people that you don't know between  0:40 and  0:50")
    KID0126 = (1575, " Alone or with people that you don't know between  0:50 and  1:00")
    KID0127 = (1576, " Alone or with people that you don't know between  1:00 and  1:10")
    KID0128 = (1577, " Alone or with people that you don't know between  1:10 and  1:20")
    KID0129 = (1578, " Alone or with people that you don't know between  1:20 and  1:30")
    KID0130 = (1579, " Alone or with people that you don't know between  1:30 and  1:40")
    KID0131 = (1580, " Alone or with people that you don't know between  1:40 and  1:50")
    KID0132 = (1581, " Alone or with people that you don't know between  1:50 and  2:00")
    KID0133 = (1582, " Alone or with people that you don't know between  2:00 and  2:10")
    KID0134 = (1583, " Alone or with people that you don't know between  2:10 and  2:20")
    KID0135 = (1584, " Alone or with people that you don't know between  2:20 and  2:30")
    KID0136 = (1585, " Alone or with people that you don't know between  2:30 and  2:40")
    KID0137 = (1586, " Alone or with people that you don't know between  2:40 and  2:50")
    KID0138 = (1587, " Alone or with people that you don't know between  2:50 and  3:00")
    KID0139 = (1588, " Alone or with people that you don't know between  3:00 and  3:10")
    KID0140 = (1589, " Alone or with people that you don't know between  3:10 and  3:20")
    KID0141 = (1590, " Alone or with people that you don't know between  3:20 and  3:30")
    KID0142 = (1591, " Alone or with people that you don't know between  3:30 and  3:40")
    KID0143 = (1592, " Alone or with people that you don't know between  3:40 and  3:50")
    KID0144 = (1593, " Alone or with people that you don't know between  3:50 and  4:00")
    KID11 = (1594, " With your parents  between  4:00 and  4:10")
    KID12 = (1595, " With your parents  between  4:10 and  4:20")
    KID13 = (1596, " With your parents  between  4:20 and  4:30")
    KID14 = (1597, " With your parents  between  4:30 and  4:40")
    KID15 = (1598, " With your parents  between  4:40 and  4:50")
    KID16 = (1599, " With your parents  between  4:50 and  5:00")
    KID17 = (1600, " With your parents  between  5:00 and  5:10")
    KID18 = (1601, " With your parents  between  5:10 and  5:20")
    KID19 = (1602, " With your parents  between  5:20 and  5:30")
    KID110 = (1603, " With your parents  between  5:30 and  5:40")
    KID111 = (1604, " With your parents  between  5:40 and  5:50")
    KID112 = (1605, " With your parents  between  5:50 and  6:00")
    KID113 = (1606, " With your parents  between  6:00 and  6:10")
    KID114 = (1607, " With your parents  between  6:10 and  6:20")
    KID115 = (1608, " With your parents  between  6:20 and  6:30")
    KID116 = (1609, " With your parents  between  6:30 and  6:40")
    KID117 = (1610, " With your parents  between  6:40 and  6:50")
    KID118 = (1611, " With your parents  between  6:50 and  7:00")
    KID119 = (1612, " With your parents  between  7:00 and  7:10")
    KID120 = (1613, " With your parents  between  7:10 and  7:20")
    KID121 = (1614, " With your parents  between  7:20 and  7:30")
    KID122 = (1615, " With your parents  between  7:30 and  7:40")
    KID123 = (1616, " With your parents  between  7:40 and  7:50")
    KID124 = (1617, " With your parents  between  7:50 and  8:00")
    KID125 = (1618, " With your parents  between  8:00 and  8:10")
    KID126 = (1619, " With your parents  between  8:10 and  8:20")
    KID127 = (1620, " With your parents  between  8:20 and  8:30")
    KID128 = (1621, " With your parents  between  8:30 and  8:40")
    KID129 = (1622, " With your parents  between  8:40 and  8:50")
    KID130 = (1623, " With your parents  between  8:50 and  9:00")
    KID131 = (1624, " With your parents  between  9:00 and  9:10")
    KID132 = (1625, " With your parents  between  9:10 and  9:20")
    KID133 = (1626, " With your parents  between  9:20 and  9:30")
    KID134 = (1627, " With your parents  between  9:30 and  9:40")
    KID135 = (1628, " With your parents  between  9:40 and  9:50")
    KID136 = (1629, " With your parents  between  9:50 and  10:00")
    KID137 = (1630, " With your parents  between  10:00 and  10:10")
    KID138 = (1631, " With your parents  between  10:10 and  10:20")
    KID139 = (1632, " With your parents  between  10:20 and  10:30")
    KID140 = (1633, " With your parents  between  10:30 and  10:40")
    KID141 = (1634, " With your parents  between  10:40 and  10:50")
    KID142 = (1635, " With your parents  between  10:50 and  11:00")
    KID143 = (1636, " With your parents  between  11:00 and  11:10")
    KID144 = (1637, " With your parents  between  11:10 and  11:20")
    KID145 = (1638, " With your parents  between  11:20 and  11:30")
    KID146 = (1639, " With your parents  between  11:30 and  11:40")
    KID147 = (1640, " With your parents  between  11:40 and  11:50")
    KID148 = (1641, " With your parents  between  11:50 and  12:00")
    KID149 = (1642, " With your parents  between  12:00 and  12:10")
    KID150 = (1643, " With your parents  between  12:10 and  12:20")
    KID151 = (1644, " With your parents  between  12:20 and  12:30")
    KID152 = (1645, " With your parents  between  12:30 and  12:40")
    KID153 = (1646, " With your parents  between  12:40 and  12:50")
    KID154 = (1647, " With your parents  between  12:50 and  13:00")
    KID155 = (1648, " With your parents  between  13:00 and  13:10")
    KID156 = (1649, " With your parents  between  13:10 and  13:20")
    KID157 = (1650, " With your parents  between  13:20 and  13:30")
    KID158 = (1651, " With your parents  between  13:30 and  13:40")
    KID159 = (1652, " With your parents  between  13:40 and  13:50")
    KID160 = (1653, " With your parents  between  13:50 and  14:00")
    KID161 = (1654, " With your parents  between  14:00 and  14:10")
    KID162 = (1655, " With your parents  between  14:10 and  14:20")
    KID163 = (1656, " With your parents  between  14:20 and  14:30")
    KID164 = (1657, " With your parents  between  14:30 and  14:40")
    KID165 = (1658, " With your parents  between  14:40 and  14:50")
    KID166 = (1659, " With your parents  between  14:50 and  15:00")
    KID167 = (1660, " With your parents  between  15:00 and  15:10")
    KID168 = (1661, " With your parents  between  15:10 and  15:20")
    KID169 = (1662, " With your parents  between  15:20 and  15:30")
    KID170 = (1663, " With your parents  between  15:30 and  15:40")
    KID171 = (1664, " With your parents  between  15:40 and  15:50")
    KID172 = (1665, " With your parents  between  15:50 and  16:00")
    KID173 = (1666, " With your parents  between  16:00 and  16:10")
    KID174 = (1667, " With your parents  between  16:10 and  16:20")
    KID175 = (1668, " With your parents  between  16:20 and  16:30")
    KID176 = (1669, " With your parents  between  16:30 and  16:40")
    KID177 = (1670, " With your parents  between  16:40 and  16:50")
    KID178 = (1671, " With your parents  between  16:50 and  17:00")
    KID179 = (1672, " With your parents  between  17:00 and  17:10")
    KID180 = (1673, " With your parents  between  17:10 and  17:20")
    KID181 = (1674, " With your parents  between  17:20 and  17:30")
    KID182 = (1675, " With your parents  between  17:30 and  17:40")
    KID183 = (1676, " With your parents  between  17:40 and  17:50")
    KID184 = (1677, " With your parents  between  17:50 and  18:00")
    KID185 = (1678, " With your parents  between  18:00 and  18:10")
    KID186 = (1679, " With your parents  between  18:10 and  18:20")
    KID187 = (1680, " With your parents  between  18:20 and  18:30")
    KID188 = (1681, " With your parents  between  18:30 and  18:40")
    KID189 = (1682, " With your parents  between  18:40 and  18:50")
    KID190 = (1683, " With your parents  between  18:50 and  19:00")
    KID191 = (1684, " With your parents  between  19:00 and  19:10")
    KID192 = (1685, " With your parents  between  19:10 and  19:20")
    KID193 = (1686, " With your parents  between  19:20 and  19:30")
    KID194 = (1687, " With your parents  between  19:30 and  19:40")
    KID195 = (1688, " With your parents  between  19:40 and  19:50")
    KID196 = (1689, " With your parents  between  19:50 and  20:00")
    KID197 = (1690, " With your parents  between  20:00 and  20:10")
    KID198 = (1691, " With your parents  between  20:10 and  20:20")
    KID199 = (1692, " With your parents  between  20:20 and  20:30")
    KID1100 = (1693, " With your parents  between  20:30 and  20:40")
    KID1101 = (1694, " With your parents  between  20:40 and  20:50")
    KID1102 = (1695, " With your parents  between  20:50 and  21:00")
    KID1103 = (1696, " With your parents  between  21:00 and  21:10")
    KID1104 = (1697, " With your parents  between  21:10 and  21:20")
    KID1105 = (1698, " With your parents  between  21:20 and  21:30")
    KID1106 = (1699, " With your parents  between  21:30 and  21:40")
    KID1107 = (1700, " With your parents  between  21:40 and  21:50")
    KID1108 = (1701, " With your parents  between  21:50 and  22:00")
    KID1109 = (1702, " With your parents  between  22:00 and  22:10")
    KID1110 = (1703, " With your parents  between  22:10 and  22:20")
    KID1111 = (1704, " With your parents  between  22:20 and  22:30")
    KID1112 = (1705, " With your parents  between  22:30 and  22:40")
    KID1113 = (1706, " With your parents  between  22:40 and  22:50")
    KID1114 = (1707, " With your parents  between  22:50 and  23:00")
    KID1115 = (1708, " With your parents  between  23:00 and  23:10")
    KID1116 = (1709, " With your parents  between  23:10 and  23:20")
    KID1117 = (1710, " With your parents  between  23:20 and  23:30")
    KID1118 = (1711, " With your parents  between  23:30 and  23:40")
    KID1119 = (1712, " With your parents  between  23:40 and  23:50")
    KID1120 = (1713, " With your parents  between  23:50 and  0:00")
    KID1121 = (1714, " With your parents  between  0:00 and  0:10")
    KID1122 = (1715, " With your parents  between  0:10 and  0:20")
    KID1123 = (1716, " With your parents  between  0:20 and  0:30")
    KID1124 = (1717, " With your parents  between  0:30 and  0:40")
    KID1125 = (1718, " With your parents  between  0:40 and  0:50")
    KID1126 = (1719, " With your parents  between  0:50 and  1:00")
    KID1127 = (1720, " With your parents  between  1:00 and  1:10")
    KID1128 = (1721, " With your parents  between  1:10 and  1:20")
    KID1129 = (1722, " With your parents  between  1:20 and  1:30")
    KID1130 = (1723, " With your parents  between  1:30 and  1:40")
    KID1131 = (1724, " With your parents  between  1:40 and  1:50")
    KID1132 = (1725, " With your parents  between  1:50 and  2:00")
    KID1133 = (1726, " With your parents  between  2:00 and  2:10")
    KID1134 = (1727, " With your parents  between  2:10 and  2:20")
    KID1135 = (1728, " With your parents  between  2:20 and  2:30")
    KID1136 = (1729, " With your parents  between  2:30 and  2:40")
    KID1137 = (1730, " With your parents  between  2:40 and  2:50")
    KID1138 = (1731, " With your parents  between  2:50 and  3:00")
    KID1139 = (1732, " With your parents  between  3:00 and  3:10")
    KID1140 = (1733, " With your parents  between  3:10 and  3:20")
    KID1141 = (1734, " With your parents  between  3:20 and  3:30")
    KID1142 = (1735, " With your parents  between  3:30 and  3:40")
    KID1143 = (1736, " With your parents  between  3:40 and  3:50")
    KID1144 = (1737, " With your parents  between  3:50 and  4:00")
    KID21 = (1738, " With other people in your household  between  4:00 and  4:10")
    KID22 = (1739, " With other people in your household  between  4:10 and  4:20")
    KID23 = (1740, " With other people in your household  between  4:20 and  4:30")
    KID24 = (1741, " With other people in your household  between  4:30 and  4:40")
    KID25 = (1742, " With other people in your household  between  4:40 and  4:50")
    KID26 = (1743, " With other people in your household  between  4:50 and  5:00")
    KID27 = (1744, " With other people in your household  between  5:00 and  5:10")
    KID28 = (1745, " With other people in your household  between  5:10 and  5:20")
    KID29 = (1746, " With other people in your household  between  5:20 and  5:30")
    KID210 = (1747, " With other people in your household  between  5:30 and  5:40")
    KID211 = (1748, " With other people in your household  between  5:40 and  5:50")
    KID212 = (1749, " With other people in your household  between  5:50 and  6:00")
    KID213 = (1750, " With other people in your household  between  6:00 and  6:10")
    KID214 = (1751, " With other people in your household  between  6:10 and  6:20")
    KID215 = (1752, " With other people in your household  between  6:20 and  6:30")
    KID216 = (1753, " With other people in your household  between  6:30 and  6:40")
    KID217 = (1754, " With other people in your household  between  6:40 and  6:50")
    KID218 = (1755, " With other people in your household  between  6:50 and  7:00")
    KID219 = (1756, " With other people in your household  between  7:00 and  7:10")
    KID220 = (1757, " With other people in your household  between  7:10 and  7:20")
    KID221 = (1758, " With other people in your household  between  7:20 and  7:30")
    KID222 = (1759, " With other people in your household  between  7:30 and  7:40")
    KID223 = (1760, " With other people in your household  between  7:40 and  7:50")
    KID224 = (1761, " With other people in your household  between  7:50 and  8:00")
    KID225 = (1762, " With other people in your household  between  8:00 and  8:10")
    KID226 = (1763, " With other people in your household  between  8:10 and  8:20")
    KID227 = (1764, " With other people in your household  between  8:20 and  8:30")
    KID228 = (1765, " With other people in your household  between  8:30 and  8:40")
    KID229 = (1766, " With other people in your household  between  8:40 and  8:50")
    KID230 = (1767, " With other people in your household  between  8:50 and  9:00")
    KID231 = (1768, " With other people in your household  between  9:00 and  9:10")
    KID232 = (1769, " With other people in your household  between  9:10 and  9:20")
    KID233 = (1770, " With other people in your household  between  9:20 and  9:30")
    KID234 = (1771, " With other people in your household  between  9:30 and  9:40")
    KID235 = (1772, " With other people in your household  between  9:40 and  9:50")
    KID236 = (1773, " With other people in your household  between  9:50 and  10:00")
    KID237 = (1774, " With other people in your household  between  10:00 and  10:10")
    KID238 = (1775, " With other people in your household  between  10:10 and  10:20")
    KID239 = (1776, " With other people in your household  between  10:20 and  10:30")
    KID240 = (1777, " With other people in your household  between  10:30 and  10:40")
    KID241 = (1778, " With other people in your household  between  10:40 and  10:50")
    KID242 = (1779, " With other people in your household  between  10:50 and  11:00")
    KID243 = (1780, " With other people in your household  between  11:00 and  11:10")
    KID244 = (1781, " With other people in your household  between  11:10 and  11:20")
    KID245 = (1782, " With other people in your household  between  11:20 and  11:30")
    KID246 = (1783, " With other people in your household  between  11:30 and  11:40")
    KID247 = (1784, " With other people in your household  between  11:40 and  11:50")
    KID248 = (1785, " With other people in your household  between  11:50 and  12:00")
    KID249 = (1786, " With other people in your household  between  12:00 and  12:10")
    KID250 = (1787, " With other people in your household  between  12:10 and  12:20")
    KID251 = (1788, " With other people in your household  between  12:20 and  12:30")
    KID252 = (1789, " With other people in your household  between  12:30 and  12:40")
    KID253 = (1790, " With other people in your household  between  12:40 and  12:50")
    KID254 = (1791, " With other people in your household  between  12:50 and  13:00")
    KID255 = (1792, " With other people in your household  between  13:00 and  13:10")
    KID256 = (1793, " With other people in your household  between  13:10 and  13:20")
    KID257 = (1794, " With other people in your household  between  13:20 and  13:30")
    KID258 = (1795, " With other people in your household  between  13:30 and  13:40")
    KID259 = (1796, " With other people in your household  between  13:40 and  13:50")
    KID260 = (1797, " With other people in your household  between  13:50 and  14:00")
    KID261 = (1798, " With other people in your household  between  14:00 and  14:10")
    KID262 = (1799, " With other people in your household  between  14:10 and  14:20")
    KID263 = (1800, " With other people in your household  between  14:20 and  14:30")
    KID264 = (1801, " With other people in your household  between  14:30 and  14:40")
    KID265 = (1802, " With other people in your household  between  14:40 and  14:50")
    KID266 = (1803, " With other people in your household  between  14:50 and  15:00")
    KID267 = (1804, " With other people in your household  between  15:00 and  15:10")
    KID268 = (1805, " With other people in your household  between  15:10 and  15:20")
    KID269 = (1806, " With other people in your household  between  15:20 and  15:30")
    KID270 = (1807, " With other people in your household  between  15:30 and  15:40")
    KID271 = (1808, " With other people in your household  between  15:40 and  15:50")
    KID272 = (1809, " With other people in your household  between  15:50 and  16:00")
    KID273 = (1810, " With other people in your household  between  16:00 and  16:10")
    KID274 = (1811, " With other people in your household  between  16:10 and  16:20")
    KID275 = (1812, " With other people in your household  between  16:20 and  16:30")
    KID276 = (1813, " With other people in your household  between  16:30 and  16:40")
    KID277 = (1814, " With other people in your household  between  16:40 and  16:50")
    KID278 = (1815, " With other people in your household  between  16:50 and  17:00")
    KID279 = (1816, " With other people in your household  between  17:00 and  17:10")
    KID280 = (1817, " With other people in your household  between  17:10 and  17:20")
    KID281 = (1818, " With other people in your household  between  17:20 and  17:30")
    KID282 = (1819, " With other people in your household  between  17:30 and  17:40")
    KID283 = (1820, " With other people in your household  between  17:40 and  17:50")
    KID284 = (1821, " With other people in your household  between  17:50 and  18:00")
    KID285 = (1822, " With other people in your household  between  18:00 and  18:10")
    KID286 = (1823, " With other people in your household  between  18:10 and  18:20")
    KID287 = (1824, " With other people in your household  between  18:20 and  18:30")
    KID288 = (1825, " With other people in your household  between  18:30 and  18:40")
    KID289 = (1826, " With other people in your household  between  18:40 and  18:50")
    KID290 = (1827, " With other people in your household  between  18:50 and  19:00")
    KID291 = (1828, " With other people in your household  between  19:00 and  19:10")
    KID292 = (1829, " With other people in your household  between  19:10 and  19:20")
    KID293 = (1830, " With other people in your household  between  19:20 and  19:30")
    KID294 = (1831, " With other people in your household  between  19:30 and  19:40")
    KID295 = (1832, " With other people in your household  between  19:40 and  19:50")
    KID296 = (1833, " With other people in your household  between  19:50 and  20:00")
    KID297 = (1834, " With other people in your household  between  20:00 and  20:10")
    KID298 = (1835, " With other people in your household  between  20:10 and  20:20")
    KID299 = (1836, " With other people in your household  between  20:20 and  20:30")
    KID2100 = (1837, " With other people in your household  between  20:30 and  20:40")
    KID2101 = (1838, " With other people in your household  between  20:40 and  20:50")
    KID2102 = (1839, " With other people in your household  between  20:50 and  21:00")
    KID2103 = (1840, " With other people in your household  between  21:00 and  21:10")
    KID2104 = (1841, " With other people in your household  between  21:10 and  21:20")
    KID2105 = (1842, " With other people in your household  between  21:20 and  21:30")
    KID2106 = (1843, " With other people in your household  between  21:30 and  21:40")
    KID2107 = (1844, " With other people in your household  between  21:40 and  21:50")
    KID2108 = (1845, " With other people in your household  between  21:50 and  22:00")
    KID2109 = (1846, " With other people in your household  between  22:00 and  22:10")
    KID2110 = (1847, " With other people in your household  between  22:10 and  22:20")
    KID2111 = (1848, " With other people in your household  between  22:20 and  22:30")
    KID2112 = (1849, " With other people in your household  between  22:30 and  22:40")
    KID2113 = (1850, " With other people in your household  between  22:40 and  22:50")
    KID2114 = (1851, " With other people in your household  between  22:50 and  23:00")
    KID2115 = (1852, " With other people in your household  between  23:00 and  23:10")
    KID2116 = (1853, " With other people in your household  between  23:10 and  23:20")
    KID2117 = (1854, " With other people in your household  between  23:20 and  23:30")
    KID2118 = (1855, " With other people in your household  between  23:30 and  23:40")
    KID2119 = (1856, " With other people in your household  between  23:40 and  23:50")
    KID2120 = (1857, " With other people in your household  between  23:50 and  0:00")
    KID2121 = (1858, " With other people in your household  between  0:00 and  0:10")
    KID2122 = (1859, " With other people in your household  between  0:10 and  0:20")
    KID2123 = (1860, " With other people in your household  between  0:20 and  0:30")
    KID2124 = (1861, " With other people in your household  between  0:30 and  0:40")
    KID2125 = (1862, " With other people in your household  between  0:40 and  0:50")
    KID2126 = (1863, " With other people in your household  between  0:50 and  1:00")
    KID2127 = (1864, " With other people in your household  between  1:00 and  1:10")
    KID2128 = (1865, " With other people in your household  between  1:10 and  1:20")
    KID2129 = (1866, " With other people in your household  between  1:20 and  1:30")
    KID2130 = (1867, " With other people in your household  between  1:30 and  1:40")
    KID2131 = (1868, " With other people in your household  between  1:40 and  1:50")
    KID2132 = (1869, " With other people in your household  between  1:50 and  2:00")
    KID2133 = (1870, " With other people in your household  between  2:00 and  2:10")
    KID2134 = (1871, " With other people in your household  between  2:10 and  2:20")
    KID2135 = (1872, " With other people in your household  between  2:20 and  2:30")
    KID2136 = (1873, " With other people in your household  between  2:30 and  2:40")
    KID2137 = (1874, " With other people in your household  between  2:40 and  2:50")
    KID2138 = (1875, " With other people in your household  between  2:50 and  3:00")
    KID2139 = (1876, " With other people in your household  between  3:00 and  3:10")
    KID2140 = (1877, " With other people in your household  between  3:10 and  3:20")
    KID2141 = (1878, " With other people in your household  between  3:20 and  3:30")
    KID2142 = (1879, " With other people in your household  between  3:30 and  3:40")
    KID2143 = (1880, " With other people in your household  between  3:40 and  3:50")
    KID2144 = (1881, " With other people in your household  between  3:50 and  4:00")
    KID31 = (1882, " With other people that you know  between  4:00 and  4:10")
    KID32 = (1883, " With other people that you know  between  4:10 and  4:20")
    KID33 = (1884, " With other people that you know  between  4:20 and  4:30")
    KID34 = (1885, " With other people that you know  between  4:30 and  4:40")
    KID35 = (1886, " With other people that you know  between  4:40 and  4:50")
    KID36 = (1887, " With other people that you know  between  4:50 and  5:00")
    KID37 = (1888, " With other people that you know  between  5:00 and  5:10")
    KID38 = (1889, " With other people that you know  between  5:10 and  5:20")
    KID39 = (1890, " With other people that you know  between  5:20 and  5:30")
    KID310 = (1891, " With other people that you know  between  5:30 and  5:40")
    KID311 = (1892, " With other people that you know  between  5:40 and  5:50")
    KID312 = (1893, " With other people that you know  between  5:50 and  6:00")
    KID313 = (1894, " With other people that you know  between  6:00 and  6:10")
    KID314 = (1895, " With other people that you know  between  6:10 and  6:20")
    KID315 = (1896, " With other people that you know  between  6:20 and  6:30")
    KID316 = (1897, " With other people that you know  between  6:30 and  6:40")
    KID317 = (1898, " With other people that you know  between  6:40 and  6:50")
    KID318 = (1899, " With other people that you know  between  6:50 and  7:00")
    KID319 = (1900, " With other people that you know  between  7:00 and  7:10")
    KID320 = (1901, " With other people that you know  between  7:10 and  7:20")
    KID321 = (1902, " With other people that you know  between  7:20 and  7:30")
    KID322 = (1903, " With other people that you know  between  7:30 and  7:40")
    KID323 = (1904, " With other people that you know  between  7:40 and  7:50")
    KID324 = (1905, " With other people that you know  between  7:50 and  8:00")
    KID325 = (1906, " With other people that you know  between  8:00 and  8:10")
    KID326 = (1907, " With other people that you know  between  8:10 and  8:20")
    KID327 = (1908, " With other people that you know  between  8:20 and  8:30")
    KID328 = (1909, " With other people that you know  between  8:30 and  8:40")
    KID329 = (1910, " With other people that you know  between  8:40 and  8:50")
    KID330 = (1911, " With other people that you know  between  8:50 and  9:00")
    KID331 = (1912, " With other people that you know  between  9:00 and  9:10")
    KID332 = (1913, " With other people that you know  between  9:10 and  9:20")
    KID333 = (1914, " With other people that you know  between  9:20 and  9:30")
    KID334 = (1915, " With other people that you know  between  9:30 and  9:40")
    KID335 = (1916, " With other people that you know  between  9:40 and  9:50")
    KID336 = (1917, " With other people that you know  between  9:50 and  10:00")
    KID337 = (1918, " With other people that you know  between  10:00 and  10:10")
    KID338 = (1919, " With other people that you know  between  10:10 and  10:20")
    KID339 = (1920, " With other people that you know  between  10:20 and  10:30")
    KID340 = (1921, " With other people that you know  between  10:30 and  10:40")
    KID341 = (1922, " With other people that you know  between  10:40 and  10:50")
    KID342 = (1923, " With other people that you know  between  10:50 and  11:00")
    KID343 = (1924, " With other people that you know  between  11:00 and  11:10")
    KID344 = (1925, " With other people that you know  between  11:10 and  11:20")
    KID345 = (1926, " With other people that you know  between  11:20 and  11:30")
    KID346 = (1927, " With other people that you know  between  11:30 and  11:40")
    KID347 = (1928, " With other people that you know  between  11:40 and  11:50")
    KID348 = (1929, " With other people that you know  between  11:50 and  12:00")
    KID349 = (1930, " With other people that you know  between  12:00 and  12:10")
    KID350 = (1931, " With other people that you know  between  12:10 and  12:20")
    KID351 = (1932, " With other people that you know  between  12:20 and  12:30")
    KID352 = (1933, " With other people that you know  between  12:30 and  12:40")
    KID353 = (1934, " With other people that you know  between  12:40 and  12:50")
    KID354 = (1935, " With other people that you know  between  12:50 and  13:00")
    KID355 = (1936, " With other people that you know  between  13:00 and  13:10")
    KID356 = (1937, " With other people that you know  between  13:10 and  13:20")
    KID357 = (1938, " With other people that you know  between  13:20 and  13:30")
    KID358 = (1939, " With other people that you know  between  13:30 and  13:40")
    KID359 = (1940, " With other people that you know  between  13:40 and  13:50")
    KID360 = (1941, " With other people that you know  between  13:50 and  14:00")
    KID361 = (1942, " With other people that you know  between  14:00 and  14:10")
    KID362 = (1943, " With other people that you know  between  14:10 and  14:20")
    KID363 = (1944, " With other people that you know  between  14:20 and  14:30")
    KID364 = (1945, " With other people that you know  between  14:30 and  14:40")
    KID365 = (1946, " With other people that you know  between  14:40 and  14:50")
    KID366 = (1947, " With other people that you know  between  14:50 and  15:00")
    KID367 = (1948, " With other people that you know  between  15:00 and  15:10")
    KID368 = (1949, " With other people that you know  between  15:10 and  15:20")
    KID369 = (1950, " With other people that you know  between  15:20 and  15:30")
    KID370 = (1951, " With other people that you know  between  15:30 and  15:40")
    KID371 = (1952, " With other people that you know  between  15:40 and  15:50")
    KID372 = (1953, " With other people that you know  between  15:50 and  16:00")
    KID373 = (1954, " With other people that you know  between  16:00 and  16:10")
    KID374 = (1955, " With other people that you know  between  16:10 and  16:20")
    KID375 = (1956, " With other people that you know  between  16:20 and  16:30")
    KID376 = (1957, " With other people that you know  between  16:30 and  16:40")
    KID377 = (1958, " With other people that you know  between  16:40 and  16:50")
    KID378 = (1959, " With other people that you know  between  16:50 and  17:00")
    KID379 = (1960, " With other people that you know  between  17:00 and  17:10")
    KID380 = (1961, " With other people that you know  between  17:10 and  17:20")
    KID381 = (1962, " With other people that you know  between  17:20 and  17:30")
    KID382 = (1963, " With other people that you know  between  17:30 and  17:40")
    KID383 = (1964, " With other people that you know  between  17:40 and  17:50")
    KID384 = (1965, " With other people that you know  between  17:50 and  18:00")
    KID385 = (1966, " With other people that you know  between  18:00 and  18:10")
    KID386 = (1967, " With other people that you know  between  18:10 and  18:20")
    KID387 = (1968, " With other people that you know  between  18:20 and  18:30")
    KID388 = (1969, " With other people that you know  between  18:30 and  18:40")
    KID389 = (1970, " With other people that you know  between  18:40 and  18:50")
    KID390 = (1971, " With other people that you know  between  18:50 and  19:00")
    KID391 = (1972, " With other people that you know  between  19:00 and  19:10")
    KID392 = (1973, " With other people that you know  between  19:10 and  19:20")
    KID393 = (1974, " With other people that you know  between  19:20 and  19:30")
    KID394 = (1975, " With other people that you know  between  19:30 and  19:40")
    KID395 = (1976, " With other people that you know  between  19:40 and  19:50")
    KID396 = (1977, " With other people that you know  between  19:50 and  20:00")
    KID397 = (1978, " With other people that you know  between  20:00 and  20:10")
    KID398 = (1979, " With other people that you know  between  20:10 and  20:20")
    KID399 = (1980, " With other people that you know  between  20:20 and  20:30")
    KID3100 = (1981, " With other people that you know  between  20:30 and  20:40")
    KID3101 = (1982, " With other people that you know  between  20:40 and  20:50")
    KID3102 = (1983, " With other people that you know  between  20:50 and  21:00")
    KID3103 = (1984, " With other people that you know  between  21:00 and  21:10")
    KID3104 = (1985, " With other people that you know  between  21:10 and  21:20")
    KID3105 = (1986, " With other people that you know  between  21:20 and  21:30")
    KID3106 = (1987, " With other people that you know  between  21:30 and  21:40")
    KID3107 = (1988, " With other people that you know  between  21:40 and  21:50")
    KID3108 = (1989, " With other people that you know  between  21:50 and  22:00")
    KID3109 = (1990, " With other people that you know  between  22:00 and  22:10")
    KID3110 = (1991, " With other people that you know  between  22:10 and  22:20")
    KID3111 = (1992, " With other people that you know  between  22:20 and  22:30")
    KID3112 = (1993, " With other people that you know  between  22:30 and  22:40")
    KID3113 = (1994, " With other people that you know  between  22:40 and  22:50")
    KID3114 = (1995, " With other people that you know  between  22:50 and  23:00")
    KID3115 = (1996, " With other people that you know  between  23:00 and  23:10")
    KID3116 = (1997, " With other people that you know  between  23:10 and  23:20")
    KID3117 = (1998, " With other people that you know  between  23:20 and  23:30")
    KID3118 = (1999, " With other people that you know  between  23:30 and  23:40")
    KID3119 = (2000, " With other people that you know  between  23:40 and  23:50")
    KID3120 = (2001, " With other people that you know  between  23:50 and  0:00")
    KID3121 = (2002, " With other people that you know  between  0:00 and  0:10")
    KID3122 = (2003, " With other people that you know  between  0:10 and  0:20")
    KID3123 = (2004, " With other people that you know  between  0:20 and  0:30")
    KID3124 = (2005, " With other people that you know  between  0:30 and  0:40")
    KID3125 = (2006, " With other people that you know  between  0:40 and  0:50")
    KID3126 = (2007, " With other people that you know  between  0:50 and  1:00")
    KID3127 = (2008, " With other people that you know  between  1:00 and  1:10")
    KID3128 = (2009, " With other people that you know  between  1:10 and  1:20")
    KID3129 = (2010, " With other people that you know  between  1:20 and  1:30")
    KID3130 = (2011, " With other people that you know  between  1:30 and  1:40")
    KID3131 = (2012, " With other people that you know  between  1:40 and  1:50")
    KID3132 = (2013, " With other people that you know  between  1:50 and  2:00")
    KID3133 = (2014, " With other people that you know  between  2:00 and  2:10")
    KID3134 = (2015, " With other people that you know  between  2:10 and  2:20")
    KID3135 = (2016, " With other people that you know  between  2:20 and  2:30")
    KID3136 = (2017, " With other people that you know  between  2:30 and  2:40")
    KID3137 = (2018, " With other people that you know  between  2:40 and  2:50")
    KID3138 = (2019, " With other people that you know  between  2:50 and  3:00")
    KID3139 = (2020, " With other people that you know  between  3:00 and  3:10")
    KID3140 = (2021, " With other people that you know  between  3:10 and  3:20")
    KID3141 = (2022, " With other people that you know  between  3:20 and  3:30")
    KID3142 = (2023, " With other people that you know  between  3:30 and  3:40")
    KID3143 = (2024, " With other people that you know  between  3:40 and  3:50")
    KID3144 = (2025, " With other people that you know  between  3:50 and  4:00")
    KID41 = (2026, " Main Activity:Asleep/ Employment/ Study between  4:00 and  4:10")
    KID42 = (2027, " Main Activity:Asleep/ Employment/ Study between  4:10 and  4:20")
    KID43 = (2028, " Main Activity:Asleep/ Employment/ Study between  4:20 and  4:30")
    KID44 = (2029, " Main Activity:Asleep/ Employment/ Study between  4:30 and  4:40")
    KID45 = (2030, " Main Activity:Asleep/ Employment/ Study between  4:40 and  4:50")
    KID46 = (2031, " Main Activity:Asleep/ Employment/ Study between  4:50 and  5:00")
    KID47 = (2032, " Main Activity:Asleep/ Employment/ Study between  5:00 and  5:10")
    KID48 = (2033, " Main Activity:Asleep/ Employment/ Study between  5:10 and  5:20")
    KID49 = (2034, " Main Activity:Asleep/ Employment/ Study between  5:20 and  5:30")
    KID410 = (2035, " Main Activity:Asleep/ Employment/ Study between  5:30 and  5:40")
    KID411 = (2036, " Main Activity:Asleep/ Employment/ Study between  5:40 and  5:50")
    KID412 = (2037, " Main Activity:Asleep/ Employment/ Study between  5:50 and  6:00")
    KID413 = (2038, " Main Activity:Asleep/ Employment/ Study between  6:00 and  6:10")
    KID414 = (2039, " Main Activity:Asleep/ Employment/ Study between  6:10 and  6:20")
    KID415 = (2040, " Main Activity:Asleep/ Employment/ Study between  6:20 and  6:30")
    KID416 = (2041, " Main Activity:Asleep/ Employment/ Study between  6:30 and  6:40")
    KID417 = (2042, " Main Activity:Asleep/ Employment/ Study between  6:40 and  6:50")
    KID418 = (2043, " Main Activity:Asleep/ Employment/ Study between  6:50 and  7:00")
    KID419 = (2044, " Main Activity:Asleep/ Employment/ Study between  7:00 and  7:10")
    KID420 = (2045, " Main Activity:Asleep/ Employment/ Study between  7:10 and  7:20")
    KID421 = (2046, " Main Activity:Asleep/ Employment/ Study between  7:20 and  7:30")
    KID422 = (2047, " Main Activity:Asleep/ Employment/ Study between  7:30 and  7:40")
    KID423 = (2048, " Main Activity:Asleep/ Employment/ Study between  7:40 and  7:50")
    KID424 = (2049, " Main Activity:Asleep/ Employment/ Study between  7:50 and  8:00")
    KID425 = (2050, " Main Activity:Asleep/ Employment/ Study between  8:00 and  8:10")
    KID426 = (2051, " Main Activity:Asleep/ Employment/ Study between  8:10 and  8:20")
    KID427 = (2052, " Main Activity:Asleep/ Employment/ Study between  8:20 and  8:30")
    KID428 = (2053, " Main Activity:Asleep/ Employment/ Study between  8:30 and  8:40")
    KID429 = (2054, " Main Activity:Asleep/ Employment/ Study between  8:40 and  8:50")
    KID430 = (2055, " Main Activity:Asleep/ Employment/ Study between  8:50 and  9:00")
    KID431 = (2056, " Main Activity:Asleep/ Employment/ Study between  9:00 and  9:10")
    KID432 = (2057, " Main Activity:Asleep/ Employment/ Study between  9:10 and  9:20")
    KID433 = (2058, " Main Activity:Asleep/ Employment/ Study between  9:20 and  9:30")
    KID434 = (2059, " Main Activity:Asleep/ Employment/ Study between  9:30 and  9:40")
    KID435 = (2060, " Main Activity:Asleep/ Employment/ Study between  9:40 and  9:50")
    KID436 = (2061, " Main Activity:Asleep/ Employment/ Study between  9:50 and  10:00")
    KID437 = (2062, " Main Activity:Asleep/ Employment/ Study between  10:00 and  10:10")
    KID438 = (2063, " Main Activity:Asleep/ Employment/ Study between  10:10 and  10:20")
    KID439 = (2064, " Main Activity:Asleep/ Employment/ Study between  10:20 and  10:30")
    KID440 = (2065, " Main Activity:Asleep/ Employment/ Study between  10:30 and  10:40")
    KID441 = (2066, " Main Activity:Asleep/ Employment/ Study between  10:40 and  10:50")
    KID442 = (2067, " Main Activity:Asleep/ Employment/ Study between  10:50 and  11:00")
    KID443 = (2068, " Main Activity:Asleep/ Employment/ Study between  11:00 and  11:10")
    KID444 = (2069, " Main Activity:Asleep/ Employment/ Study between  11:10 and  11:20")
    KID445 = (2070, " Main Activity:Asleep/ Employment/ Study between  11:20 and  11:30")
    KID446 = (2071, " Main Activity:Asleep/ Employment/ Study between  11:30 and  11:40")
    KID447 = (2072, " Main Activity:Asleep/ Employment/ Study between  11:40 and  11:50")
    KID448 = (2073, " Main Activity:Asleep/ Employment/ Study between  11:50 and  12:00")
    KID449 = (2074, " Main Activity:Asleep/ Employment/ Study between  12:00 and  12:10")
    KID450 = (2075, " Main Activity:Asleep/ Employment/ Study between  12:10 and  12:20")
    KID451 = (2076, " Main Activity:Asleep/ Employment/ Study between  12:20 and  12:30")
    KID452 = (2077, " Main Activity:Asleep/ Employment/ Study between  12:30 and  12:40")
    KID453 = (2078, " Main Activity:Asleep/ Employment/ Study between  12:40 and  12:50")
    KID454 = (2079, " Main Activity:Asleep/ Employment/ Study between  12:50 and  13:00")
    KID455 = (2080, " Main Activity:Asleep/ Employment/ Study between  13:00 and  13:10")
    KID456 = (2081, " Main Activity:Asleep/ Employment/ Study between  13:10 and  13:20")
    KID457 = (2082, " Main Activity:Asleep/ Employment/ Study between  13:20 and  13:30")
    KID458 = (2083, " Main Activity:Asleep/ Employment/ Study between  13:30 and  13:40")
    KID459 = (2084, " Main Activity:Asleep/ Employment/ Study between  13:40 and  13:50")
    KID460 = (2085, " Main Activity:Asleep/ Employment/ Study between  13:50 and  14:00")
    KID461 = (2086, " Main Activity:Asleep/ Employment/ Study between  14:00 and  14:10")
    KID462 = (2087, " Main Activity:Asleep/ Employment/ Study between  14:10 and  14:20")
    KID463 = (2088, " Main Activity:Asleep/ Employment/ Study between  14:20 and  14:30")
    KID464 = (2089, " Main Activity:Asleep/ Employment/ Study between  14:30 and  14:40")
    KID465 = (2090, " Main Activity:Asleep/ Employment/ Study between  14:40 and  14:50")
    KID466 = (2091, " Main Activity:Asleep/ Employment/ Study between  14:50 and  15:00")
    KID467 = (2092, " Main Activity:Asleep/ Employment/ Study between  15:00 and  15:10")
    KID468 = (2093, " Main Activity:Asleep/ Employment/ Study between  15:10 and  15:20")
    KID469 = (2094, " Main Activity:Asleep/ Employment/ Study between  15:20 and  15:30")
    KID470 = (2095, " Main Activity:Asleep/ Employment/ Study between  15:30 and  15:40")
    KID471 = (2096, " Main Activity:Asleep/ Employment/ Study between  15:40 and  15:50")
    KID472 = (2097, " Main Activity:Asleep/ Employment/ Study between  15:50 and  16:00")
    KID473 = (2098, " Main Activity:Asleep/ Employment/ Study between  16:00 and  16:10")
    KID474 = (2099, " Main Activity:Asleep/ Employment/ Study between  16:10 and  16:20")
    KID475 = (2100, " Main Activity:Asleep/ Employment/ Study between  16:20 and  16:30")
    KID476 = (2101, " Main Activity:Asleep/ Employment/ Study between  16:30 and  16:40")
    KID477 = (2102, " Main Activity:Asleep/ Employment/ Study between  16:40 and  16:50")
    KID478 = (2103, " Main Activity:Asleep/ Employment/ Study between  16:50 and  17:00")
    KID479 = (2104, " Main Activity:Asleep/ Employment/ Study between  17:00 and  17:10")
    KID480 = (2105, " Main Activity:Asleep/ Employment/ Study between  17:10 and  17:20")
    KID481 = (2106, " Main Activity:Asleep/ Employment/ Study between  17:20 and  17:30")
    KID482 = (2107, " Main Activity:Asleep/ Employment/ Study between  17:30 and  17:40")
    KID483 = (2108, " Main Activity:Asleep/ Employment/ Study between  17:40 and  17:50")
    KID484 = (2109, " Main Activity:Asleep/ Employment/ Study between  17:50 and  18:00")
    KID485 = (2110, " Main Activity:Asleep/ Employment/ Study between  18:00 and  18:10")
    KID486 = (2111, " Main Activity:Asleep/ Employment/ Study between  18:10 and  18:20")
    KID487 = (2112, " Main Activity:Asleep/ Employment/ Study between  18:20 and  18:30")
    KID488 = (2113, " Main Activity:Asleep/ Employment/ Study between  18:30 and  18:40")
    KID489 = (2114, " Main Activity:Asleep/ Employment/ Study between  18:40 and  18:50")
    KID490 = (2115, " Main Activity:Asleep/ Employment/ Study between  18:50 and  19:00")
    KID491 = (2116, " Main Activity:Asleep/ Employment/ Study between  19:00 and  19:10")
    KID492 = (2117, " Main Activity:Asleep/ Employment/ Study between  19:10 and  19:20")
    KID493 = (2118, " Main Activity:Asleep/ Employment/ Study between  19:20 and  19:30")
    KID494 = (2119, " Main Activity:Asleep/ Employment/ Study between  19:30 and  19:40")
    KID495 = (2120, " Main Activity:Asleep/ Employment/ Study between  19:40 and  19:50")
    KID496 = (2121, " Main Activity:Asleep/ Employment/ Study between  19:50 and  20:00")
    KID497 = (2122, " Main Activity:Asleep/ Employment/ Study between  20:00 and  20:10")
    KID498 = (2123, " Main Activity:Asleep/ Employment/ Study between  20:10 and  20:20")
    KID499 = (2124, " Main Activity:Asleep/ Employment/ Study between  20:20 and  20:30")
    KID4100 = (2125, " Main Activity:Asleep/ Employment/ Study between  20:30 and  20:40")
    KID4101 = (2126, " Main Activity:Asleep/ Employment/ Study between  20:40 and  20:50")
    KID4102 = (2127, " Main Activity:Asleep/ Employment/ Study between  20:50 and  21:00")
    KID4103 = (2128, " Main Activity:Asleep/ Employment/ Study between  21:00 and  21:10")
    KID4104 = (2129, " Main Activity:Asleep/ Employment/ Study between  21:10 and  21:20")
    KID4105 = (2130, " Main Activity:Asleep/ Employment/ Study between  21:20 and  21:30")
    KID4106 = (2131, " Main Activity:Asleep/ Employment/ Study between  21:30 and  21:40")
    KID4107 = (2132, " Main Activity:Asleep/ Employment/ Study between  21:40 and  21:50")
    KID4108 = (2133, " Main Activity:Asleep/ Employment/ Study between  21:50 and  22:00")
    KID4109 = (2134, " Main Activity:Asleep/ Employment/ Study between  22:00 and  22:10")
    KID4110 = (2135, " Main Activity:Asleep/ Employment/ Study between  22:10 and  22:20")
    KID4111 = (2136, " Main Activity:Asleep/ Employment/ Study between  22:20 and  22:30")
    KID4112 = (2137, " Main Activity:Asleep/ Employment/ Study between  22:30 and  22:40")
    KID4113 = (2138, " Main Activity:Asleep/ Employment/ Study between  22:40 and  22:50")
    KID4114 = (2139, " Main Activity:Asleep/ Employment/ Study between  22:50 and  23:00")
    KID4115 = (2140, " Main Activity:Asleep/ Employment/ Study between  23:00 and  23:10")
    KID4116 = (2141, " Main Activity:Asleep/ Employment/ Study between  23:10 and  23:20")
    KID4117 = (2142, " Main Activity:Asleep/ Employment/ Study between  23:20 and  23:30")
    KID4118 = (2143, " Main Activity:Asleep/ Employment/ Study between  23:30 and  23:40")
    KID4119 = (2144, " Main Activity:Asleep/ Employment/ Study between  23:40 and  23:50")
    KID4120 = (2145, " Main Activity:Asleep/ Employment/ Study between  23:50 and  0:00")
    KID4121 = (2146, " Main Activity:Asleep/ Employment/ Study between  0:00 and  0:10")
    KID4122 = (2147, " Main Activity:Asleep/ Employment/ Study between  0:10 and  0:20")
    KID4123 = (2148, " Main Activity:Asleep/ Employment/ Study between  0:20 and  0:30")
    KID4124 = (2149, " Main Activity:Asleep/ Employment/ Study between  0:30 and  0:40")
    KID4125 = (2150, " Main Activity:Asleep/ Employment/ Study between  0:40 and  0:50")
    KID4126 = (2151, " Main Activity:Asleep/ Employment/ Study between  0:50 and  1:00")
    KID4127 = (2152, " Main Activity:Asleep/ Employment/ Study between  1:00 and  1:10")
    KID4128 = (2153, " Main Activity:Asleep/ Employment/ Study between  1:10 and  1:20")
    KID4129 = (2154, " Main Activity:Asleep/ Employment/ Study between  1:20 and  1:30")
    KID4130 = (2155, " Main Activity:Asleep/ Employment/ Study between  1:30 and  1:40")
    KID4131 = (2156, " Main Activity:Asleep/ Employment/ Study between  1:40 and  1:50")
    KID4132 = (2157, " Main Activity:Asleep/ Employment/ Study between  1:50 and  2:00")
    KID4133 = (2158, " Main Activity:Asleep/ Employment/ Study between  2:00 and  2:10")
    KID4134 = (2159, " Main Activity:Asleep/ Employment/ Study between  2:10 and  2:20")
    KID4135 = (2160, " Main Activity:Asleep/ Employment/ Study between  2:20 and  2:30")
    KID4136 = (2161, " Main Activity:Asleep/ Employment/ Study between  2:30 and  2:40")
    KID4137 = (2162, " Main Activity:Asleep/ Employment/ Study between  2:40 and  2:50")
    KID4138 = (2163, " Main Activity:Asleep/ Employment/ Study between  2:50 and  3:00")
    KID4139 = (2164, " Main Activity:Asleep/ Employment/ Study between  3:00 and  3:10")
    KID4140 = (2165, " Main Activity:Asleep/ Employment/ Study between  3:10 and  3:20")
    KID4141 = (2166, " Main Activity:Asleep/ Employment/ Study between  3:20 and  3:30")
    KID4142 = (2167, " Main Activity:Asleep/ Employment/ Study between  3:30 and  3:40")
    KID4143 = (2168, " Main Activity:Asleep/ Employment/ Study between  3:40 and  3:50")
    KID4144 = (2169, " Main Activity:Asleep/ Employment/ Study between  3:50 and  4:00")
    KID51 = (2170, " No Answer  between  4:00 and  4:10")
    KID52 = (2171, " No Answer  between  4:10 and  4:20")
    KID53 = (2172, " No Answer  between  4:20 and  4:30")
    KID54 = (2173, " No Answer  between  4:30 and  4:40")
    KID55 = (2174, " No Answer  between  4:40 and  4:50")
    KID56 = (2175, " No Answer  between  4:50 and  5:00")
    KID57 = (2176, " No Answer  between  5:00 and  5:10")
    KID58 = (2177, " No Answer  between  5:10 and  5:20")
    KID59 = (2178, " No Answer  between  5:20 and  5:30")
    KID510 = (2179, " No Answer  between  5:30 and  5:40")
    KID511 = (2180, " No Answer  between  5:40 and  5:50")
    KID512 = (2181, " No Answer  between  5:50 and  6:00")
    KID513 = (2182, " No Answer  between  6:00 and  6:10")
    KID514 = (2183, " No Answer  between  6:10 and  6:20")
    KID515 = (2184, " No Answer  between  6:20 and  6:30")
    KID516 = (2185, " No Answer  between  6:30 and  6:40")
    KID517 = (2186, " No Answer  between  6:40 and  6:50")
    KID518 = (2187, " No Answer  between  6:50 and  7:00")
    KID519 = (2188, " No Answer  between  7:00 and  7:10")
    KID520 = (2189, " No Answer  between  7:10 and  7:20")
    KID521 = (2190, " No Answer  between  7:20 and  7:30")
    KID522 = (2191, " No Answer  between  7:30 and  7:40")
    KID523 = (2192, " No Answer  between  7:40 and  7:50")
    KID524 = (2193, " No Answer  between  7:50 and  8:00")
    KID525 = (2194, " No Answer  between  8:00 and  8:10")
    KID526 = (2195, " No Answer  between  8:10 and  8:20")
    KID527 = (2196, " No Answer  between  8:20 and  8:30")
    KID528 = (2197, " No Answer  between  8:30 and  8:40")
    KID529 = (2198, " No Answer  between  8:40 and  8:50")
    KID530 = (2199, " No Answer  between  8:50 and  9:00")
    KID531 = (2200, " No Answer  between  9:00 and  9:10")
    KID532 = (2201, " No Answer  between  9:10 and  9:20")
    KID533 = (2202, " No Answer  between  9:20 and  9:30")
    KID534 = (2203, " No Answer  between  9:30 and  9:40")
    KID535 = (2204, " No Answer  between  9:40 and  9:50")
    KID536 = (2205, " No Answer  between  9:50 and  10:00")
    KID537 = (2206, " No Answer  between  10:00 and  10:10")
    KID538 = (2207, " No Answer  between  10:10 and  10:20")
    KID539 = (2208, " No Answer  between  10:20 and  10:30")
    KID540 = (2209, " No Answer  between  10:30 and  10:40")
    KID541 = (2210, " No Answer  between  10:40 and  10:50")
    KID542 = (2211, " No Answer  between  10:50 and  11:00")
    KID543 = (2212, " No Answer  between  11:00 and  11:10")
    KID544 = (2213, " No Answer  between  11:10 and  11:20")
    KID545 = (2214, " No Answer  between  11:20 and  11:30")
    KID546 = (2215, " No Answer  between  11:30 and  11:40")
    KID547 = (2216, " No Answer  between  11:40 and  11:50")
    KID548 = (2217, " No Answer  between  11:50 and  12:00")
    KID549 = (2218, " No Answer  between  12:00 and  12:10")
    KID550 = (2219, " No Answer  between  12:10 and  12:20")
    KID551 = (2220, " No Answer  between  12:20 and  12:30")
    KID552 = (2221, " No Answer  between  12:30 and  12:40")
    KID553 = (2222, " No Answer  between  12:40 and  12:50")
    KID554 = (2223, " No Answer  between  12:50 and  13:00")
    KID555 = (2224, " No Answer  between  13:00 and  13:10")
    KID556 = (2225, " No Answer  between  13:10 and  13:20")
    KID557 = (2226, " No Answer  between  13:20 and  13:30")
    KID558 = (2227, " No Answer  between  13:30 and  13:40")
    KID559 = (2228, " No Answer  between  13:40 and  13:50")
    KID560 = (2229, " No Answer  between  13:50 and  14:00")
    KID561 = (2230, " No Answer  between  14:00 and  14:10")
    KID562 = (2231, " No Answer  between  14:10 and  14:20")
    KID563 = (2232, " No Answer  between  14:20 and  14:30")
    KID564 = (2233, " No Answer  between  14:30 and  14:40")
    KID565 = (2234, " No Answer  between  14:40 and  14:50")
    KID566 = (2235, " No Answer  between  14:50 and  15:00")
    KID567 = (2236, " No Answer  between  15:00 and  15:10")
    KID568 = (2237, " No Answer  between  15:10 and  15:20")
    KID569 = (2238, " No Answer  between  15:20 and  15:30")
    KID570 = (2239, " No Answer  between  15:30 and  15:40")
    KID571 = (2240, " No Answer  between  15:40 and  15:50")
    KID572 = (2241, " No Answer  between  15:50 and  16:00")
    KID573 = (2242, " No Answer  between  16:00 and  16:10")
    KID574 = (2243, " No Answer  between  16:10 and  16:20")
    KID575 = (2244, " No Answer  between  16:20 and  16:30")
    KID576 = (2245, " No Answer  between  16:30 and  16:40")
    KID577 = (2246, " No Answer  between  16:40 and  16:50")
    KID578 = (2247, " No Answer  between  16:50 and  17:00")
    KID579 = (2248, " No Answer  between  17:00 and  17:10")
    KID580 = (2249, " No Answer  between  17:10 and  17:20")
    KID581 = (2250, " No Answer  between  17:20 and  17:30")
    KID582 = (2251, " No Answer  between  17:30 and  17:40")
    KID583 = (2252, " No Answer  between  17:40 and  17:50")
    KID584 = (2253, " No Answer  between  17:50 and  18:00")
    KID585 = (2254, " No Answer  between  18:00 and  18:10")
    KID586 = (2255, " No Answer  between  18:10 and  18:20")
    KID587 = (2256, " No Answer  between  18:20 and  18:30")
    KID588 = (2257, " No Answer  between  18:30 and  18:40")
    KID589 = (2258, " No Answer  between  18:40 and  18:50")
    KID590 = (2259, " No Answer  between  18:50 and  19:00")
    KID591 = (2260, " No Answer  between  19:00 and  19:10")
    KID592 = (2261, " No Answer  between  19:10 and  19:20")
    KID593 = (2262, " No Answer  between  19:20 and  19:30")
    KID594 = (2263, " No Answer  between  19:30 and  19:40")
    KID595 = (2264, " No Answer  between  19:40 and  19:50")
    KID596 = (2265, " No Answer  between  19:50 and  20:00")
    KID597 = (2266, " No Answer  between  20:00 and  20:10")
    KID598 = (2267, " No Answer  between  20:10 and  20:20")
    KID599 = (2268, " No Answer  between  20:20 and  20:30")
    KID5100 = (2269, " No Answer  between  20:30 and  20:40")
    KID5101 = (2270, " No Answer  between  20:40 and  20:50")
    KID5102 = (2271, " No Answer  between  20:50 and  21:00")
    KID5103 = (2272, " No Answer  between  21:00 and  21:10")
    KID5104 = (2273, " No Answer  between  21:10 and  21:20")
    KID5105 = (2274, " No Answer  between  21:20 and  21:30")
    KID5106 = (2275, " No Answer  between  21:30 and  21:40")
    KID5107 = (2276, " No Answer  between  21:40 and  21:50")
    KID5108 = (2277, " No Answer  between  21:50 and  22:00")
    KID5109 = (2278, " No Answer  between  22:00 and  22:10")
    KID5110 = (2279, " No Answer  between  22:10 and  22:20")
    KID5111 = (2280, " No Answer  between  22:20 and  22:30")
    KID5112 = (2281, " No Answer  between  22:30 and  22:40")
    KID5113 = (2282, " No Answer  between  22:40 and  22:50")
    KID5114 = (2283, " No Answer  between  22:50 and  23:00")
    KID5115 = (2284, " No Answer  between  23:00 and  23:10")
    KID5116 = (2285, " No Answer  between  23:10 and  23:20")
    KID5117 = (2286, " No Answer  between  23:20 and  23:30")
    KID5118 = (2287, " No Answer  between  23:30 and  23:40")
    KID5119 = (2288, " No Answer  between  23:40 and  23:50")
    KID5120 = (2289, " No Answer  between  23:50 and  0:00")
    KID5121 = (2290, " No Answer  between  0:00 and  0:10")
    KID5122 = (2291, " No Answer  between  0:10 and  0:20")
    KID5123 = (2292, " No Answer  between  0:20 and  0:30")
    KID5124 = (2293, " No Answer  between  0:30 and  0:40")
    KID5125 = (2294, " No Answer  between  0:40 and  0:50")
    KID5126 = (2295, " No Answer  between  0:50 and  1:00")
    KID5127 = (2296, " No Answer  between  1:00 and  1:10")
    KID5128 = (2297, " No Answer  between  1:10 and  1:20")
    KID5129 = (2298, " No Answer  between  1:20 and  1:30")
    KID5130 = (2299, " No Answer  between  1:30 and  1:40")
    KID5131 = (2300, " No Answer  between  1:40 and  1:50")
    KID5132 = (2301, " No Answer  between  1:50 and  2:00")
    KID5133 = (2302, " No Answer  between  2:00 and  2:10")
    KID5134 = (2303, " No Answer  between  2:10 and  2:20")
    KID5135 = (2304, " No Answer  between  2:20 and  2:30")
    KID5136 = (2305, " No Answer  between  2:30 and  2:40")
    KID5137 = (2306, " No Answer  between  2:40 and  2:50")
    KID5138 = (2307, " No Answer  between  2:50 and  3:00")
    KID5139 = (2308, " No Answer  between  3:00 and  3:10")
    KID5140 = (2309, " No Answer  between  3:10 and  3:20")
    KID5141 = (2310, " No Answer  between  3:20 and  3:30")
    KID5142 = (2311, " No Answer  between  3:30 and  3:40")
    KID5143 = (2312, " No Answer  between  3:40 and  3:50")
    KID5144 = (2313, " No Answer  between  3:50 and  4:00")
    DAATQ1A = (2314, "Adult diary - Q1a: Did you help someone from outside the hhld during the diary day?")
    DQ1BAT1 = (2315, "Adult diary - Q1b: Respondent helped someone from outside the hhld - time FIRST period of help starts:")
    DQ1BAT2 = (2316, "Adult diary - Q1b: Respondent helped someone from outside the hhld - time FIRST period of help ends:")
    DQ1BAT3 = (2317, "Adult diary - Q1b: Respondent helped someone from outside the hhld - time SECOND period of help starts:")
    DQ1BAT4 = (2318, "Adult diary - Q1b: Respondent helped someone from outside the hhld - time SECOND period of help ends:")
    DQ1BAT5 = (2319, "Adult diary - Q1b: Respondent helped someone from outside the hhld - time THIRD period of help starts:")
    DQ1BAT6 = (2320, "Adult diary - Q1b: Respondent helped someone from outside the hhld - time THIRD period of help ends:")
    DQ1BAT7 = (2321, "Adult diary - Q1b: Respondent helped someone from outside the hhld - time FOURTH period of help starts:")
    DQ1BAT8 = (2322, "Adult diary - Q1b: Respondent helped someone from outside the hhld - time FOURTH period of help ends:")
    DAATQ2 = (2323, "Adult diary - Q2: When did you fill in the diary?")
    DAATQ3 = (2324, "Adult diary - Q3: Location at START of diary day (4.00am)?")
    DAATQ4 = (2325, "Adult diary - Q4: Location at END of diary day (4.00am)?")
    ATDAATQ5A1 = (2326, "Adult diary - Q5a: work/ school/ college - IN PAID WORK?")
    ATDAATQ5A2 = (2327, "Adult diary - Q5a: work/ school/ college - AT SCHOOL OR COLLEGE?")
    ATDAATQ5A3 = (2328, "Adult diary - Q5a: work/ school/ college - NONE OF THESE?")
    DAATQ5B = (2329, "Adult diary - Q5b: (For those in paid work) Were you WORKING on the diary day?")
    DAATQ6 = (2330, "Adult diary - Q6:   (For those at school/ college) Was the diary day during TERM OR HOLIDAYS?")
    DAATQ7A = (2331, "Adult diary - Q7a: Were you on a TRIP on the diary day?")
    DAATQ7BATC = (2332, "Adult diary - Q7b: (For those on a trip to another country) Country visited?")
    DAATQ8 = (2333, "Adult diary - Q8: Was the diary day UNUSUAL for any reason?")
    DAATQ8AT1 = (2334, "Adult diary - Q8: (UNUSUAL DAY) Reason number 1 for unusual day")
    DAATQ8AT2 = (2335, "Adult diary - Q8: (UNUSUAL DAY) Reason number 2 for unusual day")
    DAATQ8AT3 = (2336, "Adult diary - Q8: (UNUSUAL DAY) Reason number 3 for unusual day")
    DAATQ8AT4 = (2337, "Adult diary - Q8: (UNUSUAL DAY) Reason number 4 for unusual day")
    DAATQ8AT5 = (2338, "Adult diary - Q8: (UNUSUAL DAY) Reason number 5 for unusual day")
    DAATQ9 = (2339, "Adult diary - Q9: Did you have any PROBLEMS filling in the diary?")
    DAATQ9AT1 = (2340, "Adult diary - Q9: (DIARY PROBLEMS) Problem number 1 in filling in diary")
    DAATQ9AT2 = (2341, "Adult diary - Q9: (DIARY PROBLEMS) Problem number 2 in filling in diary")
    DAATQ9AT3 = (2342, "Adult diary - Q9: (DIARY PROBLEMS) Problem number 3 in filling in diary")
    DAATQ9AT4 = (2343, "Adult diary - Q9: (DIARY PROBLEMS) Problem number 4 in filling in diary")
    DAATQ9AT5 = (2344, "Adult diary - Q9: (DIARY PROBLEMS) Problem number 5 in filling in diary")
    DKATQ1 = (2345, "Child diary - Q1: When did you fill in the diary?")
    DKATQ2 = (2346, "Child diary - Q2: Location at START of diary day (4.00am)?")
    DKATQ3 = (2347, "Child diary - Q3: Location at END of diary day (4.00am)?")
    DKATQ4 = (2348, "Child diary - Q4: Was the diary day during TERM OR SCHOOL HOLIDAYS?")
    DKATQ5 = (2349, "Child diary - Q5: Was the diary day UNUSUAL for any reason?")
    DKATQ5AT1 = (2350, "Child diary - Q5: (UNUSUAL DAY) Reason number 1 for unusual day")
    DKATQ5AT2 = (2351, "Child diary - Q5: (UNUSUAL DAY) Reason number 2 for unusual day")
    DKATQ5AT3 = (2352, "Child diary - Q5: (UNUSUAL DAY) Reason number 3 for unusual day")
    DKATQ5AT4 = (2353, "Child diary - Q5: (UNUSUAL DAY) Reason number 4 for unusual day")
    DKATQ5AT5 = (2354, "Child diary - Q5: (UNUSUAL DAY) Reason number 5 for unusual day")
    DKATQ6 = (2355, "Child diary - Q6: Did anyone HELP you filling in the diary?")
    DML1AT0 = (2356, "Main activity - Personal care/sleep (mins per day)")
    DML1AT1 = (2357, "Main activity - Employment (mins per day)")
    DML1AT2 = (2358, "Main activity - Study (mins per day)")
    DML1AT3 = (2359, "Main activity - Household & family care (mins per day)")
    DML1AT4 = (2360, "Main activity - Volunteer work & meetings (mins per day)")
    DML1AT5 = (2361, "Main activity - Social life & entertainment (mins per day)")
    DML1AT6 = (2362, "Main activity - Sports & outdoor activities (mins per day)")
    DML1AT7 = (2363, "Main activity - Hobbies & games (mins per day)")
    DML1AT8 = (2364, "Main activity - Mass media (mins per day)")
    DML1AT9A = (2365, "Main activity - Travel (mins per day)")
    DML1AT9B = (2366, "Main activity - Other spec/ not specfd - codes 994-999 (mins per day)")
    DSL1AT0 = (2367, "Secondary activity - Personal care/sleep (mins per day)")
    DSL1AT1 = (2368, "Secondary activity - Employment (mins per day)")
    DSL1AT2 = (2369, "Secondary activity - Study (mins per day)")
    DSL1AT3 = (2370, "Secondary activity - Household & family care (mins per day)")
    DSL1AT4 = (2371, "Secondary activity - Volunteer work & meetings (mins per day)")
    DSL1AT5 = (2372, "Secondary activity - Social life & entertainment (mins per day)")
    DSL1AT6 = (2373, "Secondary activity - Sports & outdoor activities (mins per day)")
    DSL1AT7 = (2374, "Secondary activity - Hobbies & games (mins per day)")
    DSL1AT8 = (2375, "Secondary activity - Mass media (mins per day)")
    DSL1AT9A = (2376, "Secondary activity - Travel (mins per day)")
    DSL1AT9B = (2377, "Secondary activity - Other spec/ not specfd - codes 994-999 (mins per day)")
    DML2AT00 = (2378, "Main actvty - unspecified personal care")
    DML2AT01 = (2379, "Main actvty - sleep")
    DML2AT02 = (2380, "Main actvty - eating")
    DML2AT03 = (2381, "Main actvty - other personal care")
    DML2AT10 = (2382, "Main actvty - unspecified employment")
    DML2AT11 = (2383, "Main actvty - main job")
    DML2AT12 = (2384, "Main actvty - second job")
    DML2AT13 = (2385, "Main actvty - activities related to employment")
    DML2AT20 = (2386, "Main actvty - unspecified employment")
    DML2AT21 = (2387, "Main actvty - school or university")
    DML2AT22 = (2388, "Main actvty - free time study")
    DML2AT30 = (2389, "Main actvty - unspecified household and family care")
    DML2AT31 = (2390, "Main actvty - food management")
    DML2AT32 = (2391, "Main actvty - household upkeep")
    DML2AT33 = (2392, "Main actvty - making and caring for textiles")
    DML2AT34 = (2393, "Main actvty - gardening and pet care")
    DML2AT35 = (2394, "Main actvty - construction and repairs")
    DML2AT36 = (2395, "Main actvty - shopping and services")
    DML2AT37 = (2396, "Main actvty - household management")
    DML2AT38 = (2397, "Main actvty - childcare of own household members")
    DML2AT39 = (2398, "Main actvty - help to an adult household member")
    DML2AT40 = (2399, "Main actvty - unspecified volunteer work and meetings")
    DML2AT41 = (2400, "Main actvty - organisational work")
    DML2AT42 = (2401, "Main actvty - informal help to other households")
    DML2AT43 = (2402, "Main actvty - particpatory activities")
    DML2AT50 = (2403, "Main actvty - unspecified social life and entertainment")
    DML2AT51 = (2404, "Main actvty - social life")
    DML2AT52 = (2405, "Main actvty - entertainment and culture")
    DML2AT53 = (2406, "Main actvty - resting - time out")
    DML2AT60 = (2407, "Main actvty - unspecified sports and outdoor activities")
    DML2AT61 = (2408, "Main actvty - physical exercise")
    DML2AT62 = (2409, "Main actvty - productive exercise")
    DML2AT63 = (2410, "Main actvty - sports related activities")
    DML2AT70 = (2411, "Main actvty - unspecified hobbies and games")
    DML2AT71 = (2412, "Main actvty - arts")
    DML2AT72 = (2413, "Main actvty - hobbies")
    DML2AT73 = (2414, "Main actvty - games")
    DML2AT80 = (2415, "Main actvty - unspecified mass media")
    DML2AT81 = (2416, "Main actvty - reading")
    DML2AT82 = (2417, "Main actvty - TV and video/DVD")
    DML2AT83 = (2418, "Main actvty - radio and music")
    DML2AT90 = (2419, "Main actvty - travel")
    DML2AT94 = (2420, "Main actvty - punctuating activity")
    DML2AT95 = (2421, "Main actvty - filling in time use diary")
    DML2AT99 = (2422, "Main actvty - other specified and unspecfd time use (codes 996 -999)")
    DSL2AT00 = (2423, "Scndry actvty - unspecified personal care")
    DSL2AT01 = (2424, "Scndry actvty - sleep")
    DSL2AT02 = (2425, "Scndry actvty - eating")
    DSL2AT03 = (2426, "Scndry actvty - other personal care")
    DSL2AT10 = (2427, "Scndry actvty - unspecified employment")
    DSL2AT11 = (2428, "Scndry actvty - main job")
    DSL2AT12 = (2429, "Scndry actvty - second job")
    DSL2AT13 = (2430, "Scndry actvty - activities related to employment")
    DSL2AT20 = (2431, "Scndry actvty - unspecified employment")
    DSL2AT21 = (2432, "Scndry actvty - school or university")
    DSL2AT22 = (2433, "Scndry actvty - free time study")
    DSL2AT30 = (2434, "Scndry actvty - unspecified household and family care")
    DSL2AT31 = (2435, "Scndry actvty - food management")
    DSL2AT32 = (2436, "Scndry actvty - household upkeep")
    DSL2AT33 = (2437, "Scndry actvty - making and caring for textiles")
    DSL2AT34 = (2438, "Scndry actvty - gardening and pet care")
    DSL2AT35 = (2439, "Scndry actvty - construction and repairs")
    DSL2AT36 = (2440, "Scndry actvty - shopping and services")
    DSL2AT37 = (2441, "Scndry actvty - household management")
    DSL2AT38 = (2442, "Scndry actvty - childcare of own household members")
    DSL2AT39 = (2443, "Scndry actvty - help to an adult household member")
    DSL2AT40 = (2444, "Scndry actvty - unspecified volunteer work and meetings")
    DSL2AT41 = (2445, "Scndry actvty - organisational work")
    DSL2AT42 = (2446, "Scndry actvty - informal help to other households")
    DSL2AT43 = (2447, "Scndry actvty - particpatory activities")
    DSL2AT50 = (2448, "Scndry actvty - unspecified social life and entertainment")
    DSL2AT51 = (2449, "Scndry actvty - social life")
    DSL2AT52 = (2450, "Scndry actvty - entertainment and culture")
    DSL2AT53 = (2451, "Scndry actvty - resting - time out")
    DSL2AT60 = (2452, "Scndry actvty - unspecified sports and outdoor activities")
    DSL2AT61 = (2453, "Scndry actvty - physical exercise")
    DSL2AT62 = (2454, "Scndry actvty - productive exercise")
    DSL2AT63 = (2455, "Scndry actvty - sports related activities")
    DSL2AT70 = (2456, "Scndry actvty - unspecified hobbies and games")
    DSL2AT71 = (2457, "Scndry actvty - arts")
    DSL2AT72 = (2458, "Scndry actvty - hobbies")
    DSL2AT73 = (2459, "Scndry actvty - games")
    DSL2AT80 = (2460, "Scndry actvty - unspecified mass media")
    DSL2AT81 = (2461, "Scndry actvty - reading")
    DSL2AT82 = (2462, "Scndry actvty - TV and video/DVD")
    DSL2AT83 = (2463, "Scndry actvty - radio and music")
    DSL2AT90 = (2464, "Scndry actvty - travel")
    DSL2AT94 = (2465, "Scndry actvty - punctuating activity")
    DSL2AT95 = (2466, "Scndry actvty - filling in time use diary")
    DSL2AT99 = (2467, "Scndry actvty - other specified and unspecfd time use (codes 996 -999)")
    DML3AT000 = (2468, " Unspecified personal care ( minutes per day)")
    DML3AT010 = (2469, " Unspecified Sleep  ( minutes per day)")
    DML3AT011 = (2470, " Sleep ( minutes per day)")
    DML3AT012 = (2471, " Sick in bed ( minutes per day)")
    DML3AT021 = (2472, " Eating ( minutes per day)")
    DML3AT030 = (2473, " Unspecified other personal care ( minutes per day)")
    DML3AT031 = (2474, " Wash and dress ( minutes per day)")
    DML3AT039 = (2475, " Other specified personal care ( minutes per day)")
    DML3AT100 = (2476, " Unspecified employment ( minutes per day)")
    DML3AT111 = (2477, " Working time in main job ( minutes per day)")
    DML3AT112 = (2478, " Coffee and other breaks in main job ( minutes per day)")
    DML3AT121 = (2479, " Working time in second job ( minutes per day)")
    DML3AT122 = (2480, " Coffee and other breaks in second job ( minutes per day)")
    DML3AT130 = (2481, " Unspecified activities related to empl ( minutes per day)")
    DML3AT131 = (2482, " Lunch break ( minutes per day)")
    DML3AT139 = (2483, " Other specified activities related to empl  ( minutes per day)")
    DML3AT200 = (2484, " Unspecified study ( minutes per day)")
    DML3AT210 = (2485, " Unspecified act related to school or university ( minutes per day)")
    DML3AT211 = (2486, " Classes and lectures ( minutes per day)")
    DML3AT212 = (2487, " Homework ( minutes per day)")
    DML3AT219 = (2488, " Other specified act related to school or university ( minutes per day)")
    DML3AT221 = (2489, " Free Time Study ( minutes per day)")
    DML3AT300 = (2490, " Unspecified household and family care ( minutes per day)")
    DML3AT310 = (2491, " Unspecified food management ( minutes per day)")
    DML3AT311 = (2492, " Food preparation ( minutes per day)")
    DML3AT312 = (2493, " Baking ( minutes per day)")
    DML3AT313 = (2494, " Dish washing ( minutes per day)")
    DML3AT314 = (2495, " Preserving ( minutes per day)")
    DML3AT319 = (2496, " Other specified food management ( minutes per day)")
    DML3AT320 = (2497, " Unspecified household upkeep ( minutes per day)")
    DML3AT321 = (2498, " Cleaning dwelling ( minutes per day)")
    DML3AT322 = (2499, " Cleaning yard ( minutes per day)")
    DML3AT323 = (2500, " Heating and water ( minutes per day)")
    DML3AT324 = (2501, "  Various arrangements ( minutes per day)")
    DML3AT325 = (2502, " Disposal of Waste ( minutes per day)")
    DML3AT329 = (2503, " Other specified household upkeep ( minutes per day)")
    DML3AT330 = (2504, " Unspecified making and care for textiles ( minutes per day)")
    DML3AT331 = (2505, " Laundry ( minutes per day)")
    DML3AT332 = (2506, " Ironing ( minutes per day)")
    DML3AT333 = (2507, " Handicraft and producing textiles ( minutes per day)")
    DML3AT339 = (2508, " Other specified making and care for textiles ( minutes per day)")
    DML3AT340 = (2509, " Unspecified gardening and pet care ( minutes per day)")
    DML3AT341 = (2510, " Gardening ( minutes per day)")
    DML3AT342 = (2511, " Tending domestic animals ( minutes per day)")
    DML3AT343 = (2512, " Caring for pets ( minutes per day)")
    DML3AT344 = (2513, " Walking the dog ( minutes per day)")
    DML3AT349 = (2514, " Other specified gardening and pet care ( minutes per day)")
    DML3AT350 = (2515, " Unspecified construction and repairs ( minutes per day)")
    DML3AT351 = (2516, " House construction and renovation ( minutes per day)")
    DML3AT352 = (2517, " Repairs of dwelling ( minutes per day)")
    DML3AT353 = (2518, " Making, repairing and maintaining equipment ( minutes per day)")
    DML3AT354 = (2519, " Vehicle maintenance ( minutes per day)")
    DML3AT359 = (2520, " Other specified construction and repairs ( minutes per day)")
    DML3AT360 = (2521, " Unspecified shopping and services ( minutes per day)")
    DML3AT361 = (2522, "  Shopping ( minutes per day)")
    DML3AT362 = (2523, " Commercial and administrative services ( minutes per day)")
    DML3AT363 = (2524, " Personal services ( minutes per day)")
    DML3AT369 = (2525, " Other specified shopping and services ( minutes per day)")
    DML3AT371 = (2526, " Household management not using the internet ( minutes per day)")
    DML3AT372 = (2527, " Household management using the internet ( minutes per day)")
    DML3AT380 = (2528, " Unspecified childcare ( minutes per day)")
    DML3AT381 = (2529, " Physical care and supervision ( minutes per day)")
    DML3AT382 = (2530, " Teaching the child ( minutes per day)")
    DML3AT383 = (2531, " Reading, playing and talking with child ( minutes per day)")
    DML3AT384 = (2532, " Accompanying child ( minutes per day)")
    DML3AT389 = (2533, " Other specified childcare ( minutes per day)")
    DML3AT391 = (2534, " Help to an adult household member ( minutes per day)")
    DML3AT400 = (2535, " Unspecified volunteer work and meetings ( minutes per day)")
    DML3AT410 = (2536, " Unspecified organisational work ( minutes per day)")
    DML3AT411 = (2537, " Work for an organisation ( minutes per day)")
    DML3AT412 = (2538, " Volunteer work through an organisation ( minutes per day)")
    DML3AT419 = (2539, " Other specified organisational work ( minutes per day)")
    DML3AT420 = (2540, " Unspecified informal help ( minutes per day)")
    DML3AT421 = (2541, " Food management as help ( minutes per day)")
    DML3AT422 = (2542, " Household upkeep as help ( minutes per day)")
    DML3AT423 = (2543, " Gardening and pet care as help ( minutes per day)")
    DML3AT424 = (2544, " Construction and repairs as help ( minutes per day)")
    DML3AT425 = (2545, " Shopping and services as help ( minutes per day)")
    DML3AT426 = (2546, " Help in employment and farming ( minutes per day)")
    DML3AT427 = (2547, " Childcare as help ( minutes per day)")
    DML3AT428 = (2548, " Help to an adult of another household ( minutes per day)")
    DML3AT429 = (2549, " Other specified informal help ( minutes per day)")
    DML3AT430 = (2550, " Unspecified participatory activities ( minutes per day)")
    DML3AT431 = (2551, " Meetings ( minutes per day)")
    DML3AT432 = (2552, " Religious activities ( minutes per day)")
    DML3AT439 = (2553, " Other specified participatory activities ( minutes per day)")
    DML3AT500 = (2554, " Unspecified social life and entertainment ( minutes per day)")
    DML3AT510 = (2555, " Unspecified social life ( minutes per day)")
    DML3AT511 = (2556, " Socialising with household members ( minutes per day)")
    DML3AT512 = (2557, " Visiting and receiving visitors ( minutes per day)")
    DML3AT513 = (2558, " Feasts ( minutes per day)")
    DML3AT514 = (2559, " Telephone conversation ( minutes per day)")
    DML3AT519 = (2560, " Other specified social life ( minutes per day)")
    DML3AT520 = (2561, " Unspecified entertainment and culture ( minutes per day)")
    DML3AT521 = (2562, " Cinema ( minutes per day)")
    DML3AT522 = (2563, " Theatre and concerts ( minutes per day)")
    DML3AT523 = (2564, " Art exhibitions and museums ( minutes per day)")
    DML3AT524 = (2565, " Library ( minutes per day)")
    DML3AT525 = (2566, " Sports events ( minutes per day)")
    DML3AT529 = (2567, " Other specified entertainment and culture ( minutes per day)")
    DML3AT531 = (2568, " Resting – Time out ( minutes per day)")
    DML3AT600 = (2569, " Unspecified sports and outdoor activities ( minutes per day)")
    DML3AT610 = (2570, " Unspecified physical exercise ( minutes per day)")
    DML3AT611 = (2571, " Walking and hiking ( minutes per day)")
    DML3AT612 = (2572, " Jogging and running ( minutes per day)")
    DML3AT613 = (2573, " Biking, skiing and skating ( minutes per day)")
    DML3AT614 = (2574, " Ball games ( minutes per day)")
    DML3AT615 = (2575, " Gymnastics ( minutes per day)")
    DML3AT616 = (2576, " Fitness ( minutes per day)")
    DML3AT617 = (2577, " Water sports ( minutes per day)")
    DML3AT619 = (2578, " Other specified physical exercise ( minutes per day)")
    DML3AT620 = (2579, " Unspecified productive exercise ( minutes per day)")
    DML3AT621 = (2580, " Hunting and fishing ( minutes per day)")
    DML3AT622 = (2581, " Picking berries, mushroom and herbs ( minutes per day)")
    DML3AT629 = (2582, " Other specified productive exercise ( minutes per day)")
    DML3AT631 = (2583, " Sports related activities ( minutes per day)")
    DML3AT700 = (2584, " Unspecified hobbies and games ( minutes per day)")
    DML3AT710 = (2585, " Unspecified arts ( minutes per day)")
    DML3AT711 = (2586, " Visual arts ( minutes per day)")
    DML3AT712 = (2587, " Performing arts ( minutes per day)")
    DML3AT713 = (2588, " Literary arts ( minutes per day)")
    DML3AT719 = (2589, " Other specified arts ( minutes per day)")
    DML3AT720 = (2590, " Unspecified hobbies ( minutes per day)")
    DML3AT721 = (2591, " Collecting ( minutes per day)")
    DML3AT722 = (2592, " Computing – programming ( minutes per day)")
    DML3AT723 = (2593, " Information by computing ( minutes per day)")
    DML3AT724 = (2594, " Communication by computing ( minutes per day)")
    DML3AT725 = (2595, " Other computing ( minutes per day)")
    DML3AT726 = (2596, " Correspondence ( minutes per day)")
    DML3AT729 = (2597, " Other specified hobbies ( minutes per day)")
    DML3AT730 = (2598, " Unspecified games ( minutes per day)")
    DML3AT731 = (2599, " Solo games and play ( minutes per day)")
    DML3AT732 = (2600, " Games and plays with others ( minutes per day)")
    DML3AT733 = (2601, " Computer games ( minutes per day)")
    DML3AT734 = (2602, " Gambling ( minutes per day)")
    DML3AT739 = (2603, " Other specified games ( minutes per day)")
    DML3AT800 = (2604, " Unspecified mass media ( minutes per day)")
    DML3AT810 = (2605, " Unspecified reading ( minutes per day)")
    DML3AT811 = (2606, " Reading periodicals ( minutes per day)")
    DML3AT812 = (2607, " Reading books ( minutes per day)")
    DML3AT819 = (2608, " Other specified reading ( minutes per day)")
    DML3AT821 = (2609, " Watching TV ( minutes per day)")
    DML3AT822 = (2610, " Watching video ( minutes per day)")
    DML3AT830 = (2611, " Unspecified listening to radio and music ( minutes per day)")
    DML3AT831 = (2612, "  Listening to radio ( minutes per day)")
    DML3AT832 = (2613, " Listening to recordings ( minutes per day)")
    DML3AT900 = (2614, " Travel related to unspecified time use ( minutes per day)")
    DML3AT901 = (2615, " Travel related to personal business ( minutes per day)")
    DML3AT911 = (2616, " Travel in the course of work ( minutes per day)")
    DML3AT913 = (2617, " Travel to work from home and back only ( minutes per day)")
    DML3AT914 = (2618, " Travel to work from a place other than home ( minutes per day)")
    DML3AT921 = (2619, " Travel related to education ( minutes per day)")
    DML3AT923 = (2620, " Travel escorting to/ from education ( minutes per day)")
    DML3AT931 = (2621, " Travel related to household care ( minutes per day)")
    DML3AT936 = (2622, " Travel related to shopping  ( minutes per day)")
    DML3AT937 = (2623, " Travel related to services ( minutes per day)")
    DML3AT938 = (2624, " Travel escorting a child (other than education) ( minutes per day)")
    DML3AT939 = (2625, " Travel escorting an adult (other than education) ( minutes per day)")
    DML3AT941 = (2626, " Travel related to organisational work ( minutes per day)")
    DML3AT942 = (2627, " Travel related to informal help to other households ( minutes per day)")
    DML3AT943 = (2628, " Travel related to religious activities ( minutes per day)")
    DML3AT944 = (2629, " Travel related to participatory act except rel act ( minutes per day)")
    DML3AT950 = (2630, " Travel to visit friends/ relatives in their homes  ( minutes per day)")
    DML3AT951 = (2631, " Travel related to other social activities ( minutes per day)")
    DML3AT952 = (2632, " Travel related to entertainment and culture ( minutes per day)")
    DML3AT961 = (2633, " Travel related to physical exercise ( minutes per day)")
    DML3AT962 = (2634, " Travel related to hunting & fishing ( minutes per day)")
    DML3AT963 = (2635, " T rltd to productive ex except hunting & fishing ( minutes per day)")
    DML3AT971 = (2636, "  Travel related to gambling ( minutes per day)")
    DML3AT972 = (2637, " Travel related to hobbies other than gambling ( minutes per day)")
    DML3AT981 = (2638, " Travel to holiday base ( minutes per day)")
    DML3AT982 = (2639, " Travel for day trip/ just walk ( minutes per day)")
    DML3AT989 = (2640, " Other specified travel ( minutes per day)")
    DML3AT994 = (2641, " Punctuating Activity( minutes per day)")
    DML3AT995 = (2642, " Filling in the time use diary ( minutes per day)")
    DML3AT996 = (2643, "  No main activity, no idea what it might be ( minutes per day)")
    DML3AT997 = (2644, "  No main activity, some idea what it might be ( minutes per day)")
    DML3AT998 = (2645, " Illegible activity ( minutes per day)")
    DML3AT999 = (2646, " Unspecified time use ( minutes per day)")
    DSL3AT000 = (2647, " Unspecified personal care ( minutes per day)")
    DSL3AT010 = (2648, " Unspecified Sleep  ( minutes per day)")
    DSL3AT011 = (2649, " Sleep ( minutes per day)")
    DSL3AT012 = (2650, " Sick in bed ( minutes per day)")
    DSL3AT021 = (2651, " Eating ( minutes per day)")
    DSL3AT030 = (2652, " Unspecified other personal care ( minutes per day)")
    DSL3AT031 = (2653, " Wash and dress ( minutes per day)")
    DSL3AT039 = (2654, " Other specified personal care ( minutes per day)")
    DSL3AT100 = (2655, " Unspecified employment ( minutes per day)")
    DSL3AT111 = (2656, " Working time in main job ( minutes per day)")
    DSL3AT112 = (2657, " Coffee and other breaks in main job ( minutes per day)")
    DSL3AT121 = (2658, " Working time in second job ( minutes per day)")
    DSL3AT122 = (2659, " Coffee and other breaks in second job ( minutes per day)")
    DSL3AT130 = (2660, " Unspecified activities related to empl ( minutes per day)")
    DSL3AT131 = (2661, " Lunch break ( minutes per day)")
    DSL3AT139 = (2662, " Other specified activities related to empl  ( minutes per day)")
    DSL3AT200 = (2663, " Unspecified study ( minutes per day)")
    DSL3AT210 = (2664, " Unspecified act related to school or university ( minutes per day)")
    DSL3AT211 = (2665, " Classes and lectures ( minutes per day)")
    DSL3AT212 = (2666, " Homework ( minutes per day)")
    DSL3AT219 = (2667, " Other specified act related to school or university ( minutes per day)")
    DSL3AT221 = (2668, " Free Time Study ( minutes per day)")
    DSL3AT300 = (2669, " Unspecified household and family care ( minutes per day)")
    DSL3AT310 = (2670, " Unspecified food management ( minutes per day)")
    DSL3AT311 = (2671, " Food preparation ( minutes per day)")
    DSL3AT312 = (2672, " Baking ( minutes per day)")
    DSL3AT313 = (2673, " Dish washing ( minutes per day)")
    DSL3AT314 = (2674, " Preserving ( minutes per day)")
    DSL3AT319 = (2675, " Other specified food management ( minutes per day)")
    DSL3AT320 = (2676, " Unspecified household upkeep ( minutes per day)")
    DSL3AT321 = (2677, " Cleaning dwelling ( minutes per day)")
    DSL3AT322 = (2678, " Cleaning yard ( minutes per day)")
    DSL3AT323 = (2679, " Heating and water ( minutes per day)")
    DSL3AT324 = (2680, "  Various arrangements ( minutes per day)")
    DSL3AT325 = (2681, " Disposal of Waste ( minutes per day)")
    DSL3AT329 = (2682, " Other specified household upkeep ( minutes per day)")
    DSL3AT330 = (2683, " Unspecified making and care for textiles ( minutes per day)")
    DSL3AT331 = (2684, " Laundry ( minutes per day)")
    DSL3AT332 = (2685, " Ironing ( minutes per day)")
    DSL3AT333 = (2686, " Handicraft and producing textiles ( minutes per day)")
    DSL3AT339 = (2687, " Other specified making and care for textiles ( minutes per day)")
    DSL3AT340 = (2688, " Unspecified gardening and pet care ( minutes per day)")
    DSL3AT341 = (2689, " Gardening ( minutes per day)")
    DSL3AT342 = (2690, " Tending domestic animals ( minutes per day)")
    DSL3AT343 = (2691, " Caring for pets ( minutes per day)")
    DSL3AT344 = (2692, " Walking the dog ( minutes per day)")
    DSL3AT349 = (2693, " Other specified gardening and pet care ( minutes per day)")
    DSL3AT350 = (2694, " Unspecified construction and repairs ( minutes per day)")
    DSL3AT351 = (2695, " House construction and renovation ( minutes per day)")
    DSL3AT352 = (2696, " Repairs of dwelling ( minutes per day)")
    DSL3AT353 = (2697, " Making, repairing and maintaining equipment ( minutes per day)")
    DSL3AT354 = (2698, " Vehicle maintenance ( minutes per day)")
    DSL3AT359 = (2699, " Other specified construction and repairs ( minutes per day)")
    DSL3AT360 = (2700, " Unspecified shopping and services ( minutes per day)")
    DSL3AT361 = (2701, "  Shopping ( minutes per day)")
    DSL3AT362 = (2702, " Commercial and administrative services ( minutes per day)")
    DSL3AT363 = (2703, " Personal services ( minutes per day)")
    DSL3AT369 = (2704, " Other specified shopping and services ( minutes per day)")
    DSL3AT371 = (2705, " Household management not using the internet ( minutes per day)")
    DSL3AT372 = (2706, " Household management using the internet ( minutes per day)")
    DSL3AT380 = (2707, " Unspecified childcare ( minutes per day)")
    DSL3AT381 = (2708, " Physical care and supervision ( minutes per day)")
    DSL3AT382 = (2709, " Teaching the child ( minutes per day)")
    DSL3AT383 = (2710, " Reading, playing and talking with child ( minutes per day)")
    DSL3AT384 = (2711, " Accompanying child ( minutes per day)")
    DSL3AT389 = (2712, " Other specified childcare ( minutes per day)")
    DSL3AT391 = (2713, " Help to an adult household member ( minutes per day)")
    DSL3AT400 = (2714, " Unspecified volunteer work and meetings ( minutes per day)")
    DSL3AT410 = (2715, " Unspecified organisational work ( minutes per day)")
    DSL3AT411 = (2716, " Work for an organisation ( minutes per day)")
    DSL3AT412 = (2717, " Volunteer work through an organisation ( minutes per day)")
    DSL3AT419 = (2718, " Other specified organisational work ( minutes per day)")
    DSL3AT420 = (2719, " Unspecified informal help ( minutes per day)")
    DSL3AT421 = (2720, " Food management as help ( minutes per day)")
    DSL3AT422 = (2721, " Household upkeep as help ( minutes per day)")
    DSL3AT423 = (2722, " Gardening and pet care as help ( minutes per day)")
    DSL3AT424 = (2723, " Construction and repairs as help ( minutes per day)")
    DSL3AT425 = (2724, " Shopping and services as help ( minutes per day)")
    DSL3AT426 = (2725, " Help in employment and farming ( minutes per day)")
    DSL3AT427 = (2726, " Childcare as help ( minutes per day)")
    DSL3AT428 = (2727, " Help to an adult of another household ( minutes per day)")
    DSL3AT429 = (2728, " Other specified informal help ( minutes per day)")
    DSL3AT430 = (2729, " Unspecified participatory activities ( minutes per day)")
    DSL3AT431 = (2730, " Meetings ( minutes per day)")
    DSL3AT432 = (2731, " Religious activities ( minutes per day)")
    DSL3AT439 = (2732, " Other specified participatory activities ( minutes per day)")
    DSL3AT500 = (2733, " Unspecified social life and entertainment ( minutes per day)")
    DSL3AT510 = (2734, " Unspecified social life ( minutes per day)")
    DSL3AT511 = (2735, " Socialising with household members ( minutes per day)")
    DSL3AT512 = (2736, " Visiting and receiving visitors ( minutes per day)")
    DSL3AT513 = (2737, " Feasts ( minutes per day)")
    DSL3AT514 = (2738, " Telephone conversation ( minutes per day)")
    DSL3AT519 = (2739, " Other specified social life ( minutes per day)")
    DSL3AT520 = (2740, " Unspecified entertainment and culture ( minutes per day)")
    DSL3AT521 = (2741, " Cinema ( minutes per day)")
    DSL3AT522 = (2742, " Theatre and concerts ( minutes per day)")
    DSL3AT523 = (2743, " Art exhibitions and museums ( minutes per day)")
    DSL3AT524 = (2744, " Library ( minutes per day)")
    DSL3AT525 = (2745, " Sports events ( minutes per day)")
    DSL3AT529 = (2746, " Other specified entertainment and culture ( minutes per day)")
    DSL3AT531 = (2747, " Resting – Time out ( minutes per day)")
    DSL3AT600 = (2748, " Unspecified sports and outdoor activities ( minutes per day)")
    DSL3AT610 = (2749, " Unspecified physical exercise ( minutes per day)")
    DSL3AT611 = (2750, " Walking and hiking ( minutes per day)")
    DSL3AT612 = (2751, " Jogging and running ( minutes per day)")
    DSL3AT613 = (2752, " Biking, skiing and skating ( minutes per day)")
    DSL3AT614 = (2753, " Ball games ( minutes per day)")
    DSL3AT615 = (2754, " Gymnastics ( minutes per day)")
    DSL3AT616 = (2755, " Fitness ( minutes per day)")
    DSL3AT617 = (2756, " Water sports ( minutes per day)")
    DSL3AT619 = (2757, " Other specified physical exercise ( minutes per day)")
    DSL3AT620 = (2758, " Unspecified productive exercise ( minutes per day)")
    DSL3AT621 = (2759, " Hunting and fishing ( minutes per day)")
    DSL3AT622 = (2760, " Picking berries, mushroom and herbs ( minutes per day)")
    DSL3AT629 = (2761, " Other specified productive exercise ( minutes per day)")
    DSL3AT631 = (2762, " Sports related activities ( minutes per day)")
    DSL3AT700 = (2763, " Unspecified hobbies and games ( minutes per day)")
    DSL3AT710 = (2764, " Unspecified arts ( minutes per day)")
    DSL3AT711 = (2765, " Visual arts ( minutes per day)")
    DSL3AT712 = (2766, " Performing arts ( minutes per day)")
    DSL3AT713 = (2767, " Literary arts ( minutes per day)")
    DSL3AT719 = (2768, " Other specified arts ( minutes per day)")
    DSL3AT720 = (2769, " Unspecified hobbies ( minutes per day)")
    DSL3AT721 = (2770, " Collecting ( minutes per day)")
    DSL3AT722 = (2771, " Computing – programming ( minutes per day)")
    DSL3AT723 = (2772, " Information by computing ( minutes per day)")
    DSL3AT724 = (2773, " Communication by computing ( minutes per day)")
    DSL3AT725 = (2774, " Other computing ( minutes per day)")
    DSL3AT726 = (2775, " Correspondence ( minutes per day)")
    DSL3AT729 = (2776, " Other specified hobbies ( minutes per day)")
    DSL3AT730 = (2777, " Unspecified games ( minutes per day)")
    DSL3AT731 = (2778, " Solo games and play ( minutes per day)")
    DSL3AT732 = (2779, " Games and plays with others ( minutes per day)")
    DSL3AT733 = (2780, " Computer games ( minutes per day)")
    DSL3AT734 = (2781, " Gambling ( minutes per day)")
    DSL3AT739 = (2782, " Other specified games ( minutes per day)")
    DSL3AT800 = (2783, " Unspecified mass media ( minutes per day)")
    DSL3AT810 = (2784, " Unspecified reading ( minutes per day)")
    DSL3AT811 = (2785, " Reading periodicals ( minutes per day)")
    DSL3AT812 = (2786, " Reading books ( minutes per day)")
    DSL3AT819 = (2787, " Other specified reading ( minutes per day)")
    DSL3AT821 = (2788, " Watching TV ( minutes per day)")
    DSL3AT822 = (2789, " Watching video ( minutes per day)")
    DSL3AT830 = (2790, " Unspecified listening to radio and music ( minutes per day)")
    DSL3AT831 = (2791, "  Listening to radio ( minutes per day)")
    DSL3AT832 = (2792, " Listening to recordings ( minutes per day)")
    DSL3AT900 = (2793, " Travel related to unspecified time use ( minutes per day)")
    DSL3AT901 = (2794, " Travel related to personal business ( minutes per day)")
    DSL3AT911 = (2795, " Travel in the course of work ( minutes per day)")
    DSL3AT913 = (2796, " Travel to work from home and back only ( minutes per day)")
    DSL3AT914 = (2797, " Travel to work from a place other than home ( minutes per day)")
    DSL3AT921 = (2798, " Travel related to education ( minutes per day)")
    DSL3AT923 = (2799, " Travel escorting to/ from education ( minutes per day)")
    DSL3AT931 = (2800, " Travel related to household care ( minutes per day)")
    DSL3AT936 = (2801, " Travel related to shopping  ( minutes per day)")
    DSL3AT937 = (2802, " Travel related to services ( minutes per day)")
    DSL3AT938 = (2803, " Travel escorting a child (other than education) ( minutes per day)")
    DSL3AT939 = (2804, " Travel escorting an adult (other than education) ( minutes per day)")
    DSL3AT941 = (2805, " Travel related to organisational work ( minutes per day)")
    DSL3AT942 = (2806, " Travel related to informal help to other households ( minutes per day)")
    DSL3AT943 = (2807, " Travel related to religious activities ( minutes per day)")
    DSL3AT944 = (2808, " Travel related to participatory act other than rel act ( minutes per day)")
    DSL3AT951 = (2809, " Travel to visit friends/ relatives in their homes  ( minutes per day)")
    DSL3AT950 = (2810, " Travel related to other social activities ( minutes per day)")
    DSL3AT952 = (2811, " Travel related to entertainment and culture ( minutes per day)")
    DSL3AT961 = (2812, " Travel related to physical exercise ( minutes per day)")
    DSL3AT962 = (2813, " Travel related to hunting & fishing ( minutes per day)")
    DSL3AT963 = (2814, " T rltd to productive ex except hunting & fishing ( minutes per day)")
    DSL3AT971 = (2815, "  Travel related to gambling ( minutes per day)")
    DSL3AT972 = (2816, " Travel related to hobbies other than gambling ( minutes per day)")
    DSL3AT981 = (2817, " Travel to holiday base ( minutes per day)")
    DSL3AT982 = (2818, " Travel for day trip/ just walk ( minutes per day)")
    DSL3AT989 = (2819, " Other specified travel ( minutes per day)")
    DSL3AT994 = (2820, " Punctuating Activity( minutes per day)")
    DSL3AT995 = (2821, " Filling in the time use diary ( minutes per day)")
    DSL3AT996 = (2822, " No main activity, no idea what it might be ( minutes per day)")
    DSL3AT997 = (2823, " No main activity, some idea what it might be ( minutes per day)")
    DSL3AT998 = (2824, " Illegible activity ( minutes per day)")
    DSL3AT999 = (2825, " Unspecified time use ( minutes per day)")
    DM4AT1391 = (2826, " Activities related to job seeking ( minutes per day)")
    DM4AT1399 = (2827, " Other specified activities related to empl ( minutes per day)")
    DM4AT3530 = (2828, "Main actvty - unspecified making, repairing, maintaining equipment")
    DM4AT3531 = (2829, "  Woodcraft, metal craft, sculpture and pottery ( minutes per day)")
    DM4AT3539 = (2830, " Other specified making, repairing&maintaining equipment ( minutes per day)")
    DM4AT3610 = (2831, "Main actvty - unspecified shopping")
    DM4AT3611 = (2832, " Shopping mainly for food ( minutes per day)")
    DM4AT3612 = (2833, " Shopping mainly for clothing ( minutes per day)")
    DM4AT3613 = (2834, " Shopping mainly related to accommodation ( minutes per day)")
    DM4AT3614 = (2835, " Shopping or browsing at car boot sales or antique fairs ( minutes per day)")
    DM4AT3615 = (2836, "  Window shopping or other shopping as leisure ( minutes per day)")
    DM4AT3619 = (2837, " Other specified shopping ( minutes per day)")
    DM4AT3720 = (2838, "Main actvty - unspecified hshld management using the internet")
    DM4AT3721 = (2839, " Shpping for and ordering unspecified g&s via internet ( minutes per day)")
    DM4AT3722 = (2840, " Shpping for and ordering food via the internet ( minutes per day)")
    DM4AT3723 = (2841, " Shpping for and ordering clothing via the internet ( minutes per day)")
    DM4AT3724 = (2842, " Shpping for and ordering g&s related to acc via internet ( minutes per day)")
    DM4AT3725 = (2843, " Shpping for and ordering mass media via the internet ( minutes per day)")
    DM4AT3726 = (2844, " Shpping for and ordering entertainment via the internet ( minutes per day)")
    DM4AT3727 = (2845, " Banking and bill paying via the internet ( minutes per day)")
    DM4AT3729 = (2846, " Other specified household management using internet ( minutes per day)")
    DM4AT3810 = (2847, "Main actvty - unspecified physical care & supervision of child")
    DM4AT3811 = (2848, " Feeding the child ( minutes per day)")
    DM4AT3819 = (2849, " Other specified physical care & supervision of a child ( minutes per day)")
    DM4AT3910 = (2850, "Main actvty - unspecified help to an adult member")
    DM4AT3911 = (2851, " Physical care & supervision of an adult household member ( minutes per day)")
    DM4AT3914 = (2852, " Accompanying an adult household member ( minutes per day)")
    DM4AT3919 = (2853, " Other specified help to an adult household member ( minutes per day)")
    DM4AT4270 = (2854, "Main actvty - unspecified childcare as help to other hshld")
    DM4AT4271 = (2855, " Physical care and supervision of a child as help ( minutes per day)")
    DM4AT4272 = (2856, "   Teaching the child as help ( minutes per day)")
    DM4AT4273 = (2857, " Reading, playing & talking to the child as help ( minutes per day)")
    DM4AT4274 = (2858, " Accompanying the child as help ( minutes per day)")
    DM4AT4279 = (2859, " Other specified childcare as help ( minutes per day)")
    DM4AT4280 = (2860, "Main actvty - unspecified help to an adult member of another hshld")
    DM4AT4281 = (2861, " Physical care and supervision of an adult as help ( minutes per day)")
    DM4AT4284 = (2862, " Accompanying an adult as help ( minutes per day)")
    DM4AT4289 = (2863, " Other specified help to an adult member of another hh ( minutes per day)")
    DM4AT5220 = (2864, "Main actvty - unspecified theatre or concerts")
    DM4AT5221 = (2865, " Plays, musicals or pantomimes ( minutes per day)")
    DM4AT5222 = (2866, " Opera, operetta or light opera ( minutes per day)")
    DM4AT5223 = (2867, "    Concerts or other performances of classical music ( minutes per day)")
    DM4AT5224 = (2868, " Live music except classical concerts, opera and musicals ( minutes per day)")
    DM4AT5225 = (2869, "    Dance performances ( minutes per day)")
    DM4AT5229 = (2870, " Other specified theatre or concerts ( minutes per day)")
    DM4AT5240 = (2871, "Main actvty - unspecified library")
    DM4AT5241 = (2872, " Brwing bks rcds audio video,CDs,VDs from library ( minutes per day)")
    DM4AT5242 = (2873, " Ref to books and other library materials within a library ( minutes per day)")
    DM4AT5243 = (2874, " Using internet in the library ( minutes per day)")
    DM4AT5244 = (2875, " Using computers in the library other than internet use ( minutes per day)")
    DM4AT5245 = (2876, " Reading newspapers in a library ( minutes per day)")
    DM4AT5246 = (2877, " Listening to music in a library ( minutes per day)")
    DM4AT5249 = (2878, " Other specified library activities ( minutes per day)")
    DM4AT5291 = (2879, "  Visiting a historical site ( minutes per day)")
    DM4AT5292 = (2880, "  Visiting a wildlife site ( minutes per day)")
    DM4AT5293 = (2881, "  Visiting a botanical site ( minutes per day)")
    DM4AT5294 = (2882, " Visiting a leisure park ( minutes per day)")
    DM4AT5295 = (2883, "  Visiting an urban park, playground, play area ( minutes per day)")
    DM4AT5299 = (2884, "   Other specified entertainment or culture ( minutes per day)")
    DM4AT6111 = (2885, " Taking a walk or hike that lasts at least 2 miles or 1 hour ( minutes per day)")
    DM4AT6119 = (2886, " Biking ( minutes per day)")
    DM4AT6131 = (2887, " Skiing or skating ( minutes per day)")
    DM4AT6132 = (2888, " Unspecified ball games ( minutes per day)")
    DM4AT6140 = (2889, "Main actvty - unspecified ball games")
    DM4AT6141 = (2890, " Indoor pairs or doubles games ( minutes per day)")
    DM4AT6142 = (2891, " Indoor team games ( minutes per day)")
    DM4AT6143 = (2892, " Outdoor pairs or doubles games ( minutes per day)")
    DM4AT6144 = (2893, " Outdoor team games ( minutes per day)")
    DM4AT6149 = (2894, " Other specified ball games ( minutes per day)")
    DM4AT6170 = (2895, "Main actvty - unspecified water sports")
    DM4AT6171 = (2896, " Swimming ( minutes per day)")
    DM4AT6179 = (2897, " Other specified water sports ( minutes per day)")
    DM4AT6310 = (2898, "Main actvty - unspecified sports related activities")
    DM4AT6311 = (2899, " Activities related to sports ( minutes per day)")
    DM4AT6312 = (2900, " Activities related to productive exercise ( minutes per day)")
    DM4AT7110 = (2901, "Main actvty - unspecified visual arts")
    DM4AT7111 = (2902, " Painting, drawing or other graphic arts ( minutes per day)")
    DM4AT7112 = (2903, " Making videos, taking photographs or rltd photo act ( minutes per day)")
    DM4AT7119 = (2904, " Other specified visual arts ( minutes per day)")
    DM4AT7120 = (2905, "Main actvty - unspecified performing arts")
    DM4AT7121 = (2906, " Singing or other musical activities ( minutes per day)")
    DM4AT7129 = (2907, " Other specified performing arts ( minutes per day)")
    DM4AT7230 = (2908, "Main actvty - unspecified information by computing")
    DM4AT7231 = (2909, " Information searching on the internet ( minutes per day)")
    DM4AT7239 = (2910, " Other specified information by computing ( minutes per day)")
    DM4AT7240 = (2911, "Main actvty - unspecified communication by computer")
    DM4AT7241 = (2912, "  Communication on the internet ( minutes per day)")
    DM4AT7249 = (2913, " Other specified communication by computing ( minutes per day)")
    DM4AT7250 = (2914, "Main actvty - unspecified other computing")
    DM4AT7251 = (2915, "  Unspecified internet use ( minutes per day)")
    DM4AT7259 = (2916, " Other specified computing ( minutes per day)")
    DM4AT7320 = (2917, "Main actvty - unspecified games & play with others")
    DM4AT7321 = (2918, " Billiards, pool, snooker or petanque ( minutes per day)")
    DM4AT7322 = (2919, " Chess and bridge ( minutes per day)")
    DM4AT7329 = (2920, " Other specified parlour games and play ( minutes per day)")
    DM4AT8210 = (2921, "Main actvty - unspecified TV watching")
    DM4AT8211 = (2922, " Watching a film on TV ( minutes per day)")
    DM4AT8212 = (2923, " Watching sport on TV ( minutes per day)")
    DM4AT8219 = (2924, " Other specified TV watching ( minutes per day)")
    DM4AT8220 = (2925, "Main actvty - unspecified video watching")
    DM4AT8221 = (2926, " Watching a film on video ( minutes per day)")
    DM4AT8222 = (2927, " Watching sport on video ( minutes per day)")
    DM4AT8229 = (2928, " Other specified video watching ( minutes per day)")
    DM4AT8310 = (2929, "Main actvty - unspecified listening to radio & music")
    DM4AT8311 = (2930, " Listening to music on the radio ( minutes per day)")
    DM4AT8312 = (2931, " Listening to sport on the radio ( minutes per day)")
    DM4AT8319 = (2932, " Other specified radio listening ( minutes per day)")
    DS4AT1391 = (2933, " Activities related to job seeking ( minutes per day)")
    DS4AT1399 = (2934, " Other specified activities related to empl ( minutes per day)")
    DS4AT3530 = (2935, "Scndry actvty - unspecified making, repairing, maintaining equipment")
    DS4AT3531 = (2936, "  Woodcraft, metal craft, sculpture and pottery ( minutes per day)")
    DS4AT3539 = (2937, " Other specified making, repairing&maintaining equipment ( minutes per day)")
    DS4AT3610 = (2938, "Scndry actvty - unspecified shopping")
    DS4AT3611 = (2939, " Shopping mainly for food ( minutes per day)")
    DS4AT3612 = (2940, " Shopping mainly for clothing ( minutes per day)")
    DS4AT3613 = (2941, " Shopping mainly related to accommodation ( minutes per day)")
    DS4AT3614 = (2942, " Shopping or browsing at car boot sales or antique fairs ( minutes per day)")
    DS4AT3615 = (2943, "  Window shopping or other shopping as leisure ( minutes per day)")
    DS4AT3619 = (2944, " Other specified shopping ( minutes per day)")
    DS4AT3720 = (2945, "Scndry actvty - unspecified hshld management using the internet")
    DS4AT3721 = (2946, " Shpping for and ordering unspecified g&s via internet ( minutes per day)")
    DS4AT3722 = (2947, " Shpping for and ordering food via the internet ( minutes per day)")
    DS4AT3723 = (2948, " Shpping for and ordering clothing via the internet ( minutes per day)")
    DS4AT3724 = (2949, " Shpping for and ordering g&s related to acc via internet ( minutes per day)")
    DS4AT3725 = (2950, " Shpping for and ordering mass media via the internet ( minutes per day)")
    DS4AT3726 = (2951, " Shpping for and ordering entertainment via the internet ( minutes per day)")
    DS4AT3727 = (2952, " Banking and bill paying via the internet ( minutes per day)")
    DS4AT3729 = (2953, " Other specified household management using internet ( minutes per day)")
    DS4AT3810 = (2954, "Scndry actvty - unspecified physical care & supervision of child")
    DS4AT3811 = (2955, " Feeding the child ( minutes per day)")
    DS4AT3819 = (2956, " Other specified physical care & supervision of a child ( minutes per day)")
    DS4AT3910 = (2957, "Scndry actvty - unspecified help to an adult member")
    DS4AT3911 = (2958, " Physical care & supervision of an adult household member ( minutes per day)")
    DS4AT3914 = (2959, " Accompanying an adult household member ( minutes per day)")
    DS4AT3919 = (2960, " Other specified help to an adult household member ( minutes per day)")
    DS4AT4270 = (2961, "Scndry actvty - unspecified childcare as help to other hshld")
    DS4AT4271 = (2962, " Physical care and supervision of a child as help ( minutes per day)")
    DS4AT4272 = (2963, "   Teaching the child as help ( minutes per day)")
    DS4AT4273 = (2964, " Reading, playing & talking to the child as help ( minutes per day)")
    DS4AT4274 = (2965, " Accompanying the child as help ( minutes per day)")
    DS4AT4279 = (2966, " Other specified childcare as help ( minutes per day)")
    DS4AT4280 = (2967, "Scndry actvty - unspecified help to an adult member of another hshld")
    DS4AT4281 = (2968, " Physical care and supervision of an adult as help ( minutes per day)")
    DS4AT4284 = (2969, " Accompanying an adult as help ( minutes per day)")
    DS4AT4289 = (2970, " Other specified help to an adult member of another hh ( minutes per day)")
    DS4AT5220 = (2971, "Scndry actvty - unspecified theatre or concerts")
    DS4AT5221 = (2972, " Plays, musicals or pantomimes ( minutes per day)")
    DS4AT5222 = (2973, " Opera, operetta or light opera ( minutes per day)")
    DS4AT5223 = (2974, "    Concerts or other performances of classical music ( minutes per day)")
    DS4AT5224 = (2975, " Live music except classical concerts, opera and musicals ( minutes per day)")
    DS4AT5225 = (2976, "    Dance performances ( minutes per day)")
    DS4AT5229 = (2977, " Other specified theatre or concerts ( minutes per day)")
    DS4AT5240 = (2978, "Scndry actvty - unspecified library")
    DS4AT5241 = (2979, " Brwing bks rcds audio video,CDs,VDs from library ( minutes per day)")
    DS4AT5242 = (2980, " Ref to books and other library materials within a library ( minutes per day)")
    DS4AT5243 = (2981, " Using internet in the library ( minutes per day)")
    DS4AT5244 = (2982, " Using computers in the library other than internet use ( minutes per day)")
    DS4AT5245 = (2983, " Reading newspapers in a library ( minutes per day)")
    DS4AT5246 = (2984, " Listening to music in a library ( minutes per day)")
    DS4AT5249 = (2985, " Other specified library activities ( minutes per day)")
    DS4AT5291 = (2986, "  Visiting a historical site ( minutes per day)")
    DS4AT5292 = (2987, "  Visiting a wildlife site ( minutes per day)")
    DS4AT5293 = (2988, "  Visiting a botanical site ( minutes per day)")
    DS4AT5294 = (2989, " Visiting a leisure park ( minutes per day)")
    DS4AT5295 = (2990, "  Visiting an urban park, playground, play area ( minutes per day)")
    DS4AT5299 = (2991, "   Other specified entertainment or culture ( minutes per day)")
    DS4AT6111 = (2992, " Taking a walk or hike that lasts at least 2 miles or 1 hour ( minutes per day)")
    DS4AT6119 = (2993, " Biking ( minutes per day)")
    DS4AT6131 = (2994, " Skiing or skating ( minutes per day)")
    DS4AT6132 = (2995, " Unspecified ball games ( minutes per day)")
    DS4AT6140 = (2996, "Scndry actvty - unspecified ball games")
    DS4AT6141 = (2997, " Indoor pairs or doubles games ( minutes per day)")
    DS4AT6142 = (2998, " Indoor team games ( minutes per day)")
    DS4AT6143 = (2999, " Outdoor pairs or doubles games ( minutes per day)")
    DS4AT6144 = (3000, " Outdoor team games ( minutes per day)")
    DS4AT6149 = (3001, " Other specified ball games ( minutes per day)")
    DS4AT6170 = (3002, "Scndry actvty - unspecified water sports")
    DS4AT6171 = (3003, " Swimming ( minutes per day)")
    DS4AT6179 = (3004, " Other specified water sports ( minutes per day)")
    DS4AT6310 = (3005, "Scndry actvty - unspecified sports related activities")
    DS4AT6311 = (3006, " Activities related to sports ( minutes per day)")
    DS4AT6312 = (3007, " Activities related to productive exercise ( minutes per day)")
    DS4AT7110 = (3008, "Scndry actvty - unspecified visual arts")
    DS4AT7111 = (3009, " Painting, drawing or other graphic arts ( minutes per day)")
    DS4AT7112 = (3010, " Making videos, taking photographs or rltd photo act ( minutes per day)")
    DS4AT7119 = (3011, " Other specified visual arts ( minutes per day)")
    DS4AT7120 = (3012, "Scndry actvty - unspecified performing arts")
    DS4AT7121 = (3013, " Singing or other musical activities ( minutes per day)")
    DS4AT7129 = (3014, " Other specified performing arts ( minutes per day)")
    DS4AT7230 = (3015, "Scndry actvty - unspecified information by computing")
    DS4AT7231 = (3016, " Information searching on the internet ( minutes per day)")
    DS4AT7239 = (3017, " Other specified information by computing ( minutes per day)")
    DS4AT7240 = (3018, "Scndry actvty - unspecified communication by computer")
    DS4AT7241 = (3019, "  Communication on the internet ( minutes per day)")
    DS4AT7249 = (3020, " Other specified communication by computing ( minutes per day)")
    DS4AT7250 = (3021, "Scndry actvty - unspecified other computing")
    DS4AT7251 = (3022, "  Unspecified internet use ( minutes per day)")
    DS4AT7259 = (3023, " Other specified computing ( minutes per day)")
    DS4AT7320 = (3024, "Scndry actvty - unspecified games & play with others")
    DS4AT7321 = (3025, " Billiards, pool, snooker or petanque ( minutes per day)")
    DS4AT7322 = (3026, " Chess and bridge ( minutes per day)")
    DS4AT7329 = (3027, " Other specified parlour games and play ( minutes per day)")
    DS4AT8210 = (3028, "Scndry actvty - unspecified TV watching")
    DS4AT8211 = (3029, " Watching a film on TV ( minutes per day)")
    DS4AT8212 = (3030, " Watching sport on TV ( minutes per day)")
    DS4AT8219 = (3031, " Other specified TV watching ( minutes per day)")
    DS4AT8220 = (3032, "Scndry actvty - unspecified video watching")
    DS4AT8221 = (3033, " Watching a film on video ( minutes per day)")
    DS4AT8222 = (3034, " Watching sport on video ( minutes per day)")
    DS4AT8229 = (3035, " Other specified video watching ( minutes per day)")
    DS4AT8310 = (3036, "Scndry actvty - unspecified listening to radio & music")
    DS4AT8311 = (3037, " Listening to music on the radio ( minutes per day)")
    DS4AT8312 = (3038, " Listening to sport on the radio ( minutes per day)")
    DS4AT8319 = (3039, " Other specified radio listening ( minutes per day)")
    MTOTTIME = (3040, "total amount of time spent in primary activities in 24hrs - sum of 3rd level codes")
    STOTTIME = (3041, "Total amount of time spent in SECONDARY activities in 24hrs - sum of 3rd level codes")
    LOC_00 = (3042, "Total location/ travel time (mins per day) - not specified")
    LOC_01 = (3043, "Total location time (mins per day) - location not specified (not travelling)")
    LOC_02 = (3044, "Total location time (mins per day) - at home")
    LOC_03 = (3045, "Total location time (mins per day) - at second home")
    LOC_04 = (3046, "Total location time (mins per day) - at work or school")
    LOC_05 = (3047, "Total location time (mins per day) - at other people's home")
    LOC_06 = (3048, "Total location time (mins per day) - at restaurant, cafe, pub")
    LOC_07 = (3049, "Total location time (mins per day) - at sports facility")
    LOC_08 = (3050, "Total location time (mins per day) - at arts or cultural centre")
    LOC_09 = (3051, "Total location time (mins per day) - at countryside, seaside")
    LOC_10 = (3052, "Total location time (mins per day) - at other specified location")
    LOC_11 = (3053, "Total travel time (mins per day) - PRIVATE transport not specified")
    LOC_12 = (3054, "Total travel time (mins per day) - on foot")
    LOC_13 = (3055, "Total travel time (mins per day) - bicycle")
    LOC_14 = (3056, "Total travel time (mins per day) - moped/motorcycle/motorboat")
    LOC_15 = (3057, "Total travel time (mins per day) - car - driver")
    LOC_16 = (3058, "Total travel time (mins per day) - car - passenger")
    LOC_17 = (3059, "Total travel time (mins per day) - car - driver not specified")
    LOC_18 = (3060, "Total travel time (mins per day) - lorry/ tractor")
    LOC_19 = (3061, "Total travel time (mins per day) - van")
    LOC_20 = (3062, "Total travel time (mins per day) - private transport - other specified")
    LOC_21 = (3063, "Total travel time (mins per day) - PUBLIC transport not specified")
    LOC_22 = (3064, "Total travel time (mins per day) - taxi")
    LOC_23 = (3065, "Total travel time (mins per day) - bus")
    LOC_24 = (3066, "Total travel time (mins per day) - tram/ underground")
    LOC_25 = (3067, "Total travel time (mins per day) - train")
    LOC_26 = (3068, "Total travel time (mins per day) - aeroplane")
    LOC_27 = (3069, "Total travel time (mins per day) - boat or ship")
    LOC_28 = (3070, "Total travel time (mins per day) - coach")
    LOC_29 = (3071, "Total travel time (mins per day) - waiting for public transport")
    LOC_30 = (3072, "Total travel time (mins per day) - public transport - other specified")
    LOC_31 = (3073, "Total travel time (mins per day) - TRANSPORT NOT SPECIFIED")
    LOC_32 = (3074, "Total travel or location time  (mins per day) - illegible")
    LOC_NA = (3075, "Main actvty = sleep/work/study - no location code required")
    SUMLOC = (3076, "Total time - sum of all location codes (mins per day)")
    A_ALONE = (3077, "(Adult diary) Total time - ALONE or with people you don't know")
    A_WCH9 = (3078, "(Adult diary) Total time - with children up to 9yrs living in hhld")
    A_WCH14 = (3079, "(Adult diary) Total time - with children 10 - 14yrs living in hhld")
    A_WOTHH = (3080, "(Adult diary) Total time - with other household members (ie other than children up to 14yrs)")
    A_WOTHP = (3081, "(Adult diary) Total time - with other people you know (ie other than hhld members)")
    A_ASLEEP = (3082, "(Adult diary) Total time - asleep, studying or working ('who with' not required)")
    A_NOANS = (3083, "(Adult diary) Total time - NO ANSWER to 'Who were you with?' questions")
    A_TOTWTH = (3084, "(Adult diary) Total time - sum of 'who with' codes (NB can be > 1440 mins)")
    K_ALONE = (3085, "(Child diary) Total time - ALONE or with people you don't know")
    K_WPAR = (3086, "(Child diary) Total time - with your parents")
    K_WOTHH = (3087, "(Child diary) Total time - with other household members (ie other than parents)")
    K_WOTHP = (3088, "(Child diary) Total time - with other people you know (ie other than hhld members)")
    K_ASLEEP = (3089, "(Child diary) Total time - asleep, studying or working ('who with' not required)")
    K_NOANS = (3090, "(Child diary) Total time - NO ANSWER to 'Who were you with?' questions")
    K_TOTWTH = (3091, "(Child diary) Total time - sum of 'who with' codes (NB can be > 1440 mins)")
    DAGE = (3092, "Diary Age")
    DAGEGRP = (3093, "Age group")
    DSEX = (3094, "Diary-sex")
    DETHNIC = (3095, "Diary-ethnicity")
    DDAYW = (3096, "Diary day - Weekday, Saturday or Sunday")
    DDAYW2 = (3097, "Diary day - weekday or weekend")
    HDAY = (3098, "Day of household interview")
    HMONTH = (3099, "Month of household interview")
    HYEAR = (3100, "Year of household interview")
    GORPAF = (3101, "Government Office Region")
    GORPAF2 = (3102, "Govn Office Region - 8 categories")
    GORPAF3 = (3103, "Govn Office Region - 4 countries")
    POP_DEN = (3104, "Population density (persons per 10 hectares - uses 1991 Census data for postcode sector)")
    POP_DEN2 = (3105, "Population density - banded (persons per 10 hectares)")
    UNEMP = (3106, "Unemployment rate (%) - uses 1991 Census data for postcode sector")
    UNEMP2 = (3107, "Unemployment rate - percentage banded")
    HNUMB = (3108, "Number of people in household (all ages)")
    NUMADULT = (3109, "Number of adults   (16 yrs or more) in hhld")
    NUMCHILD = (3110, "Number of children (15 yrs or less) in hhld")
    CHILD = (3111, "Whether child (15yrs or less) in household or not")
    AGEYNGST = (3112, "Age of youngest person in household")
    NUM0_2 = (3113, "Number aged 0 - 2 yrs in hhld")
    NUM3_4 = (3114, "Number aged 3 - 4 yrs in hhld")
    NUM5_9 = (3115, "Number aged 5 - 9 yrs in hhld")
    NUM10_15 = (3116, "Number aged 10 - 15 yrs in hhld")
    NUM16_17 = (3117, "Number aged 16 - 17yrs")
    HRP_PER = (3118, "Household Reference Person - person number")
    SPOUSE1 = (3119, "For hhlds with one marr/cohab couple - person number of FIRST spouse")
    SPOUSE2 = (3120, "For hhlds with one marr/cohab couple - person number of SECOND spouse")
    TENURE2 = (3121, "Tenure - grouped")
    CARAVAIL = (3122, "Whether household owns/ has continuous use of car, motor bike or other motor vehicle")
    GROSHINC = (3123, "Household Income band (gross ie before deductions) - per year (source: hhld qstn 10b)")
    HHTYPE4 = (3124, "Household type - main variable for hhld type (16 categories)")
    HHTYPE5 = (3125, "Household type - 8 categories")
    MANAGE2 = (3126, "Management responsibilities (of economically active & employed)")
    ECONACT = (3127, "Economic activity")
    ECONACT3 = (3128, "Economic activity - 3")
    EMPINCBD = (3129, "Employee - Net MONTHLY income - Banded (sources: Q10 & Q11a)")
    SEINCBD = (3130, "Self-employed - Net MONTHLY income - Banded (sources: Q13c & Q13d)")
    TOTPINC = (3131, "Total net monthly personal income (for employees & self-employed together)")
    HRS_UNPD = (3132, "Total weekly hours UNPAID work in own/ relatives's business (copy of Q14a)")
    HRS_JOB1 = (3133, "Total weekly hours usually worked in MAIN job (incl paid & unpaid overtime) by people in paid work (employed or self-employed)")
    HRS_JOB2 = (3134, "Total weekly hours usually worked in SECOND job (copy of Q16F)")
    HRS_TOT = (3135, "Total hours usually worked per week: unpaid work for own/rel business + main job + second job combined")
    HRS_GRP = (3136, "Total weekly hours usually worked - paid work (main + 2nd job) or unpaid work - banded")
    SIC = (3137, "Standard Industrial Classification 1992 (4-digit) - for respondent's MAIN JOB")
    SOC = (3138, "Standard Occupational Classification 2000 for respondent's MAIN JOB")
    SIC2 = (3139, "Standard Industrial Classification 1992 (4-digit) - for respondent's SECOND JOB")
    SOC2 = (3140, "Standard Occupational Classification 2000 for respondent's SECOND JOB")
    NSSECB = (3141, "National Statistics Socio-Economic Classification")
    NSSECB_8 = (3142, "NS Socio-Economic Classification - 8 classes")
    NSSECB_5 = (3143, "NS Socio-Economic Classification - 5 classes")
    NSSECB_3 = (3144, "NS Socio-Economic Classification - 3 classes")
    HIQUAL4 = (3145, "Highest qualification gained - HARMONISED DEFINITION")
    AGELEFT = (3146, " Age left full-time education - grouped")
    LIVARR = (3147, "Living arrangements (as reported by respondent at q55 & q56 - NOT based on relationships in hhld grid )")
    PROVCARE = (3148, "Q45 & Q47: Do you look after any sick/ disabled/ elderly person (either living with you or not living with you)?")
    MGROUP = (3149, "(H) GB MOSAIC Group (area classification) - household level")
    MTYPE = (3150, "(H) GB MOSAIC Type - household level")
    MGRPPC = (3151, "(PC) GB MOSAIC Group - post code level")
    MTYPEPC = (3152, "(PC) GB MOSAIC Type - post code level")
    ISBA = (3153, "ISBA - Code")
    CINEMA = (3154, "distance to nearest cinema")
    THEATRE = (3155, "distance to nearest theatre")
    SPORT = (3156, "distance to nearest sports centre")
    SHOPPING = (3157, "distance to nearest shopping centre")
    GROCERY = (3158, "distance to nearest grocery shop")
    SCHOOL = (3159, "distance to nearest school")
    TOT_EPIS = (3160, "Total number of episodes (excluding 'not spec' activities 996 & 997)")
    MISSTIME = (3161, "Missing main activity (codes 996 & 997) - minutes per day")
    DRY_IND = (3162, "Suitability of diaries for analysis - indicator field")
    WTDRY_GR = (3163, "Diary weight - for grossing to UK population aged 8yrs or more")
    WTDRY_UG = (3164, "Diary weight - ungrossed")


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


class ACT1_001(OrderedEnum):
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


class ACT2_001(OrderedEnum):
    MAIN_ACTVTY_SLEEPWORKSTUDY___NO_SCNDRY_ACTVTY_REQUIRED = '-9'
    CHILD_DIARY___NO_SECONDARY_ACTVTY_REQUIRED = '-2'
    ADULT_DIARY___NO_SECONDARY_ACTVTY_RECORDED = '-1'
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


class WHER_001(OrderedEnum):
    MAIN_ACTVTY_EQUAL_SLEEPWORKSTUDY___NO_CODE_REQUIRED = '-9'
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


class WIT0_001(OrderedEnum):
    NOT_ALONE_NOT_WITH_PEOPLE_YOU_DON_T_KNOW = '0'
    ALONE_OR_WITH_PEOPLE_YOU_DON_T_KNOW = '1'
    MISSING1 = '-1'


class WIT1_001(OrderedEnum):
    NOT_WITH_CHILDREN_UP_TO_9_LIVING_IN_YOUR_HOUSEHOLD = '0'
    WITH_CHILDREN_UP_TO_9_LIVING_IN_YOUR_HOUSEHOLD = '1'
    MISSING1 = '-1'


class WIT2_001(OrderedEnum):
    NOT_WITH_CHILDREN_AGED_10_TO_14_LIVING_IN_YOUR_HOUSEHOLD = '0'
    WITH_CHILDREN_AGED_10_TO_14_LIVING_IN_YOUR_HOUSEHOLD = '1'
    MISSING1 = '-1'


class WIT3_001(OrderedEnum):
    NOT_WITH_OTHER_HOUSEHOLD_MEMBERS = '0'
    WITH_OTHER_HOUSEHOLD_MEMBERS = '1'
    MISSING1 = '-1'


class WIT4_001(OrderedEnum):
    NOT_WITH_OTHER_PEOPLE_THAT_YOU_KNOW = '0'
    WITH_OTHER_PEOPLE_THAT_YOU_KNOW = '1'
    MISSING1 = '-1'


class WIT5_001(OrderedEnum):
    MAIN_ACTIVITY_IS_NOT_SLEEP__EMPLOYMENT_OR_STUDY = '0'
    MAIN_ACTIVITY_IS_ASLEEP__EMPLOYMENT_OR_STUDY = '1'
    MISSING1 = '-1'


class WIT6_001(OrderedEnum):
    __WERE_YOU_WITH_ANYBODY__QUESTION_ANSWERED = '0'
    NO_ANSWERS_TO__WERE_YOU_WITH_ANYBODY__QUESTION = '1'
    MISSING1 = '-1'


ACT1_002 = ACT1_001


ACT2_002 = ACT2_001


WHER_002 = WHER_001


WIT0_002 = WIT0_001


WIT1_002 = WIT1_001


WIT2_002 = WIT2_001


WIT3_002 = WIT3_001


WIT4_002 = WIT4_001


WIT5_002 = WIT5_001


WIT6_002 = WIT6_001


ACT1_003 = ACT1_001


ACT2_003 = ACT2_001


WHER_003 = WHER_001


WIT0_003 = WIT0_001


WIT1_003 = WIT1_001


WIT2_003 = WIT2_001


WIT3_003 = WIT3_001


WIT4_003 = WIT4_001


WIT5_003 = WIT5_001


WIT6_003 = WIT6_001


ACT1_004 = ACT1_001


ACT2_004 = ACT2_001


WHER_004 = WHER_001


WIT0_004 = WIT0_001


WIT1_004 = WIT1_001


WIT2_004 = WIT2_001


WIT3_004 = WIT3_001


WIT4_004 = WIT4_001


WIT5_004 = WIT5_001


WIT6_004 = WIT6_001


ACT1_005 = ACT1_001


ACT2_005 = ACT2_001


WHER_005 = WHER_001


WIT0_005 = WIT0_001


WIT1_005 = WIT1_001


WIT2_005 = WIT2_001


WIT3_005 = WIT3_001


WIT4_005 = WIT4_001


WIT5_005 = WIT5_001


WIT6_005 = WIT6_001


ACT1_006 = ACT1_001


ACT2_006 = ACT2_001


WHER_006 = WHER_001


WIT0_006 = WIT0_001


WIT1_006 = WIT1_001


WIT2_006 = WIT2_001


WIT3_006 = WIT3_001


WIT4_006 = WIT4_001


WIT5_006 = WIT5_001


WIT6_006 = WIT6_001


ACT1_007 = ACT1_001


ACT2_007 = ACT2_001


WHER_007 = WHER_001


WIT0_007 = WIT0_001


WIT1_007 = WIT1_001


WIT2_007 = WIT2_001


WIT3_007 = WIT3_001


WIT4_007 = WIT4_001


WIT5_007 = WIT5_001


WIT6_007 = WIT6_001


ACT1_008 = ACT1_001


ACT2_008 = ACT2_001


WHER_008 = WHER_001


WIT0_008 = WIT0_001


WIT1_008 = WIT1_001


WIT2_008 = WIT2_001


WIT3_008 = WIT3_001


WIT4_008 = WIT4_001


WIT5_008 = WIT5_001


WIT6_008 = WIT6_001


ACT1_009 = ACT1_001


ACT2_009 = ACT2_001


WHER_009 = WHER_001


WIT0_009 = WIT0_001


WIT1_009 = WIT1_001


WIT2_009 = WIT2_001


WIT3_009 = WIT3_001


WIT4_009 = WIT4_001


WIT5_009 = WIT5_001


WIT6_009 = WIT6_001


ACT1_010 = ACT1_001


ACT2_010 = ACT2_001


WHER_010 = WHER_001


WIT0_010 = WIT0_001


WIT1_010 = WIT1_001


WIT2_010 = WIT2_001


WIT3_010 = WIT3_001


WIT4_010 = WIT4_001


WIT5_010 = WIT5_001


WIT6_010 = WIT6_001


ACT1_011 = ACT1_001


ACT2_011 = ACT2_001


WHER_011 = WHER_001


WIT0_011 = WIT0_001


WIT1_011 = WIT1_001


WIT2_011 = WIT2_001


WIT3_011 = WIT3_001


WIT4_011 = WIT4_001


WIT5_011 = WIT5_001


WIT6_011 = WIT6_001


ACT1_012 = ACT1_001


ACT2_012 = ACT2_001


WHER_012 = WHER_001


WIT0_012 = WIT0_001


WIT1_012 = WIT1_001


WIT2_012 = WIT2_001


WIT3_012 = WIT3_001


WIT4_012 = WIT4_001


WIT5_012 = WIT5_001


WIT6_012 = WIT6_001


ACT1_013 = ACT1_001


ACT2_013 = ACT2_001


WHER_013 = WHER_001


WIT0_013 = WIT0_001


WIT1_013 = WIT1_001


WIT2_013 = WIT2_001


WIT3_013 = WIT3_001


WIT4_013 = WIT4_001


WIT5_013 = WIT5_001


WIT6_013 = WIT6_001


ACT1_014 = ACT1_001


ACT2_014 = ACT2_001


WHER_014 = WHER_001


WIT0_014 = WIT0_001


WIT1_014 = WIT1_001


WIT2_014 = WIT2_001


WIT3_014 = WIT3_001


WIT4_014 = WIT4_001


WIT5_014 = WIT5_001


WIT6_014 = WIT6_001


ACT1_015 = ACT1_001


ACT2_015 = ACT2_001


WHER_015 = WHER_001


WIT0_015 = WIT0_001


WIT1_015 = WIT1_001


WIT2_015 = WIT2_001


WIT3_015 = WIT3_001


WIT4_015 = WIT4_001


WIT5_015 = WIT5_001


WIT6_015 = WIT6_001


ACT1_016 = ACT1_001


ACT2_016 = ACT2_001


WHER_016 = WHER_001


WIT0_016 = WIT0_001


WIT1_016 = WIT1_001


WIT2_016 = WIT2_001


WIT3_016 = WIT3_001


WIT4_016 = WIT4_001


WIT5_016 = WIT5_001


WIT6_016 = WIT6_001


ACT1_017 = ACT1_001


ACT2_017 = ACT2_001


WHER_017 = WHER_001


WIT0_017 = WIT0_001


WIT1_017 = WIT1_001


WIT2_017 = WIT2_001


WIT3_017 = WIT3_001


WIT4_017 = WIT4_001


WIT5_017 = WIT5_001


WIT6_017 = WIT6_001


ACT1_018 = ACT1_001


ACT2_018 = ACT2_001


WHER_018 = WHER_001


WIT0_018 = WIT0_001


WIT1_018 = WIT1_001


WIT2_018 = WIT2_001


WIT3_018 = WIT3_001


WIT4_018 = WIT4_001


WIT5_018 = WIT5_001


WIT6_018 = WIT6_001


ACT1_019 = ACT1_001


ACT2_019 = ACT2_001


WHER_019 = WHER_001


WIT0_019 = WIT0_001


WIT1_019 = WIT1_001


WIT2_019 = WIT2_001


WIT3_019 = WIT3_001


WIT4_019 = WIT4_001


WIT5_019 = WIT5_001


WIT6_019 = WIT6_001


ACT1_020 = ACT1_001


ACT2_020 = ACT2_001


WHER_020 = WHER_001


WIT0_020 = WIT0_001


WIT1_020 = WIT1_001


WIT2_020 = WIT2_001


WIT3_020 = WIT3_001


WIT4_020 = WIT4_001


WIT5_020 = WIT5_001


WIT6_020 = WIT6_001


ACT1_021 = ACT1_001


ACT2_021 = ACT2_001


WHER_021 = WHER_001


WIT0_021 = WIT0_001


WIT1_021 = WIT1_001


WIT2_021 = WIT2_001


WIT3_021 = WIT3_001


WIT4_021 = WIT4_001


WIT5_021 = WIT5_001


WIT6_021 = WIT6_001


ACT1_022 = ACT1_001


ACT2_022 = ACT2_001


WHER_022 = WHER_001


WIT0_022 = WIT0_001


WIT1_022 = WIT1_001


WIT2_022 = WIT2_001


WIT3_022 = WIT3_001


WIT4_022 = WIT4_001


WIT5_022 = WIT5_001


WIT6_022 = WIT6_001


ACT1_023 = ACT1_001


ACT2_023 = ACT2_001


WHER_023 = WHER_001


WIT0_023 = WIT0_001


WIT1_023 = WIT1_001


WIT2_023 = WIT2_001


WIT3_023 = WIT3_001


WIT4_023 = WIT4_001


WIT5_023 = WIT5_001


WIT6_023 = WIT6_001


ACT1_024 = ACT1_001


ACT2_024 = ACT2_001


WHER_024 = WHER_001


WIT0_024 = WIT0_001


WIT1_024 = WIT1_001


WIT2_024 = WIT2_001


WIT3_024 = WIT3_001


WIT4_024 = WIT4_001


WIT5_024 = WIT5_001


WIT6_024 = WIT6_001


ACT1_025 = ACT1_001


ACT2_025 = ACT2_001


WHER_025 = WHER_001


WIT0_025 = WIT0_001


WIT1_025 = WIT1_001


WIT2_025 = WIT2_001


WIT3_025 = WIT3_001


WIT4_025 = WIT4_001


WIT5_025 = WIT5_001


WIT6_025 = WIT6_001


ACT1_026 = ACT1_001


ACT2_026 = ACT2_001


WHER_026 = WHER_001


WIT0_026 = WIT0_001


WIT1_026 = WIT1_001


WIT2_026 = WIT2_001


WIT3_026 = WIT3_001


WIT4_026 = WIT4_001


WIT5_026 = WIT5_001


WIT6_026 = WIT6_001


ACT1_027 = ACT1_001


ACT2_027 = ACT2_001


WHER_027 = WHER_001


WIT0_027 = WIT0_001


WIT1_027 = WIT1_001


WIT2_027 = WIT2_001


WIT3_027 = WIT3_001


WIT4_027 = WIT4_001


WIT5_027 = WIT5_001


WIT6_027 = WIT6_001


ACT1_028 = ACT1_001


ACT2_028 = ACT2_001


WHER_028 = WHER_001


WIT0_028 = WIT0_001


WIT1_028 = WIT1_001


WIT2_028 = WIT2_001


WIT3_028 = WIT3_001


WIT4_028 = WIT4_001


WIT5_028 = WIT5_001


WIT6_028 = WIT6_001


ACT1_029 = ACT1_001


ACT2_029 = ACT2_001


WHER_029 = WHER_001


WIT0_029 = WIT0_001


WIT1_029 = WIT1_001


WIT2_029 = WIT2_001


WIT3_029 = WIT3_001


WIT4_029 = WIT4_001


WIT5_029 = WIT5_001


WIT6_029 = WIT6_001


ACT1_030 = ACT1_001


ACT2_030 = ACT2_001


WHER_030 = WHER_001


WIT0_030 = WIT0_001


WIT1_030 = WIT1_001


WIT2_030 = WIT2_001


WIT3_030 = WIT3_001


WIT4_030 = WIT4_001


WIT5_030 = WIT5_001


WIT6_030 = WIT6_001


ACT1_031 = ACT1_001


ACT2_031 = ACT2_001


WHER_031 = WHER_001


WIT0_031 = WIT0_001


WIT1_031 = WIT1_001


WIT2_031 = WIT2_001


WIT3_031 = WIT3_001


WIT4_031 = WIT4_001


WIT5_031 = WIT5_001


WIT6_031 = WIT6_001


ACT1_032 = ACT1_001


ACT2_032 = ACT2_001


WHER_032 = WHER_001


WIT0_032 = WIT0_001


WIT1_032 = WIT1_001


WIT2_032 = WIT2_001


WIT3_032 = WIT3_001


WIT4_032 = WIT4_001


WIT5_032 = WIT5_001


WIT6_032 = WIT6_001


ACT1_033 = ACT1_001


ACT2_033 = ACT2_001


WHER_033 = WHER_001


WIT0_033 = WIT0_001


WIT1_033 = WIT1_001


WIT2_033 = WIT2_001


WIT3_033 = WIT3_001


WIT4_033 = WIT4_001


WIT5_033 = WIT5_001


WIT6_033 = WIT6_001


ACT1_034 = ACT1_001


ACT2_034 = ACT2_001


WHER_034 = WHER_001


WIT0_034 = WIT0_001


WIT1_034 = WIT1_001


WIT2_034 = WIT2_001


WIT3_034 = WIT3_001


WIT4_034 = WIT4_001


WIT5_034 = WIT5_001


WIT6_034 = WIT6_001


ACT1_035 = ACT1_001


ACT2_035 = ACT2_001


WHER_035 = WHER_001


WIT0_035 = WIT0_001


WIT1_035 = WIT1_001


WIT2_035 = WIT2_001


WIT3_035 = WIT3_001


WIT4_035 = WIT4_001


WIT5_035 = WIT5_001


WIT6_035 = WIT6_001


ACT1_036 = ACT1_001


ACT2_036 = ACT2_001


WHER_036 = WHER_001


WIT0_036 = WIT0_001


WIT1_036 = WIT1_001


WIT2_036 = WIT2_001


WIT3_036 = WIT3_001


WIT4_036 = WIT4_001


WIT5_036 = WIT5_001


WIT6_036 = WIT6_001


ACT1_037 = ACT1_001


ACT2_037 = ACT2_001


WHER_037 = WHER_001


WIT0_037 = WIT0_001


WIT1_037 = WIT1_001


WIT2_037 = WIT2_001


WIT3_037 = WIT3_001


WIT4_037 = WIT4_001


WIT5_037 = WIT5_001


WIT6_037 = WIT6_001


ACT1_038 = ACT1_001


ACT2_038 = ACT2_001


WHER_038 = WHER_001


WIT0_038 = WIT0_001


WIT1_038 = WIT1_001


WIT2_038 = WIT2_001


WIT3_038 = WIT3_001


WIT4_038 = WIT4_001


WIT5_038 = WIT5_001


WIT6_038 = WIT6_001


ACT1_039 = ACT1_001


ACT2_039 = ACT2_001


WHER_039 = WHER_001


WIT0_039 = WIT0_001


WIT1_039 = WIT1_001


WIT2_039 = WIT2_001


WIT3_039 = WIT3_001


WIT4_039 = WIT4_001


WIT5_039 = WIT5_001


WIT6_039 = WIT6_001


ACT1_040 = ACT1_001


ACT2_040 = ACT2_001


WHER_040 = WHER_001


WIT0_040 = WIT0_001


WIT1_040 = WIT1_001


WIT2_040 = WIT2_001


WIT3_040 = WIT3_001


WIT4_040 = WIT4_001


WIT5_040 = WIT5_001


WIT6_040 = WIT6_001


ACT1_041 = ACT1_001


ACT2_041 = ACT2_001


WHER_041 = WHER_001


WIT0_041 = WIT0_001


WIT1_041 = WIT1_001


WIT2_041 = WIT2_001


WIT3_041 = WIT3_001


WIT4_041 = WIT4_001


WIT5_041 = WIT5_001


WIT6_041 = WIT6_001


ACT1_042 = ACT1_001


ACT2_042 = ACT2_001


WHER_042 = WHER_001


WIT0_042 = WIT0_001


WIT1_042 = WIT1_001


WIT2_042 = WIT2_001


WIT3_042 = WIT3_001


WIT4_042 = WIT4_001


WIT5_042 = WIT5_001


WIT6_042 = WIT6_001


ACT1_043 = ACT1_001


ACT2_043 = ACT2_001


WHER_043 = WHER_001


WIT0_043 = WIT0_001


WIT1_043 = WIT1_001


WIT2_043 = WIT2_001


WIT3_043 = WIT3_001


WIT4_043 = WIT4_001


WIT5_043 = WIT5_001


WIT6_043 = WIT6_001


ACT1_044 = ACT1_001


ACT2_044 = ACT2_001


WHER_044 = WHER_001


WIT0_044 = WIT0_001


WIT1_044 = WIT1_001


WIT2_044 = WIT2_001


WIT3_044 = WIT3_001


WIT4_044 = WIT4_001


WIT5_044 = WIT5_001


WIT6_044 = WIT6_001


ACT1_045 = ACT1_001


ACT2_045 = ACT2_001


WHER_045 = WHER_001


WIT0_045 = WIT0_001


WIT1_045 = WIT1_001


WIT2_045 = WIT2_001


WIT3_045 = WIT3_001


WIT4_045 = WIT4_001


WIT5_045 = WIT5_001


WIT6_045 = WIT6_001


ACT1_046 = ACT1_001


ACT2_046 = ACT2_001


WHER_046 = WHER_001


WIT0_046 = WIT0_001


WIT1_046 = WIT1_001


WIT2_046 = WIT2_001


WIT3_046 = WIT3_001


WIT4_046 = WIT4_001


WIT5_046 = WIT5_001


WIT6_046 = WIT6_001


ACT1_047 = ACT1_001


ACT2_047 = ACT2_001


WHER_047 = WHER_001


WIT0_047 = WIT0_001


WIT1_047 = WIT1_001


WIT2_047 = WIT2_001


WIT3_047 = WIT3_001


WIT4_047 = WIT4_001


WIT5_047 = WIT5_001


WIT6_047 = WIT6_001


ACT1_048 = ACT1_001


ACT2_048 = ACT2_001


WHER_048 = WHER_001


WIT0_048 = WIT0_001


WIT1_048 = WIT1_001


WIT2_048 = WIT2_001


WIT3_048 = WIT3_001


WIT4_048 = WIT4_001


WIT5_048 = WIT5_001


WIT6_048 = WIT6_001


ACT1_049 = ACT1_001


ACT2_049 = ACT2_001


WHER_049 = WHER_001


WIT0_049 = WIT0_001


WIT1_049 = WIT1_001


WIT2_049 = WIT2_001


WIT3_049 = WIT3_001


WIT4_049 = WIT4_001


WIT5_049 = WIT5_001


WIT6_049 = WIT6_001


ACT1_050 = ACT1_001


ACT2_050 = ACT2_001


WHER_050 = WHER_001


WIT0_050 = WIT0_001


WIT1_050 = WIT1_001


WIT2_050 = WIT2_001


WIT3_050 = WIT3_001


WIT4_050 = WIT4_001


WIT5_050 = WIT5_001


WIT6_050 = WIT6_001


ACT1_051 = ACT1_001


ACT2_051 = ACT2_001


WHER_051 = WHER_001


WIT0_051 = WIT0_001


WIT1_051 = WIT1_001


WIT2_051 = WIT2_001


WIT3_051 = WIT3_001


WIT4_051 = WIT4_001


WIT5_051 = WIT5_001


WIT6_051 = WIT6_001


ACT1_052 = ACT1_001


ACT2_052 = ACT2_001


WHER_052 = WHER_001


WIT0_052 = WIT0_001


WIT1_052 = WIT1_001


WIT2_052 = WIT2_001


WIT3_052 = WIT3_001


WIT4_052 = WIT4_001


WIT5_052 = WIT5_001


WIT6_052 = WIT6_001


ACT1_053 = ACT1_001


ACT2_053 = ACT2_001


WHER_053 = WHER_001


WIT0_053 = WIT0_001


WIT1_053 = WIT1_001


WIT2_053 = WIT2_001


WIT3_053 = WIT3_001


WIT4_053 = WIT4_001


WIT5_053 = WIT5_001


WIT6_053 = WIT6_001


ACT1_054 = ACT1_001


ACT2_054 = ACT2_001


WHER_054 = WHER_001


WIT0_054 = WIT0_001


WIT1_054 = WIT1_001


WIT2_054 = WIT2_001


WIT3_054 = WIT3_001


WIT4_054 = WIT4_001


WIT5_054 = WIT5_001


WIT6_054 = WIT6_001


ACT1_055 = ACT1_001


ACT2_055 = ACT2_001


WHER_055 = WHER_001


WIT0_055 = WIT0_001


WIT1_055 = WIT1_001


WIT2_055 = WIT2_001


WIT3_055 = WIT3_001


WIT4_055 = WIT4_001


WIT5_055 = WIT5_001


WIT6_055 = WIT6_001


ACT1_056 = ACT1_001


ACT2_056 = ACT2_001


WHER_056 = WHER_001


WIT0_056 = WIT0_001


WIT1_056 = WIT1_001


WIT2_056 = WIT2_001


WIT3_056 = WIT3_001


WIT4_056 = WIT4_001


WIT5_056 = WIT5_001


WIT6_056 = WIT6_001


ACT1_057 = ACT1_001


ACT2_057 = ACT2_001


WHER_057 = WHER_001


WIT0_057 = WIT0_001


WIT1_057 = WIT1_001


WIT2_057 = WIT2_001


WIT3_057 = WIT3_001


WIT4_057 = WIT4_001


WIT5_057 = WIT5_001


WIT6_057 = WIT6_001


ACT1_058 = ACT1_001


ACT2_058 = ACT2_001


WHER_058 = WHER_001


WIT0_058 = WIT0_001


WIT1_058 = WIT1_001


WIT2_058 = WIT2_001


WIT3_058 = WIT3_001


WIT4_058 = WIT4_001


WIT5_058 = WIT5_001


WIT6_058 = WIT6_001


ACT1_059 = ACT1_001


ACT2_059 = ACT2_001


WHER_059 = WHER_001


WIT0_059 = WIT0_001


WIT1_059 = WIT1_001


WIT2_059 = WIT2_001


WIT3_059 = WIT3_001


WIT4_059 = WIT4_001


WIT5_059 = WIT5_001


WIT6_059 = WIT6_001


ACT1_060 = ACT1_001


ACT2_060 = ACT2_001


WHER_060 = WHER_001


WIT0_060 = WIT0_001


WIT1_060 = WIT1_001


WIT2_060 = WIT2_001


WIT3_060 = WIT3_001


WIT4_060 = WIT4_001


WIT5_060 = WIT5_001


WIT6_060 = WIT6_001


ACT1_061 = ACT1_001


ACT2_061 = ACT2_001


WHER_061 = WHER_001


WIT0_061 = WIT0_001


WIT1_061 = WIT1_001


WIT2_061 = WIT2_001


WIT3_061 = WIT3_001


WIT4_061 = WIT4_001


WIT5_061 = WIT5_001


WIT6_061 = WIT6_001


ACT1_062 = ACT1_001


ACT2_062 = ACT2_001


WHER_062 = WHER_001


WIT0_062 = WIT0_001


WIT1_062 = WIT1_001


WIT2_062 = WIT2_001


WIT3_062 = WIT3_001


WIT4_062 = WIT4_001


WIT5_062 = WIT5_001


WIT6_062 = WIT6_001


ACT1_063 = ACT1_001


ACT2_063 = ACT2_001


WHER_063 = WHER_001


WIT0_063 = WIT0_001


WIT1_063 = WIT1_001


WIT2_063 = WIT2_001


WIT3_063 = WIT3_001


WIT4_063 = WIT4_001


WIT5_063 = WIT5_001


WIT6_063 = WIT6_001


ACT1_064 = ACT1_001


ACT2_064 = ACT2_001


WHER_064 = WHER_001


WIT0_064 = WIT0_001


WIT1_064 = WIT1_001


WIT2_064 = WIT2_001


WIT3_064 = WIT3_001


WIT4_064 = WIT4_001


WIT5_064 = WIT5_001


WIT6_064 = WIT6_001


ACT1_065 = ACT1_001


ACT2_065 = ACT2_001


WHER_065 = WHER_001


WIT0_065 = WIT0_001


WIT1_065 = WIT1_001


WIT2_065 = WIT2_001


WIT3_065 = WIT3_001


WIT4_065 = WIT4_001


WIT5_065 = WIT5_001


WIT6_065 = WIT6_001


ACT1_066 = ACT1_001


ACT2_066 = ACT2_001


WHER_066 = WHER_001


WIT0_066 = WIT0_001


WIT1_066 = WIT1_001


WIT2_066 = WIT2_001


WIT3_066 = WIT3_001


WIT4_066 = WIT4_001


WIT5_066 = WIT5_001


WIT6_066 = WIT6_001


ACT1_067 = ACT1_001


ACT2_067 = ACT2_001


WHER_067 = WHER_001


WIT0_067 = WIT0_001


WIT1_067 = WIT1_001


WIT2_067 = WIT2_001


WIT3_067 = WIT3_001


WIT4_067 = WIT4_001


WIT5_067 = WIT5_001


WIT6_067 = WIT6_001


ACT1_068 = ACT1_001


ACT2_068 = ACT2_001


WHER_068 = WHER_001


WIT0_068 = WIT0_001


WIT1_068 = WIT1_001


WIT2_068 = WIT2_001


WIT3_068 = WIT3_001


WIT4_068 = WIT4_001


WIT5_068 = WIT5_001


WIT6_068 = WIT6_001


ACT1_069 = ACT1_001


ACT2_069 = ACT2_001


WHER_069 = WHER_001


WIT0_069 = WIT0_001


WIT1_069 = WIT1_001


WIT2_069 = WIT2_001


WIT3_069 = WIT3_001


WIT4_069 = WIT4_001


WIT5_069 = WIT5_001


WIT6_069 = WIT6_001


ACT1_070 = ACT1_001


ACT2_070 = ACT2_001


WHER_070 = WHER_001


WIT0_070 = WIT0_001


WIT1_070 = WIT1_001


WIT2_070 = WIT2_001


WIT3_070 = WIT3_001


WIT4_070 = WIT4_001


WIT5_070 = WIT5_001


WIT6_070 = WIT6_001


ACT1_071 = ACT1_001


ACT2_071 = ACT2_001


WHER_071 = WHER_001


WIT0_071 = WIT0_001


WIT1_071 = WIT1_001


WIT2_071 = WIT2_001


WIT3_071 = WIT3_001


WIT4_071 = WIT4_001


WIT5_071 = WIT5_001


WIT6_071 = WIT6_001


ACT1_072 = ACT1_001


ACT2_072 = ACT2_001


WHER_072 = WHER_001


WIT0_072 = WIT0_001


WIT1_072 = WIT1_001


WIT2_072 = WIT2_001


WIT3_072 = WIT3_001


WIT4_072 = WIT4_001


WIT5_072 = WIT5_001


WIT6_072 = WIT6_001


ACT1_073 = ACT1_001


ACT2_073 = ACT2_001


WHER_073 = WHER_001


WIT0_073 = WIT0_001


WIT1_073 = WIT1_001


WIT2_073 = WIT2_001


WIT3_073 = WIT3_001


WIT4_073 = WIT4_001


WIT5_073 = WIT5_001


WIT6_073 = WIT6_001


ACT1_074 = ACT1_001


ACT2_074 = ACT2_001


WHER_074 = WHER_001


WIT0_074 = WIT0_001


WIT1_074 = WIT1_001


WIT2_074 = WIT2_001


WIT3_074 = WIT3_001


WIT4_074 = WIT4_001


WIT5_074 = WIT5_001


WIT6_074 = WIT6_001


ACT1_075 = ACT1_001


ACT2_075 = ACT2_001


WHER_075 = WHER_001


WIT0_075 = WIT0_001


WIT1_075 = WIT1_001


WIT2_075 = WIT2_001


WIT3_075 = WIT3_001


WIT4_075 = WIT4_001


WIT5_075 = WIT5_001


WIT6_075 = WIT6_001


ACT1_076 = ACT1_001


ACT2_076 = ACT2_001


WHER_076 = WHER_001


WIT0_076 = WIT0_001


WIT1_076 = WIT1_001


WIT2_076 = WIT2_001


WIT3_076 = WIT3_001


WIT4_076 = WIT4_001


WIT5_076 = WIT5_001


WIT6_076 = WIT6_001


ACT1_077 = ACT1_001


ACT2_077 = ACT2_001


WHER_077 = WHER_001


WIT0_077 = WIT0_001


WIT1_077 = WIT1_001


WIT2_077 = WIT2_001


WIT3_077 = WIT3_001


WIT4_077 = WIT4_001


WIT5_077 = WIT5_001


WIT6_077 = WIT6_001


ACT1_078 = ACT1_001


ACT2_078 = ACT2_001


WHER_078 = WHER_001


WIT0_078 = WIT0_001


WIT1_078 = WIT1_001


WIT2_078 = WIT2_001


WIT3_078 = WIT3_001


WIT4_078 = WIT4_001


WIT5_078 = WIT5_001


WIT6_078 = WIT6_001


ACT1_079 = ACT1_001


ACT2_079 = ACT2_001


WHER_079 = WHER_001


WIT0_079 = WIT0_001


WIT1_079 = WIT1_001


WIT2_079 = WIT2_001


WIT3_079 = WIT3_001


WIT4_079 = WIT4_001


WIT5_079 = WIT5_001


WIT6_079 = WIT6_001


ACT1_080 = ACT1_001


ACT2_080 = ACT2_001


WHER_080 = WHER_001


WIT0_080 = WIT0_001


WIT1_080 = WIT1_001


WIT2_080 = WIT2_001


WIT3_080 = WIT3_001


WIT4_080 = WIT4_001


WIT5_080 = WIT5_001


WIT6_080 = WIT6_001


ACT1_081 = ACT1_001


ACT2_081 = ACT2_001


WHER_081 = WHER_001


WIT0_081 = WIT0_001


WIT1_081 = WIT1_001


WIT2_081 = WIT2_001


WIT3_081 = WIT3_001


WIT4_081 = WIT4_001


WIT5_081 = WIT5_001


WIT6_081 = WIT6_001


ACT1_082 = ACT1_001


ACT2_082 = ACT2_001


WHER_082 = WHER_001


WIT0_082 = WIT0_001


WIT1_082 = WIT1_001


WIT2_082 = WIT2_001


WIT3_082 = WIT3_001


WIT4_082 = WIT4_001


WIT5_082 = WIT5_001


WIT6_082 = WIT6_001


ACT1_083 = ACT1_001


ACT2_083 = ACT2_001


WHER_083 = WHER_001


WIT0_083 = WIT0_001


WIT1_083 = WIT1_001


WIT2_083 = WIT2_001


WIT3_083 = WIT3_001


WIT4_083 = WIT4_001


WIT5_083 = WIT5_001


WIT6_083 = WIT6_001


ACT1_084 = ACT1_001


ACT2_084 = ACT2_001


WHER_084 = WHER_001


WIT0_084 = WIT0_001


WIT1_084 = WIT1_001


WIT2_084 = WIT2_001


WIT3_084 = WIT3_001


WIT4_084 = WIT4_001


WIT5_084 = WIT5_001


WIT6_084 = WIT6_001


ACT1_085 = ACT1_001


ACT2_085 = ACT2_001


WHER_085 = WHER_001


WIT0_085 = WIT0_001


WIT1_085 = WIT1_001


WIT2_085 = WIT2_001


WIT3_085 = WIT3_001


WIT4_085 = WIT4_001


WIT5_085 = WIT5_001


WIT6_085 = WIT6_001


ACT1_086 = ACT1_001


ACT2_086 = ACT2_001


WHER_086 = WHER_001


WIT0_086 = WIT0_001


WIT1_086 = WIT1_001


WIT2_086 = WIT2_001


WIT3_086 = WIT3_001


WIT4_086 = WIT4_001


WIT5_086 = WIT5_001


WIT6_086 = WIT6_001


ACT1_087 = ACT1_001


ACT2_087 = ACT2_001


WHER_087 = WHER_001


WIT0_087 = WIT0_001


WIT1_087 = WIT1_001


WIT2_087 = WIT2_001


WIT3_087 = WIT3_001


WIT4_087 = WIT4_001


WIT5_087 = WIT5_001


WIT6_087 = WIT6_001


ACT1_088 = ACT1_001


ACT2_088 = ACT2_001


WHER_088 = WHER_001


WIT0_088 = WIT0_001


WIT1_088 = WIT1_001


WIT2_088 = WIT2_001


WIT3_088 = WIT3_001


WIT4_088 = WIT4_001


WIT5_088 = WIT5_001


WIT6_088 = WIT6_001


ACT1_089 = ACT1_001


ACT2_089 = ACT2_001


WHER_089 = WHER_001


WIT0_089 = WIT0_001


WIT1_089 = WIT1_001


WIT2_089 = WIT2_001


WIT3_089 = WIT3_001


WIT4_089 = WIT4_001


WIT5_089 = WIT5_001


WIT6_089 = WIT6_001


ACT1_090 = ACT1_001


ACT2_090 = ACT2_001


WHER_090 = WHER_001


WIT0_090 = WIT0_001


WIT1_090 = WIT1_001


WIT2_090 = WIT2_001


WIT3_090 = WIT3_001


WIT4_090 = WIT4_001


WIT5_090 = WIT5_001


WIT6_090 = WIT6_001


ACT1_091 = ACT1_001


ACT2_091 = ACT2_001


WHER_091 = WHER_001


WIT0_091 = WIT0_001


WIT1_091 = WIT1_001


WIT2_091 = WIT2_001


WIT3_091 = WIT3_001


WIT4_091 = WIT4_001


WIT5_091 = WIT5_001


WIT6_091 = WIT6_001


ACT1_092 = ACT1_001


ACT2_092 = ACT2_001


WHER_092 = WHER_001


WIT0_092 = WIT0_001


WIT1_092 = WIT1_001


WIT2_092 = WIT2_001


WIT3_092 = WIT3_001


WIT4_092 = WIT4_001


WIT5_092 = WIT5_001


WIT6_092 = WIT6_001


ACT1_093 = ACT1_001


ACT2_093 = ACT2_001


WHER_093 = WHER_001


WIT0_093 = WIT0_001


WIT1_093 = WIT1_001


WIT2_093 = WIT2_001


WIT3_093 = WIT3_001


WIT4_093 = WIT4_001


WIT5_093 = WIT5_001


WIT6_093 = WIT6_001


ACT1_094 = ACT1_001


ACT2_094 = ACT2_001


WHER_094 = WHER_001


WIT0_094 = WIT0_001


WIT1_094 = WIT1_001


WIT2_094 = WIT2_001


WIT3_094 = WIT3_001


WIT4_094 = WIT4_001


WIT5_094 = WIT5_001


WIT6_094 = WIT6_001


ACT1_095 = ACT1_001


ACT2_095 = ACT2_001


WHER_095 = WHER_001


WIT0_095 = WIT0_001


WIT1_095 = WIT1_001


WIT2_095 = WIT2_001


WIT3_095 = WIT3_001


WIT4_095 = WIT4_001


WIT5_095 = WIT5_001


WIT6_095 = WIT6_001


ACT1_096 = ACT1_001


ACT2_096 = ACT2_001


WHER_096 = WHER_001


WIT0_096 = WIT0_001


WIT1_096 = WIT1_001


WIT2_096 = WIT2_001


WIT3_096 = WIT3_001


WIT4_096 = WIT4_001


WIT5_096 = WIT5_001


WIT6_096 = WIT6_001


ACT1_097 = ACT1_001


ACT2_097 = ACT2_001


WHER_097 = WHER_001


WIT0_097 = WIT0_001


WIT1_097 = WIT1_001


WIT2_097 = WIT2_001


WIT3_097 = WIT3_001


WIT4_097 = WIT4_001


WIT5_097 = WIT5_001


WIT6_097 = WIT6_001


ACT1_098 = ACT1_001


ACT2_098 = ACT2_001


WHER_098 = WHER_001


WIT0_098 = WIT0_001


WIT1_098 = WIT1_001


WIT2_098 = WIT2_001


WIT3_098 = WIT3_001


WIT4_098 = WIT4_001


WIT5_098 = WIT5_001


WIT6_098 = WIT6_001


ACT1_099 = ACT1_001


ACT2_099 = ACT2_001


WHER_099 = WHER_001


WIT0_099 = WIT0_001


WIT1_099 = WIT1_001


WIT2_099 = WIT2_001


WIT3_099 = WIT3_001


WIT4_099 = WIT4_001


WIT5_099 = WIT5_001


WIT6_099 = WIT6_001


ACT1_100 = ACT1_001


ACT2_100 = ACT2_001


WHER_100 = WHER_001


WIT0_100 = WIT0_001


WIT1_100 = WIT1_001


WIT2_100 = WIT2_001


WIT3_100 = WIT3_001


WIT4_100 = WIT4_001


WIT5_100 = WIT5_001


WIT6_100 = WIT6_001


ACT1_101 = ACT1_001


ACT2_101 = ACT2_001


WHER_101 = WHER_001


WIT0_101 = WIT0_001


WIT1_101 = WIT1_001


WIT2_101 = WIT2_001


WIT3_101 = WIT3_001


WIT4_101 = WIT4_001


WIT5_101 = WIT5_001


WIT6_101 = WIT6_001


ACT1_102 = ACT1_001


ACT2_102 = ACT2_001


WHER_102 = WHER_001


WIT0_102 = WIT0_001


WIT1_102 = WIT1_001


WIT2_102 = WIT2_001


WIT3_102 = WIT3_001


WIT4_102 = WIT4_001


WIT5_102 = WIT5_001


WIT6_102 = WIT6_001


ACT1_103 = ACT1_001


ACT2_103 = ACT2_001


WHER_103 = WHER_001


WIT0_103 = WIT0_001


WIT1_103 = WIT1_001


WIT2_103 = WIT2_001


WIT3_103 = WIT3_001


WIT4_103 = WIT4_001


WIT5_103 = WIT5_001


WIT6_103 = WIT6_001


ACT1_104 = ACT1_001


ACT2_104 = ACT2_001


WHER_104 = WHER_001


WIT0_104 = WIT0_001


WIT1_104 = WIT1_001


WIT2_104 = WIT2_001


WIT3_104 = WIT3_001


WIT4_104 = WIT4_001


WIT5_104 = WIT5_001


WIT6_104 = WIT6_001


ACT1_105 = ACT1_001


ACT2_105 = ACT2_001


WHER_105 = WHER_001


WIT0_105 = WIT0_001


WIT1_105 = WIT1_001


WIT2_105 = WIT2_001


WIT3_105 = WIT3_001


WIT4_105 = WIT4_001


WIT5_105 = WIT5_001


WIT6_105 = WIT6_001


ACT1_106 = ACT1_001


ACT2_106 = ACT2_001


WHER_106 = WHER_001


WIT0_106 = WIT0_001


WIT1_106 = WIT1_001


WIT2_106 = WIT2_001


WIT3_106 = WIT3_001


WIT4_106 = WIT4_001


WIT5_106 = WIT5_001


WIT6_106 = WIT6_001


ACT1_107 = ACT1_001


ACT2_107 = ACT2_001


WHER_107 = WHER_001


WIT0_107 = WIT0_001


WIT1_107 = WIT1_001


WIT2_107 = WIT2_001


WIT3_107 = WIT3_001


WIT4_107 = WIT4_001


WIT5_107 = WIT5_001


WIT6_107 = WIT6_001


ACT1_108 = ACT1_001


ACT2_108 = ACT2_001


WHER_108 = WHER_001


WIT0_108 = WIT0_001


WIT1_108 = WIT1_001


WIT2_108 = WIT2_001


WIT3_108 = WIT3_001


WIT4_108 = WIT4_001


WIT5_108 = WIT5_001


WIT6_108 = WIT6_001


ACT1_109 = ACT1_001


ACT2_109 = ACT2_001


WHER_109 = WHER_001


WIT0_109 = WIT0_001


WIT1_109 = WIT1_001


WIT2_109 = WIT2_001


WIT3_109 = WIT3_001


WIT4_109 = WIT4_001


WIT5_109 = WIT5_001


WIT6_109 = WIT6_001


ACT1_110 = ACT1_001


ACT2_110 = ACT2_001


WHER_110 = WHER_001


WIT0_110 = WIT0_001


WIT1_110 = WIT1_001


WIT2_110 = WIT2_001


WIT3_110 = WIT3_001


WIT4_110 = WIT4_001


WIT5_110 = WIT5_001


WIT6_110 = WIT6_001


ACT1_111 = ACT1_001


ACT2_111 = ACT2_001


WHER_111 = WHER_001


WIT0_111 = WIT0_001


WIT1_111 = WIT1_001


WIT2_111 = WIT2_001


WIT3_111 = WIT3_001


WIT4_111 = WIT4_001


WIT5_111 = WIT5_001


WIT6_111 = WIT6_001


ACT1_112 = ACT1_001


ACT2_112 = ACT2_001


WHER_112 = WHER_001


WIT0_112 = WIT0_001


WIT1_112 = WIT1_001


WIT2_112 = WIT2_001


WIT3_112 = WIT3_001


WIT4_112 = WIT4_001


WIT5_112 = WIT5_001


WIT6_112 = WIT6_001


ACT1_113 = ACT1_001


ACT2_113 = ACT2_001


WHER_113 = WHER_001


WIT0_113 = WIT0_001


WIT1_113 = WIT1_001


WIT2_113 = WIT2_001


WIT3_113 = WIT3_001


WIT4_113 = WIT4_001


WIT5_113 = WIT5_001


WIT6_113 = WIT6_001


ACT1_114 = ACT1_001


ACT2_114 = ACT2_001


WHER_114 = WHER_001


WIT0_114 = WIT0_001


WIT1_114 = WIT1_001


WIT2_114 = WIT2_001


WIT3_114 = WIT3_001


WIT4_114 = WIT4_001


WIT5_114 = WIT5_001


WIT6_114 = WIT6_001


ACT1_115 = ACT1_001


ACT2_115 = ACT2_001


WHER_115 = WHER_001


WIT0_115 = WIT0_001


WIT1_115 = WIT1_001


WIT2_115 = WIT2_001


WIT3_115 = WIT3_001


WIT4_115 = WIT4_001


WIT5_115 = WIT5_001


WIT6_115 = WIT6_001


ACT1_116 = ACT1_001


ACT2_116 = ACT2_001


WHER_116 = WHER_001


WIT0_116 = WIT0_001


WIT1_116 = WIT1_001


WIT2_116 = WIT2_001


WIT3_116 = WIT3_001


WIT4_116 = WIT4_001


WIT5_116 = WIT5_001


WIT6_116 = WIT6_001


ACT1_117 = ACT1_001


ACT2_117 = ACT2_001


WHER_117 = WHER_001


WIT0_117 = WIT0_001


WIT1_117 = WIT1_001


WIT2_117 = WIT2_001


WIT3_117 = WIT3_001


WIT4_117 = WIT4_001


WIT5_117 = WIT5_001


WIT6_117 = WIT6_001


ACT1_118 = ACT1_001


ACT2_118 = ACT2_001


WHER_118 = WHER_001


WIT0_118 = WIT0_001


WIT1_118 = WIT1_001


WIT2_118 = WIT2_001


WIT3_118 = WIT3_001


WIT4_118 = WIT4_001


WIT5_118 = WIT5_001


WIT6_118 = WIT6_001


ACT1_119 = ACT1_001


ACT2_119 = ACT2_001


WHER_119 = WHER_001


WIT0_119 = WIT0_001


WIT1_119 = WIT1_001


WIT2_119 = WIT2_001


WIT3_119 = WIT3_001


WIT4_119 = WIT4_001


WIT5_119 = WIT5_001


WIT6_119 = WIT6_001


ACT1_120 = ACT1_001


ACT2_120 = ACT2_001


WHER_120 = WHER_001


WIT0_120 = WIT0_001


WIT1_120 = WIT1_001


WIT2_120 = WIT2_001


WIT3_120 = WIT3_001


WIT4_120 = WIT4_001


WIT5_120 = WIT5_001


WIT6_120 = WIT6_001


ACT1_121 = ACT1_001


ACT2_121 = ACT2_001


WHER_121 = WHER_001


WIT0_121 = WIT0_001


WIT1_121 = WIT1_001


WIT2_121 = WIT2_001


WIT3_121 = WIT3_001


WIT4_121 = WIT4_001


WIT5_121 = WIT5_001


WIT6_121 = WIT6_001


ACT1_122 = ACT1_001


ACT2_122 = ACT2_001


WHER_122 = WHER_001


WIT0_122 = WIT0_001


WIT1_122 = WIT1_001


WIT2_122 = WIT2_001


WIT3_122 = WIT3_001


WIT4_122 = WIT4_001


WIT5_122 = WIT5_001


WIT6_122 = WIT6_001


ACT1_123 = ACT1_001


ACT2_123 = ACT2_001


WHER_123 = WHER_001


WIT0_123 = WIT0_001


WIT1_123 = WIT1_001


WIT2_123 = WIT2_001


WIT3_123 = WIT3_001


WIT4_123 = WIT4_001


WIT5_123 = WIT5_001


WIT6_123 = WIT6_001


ACT1_124 = ACT1_001


ACT2_124 = ACT2_001


WHER_124 = WHER_001


WIT0_124 = WIT0_001


WIT1_124 = WIT1_001


WIT2_124 = WIT2_001


WIT3_124 = WIT3_001


WIT4_124 = WIT4_001


WIT5_124 = WIT5_001


WIT6_124 = WIT6_001


ACT1_125 = ACT1_001


ACT2_125 = ACT2_001


WHER_125 = WHER_001


WIT0_125 = WIT0_001


WIT1_125 = WIT1_001


WIT2_125 = WIT2_001


WIT3_125 = WIT3_001


WIT4_125 = WIT4_001


WIT5_125 = WIT5_001


WIT6_125 = WIT6_001


ACT1_126 = ACT1_001


ACT2_126 = ACT2_001


WHER_126 = WHER_001


WIT0_126 = WIT0_001


WIT1_126 = WIT1_001


WIT2_126 = WIT2_001


WIT3_126 = WIT3_001


WIT4_126 = WIT4_001


WIT5_126 = WIT5_001


WIT6_126 = WIT6_001


ACT1_127 = ACT1_001


ACT2_127 = ACT2_001


WHER_127 = WHER_001


WIT0_127 = WIT0_001


WIT1_127 = WIT1_001


WIT2_127 = WIT2_001


WIT3_127 = WIT3_001


WIT4_127 = WIT4_001


WIT5_127 = WIT5_001


WIT6_127 = WIT6_001


ACT1_128 = ACT1_001


ACT2_128 = ACT2_001


WHER_128 = WHER_001


WIT0_128 = WIT0_001


WIT1_128 = WIT1_001


WIT2_128 = WIT2_001


WIT3_128 = WIT3_001


WIT4_128 = WIT4_001


WIT5_128 = WIT5_001


WIT6_128 = WIT6_001


ACT1_129 = ACT1_001


ACT2_129 = ACT2_001


WHER_129 = WHER_001


WIT0_129 = WIT0_001


WIT1_129 = WIT1_001


WIT2_129 = WIT2_001


WIT3_129 = WIT3_001


WIT4_129 = WIT4_001


WIT5_129 = WIT5_001


WIT6_129 = WIT6_001


ACT1_130 = ACT1_001


ACT2_130 = ACT2_001


WHER_130 = WHER_001


WIT0_130 = WIT0_001


WIT1_130 = WIT1_001


WIT2_130 = WIT2_001


WIT3_130 = WIT3_001


WIT4_130 = WIT4_001


WIT5_130 = WIT5_001


WIT6_130 = WIT6_001


ACT1_131 = ACT1_001


ACT2_131 = ACT2_001


WHER_131 = WHER_001


WIT0_131 = WIT0_001


WIT1_131 = WIT1_001


WIT2_131 = WIT2_001


WIT3_131 = WIT3_001


WIT4_131 = WIT4_001


WIT5_131 = WIT5_001


WIT6_131 = WIT6_001


ACT1_132 = ACT1_001


ACT2_132 = ACT2_001


WHER_132 = WHER_001


WIT0_132 = WIT0_001


WIT1_132 = WIT1_001


WIT2_132 = WIT2_001


WIT3_132 = WIT3_001


WIT4_132 = WIT4_001


WIT5_132 = WIT5_001


WIT6_132 = WIT6_001


ACT1_133 = ACT1_001


ACT2_133 = ACT2_001


WHER_133 = WHER_001


WIT0_133 = WIT0_001


WIT1_133 = WIT1_001


WIT2_133 = WIT2_001


WIT3_133 = WIT3_001


WIT4_133 = WIT4_001


WIT5_133 = WIT5_001


WIT6_133 = WIT6_001


ACT1_134 = ACT1_001


ACT2_134 = ACT2_001


WHER_134 = WHER_001


WIT0_134 = WIT0_001


WIT1_134 = WIT1_001


WIT2_134 = WIT2_001


WIT3_134 = WIT3_001


WIT4_134 = WIT4_001


WIT5_134 = WIT5_001


WIT6_134 = WIT6_001


ACT1_135 = ACT1_001


ACT2_135 = ACT2_001


WHER_135 = WHER_001


WIT0_135 = WIT0_001


WIT1_135 = WIT1_001


WIT2_135 = WIT2_001


WIT3_135 = WIT3_001


WIT4_135 = WIT4_001


WIT5_135 = WIT5_001


WIT6_135 = WIT6_001


ACT1_136 = ACT1_001


ACT2_136 = ACT2_001


WHER_136 = WHER_001


WIT0_136 = WIT0_001


WIT1_136 = WIT1_001


WIT2_136 = WIT2_001


WIT3_136 = WIT3_001


WIT4_136 = WIT4_001


WIT5_136 = WIT5_001


WIT6_136 = WIT6_001


ACT1_137 = ACT1_001


ACT2_137 = ACT2_001


WHER_137 = WHER_001


WIT0_137 = WIT0_001


WIT1_137 = WIT1_001


WIT2_137 = WIT2_001


WIT3_137 = WIT3_001


WIT4_137 = WIT4_001


WIT5_137 = WIT5_001


WIT6_137 = WIT6_001


ACT1_138 = ACT1_001


ACT2_138 = ACT2_001


WHER_138 = WHER_001


WIT0_138 = WIT0_001


WIT1_138 = WIT1_001


WIT2_138 = WIT2_001


WIT3_138 = WIT3_001


WIT4_138 = WIT4_001


WIT5_138 = WIT5_001


WIT6_138 = WIT6_001


ACT1_139 = ACT1_001


ACT2_139 = ACT2_001


WHER_139 = WHER_001


WIT0_139 = WIT0_001


WIT1_139 = WIT1_001


WIT2_139 = WIT2_001


WIT3_139 = WIT3_001


WIT4_139 = WIT4_001


WIT5_139 = WIT5_001


WIT6_139 = WIT6_001


ACT1_140 = ACT1_001


ACT2_140 = ACT2_001


WHER_140 = WHER_001


WIT0_140 = WIT0_001


WIT1_140 = WIT1_001


WIT2_140 = WIT2_001


WIT3_140 = WIT3_001


WIT4_140 = WIT4_001


WIT5_140 = WIT5_001


WIT6_140 = WIT6_001


ACT1_141 = ACT1_001


ACT2_141 = ACT2_001


WHER_141 = WHER_001


WIT0_141 = WIT0_001


WIT1_141 = WIT1_001


WIT2_141 = WIT2_001


WIT3_141 = WIT3_001


WIT4_141 = WIT4_001


WIT5_141 = WIT5_001


WIT6_141 = WIT6_001


ACT1_142 = ACT1_001


ACT2_142 = ACT2_001


WHER_142 = WHER_001


WIT0_142 = WIT0_001


WIT1_142 = WIT1_001


WIT2_142 = WIT2_001


WIT3_142 = WIT3_001


WIT4_142 = WIT4_001


WIT5_142 = WIT5_001


WIT6_142 = WIT6_001


ACT1_143 = ACT1_001


ACT2_143 = ACT2_001


WHER_143 = WHER_001


WIT0_143 = WIT0_001


WIT1_143 = WIT1_001


WIT2_143 = WIT2_001


WIT3_143 = WIT3_001


WIT4_143 = WIT4_001


WIT5_143 = WIT5_001


WIT6_143 = WIT6_001


ACT1_144 = ACT1_001


ACT2_144 = ACT2_001


WHER_144 = WHER_001


WIT0_144 = WIT0_001


WIT1_144 = WIT1_001


WIT2_144 = WIT2_001


WIT3_144 = WIT3_001


WIT4_144 = WIT4_001


WIT5_144 = WIT5_001


WIT6_144 = WIT6_001


class KID01(OrderedEnum):
    NOT_ALONE_NOT_WITH_PEOPLE_YOU_DON_T_KNOW = '0'
    ALONE_OR_WITH_PEOPLE_YOU_DON_T_KNOW = '1'
    MISSING1 = '-1'
    MISSING2 = '-2'


KID02 = KID01


KID03 = KID01


KID04 = KID01


KID05 = KID01


KID06 = KID01


KID07 = KID01


KID08 = KID01


KID09 = KID01


KID010 = KID01


KID011 = KID01


KID012 = KID01


KID013 = KID01


KID014 = KID01


KID015 = KID01


KID016 = KID01


KID017 = KID01


KID018 = KID01


KID019 = KID01


KID020 = KID01


KID021 = KID01


KID022 = KID01


KID023 = KID01


KID024 = KID01


KID025 = KID01


KID026 = KID01


KID027 = KID01


KID028 = KID01


KID029 = KID01


KID030 = KID01


KID031 = KID01


KID032 = KID01


KID033 = KID01


KID034 = KID01


KID035 = KID01


KID036 = KID01


KID037 = KID01


KID038 = KID01


KID039 = KID01


KID040 = KID01


KID041 = KID01


KID042 = KID01


KID043 = KID01


KID044 = KID01


KID045 = KID01


KID046 = KID01


KID047 = KID01


KID048 = KID01


KID049 = KID01


KID050 = KID01


KID051 = KID01


KID052 = KID01


KID053 = KID01


KID054 = KID01


KID055 = KID01


KID056 = KID01


KID057 = KID01


KID058 = KID01


KID059 = KID01


KID060 = KID01


KID061 = KID01


KID062 = KID01


KID063 = KID01


KID064 = KID01


KID065 = KID01


KID066 = KID01


KID067 = KID01


KID068 = KID01


KID069 = KID01


KID070 = KID01


KID071 = KID01


KID072 = KID01


KID073 = KID01


KID074 = KID01


KID075 = KID01


KID076 = KID01


KID077 = KID01


KID078 = KID01


KID079 = KID01


KID080 = KID01


KID081 = KID01


KID082 = KID01


KID083 = KID01


KID084 = KID01


KID085 = KID01


KID086 = KID01


KID087 = KID01


KID088 = KID01


KID089 = KID01


KID090 = KID01


KID091 = KID01


KID092 = KID01


KID093 = KID01


KID094 = KID01


KID095 = KID01


KID096 = KID01


KID097 = KID01


KID098 = KID01


KID099 = KID01


KID0100 = KID01


KID0101 = KID01


KID0102 = KID01


KID0103 = KID01


KID0104 = KID01


KID0105 = KID01


KID0106 = KID01


KID0107 = KID01


KID0108 = KID01


KID0109 = KID01


KID0110 = KID01


KID0111 = KID01


KID0112 = KID01


KID0113 = KID01


KID0114 = KID01


KID0115 = KID01


KID0116 = KID01


KID0117 = KID01


KID0118 = KID01


KID0119 = KID01


KID0120 = KID01


KID0121 = KID01


KID0122 = KID01


KID0123 = KID01


KID0124 = KID01


KID0125 = KID01


KID0126 = KID01


KID0127 = KID01


KID0128 = KID01


KID0129 = KID01


KID0130 = KID01


KID0131 = KID01


KID0132 = KID01


KID0133 = KID01


KID0134 = KID01


KID0135 = KID01


KID0136 = KID01


KID0137 = KID01


KID0138 = KID01


KID0139 = KID01


KID0140 = KID01


KID0141 = KID01


KID0142 = KID01


KID0143 = KID01


KID0144 = KID01


class KID11(OrderedEnum):
    NOT_WITH_YOUR_PARENTS = '0'
    WITH_YOUR_PARENTS = '1'
    MISSING1 = '-1'
    MISSING2 = '-2'


KID12 = KID11


KID13 = KID11


KID14 = KID11


KID15 = KID11


KID16 = KID11


KID17 = KID11


KID18 = KID11


KID19 = KID11


KID110 = KID11


KID111 = KID11


KID112 = KID11


KID113 = KID11


KID114 = KID11


KID115 = KID11


KID116 = KID11


KID117 = KID11


KID118 = KID11


KID119 = KID11


KID120 = KID11


KID121 = KID11


KID122 = KID11


KID123 = KID11


KID124 = KID11


KID125 = KID11


KID126 = KID11


KID127 = KID11


KID128 = KID11


KID129 = KID11


KID130 = KID11


KID131 = KID11


KID132 = KID11


KID133 = KID11


KID134 = KID11


KID135 = KID11


KID136 = KID11


KID137 = KID11


KID138 = KID11


KID139 = KID11


KID140 = KID11


KID141 = KID11


KID142 = KID11


KID143 = KID11


KID144 = KID11


KID145 = KID11


KID146 = KID11


KID147 = KID11


KID148 = KID11


KID149 = KID11


KID150 = KID11


KID151 = KID11


KID152 = KID11


KID153 = KID11


KID154 = KID11


KID155 = KID11


KID156 = KID11


KID157 = KID11


KID158 = KID11


KID159 = KID11


KID160 = KID11


KID161 = KID11


KID162 = KID11


KID163 = KID11


KID164 = KID11


KID165 = KID11


KID166 = KID11


KID167 = KID11


KID168 = KID11


KID169 = KID11


KID170 = KID11


KID171 = KID11


KID172 = KID11


KID173 = KID11


KID174 = KID11


KID175 = KID11


KID176 = KID11


KID177 = KID11


KID178 = KID11


KID179 = KID11


KID180 = KID11


KID181 = KID11


KID182 = KID11


KID183 = KID11


KID184 = KID11


KID185 = KID11


KID186 = KID11


KID187 = KID11


KID188 = KID11


KID189 = KID11


KID190 = KID11


KID191 = KID11


KID192 = KID11


KID193 = KID11


KID194 = KID11


KID195 = KID11


KID196 = KID11


KID197 = KID11


KID198 = KID11


KID199 = KID11


KID1100 = KID11


KID1101 = KID11


KID1102 = KID11


KID1103 = KID11


KID1104 = KID11


KID1105 = KID11


KID1106 = KID11


KID1107 = KID11


KID1108 = KID11


KID1109 = KID11


KID1110 = KID11


KID1111 = KID11


KID1112 = KID11


KID1113 = KID11


KID1114 = KID11


KID1115 = KID11


KID1116 = KID11


KID1117 = KID11


KID1118 = KID11


KID1119 = KID11


KID1120 = KID11


KID1121 = KID11


KID1122 = KID11


KID1123 = KID11


KID1124 = KID11


KID1125 = KID11


KID1126 = KID11


KID1127 = KID11


KID1128 = KID11


KID1129 = KID11


KID1130 = KID11


KID1131 = KID11


KID1132 = KID11


KID1133 = KID11


KID1134 = KID11


KID1135 = KID11


KID1136 = KID11


KID1137 = KID11


KID1138 = KID11


KID1139 = KID11


KID1140 = KID11


KID1141 = KID11


KID1142 = KID11


KID1143 = KID11


KID1144 = KID11


class KID21(OrderedEnum):
    NOT_WITH_OTHER_PEOPLE_IN_YOUR_HOUSEHOLD = '0'
    WITH_OTHER_PEOPLE_IN_YOUR_HOUSEHOLD = '1'
    MISSING1 = '-1'
    MISSING2 = '-2'


KID22 = KID21


KID23 = KID21


KID24 = KID21


KID25 = KID21


KID26 = KID21


KID27 = KID21


KID28 = KID21


KID29 = KID21


KID210 = KID21


KID211 = KID21


KID212 = KID21


KID213 = KID21


KID214 = KID21


KID215 = KID21


KID216 = KID21


KID217 = KID21


KID218 = KID21


KID219 = KID21


KID220 = KID21


KID221 = KID21


KID222 = KID21


KID223 = KID21


KID224 = KID21


KID225 = KID21


KID226 = KID21


KID227 = KID21


KID228 = KID21


KID229 = KID21


KID230 = KID21


KID231 = KID21


KID232 = KID21


KID233 = KID21


KID234 = KID21


KID235 = KID21


KID236 = KID21


KID237 = KID21


KID238 = KID21


KID239 = KID21


KID240 = KID21


KID241 = KID21


KID242 = KID21


KID243 = KID21


KID244 = KID21


KID245 = KID21


KID246 = KID21


KID247 = KID21


KID248 = KID21


KID249 = KID21


KID250 = KID21


KID251 = KID21


KID252 = KID21


KID253 = KID21


KID254 = KID21


KID255 = KID21


KID256 = KID21


KID257 = KID21


KID258 = KID21


KID259 = KID21


KID260 = KID21


KID261 = KID21


KID262 = KID21


KID263 = KID21


KID264 = KID21


KID265 = KID21


KID266 = KID21


KID267 = KID21


KID268 = KID21


KID269 = KID21


KID270 = KID21


KID271 = KID21


KID272 = KID21


KID273 = KID21


KID274 = KID21


KID275 = KID21


KID276 = KID21


KID277 = KID21


KID278 = KID21


KID279 = KID21


KID280 = KID21


KID281 = KID21


KID282 = KID21


KID283 = KID21


KID284 = KID21


KID285 = KID21


KID286 = KID21


KID287 = KID21


KID288 = KID21


KID289 = KID21


KID290 = KID21


KID291 = KID21


KID292 = KID21


KID293 = KID21


KID294 = KID21


KID295 = KID21


KID296 = KID21


KID297 = KID21


KID298 = KID21


KID299 = KID21


KID2100 = KID21


KID2101 = KID21


KID2102 = KID21


KID2103 = KID21


KID2104 = KID21


KID2105 = KID21


KID2106 = KID21


KID2107 = KID21


KID2108 = KID21


KID2109 = KID21


KID2110 = KID21


KID2111 = KID21


KID2112 = KID21


KID2113 = KID21


KID2114 = KID21


KID2115 = KID21


KID2116 = KID21


KID2117 = KID21


KID2118 = KID21


KID2119 = KID21


KID2120 = KID21


KID2121 = KID21


KID2122 = KID21


KID2123 = KID21


KID2124 = KID21


KID2125 = KID21


KID2126 = KID21


KID2127 = KID21


KID2128 = KID21


KID2129 = KID21


KID2130 = KID21


KID2131 = KID21


KID2132 = KID21


KID2133 = KID21


KID2134 = KID21


KID2135 = KID21


KID2136 = KID21


KID2137 = KID21


KID2138 = KID21


KID2139 = KID21


KID2140 = KID21


KID2141 = KID21


KID2142 = KID21


KID2143 = KID21


KID2144 = KID21


class KID31(OrderedEnum):
    NOT_WITH_OTHER_PEOPLE_THAT_YOU_KNOW = '0'
    WITH_OTHER_PEOPLE_THAT_YOU_KNOW = '1'
    MISSING1 = '-1'
    MISSING2 = '-2'


KID32 = KID31


KID33 = KID31


KID34 = KID31


KID35 = KID31


KID36 = KID31


KID37 = KID31


KID38 = KID31


KID39 = KID31


KID310 = KID31


KID311 = KID31


KID312 = KID31


KID313 = KID31


KID314 = KID31


KID315 = KID31


KID316 = KID31


KID317 = KID31


KID318 = KID31


KID319 = KID31


KID320 = KID31


KID321 = KID31


KID322 = KID31


KID323 = KID31


KID324 = KID31


KID325 = KID31


KID326 = KID31


KID327 = KID31


KID328 = KID31


KID329 = KID31


KID330 = KID31


KID331 = KID31


KID332 = KID31


KID333 = KID31


KID334 = KID31


KID335 = KID31


KID336 = KID31


KID337 = KID31


KID338 = KID31


KID339 = KID31


KID340 = KID31


KID341 = KID31


KID342 = KID31


KID343 = KID31


KID344 = KID31


KID345 = KID31


KID346 = KID31


KID347 = KID31


KID348 = KID31


KID349 = KID31


KID350 = KID31


KID351 = KID31


KID352 = KID31


KID353 = KID31


KID354 = KID31


KID355 = KID31


KID356 = KID31


KID357 = KID31


KID358 = KID31


KID359 = KID31


KID360 = KID31


KID361 = KID31


KID362 = KID31


KID363 = KID31


KID364 = KID31


KID365 = KID31


KID366 = KID31


KID367 = KID31


KID368 = KID31


KID369 = KID31


KID370 = KID31


KID371 = KID31


KID372 = KID31


KID373 = KID31


KID374 = KID31


KID375 = KID31


KID376 = KID31


KID377 = KID31


KID378 = KID31


KID379 = KID31


KID380 = KID31


KID381 = KID31


KID382 = KID31


KID383 = KID31


KID384 = KID31


KID385 = KID31


KID386 = KID31


KID387 = KID31


KID388 = KID31


KID389 = KID31


KID390 = KID31


KID391 = KID31


KID392 = KID31


KID393 = KID31


KID394 = KID31


KID395 = KID31


KID396 = KID31


KID397 = KID31


KID398 = KID31


KID399 = KID31


KID3100 = KID31


KID3101 = KID31


KID3102 = KID31


KID3103 = KID31


KID3104 = KID31


KID3105 = KID31


KID3106 = KID31


KID3107 = KID31


KID3108 = KID31


KID3109 = KID31


KID3110 = KID31


KID3111 = KID31


KID3112 = KID31


KID3113 = KID31


KID3114 = KID31


KID3115 = KID31


KID3116 = KID31


KID3117 = KID31


KID3118 = KID31


KID3119 = KID31


KID3120 = KID31


KID3121 = KID31


KID3122 = KID31


KID3123 = KID31


KID3124 = KID31


KID3125 = KID31


KID3126 = KID31


KID3127 = KID31


KID3128 = KID31


KID3129 = KID31


KID3130 = KID31


KID3131 = KID31


KID3132 = KID31


KID3133 = KID31


KID3134 = KID31


KID3135 = KID31


KID3136 = KID31


KID3137 = KID31


KID3138 = KID31


KID3139 = KID31


KID3140 = KID31


KID3141 = KID31


KID3142 = KID31


KID3143 = KID31


KID3144 = KID31


class KID41(OrderedEnum):
    MAIN_ACTIVITY_IS_NOT_SLEEP__EMPLOYMENT_OR_STUDY = '0'
    MAIN_ACTIVITY_IS_ASLEEP__EMPLOYMENT_OR_STUDY = '1'
    MISSING1 = '-1'
    MISSING2 = '-2'


KID42 = KID41


KID43 = KID41


KID44 = KID41


KID45 = KID41


KID46 = KID41


KID47 = KID41


KID48 = KID41


KID49 = KID41


KID410 = KID41


KID411 = KID41


KID412 = KID41


KID413 = KID41


KID414 = KID41


KID415 = KID41


KID416 = KID41


KID417 = KID41


KID418 = KID41


KID419 = KID41


KID420 = KID41


KID421 = KID41


KID422 = KID41


KID423 = KID41


KID424 = KID41


KID425 = KID41


KID426 = KID41


KID427 = KID41


KID428 = KID41


KID429 = KID41


KID430 = KID41


KID431 = KID41


KID432 = KID41


KID433 = KID41


KID434 = KID41


KID435 = KID41


KID436 = KID41


KID437 = KID41


KID438 = KID41


KID439 = KID41


KID440 = KID41


KID441 = KID41


KID442 = KID41


KID443 = KID41


KID444 = KID41


KID445 = KID41


KID446 = KID41


KID447 = KID41


KID448 = KID41


KID449 = KID41


KID450 = KID41


KID451 = KID41


KID452 = KID41


KID453 = KID41


KID454 = KID41


KID455 = KID41


KID456 = KID41


KID457 = KID41


KID458 = KID41


KID459 = KID41


KID460 = KID41


KID461 = KID41


KID462 = KID41


KID463 = KID41


KID464 = KID41


KID465 = KID41


KID466 = KID41


KID467 = KID41


KID468 = KID41


KID469 = KID41


KID470 = KID41


KID471 = KID41


KID472 = KID41


KID473 = KID41


KID474 = KID41


KID475 = KID41


KID476 = KID41


KID477 = KID41


KID478 = KID41


KID479 = KID41


KID480 = KID41


KID481 = KID41


KID482 = KID41


KID483 = KID41


KID484 = KID41


KID485 = KID41


KID486 = KID41


KID487 = KID41


KID488 = KID41


KID489 = KID41


KID490 = KID41


KID491 = KID41


KID492 = KID41


KID493 = KID41


KID494 = KID41


KID495 = KID41


KID496 = KID41


KID497 = KID41


KID498 = KID41


KID499 = KID41


KID4100 = KID41


KID4101 = KID41


KID4102 = KID41


KID4103 = KID41


KID4104 = KID41


KID4105 = KID41


KID4106 = KID41


KID4107 = KID41


KID4108 = KID41


KID4109 = KID41


KID4110 = KID41


KID4111 = KID41


KID4112 = KID41


KID4113 = KID41


KID4114 = KID41


KID4115 = KID41


KID4116 = KID41


KID4117 = KID41


KID4118 = KID41


KID4119 = KID41


KID4120 = KID41


KID4121 = KID41


KID4122 = KID41


KID4123 = KID41


KID4124 = KID41


KID4125 = KID41


KID4126 = KID41


KID4127 = KID41


KID4128 = KID41


KID4129 = KID41


KID4130 = KID41


KID4131 = KID41


KID4132 = KID41


KID4133 = KID41


KID4134 = KID41


KID4135 = KID41


KID4136 = KID41


KID4137 = KID41


KID4138 = KID41


KID4139 = KID41


KID4140 = KID41


KID4141 = KID41


KID4142 = KID41


KID4143 = KID41


KID4144 = KID41


class KID51(OrderedEnum):
    __WERE_YOU_WITH_ANYBODY__QUESTION_ANSWERED = '0'
    NO_ANSWERS_TO__WERE_YOU_WITH_ANYBODY__QUESTION = '1'
    MISSING1 = '-1'
    MISSING2 = '-2'


KID52 = KID51


KID53 = KID51


KID54 = KID51


KID55 = KID51


KID56 = KID51


KID57 = KID51


KID58 = KID51


KID59 = KID51


KID510 = KID51


KID511 = KID51


KID512 = KID51


KID513 = KID51


KID514 = KID51


KID515 = KID51


KID516 = KID51


KID517 = KID51


KID518 = KID51


KID519 = KID51


KID520 = KID51


KID521 = KID51


KID522 = KID51


KID523 = KID51


KID524 = KID51


KID525 = KID51


KID526 = KID51


KID527 = KID51


KID528 = KID51


KID529 = KID51


KID530 = KID51


KID531 = KID51


KID532 = KID51


KID533 = KID51


KID534 = KID51


KID535 = KID51


KID536 = KID51


KID537 = KID51


KID538 = KID51


KID539 = KID51


KID540 = KID51


KID541 = KID51


KID542 = KID51


KID543 = KID51


KID544 = KID51


KID545 = KID51


KID546 = KID51


KID547 = KID51


KID548 = KID51


KID549 = KID51


KID550 = KID51


KID551 = KID51


KID552 = KID51


KID553 = KID51


KID554 = KID51


KID555 = KID51


KID556 = KID51


KID557 = KID51


KID558 = KID51


KID559 = KID51


KID560 = KID51


KID561 = KID51


KID562 = KID51


KID563 = KID51


KID564 = KID51


KID565 = KID51


KID566 = KID51


KID567 = KID51


KID568 = KID51


KID569 = KID51


KID570 = KID51


KID571 = KID51


KID572 = KID51


KID573 = KID51


KID574 = KID51


KID575 = KID51


KID576 = KID51


KID577 = KID51


KID578 = KID51


KID579 = KID51


KID580 = KID51


KID581 = KID51


KID582 = KID51


KID583 = KID51


KID584 = KID51


KID585 = KID51


KID586 = KID51


KID587 = KID51


KID588 = KID51


KID589 = KID51


KID590 = KID51


KID591 = KID51


KID592 = KID51


KID593 = KID51


KID594 = KID51


KID595 = KID51


KID596 = KID51


KID597 = KID51


KID598 = KID51


KID599 = KID51


KID5100 = KID51


KID5101 = KID51


KID5102 = KID51


KID5103 = KID51


KID5104 = KID51


KID5105 = KID51


KID5106 = KID51


KID5107 = KID51


KID5108 = KID51


KID5109 = KID51


KID5110 = KID51


KID5111 = KID51


KID5112 = KID51


KID5113 = KID51


KID5114 = KID51


KID5115 = KID51


KID5116 = KID51


KID5117 = KID51


KID5118 = KID51


KID5119 = KID51


KID5120 = KID51


KID5121 = KID51


KID5122 = KID51


KID5123 = KID51


KID5124 = KID51


KID5125 = KID51


KID5126 = KID51


KID5127 = KID51


KID5128 = KID51


KID5129 = KID51


KID5130 = KID51


KID5131 = KID51


KID5132 = KID51


KID5133 = KID51


KID5134 = KID51


KID5135 = KID51


KID5136 = KID51


KID5137 = KID51


KID5138 = KID51


KID5139 = KID51


KID5140 = KID51


KID5141 = KID51


KID5142 = KID51


KID5143 = KID51


KID5144 = KID51


class DAATQ1A(OrderedEnum):
    YES = '0'
    NO = '1'
    NOT_ANSWERED = '2'
    MISSING1 = '-1'


class DAATQ2(OrderedEnum):
    NOW_AND_THEN_DURING_THE_DAY = '0'
    AT_THE_END_OF_THE_DIARY_DAY = '1'
    THE_DAY_AFTER_THE_DIARY_DAY = '2'
    LATER___DAYS_AFTER_THE_DIARY_DAY = '3'
    NOT_ANSWERED = '4'
    MISSING1 = '-1'


class DAATQ3(OrderedEnum):
    AT_HOME = '0'
    SOMEWHERE_ELSE = '1'
    NOT_ANSWERED = '2'
    MISSING1 = '-1'


DAATQ4 = DAATQ3


class ATDAATQ5A1(OrderedEnum):
    NO = '0'
    YES___IN_PAID_WORK = '1'
    MISSING1 = '-1'


class ATDAATQ5A2(OrderedEnum):
    NO = '0'
    YES___AT_SCHOOL_OR_COLLEGE = '1'
    MISSING1 = '-1'


class ATDAATQ5A3(OrderedEnum):
    NO = '0'
    YES___NOT_IN_PAID_WORK_OR_AT_SCHOOLCOLLEGE = '1'
    MISSING1 = '-1'


class DAATQ5B(OrderedEnum):
    YES__I_WAS_WORKING = '0'
    NO__IT_WAS_A_WEEK_END_DAYDAY_I_DON_T_USUALLY_WORK = '1'
    NO__I_WAS_ON_LEAVE = '2'
    NO__I_WAS_SICK = '3'
    NO__ABSENT_FOR_ANOTHER_REASON = '4'
    NOT_ANSWERED = '5'
    MISSING1 = '-1'


class DAATQ6(OrderedEnum):
    TERM_TIME = '0'
    SCHOOL_HOLIDAYSVACATION = '1'
    NOT_ANSWERED = '2'
    MISSING1 = '-1'


class DAATQ7A(OrderedEnum):
    NO = '0'
    YES__A_DAY_TRIP_WITHIN_THE_COUNTRY = '1'
    YES__A_DAY_TRIP_ABROAD = '2'
    YES__AN_OVERNIGHT_TRIP_WITHIN_THE_COUNTRY = '3'
    YES__AND_OVERNIGHT_TRIP_ABROAD = '4'
    NOT_ANSWERED = '5'
    MISSING1 = '-1'


class DAATQ7BATC(OrderedEnum):
    AUSTRIA = '0'
    BELGIUM = '1'
    CYPRUS = '2'
    DENMARK = '3'
    FINLAND = '4'
    FRANCE = '5'
    GERMANY = '6'
    GIBRALTAR = '7'
    GREAT_BRITAIN = '8'
    GREECE = '9'
    ICELAND = '10'
    IRELAND = '11'
    ITALY = '12'
    LUXEMBOURG = '13'
    MALTA = '14'
    NETHERLANDS = '15'
    NORWAY = '16'
    PORTUGAL = '17'
    RUSSIA = '18'
    SPAIN = '19'
    SWEDEN = '20'
    SWITZERLAND = '21'
    TURKEY = '22'
    OTHER_FORMER_SOVIET_UNION = '23'
    FORMER_YUGOSLAVIA = '24'
    CENTRAL_AND_EASTERN_EUROPE = '25'
    OTHER_EUROPE = '26'
    BAHRAIN = '27'
    EGYPT = '28'
    IRAN = '29'
    IRAQ = '30'
    ISRAEL = '31'
    JORDAN = '32'
    KUWAIT = '33'
    LEBANON = '34'
    OMAN = '35'
    QATAR = '36'
    SAUDI_ARABIA = '37'
    UNITED_ARAB_EMIRATES = '38'
    OTHER_MIDDLE_EAST = '39'
    ALGERIA = '40'
    BOTSWANA = '41'
    CAMEROON = '42'
    ETHIOPIA = '43'
    GHANA = '44'
    KENYA = '45'
    LIBYA = '46'
    MAURITIUS = '47'
    MOROCCO = '48'
    NIGERIA = '49'
    SOUTH_AFRICA = '50'
    SUDAN = '51'
    TANZANIA = '52'
    TUNISIA = '53'
    UGANDA = '54'
    ZAIRE = '55'
    ZAMBIA = '56'
    ZIMBABWE = '57'
    OTHER_AFRICA = '58'
    BAHAMAS = '59'
    BARBADOS = '60'
    BERMUDA = '61'
    JAMAICA = '62'
    OTHER_CARIBBEAN = '63'
    BANGLADESH = '64'
    BRUNEI = '65'
    HONG_KONG = '66'
    INDIA = '67'
    INDONESIA = '68'
    JAPAN = '69'
    MALAYSIA = '70'
    PAKISTAN = '71'
    PR_OF_CHINA = '72'
    PHILIPPINES = '73'
    SINGAPORE = '74'
    SOUTH_KOREA = '75'
    SRI_LANKA = '76'
    TAIWAN = '77'
    THAILAND = '78'
    OTHER_ASIA = '79'
    ARGENTINA = '80'
    BRAZIL = '81'
    CHILE = '82'
    COLOMBIA = '83'
    ECUADOR = '84'
    MEXICO = '85'
    PARAGUAY = '86'
    PERU = '87'
    URUGUAY = '88'
    VENEZUELA = '89'
    OTHER_CENTRALSOUTH_AMERICA = '90'
    CANADA = '91'
    USA = '92'
    OTHER_NORTH_AMERICA = '93'
    AUSTRALIA = '94'
    NEW_ZEALAND = '95'
    OTHER_SOUTH_PACIFIC = '96'
    OTHER_COUNTRIES = '97'
    DKNA = '98'
    MISSING1 = '-1'


DAATQ8 = DAATQ1A


class DAATQ8AT1(OrderedEnum):
    OWN_BIRTHDAY = '0'
    SOMEONE_ELSE_S_BIRTHDAY = '1'
    RELIGIOUS_FESTIVAL_OR_EVENT = '2'
    SPORTS_EVENT = '3'
    OTHER_SOCIAL_CELEBRATORY_EVENT = '4'
    OTHER_SOCIAL_EVENT = '5'
    WORK_EVENT = '6'
    SCHOOL_EVENT = '7'
    ANNUAL_LEAVE = '8'
    ILLNESS_OF_RESPONDENT = '9'
    ILLNESS_OF_SOMEONE_ELSE = '10'
    ACCIDENT = '11'
    VISITS_TO_HEALTH_PROFESSIONALS = '12'
    OTHER_HEALTH_RELATED_REASONS = '13'
    WEATHER_RELATED = '14'
    OTHER_ENVIRONMENTAL_REASONS = '15'
    VISITS_TO__OF_SERVICE_PROVIDERS = '16'
    MOVING_HOUSE = '17'
    LAW_RELATED = '18'
    OTHER = '19'
    IRRELEVANT_OR_VAGUE_ANSWER = '20'
    DON_T_KNOW = '21'
    NONE = '22'
    NULL = '23'
    MISSING1 = '-1'


DAATQ8AT2 = DAATQ8AT1


DAATQ8AT3 = DAATQ8AT1


DAATQ8AT4 = DAATQ8AT1


DAATQ8AT5 = DAATQ8AT1


class DAATQ9(OrderedEnum):
    NO = '0'
    YES = '1'
    NOT_ANSWERED = '2'
    MISSING1 = '-1'


class DAATQ9AT1(OrderedEnum):
    TIME_CONSUMING = '0'
    MEMORY = '1'
    REQUIRED_HELP = '2'
    DIFFICULT_TO_COMPLETE = '3'
    OTHER_REASON = '4'
    IRRELEVANT_OR_VAGUE_ANSWER = '5'
    DON_T_KNOW = '6'
    NONE = '7'
    NULL = '8'
    MISSING1 = '-1'


DAATQ9AT2 = DAATQ9AT1


DAATQ9AT3 = DAATQ9AT1


DAATQ9AT4 = DAATQ9AT1


DAATQ9AT5 = DAATQ9AT1


DKATQ1 = DAATQ2


DKATQ2 = DAATQ3


DKATQ3 = DAATQ3


DKATQ4 = DAATQ6


DKATQ5 = DAATQ1A


DKATQ5AT1 = DAATQ8AT1


DKATQ5AT2 = DAATQ8AT1


DKATQ5AT3 = DAATQ8AT1


DKATQ5AT4 = DAATQ8AT1


DKATQ5AT5 = DAATQ8AT1


DKATQ6 = DAATQ9


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
