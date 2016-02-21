describe('Work with projects as admin', function() {
    var helpers = require('./../helpers.js');

    var appConfigResponse = undefined, adminResponse=undefined, listResponse = undefined, createResponse = undefined, updateResponse = undefined, deleteResponse = undefined;

    beforeEach(function(done){
        if (appConfigResponse!==undefined){
            done();
            return;
        }
        browser.driver.manage().window().setSize(1280, 1024);
        browser.get(browser.baseUrl).then(function(){
            helpers.executeAndReturnJson(
                'if (window.AppConfig!==undefined)callback(window.AppConfig);else callback({});',
                function(response){
                    appConfigResponse = response;
                    done();
                });
            }
        );
    });

    it('response structure must be correct', function() {
        expect(appConfigResponse).toBeDefined();
        expect(typeof appConfigResponse).toEqual('object');
    });


    describe('Login on site', function() {

        beforeEach(function(done){
            if (adminResponse!==undefined){
                done();
                return;
            }
            //helpers.debug=true;
            helpers.postJson('/account/login', {
                email:'admin@email.com',
                password:'admin@email.com'
            }, function(response){
                adminResponse = response;
                done();
            });
        });

        it('response structure must be correct', function() {
            expect(typeof adminResponse).toEqual('object');
            expect(adminResponse.data).toBeDefined();
            if (adminResponse.data){
                var userData = adminResponse.data[0];
                var fields = ['id', 'username', 'email', 'firstname', 'lastname', 'roles'];
                for (var i=0; i<fields.length; i++)
                    expect(userData[fields[i]]).toBeDefined();
                if (userData.roles.length>0)
                    expect(userData.roles[0]).toEqual('admin');
            }
        });

        describe('Get projects list', function() {

            beforeEach(function(done){
                if (listResponse!==undefined){
                    done();
                    return;
                }
                //helpers.debug=true;
                helpers.getJson('/project/list', function(response){
                    listResponse = response;
                    done();
                });
            });

            it('response structure must be correct', function() {
                expect(typeof listResponse).toEqual('object');
                expect(listResponse.code).toEqual('ok');
                expect(listResponse.data).toBeDefined();
                if (listResponse.data){
                    var record = listResponse.data[0];
                    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags', 'images'];
                    for (var i=0; i<fields.length; i++)
                        expect(record[fields[i]]).toBeDefined();
                }
            });

            describe('Create new project', function() {
                var createdRecord = {};

                beforeEach(function(done){
                    if (createResponse!==undefined){
                        done();
                        return;
                    }
                    //helpers.debug=true;
                    helpers.postJson('/project/create',
                        {
                            id: 101,
                            name:'newProject',
                            title:'New Project',
                            description:'description',
                            type:1,
                            url:'url',
                            html:'html',
                            markdown:'markdown',
                            text:'bla bla bla',
                            tags:[{text:'tag1'}],
                            images:[{src:'image1'}]
                        }, function(response){
                        createResponse = response;
                        createdRecord = {};
                        if (createResponse.data){
                            createdRecord = createResponse.data[0];
                        }
                        done();
                    });
                });

                it('response structure must be correct', function() {
                    expect(typeof createResponse).toEqual('object');
                    expect(createResponse.code).toEqual('ok');
                    expect(createResponse.data).toBeDefined();
                    if (createResponse.data){
                        var record = createResponse.data[0];
                        var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags', 'images'];
                        for (var i=0; i<fields.length; i++){
                            expect(record[fields[i]]).toBeDefined();
                        }
                    }
                });

                it('tags must be created or used exists', function() {
                    expect(createResponse.data).toBeDefined();
                    if (createResponse.data){
                        var record = createResponse.data[0];
                        expect(record.tags[0].text).toEqual('tag1');
                        expect(record.tags[0].id).toBeDefined();
                    }
                });

                it('images must be created or used exists', function() {
                    expect(createResponse.data).toBeDefined();
                    if (createResponse.data){
                        var record = createResponse.data[0];
                        expect(record.images[0].src).toEqual('image1');
                        expect(record.images[0].id).toBeDefined();
                    }
                });

                describe('Update created project', function() {

                    createdRecord.title='New Project Updated';

                    beforeEach(function(done){
                        if (updateResponse!==undefined){
                            done();
                            return;
                        }
                        //helpers.debug=true;
                        helpers.postJson('/project/update/'+createdRecord.id, createdRecord, function(response){
                            updateResponse = response;
                            done();
                        });
                    });

                    it('response structure must be correct', function() {
                        expect(typeof updateResponse).toEqual('object');
                        expect(updateResponse.code).toEqual('ok');
                        expect(updateResponse.data).toBeDefined();
                        if (updateResponse.data){
                            var record = updateResponse.data[0];
                            var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags', 'images'];
                            for (var i=0; i<fields.length; i++)
                                expect(record[fields[i]]).toBeDefined();
                        }
                    });

                    it('record must be updated', function() {
                        expect(updateResponse.data).toBeDefined();
                        if (updateResponse.data){
                            var record = updateResponse.data[0];
                            var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags', 'images'];
                            for (var i=0; i<fields.length; i++)
                                expect(record[fields[i]]).toEqual(createdRecord[fields[i]]);
                        }
                    });

                    describe('Remove created project', function() {

                        beforeEach(function(done){
                            if (deleteResponse!==undefined){
                                done();
                                return;
                            }
                            //helpers.debug=true;
                            helpers.postJson('/project/delete/'+createdRecord.id, {}, function(response){
                                deleteResponse = response;
                                done();
                            });
                        });

                        it('response structure must be correct', function() {
                            expect(typeof deleteResponse).toEqual('object');
                            expect(deleteResponse.code).toEqual('ok');
                        });
                    });
                });
            });
        });
    });
});