# resize_image

PillowとOpenCVとTensorFlowのリサイズ結果を比較してみた。

## 結論

- cv2とTensorFlowのAREAは拡大ではNEAREST？
- cv2のLANCZOS4は縮小ではNEAREST？
- TensorFlowのlanczosは(元々float32で返ってくるが)clipせずuint8にキャストするとオーバーフローする事があるので要注意
- 混在はPILかTF(でちゃんと処理したもの)が一番綺麗そう？

## 実験結果

### 元画像 (`sklearn.datasets.load_sample_image("china.jpg")`)

![元画像](images/original.png)

### 縮小 (元画像 → 縮小(128x128))

| cv2 LANCZOS4                       | cv2 AREA                           | PIL NEAREST                        | PIL LANCZOS                        | tf lanc                           | tf  area                          |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | --------------------------------- | --------------------------------- |
| ![](images/reduction_cv2_lanc.png) | ![](images/reduction_cv2_area.png) | ![](images/reduction_pil_near.png) | ![](images/reduction_pil_lanc.png) | ![](images/reduction_tf_lanc.png) | ![](images/reduction_tf_area.png) |

### 拡大 (元画像 → 切り取り(32x32) → 拡大(128x128))

| cv2 LANCZOS4                           | cv2 AREA                               | PIL NEAREST                            | PIL LANCZOS                            | tf lanc                               | tf  area                              |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | ------------------------------------- | ------------------------------------- |
| ![](images/magnification_cv2_lanc.png) | ![](images/magnification_cv2_area.png) | ![](images/magnification_pil_near.png) | ![](images/magnification_pil_lanc.png) | ![](images/magnification_tf_lanc.png) | ![](images/magnification_tf_area.png) |

### 混在 (元画像 → 切り取り(512x32) → リサイズ(128x128))

| cv2 LANCZOS4                   | cv2 AREA                       | PIL NEAREST                    | PIL LANCZOS                    | tf lanc                       | tf  area                      |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ | ----------------------------- | ----------------------------- |
| ![](images/mixed_cv2_lanc.png) | ![](images/mixed_cv2_area.png) | ![](images/mixed_pil_near.png) | ![](images/mixed_pil_lanc.png) | ![](images/mixed_tf_lanc.png) | ![](images/mixed_tf_area.png) |
