import numpy as np


class Lottery(object):
    def __init__(self):
        self._member_score_dict = dict()
        pass

    def set_member_score_dict(self, ms_dict):
        """
        Sets the dictionary correlating a member's name to their weight.
        :param ms_dict: The dictionary to set.
        :return: The dict of {participant: weight}
        """
        self._member_score_dict = ms_dict
        return

    def perform_lottery(self, num_winners: int = 20, print_winners: bool = False):
        """
        Chooses num_winners winners from the list of potential winners.
        :param num_winners: The number of unique people to choose.
        :param print_winners: Whether or not to output the winners to the console.
        :return: The list of unique winners.
        """
        # Gets a list of the possible winners, where a participant's weight is determined
        # by their occurring frequency.
        potential_choices = self.__get_lottery_list()
        lottery_winners = list()

        # Handle edge case of the list of people being fewer than the number of winners.
        if len(potential_choices) <= num_winners:
            lottery_winners = potential_choices
        else:
            # Choose num_winners random winners.
            num_added = 0
            while num_added < num_winners:
                random_choice = np.random.randint(0, len(potential_choices))
                if potential_choices[random_choice] not in lottery_winners:
                    lottery_winners.append(potential_choices[random_choice])
                    num_added += 1

        if print_winners:
            print(lottery_winners)

        return lottery_winners

    def __get_lottery_list(self):
        """
        Generates a list of people who can win the lottery. A participant's name is repeated multiple times to
        make their name more likely, thus assigning a weight to their participation.
        :return: The list of members to choose from.
        """
        lottery_list = list()
        for participant in self._member_score_dict.keys():
            for i in range(self._member_score_dict[participant]):
                lottery_list.append(participant)
        return lottery_list

    def update_member_score_dict_entry(self, name: str, value: int):
        """
        Adds or updates an entry in the member_score_dict with passed arguments.
        :param name: The name of the person to update.
        :param value: The value to add or set the name's value to.
        """
        if name in self._member_score_dict.keys():
            self._member_score_dict[name] += value
        else:
            self._member_score_dict[name] = value

