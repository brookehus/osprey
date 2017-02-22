from __future__ import print_function

import numpy as np
from .config import Config
from .trials import Trial
from sklearn.pipeline import Pipeline


def execute(args, parser):
    config = Config(args.config, verbose=False)

    session = config.trials()

    items = [curr.to_dict() for curr in session.query(Trial).all()]

    #print(items)

    if not items:
        print('No Models Found')
    else:
        # mean_test_scores = np.nan_to_num(np.array([i["mean_test_score"]
        #                                           for i in items],
        #                                           dtype=float))
        # c_b_m = items[mean_test_scores.argmax()]
        # parameter_dict = c_b_m["parameters"]
        # weighted_mean = c_b_m["mean_test_score"]
        # raw_test_scores = np.array(c_b_m["test_scores"])
        # raw_test_weights = np.array(c_b_m["n_test_samples"])
        # weighted_var = np.average((raw_test_scores - weighted_mean)**2, weights=raw_test_weights)
        # weighted_std = np.sqrt(weighted_var)
        # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # print('Best Current Model = %f +- %f' % (weighted_mean,
        #                                          weighted_std))

        all_test_scores = np.nan_to_num(np.array([i["test_scores"]
                                                  for i in items
                                                  if i["test_scores"] is not None],
                                                  dtype=float))

        all_medians = np.median(all_test_scores, axis=1)
        zipped_list = zip(all_medians, all_test_scores)
        maxmed = all_test_scores[all_medians.argmax()]
        cbm_index = [index for index, i in enumerate(items)
                     if i["test_scores"] is not None
                     and np.all(i["test_scores"] == maxmed)]

        cbm = items[cbm_index[0]]
        parameter_dict = cbm["parameters"]
        median = np.median(cbm["test_scores"])
        q75, q25 = np.percentile(cbm["test_scores"], [75 ,25])
        iqrange = q75 - q25

        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Best Current Model: median = %f' % median)
        print('                    inter-quartile range = %f' % iqrange)
        print('                    scores = ')
        for score in cbm["test_scores"]:
            print('                             ',score)


        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        if isinstance(config.estimator(), Pipeline):
            print('PipelineStep\tParameter \t Value')
            for i in config.estimator().steps:
                print(i[0])
                for param in sorted(parameter_dict.keys()):
                    if str(param).startswith(i[0]):
                        print("\t\t", param.split("__")[1], "\t",
                              parameter_dict[param])
        else:
            print(config.estimator())
            search_space = config.search_space().variables.keys()
            for param in sorted(parameter_dict.keys()):
                if param in search_space:
                    print("\t\t", param, "\t", parameter_dict[param])

    return
