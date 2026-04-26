x = |3,3,5;1,2,3;1,2,3|;

print x[2,2];

data = eigenize(x);

eigenvalues = data[0];
eigenvectors = data[1];

print eigenvalues;
print eigenvectors;