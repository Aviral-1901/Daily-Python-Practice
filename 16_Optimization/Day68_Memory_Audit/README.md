1. The Compilation Pipeline 
This experiment traced the transformation of human-readable C++ into machine-executable binary.
- Compilation: The GCC compiler translates .cpp source files into independent .o (Object) files.
- Linking: The Linker stitches these .o files into a single .elf (Executable Linkable Format) container. This maps our logic to esp32's physical memory addresses.
- Flash Preparation: Finally, a stripping process removes the symbols and metadata (labels) from the .elf to produce the raw .bin file, which is then flashed onto the esp32.

2. Memory Segment Analysis
Inside the .elf file, the data is organized into logical Segments:
- .text (Flash): Stores the OpCodes. This is where our for loops and other logic live.
- .rodata (Flash): Stores Read-Only Data. By using the const keyword, we forced our 2.1KB of weights to stay in Flash rather than being copied into RAM.
- .data (RAM): Stores initialized global variables. These occupy space in both Flash (for the starting value) and RAM (to allow changes during execution).
- .bss (RAM): Block Started by Symbol. This contains uninitialized variables (starting at zero). It occupies zero space in the physical .bin file on disk.

3. The Preprocessor and Dead Code Elimination
- Inclusion Logic: Only files explicitly called via #include are seen by the compiler. Files sitting in the /include folder that are not referenced are ignored completely.
- Optimization: We verified Dead Code Elimination (DCE). If a constant is included but never referenced in the .text segment (the logic), the Linker ignores it to save space.

