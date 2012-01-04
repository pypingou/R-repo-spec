%global packname  powerSurvEpi
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          Power and sample size calculation for survival analysis of epidemiological studies

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package includes a set of functions to calculate power and sample
size for testing main effect or interaction effect in the survival
analysis of epidemiological studies (non-randomized studies), taking into
account the correlation between the covariate of the interest and other
covariates. Some calculations also take into account the competing risks.
This package also includes a set of functions to calculate power and
sample size for testing main effect in the survival analysis of randomized
clinical trials.

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
%doc %{rlibdir}/powerSurvEpi/html
%doc %{rlibdir}/powerSurvEpi/DESCRIPTION
%{rlibdir}/powerSurvEpi/help
%{rlibdir}/powerSurvEpi/INDEX
%{rlibdir}/powerSurvEpi/R
%{rlibdir}/powerSurvEpi/NAMESPACE
%{rlibdir}/powerSurvEpi/Meta
%{rlibdir}/powerSurvEpi/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.5-1
- initial package for Fedora