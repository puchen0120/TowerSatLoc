# TowerSatLocGUI

This folder is the packaged desktop release of **TowerSatLoc**.  
You can run the software directly from this folder without the source-code project.

## How to Run

1. Keep the whole `TowerSatLocGUI` folder structure unchanged.
2. Double-click:

   `TowerSatLocGUI.exe`

3. Do **not** move the `.exe` out of this folder by itself, because it depends on:
   - `_internal/`
   - `weights/`
   - runtime resource files generated during packaging

## Folder Notes

- `input/`
  - Put input data here.
- `output/`
  - Results will be written here automatically.
- `weights/`
  - Stores required local model weights.

## Main Functions

- `TowerSatLoc`
  - Match tower surveillance imagery with satellite imagery.
- `InitOriEst`
  - Estimate and refine initial orientation parameters.
- `Mapping`
  - Generate georeferenced tower-image TIFF layers after matching.

## Recommended Delivery Method

If you want to share this software with others, package and send the **entire**
`dist/TowerSatLocGUI` folder.

Recommended:

1. Compress the whole `TowerSatLocGUI` folder into a `.zip` file.
2. Send the compressed file.
3. The recipient extracts it and runs `TowerSatLocGUI.exe`.

## Citation

If you use this software in research, please cite:

```bibtex
@article{chen2026bridging,
  title={Bridging extreme viewpoint gap: Robust cross-domain matching of tower surveillance and satellite images for precise geolocation},
  author={Chen, Pu and Liu, Yuxuan and Zhang, Li and Hu, Zhihua and Lu, Linjun and Besklubova, Svetlana and Zhang, Xueping and Brilakis, Ioannis},
  journal={IEEE Transactions on Geoscience and Remote Sensing},
  year={2026},
  publisher={IEEE}
}
```

## Acknowledgement

The algorithm of this software is developed based on **RoMa** as a foundational matching component.  
We gratefully acknowledge the RoMa project and its contributors:

- RoMa GitHub: [Parskatt/RoMa](https://github.com/Parskatt/RoMa)

## Notes

- Keep the folder structure unchanged for stable execution.
- If the software cannot find input data, place files into the corresponding `input/` subfolders and run again.
- The packaged version already includes the required runtime resources for execution in this folder.
