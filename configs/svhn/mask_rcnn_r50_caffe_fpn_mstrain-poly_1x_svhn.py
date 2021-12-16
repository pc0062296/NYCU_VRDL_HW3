# The new config inherits a base config to highlight the necessary modification
_base_ = '../mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=10),
        mask_head=dict(num_classes=10)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('0','1','2','3','4','5','6','7','8','9')
data = dict(
    train=dict(
        img_prefix='dataset/train/train/',
        classes=classes,
        ann_file='dataset/train/train/traindigitStruct.json'),
    val=dict(
        img_prefix='dataset/train/train/',
        classes=classes,
        ann_file='dataset/train/train/valdigitStruct.json'),
    test=dict(
        img_prefix='dataset/test/test/',
        classes=classes,
        ann_file='dataset/test/test/littletestImgitStruct.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'
