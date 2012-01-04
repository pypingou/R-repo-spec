%global packname  ncvreg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.3.2
Release:          1%{?dist}
Summary:          Regularization paths for SCAD- and MCP-penalized regression models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.3-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Efficient algorithms for fitting regularization paths for linear or
logistic regression models penalized by MCP or SCAD, with optional
additional L2 penalty ("Mnet").

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
%doc %{rlibdir}/ncvreg/CITATION
%doc %{rlibdir}/ncvreg/NEWS
%doc %{rlibdir}/ncvreg/html
%doc %{rlibdir}/ncvreg/DESCRIPTION
%{rlibdir}/ncvreg/NAMESPACE
%{rlibdir}/ncvreg/INDEX
%{rlibdir}/ncvreg/help
%{rlibdir}/ncvreg/Meta
%{rlibdir}/ncvreg/data
%{rlibdir}/ncvreg/R
%{rlibdir}/ncvreg/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.2-1
- initial package for Fedora