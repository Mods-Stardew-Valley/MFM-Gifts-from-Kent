# Changelog
Todas as mudanças importantes deste projeto serão documentadas neste arquivo.


## v0.0.0 - 2026-08-12


### Outras alterações

#### Initial commit





## v1.0.0 - 2026-08-17


### Outras alterações

#### Merge branch 'main' of https://github.com/Mods-Stardew-Valley/MFM-Gifts-from-Kent


#### Merge branch 'main' of https://github.com/Mods-Stardew-Valley/MFM-Gifts-from-Kent


#### Merge branch 'main' of https://github.com/Mods-Stardew-Valley/MFM-Gifts-from-Kent


#### Reduce header size values in md_bbcode_sync.py

Adjust header-to-BBCode size mapping in convert_headers_md2bb: replace oversized values (e.g. 200, 175, ...) with realistic sizes (20, 17, ...) so rendered BBCode uses correct font scaling. This fixes excessively large header output when converting Markdown headers to BBCode.


#### Add Kent mail/translation and update README

Move workflow into .github/workflows, add Kent-specific mail entries and repeatable gifts in mail.json, and add corresponding Portuguese i18n keys (KentRepeteable, MailKent01-10). Update README to replace template placeholders with Kent gift lists and repeatables, and clean up extraneous template text. These changes replace generic TEMPLATE placeholders with concrete Kent mod content and reorganize the workflow location.


#### Add files via upload


#### Add files via upload

updates



### ✨ Novidades

#### zh.json

└─ Adicionado a tradução para Chines Simplificado


#### vi.json

└─ Adicionado a tradução para Vietnamita


#### uk.json

└─ Adicionado a tradução para Ucraniano


#### tr.json

└─ Adicionado a tradução para Turco


#### th.json

└─ Adicionado a tradução para Tailandes


#### ru.json

└─ Adicionado a tradução para Russo


#### pt.json

└─ Adicionado a tradução para Portugues Europeu


#### pl.json

└─ Adicionado a tradução para Polones


#### nl.json

└─ Adicionado a tradução para Holandes


#### ko.json

└─ Adicionado a tradução para Coreano


#### ja.json

└─ Adicionado a tradução para Japones


#### it.json

└─ Adicionado a tradução para Italiano


#### hu.json

└─ Hungaro adicionado as traduções


#### fr.json

└─ Frances adicionado as traduções


#### es.json

└─ Espanhol adicionado as traduções


#### default.json

└─ Ingles adicionado as traduções


#### de.json

└─ Alemão adicionado as traduções


#### da.json

└─ Dinamarques adicionado as traduções


#### PT-BR

└─ Tradução adicionada



### 🏗 Versão

#### v1.0.0

└─ Atualizada a versão para primeira funcional
Adicionado chave de atualização Nexus



### 🐛 Correções

#### name change

└─ Corrigido os nomes no manifesto para o correto



### 📚 Documentação

#### Updade no readme

└─ Adicionado descrição e alterados os tamanhos no codigo


#### atualiza CHANGELOG.md [skip ci]


#### Atualizadas traduções

└─ Acrescentada Dinamarques as traduções suportadas


#### atualiza CHANGELOG.md [skip ci]


#### atualiza CHANGELOG.md [skip ci]


#### atualiza CHANGELOG.md [skip ci]


#### atualiza CHANGELOG.md [skip ci]


#### atualiza CHANGELOG.md [skip ci]



### 🔧 Manutenção

#### sincroniza README.md <-> README.bbcode [skip ci]


#### sincroniza README.md <-> README.bbcode [skip ci]





## v1.0.1 - 2026-08-17


### Outras alterações

#### Merge branch 'main' of https://github.com/Mods-Stardew-Valley/MFM-Gifts-from-Kent


#### Adjust archive exclusions in changelog workflow

Update .github/workflows/changelog.yml to refine files excluded from the release ZIP: add .git-cliff and .scripts, exclude README.bbcode, and fix .gitattributes exclusion (file, not directory glob). This prevents auxiliary files from being packaged into the release archive.

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>



### 🐛 Correções

#### Gifts error

└─ Corrigido aviso de item errado no presente da carta 9



### 📚 Documentação

#### atualiza CHANGELOG.md [skip ci]


#### atualiza CHANGELOG.md [skip ci]




