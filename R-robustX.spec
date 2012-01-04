%global packname  robustX
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          eXperimental eXtraneous eXtraordinary ... Functionality for Robust Statistics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-robustbase 


BuildRequires:    R-devel tex(latex) R-robustbase



%description
eXperimental eXtraneous eXtraordinary Functionality for Robust Statistics

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
%doc %{rlibdir}/robustX/html
%doc %{rlibdir}/robustX/DESCRIPTION
%{rlibdir}/robustX/Meta
%{rlibdir}/robustX/R
%{rlibdir}/robustX/help
%{rlibdir}/robustX/NAMESPACE
%{rlibdir}/robustX/demo
%{rlibdir}/robustX/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora