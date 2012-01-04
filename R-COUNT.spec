%global packname  COUNT
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Functions, data and code for count data.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Functions, data and code for Hilbe, J.M. 2009. Negative Binomial
Regression, 2nd Edition (Cambridge University Press)

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
%doc %{rlibdir}/COUNT/html
%doc %{rlibdir}/COUNT/DESCRIPTION
%{rlibdir}/COUNT/R
%{rlibdir}/COUNT/Meta
%{rlibdir}/COUNT/HILBE_SCRIPTS
%{rlibdir}/COUNT/data
%{rlibdir}/COUNT/INDEX
%{rlibdir}/COUNT/help
%{rlibdir}/COUNT/HILBE_NBR2_FIGURES
%{rlibdir}/COUNT/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora