
##########################################################
##                                                      ##
## Creates a trimmed csv file with hyperparameters      ##
##                                                      ##
## How to run:                                          ##
##                                                      ##
## Copy csv_trim.R to working directory                 ##
## Edit IN_DOC  <- name of csv file from osprey dump    ##
## Edit OUT_DOC <- name of new trimmed csv file         ##
## >>> R < ./csv_trim.R --no-save                       ##
##                                                      ##
##########################################################


IN_DOC = 'OSPREY_OUTPUT.CSV'
OUT_DOC = 'TRIMMED_OSPREY_OUTPUT.CSV'

csv_raw <- read.csv(IN_DOC)
d <- dim(csv_raw)[1]
l <- length(unlist(strsplit(as.character(csv_raw[1,4]),',')))
parameters_raw <- matrix(nrow=d, ncol=l)
for(i in 1:d){
	parameters_raw[i,] <- unlist(strsplit(as.character(csv_raw[i,4]),','))
}

param_labels <- c('n_timescales', 'msm__lag_time', 'tica__lag_time',
	'tica__n_components', 'tica__gammma', 'cluster__n_clusters')

param_trix <- matrix(nrow=d, ncol=length(param_labels))
colnames(param_trix) <- param_labels
tail <- length(unlist(strsplit(parameters_raw[i,1], ':')))

for(i in 1:d){
	# n_timescales
	param_trix[i,1] <- unlist(strsplit(parameters_raw[i,9], ':'))[tail]
	# msm__lag_time
	param_trix[i,2] <- unlist(strsplit(parameters_raw[i,19], ':'))[tail]
    # tica__lag_time
    temp <- unlist(strsplit(parameters_raw[i,23], ':'))[tail]
    param_trix[i,3] <- unlist(strsplit(temp,'}'))
	# tica__n_components
	param_trix[i,4] <- unlist(strsplit(parameters_raw[i,20], ':'))[tail]
	# tica__gamma
	param_trix[i,5] <- unlist(strsplit(parameters_raw[i,14], ':'))[tail]
	# cluster__n_clusters
	param_trix[i,6] <- unlist(strsplit(parameters_raw[i,22], ':'))[tail]
}

new_labels <- c('mean_test_score', 'mean_train_score', param_labels)
new_trix <- matrix(nrow=d, ncol=length(new_labels))
colnames(new_trix) <- new_labels
for(i in 1:d){
	# mean test score
	new_trix[i,1] <- csv_raw[i,5]
	# mean train score
	new_trix[i,2] <- csv_raw[i,6]
	# hyperparameters
	new_trix[i,3:8] <- param_trix[i,]
}

write.csv(new_trix, OUT_DOC)
closeAllConnections()
