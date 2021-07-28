for i in range(13,20):
    with open(f"tables/Multi_table_of_{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}\n")

