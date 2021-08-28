var djangoTodo = angular.module('djangoTodo', []);

function mainController($scope, $http) {

    $scope.readTodos = function() {
        $http.get('/api3/todos/')
            .success(function(data) {
                $scope.formData = {};
                $scope.todos = data;
                console.log(data);
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };

    $scope.createTodo = function() {
        $http.post('/api3/todos/', $scope.formData)
            .success(function(data) {
                console.log(data);
                $scope.readTodos();
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };

    $scope.deleteTodo = function(id) {
        $http.delete('/api3/todos/' + id + '/')
            .success(function(data) {
                console.log(data);
                $scope.readTodos();
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };

    $scope.readTodos();

}
