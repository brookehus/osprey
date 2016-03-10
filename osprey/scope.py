import sklearn
try:
    import msmbuilder
    import msmbuilder.cluster
    import msmbuilder.decomposition
    import msmbuilder.lumping
    import msmbuilder.featurizer
    import msmbuilder.msm

    _SCOPE_ = {'AffinityPropagation':
               msmbuilder.cluster.AffinityPropagation,
               'AgglomerativeClustering':
               msmbuilder.cluster.AgglomerativeClustering,
               'AlphaAngleFeaturizer':
               msmbuilder.featurizer.featurizer.AlphaAngleFeaturizer,
               'AtomPairsFeaturizer':
               msmbuilder.featurizer.featurizer.AtomPairsFeaturizer,
               'BaseEstimator':
               msmbuilder.base.BaseEstimator,
               'BaseSubsetFeaturizer':
               msmbuilder.featurizer.subset_featurizer.BaseSubsetFeaturizer,
               'BayesianContinuousTimeMSM':
               msmbuilder.msm.bayes_ratematrix.BayesianContinuousTimeMSM,
               'BayesianMarkovStateModel':
               msmbuilder.msm.bayesmsm.BayesianMarkovStateModel,
               'ContactFeaturizer':
               msmbuilder.featurizer.featurizer.ContactFeaturizer,
               'ContinuousTimeMSM':
               msmbuilder.msm.ratematrix.ContinuousTimeMSM,
               'DRIDFeaturizer':
               msmbuilder.featurizer.featurizer.DRIDFeaturizer,
               'DihedralFeaturizer':
               msmbuilder.featurizer.featurizer.DihedralFeaturizer,
               'FeatureUnion':
               msmbuilder.featurizer.feature_union.FeatureUnion,
               'Featurizer':
               msmbuilder.featurizer.featurizer.Featurizer,
               'FirstSlicer':
               msmbuilder.featurizer.featurizer.FirstSlicer,
               'FunctionFeaturizer':
               msmbuilder.featurizer.featurizer.FunctionFeaturizer,
               'GMM':
               msmbuilder.cluster.GMM,
               'GaussianSolventFeaturizer':
               msmbuilder.featurizer.featurizer.GaussianSolventFeaturizer,
               'KCenters':
               msmbuilder.cluster.kcenters.KCenters,
               'KMeans':
               msmbuilder.cluster.KMeans,
               'KMedoids':
               msmbuilder.cluster.kmedoids.KMedoids,
               'KappaAngleFeaturizer':
               msmbuilder.featurizer.featurizer.KappaAngleFeaturizer,
               'LandmarkAgglomerative':
               msmbuilder.cluster.agglomerative.LandmarkAgglomerative,
               'MarkovStateModel':
               msmbuilder.msm.msm.MarkovStateModel,
               'MeanShift':
               msmbuilder.cluster.MeanShift,
               'MiniBatchKMeans':
               msmbuilder.cluster.MiniBatchKMeans,
               'MiniBatchKMedoids':
               msmbuilder.cluster.minibatchkmedoids.MiniBatchKMedoids,
               'MultiSequenceDecompositionMixin':
               msmbuilder.decomposition.base.MultiSequenceDecompositionMixin,
               'NDGrid':
               msmbuilder.cluster.ndgrid.NDGrid,
               'PCA':
               msmbuilder.decomposition.pca.PCA,
               'PCCA':
               msmbuilder.lumping.pcca.PCCA,
               'PCCAPlus':
               msmbuilder.lumping.pcca_plus.PCCAPlus,
               'Pipeline':
               sklearn.pipeline.Pipeline,
               'RMSDFeaturizer':
               msmbuilder.featurizer.featurizer.RMSDFeaturizer,
               'RawPositionsFeaturizer':
               msmbuilder.featurizer.featurizer.RawPositionsFeaturizer,
               'RegularSpatial':
               msmbuilder.cluster.regularspatial.RegularSpatial,
               'SASAFeaturizer':
               msmbuilder.featurizer.featurizer.SASAFeaturizer,
               'Slicer':
               msmbuilder.featurizer.featurizer.Slicer,
               'SparseTICA':
               msmbuilder.decomposition.sparsetica.SparseTICA,
               'SpectralClustering':
               msmbuilder.cluster.SpectralClustering,
               'StrucRMSDFeaturizer':
               msmbuilder.featurizer.featurizer.StrucRMSDFeaturizer,
               'Subsampler':
               msmbuilder.utils.subsampler.Subsampler,
               'SubsetAtomPairs':
               msmbuilder.featurizer.subset_featurizer.SubsetAtomPairs,
               'SubsetCosPhiFeaturizer':
               msmbuilder.featurizer.subset_featurizer.SubsetCosPhiFeaturizer,
               'SubsetCosPsiFeaturizer':
               msmbuilder.featurizer.subset_featurizer.SubsetCosPsiFeaturizer,
               'SubsetFeatureUnion':
               msmbuilder.featurizer.subset_featurizer.SubsetFeatureUnion,
               'SubsetSinPhiFeaturizer':
               msmbuilder.featurizer.subset_featurizer.SubsetSinPhiFeaturizer,
               'SubsetSinPsiFeaturizer':
               msmbuilder.featurizer.subset_featurizer.SubsetSinPsiFeaturizer,
               'SubsetTrigFeaturizer':
               msmbuilder.featurizer.subset_featurizer.SubsetTrigFeaturizer,
               'SuperposeFeaturizer':
               msmbuilder.featurizer.featurizer.SuperposeFeaturizer,
               'TrajFeatureUnion':
               msmbuilder.featurizer.featurizer.TrajFeatureUnion,
               'Ward':
               msmbuilder.cluster.Ward,
               'tICA':
               msmbuilder.decomposition.tica.tICA
               }
except ImportError:
    _SCOPE_ = {}
