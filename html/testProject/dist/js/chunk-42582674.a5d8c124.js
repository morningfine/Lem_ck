(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-42582674"],{"057f":function(e,t,r){var n=r("fc6a"),o=r("241c").f,a={}.toString,i="object"==typeof window&&window&&Object.getOwnPropertyNames?Object.getOwnPropertyNames(window):[],c=function(e){try{return o(e)}catch(t){return i.slice()}};e.exports.f=function(e){return i&&"[object Window]"==a.call(e)?c(e):o(n(e))}},"159b":function(e,t,r){var n=r("da84"),o=r("fdbc"),a=r("17c2"),i=r("9112");for(var c in o){var s=n[c],l=s&&s.prototype;if(l&&l.forEach!==a)try{i(l,"forEach",a)}catch(u){l.forEach=a}}},"17c2":function(e,t,r){"use strict";var n=r("b727").forEach,o=r("a640"),a=o("forEach");e.exports=a?[].forEach:function(e){return n(this,e,arguments.length>1?arguments[1]:void 0)}},"1dde":function(e,t,r){var n=r("d039"),o=r("b622"),a=r("2d00"),i=o("species");e.exports=function(e){return a>=51||!n((function(){var t=[],r=t.constructor={};return r[i]=function(){return{foo:1}},1!==t[e](Boolean).foo}))}},"4de4":function(e,t,r){"use strict";var n=r("23e7"),o=r("b727").filter,a=r("1dde"),i=a("filter");n({target:"Array",proto:!0,forced:!i},{filter:function(e){return o(this,e,arguments.length>1?arguments[1]:void 0)}})},5530:function(e,t,r){"use strict";r.d(t,"a",(function(){return a}));r("b64b"),r("a4d3"),r("4de4"),r("e439"),r("159b"),r("dbb4");function n(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function a(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){n(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}},"65f0":function(e,t,r){var n=r("861d"),o=r("e8b5"),a=r("b622"),i=a("species");e.exports=function(e,t){var r;return o(e)&&(r=e.constructor,"function"!=typeof r||r!==Array&&!o(r.prototype)?n(r)&&(r=r[i],null===r&&(r=void 0)):r=void 0),new(void 0===r?Array:r)(0===t?0:t)}},"746f":function(e,t,r){var n=r("428f"),o=r("5135"),a=r("e538"),i=r("9bf2").f;e.exports=function(e){var t=n.Symbol||(n.Symbol={});o(t,e)||i(t,e,{value:a.f(e)})}},8418:function(e,t,r){"use strict";var n=r("c04e"),o=r("9bf2"),a=r("5c6c");e.exports=function(e,t,r){var i=n(t);i in e?o.f(e,i,a(0,r)):e[i]=r}},"8cca":function(e,t,r){"use strict";r.r(t);var n=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"project_list"},[r("el-card",{staticClass:"box-card"},[r("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[r("el-breadcrumb",{attrs:{"separator-class":"el-icon-arrow-right"}},[r("el-breadcrumb-item",{attrs:{to:{path:"/"}}},[e._v("首页")]),r("el-breadcrumb-item",[e._v("项目管理")]),r("el-breadcrumb-item",[e._v("项目列表")])],1)],1),r("el-card",{staticClass:"box-card"},[r("el-button",{attrs:{type:"primary",icon:"el-icon-plus"},on:{click:function(t){e.dialogCreate="true"}}},[e._v("创建项目")]),r("el-table",{staticStyle:{width:"100%","margin-bottom":"10px"},attrs:{data:e.projectList}},[r("el-table-column",{attrs:{prop:"id",label:"ID",width:"80",sortable:""}}),r("el-table-column",{attrs:{prop:"name",label:"项目名",width:"200"}}),r("el-table-column",{attrs:{prop:"desc",label:"描述信息",width:"280"}}),r("el-table-column",{attrs:{prop:"leader",label:"负责人",width:"100",sortable:""}}),r("el-table-column",{attrs:{prop:"tester",label:"测试人员",width:"100"}}),r("el-table-column",{attrs:{prop:"interfaces",label:"接口数量",width:"120",sortable:""}}),r("el-table-column",{attrs:{prop:"testcases",label:"用例数量",width:"80"}}),r("el-table-column",{attrs:{prop:"testsuits",label:"套件数量",width:"80"}}),r("el-table-column",{attrs:{label:"操作"},scopedSlots:e._u([{key:"default",fn:function(t){return[r("el-button",{attrs:{size:"mini"},on:{click:function(r){return e.proEdit(t.row)}}},[e._v("编辑")]),r("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(r){return e.proDelete(t.row.id)}}},[e._v("删除 ")])]}}])})],1),r("el-pagination",{attrs:{"current-page":e.page,"page-sizes":[5,10,20,30],"page-size":e.size,layout:"total, sizes, prev, pager, next, jumper",total:e.count},on:{"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}})],1)],1),r("el-dialog",{attrs:{title:"编辑项目",visible:e.dialogEdit,"close-on-click-modal":"false"},on:{"update:visible":function(t){e.dialogEdit=t}}},[r("el-form",{ref:"updateRef",attrs:{model:e.editProject,rules:e.caseRules,"label-width":"80px"}},[r("el-form-item",{attrs:{label:"项目名",prop:"name"}},[r("el-input",{attrs:{autocomplete:"off"},model:{value:e.editProject.name,callback:function(t){e.$set(e.editProject,"name",t)},expression:"editProject.name"}})],1),r("el-form-item",{attrs:{label:"负责人",prop:"leader"}},[r("el-input",{attrs:{autocomplete:"off"},model:{value:e.editProject.leader,callback:function(t){e.$set(e.editProject,"leader",t)},expression:"editProject.leader"}})],1),r("el-form-item",{attrs:{label:"测试人员",prop:"tester"}},[r("el-input",{attrs:{autocomplete:"off"},model:{value:e.editProject.tester,callback:function(t){e.$set(e.editProject,"tester",t)},expression:"editProject.tester"}})],1),r("el-form-item",{attrs:{label:"开发人员",prop:"programmer"}},[r("el-input",{attrs:{autocomplete:"off"},model:{value:e.editProject.programmer,callback:function(t){e.$set(e.editProject,"programmer",t)},expression:"editProject.programmer"}})],1),r("el-form-item",{attrs:{label:"发布应用",prop:"publish_app"}},[r("el-input",{attrs:{autocomplete:"off"},model:{value:e.editProject.publish_app,callback:function(t){e.$set(e.editProject,"publish_app",t)},expression:"editProject.publish_app"}})],1),r("el-form-item",{attrs:{label:"描述信息"}},[r("el-input",{attrs:{type:"textarea",autocomplete:"off"},model:{value:e.editProject.desc,callback:function(t){e.$set(e.editProject,"desc",t)},expression:"editProject.desc"}})],1)],1),r("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[r("el-button",{on:{click:function(t){e.dialogEdit=!1}}},[e._v("取 消")]),r("el-button",{attrs:{type:"primary"},on:{click:e.updateProject}},[e._v("确 定")])],1)],1),r("el-dialog",{ref:"createRef",attrs:{visible:e.dialogCreate,rules:e.caseRules},on:{"update:visible":function(t){e.dialogCreate=t}}},[r("template",{slot:"title"},[r("div",{staticStyle:{"text-align":"center",width:"100%","font-size":"24px"}},[e._v("创建项目")])]),r("el-form",{ref:"createRef",attrs:{model:e.newProject,"label-width":"80px",size:"mini",rules:e.caseRules}},[r("el-form-item",{attrs:{label:"项目名称",prop:"name"}},[r("el-input",{model:{value:e.newProject.name,callback:function(t){e.$set(e.newProject,"name",t)},expression:"newProject.name"}})],1),r("el-form-item",{attrs:{label:"测试者",prop:"tester"}},[r("el-input",{attrs:{autocomplete:"off"},model:{value:e.newProject.tester,callback:function(t){e.$set(e.newProject,"tester",t)},expression:"newProject.tester"}})],1),r("el-form-item",{attrs:{label:"负责人",prop:"leader"}},[r("el-input",{attrs:{autocomplete:"off"},model:{value:e.newProject.leader,callback:function(t){e.$set(e.newProject,"leader",t)},expression:"newProject.leader"}})],1),r("el-form-item",{attrs:{label:"开发人员",prop:"programmer"}},[r("el-input",{attrs:{autocomplete:"off"},model:{value:e.newProject.programmer,callback:function(t){e.$set(e.newProject,"programmer",t)},expression:"newProject.programmer"}})],1),r("el-form-item",{attrs:{label:"发布应用",prop:"publish_app"}},[r("el-input",{attrs:{autocomplete:"off"},model:{value:e.newProject.publish_app,callback:function(t){e.$set(e.newProject,"publish_app",t)},expression:"newProject.publish_app"}})],1),r("el-form-item",{attrs:{label:"项目描述"}},[r("el-input",{attrs:{type:"textarea",rows:5},model:{value:e.newProject.desc,callback:function(t){e.$set(e.newProject,"desc",t)},expression:"newProject.desc"}})],1)],1),r("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[r("el-button",{on:{click:function(t){e.dialogCreate=!1}}},[e._v("取 消")]),r("el-button",{attrs:{type:"primary"},on:{click:e.createProject}},[e._v("提 交")])],1)],2)],1)},o=[],a=r("5530"),i=r("1da1"),c=(r("96cf"),{data:function(){return{projectList:[],page:1,count:0,size:10,dialogEdit:!1,editProject:{},dialogCreate:!1,newProject:{name:"",leader:"",tester:"",programmer:"",publish_app:"",desc:""},caseRules:{name:[{required:!0,message:"项目名不能为空",trigger:"blur"}],leader:[{required:!0,message:"负责人不能为空",trigger:"blur"}],tester:[{required:!0,message:"测试人员不能为空",trigger:"blur"}],programmer:[{required:!0,message:"开发人员不能为空",trigger:"blur"}],publish_app:[{required:!0,message:"发布应用不能为空",trigger:"blur"}]}}},methods:{createProject:function(){var e=this;this.$refs.createRef.validate(function(){var t=Object(i["a"])(regeneratorRuntime.mark((function t(r){var n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:if(r){t.next=2;break}return t.abrupt("return");case 2:return t.next=4,e.$request.post("/projects/",e.newProject);case 4:n=t.sent,201===n.status?(e.$message({type:"success",message:"项目创建成功!",duration:1e3}),e.getProject(),e.dialogCreate=!1):(console.log(n),e.$message.error("服务端异常!"));case 6:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}())},proEdit:function(e){console.log(e),this.editProject=Object(a["a"])({},e),this.dialogEdit=!0},updateProject:function(){var e=this;return Object(i["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:e.$refs.updateRef.validate(function(){var t=Object(i["a"])(regeneratorRuntime.mark((function t(r){var n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:if(r){t.next=2;break}return t.abrupt("return");case 2:return t.next=4,e.$request.put("/projects/"+e.editProject.id+"/",e.editProject);case 4:n=t.sent,200===n.status?(e.$message({message:"修改项目成功",type:"success",duration:1e3}),e.getProject(),e.dialogEdit=!1):e.$message({message:"修改失败",type:"error",duration:1e3});case 6:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}());case 1:case"end":return t.stop()}}),t)})))()},proDelete:function(e){var t=this;return Object(i["a"])(regeneratorRuntime.mark((function r(){var n;return regeneratorRuntime.wrap((function(r){while(1)switch(r.prev=r.next){case 0:return console.log("当前删除的数据id为：",e),r.next=3,t.$request.delete("/projects/"+e+"/");case 3:n=r.sent,204===n.status?(t.$message({message:"删除成功",type:"success",duration:1e3}),t.getProject()):t.$message({message:"删除失败",type:"error",duration:1e3});case 5:case"end":return r.stop()}}),r)})))()},getProject:function(){var e=this;return Object(i["a"])(regeneratorRuntime.mark((function t(){var r;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,e.$request.get("/projects/",{params:{page:e.page,size:e.size}});case 2:if(r=t.sent,200===r.status){t.next=5;break}return t.abrupt("return",e.$message.error("服务器异常"));case 5:e.projectList=r.data.results,e.count=r.data.count,console.log(r);case 8:case"end":return t.stop()}}),t)})))()},handleSizeChange:function(e){this.size=e,this.page=1,this.getProject()},handleCurrentChange:function(e){this.page=e,this.getProject()}},mounted:function(){this.getProject()}}),s=c,l=r("2877"),u=Object(l["a"])(s,n,o,!1,null,null,null);t["default"]=u.exports},a4d3:function(e,t,r){"use strict";var n=r("23e7"),o=r("da84"),a=r("d066"),i=r("c430"),c=r("83ab"),s=r("4930"),l=r("fdbf"),u=r("d039"),f=r("5135"),p=r("e8b5"),d=r("861d"),b=r("825a"),m=r("7b0b"),g=r("fc6a"),h=r("c04e"),v=r("5c6c"),j=r("7c73"),w=r("df75"),y=r("241c"),P=r("057f"),O=r("7418"),x=r("06cf"),k=r("9bf2"),$=r("d1e7"),_=r("9112"),S=r("6eeb"),E=r("5692"),C=r("f772"),R=r("d012"),z=r("90e3"),D=r("b622"),q=r("e538"),A=r("746f"),N=r("d44e"),J=r("69f3"),I=r("b727").forEach,L=C("hidden"),F="Symbol",T="prototype",B=D("toPrimitive"),Q=J.set,W=J.getterFor(F),G=Object[T],H=o.Symbol,K=a("JSON","stringify"),M=x.f,U=k.f,V=P.f,X=$.f,Y=E("symbols"),Z=E("op-symbols"),ee=E("string-to-symbol-registry"),te=E("symbol-to-string-registry"),re=E("wks"),ne=o.QObject,oe=!ne||!ne[T]||!ne[T].findChild,ae=c&&u((function(){return 7!=j(U({},"a",{get:function(){return U(this,"a",{value:7}).a}})).a}))?function(e,t,r){var n=M(G,t);n&&delete G[t],U(e,t,r),n&&e!==G&&U(G,t,n)}:U,ie=function(e,t){var r=Y[e]=j(H[T]);return Q(r,{type:F,tag:e,description:t}),c||(r.description=t),r},ce=l?function(e){return"symbol"==typeof e}:function(e){return Object(e)instanceof H},se=function(e,t,r){e===G&&se(Z,t,r),b(e);var n=h(t,!0);return b(r),f(Y,n)?(r.enumerable?(f(e,L)&&e[L][n]&&(e[L][n]=!1),r=j(r,{enumerable:v(0,!1)})):(f(e,L)||U(e,L,v(1,{})),e[L][n]=!0),ae(e,n,r)):U(e,n,r)},le=function(e,t){b(e);var r=g(t),n=w(r).concat(be(r));return I(n,(function(t){c&&!fe.call(r,t)||se(e,t,r[t])})),e},ue=function(e,t){return void 0===t?j(e):le(j(e),t)},fe=function(e){var t=h(e,!0),r=X.call(this,t);return!(this===G&&f(Y,t)&&!f(Z,t))&&(!(r||!f(this,t)||!f(Y,t)||f(this,L)&&this[L][t])||r)},pe=function(e,t){var r=g(e),n=h(t,!0);if(r!==G||!f(Y,n)||f(Z,n)){var o=M(r,n);return!o||!f(Y,n)||f(r,L)&&r[L][n]||(o.enumerable=!0),o}},de=function(e){var t=V(g(e)),r=[];return I(t,(function(e){f(Y,e)||f(R,e)||r.push(e)})),r},be=function(e){var t=e===G,r=V(t?Z:g(e)),n=[];return I(r,(function(e){!f(Y,e)||t&&!f(G,e)||n.push(Y[e])})),n};if(s||(H=function(){if(this instanceof H)throw TypeError("Symbol is not a constructor");var e=arguments.length&&void 0!==arguments[0]?String(arguments[0]):void 0,t=z(e),r=function(e){this===G&&r.call(Z,e),f(this,L)&&f(this[L],t)&&(this[L][t]=!1),ae(this,t,v(1,e))};return c&&oe&&ae(G,t,{configurable:!0,set:r}),ie(t,e)},S(H[T],"toString",(function(){return W(this).tag})),S(H,"withoutSetter",(function(e){return ie(z(e),e)})),$.f=fe,k.f=se,x.f=pe,y.f=P.f=de,O.f=be,q.f=function(e){return ie(D(e),e)},c&&(U(H[T],"description",{configurable:!0,get:function(){return W(this).description}}),i||S(G,"propertyIsEnumerable",fe,{unsafe:!0}))),n({global:!0,wrap:!0,forced:!s,sham:!s},{Symbol:H}),I(w(re),(function(e){A(e)})),n({target:F,stat:!0,forced:!s},{for:function(e){var t=String(e);if(f(ee,t))return ee[t];var r=H(t);return ee[t]=r,te[r]=t,r},keyFor:function(e){if(!ce(e))throw TypeError(e+" is not a symbol");if(f(te,e))return te[e]},useSetter:function(){oe=!0},useSimple:function(){oe=!1}}),n({target:"Object",stat:!0,forced:!s,sham:!c},{create:ue,defineProperty:se,defineProperties:le,getOwnPropertyDescriptor:pe}),n({target:"Object",stat:!0,forced:!s},{getOwnPropertyNames:de,getOwnPropertySymbols:be}),n({target:"Object",stat:!0,forced:u((function(){O.f(1)}))},{getOwnPropertySymbols:function(e){return O.f(m(e))}}),K){var me=!s||u((function(){var e=H();return"[null]"!=K([e])||"{}"!=K({a:e})||"{}"!=K(Object(e))}));n({target:"JSON",stat:!0,forced:me},{stringify:function(e,t,r){var n,o=[e],a=1;while(arguments.length>a)o.push(arguments[a++]);if(n=t,(d(t)||void 0!==e)&&!ce(e))return p(t)||(t=function(e,t){if("function"==typeof n&&(t=n.call(this,e,t)),!ce(t))return t}),o[1]=t,K.apply(null,o)}})}H[T][B]||_(H[T],B,H[T].valueOf),N(H,F),R[L]=!0},a640:function(e,t,r){"use strict";var n=r("d039");e.exports=function(e,t){var r=[][e];return!!r&&n((function(){r.call(null,t||function(){throw 1},1)}))}},b64b:function(e,t,r){var n=r("23e7"),o=r("7b0b"),a=r("df75"),i=r("d039"),c=i((function(){a(1)}));n({target:"Object",stat:!0,forced:c},{keys:function(e){return a(o(e))}})},b727:function(e,t,r){var n=r("0366"),o=r("44ad"),a=r("7b0b"),i=r("50c4"),c=r("65f0"),s=[].push,l=function(e){var t=1==e,r=2==e,l=3==e,u=4==e,f=6==e,p=7==e,d=5==e||f;return function(b,m,g,h){for(var v,j,w=a(b),y=o(w),P=n(m,g,3),O=i(y.length),x=0,k=h||c,$=t?k(b,O):r||p?k(b,0):void 0;O>x;x++)if((d||x in y)&&(v=y[x],j=P(v,x,w),e))if(t)$[x]=j;else if(j)switch(e){case 3:return!0;case 5:return v;case 6:return x;case 2:s.call($,v)}else switch(e){case 4:return!1;case 7:s.call($,v)}return f?-1:l||u?u:$}};e.exports={forEach:l(0),map:l(1),filter:l(2),some:l(3),every:l(4),find:l(5),findIndex:l(6),filterOut:l(7)}},dbb4:function(e,t,r){var n=r("23e7"),o=r("83ab"),a=r("56ef"),i=r("fc6a"),c=r("06cf"),s=r("8418");n({target:"Object",stat:!0,sham:!o},{getOwnPropertyDescriptors:function(e){var t,r,n=i(e),o=c.f,l=a(n),u={},f=0;while(l.length>f)r=o(n,t=l[f++]),void 0!==r&&s(u,t,r);return u}})},e439:function(e,t,r){var n=r("23e7"),o=r("d039"),a=r("fc6a"),i=r("06cf").f,c=r("83ab"),s=o((function(){i(1)})),l=!c||s;n({target:"Object",stat:!0,forced:l,sham:!c},{getOwnPropertyDescriptor:function(e,t){return i(a(e),t)}})},e538:function(e,t,r){var n=r("b622");t.f=n},e8b5:function(e,t,r){var n=r("c6b6");e.exports=Array.isArray||function(e){return"Array"==n(e)}}}]);
//# sourceMappingURL=chunk-42582674.a5d8c124.js.map