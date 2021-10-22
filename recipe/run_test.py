import subprocess
import sys

def check_outputs(bins):
    for bin_name in bins.split():
        print(f'Testing {bin_name}')
        p = subprocess.run([bin_name, '--help'], capture_output=True, text=True)
        if p.returncode == 1 and p.stderr and 'cuda' not in bin_name:
            print(f"{bin_name} had an error:")
            sys.exit(1)

openfst_bins="""fstarcsort 
fstclosure 
fstcompile 
fstcompose 
fstconcat 
fstconnect 
fstconvert 
fstdeterminize
fstdifference 
fstdisambiguate 
fstdraw 
fstencode 
fstepsnormalize 
fstequal 
fstequivalent
fstinfo 
fstintersect 
fstinvert 
fstisomorphic 
fstmap 
fstminimize 
fstprint 
fstproject 
fstprune
fstpush 
fstrandgen 
fstrelabel 
fstreplace 
fstreverse 
fstreweight 
fstrmepsilon 
fstshortestdistance
fstshortestpath 
fstsymbols 
fstsynchronize 
fsttopsort
fstunion"""

bins="""align-equal align-equal-compiled acc-tree-stats
        show-alignments compile-questions cluster-phones
        compute-wer compute-wer-bootci make-h-transducer
        add-self-loops convert-ali
        compile-train-graphs compile-train-graphs-fsts
        make-pdf-to-tid-transducer make-ilabel-transducer show-transitions
        ali-to-phones ali-to-post weight-silence-post acc-lda est-lda
        ali-to-pdf est-mllt build-tree build-tree-two-level decode-faster
        decode-faster-mapped vector-scale copy-transition-model
        phones-to-prons prons-to-wordali copy-gselect copy-tree scale-post
        post-to-weights sum-tree-stats weight-post post-to-tacc copy-matrix
        copy-vector copy-int-vector sum-post sum-matrices draw-tree
        align-mapped align-compiled-mapped latgen-faster-mapped latgen-faster-mapped-parallel
        hmm-info analyze-counts post-to-phone-post
        post-to-pdf-post logprob-to-post prob-to-post copy-post
        matrix-sum matrix-max build-pfile-from-ali get-post-on-ali tree-info am-info
        vector-sum matrix-sum-rows est-pca sum-lda-accs sum-mllt-accs
        transform-vec align-text matrix-dim post-to-smat compile-graph
        compare-int-vector latgen-incremental-mapped
        compute-gop compile-train-graphs-without-lexicon"""

chain_bins="""chain-est-phone-lm chain-get-supervision chain-make-den-fst
        nnet3-chain-get-egs nnet3-chain-copy-egs nnet3-chain-merge-egs
        nnet3-chain-shuffle-egs nnet3-chain-subset-egs
        nnet3-chain-acc-lda-stats nnet3-chain-train nnet3-chain-compute-prob
        nnet3-chain-combine nnet3-chain-normalize-egs
        nnet3-chain-e2e-get-egs nnet3-chain-compute-post
        chain-make-num-fst-e2e
		nnet3-chain-train2 nnet3-chain-combine2"""


feat_bins="""add-deltas add-deltas-sdc append-post-to-feats
           append-vector-to-feats apply-cmvn apply-cmvn-sliding compare-feats
           compose-transforms compute-and-process-kaldi-pitch-feats
           compute-cmvn-stats compute-cmvn-stats-two-channel
           compute-fbank-feats compute-kaldi-pitch-feats compute-mfcc-feats
           compute-plp-feats compute-spectrogram-feats concat-feats copy-feats
           copy-feats-to-htk copy-feats-to-sphinx extend-transform-dim
           extract-feature-segments extract-segments feat-to-dim
           feat-to-len fmpe-acc-stats fmpe-apply-transform fmpe-est
           fmpe-init fmpe-sum-accs get-full-lda-mat interpolate-pitch
           modify-cmvn-stats paste-feats post-to-feats
           process-kaldi-pitch-feats process-pitch-feats
           select-feats shift-feats splice-feats subsample-feats
           subset-feats transform-feats wav-copy wav-reverberate
           wav-to-duration multiply-vectors paste-vectors"""


fgmm_bins="""fgmm-global-acc-stats fgmm-global-sum-accs fgmm-global-est
           fgmm-global-merge fgmm-global-to-gmm fgmm-gselect fgmm-global-get-frame-likes
           fgmm-global-copy fgmm-global-gselect-to-post fgmm-global-info
           fgmm-global-acc-stats-post fgmm-global-init-from-accs"""


fst_bins="""fstdeterminizestar
           fstrmsymbols fstisstochastic fstminimizeencoded fstmakecontextfst
           fstmakecontextsyms fstaddsubsequentialloop fstaddselfloops
           fstrmepslocal fstcomposecontext fsttablecompose fstrand
           fstdeterminizelog fstphicompose fstcopy
           fstpushspecial fsts-to-transcripts fsts-project fsts-union
           fsts-concat make-grammar-fst"""


gmm_bins="""gmm-init-mono gmm-est gmm-acc-stats-ali gmm-align
           gmm-decode-faster gmm-decode-simple gmm-align-compiled
           gmm-sum-accs gmm-est-regtree-fmllr gmm-acc-stats-twofeats
           gmm-acc-stats gmm-init-lvtln gmm-est-lvtln-trans gmm-train-lvtln-special
           gmm-acc-mllt gmm-mixup gmm-init-model gmm-transform-means
           gmm-make-regtree gmm-decode-faster-regtree-fmllr gmm-post-to-gpost
           gmm-est-fmllr-gpost gmm-est-fmllr gmm-est-regtree-fmllr-ali
           gmm-est-regtree-mllr gmm-compute-likes
           gmm-decode-faster-regtree-mllr gmm-latgen-simple
           gmm-rescore-lattice gmm-decode-biglm-faster
           gmm-est-gaussians-ebw gmm-est-weights-ebw gmm-latgen-faster gmm-copy
           gmm-global-acc-stats gmm-global-est gmm-global-sum-accs gmm-gselect
           gmm-latgen-biglm-faster gmm-ismooth-stats gmm-global-get-frame-likes
           gmm-global-est-fmllr gmm-global-to-fgmm gmm-global-acc-stats-twofeats
           gmm-global-copy gmm-fmpe-acc-stats gmm-acc-stats2 gmm-init-model-flat gmm-info
           gmm-get-stats-deriv gmm-est-rescale gmm-boost-silence
           gmm-basis-fmllr-accs gmm-basis-fmllr-training gmm-est-basis-fmllr
           gmm-est-map gmm-adapt-map gmm-latgen-map gmm-basis-fmllr-accs-gpost
           gmm-est-basis-fmllr-gpost gmm-latgen-faster-parallel
           gmm-est-fmllr-raw gmm-est-fmllr-raw-gpost gmm-global-init-from-feats
           gmm-global-info gmm-latgen-faster-regtree-fmllr gmm-est-fmllr-global
           gmm-acc-mllt-global gmm-transform-means-global gmm-global-get-post
           gmm-global-gselect-to-post gmm-global-est-lvtln-trans gmm-init-biphone"""



ivector_bins="""ivector-extractor-init ivector-extractor-copy ivector-extractor-acc-stats
           ivector-extractor-sum-accs ivector-extractor-est
           ivector-extract compute-vad select-voiced-frames
           compute-vad-from-frame-likes merge-vads
           ivector-normalize-length
           ivector-transform ivector-compute-dot-products ivector-mean
           ivector-compute-lda ivector-compute-plda
           ivector-copy-plda compute-eer
           ivector-subtract-global-mean ivector-plda-scoring
           logistic-regression-train logistic-regression-eval
           logistic-regression-copy ivector-extract-online
           ivector-adapt-plda ivector-plda-scoring-dense
           agglomerative-cluster"""



kws_bins="""lattice-to-kws-index kws-index-union transcripts-to-fsts
		   kws-search generate-proxy-keywords compute-atwv print-proxy-keywords"""


lat_bins="""lattice-best-path lattice-prune lattice-equivalent lattice-to-nbest
           lattice-lmrescore lattice-scale lattice-union lattice-to-post
           lattice-determinize lattice-oracle lattice-rmali
           lattice-compose lattice-boost-ali lattice-copy lattice-to-fst
           lattice-to-phone-lattice lattice-interp lattice-project
           lattice-add-trans-probs lattice-difference
           nbest-to-linear nbest-to-lattice lattice-1best linear-to-nbest
           lattice-mbr-decode lattice-align-words lattice-to-mpe-post
           lattice-copy-backoff nbest-to-ctm lattice-determinize-pruned
           lattice-to-ctm-conf lattice-combine
           lattice-rescore-mapped lattice-depth lattice-align-phones
           lattice-to-smbr-post lattice-determinize-pruned-parallel
           lattice-add-penalty lattice-align-words-lexicon lattice-push
           lattice-minimize lattice-limit-depth lattice-depth-per-frame
           lattice-confidence lattice-determinize-phone-pruned
           lattice-determinize-phone-pruned-parallel lattice-expand-ngram
           lattice-lmrescore-const-arpa lattice-lmrescore-rnnlm nbest-to-prons
           lattice-arc-post lattice-determinize-non-compact lattice-lmrescore-kaldi-rnnlm
           lattice-lmrescore-pruned lattice-lmrescore-kaldi-rnnlm-pruned lattice-reverse
		   lattice-expand lattice-path-cover lattice-add-nnlmscore"""


lm_bins="""arpa2fst arpa-to-const-arpa"""


nnet_bins="""nnet-train-frmshuff
        nnet-train-perutt
        nnet-train-mmi-sequential
        nnet-train-mpe-sequential
        nnet-train-multistream nnet-train-multistream-perutt
        rbm-train-cd1-frmshuff rbm-convert-to-nnet
        nnet-forward nnet-copy nnet-info nnet-concat
        transf-to-nnet cmvn-to-nnet nnet-initialize
	feat-to-post paste-post train-transitions
	nnet-set-learnrate"""

nnet2_bins="""nnet-am-info nnet-init
   nnet-train-simple nnet-train-ensemble nnet-train-transitions nnet-latgen-faster nnet-am-copy
   nnet-am-init nnet-insert nnet-align-compiled
   nnet-compute-prob nnet-copy-egs nnet-combine
   nnet-am-average nnet-am-compute nnet-am-mixup
   nnet-get-egs nnet-train-parallel nnet-combine-fast
   nnet-subset-egs nnet-shuffle-egs nnet-am-fix
   nnet-latgen-faster-parallel nnet-to-raw-nnet nnet-compute
   raw-nnet-concat raw-nnet-info
   nnet-get-feature-transform nnet-compute-from-egs
   nnet-am-widen nnet-show-progress
   nnet-get-feature-transform-multi nnet-copy-egs-discriminative
   nnet-get-egs-discriminative nnet-shuffle-egs-discriminative
   nnet-compare-hash-discriminative nnet-combine-egs-discriminative
   nnet-train-discriminative-simple nnet-train-discriminative-parallel
   nnet-modify-learning-rates nnet-normalize-stddev
   nnet-get-weighted-egs nnet-adjust-priors
   nnet-replace-last-layers nnet-am-switch-preconditioning
   nnet1-to-raw-nnet raw-nnet-copy nnet-relabel-egs nnet-am-reinitialize"""



nnet3_bins="""nnet3-init nnet3-info nnet3-get-egs nnet3-copy-egs nnet3-subset-egs
   nnet3-shuffle-egs nnet3-acc-lda-stats nnet3-merge-egs
   nnet3-compute-from-egs nnet3-train nnet3-am-init nnet3-am-train-transitions
   nnet3-am-adjust-priors nnet3-am-copy nnet3-compute-prob
   nnet3-average nnet3-am-info nnet3-combine nnet3-latgen-faster
   nnet3-latgen-faster-parallel nnet3-show-progress nnet3-align-compiled
   nnet3-copy nnet3-get-egs-dense-targets nnet3-compute
   nnet3-discriminative-get-egs nnet3-discriminative-copy-egs
   nnet3-discriminative-merge-egs nnet3-discriminative-shuffle-egs
   nnet3-discriminative-compute-objf nnet3-discriminative-train
   nnet3-discriminative-subset-egs nnet3-get-egs-simple
   nnet3-discriminative-compute-from-egs nnet3-latgen-faster-looped
   nnet3-egs-augment-image nnet3-xvector-get-egs nnet3-xvector-compute
   nnet3-xvector-compute-batched
   nnet3-latgen-grammar nnet3-compute-batch nnet3-latgen-faster-batch
   nnet3-latgen-faster-lookahead cuda-gpu-available cuda-compiled"""

rnnlm_bins="""rnnlm-get-egs rnnlm-train rnnlm-get-sampling-lm
           rnnlm-get-word-embedding rnnlm-compute-prob rnnlm-sentence-probs"""



sgmm2_bins="""sgmm2-init sgmm2-gselect sgmm2-acc-stats sgmm2-est sgmm2-sum-accs
         sgmm2-align-compiled sgmm2-est-spkvecs sgmm2-post-to-gpost
         sgmm2-acc-stats-gpost sgmm2-latgen-faster sgmm2-est-spkvecs-gpost
         sgmm2-rescore-lattice sgmm2-copy sgmm2-info sgmm2-est-ebw
         sgmm2-acc-stats2 sgmm2-comp-prexform sgmm2-est-fmllr sgmm2-project
         sgmm2-latgen-faster-parallel init-ubm"""



online_bins="""online-net-client online-server-gmm-decode-faster online-gmm-decode-faster
           online-wav-gmm-decode-faster online-audio-server-decode-faster
           online-audio-client"""



online2_bins="""online2-wav-gmm-latgen-faster apply-cmvn-online
     extend-wav-with-silence compress-uncompress-speex
     online2-wav-nnet2-latgen-faster ivector-extract-online2
     online2-wav-dump-features ivector-randomize
     online2-wav-nnet2-am-compute  online2-wav-nnet2-latgen-threaded
     online2-wav-nnet3-latgen-faster online2-wav-nnet3-latgen-grammar
     online2-tcp-nnet3-decode-faster online2-wav-nnet3-latgen-incremental
     online2-wav-nnet3-wake-word-decoder-faster"""


if __name__ == '__main__':
    check_outputs(openfst_bins)
    check_outputs(bins)
    check_outputs(chain_bins)
    check_outputs(feat_bins)
    check_outputs(fst_bins)
    check_outputs(fgmm_bins)
    check_outputs(gmm_bins)
    check_outputs(ivector_bins)
    check_outputs(kws_bins)
    check_outputs(lat_bins)
    check_outputs(lm_bins)
    check_outputs(nnet_bins)
    check_outputs(nnet2_bins)
    check_outputs(nnet3_bins)
    check_outputs(rnnlm_bins)
    check_outputs(sgmm2_bins)

    if sys.platform != 'win32':
        check_outputs(online_bins)
        check_outputs(online2_bins)