%global packname  goalprog
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Weighted and lexicographical goal programming and optimization

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lpSolve 

BuildRequires:    R-devel tex(latex) R-lpSolve 

%description
A collection of functions to solve weighted and lexicographical goal
programming problems as specified by Lee (1972) and Ignizio (1976).

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
%doc %{rlibdir}/goalprog/html
%doc %{rlibdir}/goalprog/DESCRIPTION
%{rlibdir}/goalprog/NAMESPACE
%{rlibdir}/goalprog/help
%{rlibdir}/goalprog/INDEX
%{rlibdir}/goalprog/Meta
%{rlibdir}/goalprog/data
%{rlibdir}/goalprog/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora