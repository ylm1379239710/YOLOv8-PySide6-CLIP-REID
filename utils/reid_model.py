import os
import torch
import torch.nn as nn
import torchvision.transforms as T
from clipreid.model.make_model_clipreid import make_model
from clipreid.config import cfg
import os.path as osp
import argparse

# 行人重识别模型类
class CLIPReIDModel:
    # ---------- 行人重识别模型初始化 --------------------------
    def __init__(self, config_dir, wight_dir):
        parser = argparse.ArgumentParser(description="ReID Baseline Training")
        if not osp.exists(wight_dir):
            raise IOError("{} does not exist".format(wight_dir))
        if not osp.exists(config_dir):
            raise IOError("{} does not exist".format(config_dir))
        else:
            parser.add_argument(
                "--config_file", default=config_dir, help="path to config file",
                type=str)
        args = parser.parse_args()
        if args.config_file != "":
            cfg.merge_from_file(args.config_file)
        cfg.freeze()

        self.cfg = cfg
        os.environ['CUDA_VISIBLE_DEVICES'] = cfg.MODEL.DEVICE_ID
        # train_loader, train_loader_normal, val_loader, num_query, num_classes, camera_num, view_num = make_dataloader(
        #     self.cfg)
        # self.target_img = val_loader
        self.model = make_model(cfg, 751, 1, 1)
        self.model.load_param(wight_dir)
        self.transform = T.Compose([
            T.Resize(self.cfg.INPUT.SIZE_TEST),
            T.ToTensor(),
            T.Normalize(mean=self.cfg.INPUT.PIXEL_MEAN, std=self.cfg.INPUT.PIXEL_STD)
        ])
        self.device = "cuda"
        if self.device:
            if torch.cuda.device_count() > 1:
                print('Using {} GPUs for inference'.format(torch.cuda.device_count()))
                self.model.model = nn.DataParallel(self.model)
        self.model.to(self.device)
        self.model.eval()
        # 待完善

    def extract_feature(self, img):
        with torch.no_grad():
            img = img.to(self.device)
            feat = self.model(img)
        return feat

    def match(self, query_feature, frame_feature):
        cosine_similarity = torch.nn.functional.cosine_similarity(query_feature, frame_feature)
        return cosine_similarity.item()
