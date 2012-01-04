%global packname  exactLoglinTest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.7
Release:          1%{?dist}
Summary:          Monte Carlo Exact Tests for Log-linear models

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Monte Carlo and MCMC goodness of fit tests for log-linear models

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
%doc %{rlibdir}/exactLoglinTest/DESCRIPTION
%doc %{rlibdir}/exactLoglinTest/doc
%doc %{rlibdir}/exactLoglinTest/html
%{rlibdir}/exactLoglinTest/R
%{rlibdir}/exactLoglinTest/INDEX
%{rlibdir}/exactLoglinTest/Meta
%{rlibdir}/exactLoglinTest/data
%{rlibdir}/exactLoglinTest/libs
%{rlibdir}/exactLoglinTest/NAMESPACE
%{rlibdir}/exactLoglinTest/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.7-1
- initial package for Fedora