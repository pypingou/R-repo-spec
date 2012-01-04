%global packname  cvTools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Cross-validation tools for regression models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-robustbase 

BuildRequires:    R-devel tex(latex) R-lattice R-robustbase 

%description
Tools that allow developers to write functions for cross-validation with
minimal programming effort and assist users with model selection.

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
%doc %{rlibdir}/cvTools/html
%doc %{rlibdir}/cvTools/DESCRIPTION
%doc %{rlibdir}/cvTools/doc
%{rlibdir}/cvTools/NAMESPACE
%{rlibdir}/cvTools/INDEX
%{rlibdir}/cvTools/Meta
%{rlibdir}/cvTools/help
%{rlibdir}/cvTools/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora