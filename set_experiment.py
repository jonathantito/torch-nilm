from lab.nilm_experiments import *
from constants.constants import *
from constants.enumerates import *

experiment_parameters = {
    EPOCHS: 1,
    ITERATIONS: 1,
    INFERENCE_CPU: False,
    SAMPLE_PERIOD: 30,
    BATCH_SIZE: 256,
    ITERABLE_DATASET: False,
    PREPROCESSING_METHOD: SupportedPreprocessingMethods.MIDPOINT_WINDOW,
    FIXED_WINDOW: 128,
    SUBSEQ_WINDOW: 50,
    TRAIN_TEST_SPLIT: 0.8,
    CV_FOLDS: 2,
}

devices = [
    ElectricalAppliances.KETTLE,
    # ElectricalAppliances.MICROWAVE,
    # ElectricalAppliances.FRIDGE,
    # ElectricalAppliances.WASHING_MACHINE,
    # ElectricalAppliances.DISH_WASHER,
]

experiment_categories = [
    SupportedExperimentCategories.SINGLE_CATEGORY,
    # SupportedExperimentCategories.MULTI_CATEGORY
]

model_hparams = [
    # {
    #     'model_name': 'BERT',
    #     'hparams': {'window_size': None, 'n_layers': 1, 'heads': 1,
    #                 'hidden': 128, 'drop_out': 0.0},
    # },
    # {
    #     'model_name': 'VIBSeq2Point',
    #     'hparams': {'window_size': None, 'dropout': 0},
    # },
    # {
    #     'model_name': 'VAE',
    #     'hparams': {'window_size': None, 'cnn_dim': 256, 'kernel_size': 3, 'latent_dim': 16},
    # },
    # {
    #     'model_name': 'FNET',
    #     'hparams': {'depth': 1, 'kernel_size': 5, 'cnn_dim': 128, 'dual_cnn': False,
    #                 'input_dim': None, 'hidden_dim': 256, 'dropout': 0.0},
    # },
    # {
    #     'model_name': 'VIBFNET',
    #     'hparams': {'depth': 1, 'kernel_size': 5, 'cnn_dim': 128, 'dual_cnn': False,
    #                 'input_dim': None, 'hidden_dim': 256, 'dropout': 0.0},
    # },
    # {
    #     'model_name': 'DAE',
    #     'hparams': {'input_dim': None},
    # },
    {
        'model_name': 'SimpleGru',
        'hparams': {},
    },
    # {
    #     'model_name': 'SAED',
    #     'hparams': {'window_size': None},
    # },
    # {
    #     'model_name': 'WGRU',
    #     'hparams': {'dropout': 0},
    # },

]

hparam_tuning = [
    {
        'model_name': 'FNET',
        'hparams': [
            {'depth': 5, 'kernel_size': 5, 'cnn_dim': 128, 'dual_cnn': False,
             'input_dim': None, 'hidden_dim': 256, 'dropout': 0.0},
            {'depth': 3, 'kernel_size': 5, 'cnn_dim': 128, 'dual_cnn': False,
             'input_dim': None, 'hidden_dim': 256, 'dropout': 0.0},
            {'depth': 6, 'kernel_size': 5, 'cnn_dim': 128, 'dual_cnn': False,
             'input_dim': None, 'hidden_dim': 256, 'dropout': 0.0},
        ]
    },
    {
        'model_name': 'SAED',
        'hparams': [
            {'window_size': None, 'bidirectional': False, 'hidden_dim': 128},
            {'window_size': None, 'bidirectional': False, 'hidden_dim': 128, 'num_heads': 2},
            {'window_size': None, 'bidirectional': False, 'hidden_dim': 128, 'num_heads': 3},
        ]
    },
]

model_hparams = ModelHyperModelParameters(model_hparams)
hparam_tuning = HyperParameterTuning(hparam_tuning)
experiment_parameters = ExperimentParameters(**experiment_parameters)

experiment = NILMExperiments(project_name='test', clean_project=True,
                             devices=devices, save_timeseries_results=False, experiment_categories=experiment_categories,
                             experiment_volume=SupportedExperimentVolumes.SMALL_VOLUME,
                             experiment_parameters=experiment_parameters,
                             save_model=True,
                             )

# experiment.run_benchmark(model_hparams=model_hparams)
# experiment.export_report(model_hparams=model_hparams, experiment_type=SupportedNilmExperiments.BENCHMARK)
# experiment.run_cross_validation(model_hparams=model_hparams)
experiment.run_hyperparameter_tuning_cross_validation(hparam_tuning=hparam_tuning)
experiment.export_report(hparam_tuning=hparam_tuning, experiment_type=SupportedNilmExperiments.HYPERPARAM_TUNE_CV)
