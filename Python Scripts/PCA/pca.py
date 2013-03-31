from numpy import mean,cov,double,cumsum,dot,linalg,array,rank

def princomp(A, dims):
        M = (A-mean(A.T,axis=1)).T # subtract the mean (along columns)
        [latent,coeff] = linalg.eig(cov(M)) # attention:not always sorted
        score = dot(coeff[:, 0:dims].T,M) # projection of the data in the new space
        return coeff,score,latent

