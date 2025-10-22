# SRAGI Sync Loop v1.0 - Arkitektur

```mermaid
graph TD
    %% -- Definisjon av Noder (Boksene) --

    subgraph "MENNESKE & KILDE (SSOT)"
        A["HUMAN INPUT
        (Inspirasjon, teori, kode)"]
        B["SRAGI SOURCE HUB
        (GitHub: Project2040/sragi.org)
        - SRL-LICENSE.yaml (SSOT)
        - Markdown-dokumenter"]
    end

    subgraph "INFRASTRUKTUR & FRONTEND (WordPress)"
        C["SRAGI BRIDGE (WP-LAG)
        (WPCodeBox @ One.com)
        - Mottar Webhook
        - **Kjører SIKKER signatursjekk**
        - Oppdaterer 'wp_options'"]
        D["SRAGI FRONT (Human Interface)
        (Bricks Builder)
        - Viser live data fra 'wp_options'
        - /license side"]
    end

    subgraph "INTELLIGENS & ETISK RAMMEVERK"
        E["SRAGI INTELLIGENCE LAYER
        (ChatGPT / SRAGI Muse)
        - Analyserer endringer
        - Lærer fra SSOT"]
        F["SRAGI ETHICAL FRAMEWORK
        (SRL v1.0)
        - CC BY 4.0 + RSL
        - Sikrer attribusjon"]
    end

    subgraph "OUTPUT & TILBAKEKOBLING"
        G["REGENERATIVE OUTPUT
        (Websider, APIer, AI-data)"]
        H["FEEDBACK LOOP
        (Refleksjon, iterasjon, syntese)"]
    end

    %% -- Definisjon av Flyt (Pilene) --
    A -- "Commit" --> B
    B -- "🔁 GitHub Push (Webhook)" --> C
    C -- "Viser data" --> D
    D -- "Feedback / API-kall" --> E
    E -- "Validerer mot" --> F
    F -- "Styrer" --> G
    G -- "Fører til" --> H
    H -- "Nytt input" --> A

    %% -- AI Feedback Loop (v1.1 Mål) --
    E -. "Foreslår Pull Request" .-> B

    %% -- Styling (Valgfritt, men episk) --
    classDef default fill:#222,stroke:#777,color:#fff,rx:5
    classDef hub fill:#0a3,stroke:#0f0,color:#fff,rx:5
    classDef bridge fill:#00517c,stroke:#00aaff,color:#fff,rx:5
    classDef ai fill:#4a148c,stroke:#ab47bc,color:#fff,rx:5

    class B hub
    class C bridge
    class E ai
