%global packname  LIM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.2
Release:          1%{?dist}
Summary:          Linear Inverse Model examples and solution methods.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-limSolve R-diagram 

BuildRequires:    R-devel tex(latex) R-limSolve R-diagram 

%description
Functions that read and solve linear inverse problems (food web problems,
linear programming problems). These problems find solutions to linear or
quadratic functions: min or max (f(x)), where f(x) = ||Ax-b||^2 or f(x) =
sum(ai*xi) subject to equality constraints Ex=f and inequality constraints
Gx>=h. Uses package limSolve.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.2-1
- initial package for Fedora