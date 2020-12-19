suppressMessages(library(MuSiC))
suppressMessages(library("optparse"))
suppressMessages(library("Biobase"))
suppressMessages(library("xbioc"))
suppressMessages(library("reshape2"))

option_list = list(
    make_option(
        c("-f", "--file"), 
        type="character", 
        default=NULL, 
        help="path to expression matrix csv file", 
        metavar="character"
    ),
    make_option(
        c("-s", "--scset"), 
        type="character", 
        default=NULL, 
        help="path to sc set", 
        metavar="character"
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

sc_set = readRDS(opt$scset)
bulk <- read.csv(opt$file, row.names = 1)

temp = as.matrix(apply(bulk, 1, as.integer))
temp = t(temp)
colnames(temp) = colnames(bulk)
bulk = temp
rm(temp)
gc()

meta = data.frame(SampleID = colnames(bulk))
rownames(meta) <- meta$SampleID

bulk_set <- ExpressionSet(as.matrix(bulk), phenoData = AnnotatedDataFrame(meta))

bulk_dec = music_prop(
    bulk.eset = bulk_set, 
    sc.eset = sc_set, 
    clusters = "CellType",
    samples = "SampleID", 
    markers = rownames(sc_set@assayData$exprs),
    verbose = F
)

tau_set = strsplit(basename(opt$scset), ".rds")[[1]]

saveRDS(
    bulk_dec, 
    paste(opt$out, paste0("music_",  tau_set, ".rds"), sep = "/")
)
write.csv(
    bulk_dec$Est.prop.weighted, 
    paste(opt$out, paste0("music_",  tau_set, ".csv"), sep = "/"), 
    quote = F
)