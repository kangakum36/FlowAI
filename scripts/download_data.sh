cd ..
if [ -d "./data/FlowCasesDeidentify120519" ] 
then
    rm -r ./data/FlowCasesDeidentify120519
fi
gsutil -m cp -r gs://flowai-data/FlowCasesDeidentify120519 ./data/