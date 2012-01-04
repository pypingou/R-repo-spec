%global packname  bmem
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Mediation analysis with missing data using bootstrap

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-sem R-Amelia R-MASS 


BuildRequires:    R-devel tex(latex) R-sem R-Amelia R-MASS



%description
Four methods for mediation analysis with missing data: Listwise deletion,
Pairwise deletion, Multiple imputation, and Two Stage Maximum Likelihood
algorithm. For MI and TS-ML, auxiliary variables can be included.
Bootstrap confidence intervals for mediation effects are obtained. The
robust method is also implemented for TS-ML.

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
%doc %{rlibdir}/bmem/html
%doc %{rlibdir}/bmem/DESCRIPTION
%{rlibdir}/bmem/NAMESPACE
%{rlibdir}/bmem/help
%{rlibdir}/bmem/Meta
%{rlibdir}/bmem/INDEX
%{rlibdir}/bmem/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- initial package for Fedora