suppressMessages(library(tsidx))
suppressMessages(library("optparse"))
suppressMessages(library("ExpressionSet"))
 
option_list = list(
    make_option(
        c("-f", "--file"), 
        type="character", 
        default=NULL, 
        help="path to expression matrix csv file", 
        metavar="character"
    ),
    make_option(
        c("-m", "--meta"), 
        type="character", 
        default=NULL, 
        help="path to meta csv file", 
        metavar="character"
    ),
    make_option(
        c("-c", "--column"), 
        type="character", 
        default=NULL, 
        help="dataset file name", 
        metavar="character"
    ),
    make_option(
        c("--markers"), 
        type="character", 
        default=NULL, 
        help="path to list of markers", 
        metavar="character"
    ),
    make_option(
        c("-t", "--tau"), 
        type="float", 
        default=0.9, 
        help="minimum tau value", 
        metavar="float"
    ),
    make_option(
        c("-o", "--out"), 
        type="character", 
        default="out", 
        help="output directory [default= %default]", 
        metavar="character"
    )
); 
 
opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);

if (is.null(opt$file)) {
    stop("-f, --file is required")
}

if (is.null(opt$meta)) {
    stop("-m, --meta if required")
}

expr <- read.csv(opt$file, row.names = 1)
meta <- read.csv(opt$meta, row.names = 1)

if (sum(!rownames(meta) %in% colnames(expr)) > 0) {
    stop("meta (rownames) and expr matrix (colnames) mismatch")
}

if (!opt$column %in% colnames(meta)) {
    stop(paste0(opt$column, " not presents in colnames of meta"))
}

if (length(unique(meta[opt$column])) < 2) {
    stop(paste0("at least two variables need in ", opt$column, "; now only: ", unique(meta[opt$column])))
}

markers = c()
if(!if.null(opt$markers)) {
    markers = read.table(opt$markers)
    markers = markers[, 1]
}

meta$CellType <- as.factor(meta[, opt$column])
meta$SampleID <- rownames(meta)


tsi <- tsDataSetFromMatrix(
    expr[, rownames(meta)], 
    meta, 
    ~ CellType, 
    type = "expression",
    convMethod = "log2",
    IbMethod = "mingap",
    mindiff = 3, 
    tidy = FALSE, 
    breaks = NULL,
    test = "Glm"
)
gc()

tau = as.data.frame(tsi@tsData$Tau)


write.csv(tau, paste(opt$out, "tau.csv", sep = "/"), quote = F)


temp_genes = rownames(tau)[tau$Tau > opt$tau]
if(nrow(markers) > 0) {
    temp_genes = unique(c(temp_genes, markers[, 1]))
}

temp_genes = temp_genes[temp_genes %in% rownames(expr)]

sc_set <- ExpressionSet(
    as.matrix(expr[as.character(temp_genes), ]), 
    phenoData = AnnotatedDataFrame(meta)
)

saveRDS(sc_set, paste(opt$out, "sc_set.rds", sep = "/"))

