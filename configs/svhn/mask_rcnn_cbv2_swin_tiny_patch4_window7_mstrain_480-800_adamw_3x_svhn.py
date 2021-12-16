# The new config inherits a base config to highlight the necessary modification
_base_ = '../cbnet/mask_rcnn_cbv2_swin_tiny_patch4_window7_mstrain_480-800_adamw_3x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('0','1','2','3','4','5','6','7','8','9',)
"""
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
        ann_file='dataset/test/test/testImgitStruct.json'))
"""
# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/mask_rcnn_cbv2_swin_tiny_patch4_window7_mstrain_480-800_adamw_3x_coco.pth'
