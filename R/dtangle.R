
suppressMessages(library(dtangle))
suppressMessages(library("optparse"))
 

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

markers = rownames(sc_set@assayData$exprs)

res = dtangle(
    as.matrix(t(log2(bulk[rownames(bulk) %in% markers, ] + 1))), 
    references = as.matrix(t(log2(sc_set@assayData$exprs + 1))),
    markers = markers
)

tau_set = strsplit(basename(opt$scset), ".rds")[[1]]

saveRDS(
    res, 
    paste(opt$out, paste0("dtangle_",  tau_set, ".rds"), sep = "/")
)
write.csv(
    res$estimates, 
    paste(opt$out, paste0("dtangle_",  tau_set, ".rds"), sep = "/"), 
    quote = F
)

