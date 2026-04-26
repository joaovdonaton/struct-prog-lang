x = |3,3,5;1,2,3;1,2,4|;

print "Matrix";
print x;
print;

print "Transpose of that Matrix";
print T(x);
print;

print "Inverse of that Matrix";
print inv(x);
print;

print "Element at third row and third column:";
print x[2,2];
print;

data = eigenize(x);

eigenvalues = data[0];
eigenvectors = data[1];

max_eigenvalue = eigenvalues[0];
max_index = 0;
i = 1;

while (i < length(eigenvalues)) {
    if (eigenvalues[i] > max_eigenvalue) {
        max_eigenvalue = eigenvalues[i];
        max_index = i;
    }
    i = i + 1;
}

print "Max eigenvalue:";
print max_eigenvalue;
print "Max eigenvector:";
print eigenvectors[max_index];
print;

v1 = eigenvectors[0];
v2 = eigenvectors[1];

print "First Eigenvector";
print v1;
print;
print "Second Eigenvector";
print v2;
print;
print "Dot product of first and second eigenvectors";
print dot(v1, v2);
print;

a = |1,2,3;4,5,6|;
b = |7,8;9,10;11,12|;

print "Matrix multiplication with different sizes";
print "Matrix a";
print a;
print "Matrix b";
print b;
print "a multiplied by b (matrix multplication, not element-wise)";
print a @ b;
print;

print "Scalar multiplication (3*a)";
print 3 * a;
