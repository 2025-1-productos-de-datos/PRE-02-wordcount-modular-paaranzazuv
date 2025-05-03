# import os

# from ..src.wordcount import main


# def test_migracion():

#     main()

#     if not os.path.exists("data/output/results.tsv"):
#         raise FileNotFoundError(" el archivo results.tvs no existe.")

#     results = {}
#     with open("data/output/results.tsv", "r", encoding="utf-8") as f:
#         lines = f.readlines()
#         for line in lines:
#             key, value = line.strip().split("\t")
#             results[key] = value

#     assert results.get("analytics", 0) == "5", "Incorrect count for 'analytics'"
#     assert results.get("business", 0) == "7", "Incorrect count for 'business'"
#     assert results.get("by", 0) == "3", "Incorrect count for 'by'"
#     assert results.get("algorithms", 0) == "2", "Incorrect count for 'algorithms'"
#     assert results.get("analysis", 0) == "4", "Incorrect count for 'analysis'"
