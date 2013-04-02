from numpy import mean,cov,double,cumsum,dot,linalg,array,rank

#  coeff :
#    is a p-by-p matrix, each column containing coefficients 
#    for one principal component.
#  score : 
#    the principal component scores; that is, the representation 
#    of A in the principal component space. Rows of SCORE 
#    correspond to observations, columns to components.
#  latent : 
#    a vector containing the eigenvalues 
#    of the covariance matrix of A.
#  http://glowingpython.blogspot.com/2011/07/principal-component-analysis-with-numpy.html

def princomp(A, dims):
  #TODO: fix dims, this method should be independent of dims
  M = (A-mean(A.T,axis=1)).T # subtract the mean (along columns)
  [latent,coeff] = linalg.eig(cov(M)) # attention:not always sorted
  score = dot(coeff[:, 0:dims].T,M) # projection of the data in the new space
  return coeff,score,latent

