import user_inputs, score_aggregator

def main():
    company = user_inputs.prompt_user()
    p_score = score_aggregator.aggregate_scores(company)
    print "The company's p_score estimate is: %.3f\n"%(p_score)

if __name__ == "__main__":
    main()
