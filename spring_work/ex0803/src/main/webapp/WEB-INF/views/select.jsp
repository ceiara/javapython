<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Home</title>
<link
	href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css"
	rel="stylesheet"
	integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx"
	crossorigin="anonymous">
<script
	src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"
	integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa"
	crossorigin="anonymous"></script>
</head>
<body>
	<div class="container">
		<h1>Hello world!</h1>
		<p>The time on the server is ${serverTime}.</p>
		<nav aria-label="breadcrumb">
			<ol class="breadcrumb">
				<li class="breadcrumb-item"><a href="/myapp/">Home</a></li>
				<li class="breadcrumb-item"><a href="/myapp/insert">Insert</a></li>
				<li class="breadcrumb-item active" aria-current="/myapp/select">Select</li>
			</ol>
		</nav>
		<div class="m-3 p-3 border">
			<table class="table table-dark">
				<thead>
					<tr>
						<th>Index</th>
						<th>Email</th>
						<th>Name</th>
						<th>Password</th> 
						<th>Regdata</th>
					</tr>
				</thead>
				<tbody>
					<c:forEach var="i" items="${list}">
						<tr>
							<td>${i.id}</td>
							<td>${i.email}</td>
							<td>${i.name}</td>
							<td>${i.password}</td>
							<td>${i.regdata}</td>
						</tr>
					</c:forEach>
				</tbody>
			</table>
		</div>
	</div>
</body>
</html>