var todoCtrls = angular.module('todoCtrls', ['ui.bootstrap'])



todoCtrls.controller('tasksListController', ['$scope', 'api', '$sce', '$uibModal', 
    function($scope, api, $sce, $uibModal){
    
    $scope.hideDoneTasks = true;
    $scope.orderTasks = true;             //  up 
    $scope.tasks_choices = api.get_tasks_choices.get({}, function(data) {
        $scope.filter_categories = {};
        for (var k in data['categories']) {
            $scope.filter_categories[data['categories'][k]] = true;            
        };
        $scope.filter_priorities = {};
        for (var k in data['priorities']) {
            $scope.filter_priorities[data['priorities'][k]] = true;            
        };    
        $scope.getTasks();    
        return data;
    }); 
    
    $scope.getTasks = function() {
        $scope.tasks = api.tasks.query({
            filter_categories : $scope.filter_categories,
            filter_priorities : $scope.filter_priorities,
            filter_done_tasks : $scope.hideDoneTasks,
            order_tasks : $scope.orderTasks
            }, function(data) {
            return data;
        });
    };    

    $scope.changeOrderTasks = function () {
        $scope.orderTasks = ($scope.orderTasks) ? false: true;    
        $scope.getTasks();    
    };

    $scope.setTaskStatus = function(task) {
        $scope.task = task;
        $scope.task.done = !task.done;
        $scope.task.$update()
            .then(function () {
                
            });
    };

    $scope.trustAsHTML = function (html) {
        return $sce.trustAs($sce.HTML, html);
    };

    $scope.updateTask = function (task) {
        $scope.error = null;
        $scope.result = null;
        $scope.task = task;

        $uibModal.open({
            animation: false,
            scope: $scope,
            size: 'lg',
            templateUrl: '/static/modals/task-update-modal.html',
            controller: 'taskUpdateController',
            resolve: {
                data: {
                    task: $scope.task,
                    tasks_choices: $scope.tasks_choices               
                }
            }
        }); 
    };

    $scope.createTask = function () {
        $scope.error = null;
        $scope.result = null;
        $scope.newTask = new api.tasks();

        $uibModal.open({
            animation: false,            
            scope: $scope,
            size: 'lg',
            templateUrl: '/static/modals/task-update-modal.html',
            controller: 'taskCreateController',
            resolve: {
                data: {
                    task: $scope.newTask,
                }
            }
        });
    };


    $scope.deleteTask = function (task) {
        $scope.error = null;
        $scope.result = null;
        task.$delete().then(function () {
            var index = $scope.tasks.indexOf(task);
            $scope.tasks.splice(index, 1);
            $scope.result = 'Deleted successfully';
        }, function (rejection) {
            $scope.error = rejection.data
        });
    }; 


}]);

todoCtrls.controller('taskUpdateController', ['$scope', '$uibModalInstance', 'uibDateParser', 'data', function ($scope, $uibModalInstance, uibDateParser, data) {

    $scope.task = data.task;
    $scope.tasks_choices = data.tasks_choices;
    $scope.format = 'yyyy/MM/dd';
    $scope.save = function () {
        $scope.error = null;
        $scope.result = null;
        $scope.task.$update()
            .then(function () {
                $scope.task = data.task;
            })
            .then(function () {
                $scope.errors = null;
                $scope.result = 'Updated successfully';
            }, function (rejection) {
                $scope.errors = rejection.data;
            });
    }
    $scope.close = function () {
        $uibModalInstance.dismiss('cancel');
    };

}]);


todoCtrls.controller('taskCreateController', ['$scope', '$uibModalInstance', 'uibDateParser', 'data', function ($scope, $uibModalInstance, uibDateParser, data) {

    $scope.task = data.task;
    $scope.format = 'yyyy/MM/dd';
    $scope.save = function () {
        $scope.error = null;
        $scope.result = null;
        $scope.task.$create()
            .then(function () {
                $scope.task = data.task;
            })
            .then(function () {
                $scope.errors = null;
                $scope.result = 'Created successfully';
            }, function (rejection) {
                $scope.errors = rejection.data;
            });
    }
    $scope.close = function () {
        $uibModalInstance.dismiss('cancel');
    };

}]);