#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 23:42:37 2020

@author: amanda
"""

import pandas as pd
import os


if __name__ == "__main__":
    for y in range(102, 103):
        for m in range(1, 3):
            web_type_old = True
            if y > 101 and m > 2:
                web_type_old = False

            folder = "./data/" + str(y) + str(m)
            if not os.path.exists(folder):
                os.makedirs(folder)

            url = "https://mops.twse.com.tw/nas/t21/sii/t21sc03_" + \
                str(y) + "_" + str(m) + "_0.html"

            if web_type_old:
                html_df = pd.read_html(url, encoding="Big5")
            else:
                html_df = pd.read_html(url)
                #print("read as big 5")

            # print(html_df)
            #c = input()
            gap = 1
            if web_type_old:
                gap = 1
            else:
                gap = 2
            if y == 102 and m == 1:
                for i in range(1, len(html_df), gap):
                    if "產業別" in html_df[i].keys()[0][0]:
                        file_name = html_df[i].keys()[0][0]
                        # print(file_name)
                        #file_name = file_name.split("：")[1]
                        # print(file_name)
                        keys = html_df[i + 1].keys()
                        # print(keys)
                        #c = input()
                        col_name = []
                        for j in range(0, len(keys)):
                            col_name.append(keys[j][1])

                        html_df[i + 1].columns = col_name
                        html_df[i + 1].to_csv(os.path.join(folder, file_name +
                                                           ".csv"), encoding="utf-8-sig", index=False)

            for i in range(1, len(html_df), gap):
                if "產業別" in html_df[i].keys()[0]:
                    file_name = html_df[i].keys()[0].split(" : ")[0]
                    # print(html_df[i].keys()[0])
                    keys = html_df[i + 1].keys()
                    # print(keys)
                    #c = input()
                    col_name = []
                    for j in range(0, len(keys)):
                        col_name.append(keys[j][1])

                    html_df[i + 1].columns = col_name
                    html_df[i + 1].to_csv(os.path.join(folder, file_name +
                                                       ".csv"), encoding="utf-8-sig", index=False)