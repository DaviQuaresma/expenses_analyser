from pathlib import Path

# O que você precisa saber sobre pathlib

# • Criação de caminhos: Use Path() para o diretório atual, Path.cwd() para pegar a pasta de trabalho atual ou Path.home() para a pasta do usuário.

# • Concatenação intuitiva: Você pode unir diretórios e arquivos usando o operador de divisão / (ex.: pasta / "subpasta" / "arquivo.txt").

# • Propriedades úteis de inspeção:
# 	• .name: Nome do arquivo com extensão (ex.: arquivo.txt).
# 	• .stem: Apenas o nome do arquivo sem a extensão (ex.: arquivo).
# 	• .suffix: Extensão do arquivo (ex: .txt).
# 	• .parent: Pasta pai do caminho.

# • Verificações booleanas:
# 	• .exists(): Verifica se o arquivo ou pasta existe.
# 	• .is_file(): Confirma se é um arquivo.
# 	• .is_dir(): Confirma se é um diretório.

# • Leitura e escrita rápida:
# 	• .read_text() / .write_text() para arquivos de texto.
# 	• .read_bytes() / .write_bytes() para arquivos binários.

# • Navegação e busca:
# 	• .iterdir(): Lista o conteúdo de um diretório.
# 	• .glob("*") ou .rglob("*.py"): Faz buscas por padrões (o r em rglob busca de forma recursiva nas subpastas).

# • Criação e remoção:
# 	• .mkdir(parents=True, exist_ok=True): Cria pastas (e subpastas se necessário) sem dar erro se já existirem.
# 	• .unlink(): Apaga arquivos.
# 	• .rmdir(): Apaga diretórios vazios.


def csvPath(fileName: str) -> Path | None:
    # Para pegar o repositorio atual
    currentPath: Path = Path.cwd() / fileName

    if currentPath.suffix != ".csv" or not currentPath.exists():
        return None

    return currentPath