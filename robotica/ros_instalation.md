# Instalação da ferramenta de simulação do TIAGo no Ubuntu 22.04 com Docker

Primeiro de tudo. Quem, como eu, instalou conda/miniconda/anaconda, precisa desinstalar para não ter problemas com o ROS.

## Desinstalando o Conda:
No meu caso, instalei o `miniconda3`. Se não tiver segurança em fazer as coisas via terminal, dá uma pesquisada na internet como fazer isso:

Buscando o diretório onde o miniconda foi instalado:

```bash
ls ~ | grep miniconda
```

Desinstalando o miniconda.
Cuidado com esse comando, ele vai apagar tudo que estiver dentro do diretório indicado.

```bash
rm -rf ~/miniconda3
```

Remova o `PATH` do miniconda do seu arquivo `.bashrc` ou `.bash_profile`:

```bash
nano ~/.bashrc
```

e remova a linha que contém o `miniconda`:

```bash
export PATH="/home/usuario/miniconda3/bin:$PATH"
```

## Instalando o driver de vídeo da NVIDIA:

Seguindo esse tutorial, garanta que o notebook está com o driver de vídeo da NVIDIA instalado:

https://ubuntu.com/server/docs/nvidia-drivers-installation

Reinicie o computador, e verifique se o driver foi instalado corretamente.
Em seguida, abrindo o programa do driver, vá à opção `PRIME Profiles` e selecione a opção `NVIDIA (Performance Mode)`. Isso vai fazer com que o sistema utilize a placa de vídeo NVIDIA para renderizar as imagens.

**Reinicie o computador novamente.**

## Instalando o ROS2 no Ubuntu 22.04:

Basicamente, segui esse tutorial aqui:

[Install ROS2 and Setup on Ubuntu 22.04 LTS](https://medium.com/spinor/getting-started-with-ros2-install-and-setup-ros2-humble-on-ubuntu-22-04-lts-ad718d4a3ac2)

## Instalando o Rocker:
Agora, com o ROS2 instalado, vamos instalar o Rocker, que é uma ferramenta para gerenciar containers do Docker.

Essa é a documentação: [Rocker](https://github.com/osrf/rocker)

Mas basicamente, você deve precisar somente instalar via `apt-get`:

```bash
sudo apt-get install python3-rocker
```

## Instalando o TIAGo no Docker:
Agora sim dá pra instalar o TIAGo no Docker. Seguindo esse tutorial:

https://wiki.ros.org/Robots/TIAGo/Tutorials/Installation/Installing_Tiago_tutorial_docker


## Testando a Instalação:
Se tudo deu certo, você pode seguir esse tutorial para verificar e ver o robozinho na interface gráfica.

https://wiki.ros.org/Robots/TIAGo/Tutorials/Installation/Testing_simulation
