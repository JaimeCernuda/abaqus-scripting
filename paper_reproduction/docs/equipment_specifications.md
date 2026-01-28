# Lab Equipment Specifications

Technical specifications for the materials science workflow equipment.

---

## 1. Introduction

### Document Purpose

This document provides comprehensive technical specifications for all lab equipment used in the materials science workflow. It serves as a quick reference for operational limits, dimensional constraints, and capabilities when designing experiments or specimens.

### Lab Workflow Overview

The workflow consists of four main stages:

1. **Part Manufacturing** - Additive manufacturing via GE Additive M2 Series 5 (Protolabs)
2. **Mechanical Testing** - MTS 370.02 load frame with Epsilon extensometer
3. **Void Volume Analysis** - Zeiss Xradia 620 Versa X-ray CT
4. **Surface Roughness** - Keyence VHX-7000 and Zygo ZeGage Pro

---

## 2. Manufacturing Equipment

### 2.1 GE Additive M2 Series 5

Direct Metal Laser Melting (DMLM) system for metal powder bed fusion, operated by Protolabs.

| Parameter | Specification |
|-----------|---------------|
| **Build Volume** | 245 x 245 x 350 mm (X, Y, Z) |
| **Laser Configuration** | Dual laser: 2x 400W or 2x 1kW fiber laser (cw) |
| **Layer Thickness** | 25 - 120 μm |
| **Scan Speed** | Max 4.5 m/s |
| **Spot Size** | 70 - 500 μm (variable focus) |
| **Laser Coverage** | 100% overlap per laser (full build field) |
| **Technology** | Direct Metal Laser Melting (DMLM) / Laser PBF |

#### Material Compatibility

- Stainless steel (316L, 17-4PH)
- Tool steels
- Nickel alloys (Inconel 625, 718)
- Titanium alloys (Ti-6Al-4V)
- Aluminum alloys (AlSi10Mg)
- Cobalt-chrome

#### Design Considerations

- Minimum feature size: ~0.4 mm (dependent on orientation)
- Minimum wall thickness: 0.5 mm
- Support structures required for overhangs >45°
- Surface roughness as-built: Ra 5-15 μm (orientation dependent)

#### Notes

- Located at Protolabs (service bureau)
- Designed for aerospace and medical regulated industries
- 2x build speed vs. previous M2 models due to dual laser configuration

---

## 3. Mechanical Testing Equipment

### 3.1 MTS 370.02 Axial-Torsion Servohydraulic Load Frame

Two-column servohydraulic frame for combined axial and torsional testing.

| Parameter | Specification |
|-----------|---------------|
| **Axial Force Capacity** | 25 kN (5.5 kip) |
| **Torsional Capacity** | 250 Nm |
| **Torque Rating** | ±100 N-m (885 in-lbf) |
| **Actuator Stroke (Torsional)** | ±135 degrees |
| **Frame Type** | 2-column, cylinder-centric design |
| **Distance Between Columns** | 457 mm (18 in) |
| **Max Specimen Length** | 813 mm (32 in) less tooling |
| **Hydraulic Pressure** | 14 MPa (2000 psi) |
| **Hydraulic Flow** | 15 l/min |

#### Loading Modes

- Static and quasi-static
- Dynamic and cyclic
- Dwell fatigue
- Combined axial-torsional (biaxial)
- Tension, compression, torsion, and fatigue

#### Capabilities

- 2D yield surface examination
- Multiaxial fatigue testing
- Compatible with 3D DIC for full-field strain measurement
- Environmental chamber compatible

---

### 3.2 Epsilon 3442-003M-020-ST Extensometer

Miniature dual-flexure extensometer for small specimens.

| Parameter | Specification |
|-----------|---------------|
| **Gauge Length** | 3 mm |
| **Measuring Range** | ±2.0 mm |
| **Strain Range** | +20% / -10% |
| **Temperature Range (Standard)** | -40°C to +100°C |
| **Temperature Range (LHT Option)** | -270°C to +200°C |
| **Weight** | ~8 grams |
| **Module Height** | 15.2 mm (0.6 in) |
| **Bridge Configuration** | Full bridge, 350 ohm strain gage |

#### Specimen Compatibility

| Specimen Type | Dimension Range |
|---------------|-----------------|
| **Round Specimens** | 0.5 - 13 mm diameter |
| **Flat Specimens** | 0.1 - 13 mm thick, up to 15 mm wide |

#### Features

- Dual flexure design for durability
- Tension and compression capable
- Cyclic testing compatible
- Mechanical overtravel stops for protection
- Quick-attach knife edges

#### Notes

- 3 mm gauge length requires model 3442SG-006M with spacers
- Verify accuracy at 3 mm gauge length with manufacturer
- Calibration certificate provided with unit

---

## 4. Characterization Equipment

### 4.1 Zeiss Xradia 620 Versa (X-ray Microscope)

Sub-micron resolution X-ray computed tomography system.

| Parameter | Specification |
|-----------|---------------|
| **Spatial Resolution** | ~500 nm (true resolution) |
| **Minimum Voxel Size** | 40 nm |
| **X-ray Source Voltage** | 30 - 160 kV |
| **X-ray Source Power** | 25 W |
| **Objective Range** | 0.4x to 40x |
| **Scan Resolution Range** | 300 nm to 30 μm |
| **Stage Travel (X)** | 50 mm |
| **Stage Travel (Y)** | 100 mm |
| **Stage Travel (Z)** | 50 mm |
| **Max Sample Diameter** | 100 mm (single sample) |
| **Sample Stations** | Up to 14 stations, 70 samples |

#### Technology

- Two-stage magnification architecture
- Resolution at Distance (RaaD) capability
- Scout-and-Scan software for acquisition
- Wide Field mode: 3x larger 3D volume capability

#### Capabilities

- Non-destructive 3D microstructure characterization
- Void/porosity analysis and quantification
- In-situ testing stages for dynamic observation
- 4D imaging (time-resolved studies)
- Multi-scale imaging workflows

#### Typical Applications

- AM porosity characterization
- Crack initiation and propagation studies
- Inclusion and defect analysis
- Microstructural evolution

---

### 4.2 Keyence VHX-7000 Digital Microscope

High-resolution digital microscope with automated surface roughness measurement.

#### Camera Specifications

| Parameter | VHX-7020 | VHX-7100 |
|-----------|----------|----------|
| **Image Sensor** | 3.19 MP CMOS (1/1.8") | 12.22 MP CMOS (1/1.7") |
| **Frame Rate** | 50 fps max | 30 fps max |
| **High-Accuracy Resolution** | 6144 x 4608 px | 12000 x 9000 px |
| **Stitched Image Size** | 50k x 50k pixels | 50k x 50k pixels |

#### System Specifications

| Parameter | Specification |
|-----------|---------------|
| **Display** | 27" IPS LCD, 3840 x 2160 |
| **Dynamic Range** | 16-bit HDR |
| **Storage** | 1 TB (350 GB system reserved) |
| **Operating Temperature** | +5 to 40°C |
| **Operating Humidity** | 35 - 80% RH (no condensation) |

#### Surface Roughness Parameters (ISO 21920 Compliant)

| Parameter | Description |
|-----------|-------------|
| **Ra** | Arithmetic mean roughness |
| **Rz** | Average maximum height |
| **Rv** | Maximum valley depth |
| **Rp** | Maximum peak height |
| **Rsk** | Skewness |
| **Rku** | Kurtosis |

#### Optional Modules

- VHX-H5M: 3D profile measurement module

---

### 4.3 Zygo ZeGage Pro Optical Profilometer

Non-contact coherence scanning interferometer for nanometer-scale surface measurement.

| Parameter | Specification |
|-----------|---------------|
| **Vertical Precision** | 0.15 nm (HR model) |
| **Measurement Technology** | Coherence Scanning Interferometry (CSI) |
| **Z-Stage Range** | ≤ 20 mm |
| **Magnification Range** | 1x - 50x objectives |
| **Data Points** | >1.9 million per measurement |
| **Camera Resolution** | 1600 x 1200 (HR model) |

#### Physical Dimensions

| Configuration | Dimensions (L x W x H) |
|---------------|------------------------|
| **With Workstation** | 156 x 127 x 76 cm |
| **Unit Only** | 82 x 53 x 53 cm |
| **Weight** | 54 kg |

#### Features

- SureScan vibration-tolerant technology
- Smart Setup automation
- Non-contact measurement
- Constant Z-height resolution across all objectives
- MetroPro and Mx software

---

## 5. Testing Standards

### 5.1 ASTM E466-21 Summary

**Title:** Standard Practice for Conducting Force Controlled Constant Amplitude Axial Fatigue Tests of Metallic Materials

#### Scope

- Axial force-controlled fatigue testing
- Elastic strain regime (high-cycle fatigue)
- Unnotched and notched specimens
- Constant amplitude loading
- Air at room temperature (standard)

#### Key Requirements

| Requirement | Description |
|-------------|-------------|
| **Alignment** | Specimen axis aligned with load axis |
| **Surface Finish** | Controlled to avoid stress risers |
| **Machining** | Appropriate techniques to prevent damage |
| **Grip Alignment** | Consistent specimen-to-specimen |

#### Applicable Materials

- Carbon steels and stainless steels
- Aluminum alloys
- Copper and copper alloys
- Titanium alloys
- Nickel-based superalloys
- Additive manufactured metals
- Weldments
- Surface-treated materials

#### Specimen Considerations

- Gauge section must be uniform
- Fillet radii per standard tables
- Surface preparation documented
- Build orientation recorded (for AM)

---

## 6. Quick Reference

### Specimen Size Limits

| Equipment | Limiting Dimension |
|-----------|-------------------|
| **GE M2 Series 5** | 245 x 245 x 350 mm build volume |
| **MTS 370.02** | 813 mm max length, 457 mm between columns |
| **Epsilon 3442** | 0.5-13 mm diameter (round), 3 mm gauge |
| **Zeiss Xradia 620** | 100 mm max diameter |

### Resolution Summary

| Equipment | Resolution |
|-----------|------------|
| **GE M2 Series 5** | 25-120 μm layer thickness |
| **Epsilon 3442** | Strain resolution per calibration |
| **Zeiss Xradia 620** | ~500 nm spatial, 40 nm voxel |
| **Keyence VHX-7000** | Sub-micron (objective dependent) |
| **Zygo ZeGage Pro** | 0.15 nm vertical precision |

### Force/Load Capacity

| Equipment | Capacity |
|-----------|----------|
| **MTS 370.02 Axial** | 25 kN |
| **MTS 370.02 Torsion** | 250 Nm |

---

## 7. Information Gaps

The following specifications require verification from physical equipment or manufacturer contact:

| Equipment | Missing Information |
|-----------|---------------------|
| **MTS 632.41B** | Equipment type and specifications (may be second extensometer) |
| **Keyence VHX-7000** | Detailed accuracy specs for surface roughness |
| **Zygo ZeGage Pro** | Complete specification sheet |
| **GE M2 Series 5** | Machine dimensions, power requirements |

**Recommendation:** Contact manufacturers or check physical equipment labels for missing specifications.

---

## 8. Sources

- [GE Additive M2 Series 5 - Aniwaa](https://www.aniwaa.com/product/3d-printers/ge-additive-m2-series-5/)
- [MTS 370.02 - Georgia Tech AMPF](https://ampf.research.gatech.edu/mts-37002-axial-torsion-servohydraulic-load-frame)
- [Epsilon Model 3442](https://www.epsilontech.com/products/miniature-extensometer-model-3442/)
- [Zeiss Xradia 620 - MIT Nanousers](https://nanousers.mit.edu/characterizenano/focus-facilities/xray-diffraction/zeiss-xradia-versa-620-micro-ct)
- [Keyence VHX-7000](https://www.keyence.com/products/microscope/digital-microscope/vhx-7000/)
- [Zygo ZeGage Pro](https://www.zygo.com/products/metrology-systems/3d-optical-profilers/zegage-pro)
- [ASTM E466-21](https://store.astm.org/e0466-21.html)

---

*Document created: 2026-01-26*
