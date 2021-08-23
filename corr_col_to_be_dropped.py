def corr_col_to_be_dropped(df_train, corr_strength, col_cnt):
    '''
    :param df_train: Pandas dataframe having numerical features
    :param corr_strength: threshold to consider correlation strength between features
    :param col_cnt: number of columns to qualify the column to be dropped
    :return: list of columns to be dropped
    Usage example:
    col_drop = corr_col_to_be_dropped(X_train,0.41,1)
    '''
    
    
    cor_matrix = df_train.corr().abs()

    upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool))

    to_drop = [column for column in upper_tri.columns if sum(upper_tri[column] > corr_strength) > col_cnt  ]

    return to_drop
