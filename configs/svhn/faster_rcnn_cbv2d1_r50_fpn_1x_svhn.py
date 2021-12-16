# The new config inherits a base config to highlight the necessary modification
_base_ = '../faster_rcnn/faster_rcnn_r101_fpn_2x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation


# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('0','1','2','3','4','5','6','7','8','9')
data = dict(
    train=dict(
        img_prefix='dataset/train/train/',
        classes=classes,
        ann_file='dataset/train/train/valdigitStruct.json'),
    val=dict(
        img_prefix='dataset/train/train/',
        classes=classes,
        ann_file='dataset/train/train/valdigitStruct.json'),
    test=dict(
        img_prefix='dataset/test/test/',
        classes=classes,
        ann_file='dataset/test/test/littletestImgitStruct.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/faster_rcnn_r101_fpn_2x_coco_bbox_mAP-0.398_20200504_210455-1d2dac9c.pth'
fp16 = dict(loss_scale=512.)