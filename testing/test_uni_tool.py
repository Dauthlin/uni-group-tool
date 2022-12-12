import uni_group_tool.main as main_tools
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
    current_all_team = main_tools.Groups(main_tools.initialize(csv_input, size_of_teams, shuffle))
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
    data_path = os.path.join(os.path.dirname(__file__), "test_data/sample_short.csv")
    csv_input = main_tools.get_csv(data_path)
    criteria = {"diversity": ["average", "home", "gender"],
                "amount_to_be_together": [("gender", "F", 2), ("gender", "M", 1), ("home", "O", 2), ("home", "H", 1)],
                "specific_teams": [[("208026943", 3), ("208063956", 3), ("207069131", 4)]]}

    current_all_team = main_tools.Groups(main_tools.initialize(csv_input, size_of_teams, shuffle))

    group = copy.deepcopy(current_all_team)
    main_tools.overall_fitness(group, [2], criteria)
    assert group.fitness.get_all() == {'diversity': {'gender': 0, 'home': 4, 'average': 132}, 'should_be_together': {'gender': {'M': 1, 'F': 1}, 'home': {'H': 1, 'O': 0}}, 'has_required_students': 2}
    group = copy.deepcopy(current_all_team)
    main_tools.overall_fitness(group, [3], criteria)
    assert group.fitness.get_all() == {'diversity': {'gender': 0, 'home': 4, 'average': 136}, 'should_be_together': {'gender': {'M': 1, 'F': 1}, 'home': {'H': 1, 'O': 0}}, 'has_required_students': 1}
    group = copy.deepcopy(current_all_team)
    main_tools.overall_fitness(group, [7], criteria)
    assert group.fitness.get_all() == {'diversity': {'gender': 0, 'home': 0, 'average': 16}, 'should_be_together': {'gender': {'M': 1, 'F': 1}, 'home': {'H': 1, 'O': 1}}, 'has_required_students': 0}
    group = copy.deepcopy(current_all_team)
    main_tools.overall_fitness(group, [9], criteria)
    assert group.fitness.get_all() == {'diversity': {'gender': 4, 'home': 0, 'average': 12}, 'should_be_together': {'gender': {'M': 1, 'F': 0}, 'home': {'H': 1, 'O': 1}}, 'has_required_students': 0}

# if __name__ == '__main__':
#     test_single_fitness()
