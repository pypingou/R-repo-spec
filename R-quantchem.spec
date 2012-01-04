%global packname  quantchem
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.12.1
Release:          1%{?dist}
Summary:          Quantitative chemical analysis: calibration and evaluation of results

Group:            Applications/Engineering 
License:          GPL version 2 or newer. http://www.gnu.org/copyleft/gpl.html
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.12-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-outliers 

BuildRequires:    R-devel tex(latex) R-MASS R-outliers 

%description
Statistical evaluation of calibration curves by different regression
techniques: ordinary, weighted, robust (up to 4th order polynomial).
Log-log and Box-Cox transform, estimation of optimal power and weighting
scheme. Tests for heteroscedascity and normality of residuals. Different
kinds of plots commonly used in illustrating calibrations. Easy "inverse
prediction" of concentration by given responses and statistical evaluation
of results (comparison of precision and accuracy by common tests).

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
%doc %{rlibdir}/quantchem/html
%doc %{rlibdir}/quantchem/DESCRIPTION
%{rlibdir}/quantchem/data
%{rlibdir}/quantchem/help
%{rlibdir}/quantchem/Meta
%{rlibdir}/quantchem/INDEX
%{rlibdir}/quantchem/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.12.1-1
- initial package for Fedora