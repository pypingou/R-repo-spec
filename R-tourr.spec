%global packname  tourr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          Implement tour methods in pure R code

Group:            Applications/Engineering 
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Implements geodesic interpolation and basis generation functions that
allow you to create new tour methods from R.

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
%doc %{rlibdir}/tourr/NEWS
%doc %{rlibdir}/tourr/html
%doc %{rlibdir}/tourr/CITATION
%doc %{rlibdir}/tourr/DESCRIPTION
%{rlibdir}/tourr/help
%{rlibdir}/tourr/tests
%{rlibdir}/tourr/data
%{rlibdir}/tourr/NAMESPACE
%{rlibdir}/tourr/Meta
%{rlibdir}/tourr/INDEX
%{rlibdir}/tourr/R
%{rlibdir}/tourr/util

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5-1
- initial package for Fedora