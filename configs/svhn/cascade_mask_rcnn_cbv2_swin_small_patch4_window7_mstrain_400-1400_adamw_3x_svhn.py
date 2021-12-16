# The new config inherits a base config to highlight the necessary modification
_base_ = '../cbnet/cascade_mask_rcnn_cbv2_swin_small_patch4_window7_mstrain_400-1400_adamw_3x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
"""
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=10),
        mask_head=dict(num_classes=10)))
"""
# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('0','1','2','3','4','5','6','7','8','9',)
"""
data = dict(
    imgs_per_gpu=1,
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
load_from = 'checkpoints/cascade_mask_rcnn_cbv2_swin_small_patch4_window7_mstrain_400-1400_adamw_3x_coco.pth'
