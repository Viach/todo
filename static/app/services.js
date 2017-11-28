var todoServices = angular.module('todoServices', ['ngResource']);

todoServices.factory('api', ['$resource', '$http', '$q', function ($resource, $http, $q) {

    return {
        tasks: $resource('/api/tasks/', {id: '@id'}, {
            update: {method: 'PUT', url: '/api/tasks/update/'},
            delete: {method: 'DELETE', url: '/api/tasks/delete/:id'},
            create: {method: 'POST', url: '/api/tasks/create/'}
        }),
        get_tasks_choices: $resource('/api/tasks/get_tasks_choices/', {}, {})
    }
}]);

