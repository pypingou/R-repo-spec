%global packname  gamlss.dist
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          4.1.0
Release:          1%{?dist}
Summary:          Distributions to be used for GAMLSS modelling.

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
This package contains the distributions for GAMLSS modelling.

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
%doc %{rlibdir}/gamlss.dist/html
%doc %{rlibdir}/gamlss.dist/DESCRIPTION
%doc %{rlibdir}/gamlss.dist/doc
%{rlibdir}/gamlss.dist/INDEX
%{rlibdir}/gamlss.dist/help
%{rlibdir}/gamlss.dist/NAMESPACE
%{rlibdir}/gamlss.dist/libs
%{rlibdir}/gamlss.dist/R
%{rlibdir}/gamlss.dist/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.1.0-1
- initial package for Fedora