import yaml

dataset = "LibriTTS"  # [LibriTTS, VCTK, LJSpeech]
mfa_path = "./MFA"

### Text ###
# g2p_en
text_cleaners = ["english_cleaners"]

n_mel_channels = 80
prosody_conv_layer= 3
prosody_conv_filter_size = 1024
prosody_conv_kernel_size = 3
prosody_dropout = 0.1
prosody_encoder_layer = 4
prosody_encoder_head = 8
prosody_encoder_hidden = 128

transformer_conv_layer= 3
transformer_conv_filter_size = 1024
transformer_conv_kernel_size = 3
transformer_dropout = 0.1
transformer_encoder_layer = 4
transformer_encoder_head = 2
transformer_encoder_hidden = 128
transformer_decoder_layer = 6
transformer_decoder_head = 2
transformer_decoder_hidden = 128

prosody_predictor_filter_size = 128
prosody_predictor_kernel_size = 3
prosody_predictor_dropout = 0.1


encoder_layer = 4
encoder_head = 2
encoder_hidden = 128

decoder_layer = 4
decoder_head = 2
decoder_hidden = 128

fft_conv1d_filter_size = 1024
fft_conv1d_kernel_size = (9, 1)

encoder_dropout = 0.2
decoder_dropout = 0.2

variance_predictor_filter_size = 128
variance_predictor_kernel_size = 3
variance_predictor_dropout = 0.5

max_seq_len = 1150
min_seq_len = 20

### dataset ###
with open("./dataset.yaml", "r") as f:
    dataset_config = yaml.load(f, Loader=yaml.FullLoader)

    # Audio and mel
    sampling_rate = dataset_config[dataset]["sampling_rate"]
    n_fft = dataset_config[dataset]["n_fft"]
    hop_length = dataset_config[dataset]["hop_length"]
    win_length = dataset_config[dataset]["win_length"]
    n_mels = dataset_config[dataset]["n_mels"]
    mel_fmin = dataset_config[dataset]["mel_fmin"]
    mel_fmax = dataset_config[dataset]["mel_fmax"]


    # Quantization for F0 and energy
    f0_min = dataset_config[dataset]["f0_min"]
    f0_max = dataset_config[dataset]["f0_max"]
    energy_min = dataset_config[dataset]["energy_min"]
    energy_max = dataset_config[dataset]["energy_max"]
    n_bins = 256

    # Speaker embedding
    use_spk_embed = dataset_config[dataset]["use_spk_embed"]
spk_embed_dim = 256
spk_embed_weight_std = 0.01

### Optimizer ###
batch_size = 32
n_warm_up_step = 4000
grad_clip_thresh = 1.0
acc_steps = 1

betas = (0.9, 0.98)
eps = 1e-9
weight_decay = 0.0

total_steps = 2

# Vocoder
vocoder = "melgan"

# Log-scaled duration
log_offset = 1.0
log_duration = True
# Save, log and synthesis
save_step = 10000
eval_step = save_step
log_step = 1000
