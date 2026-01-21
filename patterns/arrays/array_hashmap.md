001 Two Sum 笔记建议结构：

题型识别：Array + HashMap -> 查 complement
Plan A：暴力 O(n^2)（why slow）
Plan B：两遍 HashMap（先存再查）
Plan C：一遍 HashMap（边查边存，避免重复 index）
易错点：seen[num] = index（key 是数值，不是 index）