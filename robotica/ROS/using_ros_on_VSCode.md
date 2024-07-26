# Usando ROS no VSCode em um ambiente de desenvolvimento remoto (Docker)
## Extensões necessárias:
### Dev Containers
- Id: ms-vscode-remote.remote-containers
- Description: Open any folder or repository inside a Docker container and take advantage of Visual Studio Code's full feature set.
- Version: 0.375.1
- Publisher: Microsoft
- VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

### Python
Id: ms-python.python
Description: Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more.
Version: 2024.10.0
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python

### ROS
Id: ms-iot.vscode-ros
Description: Develop Robot Operating System (ROS) with Visual Studio Code.
Version: 0.9.2
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-iot.vscode-ros

## Configurando a Execução
Com as extensões instaladas, execute um container do seu projeto ROS, com o workspace montado. Seguindo os exemplos da aula, vamos chamar o nosso aqui de `turma3_ws`.
Em todos os exemplos de código, onde você ver `USUARIO`, substitua pela sua pasta de usuário no sistema. Na dúvida, abra uma terminal novo (`Ctrl` + `Alt` + `T`) e digite:

```bash
echo $HOME
```

No lado esquerdo do VSCode, clique no ícone de `><` e na aba de **Dev Containers** selecione o container que vai estar em execução (geralmente o nome vai ser pouco intuitivo, como uma sequência de letras e números). Com um clique direito, selecione **Attach in new window**.
Isso vai abrir uma nova janela do VSCode conectado ao container. No entanto, é provável que nenhuma pasta esteja seleciona. Utilizando o botão de `Open Folder`, navegue até a pasta do seu workspace ROS, que deve estar em `/home/USUARIO/turma3_ws`.

Se seu workspace estiver corretamente configurado, você deve ver as pastas `src`, `build` e `devel` no seu workspace, além do arquivo `.catkin_workspace`. 

Se você não ver essas pastas, é possível que o workspace não esteja corretamente configurado. Nesse caso, você pode tentar rodar o comando `catkin_make` na pasta do workspace, ou seguir as instruções do [tutorial oficial do ROS](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment).

Nessa raiz, crie um diretório chamado `.vscode`, e adicione os arquivos `settings.json` e `launch.json` com o conteúdo abaixo:

### launch.json
```json
{
    "version": "0.2.0",
    "configurations": [
      {
          "name": "ROS: Launch my file",
          "request": "launch",
          "target": "<full path to your launch.py or launch file>",
          "launch": ["rviz", "gz", "gzserver", "gzclient"],
          "type": "ros"
      }
    ]
}
```

### settings.json
```json
{
    "[python]": {
        "diffEditor.ignoreTrimWhitespace": false,
        "editor.formatOnType": true,
        "editor.wordBasedSuggestions": "off"
    },
    "python.autoComplete.extraPaths": [
        "/home/USUARIO/turma3_ws/devel/lib/python3/dist-packages",
        "/opt/ros/noetic/lib/python3/dist-packages",
        "/home/USUARIO/turma3_ws/src/test1/src"
    ],
    "python.analysis.extraPaths": [
        "/home/USUARIO/turma3_ws/devel/lib/python3/dist-packages",
        "/opt/ros/noetic/lib/python3/dist-packages",
        "/home/USUARIO/turma3_ws/src/test1/src"
    ]
}
```

### Ativando a Extensão ROS
Usando o atalho `Ctrl` + `Shift` + `P`, digite `ROS: Update Python Path` e selecione a opção. Isso vai atualizar o path do Python para incluir o workspace ROS.
Em seguida, utilizando o mesmo atalho, digite `ROS: Install ROS Dependencies for this workspace using rosdep`. Isso vai instalar as dependências do ROS no seu workspace.
Com tudo isso feito, feche o VSCode e abra novamente.
Se tudo deu certo, você deve ser capaz de utilizar o `Pylance` para autocompletar e fazer debug do seu código Python.
