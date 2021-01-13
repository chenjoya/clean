from os.path import join


class DatasetCatalog(object):
    DATA_DIR = "datasets"
    DATASETS = {
        "visr_train":{
            "data": "visr/frames/",    
            "label": "visr/annotations/train.json",
        },
    }

    @staticmethod
    def get(name):
        data_dir = DatasetCatalog.DATA_DIR
        if "vr" in name:
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                data=join(data_dir, attrs["data"]),
                label=join(data_dir, attrs["label"]),
            )
            return dict(
                factory="ViSR",
                args=args,
            )
        else:
            assert False, 'Unknown Dataset.'
        
