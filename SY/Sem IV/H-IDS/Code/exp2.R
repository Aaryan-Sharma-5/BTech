A <- matrix(c(1, 1, 1, 2, -1, 1, 1, -2, 3), nrow =  3, byrow = TRUE)
B <- c(6, 3, 14)

print(A)
print(B)

augmented_matrix <- cbind(A, B)
print(augmented_matrix)

determinant_A <- det(A)
if(determinant_A == 0){
  cat("No unique solution\n")
}else{
  cat("Unique solution")
}

gauss_jordan <- function(A, B){
  augmented_matrix <- cbind(A, B)
  n <- nrow(A)
  for(i in 1:n){
    augmented_matrix[i, ] <- augmented_matrix[i, ] / augmented_matrix[i, i]
    for(j in 1:n){
      if(j != i){
        augmented_matrix[j, ] <- augmented_matrix[j, ] - augmented_matrix[j, i] * augmented_matrix[i, ]
      }
    }
  }
  solution <- augmented_matrix[, n + 1]
  return(solution)
}

solution_gauss <- gauss_jordan(A, B)
print(solution_gauss)

sol_solve <- solve(A, B)
print(sol_solve)

A_inverse <- solve(A)
solution_alt <- A_inverse %*% B
print(solution_alt)

plane1 <- function(x, y) 6 - x - y
plane2 <- function(x, y) 3 - 2 * x + y
plane3 <- function(x, y) (14 - x + 2 * y) / 3

x_vals <- seq(-10, 10, length.out = 30)
y_vals <- seq(-10, 10, length.out = 30)

z1 <- outer(x_vals, y_vals, plane1)
z2 <- outer(x_vals, y_vals, plane2)
z3 <- outer(x_vals, y_vals, plane3)

open3d()

surface3d(x_vals, y_vals, z1, color = "blue", alpha = 0.5)
surface3d(x_vals, y_vals, z2, color = "red", alpha = 0.5)
surface3d(x_vals, y_vals, z3, color = "green", alpha = 0.5)

solution <- solve(A, B)
points3d(solution[1], solution[2], solution[3], col = "black", size = 10)

texts3d(x = 0, y = 0, z = 0, text = "Origin", col = "black")
legend3d("topright", legend = c("Plane 1", "Plane 2", "Plane 3", "Solution"),
         col = c("blue", "red", "green", "black"), pch = c(NA, NA, NA, 19))