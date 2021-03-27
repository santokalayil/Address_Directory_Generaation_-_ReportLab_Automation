# importing libraries
import os
import pandas as pd


def preprocess():
    csv_file = os.path.join("csv_files", "original.csv")
    df = pd.read_csv(csv_file)

    # preparing original data
    drop = [col for col in df.columns if 'Do you want to add one more family member?' in col]
    df = df.drop(drop, axis = 1)
    idx = [i for (i, col) in enumerate(df.columns) if 'Name of the Family Member' in col]
    idx_tuple = [(a, idx[idx.index(a)+1]) for a in idx if a != idx[-1]]

    # getting families and members separate
    families = pd.DataFrame()
    members = pd.DataFrame()

    lfm = 18

    for fam_id in range(df.shape[0]):
        fm = df.iloc[fam_id, 0:lfm].copy()
        fam_ser = pd.Series({'famid': fam_id})
        fam_ser = fam_ser.append(fm)
        families = pd.concat([families, pd.DataFrame(fam_ser).T])
        for se in idx_tuple:
            mem_ser = pd.Series({'famid': fam_id})
            m = df.iloc[fam_id, se[0]:se[1]].copy()
            if se != idx_tuple[0]:
                m.index = cols
            elif se == idx_tuple[0]:
                cols = m.index
            mem_ser = mem_ser.append(m)
            member = pd.DataFrame(mem_ser).T
            members = pd.concat([members,member])

    members.where(members['Name of the Family Member'] != '', inplace=True)  # use only if using google spreadsheet

    # removing rows if name of family member field is nan
    members = members[members['Name of the Family Member'].notna()]

    members = members.reset_index().drop(columns='index')
    families = families.reset_index().drop(columns='index')

    # creating analytical columns
    to_map = dict(members.famid.value_counts())
    families['no_fam_members'] = families['famid'].map(to_map)

    # filling other jobs with specified column
    tmp = members.copy()

    # combining 'optional job' column with 'profession' column
    rpl_dict = tmp["If profession entered is 'Other Jobs', please specify (optional)"].to_dict()
    original_dict = tmp["Profession"].to_dict()
    for key, value in rpl_dict.items():
        if str(value) != 'nan':
            original_dict[key] = value
    tmp["Profession"] = pd.Series(original_dict)

    tmp.drop("If profession entered is 'Other Jobs', please specify (optional)", 1, inplace=True)
    members = tmp.copy()

    # filling Nan with single space so that it can be used with reportlab later
    for i in [families, members]:
        i.fillna(' ', inplace=True)

    directory = pd.merge(members, families, on=['famid'])
    # now members and family ready...

    families.to_csv('csv_files/families.csv', index=False)
    members.to_csv('csv_files/members.csv', index=False)
    directory.to_csv('csv_files/directory.csv', index=False)

    print("PREPROCESSING SCRIPT successfully executed!")
    return 0


if __name__ == "__main__":
    preprocess()
