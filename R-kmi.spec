%global packname  kmi
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          Kaplan-Meier multiple imputation for the analysis of cumulative incidence functions in the competing risks setting

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival R-mitools 

BuildRequires:    R-devel tex(latex) R-survival R-mitools 

%description
The package performs a Kaplan-Meier multiple imputation to recover the
missing potential censoring information from competing risks events, so
that standard right-censored methods could be applied to the imputed data
sets to perform analyses of the cumulative incidence functions.

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
%doc %{rlibdir}/kmi/html
%doc %{rlibdir}/kmi/DESCRIPTION
%{rlibdir}/kmi/NAMESPACE
%{rlibdir}/kmi/data
%{rlibdir}/kmi/INDEX
%{rlibdir}/kmi/help
%{rlibdir}/kmi/Meta
%{rlibdir}/kmi/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.4-1
- initial package for Fedora