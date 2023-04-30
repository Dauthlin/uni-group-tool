import uni_group_tool.main as main_tools
import uni_group_tool.Fitness_Data as fitness_tools
import copy
import os


def test_pull_data():
    data_path = os.path.join(os.path.dirname(__file__), "test_data/sample_short.csv")
    lines = [
        {'StudentID': '208031587', 'username': 'name1', 'surname': 'surname1', 'firstName': 'firstName1', 'gender': 'F',
         'home': 'H', 'average': '100', 'team': '', 'status': ''},
        {'StudentID': '208002991', 'username': 'name2', 'surname': 'surname2', 'firstName': 'firstName2', 'gender': 'M',
         'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '208026943', 'username': 'name3', 'surname': 'surname3', 'firstName': 'firstName3', 'gender': 'M',
         'home': 'H', 'average': '79', 'team': '', 'status': ''},
        {'StudentID': '207069131', 'username': 'name4', 'surname': 'surname4', 'firstName': 'firstName4', 'gender': 'M',
         'home': 'H', 'average': '79', 'team': '', 'status': ''},
        {'StudentID': '208014819', 'username': 'name5', 'surname': 'surname5', 'firstName': 'firstName5', 'gender': 'M',
         'home': 'O', 'average': '42', 'team': '', 'status': ''},
        {'StudentID': '208065064', 'username': 'name6', 'surname': 'surname6', 'firstName': 'firstName6', 'gender': 'F',
         'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '207045467', 'username': 'name7', 'surname': 'surname7', 'firstName': 'firstName7', 'gender': 'M',
         'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '208064954', 'username': 'name8', 'surname': 'surname8', 'firstName': 'firstName8', 'gender': 'M',
         'home': 'H', 'average': '100', 'team': '', 'status': ''},
        {'StudentID': '208022752', 'username': 'name9', 'surname': 'surname9', 'firstName': 'firstName9', 'gender': 'M',
         'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '208065155', 'username': 'name10', 'surname': 'surname10', 'firstName': 'firstName10',
         'gender': 'M', 'home': 'H', 'average': '79', 'team': '', 'status': ''},
        {'StudentID': '208009112', 'username': 'name11', 'surname': 'surname11', 'firstName': 'firstName11',
         'gender': 'M', 'home': 'H', 'average': '78', 'team': '', 'status': ''},
        {'StudentID': '208030174', 'username': 'name12', 'surname': 'surname12', 'firstName': 'firstName12',
         'gender': 'M', 'home': 'H', 'average': '42', 'team': '', 'status': ''},
        {'StudentID': '208015062', 'username': 'name13', 'surname': 'surname13', 'firstName': 'firstName13',
         'gender': 'M', 'home': 'H', 'average': '100', 'team': '', 'status': ''},
        {'StudentID': '208065130', 'username': 'name14', 'surname': 'surname14', 'firstName': 'firstName14',
         'gender': 'M', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '208001810', 'username': 'name15', 'surname': 'surname15', 'firstName': 'firstName15',
         'gender': 'M', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '208034253', 'username': 'name16', 'surname': 'surname16', 'firstName': 'firstName16',
         'gender': 'M', 'home': 'H', 'average': '78', 'team': '', 'status': ''},
        {'StudentID': '207036032', 'username': 'name17', 'surname': 'surname17', 'firstName': 'firstName17',
         'gender': 'M', 'home': 'H', 'average': '35', 'team': '', 'status': ''},
        {'StudentID': '207036776', 'username': 'name18', 'surname': 'surname18', 'firstName': 'firstName18',
         'gender': 'M', 'home': 'O', 'average': '81', 'team': '', 'status': ''},
        {'StudentID': '208064922', 'username': 'name19', 'surname': 'surname19', 'firstName': 'firstName19',
         'gender': 'M', 'home': 'H', 'average': '100', 'team': '', 'status': ''},
        {'StudentID': '208008294', 'username': 'name20', 'surname': 'surname20', 'firstName': 'firstName20',
         'gender': 'M', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '208065143', 'username': 'name21', 'surname': 'surname21', 'firstName': 'firstName21',
         'gender': 'M', 'home': 'H', 'average': '77', 'team': '', 'status': ''},
        {'StudentID': '208063956', 'username': 'name22', 'surname': 'surname22', 'firstName': 'firstName22',
         'gender': 'M', 'home': 'O', 'average': '46', 'team': '', 'status': ''},
        {'StudentID': '208016615', 'username': 'name23', 'surname': 'surname23', 'firstName': 'firstName23',
         'gender': 'M', 'home': 'H', 'average': '86', 'team': '', 'status': ''},
        {'StudentID': '207009782', 'username': 'name24', 'surname': 'surname24', 'firstName': 'firstName24',
         'gender': 'M', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '208037463', 'username': 'name25', 'surname': 'surname25', 'firstName': 'firstName25',
         'gender': 'M', 'home': 'H', 'average': '100', 'team': '', 'status': ''},
        {'StudentID': '208009084', 'username': 'name26', 'surname': 'surname26', 'firstName': 'firstName26',
         'gender': 'M', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '207026694', 'username': 'name27', 'surname': 'surname27', 'firstName': 'firstName27',
         'gender': 'M', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '208005937', 'username': 'name28', 'surname': 'surname28', 'firstName': 'firstName28',
         'gender': 'M', 'home': 'H', 'average': '81', 'team': '', 'status': ''},
        {'StudentID': '208023029', 'username': 'name29', 'surname': 'surname29', 'firstName': 'firstName29',
         'gender': 'M', 'home': 'H', 'average': '77', 'team': '', 'status': ''},
        {'StudentID': '209078254', 'username': 'name30', 'surname': 'surname30', 'firstName': 'firstName30',
         'gender': 'M', 'home': 'O', 'average': '50', 'team': '', 'status': 'Arrived for Y2, no Yr 1 score'},
        {'StudentID': '207032011', 'username': 'name31', 'surname': 'surname31', 'firstName': 'firstName31',
         'gender': 'F', 'home': 'H', 'average': '80', 'team': '', 'status': ''},
        {'StudentID': '208034026', 'username': 'name32', 'surname': 'surname32', 'firstName': 'firstName32',
         'gender': 'M', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '208047415', 'username': 'name33', 'surname': 'surname33', 'firstName': 'firstName33',
         'gender': 'M', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '206041650', 'username': 'name34', 'surname': 'surname34', 'firstName': 'firstName34',
         'gender': 'M', 'home': 'H', 'average': '52', 'team': '', 'status': ''},
        {'StudentID': '208046677', 'username': 'name35', 'surname': 'surname35', 'firstName': 'firstName35',
         'gender': 'M', 'home': 'H', 'average': '41', 'team': '', 'status': ''},
        {'StudentID': '208023584', 'username': 'name36', 'surname': 'surname36', 'firstName': 'firstName36',
         'gender': 'F', 'home': 'O', 'average': '77', 'team': '', 'status': ''},
        {'StudentID': '208014111', 'username': 'name37', 'surname': 'surname37', 'firstName': 'firstName37',
         'gender': 'M', 'home': 'H', 'average': '97', 'team': '', 'status': ''},
        {'StudentID': '208028189', 'username': 'name38', 'surname': 'surname38', 'firstName': 'firstName38',
         'gender': 'M', 'home': 'H', 'average': '99', 'team': '', 'status': ''},
        {'StudentID': '208016240', 'username': 'name39', 'surname': 'surname39', 'firstName': 'firstName39',
         'gender': 'F', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '207034595', 'username': 'name40', 'surname': 'surname40', 'firstName': 'firstName40',
         'gender': 'M', 'home': 'H', 'average': '81', 'team': '', 'status': ''},
        {'StudentID': '207030715', 'username': 'name41', 'surname': 'surname41', 'firstName': 'firstName41',
         'gender': 'M', 'home': 'H', 'average': '76', 'team': '', 'status': ''},
        {'StudentID': '208046148', 'username': 'name42', 'surname': 'surname42', 'firstName': 'firstName42',
         'gender': 'M', 'home': 'O', 'average': '52', 'team': '', 'status': ''},
        {'StudentID': '208038000', 'username': 'name43', 'surname': 'surname43', 'firstName': 'firstName43',
         'gender': 'F', 'home': 'H', 'average': '98', 'team': '', 'status': ''},
        {'StudentID': '207023254', 'username': 'name44', 'surname': 'surname44', 'firstName': 'firstName44',
         'gender': 'F', 'home': 'H', 'average': '99', 'team': '', 'status': ''},
        {'StudentID': '207001293', 'username': 'name45', 'surname': 'surname45', 'firstName': 'firstName45',
         'gender': 'M', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '208065047', 'username': 'name46', 'surname': 'surname46', 'firstName': 'firstName46',
         'gender': 'M', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '208065069', 'username': 'name47', 'surname': 'surname47', 'firstName': 'firstName47',
         'gender': 'M', 'home': 'H', 'average': '81', 'team': '', 'status': ''},
        {'StudentID': '207037221', 'username': 'name48', 'surname': 'surname48', 'firstName': 'firstName48',
         'gender': 'F', 'home': 'H', 'average': '76', 'team': '', 'status': ''},
        {'StudentID': '208022796', 'username': 'name49', 'surname': 'surname49', 'firstName': 'firstName49',
         'gender': 'M', 'home': 'H', 'average': '52', 'team': '', 'status': ''},
        {'StudentID': '208028201', 'username': 'name50', 'surname': 'surname50', 'firstName': 'firstName50',
         'gender': 'M', 'home': 'H', 'average': '99', 'team': '', 'status': ''},
        {'StudentID': '208032727', 'username': 'name51', 'surname': 'surname51', 'firstName': 'firstName51',
         'gender': 'M', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '208020120', 'username': 'name52', 'surname': 'surname52', 'firstName': 'firstName52',
         'gender': 'M', 'home': 'H', 'average': '82', 'team': '', 'status': ''},
        {'StudentID': '208064977', 'username': 'name53', 'surname': 'surname53', 'firstName': 'firstName53',
         'gender': 'M', 'home': 'H', 'average': '76', 'team': '', 'status': ''},
        {'StudentID': '208036828', 'username': 'name54', 'surname': 'surname54', 'firstName': 'firstName54',
         'gender': 'M', 'home': 'H', 'average': '52', 'team': '', 'status': ''},
        {'StudentID': '208016469', 'username': 'name55', 'surname': 'surname55', 'firstName': 'firstName55',
         'gender': 'M', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '208021639', 'username': 'name56', 'surname': 'surname56', 'firstName': 'firstName56',
         'gender': 'F', 'home': 'H', 'average': '96', 'team': '', 'status': ''},
        {'StudentID': '207060859', 'username': 'name57', 'surname': 'surname57', 'firstName': 'firstName57',
         'gender': 'F', 'home': 'H', 'average': '99', 'team': '', 'status': ''},
        {'StudentID': '208019531', 'username': 'name58', 'surname': 'surname58', 'firstName': 'firstName58',
         'gender': 'M', 'home': 'H', 'average': '83', 'team': '', 'status': ''},
        {'StudentID': '205019077', 'username': 'name59', 'surname': 'surname59', 'firstName': 'firstName59',
         'gender': 'M', 'home': 'H', 'average': '75', 'team': '', 'status': ''}]
    assert main_tools.get_csv(data_path) == lines


def test_initialize():
    # test that it initalizes correctly
    size_of_teams = 3
    shuffle = False
    data_path = os.path.join(os.path.dirname(__file__), "test_data/sample_short.csv")
    csv_input = main_tools.get_csv(data_path)
    min_group_size_or_amount_of_groups = True
    current_all_team = main_tools.Groups(main_tools.initialize(csv_input, size_of_teams, shuffle,min_group_size_or_amount_of_groups))  # type: ignore
    current_all_team = main_tools.groups_to_csv(current_all_team)
    # check that each student contains the correct keys
    for i in current_all_team:
        assert "StudentID" in i
        assert "username" in i
        assert "surname" in i
        assert "firstName" in i
        assert "gender" in i
        assert "home" in i
        assert "average" in i
        assert "team" in i
        assert "status" in i
    # check there is the correct amount of students
    assert len(current_all_team) == 59


def test_single_fitness():
    # checks that the fitness is being filled in correctly, comparisons from manual test
    size_of_teams = 3
    shuffle = False
    min_group_size_or_amount_of_groups = True
    data_path = os.path.join(os.path.dirname(__file__), "test_data/sample_short.csv")
    csv_input = main_tools.get_csv(data_path)
    criteria = {"diversity": ["average", "home", "gender"],
                "amount_to_be_together": [("gender", "F", 2), ("gender", "M", 1), ("home", "O", 2), ("home", "H", 1)],
                "specific_teams": [[("208026943", 3), ("208063956", 3), ("207069131", 4)]]}

    current_all_team = main_tools.Groups(main_tools.initialize(csv_input, size_of_teams, shuffle,min_group_size_or_amount_of_groups))  # type: ignore

    group = copy.deepcopy(current_all_team)
    main_tools.overall_fitness(group, [2], criteria)
    assert group.fitness.get_all() == {'diversity': {'gender': 0, 'home': 4, 'average': 132},
                                       'should_be_together': {'gender': {'M': 1, 'F': 1}, 'home': {'H': 1, 'O': 0}},
                                       'has_required_students': 2}
    group = copy.deepcopy(current_all_team)
    main_tools.overall_fitness(group, [3], criteria)
    assert group.fitness.get_all() == {'diversity': {'gender': 0, 'home': 4, 'average': 136},
                                       'should_be_together': {'gender': {'M': 1, 'F': 1}, 'home': {'H': 1, 'O': 0}},
                                       'has_required_students': 1}
    group = copy.deepcopy(current_all_team)
    main_tools.overall_fitness(group, [7], criteria)
    assert group.fitness.get_all() == {'diversity': {'gender': 0, 'home': 0, 'average': 16},
                                       'should_be_together': {'gender': {'M': 1, 'F': 1}, 'home': {'H': 1, 'O': 1}},
                                       'has_required_students': 0}
    group = copy.deepcopy(current_all_team)
    main_tools.overall_fitness(group, [9], criteria)
    assert group.fitness.get_all() == {'diversity': {'gender': 4, 'home': 0, 'average': 12},
                                       'should_be_together': {'gender': {'M': 1, 'F': 0}, 'home': {'H': 1, 'O': 1}},
                                       'has_required_students': 0}


def test_overall_fitness():
    # checks that the fitness is being filled in correctly, comparisons from manual test
    size_of_teams = 3
    shuffle = False
    min_group_size_or_amount_of_groups = True
    data_path = os.path.join(os.path.dirname(__file__), "test_data/sample_short.csv")
    csv_input = main_tools.get_csv(data_path)
    criteria = {"diversity": ["average", "home", "gender"],
                "amount_to_be_together": [("gender", "F", 2), ("gender", "M", 1), ("home", "O", 2), ("home", "H", 1)],
                "specific_teams": [[("208026943", 3), ("208063956", 3), ("207069131", 4)]]}

    current_all_team = main_tools.Groups(main_tools.initialize(csv_input, size_of_teams, shuffle,min_group_size_or_amount_of_groups))

    group = copy.deepcopy(current_all_team)
    main_tools.overall_fitness(group, [2, 3], criteria)
    assert group.fitness.get_all() == {'diversity': {'gender': 0, 'home': 8, 'average': 268},
                                       'should_be_together': {'gender': {'M': 2, 'F': 2}, 'home': {'H': 2, 'O': 0}},
                                       'has_required_students': 3}

    group = copy.deepcopy(current_all_team)
    main_tools.overall_fitness(group, [7, 9], criteria)
    assert group.fitness.get_all() == {'diversity': {'gender': 4, 'home': 0, 'average': 28},
                                       'should_be_together': {'gender': {'M': 2, 'F': 1}, 'home': {'H': 2, 'O': 2}},
                                       'has_required_students': 0}


def test_comparing_groups():
    # checks that the fitness is being filled in correctly, comparisons from manual test
    size_of_teams = 3
    shuffle = False
    min_group_size_or_amount_of_groups = True
    data_path = os.path.join(os.path.dirname(__file__), "test_data/sample_short.csv")
    csv_input = main_tools.get_csv(data_path)
    criteria = {"diversity": ["average", "home", "gender"],
                "amount_to_be_together": [("gender", "F", 2), ("gender", "M", 1), ("home", "O", 2), ("home", "H", 1)],
                "specific_teams": [[("208026943", 3), ("208063956", 3), ("207069131", 4)]]}

    current_all_team = main_tools.Groups(main_tools.initialize(csv_input, size_of_teams, shuffle, min_group_size_or_amount_of_groups))

    group1 = copy.deepcopy(current_all_team)
    main_tools.overall_fitness(group1, [2, 3], criteria)
    group2 = copy.deepcopy(current_all_team)
    main_tools.overall_fitness(group2, [7, 9], criteria)
    result = (main_tools.compare_fitness(group1, group2, {}))
    assert result[0] is True
    assert result[1] == group1


def test_swapping():
    size_of_teams = 3
    shuffle = False
    min_group_size_or_amount_of_groups = True
    data_path = os.path.join(os.path.dirname(__file__), "test_data/sample_short.csv")
    csv_input = main_tools.get_csv(data_path)
    current_all_team = main_tools.Groups(main_tools.initialize(csv_input, size_of_teams, shuffle, min_group_size_or_amount_of_groups))
    print(current_all_team.get_groups()[1].get_students())
    student1 = current_all_team.get_groups()[1].get_student(1)
    student2 = current_all_team.get_groups()[2].get_student(0)
    # swaps group1, group2, student1, student2
    current_all_team.swap_students(1, 2, 1, 0)
    assert current_all_team.get_groups()[1].get_student(1) == student2
    assert current_all_team.get_groups()[2].get_student(0) == student1


def test_select():
    size_of_teams = 3
    shuffle = False
    min_group_size_or_amount_of_groups = True
    data_path = os.path.join(os.path.dirname(__file__), "test_data/sample_short.csv")
    csv_input = main_tools.get_csv(data_path)
    criteria = {"diversity": ["average", "home", "gender"],
                "amount_to_be_together": [("gender", "F", 2), ("gender", "M", 1), ("home", "O", 2), ("home", "H", 1)],
                "specific_teams": [[("208026943", 3), ("208063956", 3), ("207069131", 4)]]}
    current_all_team = main_tools.Groups(main_tools.initialize(csv_input, size_of_teams, shuffle, min_group_size_or_amount_of_groups))
    main_tools.overall_fitness(current_all_team, (range(0, current_all_team.number_of_groups())), criteria)
    # swapping students that are required to be in specific groups, this means that we know they will score badly
    swap1 = copy.deepcopy(current_all_team)
    swap1.swap_students(1, 2, 1, 0)
    main_tools.overall_fitness(swap1, [1, 2], criteria)

    swap2 = copy.deepcopy(current_all_team)
    swap2.swap_students(1, 2, 1, 1)
    main_tools.overall_fitness(swap2, [1, 2], criteria)

    swap3 = copy.deepcopy(current_all_team)
    swap3.swap_students(1, 3, 1, 0)
    main_tools.overall_fitness(swap3, [1, 3], criteria)

    # only swap that doesn't swap a student that's required to be in a group
    swap4 = copy.deepcopy(current_all_team)
    swap4.swap_students(1, 5, 1, 1)
    main_tools.overall_fitness(swap4, [1, 2], criteria)

    # selecting the best group, this will be the only group which isn't swapping a required student out of it
    result = main_tools.select(
        [(swap1, (1, 2, 1, 0)), (swap2, (1, 2, 1, 1)), (swap3, (1, 3, 1, 0)), (swap4, (1, 5, 1, 1))], {})
    assert result[0] == swap4
    assert result[1] == (1, 5, 1, 1)


def test_test():
    # test(group_to_test, current_best_group, current_time, time_when_best_was_found, weights)
    size_of_teams = 3
    shuffle = False
    min_group_size_or_amount_of_groups = True
    data_path = os.path.join(os.path.dirname(__file__), "test_data/sample_short.csv")
    csv_input = main_tools.get_csv(data_path)
    criteria = {"diversity": ["average", "home", "gender"],
                "amount_to_be_together": [("gender", "F", 2), ("gender", "M", 1), ("home", "O", 2), ("home", "H", 1)],
                "specific_teams": [[("208026943", 3), ("208063956", 3), ("207069131", 4)]]}
    current_all_team = main_tools.Groups(main_tools.initialize(csv_input, size_of_teams, shuffle, min_group_size_or_amount_of_groups))
    main_tools.overall_fitness(current_all_team, (range(0, current_all_team.number_of_groups())), criteria)
    # swapping students that are required to be in specific groups, this means that we know they will score badly
    swap1 = copy.deepcopy(current_all_team)
    swap1.swap_students(1, 2, 1, 0)
    main_tools.overall_fitness(swap1, [1, 2], criteria)

    # only swap that doesn't swap a student that's required to be in a group
    swap4 = current_all_team
    swap4.swap_students(1, 5, 1, 1)
    main_tools.overall_fitness(swap4, [1, 2], criteria)
    # should return the better group (swap4) and what time it was found
    assert (swap4, 4, 0.2180685358255452) == main_tools.test(swap4, swap1, 4, 0, {})
    assert (swap4, 0, 0) == main_tools.test(swap1, swap4, 4, 0, {})


def test_generate():
    # test(group_to_test, current_best_group, current_time, time_when_best_was_found, weights)
    size_of_teams = 3
    shuffle = False
    min_group_size_or_amount_of_groups = True
    data_path = os.path.join(os.path.dirname(__file__), "test_data/sample_short.csv")
    csv_input = main_tools.get_csv(data_path)
    criteria = {"diversity": ["average", "home", "gender"],
                "amount_to_be_together": [("gender", "F", 2), ("gender", "M", 1), ("home", "O", 2), ("home", "H", 1)],
                "specific_teams": [[("208026943", 3), ("208063956", 3), ("207069131", 4)]]}
    current_all_team = main_tools.Groups(main_tools.initialize(csv_input, size_of_teams, shuffle, min_group_size_or_amount_of_groups))
    main_tools.overall_fitness(current_all_team, (range(0, current_all_team.number_of_groups())), criteria)
    subgroup1 = main_tools.Groups(copy.deepcopy(current_all_team.get_groups()[3:5]))
    current_all_team.swap_students(3, 4, 1, 1)
    bestgroup = main_tools.Groups(current_all_team.get_groups()[3:5])
    neighbours = main_tools.generate_multiprocessing(subgroup1, bestgroup, 0, criteria, {})
    names = []
    for i in neighbours:
        names.append([(j["username"], j["team"]) for j in main_tools.groups_to_csv(i[0])])
    assert names == [[('name5', 4), ('name23', 4), ('name42', 4), ('name4', 5), ('name24', 5), ('name43', 5)],
                     [('name24', 4), ('name23', 4), ('name42', 4), ('name5', 5), ('name4', 5), ('name43', 5)],
                     [('name43', 4), ('name23', 4), ('name42', 4), ('name5', 5), ('name24', 5), ('name4', 5)],
                     [('name4', 4), ('name5', 4), ('name42', 4), ('name23', 5), ('name24', 5), ('name43', 5)],
                     [('name4', 4), ('name24', 4), ('name42', 4), ('name5', 5), ('name23', 5), ('name43', 5)],
                     [('name4', 4), ('name43', 4), ('name42', 4), ('name5', 5), ('name24', 5), ('name23', 5)],
                     [('name4', 4), ('name23', 4), ('name5', 4), ('name42', 5), ('name24', 5), ('name43', 5)],
                     [('name4', 4), ('name23', 4), ('name24', 4), ('name5', 5), ('name42', 5), ('name43', 5)],
                     [('name4', 4), ('name23', 4), ('name43', 4), ('name5', 5), ('name24', 5), ('name42', 5)]]
    # repeat with slower generating
    neighbours = main_tools.generate(subgroup1, bestgroup, 0, criteria, {})
    names = []
    for i in neighbours:
        names.append([(j["username"], j["team"]) for j in main_tools.groups_to_csv(i[0])])
    assert names == [[('name5', 4), ('name23', 4), ('name42', 4), ('name4', 5), ('name24', 5), ('name43', 5)],
                     [('name24', 4), ('name23', 4), ('name42', 4), ('name5', 5), ('name4', 5), ('name43', 5)],
                     [('name43', 4), ('name23', 4), ('name42', 4), ('name5', 5), ('name24', 5), ('name4', 5)],
                     [('name4', 4), ('name5', 4), ('name42', 4), ('name23', 5), ('name24', 5), ('name43', 5)],
                     [('name4', 4), ('name24', 4), ('name42', 4), ('name5', 5), ('name23', 5), ('name43', 5)],
                     [('name4', 4), ('name43', 4), ('name42', 4), ('name5', 5), ('name24', 5), ('name23', 5)],
                     [('name4', 4), ('name23', 4), ('name5', 4), ('name42', 5), ('name24', 5), ('name43', 5)],
                     [('name4', 4), ('name23', 4), ('name24', 4), ('name5', 5), ('name42', 5), ('name43', 5)],
                     [('name4', 4), ('name23', 4), ('name43', 4), ('name5', 5), ('name24', 5), ('name42', 5)]]
    # change the tabu time for one of the students
    subgroup1.get_groups()[0].get_student(0).tabu_time = 10
    neighbours = main_tools.generate_multiprocessing(subgroup1, bestgroup, 11, criteria, {})
    names = []
    for i in neighbours:
        names.append([(j["username"], j["team"]) for j in main_tools.groups_to_csv(i[0])])
    assert names == [[('name4', 4), ('name5', 4), ('name42', 4), ('name23', 5), ('name24', 5), ('name43', 5)],
                     [('name4', 4), ('name24', 4), ('name42', 4), ('name5', 5), ('name23', 5), ('name43', 5)],
                     [('name4', 4), ('name43', 4), ('name42', 4), ('name5', 5), ('name24', 5), ('name23', 5)],
                     [('name4', 4), ('name23', 4), ('name5', 4), ('name42', 5), ('name24', 5), ('name43', 5)],
                     [('name4', 4), ('name23', 4), ('name24', 4), ('name5', 5), ('name42', 5), ('name43', 5)],
                     [('name4', 4), ('name23', 4), ('name43', 4), ('name5', 5), ('name24', 5), ('name42', 5)]]


def test_sub_generate():
    # test(group_to_test, current_best_group, current_time, time_when_best_was_found, weights)
    size_of_teams = 3
    shuffle = False
    min_group_size_or_amount_of_groups = True
    data_path = os.path.join(os.path.dirname(__file__), "test_data/sample_short.csv")
    csv_input = main_tools.get_csv(data_path)
    criteria = {"diversity": ["average", "home", "gender"],
                "amount_to_be_together": [("gender", "F", 2), ("gender", "M", 1), ("home", "O", 2), ("home", "H", 1)],
                "specific_teams": [[("208026943", 3), ("208063956", 3), ("207069131", 4)]]}
    current_all_team = main_tools.Groups(main_tools.initialize(csv_input, size_of_teams, shuffle, min_group_size_or_amount_of_groups))
    main_tools.overall_fitness(current_all_team, (range(0, current_all_team.number_of_groups())), criteria)
    subgroup1 = main_tools.Groups(copy.deepcopy(current_all_team.get_groups()[3:5]))
    current_all_team.swap_students(3, 4, 1, 1)
    bestgroup = main_tools.Groups(current_all_team.get_groups()[3:5])
    tabu_distance = 10

    segments = [[x for x in range(0, subgroup1.number_of_groups())], subgroup1, bestgroup, 0, criteria, {}, tabu_distance]
    neighbours = main_tools.sub_section_generate(segments)
    names = []
    for i in neighbours:
        names.append([(j["username"], j["team"]) for j in main_tools.groups_to_csv(i[0])])
    assert names == [[('name5', 4), ('name23', 4), ('name42', 4), ('name4', 5), ('name24', 5), ('name43', 5)],
                     [('name24', 4), ('name23', 4), ('name42', 4), ('name5', 5), ('name4', 5), ('name43', 5)],
                     [('name43', 4), ('name23', 4), ('name42', 4), ('name5', 5), ('name24', 5), ('name4', 5)],
                     [('name4', 4), ('name5', 4), ('name42', 4), ('name23', 5), ('name24', 5), ('name43', 5)],
                     [('name4', 4), ('name24', 4), ('name42', 4), ('name5', 5), ('name23', 5), ('name43', 5)],
                     [('name4', 4), ('name43', 4), ('name42', 4), ('name5', 5), ('name24', 5), ('name23', 5)],
                     [('name4', 4), ('name23', 4), ('name5', 4), ('name42', 5), ('name24', 5), ('name43', 5)],
                     [('name4', 4), ('name23', 4), ('name24', 4), ('name5', 5), ('name42', 5), ('name43', 5)],
                     [('name4', 4), ('name23', 4), ('name43', 4), ('name5', 5), ('name24', 5), ('name42', 5)]]


def test_update():
    # test(group_to_test, current_best_group, current_time, time_when_best_was_found, weights)
    size_of_teams = 3
    shuffle = False
    min_group_size_or_amount_of_groups = True
    data_path = os.path.join(os.path.dirname(__file__), "test_data/sample_short.csv")
    csv_input = main_tools.get_csv(data_path)
    criteria = {"diversity": ["average", "home", "gender"],
                "amount_to_be_together": [("gender", "F", 2), ("gender", "M", 1), ("home", "O", 2), ("home", "H", 1)],
                "specific_teams": [[("208026943", 3), ("208063956", 3), ("207069131", 4)]]}
    current_all_team = main_tools.Groups(main_tools.initialize(csv_input, size_of_teams, shuffle, min_group_size_or_amount_of_groups))
    main_tools.overall_fitness(current_all_team, (range(0, current_all_team.number_of_groups())), criteria)
    current_all_team.swap_students(3, 4, 1, 1)
    current_time = 10

    new_all_team, current_time = main_tools.update((current_all_team, 3, 4, 1, 1), current_time)
    assert (new_all_team, current_time) == (current_all_team, current_time)


def test_fitness_data():
    test_fitness = fitness_tools.FitnessData()
    assert test_fitness.get_all() == {'diversity': {'gender': None, 'home': None, 'average': None},
                                      'should_be_together': {'gender': {'M': None, 'F': None},
                                                             'home': {'H': None, 'O': None}},
                                      'has_required_students': None}
    test_fitness.set_diversity("gender", 3)
    test_fitness.set_diversity("home", 5)
    test_fitness.set_diversity("average", 15)
    average = test_fitness.get_diversity("average")
    assert average == 15
    test_fitness.set_has_required_students(1)
    has_required_students = test_fitness.get_has_required_students()
    assert has_required_students == 1
    test_fitness.set_should_be_together("gender", "F", 2)
    test_fitness.set_should_be_together("gender", "M", 1)
    test_fitness.set_should_be_together("home", "O", 2)
    test_fitness.set_should_be_together("home", "H", 1)
    to_be_together = test_fitness.get_should_be_together("gender", "F")
    assert to_be_together == 2
    assert test_fitness.get_all() == {'diversity': {'gender': 3, 'home': 5, 'average': 15},
                                      'should_be_together': {'gender': {'M': 1, 'F': 2}, 'home': {'H': 1, 'O': 2}},
                                      'has_required_students': 1}
    replacement = {'diversity': {'gender': 5, 'home': 5, 'average': 16},
                   'should_be_together': {'gender': {'M': 1, 'F': 3}, 'home': {'H': 1, 'O': 2}},
                   'has_required_students': 1}
    test_fitness.set_all(replacement)
    assert test_fitness.get_all() == replacement



if __name__ == '__main__':
    test_test()
