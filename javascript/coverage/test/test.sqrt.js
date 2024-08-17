const chai = require('chai');
const expect = chai.expect;
const My = require('../sqrt.js');

describe("sqrt", function() {
    it("4的平方根应该等于2", function(){
        expect(My.sqrt(4)).to.equal(2);
    });
    
    it("4的平方根应该等于2", function(){
        expect(function(){ My.sqrt(-1);}).to.throw("负值没有平方根");
    });
});