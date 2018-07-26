import unittest

import sports


class TestScores(unittest.TestCase):

    def test_xml(self):
        try:
            sports.scores._request_xml(sports.BASEBALL)
        except sports.errors.SportError:
            self.fail('XML request raised SportError')

        self.assertRaises(sports.errors.SportError, sports.scores._request_xml, 'fake sport')

    def test_matches(self):
        soccer = sports.get_sport(sports.SOCCER)
        match = sports.get_match(sports.SOCCER, soccer[0].home_team, soccer[1].away_team)
        self.assertIsNotNone(soccer)
        self.assertIsNotNone(match)
        self.assertIsNotNone(sports.all_matches())

        self.assertEqual(repr(match), '{} {}-{} {}'.format(match.home_team, match.home_score, match.away_score, match.away_team))
        self.assertEqual(str(match), '{} {}-{} {}'.format(match.home_team, match.home_score, match.away_score, match.away_team))

        self.assertRaises(sports.errors.MatchError, sports.get_match, sports.SOCCER, 'fake team', 'fake team')

    def test_teams(self):
        self.assertIsNotNone(sports.get_team(sports.FOOTBALL, 'steelers'))
        self.assertIsNotNone(sports.get_team(sports.HOCKEY, 'penguins'))
        self.assertIsNotNone(sports.get_team(sports.BASKETBALL, '76ers'))
        self.assertIsNotNone(sports.get_team(sports.BASEBALL, 'pirates'))

    def test_errors(self):
        sport = sports.FOOTBALL
        teams = ['steelers', 'patriots']
        self.assertEqual(str(sports.errors.MatchError(sport, teams)), 'football match not found for steelers, patriots')
        self.assertEqual(str(sports.errors.SportError('fake sport')), 'Sport not found for fake sport')
        self.assertEqual(str(sports.errors.StatsNotFound(sport)), 'Extra stats not yet supported for football')
        self.assertEqual(str(sports.errors.TeamNotFoundError(sport, teams[0])), 'Team steelers not found for sport football')

        self.assertRaises(sports.errors.StatsNotFound, sports.get_team, 'fake sport', 'fake team')


if __name__ == '__main__':
    unittest.main()
