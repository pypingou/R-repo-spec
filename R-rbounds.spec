%global packname  rbounds
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9
Release:          1%{?dist}
Summary:          Perform Rosenbaum bounds sensitivity tests for matched and unmatched data.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Matching 

BuildRequires:    R-devel tex(latex) R-Matching 

%description
Takes matched and umatched data and calculates Rosenbaum bounds for the
treatment effect.  Calculates bounds for binary data, Hodges-Lehmann point
estimates, Wilcoxon signed-rank test for matched data and matched IV
estimators, and for data with multiple matched controls.  Is designed to
work with the Matching package and operate on Match() objects.

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
%doc %{rlibdir}/rbounds/html
%doc %{rlibdir}/rbounds/DESCRIPTION
%{rlibdir}/rbounds/INDEX
%{rlibdir}/rbounds/data
%{rlibdir}/rbounds/Meta
%{rlibdir}/rbounds/R
%{rlibdir}/rbounds/NAMESPACE
%{rlibdir}/rbounds/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9-1
- initial package for Fedora