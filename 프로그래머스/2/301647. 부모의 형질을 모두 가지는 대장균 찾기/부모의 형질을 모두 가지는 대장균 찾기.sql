SELECT CHILD.ID, CHILD.GENOTYPE, PARENT.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA CHILD
JOIN ECOLI_DATA PARENT ON CHILD.PARENT_ID = PARENT.ID
WHERE (CHILD.GENOTYPE & PARENT.GENOTYPE) = PARENT.GENOTYPE
ORDER BY CHILD.ID ASC;
