(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-b5420b60"],{4645:function(t,e,n){"use strict";n("7439")},"57da":function(t,e,n){"use strict";n.r(e);var s=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("el-container",[n("el-header",[n("div",{staticClass:"title"},[t._v(" 接 口 自 动 化 测 试 平 台 ")]),n("div",{staticClass:"logonout"},[n("el-popconfirm",{attrs:{title:"确认退出登录？"},on:{confirm:function(e){return t.loginout()}}},[n("div",{attrs:{slot:"reference"},slot:"reference"},[t._v("退出登录")])])],1)]),n("el-container",[n("el-aside",{attrs:{width:"250px"}},[n("el-menu",{staticClass:"el-menu-demo",attrs:{router:t.rou,"background-color":"#555500","default-active":t.activeMenu,"text-color":"#fff","active-text-color":"#00aaff","unique-opened":""}},[n("el-submenu",{attrs:{index:"projectManage"}},[n("template",{slot:"title"},[n("i",{staticClass:"el-icon-s-home"}),n("span",[t._v("项目管理")])]),n("el-menu-item",{attrs:{index:"/projects"}},[n("template",{slot:"title"},[n("i",{staticClass:"el-icon-document-copy"}),n("span",[t._v("项目列表")])])],2)],2),n("el-submenu",{attrs:{index:"interfacaseManage"}},[n("template",{slot:"title"},[n("i",{staticClass:"el-icon-folder-opened"}),n("span",[t._v("接口管理")])]),n("el-menu-item",{attrs:{index:"/interface"}},[n("template",{slot:"title"},[n("i",{staticClass:"el-icon-tickets"}),n("span",[t._v("接口列表")])])],2)],2),n("el-submenu",{attrs:{index:"caseManage"}},[n("template",{slot:"title"},[n("i",{staticClass:"el-icon-notebook-2"}),n("span",[t._v("用例管理")])]),n("el-menu-item",{attrs:{index:"/cases"}},[n("template",{slot:"title"},[n("i",{staticClass:"el-icon-notebook-1"}),n("span",[t._v("用例列表")])])],2)],2)],1)],1),n("el-main",{staticStyle:{padding:"0 5px"}},[n("router-view")],1)],1)],1)},a=[],i={data:function(){return{rou:!0,activeMenu:"/dprojects"}},methods:{loginout:function(){window.sessionStorage.removeItem("token"),this.$router.push("/login")}}},o=i,l=(n("4645"),n("2877")),c=Object(l["a"])(o,s,a,!1,null,"3f719eb5",null);e["default"]=c.exports},7439:function(t,e,n){}}]);
//# sourceMappingURL=chunk-b5420b60.5ea5b71d.js.map