%global packname  giRaph
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          The giRaph package for graph representation in R

Group:            Applications/Engineering 
License:          GPL Version 2 or later.
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-methods 

BuildRequires:    R-devel tex(latex) R-graphics R-methods 

%description
Supply classes and methods to represent and manipulate graphs

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
%doc %{rlibdir}/giRaph/html
%doc %{rlibdir}/giRaph/DESCRIPTION
%{rlibdir}/giRaph/demo
%{rlibdir}/giRaph/R
%{rlibdir}/giRaph/NAMESPACE
%{rlibdir}/giRaph/help
%{rlibdir}/giRaph/Meta
%{rlibdir}/giRaph/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora