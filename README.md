<div align="center">
   <img width="93" src="logo.png" alt="Logo">
   <h1><b>AFGAN</b></h1>
   <p><i>~ Generate & use! ~</i></p>
</div>

<div align="center">
   <a href="https://github.com/StafLoker/afgan/releases"><img src="https://img.shields.io/github/downloads/StafLoker/afgan/total.svg?style=flat" alt="downloads"></a>
   <a href="https://github.com/StafLoker/afgan/pkgs/container/afgan"><img src="https://img.shields.io/badge/ghcr.io-afgan-blue?style=flat&logo=docker" alt="ghcr"/></a>
   <a href="https://github.com/StafLoker/afgan/releases"><img src="https://img.shields.io/github/v/release/StafLoker/afgan?style=flat" alt="latest version"/></a>
   <a href="https://github.com/StafLoker/afgan/blob/main/LICENSE"><img src="https://img.shields.io/github/license/StafLoker/afgan.svg?style=flat" alt="license"><a>

   <p>Minimalist web server for generating anime faces using AFGAN (Anime Face GAN).</p>

<img src="media/afgan_grid.png" width="550" alt="Faces">
</div>

## Quick Start

**Docker**
```bash
docker pull ghcr.io/stafloker/afgan:latest
docker run -p 80:38880 ghcr.io/stafloker/afgan:latest
```

**Docker Compose**
```bash
docker-compose up
```

## Model architecture

DFGAN ( like DCGAN ).

<div align="center">
   <img src="media/afgan_arch.png" width="700" alt="Model architecture">
</div>

## Training
### Loss
<div align="center">
   <img src="media/loss_history.png" width="500" alt="History of image 1">
</div>

### History
<div align="center">
   <img src="media/training_0.gif" width="90" alt="History of image 1">
   <img src="media/training_1.gif" width="90" alt="History of image 2">
   <img src="media/training_2.gif" width="90" alt="History of image 3">
   <img src="media/training_3.gif" width="90" alt="History of image 4">
   <img src="media/training_4.gif" width="90" alt="History of image 5">
</div>

## Screenshots

<div align="center">
   <img src="media/web.png" width="700" alt="Web screenshots">
</div>

## Contributing

Contributions are welcome! Please read the contributing guidelines and submit pull requests for any improvements.

## License

This project is licensed under the terms specified in the LICENSE file.