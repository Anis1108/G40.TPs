def get_evaluation(self):

    if self.nb_scores == 0:
        return 0

    return self.total_score / self.nb_scores
