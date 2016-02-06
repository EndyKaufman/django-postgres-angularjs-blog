describe('Update user profile with user role', function() {
    var helpers = require('./../helpers.js');

    var appConfigResponse = undefined, userResponse = undefined, logoutResponse = undefined, profileResponse = undefined, restoreProfileResponse = undefined;

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
        if (userResponse!==undefined){
            done();
            return;
        }
        helpers.postJson('/account/login', {
            email:'user@email.com',
            password:'user@email.com'
        }, function(response){
            userResponse = response;
            done();
        });
      });

      it('response structure must be correct', function() {
        expect(typeof userResponse).toEqual('object');
        var userData = userResponse.data[0];
        var fields = ['id', 'username', 'email', 'firstname', 'lastname', 'roles'];
        for (var i=0; i<fields.length; i++)
            expect(userData[fields[i]]).toBeDefined();
        if (userData.roles.length>0)
            expect(userData.roles[0]).toEqual('user');
      });

      describe('Update first name', function() {

        beforeEach(function(done){
            if (profileResponse!==undefined){
                done();
                return;
            }
            helpers.postJson('/account/profile/update', {
                firstname:'New Name',
                email:'user@email.com'
            }, function(response){
                profileResponse = response;
                done();
            });
        });

        it('response structure must be correct', function() {
            expect(typeof profileResponse).toEqual('object');
            var userData = profileResponse.data[0];
            var fields = ['id', 'username', 'email', 'firstname', 'lastname', 'roles'];
            for (var i=0; i<fields.length; i++)
                expect(userData[fields[i]]).toBeDefined();
            if (userData.roles.length>0)
                expect(userData.roles[0]).toEqual('user');
            expect(userData.firstname).toEqual('New Name');
        });

        describe('Cancel modify first name', function() {

            beforeEach(function(done){
                if (restoreProfileResponse!==undefined){
                    done();
                    return;
                }
                helpers.postJson('/account/profile/update', {
                    firstname:userResponse.data[0].firstname,
                    email:'user@email.com'
                }, function(response){
                    restoreProfileResponse=response;
                    done();
                });
            });

            it('response structure must be correct', function() {
                expect(typeof restoreProfileResponse).toEqual('object');
                var oldData = userResponse.data[0];
                var userData = restoreProfileResponse.data[0];
                expect(oldData.firstname).toEqual(userData.firstname);
            });

            describe('Logout from site', function() {

                beforeEach(function(done){
                    if (logoutResponse!==undefined){
                        done();
                        return;
                    }
                    helpers.postJson('/account/logout', {
                    }, function(response){
                        logoutResponse = response;
                        done()

                    });
                });

                it('response structure must be correct', function() {
                    expect(typeof logoutResponse).toEqual('object');
                    expect(logoutResponse.code).toEqual('ok');
                });

            });

        });

      });

    });

});