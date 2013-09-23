#!/usr/bin/python

import mimetools
import multifile
import StringIO
import sys

img_eml = """
Return-Path: <all-bounces@mailman.softservecom.com>
X-Original-To: allalias@softservecom.com
Delivered-To: ygrabar@softservecom.com
Received: by mail-int.softservecom.com (Postfix)
	id 552951B4012; Fri, 14 Mar 2008 13:45:46 +0200 (EET)
Delivered-To: allalias@softservecom.com
Received: from mailman.softservecom.com (mailman.softservecom.com [192.168.2.73])
	by mail-int.softservecom.com (Postfix) with ESMTP id 3CFEC1B4011
	for <allalias@softservecom.com>; Fri, 14 Mar 2008 13:45:46 +0200 (EET)
Received: from mailman.softservecom.com (localhost.localdomain [127.0.0.1])
	by mailman.softservecom.com (Postfix) with ESMTP id 030844082
	for <allalias@softservecom.com>; Fri, 14 Mar 2008 13:55:52 +0200 (EET)
X-Original-To: all@mailman.softservecom.com
Delivered-To: all@mailman.softservecom.com
Received: from mail-int.softservecom.com (mail-int.softservecom.com
	[192.168.2.11])
	by mailman.softservecom.com (Postfix) with ESMTP id 6DC7D4082
	for <all@mailman.softservecom.com>;
	Fri, 14 Mar 2008 13:55:50 +0200 (EET)
Received: by mail-int.softservecom.com (Postfix, from userid 1144)
	id 77DBE1B4011; Fri, 14 Mar 2008 13:45:44 +0200 (EET)
X-Original-To: all@softservecom.com
Delivered-To: all@softservecom.com
Received: from Dio (dio.softservecom.com [192.168.16.171])
	by mail-int.softservecom.com (Postfix) with ESMTP id F30381B4011
	for <all@softservecom.com>; Fri, 14 Mar 2008 13:45:43 +0200 (EET)
From: "HR" <HR@softservecom.com>
To: "ALL" <all@softservecom.com>
Date: Fri, 14 Mar 2008 13:55:36 +0200
Message-ID: <000001c885ca$533fb070$ab10a8c0@softservecom.com>
MIME-Version: 1.0
Content-Type: multipart/related;
	boundary="----=_NextPart_000_0001_01C885DB.16C88070"
X-Mailer: Microsoft Office Outlook 11
Thread-Index: AccrWzslbnq/Gnf7TOKHUX95yTrCaAAADmlAAAHhjCAAu/9sIAYdQFNQAABEfAAAAQVMwAAAgLOgAAXMucAAhuP9cAAJqIegAAGXCXAALjMS4AFkW5MAAAG8eDAAJTE1YABFL/9QACFRylAAACeJ0ACUgdJgAACXpeAAACFi4AMDTg4gAIaleKAAAGWFYAAAJNbgAAEUg1AAABMq0AChl4VgAACBX/AAiogZcAAAWI6QAABe9CACL/XqIAAAUtkwACYyTCAAAFwnsAzLlzCgAAB9YxAAAAWOMAJaWgjQAABdhVAAAMo8sAAC5gswAATNU0AAJ+jTIAKRchYQAAYX1AAAh94lwAPAN0vgAAHT+fAAABSm0Ama3bVAAAPyS6AAABjJsAPoRQzQADLLbeAAbmx7AACMavEwADTmdiAAAIzBkAAAIQ2wAAEJE9AAAr7joAAAFw9QAAahDuAALpGCYAAAFoDgAAA0nSAAAF4N4AEBtsswAADCNzAAADL3YAc+7q7wAAT+f6ACWZX3sAACHe1QACa+9MAAB/Or0AAAOvcAAJZJqxAAAChAgAAAOjJgAAC85DAAABaXEAAAEHmgAAAXq7AAALU70AIi9b4QAAAdWlAAAAk6MAAtyStwAAAQnZAAAAxCoABmOKqQAAAt2VAAACVzsAAAKiVABVP1sNAAAIOuwAAAPtWgAAATMaACiCUoEAoE3uCQAAAwRnAAAB878AAANOgwAABoeMAAABElMAAADgXwAABES3AAADn+QA==
X-MimeOLE: Produced By Microsoft MimeOLE V6.00.2900.3198
Cc: 
Subject: [All] Outstanding Performance - Another Satisfied Customer!
X-BeenThere: all@mailman.softservecom.com
X-Mailman-Version: 2.1.5
Precedence: list
List-Id: All alias <all.mailman.softservecom.com>
List-Unsubscribe: <http://mailman.softservecom.com/mailman/listinfo/all>,
	<mailto:all-request@mailman.softservecom.com?subject=unsubscribe>
List-Archive: <http://mailman.softservecom.com/pipermail/all>
List-Post: <mailto:all@mailman.softservecom.com>
List-Help: <mailto:all-request@mailman.softservecom.com?subject=help>
List-Subscribe: <http://mailman.softservecom.com/mailman/listinfo/all>,
	<mailto:all-request@mailman.softservecom.com?subject=subscribe>
Sender: all-bounces@mailman.softservecom.com
Errors-To: all-bounces@mailman.softservecom.com

This is a multi-part message in MIME format.

------=_NextPart_000_0001_01C885DB.16C88070
Content-Type: multipart/alternative;
	boundary="----=_NextPart_001_0002_01C885DB.16D48E60"


------=_NextPart_001_0002_01C885DB.16D48E60
Content-Type: text/plain;
	charset="us-ascii"
Content-Transfer-Encoding: 7bit

 

 


Outstanding Performance - 

Another Satisfied Customer!

 





 

A big thank you to Steve and Mykola. They've been planning and testing for
months to make sure this launch went smoothly. Last night we made the
switchover, and everything went according to plan. The C4 cluster is now
running in production.

A brief description of what this means: We split our customers onto
different server groups, called clusters, so we don't overload any one
server with too much traffic. For the most part this is transparent to
customers - it affects the workbench URL and the content moderators, but not
the production sites. As we've continued to grow, our current clusters are
getting more and more heavily loaded. C4 is our newest cluster, taking some
of the bigger customers off of C1. This will give us room to grow as we
continue to add new customers. It's also the first new cluster in a year, so
Steve and Mykola were designing new processes as they went. We can reuse
those processes in the coming months, because we're already planning a C5
cluster and discussing C6 as well (love that growth curve).

Steve and Mykola, great job on the migration. Thanks for all the work that
went into it - the planning and communication and the flawless execution.
You really made it happen.

Paul DeVere
Director, Operations
Bazaarvoice, Inc.

 

A huge thanks to Mykola for masterminding this migration process and
executing its steps with very few errors.  Also thanks to our QA team for a
lot of on-demand regression testing at each stage.  Now we get to do this
again for C5 immediately.

 

Steve Verleye

Sr. Developer

Bazaarvoice, Inc.

 

 

 

Great work!

Brett A. Hurt
Founder and CEO
Bazaarvoice, Inc.

 

 

 

 

 

 


------=_NextPart_001_0002_01C885DB.16D48E60
Content-Type: text/html;
	charset="us-ascii"
Content-Transfer-Encoding: quoted-printable

<html xmlns:v=3D"urn:schemas-microsoft-com:vml" =
xmlns:o=3D"urn:schemas-microsoft-com:office:office" =
xmlns:w=3D"urn:schemas-microsoft-com:office:word" =
xmlns:x=3D"urn:schemas-microsoft-com:office:excel" =
xmlns:p=3D"urn:schemas-microsoft-com:office:powerpoint" =
xmlns:a=3D"urn:schemas-microsoft-com:office:access" =
xmlns:dt=3D"uuid:C2F41010-65B3-11d1-A29F-00AA00C14882" =
xmlns:s=3D"uuid:BDC6E3F0-6DA3-11d1-A2A3-00AA00C14882" =
xmlns:rs=3D"urn:schemas-microsoft-com:rowset" xmlns:z=3D"#RowsetSchema" =
xmlns:b=3D"urn:schemas-microsoft-com:office:publisher" =
xmlns:ss=3D"urn:schemas-microsoft-com:office:spreadsheet" =
xmlns:c=3D"urn:schemas-microsoft-com:office:component:spreadsheet" =
xmlns:oa=3D"urn:schemas-microsoft-com:office:activation" =
xmlns:html=3D"http://www.w3.org/TR/REC-html40" =
xmlns:q=3D"http://schemas.xmlsoap.org/soap/envelope/" xmlns:D=3D"DAV:" =
xmlns:x2=3D"http://schemas.microsoft.com/office/excel/2003/xml" =
xmlns:ois=3D"http://schemas.microsoft.com/sharepoint/soap/ois/" =
xmlns:dir=3D"http://schemas.microsoft.com/sharepoint/soap/directory/" =
xmlns:ds=3D"http://www.w3.org/2000/09/xmldsig#" =
xmlns:dsp=3D"http://schemas.microsoft.com/sharepoint/dsp" =
xmlns:udc=3D"http://schemas.microsoft.com/data/udc" =
xmlns:xsd=3D"http://www.w3.org/2001/XMLSchema" =
xmlns:sps=3D"http://schemas.microsoft.com/sharepoint/soap/" =
xmlns:xsi=3D"http://www.w3.org/2001/XMLSchema-instance" =
xmlns:udcxf=3D"http://schemas.microsoft.com/data/udc/xmlfile" =
xmlns=3D"http://www.w3.org/TR/REC-html40">

<head>
<meta name=3D"Microsoft Theme 2.00" content=3D"Breeze 011">
<meta http-equiv=3DContent-Type content=3D"text/html; =
charset=3Dus-ascii">
<meta name=3DGenerator content=3D"Microsoft Word 11 (filtered medium)">
<!--[if !mso]>
<style>
v\:* {behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
w\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style>
<![endif]-->
<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:Verdana;
	panose-1:2 11 6 4 3 5 4 4 2 4;}
@font-face
	{font-family:"Comic Sans MS";
	panose-1:3 15 7 2 3 3 2 2 2 4;}
@font-face
	{font-family:"Trebuchet MS";
	panose-1:2 11 6 3 2 2 2 2 2 4;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin:0in;
	margin-bottom:.0001pt;
	font-size:12.0pt;
	font-family:"Trebuchet MS";
	color:#E9E8ED;}
h1
	{margin-top:12.0pt;
	margin-right:0in;
	margin-bottom:3.0pt;
	margin-left:0in;
	font-size:16.0pt;
	font-family:"Trebuchet MS";
	color:#E9E8ED;
	font-weight:bold;}
h2
	{margin-top:12.0pt;
	margin-right:0in;
	margin-bottom:3.0pt;
	margin-left:0in;
	font-size:14.0pt;
	font-family:"Trebuchet MS";
	color:#E9E8ED;
	font-weight:normal;}
h3
	{margin-top:12.0pt;
	margin-right:0in;
	margin-bottom:3.0pt;
	margin-left:0in;
	font-size:13.0pt;
	font-family:"Trebuchet MS";
	color:#E9E8ED;
	font-weight:normal;}
h4
	{margin-top:12.0pt;
	margin-right:0in;
	margin-bottom:3.0pt;
	margin-left:0in;
	font-size:14.0pt;
	font-family:"Trebuchet MS";
	color:#E9E8ED;
	font-weight:normal;}
h5
	{margin-top:12.0pt;
	margin-right:0in;
	margin-bottom:3.0pt;
	margin-left:0in;
	font-size:13.0pt;
	font-family:"Trebuchet MS";
	color:#E9E8ED;
	font-weight:normal;}
h6
	{margin-top:12.0pt;
	margin-right:0in;
	margin-bottom:3.0pt;
	margin-left:0in;
	font-size:11.0pt;
	font-family:"Trebuchet MS";
	color:#E9E8ED;
	font-weight:normal;}
a:link, span.MsoHyperlink
	{color:#C0D8B8;
	text-decoration:underline;}
a:visited, span.MsoHyperlinkFollowed
	{color:#B685ED;
	text-decoration:underline;}
p.MsoPlainText, li.MsoPlainText, div.MsoPlainText
	{mso-margin-top-alt:auto;
	margin-right:0in;
	mso-margin-bottom-alt:auto;
	margin-left:0in;
	font-size:12.0pt;
	font-family:"Trebuchet MS";
	color:#E9E8ED;}
p.MsoAutoSig, li.MsoAutoSig, div.MsoAutoSig
	{mso-margin-top-alt:auto;
	margin-right:0in;
	mso-margin-bottom-alt:auto;
	margin-left:0in;
	font-size:12.0pt;
	font-family:"Trebuchet MS";
	color:#E9E8ED;}
p
	{mso-margin-top-alt:auto;
	margin-right:0in;
	mso-margin-bottom-alt:auto;
	margin-left:0in;
	font-size:12.0pt;
	font-family:"Times New Roman";}
span.EmailStyle20
	{mso-style-type:personal;
	font-family:"Times New Roman";
	color:windowtext;
	font-weight:normal;
	font-style:normal;
	text-decoration:none none;}
span.EmailStyle21
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle22
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle23
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle24
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle25
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle26
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle27
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle28
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle29
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle30
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle31
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle32
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle33
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle34
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle35
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle36
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle37
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle38
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle39
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle40
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle41
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle42
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle43
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle44
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle45
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle46
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle47
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle48
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle49
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle50
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle51
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle52
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle53
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle54
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle55
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle56
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle57
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle58
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle59
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle60
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle61
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle62
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle63
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle64
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle65
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle66
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle67
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle68
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle69
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle70
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle71
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle72
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle73
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle74
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle75
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle76
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle77
	{mso-style-type:personal;
	font-family:Verdana;
	color:blue;
	font-weight:normal;
	font-style:normal;
	text-decoration:none none;}
span.EmailStyle78
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle79
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle80
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle81
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle82
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle83
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle84
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle85
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle86
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle87
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle88
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle89
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle90
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle91
	{mso-style-type:personal;
	font-family:Verdana;
	color:blue;
	font-weight:normal;
	font-style:normal;
	text-decoration:none none;}
span.EmailStyle92
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle93
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle94
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle95
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle96
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle97
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle98
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle99
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle100
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle101
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle102
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle103
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle104
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle105
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle106
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle107
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle108
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle109
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle110
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle111
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle112
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle113
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle114
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle115
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle116
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle117
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle118
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle119
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle120
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle121
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle122
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle123
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle124
	{mso-style-type:personal;
	font-family:Arial;
	color:navy;}
span.EmailStyle125
	{mso-style-type:personal-reply;
	font-family:Arial;
	color:navy;}
@page Section1
	{size:595.3pt 841.9pt;
	margin:42.5pt 42.5pt 42.5pt 70.85pt;}
div.Section1
	{page:Section1;}
-->
</style>
<!--[if gte mso 9]><xml>
 <o:shapedefaults v:ext=3D"edit" spidmax=3D"1026">
  <o:colormenu v:ext=3D"edit" fillcolor=3D"white" />
 </o:shapedefaults></xml><![endif]--><!--[if gte mso 9]><xml>
 <o:shapelayout v:ext=3D"edit">
  <o:idmap v:ext=3D"edit" data=3D"1" />
 </o:shapelayout></xml><![endif]-->
</head>

<body bgcolor=3D"#CCECFF" =
background=3D"cid:image001.jpg@01C885D8.C3234D80"
lang=3DUK link=3D"#C0D8B8" vlink=3D"#B685ED">
<img src=3D"cid:image001.jpg@01C885D8.C3234D80"
v:src=3D"cid:image001.jpg@01C885D8.C3234D80" v:shapes=3D"_x0000_Mail" =
width=3D0
height=3D0 class=3Dshape style=3D'display:none;width:0;height:0'>

<div class=3DSection1>

<p class=3DMsoNormal><font size=3D2 color=3Dnavy face=3DArial><span =
style=3D'font-size:
10.0pt;font-family:Arial;color:navy'><o:p>&nbsp;</o:p></span></font></p>

<table class=3DMsoNormalTable border=3D0 cellspacing=3D0 cellpadding=3D0
 style=3D'margin-left:.2in;border-collapse:collapse'>
 <tr height=3D47 style=3D'height:35.3pt'>
  <td width=3D708 height=3D47 valign=3Dtop =
style=3D'width:531.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:35.3pt'>
  <p class=3DMsoNormal align=3Dcenter =
style=3D'margin-left:14.3pt;text-align:center'><b><font
  size=3D7 color=3Dred face=3D"Comic Sans MS"><span lang=3DEN-US =
style=3D'font-size:32.0pt;
  font-family:"Comic Sans MS";color:red;font-weight:bold'>Outstanding
  Performance - <o:p></o:p></span></font></b></p>
  <p class=3DMsoNormal align=3Dcenter =
style=3D'text-align:center'><b><font size=3D7
  color=3Dred face=3D"Comic Sans MS"><span lang=3DEN-US =
style=3D'font-size:32.0pt;
  font-family:"Comic Sans MS";color:red;font-weight:bold'>Another =
Satisfied
  Customer</span></font></b><b><font size=3D6 color=3Dred face=3D"Comic =
Sans MS"><span
  lang=3DEN-US style=3D'font-size:28.0pt;font-family:"Comic Sans =
MS";color:red;
  font-weight:bold'>!<o:p></o:p></span></font></b></p>
  </td>
  <td width=3D16 height=3D47 style=3D'width:12.2pt;padding:0in 0in 0in =
0in;
  height:35.3pt'>
  <p class=3DMsoNormal><font size=3D3 color=3D"#e9e8ed" =
face=3D"Trebuchet MS"><span
  style=3D'font-size:12.0pt'>&nbsp;<o:p></o:p></span></font></p>
  </td>
 </tr>
 <tr height=3D402 style=3D'height:301.7pt'>
  <td width=3D724 colspan=3D2 height=3D402 valign=3Dtop =
style=3D'width:543.2pt;
  padding:0in 5.4pt 0in 5.4pt;height:301.7pt'>
  <p class=3DMsoNormal align=3Dcenter =
style=3D'mso-margin-top-alt:0in;margin-right:
  12.95pt;margin-bottom:0in;margin-left:-5.4pt;margin-bottom:.0001pt;
  text-align:center'><font size=3D3 color=3D"#e9e8ed" face=3D"Trebuchet =
MS"><span
  lang=3DEN-US style=3D'font-size:12.0pt'><img width=3D637 height=3D441
  id=3D"_x0000_i1182" =
src=3D"cid:image002.jpg@01C885D8.C3234D80"><o:p></o:p></span></font></p>
  </td>
 </tr>
 <tr height=3D163 style=3D'height:122.15pt'>
  <td width=3D708 height=3D163 valign=3Dtop =
style=3D'width:531.0pt;padding:0in 5.4pt 0in 5.4pt;
  height:122.15pt'>
  <p class=3DMsoNormal><font size=3D3 color=3Dblue face=3D"Comic Sans =
MS"><span
  lang=3DEN-US style=3D'font-size:12.0pt;font-family:"Comic Sans =
MS";color:blue'><o:p>&nbsp;</o:p></span></font></p>
  <p =
style=3D'mso-margin-top-alt:0in;margin-right:0in;margin-bottom:12.0pt;
  margin-left:0in'><font size=3D3 color=3Dblue face=3D"Comic Sans =
MS"><span
  lang=3DEN-US style=3D'font-size:12.0pt;font-family:"Comic Sans =
MS";color:blue'>A
  big thank you to Steve and Mykola. They&#8217;ve been planning and =
testing for
  months to make sure this launch went smoothly. Last night we made the
  switchover, and everything went according to plan. The C4 cluster is =
now
  running in production.<br>
  <br>
  A brief description of what this means: We split our customers onto =
different
  server groups, called clusters, so we don&#8217;t overload any one =
server
  with too much traffic. For the most part this is transparent to =
customers
  &#8211; it affects the workbench URL and the content moderators, but =
not the
  production sites. As we&#8217;ve continued to grow, our current =
clusters are
  getting more and more heavily loaded. C4 is our newest cluster, taking =
some
  of the bigger customers off of C1. This will give us room to grow as =
we
  continue to add new customers. It&#8217;s also the first new cluster =
in a
  year, so Steve and Mykola were designing new processes as they went. =
We can
  reuse those processes in the coming months, because we&#8217;re =
already
  planning a C5 cluster and discussing C6 as well (love that growth =
curve).<br>
  <br>
  Steve and Mykola, great job on the migration. Thanks for all the work =
that
  went into it &#8211; the planning and communication and the flawless
  execution. You really made it happen.<br>
  <br>
  </span></font><b><font color=3Dgreen face=3D"Comic Sans MS"><span =
lang=3DEN-US
  style=3D'font-family:"Comic Sans =
MS";color:green;font-weight:bold'>Paul DeVere<br>
  Director, Operations<br>
  Bazaarvoice, Inc.</span></font></b><font color=3Dblue face=3D"Comic =
Sans MS"><span
  lang=3DEN-US style=3D'font-family:"Comic Sans =
MS";color:blue'><o:p></o:p></span></font></p>
  <p =
style=3D'mso-margin-top-alt:0in;margin-right:0in;margin-bottom:12.0pt;
  margin-left:0in'><font size=3D3 color=3Dblue face=3D"Comic Sans =
MS"><span
  lang=3DEN-US style=3D'font-size:12.0pt;font-family:"Comic Sans =
MS";color:blue'><o:p>&nbsp;</o:p></span></font></p>
  <p class=3DMsoNormal><font size=3D3 color=3Dblue face=3D"Comic Sans =
MS"><span
  lang=3DEN-US style=3D'font-size:12.0pt;font-family:"Comic Sans =
MS";color:blue'>A
  huge thanks to Mykola for masterminding this migration process and =
executing
  its steps with very few errors. &nbsp;Also thanks to our QA team for a =
lot of
  on-demand regression testing at each stage. &nbsp;Now we get to do =
this again
  for C5 immediately.<o:p></o:p></span></font></p>
  <p class=3DMsoNormal><font size=3D3 color=3Dblue face=3D"Comic Sans =
MS"><span
  lang=3DEN-US style=3D'font-size:12.0pt;font-family:"Comic Sans =
MS";color:blue'><o:p>&nbsp;</o:p></span></font></p>
  <p class=3DMsoNormal><b><font size=3D3 color=3Dgreen face=3D"Comic =
Sans MS"><span
  lang=3DEN-US style=3D'font-size:12.0pt;font-family:"Comic Sans =
MS";color:green;
  font-weight:bold'>Steve Verleye<o:p></o:p></span></font></b></p>
  <p class=3DMsoNormal><b><font size=3D3 color=3Dgreen face=3D"Comic =
Sans MS"><span
  lang=3DEN-US style=3D'font-size:12.0pt;font-family:"Comic Sans =
MS";color:green;
  font-weight:bold'>Sr. Developer<o:p></o:p></span></font></b></p>
  <p style=3D'margin:0in;margin-bottom:.0001pt'><b><font size=3D3 =
color=3Dgreen
  face=3D"Comic Sans MS"><span lang=3DEN-US =
style=3D'font-size:12.0pt;font-family:
  "Comic Sans MS";color:green;font-weight:bold'>Bazaarvoice, =
Inc.<o:p></o:p></span></font></b></p>
  <p style=3D'margin:0in;margin-bottom:.0001pt'><font size=3D3 =
color=3Dnavy
  face=3D"Comic Sans MS"><span lang=3DEN-US =
style=3D'font-size:12.0pt;font-family:
  "Comic Sans MS";color:navy'><o:p>&nbsp;</o:p></span></font></p>
  <p style=3D'margin:0in;margin-bottom:.0001pt'><font size=3D2 =
color=3Dnavy
  face=3DArial><span lang=3DEN-US =
style=3D'font-size:10.0pt;font-family:Arial;
  color:navy'><o:p>&nbsp;</o:p></span></font></p>
  <p style=3D'margin:0in;margin-bottom:.0001pt'><font size=3D3 =
color=3Dblue
  face=3D"Comic Sans MS"><span lang=3DEN-US =
style=3D'font-size:12.0pt;font-family:
  "Comic Sans MS";color:blue'><o:p>&nbsp;</o:p></span></font></p>
  <p style=3D'margin:0in;margin-bottom:.0001pt'><font size=3D3 =
color=3Dblue
  face=3D"Comic Sans MS"><span lang=3DEN-US =
style=3D'font-size:12.0pt;font-family:
  "Comic Sans MS";color:blue'>Great work!<br>
  <br>
  </span></font><b><font color=3Dgreen face=3D"Comic Sans MS"><span =
lang=3DEN-US
  style=3D'font-family:"Comic Sans =
MS";color:green;font-weight:bold'>Brett A.
  Hurt<br>
  Founder and CEO<br>
  Bazaarvoice, Inc.</span></font></b><b><font color=3Dblue face=3D"Comic =
Sans MS"><span
  lang=3DEN-US style=3D'font-family:"Comic Sans =
MS";color:blue;font-weight:bold'><o:p></o:p></span></font></b></p>
  <p class=3DMsoNormal style=3D'margin-left:.8pt'><b><font size=3D3 =
color=3Dteal
  face=3D"Comic Sans MS"><span lang=3DEN-US =
style=3D'font-size:12.0pt;font-family:
  "Comic Sans =
MS";color:teal;font-weight:bold'>&nbsp;<o:p></o:p></span></font></b></p>
  <p class=3DMsoNormal><font size=3D2 color=3D"#e9e8ed" =
face=3DArial><span lang=3DEN-US
  =
style=3D'font-size:10.0pt;font-family:Arial'><o:p>&nbsp;</o:p></span></fo=
nt></p>
  <p class=3DMsoNormal><b><font size=3D3 color=3Dteal face=3D"Comic Sans =
MS"><span
  lang=3DEN-US style=3D'font-size:12.0pt;font-family:"Comic Sans =
MS";color:teal;
  font-weight:bold'><o:p>&nbsp;</o:p></span></font></b></p>
  <p class=3DMsoNormal><font size=3D3 color=3D"#e9e8ed" =
face=3D"Trebuchet MS"><span
  lang=3DEN-US =
style=3D'font-size:12.0pt'><o:p>&nbsp;</o:p></span></font></p>
  </td>
  <td width=3D16 height=3D163 style=3D'width:12.2pt;padding:0in 0in 0in =
0in;
  height:122.15pt'>
  <p class=3DMsoNormal><font size=3D3 color=3D"#e9e8ed" =
face=3D"Trebuchet MS"><span
  style=3D'font-size:12.0pt'>&nbsp;<o:p></o:p></span></font></p>
  </td>
 </tr>
</table>

<p class=3DMsoNormal><font size=3D2 color=3Dnavy face=3DArial><span =
lang=3DEN-US
style=3D'font-size:10.0pt;font-family:Arial;color:navy'><o:p>&nbsp;</o:p>=
</span></font></p>

</div>

</body>

</html>

------=_NextPart_001_0002_01C885DB.16D48E60--

------=_NextPart_000_0001_01C885DB.16C88070
Content-Type: image/jpeg;
	name="image001.jpg"
Content-Transfer-Encoding: base64
Content-ID: <image001.jpg@01C885D8.C3234D80>

/9j/4AAQSkZJRgABAQEASwBLAAD/4wMOTVNPIFBhbGV0dGUguN37wOD7xeH7x+P7y+P7y+T7zeX7
z+b70eX70uf71Of71uj71+f72Oj72On72ur73On73er73uv73uz74ev74ez75Oz75O775+z75+/7
6u/77PH77e/78fL78/T7+ff7qtj7sNr7s9v7tNz7ttv7t937t977uN/7ut77u937u9/7vOD7vd77
vt77vuD7v+H7wN77wOL7weD7weH7wuH7wuL7w9/7w+H7w+L7xOH7xOL7xOP7xeL7xeP7xeT7xuD7
xuH7xuL7xuP7x+L7x+T7x+X7yOL7yOP7yOT7yeH7yeP7yeT7yeX7yuL7yuT7yuX7yub7y+X7zOP7
zOT7zOX7zOb7zOf7zeP7zeT7zeb7zef7zuT7zuX7zub7zuf7zuj7z+P7z+X7z+f7z+j70OT70OX7
0Ob70Of70eb70ef70ej70uT70ub70uj70+T70+b70+f70+j70+n71Ob71Oj71eb71ef71ej71en7
1uX71uf71un71+j71+n71+r72Ob72Of72Or72Ov72ej72en72er72uj72un72uv72uz72+f72+n7
2+r72+v73Oj73Or73Ov73Oz73O373ej73en73ev73ez73uj73ur73u373+r73+v73+z73+373+77
4On74Or74Ov74Oz74O374O774e374e774ur74uv74uz74u374+v74+z74+374+774+/75Ov75O37
5PD75ev75ez75e375e775e/75u375u775u/75vD75+375+775/D75/H76O776O/76PD76PH76e77
6e/76fD76fH76uz76u776vD76vH76vL76+776+/76/D76/H77O777PD77PL77e777fD77fH77fL7
7fP77vD77vH77vL77vT77/H77/L77/P78O/78PH78PL78PP78PX78fH78fP78fT78vL78vP78vT7
8vX78/H78/P78/b79PP79PT79PX79fL79fP79fb79vT79vf79/X7+Pb7+fT7+fj7+/b7+/j7/vj7
/vr7/vz7/9sAQwALCAgKCAcLCgkKDQwLDREcEhEPDxEiGRoUHCkkKyooJCcnLTJANy0wPTAnJzhM
OT1DRUhJSCs2T1VORlRAR0hF/9sAQwEMDQ0RDxEhEhIhRS4nLkVFRUVFRUVFRUVFRUVFRUVFRUVF
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

------=_NextPart_000_0001_01C885DB.16C88070
Content-Type: image/jpeg;
	name="image002.jpg"
Content-Transfer-Encoding: base64
Content-ID: <image002.jpg@01C885D8.C3234D80>

/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAoHBwgHBgoICAgLCgoLDhgQDg0NDh0VFhEYIx8lJCIf
IiEmKzcvJik0KSEiMEExNDk7Pj4+JS5ESUM8SDc9Pjv/2wBDAQoLCw4NDhwQEBw7KCIoOzs7Ozs7
Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozv/wAARCAG5An0DASIA
AhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQA
AAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3
ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWm
p6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEA
AwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSEx
BhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElK
U1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3
uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD1SlpK
dUAFLSUtAC0UUUALS0lLQAUtJS0CAUtFFAwpaSloAKWkooAWiiigAooooAKKKKACiikoAWkoooAK
KKSmAUUUUgEooooASkNKaSgApKKKAEoooNIBDSUUlMANJmg0hoAQmkJozVa8vreyiMlxKqD36n8K
ALGaTNc1c+N9JijZkmMj5wEC80tt4tjlwZYigb1qeeI7M6OkqvbX1vdD91ICfTvU9VcQUhopDQAh
NNzSmmmgANNNLTTQAhNIaU000AIaaTSmmmgBDTTSmmmgBDTTSmmmgBDTDTjTTQA00w0400mgBpph
pxppoAaaYTTjTTQAw1Wu32wH3OKstVC+flV/GgCqTzTCaVjTCaYDWOWJ9OKi+9KPRRmnMePrzUaH
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
3NA70zvVJEtgWANN3t2GKVPv0p61RJ//2Q==

------=_NextPart_000_0001_01C885DB.16C88070--
"""




def extract_mime_part_matching(stream, mimetype):
    """Return the first element in a multipart MIME message on stream
    matching mimetype."""

    msg = mimetools.Message(stream)
    msgtype = msg.gettype()
    params = msg.getplist()

    data = StringIO.StringIO()
    if msgtype[:10] == "multipart/":

        file = multifile.MultiFile(stream)
        file.push(msg.getparam("boundary"))
        while file.next():
            submsg = mimetools.Message(file)
            try:
                data = StringIO.StringIO()
                mimetools.decode(file, data, submsg.getencoding())
            except ValueError:
                continue
            if submsg.gettype() == mimetype:
                break
        file.pop()
    return data.getvalue()

if __name__ == '__main__':
    extract_mime_part_matching(img_eml, "image/jpeg")
    

